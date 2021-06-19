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
    BgpPeerLabels: Optional[Sequence[str]]
    CloudRef: Optional[str]
    EastWestPlacement: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    TenantRef: Optional[str]
    Tier1Lr: Optional[str]
    UseStandardAlb: Optional[bool]
    Uuid: Optional[str]
    VrfContextRef: Optional[str]
    VsvipCloudConfigCksum: Optional[str]
    DnsInfo: Optional[Sequence["_DnsInfoDefinition"]]
    IpamSelector: Optional[Sequence["_IpamSelectorDefinition"]]
    Markers: Optional[Sequence["_MarkersDefinition"]]
    Vip: Optional[Sequence["_VipDefinition"]]

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
            BgpPeerLabels=json_data.get("BgpPeerLabels"),
            CloudRef=json_data.get("CloudRef"),
            EastWestPlacement=json_data.get("EastWestPlacement"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            TenantRef=json_data.get("TenantRef"),
            Tier1Lr=json_data.get("Tier1Lr"),
            UseStandardAlb=json_data.get("UseStandardAlb"),
            Uuid=json_data.get("Uuid"),
            VrfContextRef=json_data.get("VrfContextRef"),
            VsvipCloudConfigCksum=json_data.get("VsvipCloudConfigCksum"),
            DnsInfo=deserialize_list(json_data.get("DnsInfo"), DnsInfoDefinition),
            IpamSelector=deserialize_list(json_data.get("IpamSelector"), IpamSelectorDefinition),
            Markers=deserialize_list(json_data.get("Markers"), MarkersDefinition),
            Vip=deserialize_list(json_data.get("Vip"), VipDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DnsInfoDefinition(BaseModel):
    Algorithm: Optional[str]
    Fqdn: Optional[str]
    NumRecordsInResponse: Optional[float]
    Ttl: Optional[float]
    Type: Optional[str]
    Cname: Optional[Sequence["_CnameDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DnsInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Algorithm=json_data.get("Algorithm"),
            Fqdn=json_data.get("Fqdn"),
            NumRecordsInResponse=json_data.get("NumRecordsInResponse"),
            Ttl=json_data.get("Ttl"),
            Type=json_data.get("Type"),
            Cname=deserialize_list(json_data.get("Cname"), CnameDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsInfoDefinition = DnsInfoDefinition


@dataclass
class CnameDefinition(BaseModel):
    Cname: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CnameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CnameDefinition"]:
        if not json_data:
            return None
        return cls(
            Cname=json_data.get("Cname"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CnameDefinition = CnameDefinition


@dataclass
class IpamSelectorDefinition(BaseModel):
    Type: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IpamSelectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpamSelectorDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpamSelectorDefinition = IpamSelectorDefinition


@dataclass
class LabelsDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class MarkersDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MarkersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MarkersDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MarkersDefinition = MarkersDefinition


@dataclass
class VipDefinition(BaseModel):
    AutoAllocateFloatingIp: Optional[bool]
    AutoAllocateIp: Optional[bool]
    AutoAllocateIpType: Optional[str]
    AvailabilityZone: Optional[str]
    AviAllocatedFip: Optional[bool]
    AviAllocatedVip: Optional[bool]
    Enabled: Optional[bool]
    FloatingSubnet6Uuid: Optional[str]
    FloatingSubnetUuid: Optional[str]
    NetworkRef: Optional[str]
    PortUuid: Optional[str]
    PrefixLength: Optional[float]
    Subnet6Uuid: Optional[str]
    SubnetUuid: Optional[str]
    VipId: Optional[str]
    DiscoveredNetworks: Optional[Sequence["_DiscoveredNetworksDefinition"]]
    FloatingIp: Optional[Sequence["_FloatingIpDefinition"]]
    FloatingIp6: Optional[Sequence["_FloatingIp6Definition"]]
    Ip6Address: Optional[Sequence["_Ip6AddressDefinition"]]
    IpAddress: Optional[Sequence["_IpAddressDefinition"]]
    IpamNetworkSubnet: Optional[Sequence["_IpamNetworkSubnetDefinition"]]
    PlacementNetworks: Optional[Sequence["_PlacementNetworksDefinition"]]
    Subnet: Optional[Sequence["_SubnetDefinition"]]
    Subnet6: Optional[Sequence["_Subnet6Definition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VipDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VipDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoAllocateFloatingIp=json_data.get("AutoAllocateFloatingIp"),
            AutoAllocateIp=json_data.get("AutoAllocateIp"),
            AutoAllocateIpType=json_data.get("AutoAllocateIpType"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            AviAllocatedFip=json_data.get("AviAllocatedFip"),
            AviAllocatedVip=json_data.get("AviAllocatedVip"),
            Enabled=json_data.get("Enabled"),
            FloatingSubnet6Uuid=json_data.get("FloatingSubnet6Uuid"),
            FloatingSubnetUuid=json_data.get("FloatingSubnetUuid"),
            NetworkRef=json_data.get("NetworkRef"),
            PortUuid=json_data.get("PortUuid"),
            PrefixLength=json_data.get("PrefixLength"),
            Subnet6Uuid=json_data.get("Subnet6Uuid"),
            SubnetUuid=json_data.get("SubnetUuid"),
            VipId=json_data.get("VipId"),
            DiscoveredNetworks=deserialize_list(json_data.get("DiscoveredNetworks"), DiscoveredNetworksDefinition),
            FloatingIp=deserialize_list(json_data.get("FloatingIp"), FloatingIpDefinition),
            FloatingIp6=deserialize_list(json_data.get("FloatingIp6"), FloatingIp6Definition),
            Ip6Address=deserialize_list(json_data.get("Ip6Address"), Ip6AddressDefinition),
            IpAddress=deserialize_list(json_data.get("IpAddress"), IpAddressDefinition),
            IpamNetworkSubnet=deserialize_list(json_data.get("IpamNetworkSubnet"), IpamNetworkSubnetDefinition),
            PlacementNetworks=deserialize_list(json_data.get("PlacementNetworks"), PlacementNetworksDefinition),
            Subnet=deserialize_list(json_data.get("Subnet"), SubnetDefinition),
            Subnet6=deserialize_list(json_data.get("Subnet6"), Subnet6Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VipDefinition = VipDefinition


@dataclass
class DiscoveredNetworksDefinition(BaseModel):
    NetworkRef: Optional[str]
    Subnet: Optional[Sequence["_SubnetDefinition"]]
    Subnet6: Optional[Sequence["_Subnet6Definition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DiscoveredNetworksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiscoveredNetworksDefinition"]:
        if not json_data:
            return None
        return cls(
            NetworkRef=json_data.get("NetworkRef"),
            Subnet=deserialize_list(json_data.get("Subnet"), SubnetDefinition),
            Subnet6=deserialize_list(json_data.get("Subnet6"), Subnet6Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiscoveredNetworksDefinition = DiscoveredNetworksDefinition


@dataclass
class SubnetDefinition(BaseModel):
    Mask: Optional[float]
    IpAddr: Optional[Sequence["_IpAddrDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SubnetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubnetDefinition"]:
        if not json_data:
            return None
        return cls(
            Mask=json_data.get("Mask"),
            IpAddr=deserialize_list(json_data.get("IpAddr"), IpAddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubnetDefinition = SubnetDefinition


@dataclass
class IpAddrDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpAddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAddrDefinition = IpAddrDefinition


@dataclass
class Subnet6Definition(BaseModel):
    Mask: Optional[float]
    IpAddr: Optional[Sequence["_IpAddrDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_Subnet6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Subnet6Definition"]:
        if not json_data:
            return None
        return cls(
            Mask=json_data.get("Mask"),
            IpAddr=deserialize_list(json_data.get("IpAddr"), IpAddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_Subnet6Definition = Subnet6Definition


@dataclass
class FloatingIpDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FloatingIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FloatingIpDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FloatingIpDefinition = FloatingIpDefinition


@dataclass
class FloatingIp6Definition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FloatingIp6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FloatingIp6Definition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FloatingIp6Definition = FloatingIp6Definition


@dataclass
class Ip6AddressDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ip6AddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ip6AddressDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ip6AddressDefinition = Ip6AddressDefinition


@dataclass
class IpAddressDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAddressDefinition = IpAddressDefinition


@dataclass
class IpamNetworkSubnetDefinition(BaseModel):
    NetworkRef: Optional[str]
    Subnet6Uuid: Optional[str]
    SubnetUuid: Optional[str]
    Subnet: Optional[Sequence["_SubnetDefinition"]]
    Subnet6: Optional[Sequence["_Subnet6Definition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IpamNetworkSubnetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpamNetworkSubnetDefinition"]:
        if not json_data:
            return None
        return cls(
            NetworkRef=json_data.get("NetworkRef"),
            Subnet6Uuid=json_data.get("Subnet6Uuid"),
            SubnetUuid=json_data.get("SubnetUuid"),
            Subnet=deserialize_list(json_data.get("Subnet"), SubnetDefinition),
            Subnet6=deserialize_list(json_data.get("Subnet6"), Subnet6Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpamNetworkSubnetDefinition = IpamNetworkSubnetDefinition


@dataclass
class PlacementNetworksDefinition(BaseModel):
    NetworkRef: Optional[str]
    Subnet: Optional[Sequence["_SubnetDefinition"]]
    Subnet6: Optional[Sequence["_Subnet6Definition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PlacementNetworksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlacementNetworksDefinition"]:
        if not json_data:
            return None
        return cls(
            NetworkRef=json_data.get("NetworkRef"),
            Subnet=deserialize_list(json_data.get("Subnet"), SubnetDefinition),
            Subnet6=deserialize_list(json_data.get("Subnet6"), Subnet6Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlacementNetworksDefinition = PlacementNetworksDefinition


