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
    Collection: Optional[str]
    Database: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    QueryScope: Optional[str]
    Fields: Optional[Sequence["_Fields"]]
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
            Collection=json_data.get("Collection"),
            Database=json_data.get("Database"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            QueryScope=json_data.get("QueryScope"),
            Fields=json_data.get("Fields"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Fields:
    ArrayConfig: Optional[str]
    FieldPath: Optional[str]
    Order: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Fields"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Fields"]:
        if not json_data:
            return None
        return cls(
            ArrayConfig=json_data.get("ArrayConfig"),
            FieldPath=json_data.get("FieldPath"),
            Order=json_data.get("Order"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Fields = Fields


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


