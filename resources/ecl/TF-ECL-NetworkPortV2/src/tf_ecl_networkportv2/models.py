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
    AdminStateUp: Optional[bool]
    AllFixedIps: Optional[Sequence[str]]
    Description: Optional[str]
    DeviceId: Optional[str]
    DeviceOwner: Optional[str]
    Id: Optional[str]
    MacAddress: Optional[str]
    ManagedByService: Optional[bool]
    Name: Optional[str]
    NetworkId: Optional[str]
    NoFixedIp: Optional[bool]
    Region: Optional[str]
    SegmentationId: Optional[float]
    SegmentationType: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TenantId: Optional[str]
    AllowedAddressPairs: Optional[Sequence["_AllowedAddressPairsDefinition"]]
    FixedIp: Optional[Sequence["_FixedIpDefinition"]]
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
            AdminStateUp=json_data.get("AdminStateUp"),
            AllFixedIps=json_data.get("AllFixedIps"),
            Description=json_data.get("Description"),
            DeviceId=json_data.get("DeviceId"),
            DeviceOwner=json_data.get("DeviceOwner"),
            Id=json_data.get("Id"),
            MacAddress=json_data.get("MacAddress"),
            ManagedByService=json_data.get("ManagedByService"),
            Name=json_data.get("Name"),
            NetworkId=json_data.get("NetworkId"),
            NoFixedIp=json_data.get("NoFixedIp"),
            Region=json_data.get("Region"),
            SegmentationId=json_data.get("SegmentationId"),
            SegmentationType=json_data.get("SegmentationType"),
            Status=json_data.get("Status"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TenantId=json_data.get("TenantId"),
            AllowedAddressPairs=deserialize_list(json_data.get("AllowedAddressPairs"), AllowedAddressPairsDefinition),
            FixedIp=deserialize_list(json_data.get("FixedIp"), FixedIpDefinition),
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
class AllowedAddressPairsDefinition(BaseModel):
    IpAddress: Optional[str]
    MacAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AllowedAddressPairsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllowedAddressPairsDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
            MacAddress=json_data.get("MacAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllowedAddressPairsDefinition = AllowedAddressPairsDefinition


@dataclass
class FixedIpDefinition(BaseModel):
    IpAddress: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FixedIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FixedIpDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FixedIpDefinition = FixedIpDefinition


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


