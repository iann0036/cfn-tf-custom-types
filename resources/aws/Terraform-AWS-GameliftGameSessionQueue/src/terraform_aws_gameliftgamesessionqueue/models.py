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
    Destinations: Optional[Sequence[str]]
    Id: Optional[str]
    Name: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    TimeoutInSeconds: Optional[float]
    PlayerLatencyPolicy: Optional[Sequence["_PlayerLatencyPolicy"]]

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
            Destinations=json_data.get("Destinations"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            TimeoutInSeconds=json_data.get("TimeoutInSeconds"),
            PlayerLatencyPolicy=json_data.get("PlayerLatencyPolicy"),
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
class PlayerLatencyPolicy:
    MaximumIndividualPlayerLatencyMilliseconds: Optional[float]
    PolicyDurationSeconds: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PlayerLatencyPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlayerLatencyPolicy"]:
        if not json_data:
            return None
        return cls(
            MaximumIndividualPlayerLatencyMilliseconds=json_data.get("MaximumIndividualPlayerLatencyMilliseconds"),
            PolicyDurationSeconds=json_data.get("PolicyDurationSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlayerLatencyPolicy = PlayerLatencyPolicy


