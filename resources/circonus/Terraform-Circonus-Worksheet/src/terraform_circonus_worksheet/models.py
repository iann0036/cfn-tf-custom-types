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
    Description: Optional[str]
    Favourite: Optional[bool]
    Graphs: Optional[Sequence[str]]
    Notes: Optional[str]
    Tags: Optional[Sequence[str]]
    Title: Optional[str]
    SmartQueries: Optional[Sequence["_SmartQueries"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            Favourite=json_data.get("Favourite"),
            Graphs=json_data.get("Graphs"),
            Notes=json_data.get("Notes"),
            Tags=json_data.get("Tags"),
            Title=json_data.get("Title"),
            SmartQueries=json_data.get("SmartQueries"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SmartQueries:
    Name: Optional[str]
    Order: Optional[Sequence[str]]
    Query: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SmartQueries"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SmartQueries"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Order=json_data.get("Order"),
            Query=json_data.get("Query"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SmartQueries = SmartQueries


