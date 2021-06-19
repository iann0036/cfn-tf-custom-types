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
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    VpcId: Optional[str]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            VpcId=json_data.get("VpcId"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
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
class TimeoutsDefinition(BaseModel):
    Read: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Read=json_data.get("Read"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


