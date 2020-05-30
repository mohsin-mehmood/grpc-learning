using Google.Protobuf.WellKnownTypes;
using Grpc.Core;
using MeterReaderLib;
using MeterReaderWeb.Data;
using MeterReaderWeb.Data.Entities;
using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.AspNetCore.Authorization;
using Microsoft.Extensions.Logging;
using System;
using System.Linq;
using System.Threading.Tasks;

namespace MeterReaderWeb.Services
{
    [Authorize(AuthenticationSchemes = JwtBearerDefaults.AuthenticationScheme)]
    public class MeterService : MeterReadingService.MeterReadingServiceBase
    {
        private readonly ILogger<MeterService> _logger;
        private readonly IReadingRepository _readingRepository;
        private readonly JwtTokenValidationService _tokenService;



        public MeterService(ILogger<MeterService> logger, IReadingRepository readingRepository, JwtTokenValidationService tokenService)
        {
            _logger = logger;
            _readingRepository = readingRepository;
            _tokenService = tokenService;
        }

        [AllowAnonymous]
        public async override Task<TokenResponse> CreateToken(TokenRequest request, ServerCallContext context)
        {
            var response = await _tokenService.GenerateTokenModelAsync(new MeterReaderLib.Models.CredentialModel
            {
                UserName = request.Username,
                Passcode = request.Password
            });

            if (response.Success)
            {
                return new TokenResponse
                {
                    Success = response.Success,
                    Token = response.Token,
                    Expiration = Timestamp.FromDateTime(response.Expiration)
                };
            }

            return new TokenResponse
            {
                Success = false
            };
        }

        public async override Task<Empty> SendDiagnostics(IAsyncStreamReader<MeterReadingMessage> requestStream, ServerCallContext context)
        {

            var task = Task.Run(async () =>
            {
                await foreach (var reading in requestStream.ReadAllAsync())
                {
                    _logger.LogInformation($"Received reading {reading}");
                }
            });

            await task;

            return new Empty();
        }

        public async override Task<StatusMessage> AddReading(ReadingPacketMessage request, ServerCallContext context)
        {
            var result = new StatusMessage
            {
                Success = ReadingStatus.Failure
            };

            if (request.Successful == ReadingStatus.Success)
            {
                try
                {
                    foreach (var reading in request.Readings)
                    {

                        if (reading.ReadingValue < 1000)
                        {
                            _logger.LogDebug("Reading value below acceptable level");

                            var trailer = new Metadata()
                            {
                                { "ReadingValue", reading.ReadingValue.ToString() },
                                { "Message", "Reading Value Invalid" }
                            };

                            throw new RpcException(new Status(StatusCode.OutOfRange, "Value too low"), trailer);
                        }

                        var readingEntity = new MeterReading
                        {
                            CustomerId = reading.CustomerId,
                            Value = reading.ReadingValue,
                            ReadingDate = reading.ReadingTime.ToDateTime()
                        };

                        _readingRepository.AddEntity(readingEntity);
                    }

                    if (await _readingRepository.SaveAllAsync())
                    {
                        result.Success = ReadingStatus.Success;
                        _logger.LogInformation($"Added {request.Readings.Count} for {request.Readings.First().CustomerId}");
                    }
                }
                catch (RpcException)
                {
                    throw;
                }
                catch (Exception ex)
                {
                    _logger.LogError($"An error occurred while saving meter readings: {ex}");
                    throw new RpcException(Status.DefaultCancelled, "An error occurred while saving meter readings.");
                }
            }

            return result;
        }
    }
}
