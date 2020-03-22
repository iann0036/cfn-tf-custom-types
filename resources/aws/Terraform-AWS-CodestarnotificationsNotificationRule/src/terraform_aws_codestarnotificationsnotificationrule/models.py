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
    DetailType: Optional[str]
    EventTypeIds: Optional[Sequence[str]]
    Id: Optional[str]
    Name: Optional[str]
    Resource: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Target: Optional[Sequence["_Target"]]

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
            DetailType=json_data.get("DetailType"),
            EventTypeIds=json_data.get("EventTypeIds"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Resource=json_data.get("Resource"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
            Target=json_data.get("Target"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Target:
    Address: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Target"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Target"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Target = Target


