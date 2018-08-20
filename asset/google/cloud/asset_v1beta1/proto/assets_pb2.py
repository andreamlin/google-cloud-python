# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/asset_v1beta1/proto/assets.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/asset_v1beta1/proto/assets.proto',
  package='google.cloud.asset.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n-google/cloud/asset_v1beta1/proto/assets.proto\x12\x1agoogle.cloud.asset.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x8a\x01\n\rTemporalAsset\x12\x36\n\x06window\x18\x01 \x01(\x0b\x32&.google.cloud.asset.v1beta1.TimeWindow\x12\x0f\n\x07\x64\x65leted\x18\x02 \x01(\x08\x12\x30\n\x05\x61sset\x18\x03 \x01(\x0b\x32!.google.cloud.asset.v1beta1.Asset\"j\n\nTimeWindow\x12.\n\nstart_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x8c\x01\n\x05\x41sset\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nasset_type\x18\x02 \x01(\t\x12\x36\n\x08resource\x18\x03 \x01(\x0b\x32$.google.cloud.asset.v1beta1.Resource\x12)\n\niam_policy\x18\x04 \x01(\x0b\x32\x15.google.iam.v1.Policy\"\xa0\x01\n\x08Resource\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x1e\n\x16\x64iscovery_document_uri\x18\x02 \x01(\t\x12\x16\n\x0e\x64iscovery_name\x18\x03 \x01(\t\x12\x14\n\x0cresource_url\x18\x04 \x01(\t\x12\x0e\n\x06parent\x18\x05 \x01(\t\x12%\n\x04\x64\x61ta\x18\x06 \x01(\x0b\x32\x17.google.protobuf.StructB\xa9\x01\n\x1e\x63om.google.cloud.asset.v1beta1B\nAssetProtoP\x01Z?google.golang.org/genproto/googleapis/cloud/asset/v1beta1;asset\xaa\x02\x1aGoogle.Cloud.Asset.V1Beta1\xca\x02\x1aGoogle\\Cloud\\Asset\\V1beta1b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_iam_dot_v1_dot_policy__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_TEMPORALASSET = _descriptor.Descriptor(
  name='TemporalAsset',
  full_name='google.cloud.asset.v1beta1.TemporalAsset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='window', full_name='google.cloud.asset.v1beta1.TemporalAsset.window', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deleted', full_name='google.cloud.asset.v1beta1.TemporalAsset.deleted', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='asset', full_name='google.cloud.asset.v1beta1.TemporalAsset.asset', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=226,
  serialized_end=364,
)


_TIMEWINDOW = _descriptor.Descriptor(
  name='TimeWindow',
  full_name='google.cloud.asset.v1beta1.TimeWindow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_time', full_name='google.cloud.asset.v1beta1.TimeWindow.start_time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='google.cloud.asset.v1beta1.TimeWindow.end_time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=366,
  serialized_end=472,
)


_ASSET = _descriptor.Descriptor(
  name='Asset',
  full_name='google.cloud.asset.v1beta1.Asset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.asset.v1beta1.Asset.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='asset_type', full_name='google.cloud.asset.v1beta1.Asset.asset_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resource', full_name='google.cloud.asset.v1beta1.Asset.resource', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iam_policy', full_name='google.cloud.asset.v1beta1.Asset.iam_policy', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=475,
  serialized_end=615,
)


_RESOURCE = _descriptor.Descriptor(
  name='Resource',
  full_name='google.cloud.asset.v1beta1.Resource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='google.cloud.asset.v1beta1.Resource.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='discovery_document_uri', full_name='google.cloud.asset.v1beta1.Resource.discovery_document_uri', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='discovery_name', full_name='google.cloud.asset.v1beta1.Resource.discovery_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resource_url', full_name='google.cloud.asset.v1beta1.Resource.resource_url', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.asset.v1beta1.Resource.parent', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='google.cloud.asset.v1beta1.Resource.data', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=618,
  serialized_end=778,
)

_TEMPORALASSET.fields_by_name['window'].message_type = _TIMEWINDOW
_TEMPORALASSET.fields_by_name['asset'].message_type = _ASSET
_TIMEWINDOW.fields_by_name['start_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TIMEWINDOW.fields_by_name['end_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ASSET.fields_by_name['resource'].message_type = _RESOURCE
_ASSET.fields_by_name['iam_policy'].message_type = google_dot_iam_dot_v1_dot_policy__pb2._POLICY
_RESOURCE.fields_by_name['data'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['TemporalAsset'] = _TEMPORALASSET
DESCRIPTOR.message_types_by_name['TimeWindow'] = _TIMEWINDOW
DESCRIPTOR.message_types_by_name['Asset'] = _ASSET
DESCRIPTOR.message_types_by_name['Resource'] = _RESOURCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TemporalAsset = _reflection.GeneratedProtocolMessageType('TemporalAsset', (_message.Message,), dict(
  DESCRIPTOR = _TEMPORALASSET,
  __module__ = 'google.cloud.asset_v1beta1.proto.assets_pb2'
  ,
  __doc__ = """Temporal asset. In addition to the asset, the temporal asset includes
  the status of the asset and valid from and to time of it.
  
  
  Attributes:
      window:
          The time window when the asset data and state was observed.
      deleted:
          If the asset is deleted or not.
      asset:
          Asset.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.asset.v1beta1.TemporalAsset)
  ))
_sym_db.RegisterMessage(TemporalAsset)

TimeWindow = _reflection.GeneratedProtocolMessageType('TimeWindow', (_message.Message,), dict(
  DESCRIPTOR = _TIMEWINDOW,
  __module__ = 'google.cloud.asset_v1beta1.proto.assets_pb2'
  ,
  __doc__ = """A time window of [start\_time, end\_time).
  
  
  Attributes:
      start_time:
          Start time of the time window (inclusive). Infinite past if
          not specified.
      end_time:
          End time of the time window (exclusive). Infinite future if
          not specified.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.asset.v1beta1.TimeWindow)
  ))
_sym_db.RegisterMessage(TimeWindow)

Asset = _reflection.GeneratedProtocolMessageType('Asset', (_message.Message,), dict(
  DESCRIPTOR = _ASSET,
  __module__ = 'google.cloud.asset_v1beta1.proto.assets_pb2'
  ,
  __doc__ = """Cloud asset. This include all Google Cloud Platform resources, as well
  as IAM policies and other non-GCP assets.
  
  
  Attributes:
      name:
          The full name of the asset. See: https://cloud.google.com/apis
          /design/resource\_names#full\_resource\_name Example: "//compu
          te.googleapis.com/projects/my\_project\_123/zones/zone1/instan
          ces/instance1".
      asset_type:
          Type of the asset. Example: "google.compute.disk".
      resource:
          Representation of the resource.
      iam_policy:
          Representation of the actual IAM policy set on a cloud
          resource. For each resource, there must be at most one IAM
          policy set on it.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.asset.v1beta1.Asset)
  ))
_sym_db.RegisterMessage(Asset)

Resource = _reflection.GeneratedProtocolMessageType('Resource', (_message.Message,), dict(
  DESCRIPTOR = _RESOURCE,
  __module__ = 'google.cloud.asset_v1beta1.proto.assets_pb2'
  ,
  __doc__ = """Representation of a cloud resource.
  
  
  Attributes:
      version:
          The API version. Example: "v1".
      discovery_document_uri:
          The URL of the discovery document containing the resource's
          JSON schema. Example: "https://www.googleapis.com/discovery/v1
          /apis/compute/v1/rest". It will be left unspecified for
          resources without a discovery-based API, such as Cloud
          Bigtable.
      discovery_name:
          The JSON schema name listed in the discovery document.
          Example: "Project". It will be left unspecified for resources
          (such as Cloud Bigtable) without a discovery-based API.
      resource_url:
          The REST URL for accessing the resource. An HTTP GET operation
          using this URL returns the resource itself. Example:
          ``https://cloudresourcemanager.googleapis.com/v1/projects/my-
          project-123``. It will be left unspecified for resources
          without a REST API.
      parent:
          The full name of the immediate parent of this resource. See: h
          ttps://cloud.google.com/apis/design/resource\_names#full\_reso
          urce\_name  For GCP assets, it is the parent resource defined
          in the IAM policy hierarchy:
          https://cloud.google.com/iam/docs/overview#policy\_hierarchy.
          Example: "//cloudresourcemanager.googleapis.com/projects/my\_p
          roject\_123".  For third-party assets, it is up to the users
          to define.
      data:
          The content of the resource, in which some sensitive fields
          are scrubbed away and may not be present.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.asset.v1beta1.Resource)
  ))
_sym_db.RegisterMessage(Resource)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\036com.google.cloud.asset.v1beta1B\nAssetProtoP\001Z?google.golang.org/genproto/googleapis/cloud/asset/v1beta1;asset\252\002\032Google.Cloud.Asset.V1Beta1\312\002\032Google\\Cloud\\Asset\\V1beta1'))
# @@protoc_insertion_point(module_scope)
