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
    Hardware: Optional[str]
    Id: Optional[str]
    IgnoreErrors: Optional[bool]
    IgnoreWarnings: Optional[bool]
    Ipv4Address: Optional[str]
    Ipv6Address: Optional[str]
    LogsSettings: Optional[Sequence["_LogsSettingsDefinition"]]
    ManagementBlades: Optional[Sequence["_ManagementBladesDefinition"]]
    Name: Optional[str]
    NatSettings: Optional[Sequence["_NatSettingsDefinition"]]
    OneTimePassword: Optional[str]
    Os: Optional[str]
    SaveLogsLocally: Optional[bool]
    SendAlertsToServer: Optional[Sequence[str]]
    SendLogsToBackupServer: Optional[Sequence[str]]
    SendLogsToServer: Optional[Sequence[str]]
    SicName: Optional[str]
    SicState: Optional[str]
    Tags: Optional[Sequence[str]]
    Version: Optional[str]
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
            Hardware=json_data.get("Hardware"),
            Id=json_data.get("Id"),
            IgnoreErrors=json_data.get("IgnoreErrors"),
            IgnoreWarnings=json_data.get("IgnoreWarnings"),
            Ipv4Address=json_data.get("Ipv4Address"),
            Ipv6Address=json_data.get("Ipv6Address"),
            LogsSettings=deserialize_list(json_data.get("LogsSettings"), LogsSettingsDefinition),
            ManagementBlades=deserialize_list(json_data.get("ManagementBlades"), ManagementBladesDefinition),
            Name=json_data.get("Name"),
            NatSettings=deserialize_list(json_data.get("NatSettings"), NatSettingsDefinition),
            OneTimePassword=json_data.get("OneTimePassword"),
            Os=json_data.get("Os"),
            SaveLogsLocally=json_data.get("SaveLogsLocally"),
            SendAlertsToServer=json_data.get("SendAlertsToServer"),
            SendLogsToBackupServer=json_data.get("SendLogsToBackupServer"),
            SendLogsToServer=json_data.get("SendLogsToServer"),
            SicName=json_data.get("SicName"),
            SicState=json_data.get("SicState"),
            Tags=json_data.get("Tags"),
            Version=json_data.get("Version"),
            Interfaces=deserialize_list(json_data.get("Interfaces"), InterfacesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class ManagementBladesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ManagementBladesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagementBladesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManagementBladesDefinition = ManagementBladesDefinition


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
    SubnetMask: Optional[str]

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
            SubnetMask=json_data.get("SubnetMask"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InterfacesDefinition = InterfacesDefinition


