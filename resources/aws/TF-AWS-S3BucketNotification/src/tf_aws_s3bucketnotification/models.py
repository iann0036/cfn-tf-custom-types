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
    Bucket: Optional[str]
    Id: Optional[str]
    LambdaFunction: Optional[Sequence["_LambdaFunctionDefinition"]]
    Queue: Optional[Sequence["_QueueDefinition"]]
    Topic: Optional[Sequence["_TopicDefinition"]]

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
            Bucket=json_data.get("Bucket"),
            Id=json_data.get("Id"),
            LambdaFunction=deserialize_list(json_data.get("LambdaFunction"), LambdaFunctionDefinition),
            Queue=deserialize_list(json_data.get("Queue"), QueueDefinition),
            Topic=deserialize_list(json_data.get("Topic"), TopicDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LambdaFunctionDefinition(BaseModel):
    Events: Optional[Sequence[str]]
    FilterPrefix: Optional[str]
    FilterSuffix: Optional[str]
    Id: Optional[str]
    LambdaFunctionArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaFunctionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaFunctionDefinition"]:
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
_LambdaFunctionDefinition = LambdaFunctionDefinition


@dataclass
class QueueDefinition(BaseModel):
    Events: Optional[Sequence[str]]
    FilterPrefix: Optional[str]
    FilterSuffix: Optional[str]
    Id: Optional[str]
    QueueArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_QueueDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueueDefinition"]:
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
_QueueDefinition = QueueDefinition


@dataclass
class TopicDefinition(BaseModel):
    Events: Optional[Sequence[str]]
    FilterPrefix: Optional[str]
    FilterSuffix: Optional[str]
    Id: Optional[str]
    TopicArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TopicDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TopicDefinition"]:
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
_TopicDefinition = TopicDefinition


