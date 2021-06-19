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
    Comparison: Optional[str]
    CreatedAt: Optional[float]
    Description: Optional[str]
    Enabled: Optional[bool]
    Event: Optional[str]
    Id: Optional[str]
    IntegrationProvider: Optional[str]
    Name: Optional[str]
    PolicyId: Optional[float]
    ProcessWhere: Optional[str]
    RunbookUrl: Optional[str]
    Select: Optional[str]
    Type: Optional[str]
    UpdatedAt: Optional[float]
    ViolationCloseTimer: Optional[float]
    Where: Optional[str]
    Critical: Optional[Sequence["_CriticalDefinition"]]
    Warning: Optional[Sequence["_WarningDefinition"]]

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
            Comparison=json_data.get("Comparison"),
            CreatedAt=json_data.get("CreatedAt"),
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            Event=json_data.get("Event"),
            Id=json_data.get("Id"),
            IntegrationProvider=json_data.get("IntegrationProvider"),
            Name=json_data.get("Name"),
            PolicyId=json_data.get("PolicyId"),
            ProcessWhere=json_data.get("ProcessWhere"),
            RunbookUrl=json_data.get("RunbookUrl"),
            Select=json_data.get("Select"),
            Type=json_data.get("Type"),
            UpdatedAt=json_data.get("UpdatedAt"),
            ViolationCloseTimer=json_data.get("ViolationCloseTimer"),
            Where=json_data.get("Where"),
            Critical=deserialize_list(json_data.get("Critical"), CriticalDefinition),
            Warning=deserialize_list(json_data.get("Warning"), WarningDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CriticalDefinition(BaseModel):
    Duration: Optional[float]
    TimeFunction: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CriticalDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CriticalDefinition"]:
        if not json_data:
            return None
        return cls(
            Duration=json_data.get("Duration"),
            TimeFunction=json_data.get("TimeFunction"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CriticalDefinition = CriticalDefinition


@dataclass
class WarningDefinition(BaseModel):
    Duration: Optional[float]
    TimeFunction: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_WarningDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WarningDefinition"]:
        if not json_data:
            return None
        return cls(
            Duration=json_data.get("Duration"),
            TimeFunction=json_data.get("TimeFunction"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WarningDefinition = WarningDefinition


