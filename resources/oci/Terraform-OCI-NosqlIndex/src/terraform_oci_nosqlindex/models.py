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
    CompartmentId: Optional[str]
    IsIfNotExists: Optional[bool]
    LifecycleDetails: Optional[str]
    Name: Optional[str]
    State: Optional[str]
    TableId: Optional[str]
    TableName: Optional[str]
    TableNameOrId: Optional[str]
    Keys: Optional[Sequence["_Keys"]]
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
            CompartmentId=json_data.get("CompartmentId"),
            IsIfNotExists=json_data.get("IsIfNotExists"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            Name=json_data.get("Name"),
            State=json_data.get("State"),
            TableId=json_data.get("TableId"),
            TableName=json_data.get("TableName"),
            TableNameOrId=json_data.get("TableNameOrId"),
            Keys=json_data.get("Keys"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Keys:
    ColumnName: Optional[str]
    JsonFieldType: Optional[str]
    JsonPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Keys"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Keys"]:
        if not json_data:
            return None
        return cls(
            ColumnName=json_data.get("ColumnName"),
            JsonFieldType=json_data.get("JsonFieldType"),
            JsonPath=json_data.get("JsonPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Keys = Keys


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


