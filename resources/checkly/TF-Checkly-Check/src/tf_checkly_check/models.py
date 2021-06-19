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
    Activated: Optional[bool]
    DegradedResponseTime: Optional[float]
    DoubleCheck: Optional[bool]
    EnvironmentVariables: Optional[Sequence["_EnvironmentVariablesDefinition"]]
    Frequency: Optional[float]
    FrequencyOffset: Optional[float]
    GroupId: Optional[float]
    GroupOrder: Optional[float]
    Id: Optional[str]
    LocalSetupScript: Optional[str]
    LocalTeardownScript: Optional[str]
    Locations: Optional[Sequence[str]]
    MaxResponseTime: Optional[float]
    Muted: Optional[bool]
    Name: Optional[str]
    Script: Optional[str]
    SetupSnippetId: Optional[float]
    ShouldFail: Optional[bool]
    SslCheck: Optional[bool]
    Tags: Optional[Sequence[str]]
    TeardownSnippetId: Optional[float]
    Type: Optional[str]
    UseGlobalAlertSettings: Optional[bool]
    AlertChannelSubscription: Optional[Sequence["_AlertChannelSubscriptionDefinition"]]
    AlertSettings: Optional[Sequence["_AlertSettingsDefinition"]]
    Request: Optional[Sequence["_RequestDefinition"]]

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
            Activated=json_data.get("Activated"),
            DegradedResponseTime=json_data.get("DegradedResponseTime"),
            DoubleCheck=json_data.get("DoubleCheck"),
            EnvironmentVariables=deserialize_list(json_data.get("EnvironmentVariables"), EnvironmentVariablesDefinition),
            Frequency=json_data.get("Frequency"),
            FrequencyOffset=json_data.get("FrequencyOffset"),
            GroupId=json_data.get("GroupId"),
            GroupOrder=json_data.get("GroupOrder"),
            Id=json_data.get("Id"),
            LocalSetupScript=json_data.get("LocalSetupScript"),
            LocalTeardownScript=json_data.get("LocalTeardownScript"),
            Locations=json_data.get("Locations"),
            MaxResponseTime=json_data.get("MaxResponseTime"),
            Muted=json_data.get("Muted"),
            Name=json_data.get("Name"),
            Script=json_data.get("Script"),
            SetupSnippetId=json_data.get("SetupSnippetId"),
            ShouldFail=json_data.get("ShouldFail"),
            SslCheck=json_data.get("SslCheck"),
            Tags=json_data.get("Tags"),
            TeardownSnippetId=json_data.get("TeardownSnippetId"),
            Type=json_data.get("Type"),
            UseGlobalAlertSettings=json_data.get("UseGlobalAlertSettings"),
            AlertChannelSubscription=deserialize_list(json_data.get("AlertChannelSubscription"), AlertChannelSubscriptionDefinition),
            AlertSettings=deserialize_list(json_data.get("AlertSettings"), AlertSettingsDefinition),
            Request=deserialize_list(json_data.get("Request"), RequestDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EnvironmentVariablesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvironmentVariablesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvironmentVariablesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvironmentVariablesDefinition = EnvironmentVariablesDefinition


@dataclass
class AlertChannelSubscriptionDefinition(BaseModel):
    Activated: Optional[bool]
    ChannelId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AlertChannelSubscriptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlertChannelSubscriptionDefinition"]:
        if not json_data:
            return None
        return cls(
            Activated=json_data.get("Activated"),
            ChannelId=json_data.get("ChannelId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlertChannelSubscriptionDefinition = AlertChannelSubscriptionDefinition


@dataclass
class AlertSettingsDefinition(BaseModel):
    EscalationType: Optional[str]
    Reminders: Optional[Sequence["_RemindersDefinition"]]
    RunBasedEscalation: Optional[Sequence["_RunBasedEscalationDefinition"]]
    SslCertificates: Optional[Sequence["_SslCertificatesDefinition"]]
    TimeBasedEscalation: Optional[Sequence["_TimeBasedEscalationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AlertSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlertSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            EscalationType=json_data.get("EscalationType"),
            Reminders=deserialize_list(json_data.get("Reminders"), RemindersDefinition),
            RunBasedEscalation=deserialize_list(json_data.get("RunBasedEscalation"), RunBasedEscalationDefinition),
            SslCertificates=deserialize_list(json_data.get("SslCertificates"), SslCertificatesDefinition),
            TimeBasedEscalation=deserialize_list(json_data.get("TimeBasedEscalation"), TimeBasedEscalationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlertSettingsDefinition = AlertSettingsDefinition


@dataclass
class RemindersDefinition(BaseModel):
    Amount: Optional[float]
    Interval: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RemindersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RemindersDefinition"]:
        if not json_data:
            return None
        return cls(
            Amount=json_data.get("Amount"),
            Interval=json_data.get("Interval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RemindersDefinition = RemindersDefinition


@dataclass
class RunBasedEscalationDefinition(BaseModel):
    FailedRunThreshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RunBasedEscalationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RunBasedEscalationDefinition"]:
        if not json_data:
            return None
        return cls(
            FailedRunThreshold=json_data.get("FailedRunThreshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RunBasedEscalationDefinition = RunBasedEscalationDefinition


@dataclass
class SslCertificatesDefinition(BaseModel):
    AlertThreshold: Optional[float]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SslCertificatesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SslCertificatesDefinition"]:
        if not json_data:
            return None
        return cls(
            AlertThreshold=json_data.get("AlertThreshold"),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SslCertificatesDefinition = SslCertificatesDefinition


@dataclass
class TimeBasedEscalationDefinition(BaseModel):
    MinutesFailingThreshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TimeBasedEscalationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeBasedEscalationDefinition"]:
        if not json_data:
            return None
        return cls(
            MinutesFailingThreshold=json_data.get("MinutesFailingThreshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeBasedEscalationDefinition = TimeBasedEscalationDefinition


@dataclass
class RequestDefinition(BaseModel):
    Body: Optional[str]
    BodyType: Optional[str]
    FollowRedirects: Optional[bool]
    Headers: Optional[Sequence["_HeadersDefinition"]]
    Method: Optional[str]
    QueryParameters: Optional[Sequence["_QueryParametersDefinition"]]
    Url: Optional[str]
    Assertion: Optional[Sequence["_AssertionDefinition"]]
    BasicAuth: Optional[Sequence["_BasicAuthDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RequestDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestDefinition"]:
        if not json_data:
            return None
        return cls(
            Body=json_data.get("Body"),
            BodyType=json_data.get("BodyType"),
            FollowRedirects=json_data.get("FollowRedirects"),
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition),
            Method=json_data.get("Method"),
            QueryParameters=deserialize_list(json_data.get("QueryParameters"), QueryParametersDefinition),
            Url=json_data.get("Url"),
            Assertion=deserialize_list(json_data.get("Assertion"), AssertionDefinition),
            BasicAuth=deserialize_list(json_data.get("BasicAuth"), BasicAuthDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestDefinition = RequestDefinition


@dataclass
class HeadersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersDefinition = HeadersDefinition


@dataclass
class QueryParametersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_QueryParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryParametersDefinition = QueryParametersDefinition


@dataclass
class AssertionDefinition(BaseModel):
    Comparison: Optional[str]
    Property: Optional[str]
    Source: Optional[str]
    Target: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AssertionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AssertionDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Property=json_data.get("Property"),
            Source=json_data.get("Source"),
            Target=json_data.get("Target"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AssertionDefinition = AssertionDefinition


@dataclass
class BasicAuthDefinition(BaseModel):
    Password: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BasicAuthDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BasicAuthDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BasicAuthDefinition = BasicAuthDefinition


