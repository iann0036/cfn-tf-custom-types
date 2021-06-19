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
    AzureAsn: Optional[float]
    ExpressRouteCircuitName: Optional[str]
    Id: Optional[str]
    PeerAsn: Optional[float]
    PeeringType: Optional[str]
    PrimaryAzurePort: Optional[str]
    PrimaryPeerAddressPrefix: Optional[str]
    ResourceGroupName: Optional[str]
    RouteFilterId: Optional[str]
    SecondaryAzurePort: Optional[str]
    SecondaryPeerAddressPrefix: Optional[str]
    SharedKey: Optional[str]
    VlanId: Optional[float]
    Ipv6: Optional[Sequence["_Ipv6Definition"]]
    MicrosoftPeeringConfig: Optional[Sequence["_MicrosoftPeeringConfigDefinition"]]
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
            AzureAsn=json_data.get("AzureAsn"),
            ExpressRouteCircuitName=json_data.get("ExpressRouteCircuitName"),
            Id=json_data.get("Id"),
            PeerAsn=json_data.get("PeerAsn"),
            PeeringType=json_data.get("PeeringType"),
            PrimaryAzurePort=json_data.get("PrimaryAzurePort"),
            PrimaryPeerAddressPrefix=json_data.get("PrimaryPeerAddressPrefix"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            RouteFilterId=json_data.get("RouteFilterId"),
            SecondaryAzurePort=json_data.get("SecondaryAzurePort"),
            SecondaryPeerAddressPrefix=json_data.get("SecondaryPeerAddressPrefix"),
            SharedKey=json_data.get("SharedKey"),
            VlanId=json_data.get("VlanId"),
            Ipv6=deserialize_list(json_data.get("Ipv6"), Ipv6Definition),
            MicrosoftPeeringConfig=deserialize_list(json_data.get("MicrosoftPeeringConfig"), MicrosoftPeeringConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Ipv6Definition(BaseModel):
    PrimaryPeerAddressPrefix: Optional[str]
    RouteFilterId: Optional[str]
    SecondaryPeerAddressPrefix: Optional[str]
    MicrosoftPeering: Optional[Sequence["_MicrosoftPeeringDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv6Definition"]:
        if not json_data:
            return None
        return cls(
            PrimaryPeerAddressPrefix=json_data.get("PrimaryPeerAddressPrefix"),
            RouteFilterId=json_data.get("RouteFilterId"),
            SecondaryPeerAddressPrefix=json_data.get("SecondaryPeerAddressPrefix"),
            MicrosoftPeering=deserialize_list(json_data.get("MicrosoftPeering"), MicrosoftPeeringDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv6Definition = Ipv6Definition


@dataclass
class MicrosoftPeeringDefinition(BaseModel):
    AdvertisedPublicPrefixes: Optional[Sequence[str]]
    CustomerAsn: Optional[float]
    RoutingRegistryName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MicrosoftPeeringDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MicrosoftPeeringDefinition"]:
        if not json_data:
            return None
        return cls(
            AdvertisedPublicPrefixes=json_data.get("AdvertisedPublicPrefixes"),
            CustomerAsn=json_data.get("CustomerAsn"),
            RoutingRegistryName=json_data.get("RoutingRegistryName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MicrosoftPeeringDefinition = MicrosoftPeeringDefinition


@dataclass
class MicrosoftPeeringConfigDefinition(BaseModel):
    AdvertisedPublicPrefixes: Optional[Sequence[str]]
    CustomerAsn: Optional[float]
    RoutingRegistryName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MicrosoftPeeringConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MicrosoftPeeringConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AdvertisedPublicPrefixes=json_data.get("AdvertisedPublicPrefixes"),
            CustomerAsn=json_data.get("CustomerAsn"),
            RoutingRegistryName=json_data.get("RoutingRegistryName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MicrosoftPeeringConfigDefinition = MicrosoftPeeringConfigDefinition


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


