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
    Description: Optional[str]
    DeviceGroup: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    PacketCapture: Optional[str]
    SinkholeIpv4Address: Optional[str]
    SinkholeIpv6Address: Optional[str]
    ThreatExceptions: Optional[Sequence[str]]
    Vsys: Optional[str]
    BotnetList: Optional[Sequence["_BotnetListDefinition"]]
    DnsCategory: Optional[Sequence["_DnsCategoryDefinition"]]
    Exception: Optional[Sequence["_ExceptionDefinition"]]
    Rule: Optional[Sequence["_RuleDefinition"]]
    WhiteList: Optional[Sequence["_WhiteListDefinition"]]

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
            Description=json_data.get("Description"),
            DeviceGroup=json_data.get("DeviceGroup"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PacketCapture=json_data.get("PacketCapture"),
            SinkholeIpv4Address=json_data.get("SinkholeIpv4Address"),
            SinkholeIpv6Address=json_data.get("SinkholeIpv6Address"),
            ThreatExceptions=json_data.get("ThreatExceptions"),
            Vsys=json_data.get("Vsys"),
            BotnetList=deserialize_list(json_data.get("BotnetList"), BotnetListDefinition),
            DnsCategory=deserialize_list(json_data.get("DnsCategory"), DnsCategoryDefinition),
            Exception=deserialize_list(json_data.get("Exception"), ExceptionDefinition),
            Rule=deserialize_list(json_data.get("Rule"), RuleDefinition),
            WhiteList=deserialize_list(json_data.get("WhiteList"), WhiteListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BotnetListDefinition(BaseModel):
    Action: Optional[str]
    Name: Optional[str]
    PacketCapture: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BotnetListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BotnetListDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Name=json_data.get("Name"),
            PacketCapture=json_data.get("PacketCapture"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BotnetListDefinition = BotnetListDefinition


@dataclass
class DnsCategoryDefinition(BaseModel):
    Action: Optional[str]
    LogLevel: Optional[str]
    Name: Optional[str]
    PacketCapture: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DnsCategoryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsCategoryDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            LogLevel=json_data.get("LogLevel"),
            Name=json_data.get("Name"),
            PacketCapture=json_data.get("PacketCapture"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsCategoryDefinition = DnsCategoryDefinition


@dataclass
class ExceptionDefinition(BaseModel):
    Action: Optional[str]
    BlockIpDuration: Optional[float]
    BlockIpTrackBy: Optional[str]
    ExemptIps: Optional[Sequence[str]]
    Name: Optional[str]
    PacketCapture: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExceptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExceptionDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            BlockIpDuration=json_data.get("BlockIpDuration"),
            BlockIpTrackBy=json_data.get("BlockIpTrackBy"),
            ExemptIps=json_data.get("ExemptIps"),
            Name=json_data.get("Name"),
            PacketCapture=json_data.get("PacketCapture"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExceptionDefinition = ExceptionDefinition


@dataclass
class RuleDefinition(BaseModel):
    Action: Optional[str]
    BlockIpDuration: Optional[float]
    BlockIpTrackBy: Optional[str]
    Category: Optional[str]
    Name: Optional[str]
    PacketCapture: Optional[str]
    Severities: Optional[Sequence[str]]
    ThreatName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            BlockIpDuration=json_data.get("BlockIpDuration"),
            BlockIpTrackBy=json_data.get("BlockIpTrackBy"),
            Category=json_data.get("Category"),
            Name=json_data.get("Name"),
            PacketCapture=json_data.get("PacketCapture"),
            Severities=json_data.get("Severities"),
            ThreatName=json_data.get("ThreatName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleDefinition = RuleDefinition


@dataclass
class WhiteListDefinition(BaseModel):
    Description: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WhiteListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WhiteListDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WhiteListDefinition = WhiteListDefinition


