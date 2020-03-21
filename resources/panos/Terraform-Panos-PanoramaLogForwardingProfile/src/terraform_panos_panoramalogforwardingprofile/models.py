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
    Description: Optional[str]
    DeviceGroup: Optional[str]
    EnhancedLogging: Optional[bool]
    Name: Optional[str]
    MatchList: Optional[Sequence["_MatchList"]]
    Action: Optional[Sequence["_Action"]]
    AzureIntegration: Optional[Sequence["_AzureIntegration"]]
    TaggingIntegration: Optional[Sequence["_TaggingIntegration"]]
    LocalRegistration: Optional[Sequence["_LocalRegistration"]]
    PanoramaRegistration: Optional[Sequence["_PanoramaRegistration"]]
    RemoteRegistration: Optional[Sequence["_RemoteRegistration"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            DeviceGroup=json_data.get("DeviceGroup"),
            EnhancedLogging=json_data.get("EnhancedLogging"),
            Name=json_data.get("Name"),
            MatchList=json_data.get("MatchList"),
            Action=json_data.get("Action"),
            AzureIntegration=json_data.get("AzureIntegration"),
            TaggingIntegration=json_data.get("TaggingIntegration"),
            LocalRegistration=json_data.get("LocalRegistration"),
            PanoramaRegistration=json_data.get("PanoramaRegistration"),
            RemoteRegistration=json_data.get("RemoteRegistration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MatchList:
    Description: Optional[str]
    EmailServerProfiles: Optional[Sequence[str]]
    Filter: Optional[str]
    HttpServerProfiles: Optional[Sequence[str]]
    LogType: Optional[str]
    Name: Optional[str]
    SendToPanorama: Optional[bool]
    SnmptrapServerProfiles: Optional[Sequence[str]]
    SyslogServerProfiles: Optional[Sequence[str]]
    Action: Optional[Sequence["_Action"]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchList"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchList"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            EmailServerProfiles=json_data.get("EmailServerProfiles"),
            Filter=json_data.get("Filter"),
            HttpServerProfiles=json_data.get("HttpServerProfiles"),
            LogType=json_data.get("LogType"),
            Name=json_data.get("Name"),
            SendToPanorama=json_data.get("SendToPanorama"),
            SnmptrapServerProfiles=json_data.get("SnmptrapServerProfiles"),
            SyslogServerProfiles=json_data.get("SyslogServerProfiles"),
            Action=json_data.get("Action"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchList = MatchList


@dataclass
class Action:
    Name: Optional[str]
    AzureIntegration: Optional[Sequence["_AzureIntegration"]]
    TaggingIntegration: Optional[Sequence["_TaggingIntegration"]]

    @classmethod
    def _deserialize(
        cls: Type["_Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Action"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            AzureIntegration=json_data.get("AzureIntegration"),
            TaggingIntegration=json_data.get("TaggingIntegration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Action = Action


@dataclass
class AzureIntegration:
    AzureIntegration: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AzureIntegration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureIntegration"]:
        if not json_data:
            return None
        return cls(
            AzureIntegration=json_data.get("AzureIntegration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureIntegration = AzureIntegration


@dataclass
class TaggingIntegration:
    Action: Optional[str]
    Target: Optional[str]
    Timeout: Optional[float]
    LocalRegistration: Optional[Sequence["_LocalRegistration"]]
    PanoramaRegistration: Optional[Sequence["_PanoramaRegistration"]]
    RemoteRegistration: Optional[Sequence["_RemoteRegistration"]]

    @classmethod
    def _deserialize(
        cls: Type["_TaggingIntegration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaggingIntegration"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Target=json_data.get("Target"),
            Timeout=json_data.get("Timeout"),
            LocalRegistration=json_data.get("LocalRegistration"),
            PanoramaRegistration=json_data.get("PanoramaRegistration"),
            RemoteRegistration=json_data.get("RemoteRegistration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaggingIntegration = TaggingIntegration


@dataclass
class LocalRegistration:
    Tags: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_LocalRegistration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocalRegistration"]:
        if not json_data:
            return None
        return cls(
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocalRegistration = LocalRegistration


@dataclass
class PanoramaRegistration:
    Tags: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PanoramaRegistration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PanoramaRegistration"]:
        if not json_data:
            return None
        return cls(
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PanoramaRegistration = PanoramaRegistration


@dataclass
class RemoteRegistration:
    HttpProfile: Optional[str]
    Tags: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RemoteRegistration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RemoteRegistration"]:
        if not json_data:
            return None
        return cls(
            HttpProfile=json_data.get("HttpProfile"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RemoteRegistration = RemoteRegistration


