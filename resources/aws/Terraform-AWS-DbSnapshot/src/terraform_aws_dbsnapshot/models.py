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
    AllocatedStorage: Optional[float]
    AvailabilityZone: Optional[str]
    DbInstanceIdentifier: Optional[str]
    DbSnapshotArn: Optional[str]
    DbSnapshotIdentifier: Optional[str]
    Encrypted: Optional[bool]
    Engine: Optional[str]
    EngineVersion: Optional[str]
    Id: Optional[str]
    Iops: Optional[float]
    KmsKeyId: Optional[str]
    LicenseModel: Optional[str]
    OptionGroupName: Optional[str]
    Port: Optional[float]
    SnapshotType: Optional[str]
    SourceDbSnapshotIdentifier: Optional[str]
    SourceRegion: Optional[str]
    Status: Optional[str]
    StorageType: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    VpcId: Optional[str]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AllocatedStorage=json_data.get("AllocatedStorage"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            DbInstanceIdentifier=json_data.get("DbInstanceIdentifier"),
            DbSnapshotArn=json_data.get("DbSnapshotArn"),
            DbSnapshotIdentifier=json_data.get("DbSnapshotIdentifier"),
            Encrypted=json_data.get("Encrypted"),
            Engine=json_data.get("Engine"),
            EngineVersion=json_data.get("EngineVersion"),
            Id=json_data.get("Id"),
            Iops=json_data.get("Iops"),
            KmsKeyId=json_data.get("KmsKeyId"),
            LicenseModel=json_data.get("LicenseModel"),
            OptionGroupName=json_data.get("OptionGroupName"),
            Port=json_data.get("Port"),
            SnapshotType=json_data.get("SnapshotType"),
            SourceDbSnapshotIdentifier=json_data.get("SourceDbSnapshotIdentifier"),
            SourceRegion=json_data.get("SourceRegion"),
            Status=json_data.get("Status"),
            StorageType=json_data.get("StorageType"),
            Tags=json_data.get("Tags"),
            VpcId=json_data.get("VpcId"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
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
class Timeouts:
    Read: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Read=json_data.get("Read"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts

