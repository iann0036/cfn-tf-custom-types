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
    AdvancedFeatures: Optional[str]
    AvailabilityZone: Optional[str]
    Category: Optional[str]
    DedicatedBlockStorageClusterId: Optional[str]
    DeleteAutoSnapshot: Optional[bool]
    DeleteWithInstance: Optional[bool]
    Description: Optional[str]
    DiskName: Optional[str]
    DryRun: Optional[bool]
    EnableAutoSnapshot: Optional[bool]
    EncryptAlgorithm: Optional[str]
    Encrypted: Optional[bool]
    Id: Optional[str]
    InstanceId: Optional[str]
    KmsKeyId: Optional[str]
    Name: Optional[str]
    PaymentType: Optional[str]
    PerformanceLevel: Optional[str]
    ResourceGroupId: Optional[str]
    Size: Optional[float]
    SnapshotId: Optional[str]
    Status: Optional[str]
    StorageSetId: Optional[str]
    StorageSetPartitionNumber: Optional[float]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Type: Optional[str]
    ZoneId: Optional[str]
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
            AdvancedFeatures=json_data.get("AdvancedFeatures"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            Category=json_data.get("Category"),
            DedicatedBlockStorageClusterId=json_data.get("DedicatedBlockStorageClusterId"),
            DeleteAutoSnapshot=json_data.get("DeleteAutoSnapshot"),
            DeleteWithInstance=json_data.get("DeleteWithInstance"),
            Description=json_data.get("Description"),
            DiskName=json_data.get("DiskName"),
            DryRun=json_data.get("DryRun"),
            EnableAutoSnapshot=json_data.get("EnableAutoSnapshot"),
            EncryptAlgorithm=json_data.get("EncryptAlgorithm"),
            Encrypted=json_data.get("Encrypted"),
            Id=json_data.get("Id"),
            InstanceId=json_data.get("InstanceId"),
            KmsKeyId=json_data.get("KmsKeyId"),
            Name=json_data.get("Name"),
            PaymentType=json_data.get("PaymentType"),
            PerformanceLevel=json_data.get("PerformanceLevel"),
            ResourceGroupId=json_data.get("ResourceGroupId"),
            Size=json_data.get("Size"),
            SnapshotId=json_data.get("SnapshotId"),
            Status=json_data.get("Status"),
            StorageSetId=json_data.get("StorageSetId"),
            StorageSetPartitionNumber=json_data.get("StorageSetPartitionNumber"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Type=json_data.get("Type"),
            ZoneId=json_data.get("ZoneId"),
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


