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
    AlertsConsole: Optional[bool]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    ChangeDetection: Optional[Sequence["_ChangeDetectionDefinition"]]
    GcpSecurityCommandCenterIntegration: Optional[Sequence["_GcpSecurityCommandCenterIntegrationDefinition"]]
    ScheduledReport: Optional[Sequence["_ScheduledReportDefinition"]]

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
            AlertsConsole=json_data.get("AlertsConsole"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ChangeDetection=deserialize_list(json_data.get("ChangeDetection"), ChangeDetectionDefinition),
            GcpSecurityCommandCenterIntegration=deserialize_list(json_data.get("GcpSecurityCommandCenterIntegration"), GcpSecurityCommandCenterIntegrationDefinition),
            ScheduledReport=deserialize_list(json_data.get("ScheduledReport"), ScheduledReportDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ChangeDetectionDefinition(BaseModel):
    AwsSecurityHubIntegrationState: Optional[str]
    EmailPerFindingSendingState: Optional[str]
    EmailSendingState: Optional[str]
    ExternalTicketCreatingState: Optional[str]
    SnsSendingState: Optional[str]
    WebhookIntegrationState: Optional[str]
    AwsSecurityHubIntegration: Optional[Sequence["_AwsSecurityHubIntegrationDefinition"]]
    EmailData: Optional[Sequence["_EmailDataDefinition"]]
    EmailPerFindingData: Optional[Sequence["_EmailPerFindingDataDefinition"]]
    SnsData: Optional[Sequence["_SnsDataDefinition"]]
    TicketingSystemData: Optional[Sequence["_TicketingSystemDataDefinition"]]
    WebhookData: Optional[Sequence["_WebhookDataDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ChangeDetectionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ChangeDetectionDefinition"]:
        if not json_data:
            return None
        return cls(
            AwsSecurityHubIntegrationState=json_data.get("AwsSecurityHubIntegrationState"),
            EmailPerFindingSendingState=json_data.get("EmailPerFindingSendingState"),
            EmailSendingState=json_data.get("EmailSendingState"),
            ExternalTicketCreatingState=json_data.get("ExternalTicketCreatingState"),
            SnsSendingState=json_data.get("SnsSendingState"),
            WebhookIntegrationState=json_data.get("WebhookIntegrationState"),
            AwsSecurityHubIntegration=deserialize_list(json_data.get("AwsSecurityHubIntegration"), AwsSecurityHubIntegrationDefinition),
            EmailData=deserialize_list(json_data.get("EmailData"), EmailDataDefinition),
            EmailPerFindingData=deserialize_list(json_data.get("EmailPerFindingData"), EmailPerFindingDataDefinition),
            SnsData=deserialize_list(json_data.get("SnsData"), SnsDataDefinition),
            TicketingSystemData=deserialize_list(json_data.get("TicketingSystemData"), TicketingSystemDataDefinition),
            WebhookData=deserialize_list(json_data.get("WebhookData"), WebhookDataDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ChangeDetectionDefinition = ChangeDetectionDefinition


@dataclass
class AwsSecurityHubIntegrationDefinition(BaseModel):
    ExternalAccountId: Optional[str]
    Region: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSecurityHubIntegrationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSecurityHubIntegrationDefinition"]:
        if not json_data:
            return None
        return cls(
            ExternalAccountId=json_data.get("ExternalAccountId"),
            Region=json_data.get("Region"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSecurityHubIntegrationDefinition = AwsSecurityHubIntegrationDefinition


@dataclass
class EmailDataDefinition(BaseModel):
    Recipients: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_EmailDataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EmailDataDefinition"]:
        if not json_data:
            return None
        return cls(
            Recipients=json_data.get("Recipients"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EmailDataDefinition = EmailDataDefinition


@dataclass
class EmailPerFindingDataDefinition(BaseModel):
    NotificationOutputFormat: Optional[str]
    Recipients: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_EmailPerFindingDataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EmailPerFindingDataDefinition"]:
        if not json_data:
            return None
        return cls(
            NotificationOutputFormat=json_data.get("NotificationOutputFormat"),
            Recipients=json_data.get("Recipients"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EmailPerFindingDataDefinition = EmailPerFindingDataDefinition


@dataclass
class SnsDataDefinition(BaseModel):
    SnsOutputFormat: Optional[str]
    SnsTopicArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnsDataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnsDataDefinition"]:
        if not json_data:
            return None
        return cls(
            SnsOutputFormat=json_data.get("SnsOutputFormat"),
            SnsTopicArn=json_data.get("SnsTopicArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnsDataDefinition = SnsDataDefinition


@dataclass
class TicketingSystemDataDefinition(BaseModel):
    Domain: Optional[str]
    IssueType: Optional[str]
    Pass: Optional[str]
    ProjectKey: Optional[str]
    ShouldCloseTickets: Optional[bool]
    SystemType: Optional[str]
    User: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TicketingSystemDataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TicketingSystemDataDefinition"]:
        if not json_data:
            return None
        return cls(
            Domain=json_data.get("Domain"),
            IssueType=json_data.get("IssueType"),
            Pass=json_data.get("Pass"),
            ProjectKey=json_data.get("ProjectKey"),
            ShouldCloseTickets=json_data.get("ShouldCloseTickets"),
            SystemType=json_data.get("SystemType"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TicketingSystemDataDefinition = TicketingSystemDataDefinition


@dataclass
class WebhookDataDefinition(BaseModel):
    AuthMethod: Optional[str]
    FormatType: Optional[str]
    HttpMethod: Optional[str]
    Password: Optional[str]
    Url: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WebhookDataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebhookDataDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthMethod=json_data.get("AuthMethod"),
            FormatType=json_data.get("FormatType"),
            HttpMethod=json_data.get("HttpMethod"),
            Password=json_data.get("Password"),
            Url=json_data.get("Url"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebhookDataDefinition = WebhookDataDefinition


@dataclass
class GcpSecurityCommandCenterIntegrationDefinition(BaseModel):
    ProjectId: Optional[str]
    SourceId: Optional[str]
    State: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GcpSecurityCommandCenterIntegrationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GcpSecurityCommandCenterIntegrationDefinition"]:
        if not json_data:
            return None
        return cls(
            ProjectId=json_data.get("ProjectId"),
            SourceId=json_data.get("SourceId"),
            State=json_data.get("State"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GcpSecurityCommandCenterIntegrationDefinition = GcpSecurityCommandCenterIntegrationDefinition


@dataclass
class ScheduledReportDefinition(BaseModel):
    EmailSendingState: Optional[str]
    ScheduleData: Optional[Sequence["_ScheduleDataDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduledReportDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduledReportDefinition"]:
        if not json_data:
            return None
        return cls(
            EmailSendingState=json_data.get("EmailSendingState"),
            ScheduleData=deserialize_list(json_data.get("ScheduleData"), ScheduleDataDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduledReportDefinition = ScheduledReportDefinition


@dataclass
class ScheduleDataDefinition(BaseModel):
    CronExpression: Optional[str]
    Recipients: Optional[Sequence[str]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduleDataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduleDataDefinition"]:
        if not json_data:
            return None
        return cls(
            CronExpression=json_data.get("CronExpression"),
            Recipients=json_data.get("Recipients"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduleDataDefinition = ScheduleDataDefinition


