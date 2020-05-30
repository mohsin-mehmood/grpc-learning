# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import MeterReader_pb2 as MeterReader__pb2


class MeterReadingServiceStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddReading = channel.unary_unary(
                '/MeterReadingService/AddReading',
                request_serializer=MeterReader__pb2.ReadingPacketMessage.SerializeToString,
                response_deserializer=MeterReader__pb2.StatusMessage.FromString,
                )


class MeterReadingServiceServicer(object):
    """Missing associated documentation comment in .proto file"""

    def AddReading(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MeterReadingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddReading': grpc.unary_unary_rpc_method_handler(
                    servicer.AddReading,
                    request_deserializer=MeterReader__pb2.ReadingPacketMessage.FromString,
                    response_serializer=MeterReader__pb2.StatusMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'MeterReadingService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MeterReadingService(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def AddReading(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MeterReadingService/AddReading',
            MeterReader__pb2.ReadingPacketMessage.SerializeToString,
            MeterReader__pb2.StatusMessage.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
