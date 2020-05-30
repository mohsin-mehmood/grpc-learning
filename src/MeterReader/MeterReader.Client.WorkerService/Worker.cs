using Grpc.Core;
using Grpc.Net.Client;
using MeterReaderWeb.Services;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using System;
using System.Threading;
using System.Threading.Tasks;

namespace MeterReader.Client.WorkerService
{
    public class Worker : BackgroundService
    {
        private readonly ILogger<Worker> _logger;
        private readonly IConfiguration _config;
        private readonly ReadingFactory _factory;
        private readonly ILoggerFactory _loggerFactory;
        private MeterReadingService.MeterReadingServiceClient _client = null;

        private string _token;
        private DateTime _expiration = DateTime.MinValue;

        public Worker(ILogger<Worker> logger, IConfiguration config, ReadingFactory factory, ILoggerFactory loggerFactory)
        {
            _logger = logger;
            _config = config;
            _factory = factory;
            _loggerFactory = loggerFactory;
        }

        protected bool NeedsLogin() => string.IsNullOrWhiteSpace(_token) || _expiration > DateTime.UtcNow;

        protected MeterReadingService.MeterReadingServiceClient Client
        {
            get
            {
                if (_client == null)
                {
                    var channel = GrpcChannel.ForAddress(_config["Service:ServerUrl"], new GrpcChannelOptions
                    {
                        LoggerFactory = _loggerFactory
                    });

                    _client = new MeterReadingService.MeterReadingServiceClient(channel);
                }

                return _client;
            }
        }


        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            var counter = 0;
            var customerId = _config.GetValue<int>("Service:CustomerId");

            while (!stoppingToken.IsCancellationRequested)
            {
                _logger.LogInformation("Worker running at: {time}", DateTimeOffset.Now);


                counter++;

                //if (counter % 10 == 0)
                //{
                //    Console.WriteLine("Sending Diagnostics");
                //    var stream = Client.SendDiagnostics();

                //    for (var x = 0; x < 5; x++)
                //    {
                //        await stream.RequestStream.WriteAsync(await _factory.Generate(customerId));
                //    }

                //    await stream.RequestStream.CompleteAsync();
                //}



                var pkt = new ReadingPacketMessage
                {
                    Successful = ReadingStatus.Success,
                    Notes = "Test Notes"
                };

                for (var i = 0; i < 5; i++)
                {
                    pkt.Readings.Add(await _factory.Generate(customerId));
                }


                try
                {

                    if (!NeedsLogin() || await GenerateToken())
                    {

                        var authHeader = new Metadata();

                        authHeader.Add("Authorization", $"Bearer {_token}");

                        var result = await Client.AddReadingAsync(pkt, headers: authHeader);

                        if (result.Success == ReadingStatus.Success)
                        {
                            _logger.LogInformation("Successfully added new readings");
                        }
                        else
                        {
                            _logger.LogInformation("Error adding new readings");
                        }
                    }
                }
                catch (RpcException ex)
                {
                    if (ex.StatusCode == StatusCode.OutOfRange)
                    {
                        _logger.LogInformation($"{ex.Trailers}");
                    }
                }

                await Task.Delay(_config.GetValue<int>("Service:DelayInterval"), stoppingToken);
            }
        }

        private async Task<bool> GenerateToken()
        {
            var tokenRequest = new TokenRequest
            {
                Username = _config.GetValue<string>("Service:Username"),
                Password = _config.GetValue<string>("Service:Password")
            };

            var tokenResponse = await Client.CreateTokenAsync(tokenRequest);

            if (tokenResponse.Success)
            {
                _token = tokenResponse.Token;
                _expiration = tokenResponse.Expiration.ToDateTime();
            }

            return tokenResponse.Success;
        }
    }
}
