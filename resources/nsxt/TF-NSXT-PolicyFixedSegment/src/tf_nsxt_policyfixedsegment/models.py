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
    ConnectivityPath: Optional[str]
    Description: Optional[str]
    DhcpConfigPath: Optional[str]
    DisplayName: Optional[str]
    DomainName: Optional[str]
    Id: Optional[str]
    NsxId: Optional[str]
    OverlayId: Optional[float]
    Path: Optional[str]
    Revision: Optional[float]
    TransportZonePath: Optional[str]
    VlanIds: Optional[Sequence[str]]
    AdvancedConfig: Optional[Sequence["_AdvancedConfigDefinition"]]
    L2Extension: Optional[Sequence["_L2ExtensionDefinition"]]
    Subnet: Optional[Sequence["_SubnetDefinition"]]
    Tag: Optional[Sequence["_TagDefinition"]]

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
            ConnectivityPath=json_data.get("ConnectivityPath"),
            Description=json_data.get("Description"),
            DhcpConfigPath=json_data.get("DhcpConfigPath"),
            DisplayName=json_data.get("DisplayName"),
            DomainName=json_data.get("DomainName"),
            Id=json_data.get("Id"),
            NsxId=json_data.get("NsxId"),
            OverlayId=json_data.get("OverlayId"),
            Path=json_data.get("Path"),
            Revision=json_data.get("Revision"),
            TransportZonePath=json_data.get("TransportZonePath"),
            VlanIds=json_data.get("VlanIds"),
            AdvancedConfig=deserialize_list(json_data.get("AdvancedConfig"), AdvancedConfigDefinition),
            L2Extension=deserialize_list(json_data.get("L2Extension"), L2ExtensionDefinition),
            Subnet=deserialize_list(json_data.get("Subnet"), SubnetDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AdvancedConfigDefinition(BaseModel):
    AddressPoolPath: Optional[str]
    Connectivity: Optional[str]
    Hybrid: Optional[bool]
    LocalEgress: Optional[bool]
    UplinkTeamingPolicy: Optional[str]
    UrpfMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdvancedConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvancedConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AddressPoolPath=json_data.get("AddressPoolPath"),
            Connectivity=json_data.get("Connectivity"),
            Hybrid=json_data.get("Hybrid"),
            LocalEgress=json_data.get("LocalEgress"),
            UplinkTeamingPolicy=json_data.get("UplinkTeamingPolicy"),
            UrpfMode=json_data.get("UrpfMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvancedConfigDefinition = AdvancedConfigDefinition


@dataclass
class L2ExtensionDefinition(BaseModel):
    L2vpnPaths: Optional[Sequence[str]]
    TunnelId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_L2ExtensionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_L2ExtensionDefinition"]:
        if not json_data:
            return None
        return cls(
            L2vpnPaths=json_data.get("L2vpnPaths"),
            TunnelId=json_data.get("TunnelId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_L2ExtensionDefinition = L2ExtensionDefinition


@dataclass
class SubnetDefinition(BaseModel):
    Cidr: Optional[str]
    DhcpRanges: Optional[Sequence[str]]
    DhcpV4Config: Optional[Sequence["_DhcpV4ConfigDefinition"]]
    DhcpV6Config: Optional[Sequence["_DhcpV6ConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SubnetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubnetDefinition"]:
        if not json_data:
            return None
        return cls(
            Cidr=json_data.get("Cidr"),
            DhcpRanges=json_data.get("DhcpRanges"),
            DhcpV4Config=deserialize_list(json_data.get("DhcpV4Config"), DhcpV4ConfigDefinition),
            DhcpV6Config=deserialize_list(json_data.get("DhcpV6Config"), DhcpV6ConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubnetDefinition = SubnetDefinition


@dataclass
class DhcpV4ConfigDefinition(BaseModel):
    DnsServers: Optional[Sequence[str]]
    LeaseTime: Optional[float]
    ServerAddress: Optional[str]
    DhcpGenericOption: Optional[Sequence["_DhcpGenericOptionDefinition"]]
    DhcpOption121: Optional[Sequence["_DhcpOption121Definition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DhcpV4ConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DhcpV4ConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            DnsServers=json_data.get("DnsServers"),
            LeaseTime=json_data.get("LeaseTime"),
            ServerAddress=json_data.get("ServerAddress"),
            DhcpGenericOption=deserialize_list(json_data.get("DhcpGenericOption"), DhcpGenericOptionDefinition),
            DhcpOption121=deserialize_list(json_data.get("DhcpOption121"), DhcpOption121Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DhcpV4ConfigDefinition = DhcpV4ConfigDefinition


@dataclass
class DhcpGenericOptionDefinition(BaseModel):
    Code: Optional[float]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DhcpGenericOptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DhcpGenericOptionDefinition"]:
        if not json_data:
            return None
        return cls(
            Code=json_data.get("Code"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DhcpGenericOptionDefinition = DhcpGenericOptionDefinition


@dataclass
class DhcpOption121Definition(BaseModel):
    Network: Optional[str]
    NextHop: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DhcpOption121Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DhcpOption121Definition"]:
        if not json_data:
            return None
        return cls(
            Network=json_data.get("Network"),
            NextHop=json_data.get("NextHop"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DhcpOption121Definition = DhcpOption121Definition


@dataclass
class DhcpV6ConfigDefinition(BaseModel):
    DnsServers: Optional[Sequence[str]]
    DomainNames: Optional[Sequence[str]]
    LeaseTime: Optional[float]
    PreferredTime: Optional[float]
    ServerAddress: Optional[str]
    SntpServers: Optional[Sequence[str]]
    ExcludedRange: Optional[Sequence["_ExcludedRangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DhcpV6ConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DhcpV6ConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            DnsServers=json_data.get("DnsServers"),
            DomainNames=json_data.get("DomainNames"),
            LeaseTime=json_data.get("LeaseTime"),
            PreferredTime=json_data.get("PreferredTime"),
            ServerAddress=json_data.get("ServerAddress"),
            SntpServers=json_data.get("SntpServers"),
            ExcludedRange=deserialize_list(json_data.get("ExcludedRange"), ExcludedRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DhcpV6ConfigDefinition = DhcpV6ConfigDefinition


@dataclass
class ExcludedRangeDefinition(BaseModel):
    End: Optional[str]
    Start: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExcludedRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExcludedRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Start=json_data.get("Start"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExcludedRangeDefinition = ExcludedRangeDefinition


@dataclass
class TagDefinition(BaseModel):
    Scope: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagDefinition"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagDefinition = TagDefinition


