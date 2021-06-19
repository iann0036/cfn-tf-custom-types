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
    Id: Optional[str]
    AnsibleTower: Optional[Sequence["_AnsibleTowerDefinition"]]
    Config: Optional[Sequence["_ConfigDefinition"]]
    Email: Optional[Sequence["_EmailDefinition"]]
    Hipchat: Optional[Sequence["_HipchatDefinition"]]
    Jira: Optional[Sequence["_JiraDefinition"]]
    OpsGenie: Optional[Sequence["_OpsGenieDefinition"]]
    PagerDuty: Optional[Sequence["_PagerDutyDefinition"]]
    ServiceNow: Optional[Sequence["_ServiceNowDefinition"]]
    Slack: Optional[Sequence["_SlackDefinition"]]
    Trello: Optional[Sequence["_TrelloDefinition"]]
    VictorOps: Optional[Sequence["_VictorOpsDefinition"]]
    WebHook: Optional[Sequence["_WebHookDefinition"]]
    Xmatters: Optional[Sequence["_XmattersDefinition"]]

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
            Id=json_data.get("Id"),
            AnsibleTower=deserialize_list(json_data.get("AnsibleTower"), AnsibleTowerDefinition),
            Config=deserialize_list(json_data.get("Config"), ConfigDefinition),
            Email=deserialize_list(json_data.get("Email"), EmailDefinition),
            Hipchat=deserialize_list(json_data.get("Hipchat"), HipchatDefinition),
            Jira=deserialize_list(json_data.get("Jira"), JiraDefinition),
            OpsGenie=deserialize_list(json_data.get("OpsGenie"), OpsGenieDefinition),
            PagerDuty=deserialize_list(json_data.get("PagerDuty"), PagerDutyDefinition),
            ServiceNow=deserialize_list(json_data.get("ServiceNow"), ServiceNowDefinition),
            Slack=deserialize_list(json_data.get("Slack"), SlackDefinition),
            Trello=deserialize_list(json_data.get("Trello"), TrelloDefinition),
            VictorOps=deserialize_list(json_data.get("VictorOps"), VictorOpsDefinition),
            WebHook=deserialize_list(json_data.get("WebHook"), WebHookDefinition),
            Xmatters=deserialize_list(json_data.get("Xmatters"), XmattersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AnsibleTowerDefinition(BaseModel):
    AcceptAnyCertificate: Optional[bool]
    Active: Optional[bool]
    AlertingProfile: Optional[str]
    CustomMessage: Optional[str]
    JobTemplateId: Optional[float]
    JobTemplateUrl: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Unknowns: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnsibleTowerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnsibleTowerDefinition"]:
        if not json_data:
            return None
        return cls(
            AcceptAnyCertificate=json_data.get("AcceptAnyCertificate"),
            Active=json_data.get("Active"),
            AlertingProfile=json_data.get("AlertingProfile"),
            CustomMessage=json_data.get("CustomMessage"),
            JobTemplateId=json_data.get("JobTemplateId"),
            JobTemplateUrl=json_data.get("JobTemplateUrl"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Unknowns=json_data.get("Unknowns"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnsibleTowerDefinition = AnsibleTowerDefinition


@dataclass
class ConfigDefinition(BaseModel):
    Active: Optional[bool]
    AlertingProfile: Optional[str]
    Name: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Active=json_data.get("Active"),
            AlertingProfile=json_data.get("AlertingProfile"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigDefinition = ConfigDefinition


@dataclass
class EmailDefinition(BaseModel):
    Active: Optional[bool]
    AlertingProfile: Optional[str]
    BccReceivers: Optional[Sequence[str]]
    Body: Optional[str]
    CcReceivers: Optional[Sequence[str]]
    Name: Optional[str]
    Receivers: Optional[Sequence[str]]
    Subject: Optional[str]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EmailDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EmailDefinition"]:
        if not json_data:
            return None
        return cls(
            Active=json_data.get("Active"),
            AlertingProfile=json_data.get("AlertingProfile"),
            BccReceivers=json_data.get("BccReceivers"),
            Body=json_data.get("Body"),
            CcReceivers=json_data.get("CcReceivers"),
            Name=json_data.get("Name"),
            Receivers=json_data.get("Receivers"),
            Subject=json_data.get("Subject"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EmailDefinition = EmailDefinition


@dataclass
class HipchatDefinition(BaseModel):
    Active: Optional[bool]
    AlertingProfile: Optional[str]
    Message: Optional[str]
    Name: Optional[str]
    Unknowns: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HipchatDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HipchatDefinition"]:
        if not json_data:
            return None
        return cls(
            Active=json_data.get("Active"),
            AlertingProfile=json_data.get("AlertingProfile"),
            Message=json_data.get("Message"),
            Name=json_data.get("Name"),
            Unknowns=json_data.get("Unknowns"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HipchatDefinition = HipchatDefinition


@dataclass
class JiraDefinition(BaseModel):
    Active: Optional[bool]
    AlertingProfile: Optional[str]
    Description: Optional[str]
    IssueType: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    ProjectKey: Optional[str]
    Summary: Optional[str]
    Unknowns: Optional[str]
    Url: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JiraDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JiraDefinition"]:
        if not json_data:
            return None
        return cls(
            Active=json_data.get("Active"),
            AlertingProfile=json_data.get("AlertingProfile"),
            Description=json_data.get("Description"),
            IssueType=json_data.get("IssueType"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            ProjectKey=json_data.get("ProjectKey"),
            Summary=json_data.get("Summary"),
            Unknowns=json_data.get("Unknowns"),
            Url=json_data.get("Url"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JiraDefinition = JiraDefinition


@dataclass
class OpsGenieDefinition(BaseModel):
    Active: Optional[bool]
    AlertingProfile: Optional[str]
    ApiKey: Optional[str]
    Domain: Optional[str]
    Message: Optional[str]
    Name: Optional[str]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OpsGenieDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OpsGenieDefinition"]:
        if not json_data:
            return None
        return cls(
            Active=json_data.get("Active"),
            AlertingProfile=json_data.get("AlertingProfile"),
            ApiKey=json_data.get("ApiKey"),
            Domain=json_data.get("Domain"),
            Message=json_data.get("Message"),
            Name=json_data.get("Name"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OpsGenieDefinition = OpsGenieDefinition


@dataclass
class PagerDutyDefinition(BaseModel):
    Account: Optional[str]
    Active: Optional[bool]
    AlertingProfile: Optional[str]
    Name: Optional[str]
    ServiceApiKey: Optional[str]
    ServiceName: Optional[str]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PagerDutyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PagerDutyDefinition"]:
        if not json_data:
            return None
        return cls(
            Account=json_data.get("Account"),
            Active=json_data.get("Active"),
            AlertingProfile=json_data.get("AlertingProfile"),
            Name=json_data.get("Name"),
            ServiceApiKey=json_data.get("ServiceApiKey"),
            ServiceName=json_data.get("ServiceName"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PagerDutyDefinition = PagerDutyDefinition


@dataclass
class ServiceNowDefinition(BaseModel):
    Active: Optional[bool]
    AlertingProfile: Optional[str]
    InstanceName: Optional[str]
    Message: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    SendEvents: Optional[bool]
    SendIncidents: Optional[bool]
    Unknowns: Optional[str]
    Url: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceNowDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceNowDefinition"]:
        if not json_data:
            return None
        return cls(
            Active=json_data.get("Active"),
            AlertingProfile=json_data.get("AlertingProfile"),
            InstanceName=json_data.get("InstanceName"),
            Message=json_data.get("Message"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            SendEvents=json_data.get("SendEvents"),
            SendIncidents=json_data.get("SendIncidents"),
            Unknowns=json_data.get("Unknowns"),
            Url=json_data.get("Url"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceNowDefinition = ServiceNowDefinition


@dataclass
class SlackDefinition(BaseModel):
    Active: Optional[bool]
    AlertingProfile: Optional[str]
    Channel: Optional[str]
    Name: Optional[str]
    Title: Optional[str]
    Unknowns: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SlackDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SlackDefinition"]:
        if not json_data:
            return None
        return cls(
            Active=json_data.get("Active"),
            AlertingProfile=json_data.get("AlertingProfile"),
            Channel=json_data.get("Channel"),
            Name=json_data.get("Name"),
            Title=json_data.get("Title"),
            Unknowns=json_data.get("Unknowns"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SlackDefinition = SlackDefinition


@dataclass
class TrelloDefinition(BaseModel):
    Active: Optional[bool]
    AlertingProfile: Optional[str]
    ApplicationKey: Optional[str]
    AuthorizationToken: Optional[str]
    BoardId: Optional[str]
    Description: Optional[str]
    ListId: Optional[str]
    Name: Optional[str]
    ResolvedListId: Optional[str]
    Text: Optional[str]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TrelloDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrelloDefinition"]:
        if not json_data:
            return None
        return cls(
            Active=json_data.get("Active"),
            AlertingProfile=json_data.get("AlertingProfile"),
            ApplicationKey=json_data.get("ApplicationKey"),
            AuthorizationToken=json_data.get("AuthorizationToken"),
            BoardId=json_data.get("BoardId"),
            Description=json_data.get("Description"),
            ListId=json_data.get("ListId"),
            Name=json_data.get("Name"),
            ResolvedListId=json_data.get("ResolvedListId"),
            Text=json_data.get("Text"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrelloDefinition = TrelloDefinition


@dataclass
class VictorOpsDefinition(BaseModel):
    Active: Optional[bool]
    AlertingProfile: Optional[str]
    ApiKey: Optional[str]
    Message: Optional[str]
    Name: Optional[str]
    RoutingKey: Optional[str]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VictorOpsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VictorOpsDefinition"]:
        if not json_data:
            return None
        return cls(
            Active=json_data.get("Active"),
            AlertingProfile=json_data.get("AlertingProfile"),
            ApiKey=json_data.get("ApiKey"),
            Message=json_data.get("Message"),
            Name=json_data.get("Name"),
            RoutingKey=json_data.get("RoutingKey"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VictorOpsDefinition = VictorOpsDefinition


@dataclass
class WebHookDefinition(BaseModel):
    AcceptAnyCertificate: Optional[bool]
    Active: Optional[bool]
    AlertingProfile: Optional[str]
    Name: Optional[str]
    NotifyEventMerges: Optional[bool]
    Payload: Optional[str]
    Unknowns: Optional[str]
    Url: Optional[str]
    Header: Optional[Sequence["_HeaderDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WebHookDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebHookDefinition"]:
        if not json_data:
            return None
        return cls(
            AcceptAnyCertificate=json_data.get("AcceptAnyCertificate"),
            Active=json_data.get("Active"),
            AlertingProfile=json_data.get("AlertingProfile"),
            Name=json_data.get("Name"),
            NotifyEventMerges=json_data.get("NotifyEventMerges"),
            Payload=json_data.get("Payload"),
            Unknowns=json_data.get("Unknowns"),
            Url=json_data.get("Url"),
            Header=deserialize_list(json_data.get("Header"), HeaderDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebHookDefinition = WebHookDefinition


@dataclass
class HeaderDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeaderDefinition = HeaderDefinition


@dataclass
class XmattersDefinition(BaseModel):
    AcceptAnyCertificate: Optional[bool]
    Active: Optional[bool]
    AlertingProfile: Optional[str]
    Name: Optional[str]
    Payload: Optional[str]
    Unknowns: Optional[str]
    Url: Optional[str]
    Header: Optional[Sequence["_HeaderDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_XmattersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_XmattersDefinition"]:
        if not json_data:
            return None
        return cls(
            AcceptAnyCertificate=json_data.get("AcceptAnyCertificate"),
            Active=json_data.get("Active"),
            AlertingProfile=json_data.get("AlertingProfile"),
            Name=json_data.get("Name"),
            Payload=json_data.get("Payload"),
            Unknowns=json_data.get("Unknowns"),
            Url=json_data.get("Url"),
            Header=deserialize_list(json_data.get("Header"), HeaderDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_XmattersDefinition = XmattersDefinition


