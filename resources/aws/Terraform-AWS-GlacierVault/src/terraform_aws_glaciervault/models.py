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
    AccessPolicy: Optional[str]
    Arn: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Notification: Optional[Sequence["_Notification"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AccessPolicy=json_data.get("AccessPolicy"),
            Arn=json_data.get("Arn"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            Notification=json_data.get("Notification"),
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
class Notification:
    Events: Optional[Sequence[str]]
    SnsTopic: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Notification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Notification"]:
        if not json_data:
            return None
        return cls(
            Events=json_data.get("Events"),
            SnsTopic=json_data.get("SnsTopic"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Notification = Notification


