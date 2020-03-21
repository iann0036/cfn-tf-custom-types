# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
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
    Tags: Optional[Sequence["_Tags"]]
    WriteCapacity: Optional[float]
    Attribute: Optional[Sequence["_Attribute"]]
    GlobalSecondaryIndex: Optional[Sequence["_GlobalSecondaryIndex"]]
    LocalSecondaryIndex: Optional[Sequence["_LocalSecondaryIndex"]]
    PointInTimeRecovery: Optional[Sequence["_PointInTimeRecovery"]]
    ServerSideEncryption: Optional[Sequence["_ServerSideEncryption"]]
    Timeouts: Optional["_Timeouts"]
    Ttl: Optional[Sequence["_Ttl"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
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
            Tags=json_data.get("Tags"),
            WriteCapacity=json_data.get("WriteCapacity"),
            Attribute=json_data.get("Attribute"),
            GlobalSecondaryIndex=json_data.get("GlobalSecondaryIndex"),
            LocalSecondaryIndex=json_data.get("LocalSecondaryIndex"),
            PointInTimeRecovery=json_data.get("PointInTimeRecovery"),
            ServerSideEncryption=json_data.get("ServerSideEncryption"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Ttl=json_data.get("Ttl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Attribute:
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Attribute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Attribute"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Attribute = Attribute


@dataclass
class GlobalSecondaryIndex:
    HashKey: Optional[str]
    Name: Optional[str]
    NonKeyAttributes: Optional[Sequence[str]]
    ProjectionType: Optional[str]
    RangeKey: Optional[str]
    ReadCapacity: Optional[float]
    WriteCapacity: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_GlobalSecondaryIndex"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GlobalSecondaryIndex"]:
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
_GlobalSecondaryIndex = GlobalSecondaryIndex


@dataclass
class LocalSecondaryIndex:
    Name: Optional[str]
    NonKeyAttributes: Optional[Sequence[str]]
    ProjectionType: Optional[str]
    RangeKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LocalSecondaryIndex"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocalSecondaryIndex"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            NonKeyAttributes=json_data.get("NonKeyAttributes"),
            ProjectionType=json_data.get("ProjectionType"),
            RangeKey=json_data.get("RangeKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocalSecondaryIndex = LocalSecondaryIndex


@dataclass
class PointInTimeRecovery:
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PointInTimeRecovery"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PointInTimeRecovery"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PointInTimeRecovery = PointInTimeRecovery


@dataclass
class ServerSideEncryption:
    Enabled: Optional[bool]
    KmsKeyArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerSideEncryption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerSideEncryption"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerSideEncryption = ServerSideEncryption


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


@dataclass
class Ttl:
    AttributeName: Optional[str]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Ttl"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ttl"]:
        if not json_data:
            return None
        return cls(
            AttributeName=json_data.get("AttributeName"),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ttl = Ttl


