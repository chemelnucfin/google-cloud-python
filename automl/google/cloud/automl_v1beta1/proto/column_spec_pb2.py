# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl_v1beta1/proto/column_spec.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.cloud.automl_v1beta1.proto import (
    data_stats_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_data__stats__pb2,
)
from google.cloud.automl_v1beta1.proto import (
    data_types_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_data__types__pb2,
)
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/automl_v1beta1/proto/column_spec.proto",
    package="google.cloud.automl.v1beta1",
    syntax="proto3",
    serialized_options=_b(
        "\n\037com.google.cloud.automl.v1beta1P\001ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\312\002\033Google\\Cloud\\AutoMl\\V1beta1\352\002\036Google::Cloud::AutoML::V1beta1"
    ),
    serialized_pb=_b(
        '\n3google/cloud/automl_v1beta1/proto/column_spec.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a\x32google/cloud/automl_v1beta1/proto/data_stats.proto\x1a\x32google/cloud/automl_v1beta1/proto/data_types.proto\x1a\x1cgoogle/api/annotations.proto"\x84\x03\n\nColumnSpec\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x38\n\tdata_type\x18\x02 \x01(\x0b\x32%.google.cloud.automl.v1beta1.DataType\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t\x12:\n\ndata_stats\x18\x04 \x01(\x0b\x32&.google.cloud.automl.v1beta1.DataStats\x12X\n\x16top_correlated_columns\x18\x05 \x03(\x0b\x32\x38.google.cloud.automl.v1beta1.ColumnSpec.CorrelatedColumn\x12\x0c\n\x04\x65tag\x18\x06 \x01(\t\x1at\n\x10\x43orrelatedColumn\x12\x16\n\x0e\x63olumn_spec_id\x18\x01 \x01(\t\x12H\n\x11\x63orrelation_stats\x18\x02 \x01(\x0b\x32-.google.cloud.automl.v1beta1.CorrelationStatsB\xa5\x01\n\x1f\x63om.google.cloud.automl.v1beta1P\x01ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3'
    ),
    dependencies=[
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_data__stats__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_data__types__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
    ],
)


_COLUMNSPEC_CORRELATEDCOLUMN = _descriptor.Descriptor(
    name="CorrelatedColumn",
    full_name="google.cloud.automl.v1beta1.ColumnSpec.CorrelatedColumn",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="column_spec_id",
            full_name="google.cloud.automl.v1beta1.ColumnSpec.CorrelatedColumn.column_spec_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="correlation_stats",
            full_name="google.cloud.automl.v1beta1.ColumnSpec.CorrelatedColumn.correlation_stats",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=491,
    serialized_end=607,
)

_COLUMNSPEC = _descriptor.Descriptor(
    name="ColumnSpec",
    full_name="google.cloud.automl.v1beta1.ColumnSpec",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.automl.v1beta1.ColumnSpec.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="data_type",
            full_name="google.cloud.automl.v1beta1.ColumnSpec.data_type",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="display_name",
            full_name="google.cloud.automl.v1beta1.ColumnSpec.display_name",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="data_stats",
            full_name="google.cloud.automl.v1beta1.ColumnSpec.data_stats",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="top_correlated_columns",
            full_name="google.cloud.automl.v1beta1.ColumnSpec.top_correlated_columns",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="etag",
            full_name="google.cloud.automl.v1beta1.ColumnSpec.etag",
            index=5,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_COLUMNSPEC_CORRELATEDCOLUMN],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=219,
    serialized_end=607,
)

_COLUMNSPEC_CORRELATEDCOLUMN.fields_by_name[
    "correlation_stats"
].message_type = (
    google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_data__stats__pb2._CORRELATIONSTATS
)
_COLUMNSPEC_CORRELATEDCOLUMN.containing_type = _COLUMNSPEC
_COLUMNSPEC.fields_by_name[
    "data_type"
].message_type = (
    google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_data__types__pb2._DATATYPE
)
_COLUMNSPEC.fields_by_name[
    "data_stats"
].message_type = (
    google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_data__stats__pb2._DATASTATS
)
_COLUMNSPEC.fields_by_name[
    "top_correlated_columns"
].message_type = _COLUMNSPEC_CORRELATEDCOLUMN
DESCRIPTOR.message_types_by_name["ColumnSpec"] = _COLUMNSPEC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ColumnSpec = _reflection.GeneratedProtocolMessageType(
    "ColumnSpec",
    (_message.Message,),
    dict(
        CorrelatedColumn=_reflection.GeneratedProtocolMessageType(
            "CorrelatedColumn",
            (_message.Message,),
            dict(
                DESCRIPTOR=_COLUMNSPEC_CORRELATEDCOLUMN,
                __module__="google.cloud.automl_v1beta1.proto.column_spec_pb2",
                __doc__="""Identifies the table's column, and its correlation with the column this
    ColumnSpec describes.
    
    
    Attributes:
        column_spec_id:
            The column\_spec\_id of the correlated column, which belongs
            to the same table as the in-context column.
        correlation_stats:
            Correlation between this and the in-context column.
    """,
                # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.ColumnSpec.CorrelatedColumn)
            ),
        ),
        DESCRIPTOR=_COLUMNSPEC,
        __module__="google.cloud.automl_v1beta1.proto.column_spec_pb2",
        __doc__="""A representation of a column in a relational table. When listing them,
  column specs are returned in the same order in which they were given on
  import . Used by: \* Tables
  
  
  Attributes:
      name:
          Output only. The resource name of the column specs. Form:  ``p
          rojects/{project_id}/locations/{location_id}/datasets/{dataset
          _id}/tableSpecs/{table_spec_id}/columnSpecs/{column_spec_id}``
      data_type:
          The data type of elements stored in the column.
      display_name:
          Output only. The name of the column to show in the interface.
          The name can be up to 100 characters long and can consist only
          of ASCII Latin letters A-Z and a-z, ASCII digits 0-9,
          underscores(\_), and forward slashes(/), and must start with a
          letter or a digit.
      data_stats:
          Output only. Stats of the series of values in the column. This
          field may be stale, see the ancestor's
          Dataset.tables\_dataset\_metadata.stats\_update\_time field
          for the timestamp at which these stats were last updated.
      top_correlated_columns:
          Deprecated.
      etag:
          Used to perform consistent read-modify-write updates. If not
          set, a blind "overwrite" update happens.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.ColumnSpec)
    ),
)
_sym_db.RegisterMessage(ColumnSpec)
_sym_db.RegisterMessage(ColumnSpec.CorrelatedColumn)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
