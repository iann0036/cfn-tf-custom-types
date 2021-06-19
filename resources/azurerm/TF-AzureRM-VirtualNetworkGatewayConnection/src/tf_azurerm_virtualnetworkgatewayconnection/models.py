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
    AuthorizationKey: Optional[str]
    ConnectionProtocol: Optional[str]
    DpdTimeoutSeconds: Optional[float]
    EnableBgp: Optional[bool]
    ExpressRouteCircuitId: Optional[str]
    ExpressRouteGatewayBypass: Optional[bool]
    Id: Optional[str]
    LocalAzureIpAddressEnabled: Optional[bool]
    LocalNetworkGatewayId: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    PeerVirtualNetworkGatewayId: Optional[str]
    ResourceGroupName: Optional[str]
    RoutingWeight: Optional[float]
    SharedKey: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Type: Optional[str]
    UsePolicyBasedTrafficSelectors: Optional[bool]
    VirtualNetworkGatewayId: Optional[str]
    IpsecPolicy: Optional[Sequence["_IpsecPolicyDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    TrafficSelectorPolicy: Optional[Sequence["_TrafficSelectorPolicyDefinition"]]

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
            AuthorizationKey=json_data.get("AuthorizationKey"),
            ConnectionProtocol=json_data.get("ConnectionProtocol"),
            DpdTimeoutSeconds=json_data.get("DpdTimeoutSeconds"),
            EnableBgp=json_data.get("EnableBgp"),
            ExpressRouteCircuitId=json_data.get("ExpressRouteCircuitId"),
            ExpressRouteGatewayBypass=json_data.get("ExpressRouteGatewayBypass"),
            Id=json_data.get("Id"),
            LocalAzureIpAddressEnabled=json_data.get("LocalAzureIpAddressEnabled"),
            LocalNetworkGatewayId=json_data.get("LocalNetworkGatewayId"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            PeerVirtualNetworkGatewayId=json_data.get("PeerVirtualNetworkGatewayId"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            RoutingWeight=json_data.get("RoutingWeight"),
            SharedKey=json_data.get("SharedKey"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Type=json_data.get("Type"),
            UsePolicyBasedTrafficSelectors=json_data.get("UsePolicyBasedTrafficSelectors"),
            VirtualNetworkGatewayId=json_data.get("VirtualNetworkGatewayId"),
            IpsecPolicy=deserialize_list(json_data.get("IpsecPolicy"), IpsecPolicyDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            TrafficSelectorPolicy=deserialize_list(json_data.get("TrafficSelectorPolicy"), TrafficSelectorPolicyDefinition),
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
class IpsecPolicyDefinition(BaseModel):
    DhGroup: Optional[str]
    IkeEncryption: Optional[str]
    IkeIntegrity: Optional[str]
    IpsecEncryption: Optional[str]
    IpsecIntegrity: Optional[str]
    PfsGroup: Optional[str]
    SaDatasize: Optional[float]
    SaLifetime: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IpsecPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpsecPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            DhGroup=json_data.get("DhGroup"),
            IkeEncryption=json_data.get("IkeEncryption"),
            IkeIntegrity=json_data.get("IkeIntegrity"),
            IpsecEncryption=json_data.get("IpsecEncryption"),
            IpsecIntegrity=json_data.get("IpsecIntegrity"),
            PfsGroup=json_data.get("PfsGroup"),
            SaDatasize=json_data.get("SaDatasize"),
            SaLifetime=json_data.get("SaLifetime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpsecPolicyDefinition = IpsecPolicyDefinition


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


@dataclass
class TrafficSelectorPolicyDefinition(BaseModel):
    LocalAddressCidrs: Optional[Sequence[str]]
    RemoteAddressCidrs: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_TrafficSelectorPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrafficSelectorPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            LocalAddressCidrs=json_data.get("LocalAddressCidrs"),
            RemoteAddressCidrs=json_data.get("RemoteAddressCidrs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrafficSelectorPolicyDefinition = TrafficSelectorPolicyDefinition


