# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: file_system.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='file_system.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11\x66ile_system.proto\"\x15\n\x04Path\x12\r\n\x05value\x18\x01 \x01(\t\"\x1b\n\tPathFiles\x12\x0e\n\x06values\x18\x02 \x03(\t\"P\n\x12ReadFileParameters\x12\x16\n\x0enombre_archivo\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x05\x12\x12\n\ncant_bytes\x18\x03 \x01(\x05\"\"\n\rResultadoOpen\x12\x11\n\trespuesta\x18\x01 \x01(\t\" \n\x0bResultadoRF\x12\x11\n\tcontenido\x18\x01 \x01(\x0c\"#\n\x0eResultadoClose\x12\x11\n\trespuesta\x18\x01 \x01(\t2\xa3\x01\n\x02\x46S\x12 \n\tListFiles\x12\x05.Path\x1a\n.PathFiles\"\x00\x12#\n\x08OpenFile\x12\x05.Path\x1a\x0e.ResultadoOpen\"\x00\x12/\n\x08ReadFile\x12\x13.ReadFileParameters\x1a\x0c.ResultadoRF\"\x00\x12%\n\tCloseFile\x12\x05.Path\x1a\x0f.ResultadoClose\"\x00\x62\x06proto3'
)




_PATH = _descriptor.Descriptor(
  name='Path',
  full_name='Path',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='Path.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=21,
  serialized_end=42,
)


_PATHFILES = _descriptor.Descriptor(
  name='PathFiles',
  full_name='PathFiles',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='PathFiles.values', index=0,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=44,
  serialized_end=71,
)


_READFILEPARAMETERS = _descriptor.Descriptor(
  name='ReadFileParameters',
  full_name='ReadFileParameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nombre_archivo', full_name='ReadFileParameters.nombre_archivo', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='offset', full_name='ReadFileParameters.offset', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cant_bytes', full_name='ReadFileParameters.cant_bytes', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=73,
  serialized_end=153,
)


_RESULTADOOPEN = _descriptor.Descriptor(
  name='ResultadoOpen',
  full_name='ResultadoOpen',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='respuesta', full_name='ResultadoOpen.respuesta', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=155,
  serialized_end=189,
)


_RESULTADORF = _descriptor.Descriptor(
  name='ResultadoRF',
  full_name='ResultadoRF',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='contenido', full_name='ResultadoRF.contenido', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=191,
  serialized_end=223,
)


_RESULTADOCLOSE = _descriptor.Descriptor(
  name='ResultadoClose',
  full_name='ResultadoClose',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='respuesta', full_name='ResultadoClose.respuesta', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=225,
  serialized_end=260,
)

DESCRIPTOR.message_types_by_name['Path'] = _PATH
DESCRIPTOR.message_types_by_name['PathFiles'] = _PATHFILES
DESCRIPTOR.message_types_by_name['ReadFileParameters'] = _READFILEPARAMETERS
DESCRIPTOR.message_types_by_name['ResultadoOpen'] = _RESULTADOOPEN
DESCRIPTOR.message_types_by_name['ResultadoRF'] = _RESULTADORF
DESCRIPTOR.message_types_by_name['ResultadoClose'] = _RESULTADOCLOSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Path = _reflection.GeneratedProtocolMessageType('Path', (_message.Message,), {
  'DESCRIPTOR' : _PATH,
  '__module__' : 'file_system_pb2'
  # @@protoc_insertion_point(class_scope:Path)
  })
_sym_db.RegisterMessage(Path)

PathFiles = _reflection.GeneratedProtocolMessageType('PathFiles', (_message.Message,), {
  'DESCRIPTOR' : _PATHFILES,
  '__module__' : 'file_system_pb2'
  # @@protoc_insertion_point(class_scope:PathFiles)
  })
_sym_db.RegisterMessage(PathFiles)

ReadFileParameters = _reflection.GeneratedProtocolMessageType('ReadFileParameters', (_message.Message,), {
  'DESCRIPTOR' : _READFILEPARAMETERS,
  '__module__' : 'file_system_pb2'
  # @@protoc_insertion_point(class_scope:ReadFileParameters)
  })
_sym_db.RegisterMessage(ReadFileParameters)

ResultadoOpen = _reflection.GeneratedProtocolMessageType('ResultadoOpen', (_message.Message,), {
  'DESCRIPTOR' : _RESULTADOOPEN,
  '__module__' : 'file_system_pb2'
  # @@protoc_insertion_point(class_scope:ResultadoOpen)
  })
_sym_db.RegisterMessage(ResultadoOpen)

ResultadoRF = _reflection.GeneratedProtocolMessageType('ResultadoRF', (_message.Message,), {
  'DESCRIPTOR' : _RESULTADORF,
  '__module__' : 'file_system_pb2'
  # @@protoc_insertion_point(class_scope:ResultadoRF)
  })
_sym_db.RegisterMessage(ResultadoRF)

ResultadoClose = _reflection.GeneratedProtocolMessageType('ResultadoClose', (_message.Message,), {
  'DESCRIPTOR' : _RESULTADOCLOSE,
  '__module__' : 'file_system_pb2'
  # @@protoc_insertion_point(class_scope:ResultadoClose)
  })
_sym_db.RegisterMessage(ResultadoClose)



_FS = _descriptor.ServiceDescriptor(
  name='FS',
  full_name='FS',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=263,
  serialized_end=426,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListFiles',
    full_name='FS.ListFiles',
    index=0,
    containing_service=None,
    input_type=_PATH,
    output_type=_PATHFILES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='OpenFile',
    full_name='FS.OpenFile',
    index=1,
    containing_service=None,
    input_type=_PATH,
    output_type=_RESULTADOOPEN,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReadFile',
    full_name='FS.ReadFile',
    index=2,
    containing_service=None,
    input_type=_READFILEPARAMETERS,
    output_type=_RESULTADORF,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CloseFile',
    full_name='FS.CloseFile',
    index=3,
    containing_service=None,
    input_type=_PATH,
    output_type=_RESULTADOCLOSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FS)

DESCRIPTOR.services_by_name['FS'] = _FS

# @@protoc_insertion_point(module_scope)
