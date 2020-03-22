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
    AlertOption: Optional[Sequence["_AlertOption"]]
    Email: Optional[Sequence["_Email"]]
    Http: Optional[Sequence["_Http"]]
    Irc: Optional[Sequence["_Irc"]]
    PagerDuty: Optional[Sequence["_PagerDuty"]]
    Slack: Optional[Sequence["_Slack"]]
    Sms: Optional[Sequence["_Sms"]]
    Victorops: Optional[Sequence["_Victorops"]]
    Xmpp: Optional[Sequence["_Xmpp"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
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
            AlertOption=json_data.get("AlertOption"),
            Email=json_data.get("Email"),
            Http=json_data.get("Http"),
            Irc=json_data.get("Irc"),
            PagerDuty=json_data.get("PagerDuty"),
            Slack=json_data.get("Slack"),
            Sms=json_data.get("Sms"),
            Victorops=json_data.get("Victorops"),
            Xmpp=json_data.get("Xmpp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AlertOption:
    EscalateAfter: Optional[str]
    EscalateTo: Optional[str]
    Reminder: Optional[str]
    Severity: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AlertOption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlertOption"]:
        if not json_data:
            return None
        return cls(
            EscalateAfter=json_data.get("EscalateAfter"),
            EscalateTo=json_data.get("EscalateTo"),
            Reminder=json_data.get("Reminder"),
            Severity=json_data.get("Severity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlertOption = AlertOption


@dataclass
class Email:
    Address: Optional[str]
    User: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Email"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Email"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Email = Email


@dataclass
class Http:
    Address: Optional[str]
    Format: Optional[str]
    Method: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Http"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Http"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Format=json_data.get("Format"),
            Method=json_data.get("Method"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Http = Http


@dataclass
class Irc:
    User: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Irc"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Irc"]:
        if not json_data:
            return None
        return cls(
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Irc = Irc


@dataclass
class PagerDuty:
    ContactGroupFallback: Optional[str]
    ServiceKey: Optional[str]
    WebhookUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PagerDuty"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PagerDuty"]:
        if not json_data:
            return None
        return cls(
            ContactGroupFallback=json_data.get("ContactGroupFallback"),
            ServiceKey=json_data.get("ServiceKey"),
            WebhookUrl=json_data.get("WebhookUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PagerDuty = PagerDuty


@dataclass
class Slack:
    Buttons: Optional[bool]
    Channel: Optional[str]
    ContactGroupFallback: Optional[str]
    Team: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Slack"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Slack"]:
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
_Slack = Slack


@dataclass
class Sms:
    Address: Optional[str]
    User: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Sms"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Sms"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Sms = Sms


@dataclass
class Victorops:
    ApiKey: Optional[str]
    ContactGroupFallback: Optional[str]
    Critical: Optional[float]
    Info: Optional[float]
    Team: Optional[str]
    Warning: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Victorops"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Victorops"]:
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
_Victorops = Victorops


@dataclass
class Xmpp:
    Address: Optional[str]
    User: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Xmpp"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Xmpp"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Xmpp = Xmpp


