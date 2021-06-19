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
    CreatedAt: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Type: Optional[str]
    UpdatedAt: Optional[str]
    Autotask: Optional[Sequence["_AutotaskDefinition"]]
    AwsLambda: Optional[Sequence["_AwsLambdaDefinition"]]
    AzureFaas: Optional[Sequence["_AzureFaasDefinition"]]
    Datadog: Optional[Sequence["_DatadogDefinition"]]
    Discord: Optional[Sequence["_DiscordDefinition"]]
    Github: Optional[Sequence["_GithubDefinition"]]
    GoogleFaas: Optional[Sequence["_GoogleFaasDefinition"]]
    Jira: Optional[Sequence["_JiraDefinition"]]
    Mattermost: Optional[Sequence["_MattermostDefinition"]]
    MicrosoftTeams: Optional[Sequence["_MicrosoftTeamsDefinition"]]
    Servicenow: Optional[Sequence["_ServicenowDefinition"]]
    StatusPageIo: Optional[Sequence["_StatusPageIoDefinition"]]
    Sysdig: Optional[Sequence["_SysdigDefinition"]]
    Topdesk: Optional[Sequence["_TopdeskDefinition"]]
    Zammad: Optional[Sequence["_ZammadDefinition"]]
    Zendesk: Optional[Sequence["_ZendeskDefinition"]]

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
            CreatedAt=json_data.get("CreatedAt"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            UpdatedAt=json_data.get("UpdatedAt"),
            Autotask=deserialize_list(json_data.get("Autotask"), AutotaskDefinition),
            AwsLambda=deserialize_list(json_data.get("AwsLambda"), AwsLambdaDefinition),
            AzureFaas=deserialize_list(json_data.get("AzureFaas"), AzureFaasDefinition),
            Datadog=deserialize_list(json_data.get("Datadog"), DatadogDefinition),
            Discord=deserialize_list(json_data.get("Discord"), DiscordDefinition),
            Github=deserialize_list(json_data.get("Github"), GithubDefinition),
            GoogleFaas=deserialize_list(json_data.get("GoogleFaas"), GoogleFaasDefinition),
            Jira=deserialize_list(json_data.get("Jira"), JiraDefinition),
            Mattermost=deserialize_list(json_data.get("Mattermost"), MattermostDefinition),
            MicrosoftTeams=deserialize_list(json_data.get("MicrosoftTeams"), MicrosoftTeamsDefinition),
            Servicenow=deserialize_list(json_data.get("Servicenow"), ServicenowDefinition),
            StatusPageIo=deserialize_list(json_data.get("StatusPageIo"), StatusPageIoDefinition),
            Sysdig=deserialize_list(json_data.get("Sysdig"), SysdigDefinition),
            Topdesk=deserialize_list(json_data.get("Topdesk"), TopdeskDefinition),
            Zammad=deserialize_list(json_data.get("Zammad"), ZammadDefinition),
            Zendesk=deserialize_list(json_data.get("Zendesk"), ZendeskDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AutotaskDefinition(BaseModel):
    Email: Optional[str]
    Password: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AutotaskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutotaskDefinition"]:
        if not json_data:
            return None
        return cls(
            Email=json_data.get("Email"),
            Password=json_data.get("Password"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutotaskDefinition = AutotaskDefinition


@dataclass
class AwsLambdaDefinition(BaseModel):
    Authorization: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLambdaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLambdaDefinition"]:
        if not json_data:
            return None
        return cls(
            Authorization=json_data.get("Authorization"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLambdaDefinition = AwsLambdaDefinition


@dataclass
class AzureFaasDefinition(BaseModel):
    Authorization: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureFaasDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureFaasDefinition"]:
        if not json_data:
            return None
        return cls(
            Authorization=json_data.get("Authorization"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureFaasDefinition = AzureFaasDefinition


@dataclass
class DatadogDefinition(BaseModel):
    ApiKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DatadogDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatadogDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiKey=json_data.get("ApiKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatadogDefinition = DatadogDefinition


@dataclass
class DiscordDefinition(BaseModel):
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DiscordDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiscordDefinition"]:
        if not json_data:
            return None
        return cls(
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiscordDefinition = DiscordDefinition


@dataclass
class GithubDefinition(BaseModel):
    ApiKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GithubDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GithubDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiKey=json_data.get("ApiKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GithubDefinition = GithubDefinition


@dataclass
class GoogleFaasDefinition(BaseModel):
    Authorization: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GoogleFaasDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GoogleFaasDefinition"]:
        if not json_data:
            return None
        return cls(
            Authorization=json_data.get("Authorization"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GoogleFaasDefinition = GoogleFaasDefinition


@dataclass
class JiraDefinition(BaseModel):
    Email: Optional[str]
    Password: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JiraDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JiraDefinition"]:
        if not json_data:
            return None
        return cls(
            Email=json_data.get("Email"),
            Password=json_data.get("Password"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JiraDefinition = JiraDefinition


@dataclass
class MattermostDefinition(BaseModel):
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MattermostDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MattermostDefinition"]:
        if not json_data:
            return None
        return cls(
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MattermostDefinition = MattermostDefinition


@dataclass
class MicrosoftTeamsDefinition(BaseModel):
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MicrosoftTeamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MicrosoftTeamsDefinition"]:
        if not json_data:
            return None
        return cls(
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MicrosoftTeamsDefinition = MicrosoftTeamsDefinition


@dataclass
class ServicenowDefinition(BaseModel):
    Password: Optional[str]
    Url: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServicenowDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServicenowDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Url=json_data.get("Url"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServicenowDefinition = ServicenowDefinition


@dataclass
class StatusPageIoDefinition(BaseModel):
    ApiKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StatusPageIoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatusPageIoDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiKey=json_data.get("ApiKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatusPageIoDefinition = StatusPageIoDefinition


@dataclass
class SysdigDefinition(BaseModel):
    ApiKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SysdigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SysdigDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiKey=json_data.get("ApiKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SysdigDefinition = SysdigDefinition


@dataclass
class TopdeskDefinition(BaseModel):
    Password: Optional[str]
    Url: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TopdeskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TopdeskDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Url=json_data.get("Url"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TopdeskDefinition = TopdeskDefinition


@dataclass
class ZammadDefinition(BaseModel):
    ApiKey: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ZammadDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ZammadDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiKey=json_data.get("ApiKey"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ZammadDefinition = ZammadDefinition


@dataclass
class ZendeskDefinition(BaseModel):
    ApiKey: Optional[str]
    Email: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ZendeskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ZendeskDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiKey=json_data.get("ApiKey"),
            Email=json_data.get("Email"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ZendeskDefinition = ZendeskDefinition


