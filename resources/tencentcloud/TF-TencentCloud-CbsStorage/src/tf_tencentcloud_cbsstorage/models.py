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
    Attached: Optional[bool]
    AvailabilityZone: Optional[str]
    ChargeType: Optional[str]
    Encrypt: Optional[bool]
    ForceDelete: Optional[bool]
    Id: Optional[str]
    Period: Optional[float]
    PrepaidPeriod: Optional[float]
    PrepaidRenewFlag: Optional[str]
    ProjectId: Optional[float]
    SnapshotId: Optional[str]
    StorageName: Optional[str]
    StorageSize: Optional[float]
    StorageStatus: Optional[str]
    StorageType: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    ThroughputPerformance: Optional[float]

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
            Attached=json_data.get("Attached"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            ChargeType=json_data.get("ChargeType"),
            Encrypt=json_data.get("Encrypt"),
            ForceDelete=json_data.get("ForceDelete"),
            Id=json_data.get("Id"),
            Period=json_data.get("Period"),
            PrepaidPeriod=json_data.get("PrepaidPeriod"),
            PrepaidRenewFlag=json_data.get("PrepaidRenewFlag"),
            ProjectId=json_data.get("ProjectId"),
            SnapshotId=json_data.get("SnapshotId"),
            StorageName=json_data.get("StorageName"),
            StorageSize=json_data.get("StorageSize"),
            StorageStatus=json_data.get("StorageStatus"),
            StorageType=json_data.get("StorageType"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            ThroughputPerformance=json_data.get("ThroughputPerformance"),
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


