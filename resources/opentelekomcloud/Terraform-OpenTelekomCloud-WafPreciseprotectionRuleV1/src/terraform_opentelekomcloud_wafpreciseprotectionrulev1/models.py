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
    ActionCategory: Optional[str]
    End: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    PolicyId: Optional[str]
    Priority: Optional[float]
    Start: Optional[str]
    Time: Optional[bool]
    Conditions: Optional[Sequence["_Conditions"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ActionCategory=json_data.get("ActionCategory"),
            End=json_data.get("End"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PolicyId=json_data.get("PolicyId"),
            Priority=json_data.get("Priority"),
            Start=json_data.get("Start"),
            Time=json_data.get("Time"),
            Conditions=json_data.get("Conditions"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Conditions:
    Category: Optional[str]
    Contents: Optional[Sequence[str]]
    Index: Optional[str]
    Logic: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Conditions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Conditions"]:
        if not json_data:
            return None
        return cls(
            Category=json_data.get("Category"),
            Contents=json_data.get("Contents"),
            Index=json_data.get("Index"),
            Logic=json_data.get("Logic"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Conditions = Conditions


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


