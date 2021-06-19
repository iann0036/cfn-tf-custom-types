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
    Color: Optional[str]
    Comments: Optional[str]
    Id: Optional[str]
    IgnoreErrors: Optional[bool]
    IgnoreWarnings: Optional[bool]
    Ipv4Address: Optional[str]
    Ipv6Address: Optional[str]
    Name: Optional[str]
    NatSettings: Optional[Sequence["_NatSettingsDefinition"]]
    Tags: Optional[Sequence[str]]
    HostServers: Optional[Sequence["_HostServersDefinition"]]
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
            Color=json_data.get("Color"),
            Comments=json_data.get("Comments"),
            Id=json_data.get("Id"),
            IgnoreErrors=json_data.get("IgnoreErrors"),
            IgnoreWarnings=json_data.get("IgnoreWarnings"),
            Ipv4Address=json_data.get("Ipv4Address"),
            Ipv6Address=json_data.get("Ipv6Address"),
            Name=json_data.get("Name"),
            NatSettings=deserialize_list(json_data.get("NatSettings"), NatSettingsDefinition),
            Tags=json_data.get("Tags"),
            HostServers=deserialize_list(json_data.get("HostServers"), HostServersDefinition),
            Interfaces=deserialize_list(json_data.get("Interfaces"), InterfacesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class NatSettingsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NatSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NatSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NatSettingsDefinition = NatSettingsDefinition


@dataclass
class HostServersDefinition(BaseModel):
    DnsServer: Optional[bool]
    MailServer: Optional[bool]
    WebServer: Optional[bool]
    WebServerConfig: Optional[Sequence["_WebServerConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HostServersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostServersDefinition"]:
        if not json_data:
            return None
        return cls(
            DnsServer=json_data.get("DnsServer"),
            MailServer=json_data.get("MailServer"),
            WebServer=json_data.get("WebServer"),
            WebServerConfig=deserialize_list(json_data.get("WebServerConfig"), WebServerConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostServersDefinition = HostServersDefinition


@dataclass
class WebServerConfigDefinition(BaseModel):
    AdditionalPorts: Optional[Sequence[str]]
    ApplicationEngines: Optional[Sequence[str]]
    ListenStandardPort: Optional[bool]
    OperatingSystem: Optional[str]
    ProtectedBy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WebServerConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebServerConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalPorts=json_data.get("AdditionalPorts"),
            ApplicationEngines=json_data.get("ApplicationEngines"),
            ListenStandardPort=json_data.get("ListenStandardPort"),
            OperatingSystem=json_data.get("OperatingSystem"),
            ProtectedBy=json_data.get("ProtectedBy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebServerConfigDefinition = WebServerConfigDefinition


@dataclass
class InterfacesDefinition(BaseModel):
    Color: Optional[str]
    Comments: Optional[str]
    IgnoreErrors: Optional[bool]
    IgnoreWarnings: Optional[bool]
    MaskLength4: Optional[float]
    MaskLength6: Optional[float]
    Name: Optional[str]
    Subnet4: Optional[str]
    Subnet6: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InterfacesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InterfacesDefinition"]:
        if not json_data:
            return None
        return cls(
            Color=json_data.get("Color"),
            Comments=json_data.get("Comments"),
            IgnoreErrors=json_data.get("IgnoreErrors"),
            IgnoreWarnings=json_data.get("IgnoreWarnings"),
            MaskLength4=json_data.get("MaskLength4"),
            MaskLength6=json_data.get("MaskLength6"),
            Name=json_data.get("Name"),
            Subnet4=json_data.get("Subnet4"),
            Subnet6=json_data.get("Subnet6"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InterfacesDefinition = InterfacesDefinition


