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
    DnsServers: Optional[Sequence[str]]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    ScaleUnit: Optional[float]
    Tags: Optional[Sequence["_TagsDefinition"]]
    VirtualHubId: Optional[str]
    VpnServerConfigurationId: Optional[str]
    ConnectionConfiguration: Optional[Sequence["_ConnectionConfigurationDefinition"]]
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
            DnsServers=json_data.get("DnsServers"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            ScaleUnit=json_data.get("ScaleUnit"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            VirtualHubId=json_data.get("VirtualHubId"),
            VpnServerConfigurationId=json_data.get("VpnServerConfigurationId"),
            ConnectionConfiguration=deserialize_list(json_data.get("ConnectionConfiguration"), ConnectionConfigurationDefinition),
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
class ConnectionConfigurationDefinition(BaseModel):
    Name: Optional[str]
    Route: Optional[Sequence["_RouteDefinition"]]
    VpnClientAddressPool: Optional[Sequence["_VpnClientAddressPoolDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Route=deserialize_list(json_data.get("Route"), RouteDefinition),
            VpnClientAddressPool=deserialize_list(json_data.get("VpnClientAddressPool"), VpnClientAddressPoolDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionConfigurationDefinition = ConnectionConfigurationDefinition


@dataclass
class RouteDefinition(BaseModel):
    AssociatedRouteTableId: Optional[str]
    PropagatedRouteTable: Optional[Sequence["_PropagatedRouteTableDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RouteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RouteDefinition"]:
        if not json_data:
            return None
        return cls(
            AssociatedRouteTableId=json_data.get("AssociatedRouteTableId"),
            PropagatedRouteTable=deserialize_list(json_data.get("PropagatedRouteTable"), PropagatedRouteTableDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RouteDefinition = RouteDefinition


@dataclass
class PropagatedRouteTableDefinition(BaseModel):
    Ids: Optional[Sequence[str]]
    Labels: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PropagatedRouteTableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropagatedRouteTableDefinition"]:
        if not json_data:
            return None
        return cls(
            Ids=json_data.get("Ids"),
            Labels=json_data.get("Labels"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropagatedRouteTableDefinition = PropagatedRouteTableDefinition


@dataclass
class VpnClientAddressPoolDefinition(BaseModel):
    AddressPrefixes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VpnClientAddressPoolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpnClientAddressPoolDefinition"]:
        if not json_data:
            return None
        return cls(
            AddressPrefixes=json_data.get("AddressPrefixes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpnClientAddressPoolDefinition = VpnClientAddressPoolDefinition


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


