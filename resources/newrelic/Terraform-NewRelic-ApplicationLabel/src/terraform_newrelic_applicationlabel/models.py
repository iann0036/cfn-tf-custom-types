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
    Category: Optional[str]
    Name: Optional[str]
    Links: Optional[Sequence["_Links"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Category=json_data.get("Category"),
            Name=json_data.get("Name"),
            Links=json_data.get("Links"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Links:
    Applications: Optional[Sequence[float]]
    Servers: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_Links"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Links"]:
        if not json_data:
            return None
        return cls(
            Applications=json_data.get("Applications"),
            Servers=json_data.get("Servers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Links = Links


