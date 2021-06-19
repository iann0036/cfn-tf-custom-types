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
    ExecutionRoleArn: Optional[str]
    Id: Optional[str]
    State: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    PolicyDetails: Optional[Sequence["_PolicyDetailsDefinition"]]

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
            ExecutionRoleArn=json_data.get("ExecutionRoleArn"),
            Id=json_data.get("Id"),
            State=json_data.get("State"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            PolicyDetails=deserialize_list(json_data.get("PolicyDetails"), PolicyDetailsDefinition),
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
class PolicyDetailsDefinition(BaseModel):
    ResourceTypes: Optional[Sequence[str]]
    TargetTags: Optional[Sequence["_TargetTagsDefinition"]]
    Schedule: Optional[Sequence["_ScheduleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PolicyDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicyDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            ResourceTypes=json_data.get("ResourceTypes"),
            TargetTags=deserialize_list(json_data.get("TargetTags"), TargetTagsDefinition),
            Schedule=deserialize_list(json_data.get("Schedule"), ScheduleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicyDetailsDefinition = PolicyDetailsDefinition


@dataclass
class TargetTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TargetTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetTagsDefinition = TargetTagsDefinition


@dataclass
class ScheduleDefinition(BaseModel):
    CopyTags: Optional[bool]
    Name: Optional[str]
    TagsToAdd: Optional[Sequence["_TagsToAddDefinition"]]
    CreateRule: Optional[Sequence["_CreateRuleDefinition"]]
    RetainRule: Optional[Sequence["_RetainRuleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduleDefinition"]:
        if not json_data:
            return None
        return cls(
            CopyTags=json_data.get("CopyTags"),
            Name=json_data.get("Name"),
            TagsToAdd=deserialize_list(json_data.get("TagsToAdd"), TagsToAddDefinition),
            CreateRule=deserialize_list(json_data.get("CreateRule"), CreateRuleDefinition),
            RetainRule=deserialize_list(json_data.get("RetainRule"), RetainRuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduleDefinition = ScheduleDefinition


@dataclass
class TagsToAddDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsToAddDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsToAddDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsToAddDefinition = TagsToAddDefinition


@dataclass
class CreateRuleDefinition(BaseModel):
    Interval: Optional[float]
    IntervalUnit: Optional[str]
    Times: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CreateRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CreateRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Interval=json_data.get("Interval"),
            IntervalUnit=json_data.get("IntervalUnit"),
            Times=json_data.get("Times"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CreateRuleDefinition = CreateRuleDefinition


@dataclass
class RetainRuleDefinition(BaseModel):
    Count: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RetainRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetainRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetainRuleDefinition = RetainRuleDefinition


