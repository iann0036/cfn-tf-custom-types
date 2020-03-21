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
    Bucket: Optional[str]
    Id: Optional[str]
    LambdaFunction: Optional[Sequence["_LambdaFunction"]]
    Queue: Optional[Sequence["_Queue"]]
    Topic: Optional[Sequence["_Topic"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Bucket=json_data.get("Bucket"),
            Id=json_data.get("Id"),
            LambdaFunction=json_data.get("LambdaFunction"),
            Queue=json_data.get("Queue"),
            Topic=json_data.get("Topic"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LambdaFunction:
    Events: Optional[Sequence[str]]
    FilterPrefix: Optional[str]
    FilterSuffix: Optional[str]
    Id: Optional[str]
    LambdaFunctionArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaFunction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaFunction"]:
        if not json_data:
            return None
        return cls(
            Events=json_data.get("Events"),
            FilterPrefix=json_data.get("FilterPrefix"),
            FilterSuffix=json_data.get("FilterSuffix"),
            Id=json_data.get("Id"),
            LambdaFunctionArn=json_data.get("LambdaFunctionArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaFunction = LambdaFunction


@dataclass
class Queue:
    Events: Optional[Sequence[str]]
    FilterPrefix: Optional[str]
    FilterSuffix: Optional[str]
    Id: Optional[str]
    QueueArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Queue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Queue"]:
        if not json_data:
            return None
        return cls(
            Events=json_data.get("Events"),
            FilterPrefix=json_data.get("FilterPrefix"),
            FilterSuffix=json_data.get("FilterSuffix"),
            Id=json_data.get("Id"),
            QueueArn=json_data.get("QueueArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Queue = Queue


@dataclass
class Topic:
    Events: Optional[Sequence[str]]
    FilterPrefix: Optional[str]
    FilterSuffix: Optional[str]
    Id: Optional[str]
    TopicArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Topic"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Topic"]:
        if not json_data:
            return None
        return cls(
            Events=json_data.get("Events"),
            FilterPrefix=json_data.get("FilterPrefix"),
            FilterSuffix=json_data.get("FilterSuffix"),
            Id=json_data.get("Id"),
            TopicArn=json_data.get("TopicArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Topic = Topic


