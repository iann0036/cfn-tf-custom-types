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
    ActionOnMaintenance: Optional[str]
    AutoPlacement: Optional[str]
    AutoReleaseTime: Optional[str]
    AutoRenew: Optional[bool]
    AutoRenewPeriod: Optional[float]
    CpuOverCommitRatio: Optional[float]
    DedicatedHostClusterId: Optional[str]
    DedicatedHostName: Optional[str]
    DedicatedHostType: Optional[str]
    Description: Optional[str]
    DetailFee: Optional[bool]
    DryRun: Optional[bool]
    ExpiredTime: Optional[str]
    Id: Optional[str]
    MinQuantity: Optional[float]
    PaymentType: Optional[str]
    ResourceGroupId: Optional[str]
    SaleCycle: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    ZoneId: Optional[str]
    NetworkAttributes: Optional[Sequence["_NetworkAttributesDefinition"]]
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
            ActionOnMaintenance=json_data.get("ActionOnMaintenance"),
            AutoPlacement=json_data.get("AutoPlacement"),
            AutoReleaseTime=json_data.get("AutoReleaseTime"),
            AutoRenew=json_data.get("AutoRenew"),
            AutoRenewPeriod=json_data.get("AutoRenewPeriod"),
            CpuOverCommitRatio=json_data.get("CpuOverCommitRatio"),
            DedicatedHostClusterId=json_data.get("DedicatedHostClusterId"),
            DedicatedHostName=json_data.get("DedicatedHostName"),
            DedicatedHostType=json_data.get("DedicatedHostType"),
            Description=json_data.get("Description"),
            DetailFee=json_data.get("DetailFee"),
            DryRun=json_data.get("DryRun"),
            ExpiredTime=json_data.get("ExpiredTime"),
            Id=json_data.get("Id"),
            MinQuantity=json_data.get("MinQuantity"),
            PaymentType=json_data.get("PaymentType"),
            ResourceGroupId=json_data.get("ResourceGroupId"),
            SaleCycle=json_data.get("SaleCycle"),
            Status=json_data.get("Status"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            ZoneId=json_data.get("ZoneId"),
            NetworkAttributes=deserialize_list(json_data.get("NetworkAttributes"), NetworkAttributesDefinition),
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
class NetworkAttributesDefinition(BaseModel):
    SlbUdpTimeout: Optional[float]
    UdpTimeout: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkAttributesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkAttributesDefinition"]:
        if not json_data:
            return None
        return cls(
            SlbUdpTimeout=json_data.get("SlbUdpTimeout"),
            UdpTimeout=json_data.get("UdpTimeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkAttributesDefinition = NetworkAttributesDefinition


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


