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
    EndpointType: Optional[str]
    Id: Optional[str]
    Title: Optional[str]
    BigPanda: Optional[Sequence["_BigPandaDefinition"]]
    Custom: Optional[Sequence["_CustomDefinition"]]
    DataDog: Optional[Sequence["_DataDogDefinition"]]
    PagerDuty: Optional[Sequence["_PagerDutyDefinition"]]
    Slack: Optional[Sequence["_SlackDefinition"]]
    Victorops: Optional[Sequence["_VictoropsDefinition"]]

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
            EndpointType=json_data.get("EndpointType"),
            Id=json_data.get("Id"),
            Title=json_data.get("Title"),
            BigPanda=deserialize_list(json_data.get("BigPanda"), BigPandaDefinition),
            Custom=deserialize_list(json_data.get("Custom"), CustomDefinition),
            DataDog=deserialize_list(json_data.get("DataDog"), DataDogDefinition),
            PagerDuty=deserialize_list(json_data.get("PagerDuty"), PagerDutyDefinition),
            Slack=deserialize_list(json_data.get("Slack"), SlackDefinition),
            Victorops=deserialize_list(json_data.get("Victorops"), VictoropsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BigPandaDefinition(BaseModel):
    ApiToken: Optional[str]
    AppKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BigPandaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BigPandaDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiToken=json_data.get("ApiToken"),
            AppKey=json_data.get("AppKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BigPandaDefinition = BigPandaDefinition


@dataclass
class CustomDefinition(BaseModel):
    BodyTemplate: Optional[Sequence["_BodyTemplateDefinition"]]
    Headers: Optional[Sequence["_HeadersDefinition"]]
    Method: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomDefinition"]:
        if not json_data:
            return None
        return cls(
            BodyTemplate=deserialize_list(json_data.get("BodyTemplate"), BodyTemplateDefinition),
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition),
            Method=json_data.get("Method"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomDefinition = CustomDefinition


@dataclass
class BodyTemplateDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BodyTemplateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BodyTemplateDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BodyTemplateDefinition = BodyTemplateDefinition


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
class DataDogDefinition(BaseModel):
    ApiKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataDogDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataDogDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiKey=json_data.get("ApiKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataDogDefinition = DataDogDefinition


@dataclass
class PagerDutyDefinition(BaseModel):
    ServiceKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PagerDutyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PagerDutyDefinition"]:
        if not json_data:
            return None
        return cls(
            ServiceKey=json_data.get("ServiceKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PagerDutyDefinition = PagerDutyDefinition


@dataclass
class SlackDefinition(BaseModel):
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SlackDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SlackDefinition"]:
        if not json_data:
            return None
        return cls(
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SlackDefinition = SlackDefinition


@dataclass
class VictoropsDefinition(BaseModel):
    MessageType: Optional[str]
    RoutingKey: Optional[str]
    ServiceApiKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VictoropsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VictoropsDefinition"]:
        if not json_data:
            return None
        return cls(
            MessageType=json_data.get("MessageType"),
            RoutingKey=json_data.get("RoutingKey"),
            ServiceApiKey=json_data.get("ServiceApiKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VictoropsDefinition = VictoropsDefinition


