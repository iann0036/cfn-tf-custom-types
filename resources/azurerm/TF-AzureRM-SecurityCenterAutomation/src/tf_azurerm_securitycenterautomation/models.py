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
    Description: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    Scopes: Optional[Sequence[str]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Action: Optional[Sequence["_ActionDefinition"]]
    Source: Optional[Sequence["_SourceDefinition"]]
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
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Scopes=json_data.get("Scopes"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Action=deserialize_list(json_data.get("Action"), ActionDefinition),
            Source=deserialize_list(json_data.get("Source"), SourceDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class ActionDefinition(BaseModel):
    ConnectionString: Optional[str]
    ResourceId: Optional[str]
    TriggerUrl: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnectionString=json_data.get("ConnectionString"),
            ResourceId=json_data.get("ResourceId"),
            TriggerUrl=json_data.get("TriggerUrl"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionDefinition = ActionDefinition


@dataclass
class SourceDefinition(BaseModel):
    EventSource: Optional[str]
    RuleSet: Optional[Sequence["_RuleSetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceDefinition"]:
        if not json_data:
            return None
        return cls(
            EventSource=json_data.get("EventSource"),
            RuleSet=deserialize_list(json_data.get("RuleSet"), RuleSetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceDefinition = SourceDefinition


@dataclass
class RuleSetDefinition(BaseModel):
    Rule: Optional[Sequence["_RuleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleSetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleSetDefinition"]:
        if not json_data:
            return None
        return cls(
            Rule=deserialize_list(json_data.get("Rule"), RuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleSetDefinition = RuleSetDefinition


@dataclass
class RuleDefinition(BaseModel):
    ExpectedValue: Optional[str]
    Operator: Optional[str]
    PropertyPath: Optional[str]
    PropertyType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleDefinition"]:
        if not json_data:
            return None
        return cls(
            ExpectedValue=json_data.get("ExpectedValue"),
            Operator=json_data.get("Operator"),
            PropertyPath=json_data.get("PropertyPath"),
            PropertyType=json_data.get("PropertyType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleDefinition = RuleDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


