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
    AntiBot: Optional[bool]
    AntiVirus: Optional[bool]
    ApplicationControl: Optional[bool]
    Color: Optional[str]
    Comments: Optional[str]
    ContentAwareness: Optional[bool]
    DynamicIp: Optional[bool]
    Firewall: Optional[bool]
    FirewallSettings: Optional[Sequence["_FirewallSettingsDefinition"]]
    Hardware: Optional[str]
    IcapServer: Optional[bool]
    Id: Optional[str]
    IgnoreWarnings: Optional[bool]
    Ips: Optional[bool]
    Ipv4Address: Optional[str]
    Ipv6Address: Optional[str]
    LogsSettings: Optional[Sequence["_LogsSettingsDefinition"]]
    Name: Optional[str]
    OneTimePassword: Optional[str]
    OsName: Optional[str]
    SaveLogsLocally: Optional[bool]
    SendAlertsToServer: Optional[Sequence[str]]
    SendLogsToBackupServer: Optional[Sequence[str]]
    SendLogsToServer: Optional[Sequence[str]]
    SicName: Optional[str]
    SicState: Optional[str]
    Tags: Optional[Sequence[str]]
    ThreatEmulation: Optional[bool]
    ThreatExtraction: Optional[bool]
    UrlFiltering: Optional[bool]
    Version: Optional[str]
    Vpn: Optional[bool]
    VpnSettings: Optional[Sequence["_VpnSettingsDefinition"]]
    Interfaces: Optional[Sequence["_InterfacesDefinition"]]

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
            AntiBot=json_data.get("AntiBot"),
            AntiVirus=json_data.get("AntiVirus"),
            ApplicationControl=json_data.get("ApplicationControl"),
            Color=json_data.get("Color"),
            Comments=json_data.get("Comments"),
            ContentAwareness=json_data.get("ContentAwareness"),
            DynamicIp=json_data.get("DynamicIp"),
            Firewall=json_data.get("Firewall"),
            FirewallSettings=deserialize_list(json_data.get("FirewallSettings"), FirewallSettingsDefinition),
            Hardware=json_data.get("Hardware"),
            IcapServer=json_data.get("IcapServer"),
            Id=json_data.get("Id"),
            IgnoreWarnings=json_data.get("IgnoreWarnings"),
            Ips=json_data.get("Ips"),
            Ipv4Address=json_data.get("Ipv4Address"),
            Ipv6Address=json_data.get("Ipv6Address"),
            LogsSettings=deserialize_list(json_data.get("LogsSettings"), LogsSettingsDefinition),
            Name=json_data.get("Name"),
            OneTimePassword=json_data.get("OneTimePassword"),
            OsName=json_data.get("OsName"),
            SaveLogsLocally=json_data.get("SaveLogsLocally"),
            SendAlertsToServer=json_data.get("SendAlertsToServer"),
            SendLogsToBackupServer=json_data.get("SendLogsToBackupServer"),
            SendLogsToServer=json_data.get("SendLogsToServer"),
            SicName=json_data.get("SicName"),
            SicState=json_data.get("SicState"),
            Tags=json_data.get("Tags"),
            ThreatEmulation=json_data.get("ThreatEmulation"),
            ThreatExtraction=json_data.get("ThreatExtraction"),
            UrlFiltering=json_data.get("UrlFiltering"),
            Version=json_data.get("Version"),
            Vpn=json_data.get("Vpn"),
            VpnSettings=deserialize_list(json_data.get("VpnSettings"), VpnSettingsDefinition),
            Interfaces=deserialize_list(json_data.get("Interfaces"), InterfacesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FirewallSettingsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FirewallSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FirewallSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FirewallSettingsDefinition = FirewallSettingsDefinition


@dataclass
class LogsSettingsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogsSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogsSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogsSettingsDefinition = LogsSettingsDefinition


@dataclass
class VpnSettingsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VpnSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpnSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpnSettingsDefinition = VpnSettingsDefinition


@dataclass
class InterfacesDefinition(BaseModel):
    AntiSpoofing: Optional[bool]
    AntiSpoofingSettings: Optional[Sequence["_AntiSpoofingSettingsDefinition"]]
    Color: Optional[str]
    Comments: Optional[str]
    Ipv4Address: Optional[str]
    Ipv4MaskLength: Optional[str]
    Ipv4NetworkMask: Optional[str]
    Ipv6Address: Optional[str]
    Ipv6MaskLength: Optional[str]
    Ipv6NetworkMask: Optional[str]
    Name: Optional[str]
    SecurityZone: Optional[bool]
    SecurityZoneSettings: Optional[Sequence["_SecurityZoneSettingsDefinition"]]
    Topology: Optional[str]
    TopologySettings: Optional[Sequence["_TopologySettingsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InterfacesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InterfacesDefinition"]:
        if not json_data:
            return None
        return cls(
            AntiSpoofing=json_data.get("AntiSpoofing"),
            AntiSpoofingSettings=deserialize_list(json_data.get("AntiSpoofingSettings"), AntiSpoofingSettingsDefinition),
            Color=json_data.get("Color"),
            Comments=json_data.get("Comments"),
            Ipv4Address=json_data.get("Ipv4Address"),
            Ipv4MaskLength=json_data.get("Ipv4MaskLength"),
            Ipv4NetworkMask=json_data.get("Ipv4NetworkMask"),
            Ipv6Address=json_data.get("Ipv6Address"),
            Ipv6MaskLength=json_data.get("Ipv6MaskLength"),
            Ipv6NetworkMask=json_data.get("Ipv6NetworkMask"),
            Name=json_data.get("Name"),
            SecurityZone=json_data.get("SecurityZone"),
            SecurityZoneSettings=deserialize_list(json_data.get("SecurityZoneSettings"), SecurityZoneSettingsDefinition),
            Topology=json_data.get("Topology"),
            TopologySettings=deserialize_list(json_data.get("TopologySettings"), TopologySettingsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InterfacesDefinition = InterfacesDefinition


@dataclass
class AntiSpoofingSettingsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AntiSpoofingSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AntiSpoofingSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AntiSpoofingSettingsDefinition = AntiSpoofingSettingsDefinition


@dataclass
class SecurityZoneSettingsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecurityZoneSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecurityZoneSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecurityZoneSettingsDefinition = SecurityZoneSettingsDefinition


@dataclass
class TopologySettingsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TopologySettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TopologySettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TopologySettingsDefinition = TopologySettingsDefinition


