import grpc
from google.protobuf.timestamp_pb2 import Timestamp

import enums_pb2 as Enums
import MeterReader_pb2 as MeterReader
import MeterReader_pb2_grpc as MeterReaderService


def main():

    with open("localhost.cer", "rb") as certFile:
        cert = certFile.read()

    credentials = grpc.ssl_channel_credentials(cert)

    channel = grpc.secure_channel("localhost:5001", credentials)
    stub = MeterReaderService.MeterReadingServiceStub(channel)

    now = Timestamp()
    now.GetCurrentTime()
    
    request = MeterReader.ReadingPacketMessage(successful = Enums.SUCCESS)
    reading = MeterReader.MeterReadingMessage(customerId = 1,
                                              readingValue = 1,
                                              readingTime = now)
    request.readings.append(reading)

    result = stub.AddReading(request)

    if(result.success == Enums.SUCCESS):
        print("Success")
    else:
        print("Failure")

main()