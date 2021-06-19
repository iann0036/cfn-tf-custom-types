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
    Arn: Optional[str]
    Description: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Schedule: Optional[str]
    State: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Type: Optional[str]
    WorkflowName: Optional[str]
    Actions: Optional[Sequence["_ActionsDefinition"]]
    Predicate: Optional[Sequence["_PredicateDefinition"]]
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
            Arn=json_data.get("Arn"),
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Schedule=json_data.get("Schedule"),
            State=json_data.get("State"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Type=json_data.get("Type"),
            WorkflowName=json_data.get("WorkflowName"),
            Actions=deserialize_list(json_data.get("Actions"), ActionsDefinition),
            Predicate=deserialize_list(json_data.get("Predicate"), PredicateDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class ActionsDefinition(BaseModel):
    Arguments: Optional[Sequence["_ArgumentsDefinition"]]
    CrawlerName: Optional[str]
    JobName: Optional[str]
    SecurityConfiguration: Optional[str]
    Timeout: Optional[float]
    NotificationProperty: Optional[Sequence["_NotificationPropertyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ActionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Arguments=deserialize_list(json_data.get("Arguments"), ArgumentsDefinition),
            CrawlerName=json_data.get("CrawlerName"),
            JobName=json_data.get("JobName"),
            SecurityConfiguration=json_data.get("SecurityConfiguration"),
            Timeout=json_data.get("Timeout"),
            NotificationProperty=deserialize_list(json_data.get("NotificationProperty"), NotificationPropertyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionsDefinition = ActionsDefinition


@dataclass
class ArgumentsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ArgumentsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArgumentsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ArgumentsDefinition = ArgumentsDefinition


@dataclass
class NotificationPropertyDefinition(BaseModel):
    NotifyDelayAfter: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationPropertyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationPropertyDefinition"]:
        if not json_data:
            return None
        return cls(
            NotifyDelayAfter=json_data.get("NotifyDelayAfter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationPropertyDefinition = NotificationPropertyDefinition


@dataclass
class PredicateDefinition(BaseModel):
    Logical: Optional[str]
    Conditions: Optional[Sequence["_ConditionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PredicateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PredicateDefinition"]:
        if not json_data:
            return None
        return cls(
            Logical=json_data.get("Logical"),
            Conditions=deserialize_list(json_data.get("Conditions"), ConditionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PredicateDefinition = PredicateDefinition


@dataclass
class ConditionsDefinition(BaseModel):
    CrawlState: Optional[str]
    CrawlerName: Optional[str]
    JobName: Optional[str]
    LogicalOperator: Optional[str]
    State: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionsDefinition"]:
        if not json_data:
            return None
        return cls(
            CrawlState=json_data.get("CrawlState"),
            CrawlerName=json_data.get("CrawlerName"),
            JobName=json_data.get("JobName"),
            LogicalOperator=json_data.get("LogicalOperator"),
            State=json_data.get("State"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionsDefinition = ConditionsDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


