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
    Bucket: Optional[str]
    Id: Optional[str]
    Namespace: Optional[str]
    TimeCreated: Optional[str]
    Rules: Optional[Sequence["_RulesDefinition"]]
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
            Bucket=json_data.get("Bucket"),
            Id=json_data.get("Id"),
            Namespace=json_data.get("Namespace"),
            TimeCreated=json_data.get("TimeCreated"),
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RulesDefinition(BaseModel):
    Action: Optional[str]
    IsEnabled: Optional[bool]
    Name: Optional[str]
    Target: Optional[str]
    TimeAmount: Optional[str]
    TimeUnit: Optional[str]
    ObjectNameFilter: Optional[Sequence["_ObjectNameFilterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            IsEnabled=json_data.get("IsEnabled"),
            Name=json_data.get("Name"),
            Target=json_data.get("Target"),
            TimeAmount=json_data.get("TimeAmount"),
            TimeUnit=json_data.get("TimeUnit"),
            ObjectNameFilter=deserialize_list(json_data.get("ObjectNameFilter"), ObjectNameFilterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesDefinition = RulesDefinition


@dataclass
class ObjectNameFilterDefinition(BaseModel):
    ExclusionPatterns: Optional[Sequence[str]]
    InclusionPatterns: Optional[Sequence[str]]
    InclusionPrefixes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ObjectNameFilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ObjectNameFilterDefinition"]:
        if not json_data:
            return None
        return cls(
            ExclusionPatterns=json_data.get("ExclusionPatterns"),
            InclusionPatterns=json_data.get("InclusionPatterns"),
            InclusionPrefixes=json_data.get("InclusionPrefixes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ObjectNameFilterDefinition = ObjectNameFilterDefinition


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


