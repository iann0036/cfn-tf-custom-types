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
    TriggerMode: Optional[str]
    TriggerTypes: Optional[Sequence[str]]
    UpdatedAt: Optional[str]
    AlertSource: Optional[Sequence["_AlertSourceDefinition"]]
    Autotask: Optional[Sequence["_AutotaskDefinition"]]
    AwsLambda: Optional[Sequence["_AwsLambdaDefinition"]]
    AzureFaas: Optional[Sequence["_AzureFaasDefinition"]]
    Connector: Optional[Sequence["_ConnectorDefinition"]]
    Datadog: Optional[Sequence["_DatadogDefinition"]]
    Email: Optional[Sequence["_EmailDefinition"]]
    Github: Optional[Sequence["_GithubDefinition"]]
    GoogleFaas: Optional[Sequence["_GoogleFaasDefinition"]]
    Jira: Optional[Sequence["_JiraDefinition"]]
    Servicenow: Optional[Sequence["_ServicenowDefinition"]]
    Slack: Optional[Sequence["_SlackDefinition"]]
    StatusPageIo: Optional[Sequence["_StatusPageIoDefinition"]]
    Sysdig: Optional[Sequence["_SysdigDefinition"]]
    Topdesk: Optional[Sequence["_TopdeskDefinition"]]
    Webhook: Optional[Sequence["_WebhookDefinition"]]
    Zammad: Optional[Sequence["_ZammadDefinition"]]
    Zapier: Optional[Sequence["_ZapierDefinition"]]
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
            TriggerMode=json_data.get("TriggerMode"),
            TriggerTypes=json_data.get("TriggerTypes"),
            UpdatedAt=json_data.get("UpdatedAt"),
            AlertSource=deserialize_list(json_data.get("AlertSource"), AlertSourceDefinition),
            Autotask=deserialize_list(json_data.get("Autotask"), AutotaskDefinition),
            AwsLambda=deserialize_list(json_data.get("AwsLambda"), AwsLambdaDefinition),
            AzureFaas=deserialize_list(json_data.get("AzureFaas"), AzureFaasDefinition),
            Connector=deserialize_list(json_data.get("Connector"), ConnectorDefinition),
            Datadog=deserialize_list(json_data.get("Datadog"), DatadogDefinition),
            Email=deserialize_list(json_data.get("Email"), EmailDefinition),
            Github=deserialize_list(json_data.get("Github"), GithubDefinition),
            GoogleFaas=deserialize_list(json_data.get("GoogleFaas"), GoogleFaasDefinition),
            Jira=deserialize_list(json_data.get("Jira"), JiraDefinition),
            Servicenow=deserialize_list(json_data.get("Servicenow"), ServicenowDefinition),
            Slack=deserialize_list(json_data.get("Slack"), SlackDefinition),
            StatusPageIo=deserialize_list(json_data.get("StatusPageIo"), StatusPageIoDefinition),
            Sysdig=deserialize_list(json_data.get("Sysdig"), SysdigDefinition),
            Topdesk=deserialize_list(json_data.get("Topdesk"), TopdeskDefinition),
            Webhook=deserialize_list(json_data.get("Webhook"), WebhookDefinition),
            Zammad=deserialize_list(json_data.get("Zammad"), ZammadDefinition),
            Zapier=deserialize_list(json_data.get("Zapier"), ZapierDefinition),
            Zendesk=deserialize_list(json_data.get("Zendesk"), ZendeskDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AlertSourceDefinition(BaseModel):
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AlertSourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlertSourceDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlertSourceDefinition = AlertSourceDefinition


@dataclass
class AutotaskDefinition(BaseModel):
    CompanyId: Optional[str]
    IssueType: Optional[str]
    QueueId: Optional[float]
    TicketCategory: Optional[str]
    TicketType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AutotaskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutotaskDefinition"]:
        if not json_data:
            return None
        return cls(
            CompanyId=json_data.get("CompanyId"),
            IssueType=json_data.get("IssueType"),
            QueueId=json_data.get("QueueId"),
            TicketCategory=json_data.get("TicketCategory"),
            TicketType=json_data.get("TicketType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutotaskDefinition = AutotaskDefinition


@dataclass
class AwsLambdaDefinition(BaseModel):
    BodyTemplate: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLambdaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLambdaDefinition"]:
        if not json_data:
            return None
        return cls(
            BodyTemplate=json_data.get("BodyTemplate"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLambdaDefinition = AwsLambdaDefinition


@dataclass
class AzureFaasDefinition(BaseModel):
    BodyTemplate: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureFaasDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureFaasDefinition"]:
        if not json_data:
            return None
        return cls(
            BodyTemplate=json_data.get("BodyTemplate"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureFaasDefinition = AzureFaasDefinition


@dataclass
class ConnectorDefinition(BaseModel):
    Id: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectorDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectorDefinition = ConnectorDefinition


@dataclass
class DatadogDefinition(BaseModel):
    Priority: Optional[str]
    Site: Optional[str]
    Tags: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DatadogDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatadogDefinition"]:
        if not json_data:
            return None
        return cls(
            Priority=json_data.get("Priority"),
            Site=json_data.get("Site"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatadogDefinition = DatadogDefinition


@dataclass
class EmailDefinition(BaseModel):
    BodyTemplate: Optional[str]
    Recipients: Optional[Sequence[str]]
    Subject: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EmailDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EmailDefinition"]:
        if not json_data:
            return None
        return cls(
            BodyTemplate=json_data.get("BodyTemplate"),
            Recipients=json_data.get("Recipients"),
            Subject=json_data.get("Subject"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EmailDefinition = EmailDefinition


@dataclass
class GithubDefinition(BaseModel):
    Labels: Optional[Sequence[str]]
    Owner: Optional[str]
    Repository: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GithubDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GithubDefinition"]:
        if not json_data:
            return None
        return cls(
            Labels=json_data.get("Labels"),
            Owner=json_data.get("Owner"),
            Repository=json_data.get("Repository"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GithubDefinition = GithubDefinition


@dataclass
class GoogleFaasDefinition(BaseModel):
    BodyTemplate: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GoogleFaasDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GoogleFaasDefinition"]:
        if not json_data:
            return None
        return cls(
            BodyTemplate=json_data.get("BodyTemplate"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GoogleFaasDefinition = GoogleFaasDefinition


@dataclass
class JiraDefinition(BaseModel):
    BodyTemplate: Optional[str]
    IssueType: Optional[str]
    Project: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JiraDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JiraDefinition"]:
        if not json_data:
            return None
        return cls(
            BodyTemplate=json_data.get("BodyTemplate"),
            IssueType=json_data.get("IssueType"),
            Project=json_data.get("Project"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JiraDefinition = JiraDefinition


@dataclass
class ServicenowDefinition(BaseModel):
    CallerId: Optional[str]
    Impact: Optional[str]
    Urgency: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServicenowDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServicenowDefinition"]:
        if not json_data:
            return None
        return cls(
            CallerId=json_data.get("CallerId"),
            Impact=json_data.get("Impact"),
            Urgency=json_data.get("Urgency"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServicenowDefinition = ServicenowDefinition


@dataclass
class SlackDefinition(BaseModel):
    ChannelId: Optional[str]
    ChannelName: Optional[str]
    TeamDomain: Optional[str]
    TeamId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SlackDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SlackDefinition"]:
        if not json_data:
            return None
        return cls(
            ChannelId=json_data.get("ChannelId"),
            ChannelName=json_data.get("ChannelName"),
            TeamDomain=json_data.get("TeamDomain"),
            TeamId=json_data.get("TeamId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SlackDefinition = SlackDefinition


@dataclass
class StatusPageIoDefinition(BaseModel):
    PageId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StatusPageIoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatusPageIoDefinition"]:
        if not json_data:
            return None
        return cls(
            PageId=json_data.get("PageId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatusPageIoDefinition = StatusPageIoDefinition


@dataclass
class SysdigDefinition(BaseModel):
    EventFilter: Optional[str]
    Tags: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SysdigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SysdigDefinition"]:
        if not json_data:
            return None
        return cls(
            EventFilter=json_data.get("EventFilter"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SysdigDefinition = SysdigDefinition


@dataclass
class TopdeskDefinition(BaseModel):
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TopdeskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TopdeskDefinition"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TopdeskDefinition = TopdeskDefinition


@dataclass
class WebhookDefinition(BaseModel):
    BodyTemplate: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WebhookDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebhookDefinition"]:
        if not json_data:
            return None
        return cls(
            BodyTemplate=json_data.get("BodyTemplate"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebhookDefinition = WebhookDefinition


@dataclass
class ZammadDefinition(BaseModel):
    Email: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ZammadDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ZammadDefinition"]:
        if not json_data:
            return None
        return cls(
            Email=json_data.get("Email"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ZammadDefinition = ZammadDefinition


@dataclass
class ZapierDefinition(BaseModel):
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ZapierDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ZapierDefinition"]:
        if not json_data:
            return None
        return cls(
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ZapierDefinition = ZapierDefinition


@dataclass
class ZendeskDefinition(BaseModel):
    Priority: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ZendeskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ZendeskDefinition"]:
        if not json_data:
            return None
        return cls(
            Priority=json_data.get("Priority"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ZendeskDefinition = ZendeskDefinition


