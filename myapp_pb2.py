# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: myapp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bmyapp.proto\x12\x05myapp\"2\n\x07Product\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05price\x18\x03 \x01(\x02\x32\xa0\x01\n\x0eProductService\x12,\n\nAddProduct\x12\x0e.myapp.Product\x1a\x0e.myapp.Product\x12/\n\rDeleteProduct\x12\x0e.myapp.Product\x1a\x0e.myapp.Product\x12/\n\rUpdateProduct\x12\x0e.myapp.Product\x1a\x0e.myapp.Productb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'myapp_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_PRODUCT']._serialized_start=22
  _globals['_PRODUCT']._serialized_end=72
  _globals['_PRODUCTSERVICE']._serialized_start=75
  _globals['_PRODUCTSERVICE']._serialized_end=235
# @@protoc_insertion_point(module_scope)
