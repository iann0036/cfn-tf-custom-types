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
    Id: Optional[str]
    UserTag: Optional[str]
    Uuid: Optional[str]
    VridVal: Optional[float]
    BladeParameters: Optional[Sequence["_BladeParametersDefinition"]]
    FloatingIp: Optional[Sequence["_FloatingIpDefinition"]]
    Follow: Optional[Sequence["_FollowDefinition"]]
    PreemptMode: Optional[Sequence["_PreemptModeDefinition"]]

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
            Id=json_data.get("Id"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            VridVal=json_data.get("VridVal"),
            BladeParameters=deserialize_list(json_data.get("BladeParameters"), BladeParametersDefinition),
            FloatingIp=deserialize_list(json_data.get("FloatingIp"), FloatingIpDefinition),
            Follow=deserialize_list(json_data.get("Follow"), FollowDefinition),
            PreemptMode=deserialize_list(json_data.get("PreemptMode"), PreemptModeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BladeParametersDefinition(BaseModel):
    FailOverPolicyTemplate: Optional[str]
    Priority: Optional[float]
    Uuid: Optional[str]
    TrackingOptions: Optional[Sequence["_TrackingOptionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BladeParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BladeParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            FailOverPolicyTemplate=json_data.get("FailOverPolicyTemplate"),
            Priority=json_data.get("Priority"),
            Uuid=json_data.get("Uuid"),
            TrackingOptions=deserialize_list(json_data.get("TrackingOptions"), TrackingOptionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BladeParametersDefinition = BladeParametersDefinition


@dataclass
class TrackingOptionsDefinition(BaseModel):
    Uuid: Optional[str]
    Bgp: Optional[Sequence["_BgpDefinition"]]
    Gateway: Optional[Sequence["_GatewayDefinition"]]
    Interface: Optional[Sequence["_InterfaceDefinition"]]
    Route: Optional[Sequence["_RouteDefinition"]]
    TrunkCfg: Optional[Sequence["_TrunkCfgDefinition"]]
    VlanCfg: Optional[Sequence["_VlanCfgDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TrackingOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrackingOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Uuid=json_data.get("Uuid"),
            Bgp=deserialize_list(json_data.get("Bgp"), BgpDefinition),
            Gateway=deserialize_list(json_data.get("Gateway"), GatewayDefinition),
            Interface=deserialize_list(json_data.get("Interface"), InterfaceDefinition),
            Route=deserialize_list(json_data.get("Route"), RouteDefinition),
            TrunkCfg=deserialize_list(json_data.get("TrunkCfg"), TrunkCfgDefinition),
            VlanCfg=deserialize_list(json_data.get("VlanCfg"), VlanCfgDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrackingOptionsDefinition = TrackingOptionsDefinition


@dataclass
class BgpDefinition(BaseModel):
    BgpIpv4AddressCfg: Optional[Sequence["_BgpIpv4AddressCfgDefinition"]]
    BgpIpv6AddressCfg: Optional[Sequence["_BgpIpv6AddressCfgDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BgpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BgpDefinition"]:
        if not json_data:
            return None
        return cls(
            BgpIpv4AddressCfg=deserialize_list(json_data.get("BgpIpv4AddressCfg"), BgpIpv4AddressCfgDefinition),
            BgpIpv6AddressCfg=deserialize_list(json_data.get("BgpIpv6AddressCfg"), BgpIpv6AddressCfgDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BgpDefinition = BgpDefinition


@dataclass
class BgpIpv4AddressCfgDefinition(BaseModel):
    BgpIpv4Address: Optional[str]
    PriorityCost: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_BgpIpv4AddressCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BgpIpv4AddressCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            BgpIpv4Address=json_data.get("BgpIpv4Address"),
            PriorityCost=json_data.get("PriorityCost"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BgpIpv4AddressCfgDefinition = BgpIpv4AddressCfgDefinition


@dataclass
class BgpIpv6AddressCfgDefinition(BaseModel):
    BgpIpv6Address: Optional[str]
    PriorityCost: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_BgpIpv6AddressCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BgpIpv6AddressCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            BgpIpv6Address=json_data.get("BgpIpv6Address"),
            PriorityCost=json_data.get("PriorityCost"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BgpIpv6AddressCfgDefinition = BgpIpv6AddressCfgDefinition


@dataclass
class GatewayDefinition(BaseModel):
    Ipv4GatewayList: Optional[Sequence["_Ipv4GatewayListDefinition"]]
    Ipv6GatewayList: Optional[Sequence["_Ipv6GatewayListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_GatewayDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GatewayDefinition"]:
        if not json_data:
            return None
        return cls(
            Ipv4GatewayList=deserialize_list(json_data.get("Ipv4GatewayList"), Ipv4GatewayListDefinition),
            Ipv6GatewayList=deserialize_list(json_data.get("Ipv6GatewayList"), Ipv6GatewayListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_GatewayDefinition = GatewayDefinition


@dataclass
class Ipv4GatewayListDefinition(BaseModel):
    IpAddress: Optional[str]
    PriorityCost: Optional[float]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv4GatewayListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv4GatewayListDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
            PriorityCost=json_data.get("PriorityCost"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv4GatewayListDefinition = Ipv4GatewayListDefinition


@dataclass
class Ipv6GatewayListDefinition(BaseModel):
    Ipv6Address: Optional[str]
    PriorityCost: Optional[float]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv6GatewayListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv6GatewayListDefinition"]:
        if not json_data:
            return None
        return cls(
            Ipv6Address=json_data.get("Ipv6Address"),
            PriorityCost=json_data.get("PriorityCost"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv6GatewayListDefinition = Ipv6GatewayListDefinition


@dataclass
class InterfaceDefinition(BaseModel):
    Ethernet: Optional[float]
    PriorityCost: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_InterfaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InterfaceDefinition"]:
        if not json_data:
            return None
        return cls(
            Ethernet=json_data.get("Ethernet"),
            PriorityCost=json_data.get("PriorityCost"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InterfaceDefinition = InterfaceDefinition


@dataclass
class RouteDefinition(BaseModel):
    IpDestinationCfg: Optional[Sequence["_IpDestinationCfgDefinition"]]
    Ipv6DestinationCfg: Optional[Sequence["_Ipv6DestinationCfgDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RouteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RouteDefinition"]:
        if not json_data:
            return None
        return cls(
            IpDestinationCfg=deserialize_list(json_data.get("IpDestinationCfg"), IpDestinationCfgDefinition),
            Ipv6DestinationCfg=deserialize_list(json_data.get("Ipv6DestinationCfg"), Ipv6DestinationCfgDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RouteDefinition = RouteDefinition


@dataclass
class IpDestinationCfgDefinition(BaseModel):
    Distance: Optional[float]
    Gateway: Optional[str]
    IpDestination: Optional[str]
    Mask: Optional[str]
    PriorityCost: Optional[float]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpDestinationCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpDestinationCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Distance=json_data.get("Distance"),
            Gateway=json_data.get("Gateway"),
            IpDestination=json_data.get("IpDestination"),
            Mask=json_data.get("Mask"),
            PriorityCost=json_data.get("PriorityCost"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpDestinationCfgDefinition = IpDestinationCfgDefinition


@dataclass
class Ipv6DestinationCfgDefinition(BaseModel):
    Distance: Optional[float]
    Gatewayv6: Optional[str]
    Ipv6Destination: Optional[str]
    PriorityCost: Optional[float]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv6DestinationCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv6DestinationCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Distance=json_data.get("Distance"),
            Gatewayv6=json_data.get("Gatewayv6"),
            Ipv6Destination=json_data.get("Ipv6Destination"),
            PriorityCost=json_data.get("PriorityCost"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv6DestinationCfgDefinition = Ipv6DestinationCfgDefinition


@dataclass
class TrunkCfgDefinition(BaseModel):
    PerPortPri: Optional[float]
    PriorityCost: Optional[float]
    Trunk: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TrunkCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrunkCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            PerPortPri=json_data.get("PerPortPri"),
            PriorityCost=json_data.get("PriorityCost"),
            Trunk=json_data.get("Trunk"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrunkCfgDefinition = TrunkCfgDefinition


@dataclass
class VlanCfgDefinition(BaseModel):
    PriorityCost: Optional[float]
    Timeout: Optional[float]
    Vlan: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_VlanCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VlanCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            PriorityCost=json_data.get("PriorityCost"),
            Timeout=json_data.get("Timeout"),
            Vlan=json_data.get("Vlan"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VlanCfgDefinition = VlanCfgDefinition


@dataclass
class FloatingIpDefinition(BaseModel):
    IpAddressCfg: Optional[Sequence["_IpAddressCfgDefinition"]]
    IpAddressPartCfg: Optional[Sequence["_IpAddressPartCfgDefinition"]]
    Ipv6AddressCfg: Optional[Sequence["_Ipv6AddressCfgDefinition"]]
    Ipv6AddressPartCfg: Optional[Sequence["_Ipv6AddressPartCfgDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FloatingIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FloatingIpDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddressCfg=deserialize_list(json_data.get("IpAddressCfg"), IpAddressCfgDefinition),
            IpAddressPartCfg=deserialize_list(json_data.get("IpAddressPartCfg"), IpAddressPartCfgDefinition),
            Ipv6AddressCfg=deserialize_list(json_data.get("Ipv6AddressCfg"), Ipv6AddressCfgDefinition),
            Ipv6AddressPartCfg=deserialize_list(json_data.get("Ipv6AddressPartCfg"), Ipv6AddressPartCfgDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FloatingIpDefinition = FloatingIpDefinition


@dataclass
class IpAddressCfgDefinition(BaseModel):
    IpAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpAddressCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAddressCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAddressCfgDefinition = IpAddressCfgDefinition


@dataclass
class IpAddressPartCfgDefinition(BaseModel):
    IpAddressPartition: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpAddressPartCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAddressPartCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddressPartition=json_data.get("IpAddressPartition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAddressPartCfgDefinition = IpAddressPartCfgDefinition


@dataclass
class Ipv6AddressCfgDefinition(BaseModel):
    Ethernet: Optional[float]
    Ipv6Address: Optional[str]
    Trunk: Optional[float]
    Ve: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv6AddressCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv6AddressCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Ethernet=json_data.get("Ethernet"),
            Ipv6Address=json_data.get("Ipv6Address"),
            Trunk=json_data.get("Trunk"),
            Ve=json_data.get("Ve"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv6AddressCfgDefinition = Ipv6AddressCfgDefinition


@dataclass
class Ipv6AddressPartCfgDefinition(BaseModel):
    Ethernet: Optional[float]
    Ipv6AddressPartition: Optional[str]
    Trunk: Optional[float]
    Ve: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv6AddressPartCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv6AddressPartCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Ethernet=json_data.get("Ethernet"),
            Ipv6AddressPartition=json_data.get("Ipv6AddressPartition"),
            Trunk=json_data.get("Trunk"),
            Ve=json_data.get("Ve"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv6AddressPartCfgDefinition = Ipv6AddressPartCfgDefinition


@dataclass
class FollowDefinition(BaseModel):
    VridLead: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FollowDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FollowDefinition"]:
        if not json_data:
            return None
        return cls(
            VridLead=json_data.get("VridLead"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FollowDefinition = FollowDefinition


@dataclass
class PreemptModeDefinition(BaseModel):
    Disable: Optional[float]
    Threshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PreemptModeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PreemptModeDefinition"]:
        if not json_data:
            return None
        return cls(
            Disable=json_data.get("Disable"),
            Threshold=json_data.get("Threshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PreemptModeDefinition = PreemptModeDefinition


