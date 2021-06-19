# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

from cloudformation_cli_python_lib.interface import (
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class ResourceHandlerRequest(BaseResourceHandlerRequest):
    # pylint: disable=invalid-name
    desiredResourceState: Optional["ResourceModel"]
    previousResourceState: Optional["ResourceModel"]


@dataclass
class ResourceModel(BaseModel):
    tfcfnid: Optional[str]
    Arn: Optional[str]
    BillingMode: Optional[str]
    HashKey: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    RangeKey: Optional[str]
    ReadCapacity: Optional[float]
    StreamArn: Optional[str]
    StreamEnabled: Optional[bool]
    StreamLabel: Optional[str]
    StreamViewType: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    WriteCapacity: Optional[float]
    Attribute: Optional[Sequence["_AttributeDefinition"]]
    GlobalSecondaryIndex: Optional[Sequence["_GlobalSecondaryIndexDefinition"]]
    LocalSecondaryIndex: Optional[Sequence["_LocalSecondaryIndexDefinition"]]
    PointInTimeRecovery: Optional[Sequence["_PointInTimeRecoveryDefinition"]]
    Replica: Optional[Sequence["_ReplicaDefinition"]]
    ServerSideEncryption: Optional[Sequence["_ServerSideEncryptionDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    Ttl: Optional[Sequence["_TtlDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            BillingMode=json_data.get("BillingMode"),
            HashKey=json_data.get("HashKey"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            RangeKey=json_data.get("RangeKey"),
            ReadCapacity=json_data.get("ReadCapacity"),
            StreamArn=json_data.get("StreamArn"),
            StreamEnabled=json_data.get("StreamEnabled"),
            StreamLabel=json_data.get("StreamLabel"),
            StreamViewType=json_data.get("StreamViewType"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            WriteCapacity=json_data.get("WriteCapacity"),
            Attribute=deserialize_list(json_data.get("Attribute"), AttributeDefinition),
            GlobalSecondaryIndex=deserialize_list(json_data.get("GlobalSecondaryIndex"), GlobalSecondaryIndexDefinition),
            LocalSecondaryIndex=deserialize_list(json_data.get("LocalSecondaryIndex"), LocalSecondaryIndexDefinition),
            PointInTimeRecovery=deserialize_list(json_data.get("PointInTimeRecovery"), PointInTimeRecoveryDefinition),
            Replica=deserialize_list(json_data.get("Replica"), ReplicaDefinition),
            ServerSideEncryption=deserialize_list(json_data.get("ServerSideEncryption"), ServerSideEncryptionDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            Ttl=deserialize_list(json_data.get("Ttl"), TtlDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class AttributeDefinition(BaseModel):
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AttributeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttributeDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttributeDefinition = AttributeDefinition


@dataclass
class GlobalSecondaryIndexDefinition(BaseModel):
    HashKey: Optional[str]
    Name: Optional[str]
    NonKeyAttributes: Optional[Sequence[str]]
    ProjectionType: Optional[str]
    RangeKey: Optional[str]
    ReadCapacity: Optional[float]
    WriteCapacity: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_GlobalSecondaryIndexDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GlobalSecondaryIndexDefinition"]:
        if not json_data:
            return None
        return cls(
            HashKey=json_data.get("HashKey"),
            Name=json_data.get("Name"),
            NonKeyAttributes=json_data.get("NonKeyAttributes"),
            ProjectionType=json_data.get("ProjectionType"),
            RangeKey=json_data.get("RangeKey"),
            ReadCapacity=json_data.get("ReadCapacity"),
            WriteCapacity=json_data.get("WriteCapacity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GlobalSecondaryIndexDefinition = GlobalSecondaryIndexDefinition


@dataclass
class LocalSecondaryIndexDefinition(BaseModel):
    Name: Optional[str]
    NonKeyAttributes: Optional[Sequence[str]]
    ProjectionType: Optional[str]
    RangeKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LocalSecondaryIndexDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocalSecondaryIndexDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            NonKeyAttributes=json_data.get("NonKeyAttributes"),
            ProjectionType=json_data.get("ProjectionType"),
            RangeKey=json_data.get("RangeKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocalSecondaryIndexDefinition = LocalSecondaryIndexDefinition


@dataclass
class PointInTimeRecoveryDefinition(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PointInTimeRecoveryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PointInTimeRecoveryDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PointInTimeRecoveryDefinition = PointInTimeRecoveryDefinition


@dataclass
class ReplicaDefinition(BaseModel):
    KmsKeyArn: Optional[str]
    RegionName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicaDefinition"]:
        if not json_data:
            return None
        return cls(
            KmsKeyArn=json_data.get("KmsKeyArn"),
            RegionName=json_data.get("RegionName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicaDefinition = ReplicaDefinition


@dataclass
class ServerSideEncryptionDefinition(BaseModel):
    Enabled: Optional[bool]
    KmsKeyArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerSideEncryptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerSideEncryptionDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerSideEncryptionDefinition = ServerSideEncryptionDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


@dataclass
class TtlDefinition(BaseModel):
    AttributeName: Optional[str]
    Enabled: Optional[bool]
    KmsKeyArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TtlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TtlDefinition"]:
        if not json_data:
            return None
        return cls(
            AttributeName=json_data.get("AttributeName"),
            Enabled=json_data.get("Enabled"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TtlDefinition = TtlDefinition


