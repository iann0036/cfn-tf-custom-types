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
    Address: Optional[str]
    AddressIpVersion: Optional[str]
    AddressType: Optional[str]
    Bandwidth: Optional[float]
    DeleteProtection: Optional[str]
    Id: Optional[str]
    InstanceChargeType: Optional[str]
    Internet: Optional[bool]
    InternetChargeType: Optional[str]
    LoadBalancerName: Optional[str]
    LoadBalancerSpec: Optional[str]
    MasterZoneId: Optional[str]
    ModificationProtectionReason: Optional[str]
    ModificationProtectionStatus: Optional[str]
    Name: Optional[str]
    PaymentType: Optional[str]
    Period: Optional[float]
    ResourceGroupId: Optional[str]
    SlaveZoneId: Optional[str]
    Specification: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    VswitchId: Optional[str]
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
            Address=json_data.get("Address"),
            AddressIpVersion=json_data.get("AddressIpVersion"),
            AddressType=json_data.get("AddressType"),
            Bandwidth=json_data.get("Bandwidth"),
            DeleteProtection=json_data.get("DeleteProtection"),
            Id=json_data.get("Id"),
            InstanceChargeType=json_data.get("InstanceChargeType"),
            Internet=json_data.get("Internet"),
            InternetChargeType=json_data.get("InternetChargeType"),
            LoadBalancerName=json_data.get("LoadBalancerName"),
            LoadBalancerSpec=json_data.get("LoadBalancerSpec"),
            MasterZoneId=json_data.get("MasterZoneId"),
            ModificationProtectionReason=json_data.get("ModificationProtectionReason"),
            ModificationProtectionStatus=json_data.get("ModificationProtectionStatus"),
            Name=json_data.get("Name"),
            PaymentType=json_data.get("PaymentType"),
            Period=json_data.get("Period"),
            ResourceGroupId=json_data.get("ResourceGroupId"),
            SlaveZoneId=json_data.get("SlaveZoneId"),
            Specification=json_data.get("Specification"),
            Status=json_data.get("Status"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            VswitchId=json_data.get("VswitchId"),
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
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


