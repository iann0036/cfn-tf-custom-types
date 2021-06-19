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
    Action: Optional[str]
    FilterType: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    NamespaceName: Optional[str]
    ResourceGroupName: Optional[str]
    SqlFilter: Optional[str]
    SubscriptionName: Optional[str]
    TopicName: Optional[str]
    CorrelationFilter: Optional[Sequence["_CorrelationFilterDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            Action=json_data.get("Action"),
            FilterType=json_data.get("FilterType"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NamespaceName=json_data.get("NamespaceName"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SqlFilter=json_data.get("SqlFilter"),
            SubscriptionName=json_data.get("SubscriptionName"),
            TopicName=json_data.get("TopicName"),
            CorrelationFilter=deserialize_list(json_data.get("CorrelationFilter"), CorrelationFilterDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CorrelationFilterDefinition(BaseModel):
    ContentType: Optional[str]
    CorrelationId: Optional[str]
    Label: Optional[str]
    MessageId: Optional[str]
    Properties: Optional[Sequence["_PropertiesDefinition"]]
    ReplyTo: Optional[str]
    ReplyToSessionId: Optional[str]
    SessionId: Optional[str]
    To: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CorrelationFilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CorrelationFilterDefinition"]:
        if not json_data:
            return None
        return cls(
            ContentType=json_data.get("ContentType"),
            CorrelationId=json_data.get("CorrelationId"),
            Label=json_data.get("Label"),
            MessageId=json_data.get("MessageId"),
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition),
            ReplyTo=json_data.get("ReplyTo"),
            ReplyToSessionId=json_data.get("ReplyToSessionId"),
            SessionId=json_data.get("SessionId"),
            To=json_data.get("To"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CorrelationFilterDefinition = CorrelationFilterDefinition


@dataclass
class PropertiesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition = PropertiesDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


