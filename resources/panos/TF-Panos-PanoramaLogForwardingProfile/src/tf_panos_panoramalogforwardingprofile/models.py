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
    EnhancedLogging: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    MatchList: Optional[Sequence["_MatchListDefinition"]]

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
            EnhancedLogging=json_data.get("EnhancedLogging"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            MatchList=deserialize_list(json_data.get("MatchList"), MatchListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MatchListDefinition(BaseModel):
    Description: Optional[str]
    EmailServerProfiles: Optional[Sequence[str]]
    Filter: Optional[str]
    HttpServerProfiles: Optional[Sequence[str]]
    LogType: Optional[str]
    Name: Optional[str]
    SendToPanorama: Optional[bool]
    SnmptrapServerProfiles: Optional[Sequence[str]]
    SyslogServerProfiles: Optional[Sequence[str]]
    Action: Optional[Sequence["_ActionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchListDefinition"]:
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
            Action=deserialize_list(json_data.get("Action"), ActionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchListDefinition = MatchListDefinition


@dataclass
class ActionDefinition(BaseModel):
    Name: Optional[str]
    AzureIntegration: Optional[Sequence["_AzureIntegrationDefinition"]]
    TaggingIntegration: Optional[Sequence["_TaggingIntegrationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            AzureIntegration=deserialize_list(json_data.get("AzureIntegration"), AzureIntegrationDefinition),
            TaggingIntegration=deserialize_list(json_data.get("TaggingIntegration"), TaggingIntegrationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionDefinition = ActionDefinition


@dataclass
class AzureIntegrationDefinition(BaseModel):
    AzureIntegration: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AzureIntegrationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureIntegrationDefinition"]:
        if not json_data:
            return None
        return cls(
            AzureIntegration=json_data.get("AzureIntegration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureIntegrationDefinition = AzureIntegrationDefinition


@dataclass
class TaggingIntegrationDefinition(BaseModel):
    Action: Optional[str]
    Target: Optional[str]
    Timeout: Optional[float]
    LocalRegistration: Optional[Sequence["_LocalRegistrationDefinition"]]
    PanoramaRegistration: Optional[Sequence["_PanoramaRegistrationDefinition"]]
    RemoteRegistration: Optional[Sequence["_RemoteRegistrationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TaggingIntegrationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaggingIntegrationDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Target=json_data.get("Target"),
            Timeout=json_data.get("Timeout"),
            LocalRegistration=deserialize_list(json_data.get("LocalRegistration"), LocalRegistrationDefinition),
            PanoramaRegistration=deserialize_list(json_data.get("PanoramaRegistration"), PanoramaRegistrationDefinition),
            RemoteRegistration=deserialize_list(json_data.get("RemoteRegistration"), RemoteRegistrationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaggingIntegrationDefinition = TaggingIntegrationDefinition


@dataclass
class LocalRegistrationDefinition(BaseModel):
    Tags: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_LocalRegistrationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocalRegistrationDefinition"]:
        if not json_data:
            return None
        return cls(
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocalRegistrationDefinition = LocalRegistrationDefinition


@dataclass
class PanoramaRegistrationDefinition(BaseModel):
    Tags: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PanoramaRegistrationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PanoramaRegistrationDefinition"]:
        if not json_data:
            return None
        return cls(
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PanoramaRegistrationDefinition = PanoramaRegistrationDefinition


@dataclass
class RemoteRegistrationDefinition(BaseModel):
    HttpProfile: Optional[str]
    Tags: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RemoteRegistrationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RemoteRegistrationDefinition"]:
        if not json_data:
            return None
        return cls(
            HttpProfile=json_data.get("HttpProfile"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RemoteRegistrationDefinition = RemoteRegistrationDefinition


