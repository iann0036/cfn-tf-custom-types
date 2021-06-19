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
    SendDegraded: Optional[bool]
    SendFailure: Optional[bool]
    SendRecovery: Optional[bool]
    SslExpiry: Optional[bool]
    SslExpiryThreshold: Optional[float]
    Email: Optional[Sequence["_EmailDefinition"]]
    Opsgenie: Optional[Sequence["_OpsgenieDefinition"]]
    Slack: Optional[Sequence["_SlackDefinition"]]
    Sms: Optional[Sequence["_SmsDefinition"]]
    Webhook: Optional[Sequence["_WebhookDefinition"]]

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
            SendDegraded=json_data.get("SendDegraded"),
            SendFailure=json_data.get("SendFailure"),
            SendRecovery=json_data.get("SendRecovery"),
            SslExpiry=json_data.get("SslExpiry"),
            SslExpiryThreshold=json_data.get("SslExpiryThreshold"),
            Email=deserialize_list(json_data.get("Email"), EmailDefinition),
            Opsgenie=deserialize_list(json_data.get("Opsgenie"), OpsgenieDefinition),
            Slack=deserialize_list(json_data.get("Slack"), SlackDefinition),
            Sms=deserialize_list(json_data.get("Sms"), SmsDefinition),
            Webhook=deserialize_list(json_data.get("Webhook"), WebhookDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EmailDefinition(BaseModel):
    Address: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EmailDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EmailDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EmailDefinition = EmailDefinition


@dataclass
class OpsgenieDefinition(BaseModel):
    ApiKey: Optional[str]
    Name: Optional[str]
    Priority: Optional[str]
    Region: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OpsgenieDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OpsgenieDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiKey=json_data.get("ApiKey"),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            Region=json_data.get("Region"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OpsgenieDefinition = OpsgenieDefinition


@dataclass
class SlackDefinition(BaseModel):
    Channel: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SlackDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SlackDefinition"]:
        if not json_data:
            return None
        return cls(
            Channel=json_data.get("Channel"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SlackDefinition = SlackDefinition


@dataclass
class SmsDefinition(BaseModel):
    Name: Optional[str]
    Number: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SmsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SmsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Number=json_data.get("Number"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SmsDefinition = SmsDefinition


@dataclass
class WebhookDefinition(BaseModel):
    Headers: Optional[Sequence["_HeadersDefinition"]]
    Method: Optional[str]
    Name: Optional[str]
    QueryParameters: Optional[Sequence["_QueryParametersDefinition"]]
    Template: Optional[str]
    Url: Optional[str]
    WebhookSecret: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WebhookDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebhookDefinition"]:
        if not json_data:
            return None
        return cls(
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition),
            Method=json_data.get("Method"),
            Name=json_data.get("Name"),
            QueryParameters=deserialize_list(json_data.get("QueryParameters"), QueryParametersDefinition),
            Template=json_data.get("Template"),
            Url=json_data.get("Url"),
            WebhookSecret=json_data.get("WebhookSecret"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebhookDefinition = WebhookDefinition


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


