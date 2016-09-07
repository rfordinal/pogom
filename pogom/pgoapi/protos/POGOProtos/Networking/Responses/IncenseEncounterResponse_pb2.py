# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Networking/Responses/IncenseEncounterResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos.Data.Capture import CaptureProbability_pb2 as POGOProtos_dot_Data_dot_Capture_dot_CaptureProbability__pb2
from POGOProtos.Data import PokemonData_pb2 as POGOProtos_dot_Data_dot_PokemonData__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Networking/Responses/IncenseEncounterResponse.proto',
  package='POGOProtos.Networking.Responses',
  syntax='proto3',
  serialized_pb=_b('\n>POGOProtos/Networking/Responses/IncenseEncounterResponse.proto\x12\x1fPOGOProtos.Networking.Responses\x1a\x30POGOProtos/Data/Capture/CaptureProbability.proto\x1a!POGOProtos/Data/PokemonData.proto\"\xf4\x02\n\x18IncenseEncounterResponse\x12P\n\x06result\x18\x01 \x01(\x0e\x32@.POGOProtos.Networking.Responses.IncenseEncounterResponse.Result\x12\x32\n\x0cpokemon_data\x18\x02 \x01(\x0b\x32\x1c.POGOProtos.Data.PokemonData\x12H\n\x13\x63\x61pture_probability\x18\x03 \x01(\x0b\x32+.POGOProtos.Data.Capture.CaptureProbability\"\x87\x01\n\x06Result\x12\x1d\n\x19INCENSE_ENCOUNTER_UNKNOWN\x10\x00\x12\x1d\n\x19INCENSE_ENCOUNTER_SUCCESS\x10\x01\x12#\n\x1fINCENSE_ENCOUNTER_NOT_AVAILABLE\x10\x02\x12\x1a\n\x16POKEMON_INVENTORY_FULL\x10\x03\x62\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Data_dot_Capture_dot_CaptureProbability__pb2.DESCRIPTOR,POGOProtos_dot_Data_dot_PokemonData__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_INCENSEENCOUNTERRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='POGOProtos.Networking.Responses.IncenseEncounterResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INCENSE_ENCOUNTER_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCENSE_ENCOUNTER_SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCENSE_ENCOUNTER_NOT_AVAILABLE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_INVENTORY_FULL', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=422,
  serialized_end=557,
)
_sym_db.RegisterEnumDescriptor(_INCENSEENCOUNTERRESPONSE_RESULT)


_INCENSEENCOUNTERRESPONSE = _descriptor.Descriptor(
  name='IncenseEncounterResponse',
  full_name='POGOProtos.Networking.Responses.IncenseEncounterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='POGOProtos.Networking.Responses.IncenseEncounterResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_data', full_name='POGOProtos.Networking.Responses.IncenseEncounterResponse.pokemon_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='capture_probability', full_name='POGOProtos.Networking.Responses.IncenseEncounterResponse.capture_probability', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _INCENSEENCOUNTERRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=185,
  serialized_end=557,
)

_INCENSEENCOUNTERRESPONSE.fields_by_name['result'].enum_type = _INCENSEENCOUNTERRESPONSE_RESULT
_INCENSEENCOUNTERRESPONSE.fields_by_name['pokemon_data'].message_type = POGOProtos_dot_Data_dot_PokemonData__pb2._POKEMONDATA
_INCENSEENCOUNTERRESPONSE.fields_by_name['capture_probability'].message_type = POGOProtos_dot_Data_dot_Capture_dot_CaptureProbability__pb2._CAPTUREPROBABILITY
_INCENSEENCOUNTERRESPONSE_RESULT.containing_type = _INCENSEENCOUNTERRESPONSE
DESCRIPTOR.message_types_by_name['IncenseEncounterResponse'] = _INCENSEENCOUNTERRESPONSE

IncenseEncounterResponse = _reflection.GeneratedProtocolMessageType('IncenseEncounterResponse', (_message.Message,), dict(
  DESCRIPTOR = _INCENSEENCOUNTERRESPONSE,
  __module__ = 'POGOProtos.Networking.Responses.IncenseEncounterResponse_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Responses.IncenseEncounterResponse)
  ))
_sym_db.RegisterMessage(IncenseEncounterResponse)


# @@protoc_insertion_point(module_scope)
