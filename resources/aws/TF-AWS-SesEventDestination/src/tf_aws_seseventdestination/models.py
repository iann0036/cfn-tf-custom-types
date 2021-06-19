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
    ConfigurationSetName: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    MatchingTypes: Optional[Sequence[str]]
    Name: Optional[str]
    CloudwatchDestination: Optional[Sequence["_CloudwatchDestinationDefinition"]]
    KinesisDestination: Optional[Sequence["_KinesisDestinationDefinition"]]
    SnsDestination: Optional[Sequence["_SnsDestinationDefinition"]]

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
            ConfigurationSetName=json_data.get("ConfigurationSetName"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            MatchingTypes=json_data.get("MatchingTypes"),
            Name=json_data.get("Name"),
            CloudwatchDestination=deserialize_list(json_data.get("CloudwatchDestination"), CloudwatchDestinationDefinition),
            KinesisDestination=deserialize_list(json_data.get("KinesisDestination"), KinesisDestinationDefinition),
            SnsDestination=deserialize_list(json_data.get("SnsDestination"), SnsDestinationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CloudwatchDestinationDefinition(BaseModel):
    DefaultValue: Optional[str]
    DimensionName: Optional[str]
    ValueSource: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudwatchDestinationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudwatchDestinationDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultValue=json_data.get("DefaultValue"),
            DimensionName=json_data.get("DimensionName"),
            ValueSource=json_data.get("ValueSource"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudwatchDestinationDefinition = CloudwatchDestinationDefinition


@dataclass
class KinesisDestinationDefinition(BaseModel):
    RoleArn: Optional[str]
    StreamArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisDestinationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisDestinationDefinition"]:
        if not json_data:
            return None
        return cls(
            RoleArn=json_data.get("RoleArn"),
            StreamArn=json_data.get("StreamArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisDestinationDefinition = KinesisDestinationDefinition


@dataclass
class SnsDestinationDefinition(BaseModel):
    TopicArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnsDestinationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnsDestinationDefinition"]:
        if not json_data:
            return None
        return cls(
            TopicArn=json_data.get("TopicArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnsDestinationDefinition = SnsDestinationDefinition


