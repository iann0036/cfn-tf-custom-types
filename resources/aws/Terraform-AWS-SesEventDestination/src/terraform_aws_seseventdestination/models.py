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
    ConfigurationSetName: Optional[str]
    Enabled: Optional[bool]
    MatchingTypes: Optional[Sequence[str]]
    Name: Optional[str]
    CloudwatchDestination: Optional[Sequence["_CloudwatchDestination"]]
    KinesisDestination: Optional[Sequence["_KinesisDestination"]]
    SnsDestination: Optional[Sequence["_SnsDestination"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ConfigurationSetName=json_data.get("ConfigurationSetName"),
            Enabled=json_data.get("Enabled"),
            MatchingTypes=json_data.get("MatchingTypes"),
            Name=json_data.get("Name"),
            CloudwatchDestination=json_data.get("CloudwatchDestination"),
            KinesisDestination=json_data.get("KinesisDestination"),
            SnsDestination=json_data.get("SnsDestination"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CloudwatchDestination:
    DefaultValue: Optional[str]
    DimensionName: Optional[str]
    ValueSource: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudwatchDestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudwatchDestination"]:
        if not json_data:
            return None
        return cls(
            DefaultValue=json_data.get("DefaultValue"),
            DimensionName=json_data.get("DimensionName"),
            ValueSource=json_data.get("ValueSource"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudwatchDestination = CloudwatchDestination


@dataclass
class KinesisDestination:
    RoleArn: Optional[str]
    StreamArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisDestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisDestination"]:
        if not json_data:
            return None
        return cls(
            RoleArn=json_data.get("RoleArn"),
            StreamArn=json_data.get("StreamArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisDestination = KinesisDestination


@dataclass
class SnsDestination:
    TopicArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnsDestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnsDestination"]:
        if not json_data:
            return None
        return cls(
            TopicArn=json_data.get("TopicArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnsDestination = SnsDestination


