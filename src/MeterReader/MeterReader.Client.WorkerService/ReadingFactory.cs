using Google.Protobuf.WellKnownTypes;
using MeterReaderWeb.Services;
using Microsoft.Extensions.Logging;
using System;
using System.Threading.Tasks;

namespace MeterReader.Client.WorkerService
{
    public class ReadingFactory
    {
        private readonly ILogger<ReadingFactory> _logger;

        public ReadingFactory(ILogger<ReadingFactory> logger)
        {
            _logger = logger;
        }

        public Task<MeterReadingMessage> Generate(int customerId)
        {
            var reading = new MeterReadingMessage
            {
                CustomerId = customerId,
                ReadingTime = Timestamp.FromDateTime(DateTime.UtcNow),
                ReadingValue = new Random().Next(10000)
            };

            return Task.FromResult(reading);
        }

    }
}
