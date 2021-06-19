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
    BlockedConnection: Optional[str]
    BotnetConnectionDetected: Optional[str]
    DynamicSortSubtable: Optional[str]
    FailedConnection: Optional[str]
    Id: Optional[str]
    Status: Optional[str]
    UrlBlockDetected: Optional[str]
    Vdomparam: Optional[str]
    Application: Optional[Sequence["_ApplicationDefinition"]]
    Geolocation: Optional[Sequence["_GeolocationDefinition"]]
    Ips: Optional[Sequence["_IpsDefinition"]]
    Level: Optional[Sequence["_LevelDefinition"]]
    Malware: Optional[Sequence["_MalwareDefinition"]]
    Web: Optional[Sequence["_WebDefinition"]]

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
            BlockedConnection=json_data.get("BlockedConnection"),
            BotnetConnectionDetected=json_data.get("BotnetConnectionDetected"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            FailedConnection=json_data.get("FailedConnection"),
            Id=json_data.get("Id"),
            Status=json_data.get("Status"),
            UrlBlockDetected=json_data.get("UrlBlockDetected"),
            Vdomparam=json_data.get("Vdomparam"),
            Application=deserialize_list(json_data.get("Application"), ApplicationDefinition),
            Geolocation=deserialize_list(json_data.get("Geolocation"), GeolocationDefinition),
            Ips=deserialize_list(json_data.get("Ips"), IpsDefinition),
            Level=deserialize_list(json_data.get("Level"), LevelDefinition),
            Malware=deserialize_list(json_data.get("Malware"), MalwareDefinition),
            Web=deserialize_list(json_data.get("Web"), WebDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ApplicationDefinition(BaseModel):
    Category: Optional[float]
    Id: Optional[float]
    Level: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationDefinition"]:
        if not json_data:
            return None
        return cls(
            Category=json_data.get("Category"),
            Id=json_data.get("Id"),
            Level=json_data.get("Level"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationDefinition = ApplicationDefinition


@dataclass
class GeolocationDefinition(BaseModel):
    Country: Optional[str]
    Id: Optional[float]
    Level: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GeolocationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeolocationDefinition"]:
        if not json_data:
            return None
        return cls(
            Country=json_data.get("Country"),
            Id=json_data.get("Id"),
            Level=json_data.get("Level"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeolocationDefinition = GeolocationDefinition


@dataclass
class IpsDefinition(BaseModel):
    CriticalSeverity: Optional[str]
    HighSeverity: Optional[str]
    InfoSeverity: Optional[str]
    LowSeverity: Optional[str]
    MediumSeverity: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpsDefinition"]:
        if not json_data:
            return None
        return cls(
            CriticalSeverity=json_data.get("CriticalSeverity"),
            HighSeverity=json_data.get("HighSeverity"),
            InfoSeverity=json_data.get("InfoSeverity"),
            LowSeverity=json_data.get("LowSeverity"),
            MediumSeverity=json_data.get("MediumSeverity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpsDefinition = IpsDefinition


@dataclass
class LevelDefinition(BaseModel):
    Critical: Optional[float]
    High: Optional[float]
    Low: Optional[float]
    Medium: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_LevelDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LevelDefinition"]:
        if not json_data:
            return None
        return cls(
            Critical=json_data.get("Critical"),
            High=json_data.get("High"),
            Low=json_data.get("Low"),
            Medium=json_data.get("Medium"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LevelDefinition = LevelDefinition


@dataclass
class MalwareDefinition(BaseModel):
    BotnetConnection: Optional[str]
    CommandBlocked: Optional[str]
    ContentDisarm: Optional[str]
    FileBlocked: Optional[str]
    FsaHighRisk: Optional[str]
    FsaMalicious: Optional[str]
    FsaMediumRisk: Optional[str]
    MalwareList: Optional[str]
    Mimefragmented: Optional[str]
    Oversized: Optional[str]
    SwitchProto: Optional[str]
    VirusFileTypeExecutable: Optional[str]
    VirusInfected: Optional[str]
    VirusOutbreakPrevention: Optional[str]
    VirusScanError: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MalwareDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MalwareDefinition"]:
        if not json_data:
            return None
        return cls(
            BotnetConnection=json_data.get("BotnetConnection"),
            CommandBlocked=json_data.get("CommandBlocked"),
            ContentDisarm=json_data.get("ContentDisarm"),
            FileBlocked=json_data.get("FileBlocked"),
            FsaHighRisk=json_data.get("FsaHighRisk"),
            FsaMalicious=json_data.get("FsaMalicious"),
            FsaMediumRisk=json_data.get("FsaMediumRisk"),
            MalwareList=json_data.get("MalwareList"),
            Mimefragmented=json_data.get("Mimefragmented"),
            Oversized=json_data.get("Oversized"),
            SwitchProto=json_data.get("SwitchProto"),
            VirusFileTypeExecutable=json_data.get("VirusFileTypeExecutable"),
            VirusInfected=json_data.get("VirusInfected"),
            VirusOutbreakPrevention=json_data.get("VirusOutbreakPrevention"),
            VirusScanError=json_data.get("VirusScanError"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MalwareDefinition = MalwareDefinition


@dataclass
class WebDefinition(BaseModel):
    Category: Optional[float]
    Id: Optional[float]
    Level: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WebDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebDefinition"]:
        if not json_data:
            return None
        return cls(
            Category=json_data.get("Category"),
            Id=json_data.get("Id"),
            Level=json_data.get("Level"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebDefinition = WebDefinition


