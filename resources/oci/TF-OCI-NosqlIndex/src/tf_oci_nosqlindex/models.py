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
    CompartmentId: Optional[str]
    Id: Optional[str]
    IsIfNotExists: Optional[bool]
    LifecycleDetails: Optional[str]
    Name: Optional[str]
    State: Optional[str]
    TableId: Optional[str]
    TableName: Optional[str]
    TableNameOrId: Optional[str]
    Keys: Optional[Sequence["_KeysDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            CompartmentId=json_data.get("CompartmentId"),
            Id=json_data.get("Id"),
            IsIfNotExists=json_data.get("IsIfNotExists"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            Name=json_data.get("Name"),
            State=json_data.get("State"),
            TableId=json_data.get("TableId"),
            TableName=json_data.get("TableName"),
            TableNameOrId=json_data.get("TableNameOrId"),
            Keys=deserialize_list(json_data.get("Keys"), KeysDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class KeysDefinition(BaseModel):
    ColumnName: Optional[str]
    JsonFieldType: Optional[str]
    JsonPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KeysDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeysDefinition"]:
        if not json_data:
            return None
        return cls(
            ColumnName=json_data.get("ColumnName"),
            JsonFieldType=json_data.get("JsonFieldType"),
            JsonPath=json_data.get("JsonPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeysDefinition = KeysDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


