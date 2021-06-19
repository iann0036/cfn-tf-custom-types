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
    AddressCidrs: Optional[Sequence[str]]
    DeviceModel: Optional[str]
    DeviceVendor: Optional[str]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    VirtualWanId: Optional[str]
    Link: Optional[Sequence["_LinkDefinition"]]
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
            AddressCidrs=json_data.get("AddressCidrs"),
            DeviceModel=json_data.get("DeviceModel"),
            DeviceVendor=json_data.get("DeviceVendor"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            VirtualWanId=json_data.get("VirtualWanId"),
            Link=deserialize_list(json_data.get("Link"), LinkDefinition),
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
class LinkDefinition(BaseModel):
    Fqdn: Optional[str]
    IpAddress: Optional[str]
    Name: Optional[str]
    ProviderName: Optional[str]
    SpeedInMbps: Optional[float]
    Bgp: Optional[Sequence["_BgpDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LinkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LinkDefinition"]:
        if not json_data:
            return None
        return cls(
            Fqdn=json_data.get("Fqdn"),
            IpAddress=json_data.get("IpAddress"),
            Name=json_data.get("Name"),
            ProviderName=json_data.get("ProviderName"),
            SpeedInMbps=json_data.get("SpeedInMbps"),
            Bgp=deserialize_list(json_data.get("Bgp"), BgpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LinkDefinition = LinkDefinition


@dataclass
class BgpDefinition(BaseModel):
    Asn: Optional[float]
    PeeringAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BgpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BgpDefinition"]:
        if not json_data:
            return None
        return cls(
            Asn=json_data.get("Asn"),
            PeeringAddress=json_data.get("PeeringAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BgpDefinition = BgpDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


