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
    CreateTime: Optional[str]
    Description: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    InitialGroupConfig: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    Parent: Optional[str]
    UpdateTime: Optional[str]
    GroupKey: Optional[Sequence["_GroupKeyDefinition"]]
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
            CreateTime=json_data.get("CreateTime"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            InitialGroupConfig=json_data.get("InitialGroupConfig"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            Parent=json_data.get("Parent"),
            UpdateTime=json_data.get("UpdateTime"),
            GroupKey=deserialize_list(json_data.get("GroupKey"), GroupKeyDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class GroupKeyDefinition(BaseModel):
    Id: Optional[str]
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GroupKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GroupKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GroupKeyDefinition = GroupKeyDefinition


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

