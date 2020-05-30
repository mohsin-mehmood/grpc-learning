# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MeterReader.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import enums_pb2 as enums__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='MeterReader.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\252\002\027MeterReaderWeb.Services',
  serialized_pb=b'\n\x11MeterReader.proto\x1a\x0b\x65nums.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"q\n\x14ReadingPacketMessage\x12&\n\x08readings\x18\x01 \x03(\x0b\x32\x14.MeterReadingMessage\x12\r\n\x05notes\x18\x02 \x01(\t\x12\"\n\nsuccessful\x18\x03 \x01(\x0e\x32\x0e.ReadingStatus\"\x88\x01\n\x13MeterReadingMessage\x12\x12\n\ncustomerId\x18\x01 \x01(\x05\x12\x14\n\x0creadingValue\x18\x02 \x01(\x05\x12/\n\x0breadingTime\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampJ\x04\x08\x03\x10\x04J\x04\x08\x04\x10\x05R\nsuccessful\"A\n\rStatusMessage\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x1f\n\x07success\x18\x02 \x01(\x0e\x32\x0e.ReadingStatus2J\n\x13MeterReadingService\x12\x33\n\nAddReading\x12\x15.ReadingPacketMessage\x1a\x0e.StatusMessageB\x1a\xaa\x02\x17MeterReaderWeb.Servicesb\x06proto3'
  ,
  dependencies=[enums__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_READINGPACKETMESSAGE = _descriptor.Descriptor(
  name='ReadingPacketMessage',
  full_name='ReadingPacketMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='readings', full_name='ReadingPacketMessage.readings', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='notes', full_name='ReadingPacketMessage.notes', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='successful', full_name='ReadingPacketMessage.successful', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=180,
)


_METERREADINGMESSAGE = _descriptor.Descriptor(
  name='MeterReadingMessage',
  full_name='MeterReadingMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customerId', full_name='MeterReadingMessage.customerId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readingValue', full_name='MeterReadingMessage.readingValue', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readingTime', full_name='MeterReadingMessage.readingTime', index=2,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=183,
  serialized_end=319,
)


_STATUSMESSAGE = _descriptor.Descriptor(
  name='StatusMessage',
  full_name='StatusMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='StatusMessage.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='success', full_name='StatusMessage.success', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=321,
  serialized_end=386,
)

_READINGPACKETMESSAGE.fields_by_name['readings'].message_type = _METERREADINGMESSAGE
_READINGPACKETMESSAGE.fields_by_name['successful'].enum_type = enums__pb2._READINGSTATUS
_METERREADINGMESSAGE.fields_by_name['readingTime'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_STATUSMESSAGE.fields_by_name['success'].enum_type = enums__pb2._READINGSTATUS
DESCRIPTOR.message_types_by_name['ReadingPacketMessage'] = _READINGPACKETMESSAGE
DESCRIPTOR.message_types_by_name['MeterReadingMessage'] = _METERREADINGMESSAGE
DESCRIPTOR.message_types_by_name['StatusMessage'] = _STATUSMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReadingPacketMessage = _reflection.GeneratedProtocolMessageType('ReadingPacketMessage', (_message.Message,), {
  'DESCRIPTOR' : _READINGPACKETMESSAGE,
  '__module__' : 'MeterReader_pb2'
  # @@protoc_insertion_point(class_scope:ReadingPacketMessage)
  })
_sym_db.RegisterMessage(ReadingPacketMessage)

MeterReadingMessage = _reflection.GeneratedProtocolMessageType('MeterReadingMessage', (_message.Message,), {
  'DESCRIPTOR' : _METERREADINGMESSAGE,
  '__module__' : 'MeterReader_pb2'
  # @@protoc_insertion_point(class_scope:MeterReadingMessage)
  })
_sym_db.RegisterMessage(MeterReadingMessage)

StatusMessage = _reflection.GeneratedProtocolMessageType('StatusMessage', (_message.Message,), {
  'DESCRIPTOR' : _STATUSMESSAGE,
  '__module__' : 'MeterReader_pb2'
  # @@protoc_insertion_point(class_scope:StatusMessage)
  })
_sym_db.RegisterMessage(StatusMessage)


DESCRIPTOR._options = None

_METERREADINGSERVICE = _descriptor.ServiceDescriptor(
  name='MeterReadingService',
  full_name='MeterReadingService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=388,
  serialized_end=462,
  methods=[
  _descriptor.MethodDescriptor(
    name='AddReading',
    full_name='MeterReadingService.AddReading',
    index=0,
    containing_service=None,
    input_type=_READINGPACKETMESSAGE,
    output_type=_STATUSMESSAGE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_METERREADINGSERVICE)

DESCRIPTOR.services_by_name['MeterReadingService'] = _METERREADINGSERVICE

# @@protoc_insertion_point(module_scope)
