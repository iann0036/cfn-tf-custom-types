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
    Arn: Optional[str]
    Description: Optional[str]
    ExecutionRoleArn: Optional[str]
    State: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    PolicyDetails: Optional[Sequence["_PolicyDetails"]]
    Schedule: Optional[Sequence["_Schedule"]]
    CreateRule: Optional[Sequence["_CreateRule"]]
    RetainRule: Optional[Sequence["_RetainRule"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            Description=json_data.get("Description"),
            ExecutionRoleArn=json_data.get("ExecutionRoleArn"),
            State=json_data.get("State"),
            Tags=json_data.get("Tags"),
            PolicyDetails=json_data.get("PolicyDetails"),
            Schedule=json_data.get("Schedule"),
            CreateRule=json_data.get("CreateRule"),
            RetainRule=json_data.get("RetainRule"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class PolicyDetails:
    ResourceTypes: Optional[Sequence[str]]
    TargetTags: Optional[Sequence["_TargetTags"]]
    Schedule: Optional[Sequence["_Schedule"]]

    @classmethod
    def _deserialize(
        cls: Type["_PolicyDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicyDetails"]:
        if not json_data:
            return None
        return cls(
            ResourceTypes=json_data.get("ResourceTypes"),
            TargetTags=json_data.get("TargetTags"),
            Schedule=json_data.get("Schedule"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicyDetails = PolicyDetails


@dataclass
class TargetTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TargetTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetTags = TargetTags


@dataclass
class Schedule:
    CopyTags: Optional[bool]
    Name: Optional[str]
    TagsToAdd: Optional[Sequence["_TagsToAdd"]]
    CreateRule: Optional[Sequence["_CreateRule"]]
    RetainRule: Optional[Sequence["_RetainRule"]]

    @classmethod
    def _deserialize(
        cls: Type["_Schedule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Schedule"]:
        if not json_data:
            return None
        return cls(
            CopyTags=json_data.get("CopyTags"),
            Name=json_data.get("Name"),
            TagsToAdd=json_data.get("TagsToAdd"),
            CreateRule=json_data.get("CreateRule"),
            RetainRule=json_data.get("RetainRule"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Schedule = Schedule


@dataclass
class TagsToAdd:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsToAdd"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsToAdd"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsToAdd = TagsToAdd


@dataclass
class CreateRule:
    Interval: Optional[float]
    IntervalUnit: Optional[str]
    Times: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CreateRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CreateRule"]:
        if not json_data:
            return None
        return cls(
            Interval=json_data.get("Interval"),
            IntervalUnit=json_data.get("IntervalUnit"),
            Times=json_data.get("Times"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CreateRule = CreateRule


@dataclass
class RetainRule:
    Count: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RetainRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetainRule"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetainRule = RetainRule


