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
    AggregationWindow: Optional[str]
    AlwaysSendClear: Optional[bool]
    GroupType: Optional[str]
    Id: Optional[str]
    LastModified: Optional[float]
    LastModifiedBy: Optional[str]
    LongMessage: Optional[str]
    LongSubject: Optional[str]
    LongSummary: Optional[str]
    Name: Optional[str]
    ShortMessage: Optional[str]
    ShortSummary: Optional[str]
    Tags: Optional[Sequence[str]]
    AlertOption: Optional[Sequence["_AlertOptionDefinition"]]
    Email: Optional[Sequence["_EmailDefinition"]]
    Http: Optional[Sequence["_HttpDefinition"]]
    PagerDuty: Optional[Sequence["_PagerDutyDefinition"]]
    Slack: Optional[Sequence["_SlackDefinition"]]
    Sms: Optional[Sequence["_SmsDefinition"]]
    Victorops: Optional[Sequence["_VictoropsDefinition"]]
    Xmpp: Optional[Sequence["_XmppDefinition"]]

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
            AggregationWindow=json_data.get("AggregationWindow"),
            AlwaysSendClear=json_data.get("AlwaysSendClear"),
            GroupType=json_data.get("GroupType"),
            Id=json_data.get("Id"),
            LastModified=json_data.get("LastModified"),
            LastModifiedBy=json_data.get("LastModifiedBy"),
            LongMessage=json_data.get("LongMessage"),
            LongSubject=json_data.get("LongSubject"),
            LongSummary=json_data.get("LongSummary"),
            Name=json_data.get("Name"),
            ShortMessage=json_data.get("ShortMessage"),
            ShortSummary=json_data.get("ShortSummary"),
            Tags=json_data.get("Tags"),
            AlertOption=deserialize_list(json_data.get("AlertOption"), AlertOptionDefinition),
            Email=deserialize_list(json_data.get("Email"), EmailDefinition),
            Http=deserialize_list(json_data.get("Http"), HttpDefinition),
            PagerDuty=deserialize_list(json_data.get("PagerDuty"), PagerDutyDefinition),
            Slack=deserialize_list(json_data.get("Slack"), SlackDefinition),
            Sms=deserialize_list(json_data.get("Sms"), SmsDefinition),
            Victorops=deserialize_list(json_data.get("Victorops"), VictoropsDefinition),
            Xmpp=deserialize_list(json_data.get("Xmpp"), XmppDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AlertOptionDefinition(BaseModel):
    EscalateAfter: Optional[str]
    EscalateTo: Optional[str]
    Reminder: Optional[str]
    Severity: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AlertOptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlertOptionDefinition"]:
        if not json_data:
            return None
        return cls(
            EscalateAfter=json_data.get("EscalateAfter"),
            EscalateTo=json_data.get("EscalateTo"),
            Reminder=json_data.get("Reminder"),
            Severity=json_data.get("Severity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlertOptionDefinition = AlertOptionDefinition


@dataclass
class EmailDefinition(BaseModel):
    Address: Optional[str]
    User: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EmailDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EmailDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EmailDefinition = EmailDefinition


@dataclass
class HttpDefinition(BaseModel):
    Address: Optional[str]
    Format: Optional[str]
    Method: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Format=json_data.get("Format"),
            Method=json_data.get("Method"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpDefinition = HttpDefinition


@dataclass
class PagerDutyDefinition(BaseModel):
    Account: Optional[str]
    ContactGroupFallback: Optional[str]
    ServiceKey: Optional[str]
    WebhookUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PagerDutyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PagerDutyDefinition"]:
        if not json_data:
            return None
        return cls(
            Account=json_data.get("Account"),
            ContactGroupFallback=json_data.get("ContactGroupFallback"),
            ServiceKey=json_data.get("ServiceKey"),
            WebhookUrl=json_data.get("WebhookUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PagerDutyDefinition = PagerDutyDefinition


@dataclass
class SlackDefinition(BaseModel):
    Buttons: Optional[bool]
    Channel: Optional[str]
    ContactGroupFallback: Optional[str]
    Team: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SlackDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SlackDefinition"]:
        if not json_data:
            return None
        return cls(
            Buttons=json_data.get("Buttons"),
            Channel=json_data.get("Channel"),
            ContactGroupFallback=json_data.get("ContactGroupFallback"),
            Team=json_data.get("Team"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SlackDefinition = SlackDefinition


@dataclass
class SmsDefinition(BaseModel):
    Address: Optional[str]
    User: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SmsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SmsDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SmsDefinition = SmsDefinition


@dataclass
class VictoropsDefinition(BaseModel):
    ApiKey: Optional[str]
    ContactGroupFallback: Optional[str]
    Critical: Optional[float]
    Info: Optional[float]
    Team: Optional[str]
    Warning: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_VictoropsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VictoropsDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiKey=json_data.get("ApiKey"),
            ContactGroupFallback=json_data.get("ContactGroupFallback"),
            Critical=json_data.get("Critical"),
            Info=json_data.get("Info"),
            Team=json_data.get("Team"),
            Warning=json_data.get("Warning"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VictoropsDefinition = VictoropsDefinition


@dataclass
class XmppDefinition(BaseModel):
    Address: Optional[str]
    User: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_XmppDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_XmppDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_XmppDefinition = XmppDefinition


