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
    Fields: Optional[Sequence[str]]
    Id: Optional[str]
    Name: Optional[str]
    SamplingRate: Optional[float]
    Endpoint: Optional[Sequence["_EndpointDefinition"]]

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
            Fields=json_data.get("Fields"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            SamplingRate=json_data.get("SamplingRate"),
            Endpoint=deserialize_list(json_data.get("Endpoint"), EndpointDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EndpointDefinition(BaseModel):
    StreamType: Optional[str]
    KinesisStreamConfig: Optional[Sequence["_KinesisStreamConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointDefinition"]:
        if not json_data:
            return None
        return cls(
            StreamType=json_data.get("StreamType"),
            KinesisStreamConfig=deserialize_list(json_data.get("KinesisStreamConfig"), KinesisStreamConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointDefinition = EndpointDefinition


@dataclass
class KinesisStreamConfigDefinition(BaseModel):
    RoleArn: Optional[str]
    StreamArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisStreamConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisStreamConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            RoleArn=json_data.get("RoleArn"),
            StreamArn=json_data.get("StreamArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisStreamConfigDefinition = KinesisStreamConfigDefinition


