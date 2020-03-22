# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    AuthorizationKey: Optional[str]
    ConnectionProtocol: Optional[str]
    EnableBgp: Optional[bool]
    ExpressRouteCircuitId: Optional[str]
    ExpressRouteGatewayBypass: Optional[bool]
    Id: Optional[str]
    LocalNetworkGatewayId: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    PeerVirtualNetworkGatewayId: Optional[str]
    ResourceGroupName: Optional[str]
    RoutingWeight: Optional[float]
    SharedKey: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Type: Optional[str]
    UsePolicyBasedTrafficSelectors: Optional[bool]
    VirtualNetworkGatewayId: Optional[str]
    IpsecPolicy: Optional[Sequence["_IpsecPolicy"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AuthorizationKey=json_data.get("AuthorizationKey"),
            ConnectionProtocol=json_data.get("ConnectionProtocol"),
            EnableBgp=json_data.get("EnableBgp"),
            ExpressRouteCircuitId=json_data.get("ExpressRouteCircuitId"),
            ExpressRouteGatewayBypass=json_data.get("ExpressRouteGatewayBypass"),
            Id=json_data.get("Id"),
            LocalNetworkGatewayId=json_data.get("LocalNetworkGatewayId"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            PeerVirtualNetworkGatewayId=json_data.get("PeerVirtualNetworkGatewayId"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            RoutingWeight=json_data.get("RoutingWeight"),
            SharedKey=json_data.get("SharedKey"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
            UsePolicyBasedTrafficSelectors=json_data.get("UsePolicyBasedTrafficSelectors"),
            VirtualNetworkGatewayId=json_data.get("VirtualNetworkGatewayId"),
            IpsecPolicy=json_data.get("IpsecPolicy"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class IpsecPolicy:
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
        cls: Type["_IpsecPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpsecPolicy"]:
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
_IpsecPolicy = IpsecPolicy


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


