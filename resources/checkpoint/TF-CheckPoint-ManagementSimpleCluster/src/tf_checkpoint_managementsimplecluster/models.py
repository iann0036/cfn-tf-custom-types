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
    ClusterMode: Optional[str]
    Color: Optional[str]
    Comments: Optional[str]
    ContentAwareness: Optional[bool]
    DataAwareness: Optional[bool]
    DynamicIp: Optional[bool]
    Firewall: Optional[bool]
    FirewallSettings: Optional[Sequence["_FirewallSettingsDefinition"]]
    Hardware: Optional[str]
    Id: Optional[str]
    IgnoreErrors: Optional[bool]
    IgnoreWarnings: Optional[bool]
    Ips: Optional[bool]
    Ipv4Address: Optional[str]
    Ipv6Address: Optional[str]
    Name: Optional[str]
    OsName: Optional[str]
    SaveLogsLocally: Optional[bool]
    SendAlertsToServer: Optional[Sequence[str]]
    SendLogsToBackupServer: Optional[Sequence[str]]
    SendLogsToServer: Optional[Sequence[str]]
    SicName: Optional[str]
    SicState: Optional[str]
    Tags: Optional[Sequence[str]]
    ThreatEmulation: Optional[bool]
    UrlFiltering: Optional[bool]
    Version: Optional[str]
    Vpn: Optional[bool]
    VpnSettings: Optional[Sequence["_VpnSettingsDefinition"]]
    Interfaces: Optional[Sequence["_InterfacesDefinition"]]
    Members: Optional[Sequence["_MembersDefinition"]]

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
            ClusterMode=json_data.get("ClusterMode"),
            Color=json_data.get("Color"),
            Comments=json_data.get("Comments"),
            ContentAwareness=json_data.get("ContentAwareness"),
            DataAwareness=json_data.get("DataAwareness"),
            DynamicIp=json_data.get("DynamicIp"),
            Firewall=json_data.get("Firewall"),
            FirewallSettings=deserialize_list(json_data.get("FirewallSettings"), FirewallSettingsDefinition),
            Hardware=json_data.get("Hardware"),
            Id=json_data.get("Id"),
            IgnoreErrors=json_data.get("IgnoreErrors"),
            IgnoreWarnings=json_data.get("IgnoreWarnings"),
            Ips=json_data.get("Ips"),
            Ipv4Address=json_data.get("Ipv4Address"),
            Ipv6Address=json_data.get("Ipv6Address"),
            Name=json_data.get("Name"),
            OsName=json_data.get("OsName"),
            SaveLogsLocally=json_data.get("SaveLogsLocally"),
            SendAlertsToServer=json_data.get("SendAlertsToServer"),
            SendLogsToBackupServer=json_data.get("SendLogsToBackupServer"),
            SendLogsToServer=json_data.get("SendLogsToServer"),
            SicName=json_data.get("SicName"),
            SicState=json_data.get("SicState"),
            Tags=json_data.get("Tags"),
            ThreatEmulation=json_data.get("ThreatEmulation"),
            UrlFiltering=json_data.get("UrlFiltering"),
            Version=json_data.get("Version"),
            Vpn=json_data.get("Vpn"),
            VpnSettings=deserialize_list(json_data.get("VpnSettings"), VpnSettingsDefinition),
            Interfaces=deserialize_list(json_data.get("Interfaces"), InterfacesDefinition),
            Members=deserialize_list(json_data.get("Members"), MembersDefinition),
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
    Ipv4Address: Optional[str]
    Ipv4MaskLength: Optional[str]
    Ipv4NetworkMask: Optional[str]
    Ipv6Address: Optional[str]
    Ipv6MaskLength: Optional[str]
    Ipv6NetworkMask: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InterfacesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InterfacesDefinition"]:
        if not json_data:
            return None
        return cls(
            Ipv4Address=json_data.get("Ipv4Address"),
            Ipv4MaskLength=json_data.get("Ipv4MaskLength"),
            Ipv4NetworkMask=json_data.get("Ipv4NetworkMask"),
            Ipv6Address=json_data.get("Ipv6Address"),
            Ipv6MaskLength=json_data.get("Ipv6MaskLength"),
            Ipv6NetworkMask=json_data.get("Ipv6NetworkMask"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InterfacesDefinition = InterfacesDefinition


@dataclass
class MembersDefinition(BaseModel):
    IpAddress: Optional[str]
    Name: Optional[str]
    OneTimePassword: Optional[str]
    Interfaces: Optional[Sequence["_InterfacesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MembersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MembersDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
            Name=json_data.get("Name"),
            OneTimePassword=json_data.get("OneTimePassword"),
            Interfaces=deserialize_list(json_data.get("Interfaces"), InterfacesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MembersDefinition = MembersDefinition


