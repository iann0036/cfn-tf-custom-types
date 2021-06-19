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
    Id: Optional[str]
    Name: Optional[str]
    Tags: Optional[Sequence[str]]
    Condition: Optional[Sequence["_ConditionDefinition"]]
    Formula: Optional[Sequence["_FormulaDefinition"]]
    Notify: Optional[Sequence["_NotifyDefinition"]]

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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            Condition=deserialize_list(json_data.get("Condition"), ConditionDefinition),
            Formula=deserialize_list(json_data.get("Formula"), FormulaDefinition),
            Notify=deserialize_list(json_data.get("Notify"), NotifyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConditionDefinition(BaseModel):
    Index: Optional[float]
    MatchingSeverities: Optional[Sequence[str]]
    RuleSet: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            Index=json_data.get("Index"),
            MatchingSeverities=json_data.get("MatchingSeverities"),
            RuleSet=json_data.get("RuleSet"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionDefinition = ConditionDefinition


@dataclass
class FormulaDefinition(BaseModel):
    Expression: Optional[str]
    RaiseSeverity: Optional[float]
    Wait: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_FormulaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FormulaDefinition"]:
        if not json_data:
            return None
        return cls(
            Expression=json_data.get("Expression"),
            RaiseSeverity=json_data.get("RaiseSeverity"),
            Wait=json_data.get("Wait"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FormulaDefinition = FormulaDefinition


@dataclass
class NotifyDefinition(BaseModel):
    Sev1: Optional[Sequence[str]]
    Sev2: Optional[Sequence[str]]
    Sev3: Optional[Sequence[str]]
    Sev4: Optional[Sequence[str]]
    Sev5: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_NotifyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotifyDefinition"]:
        if not json_data:
            return None
        return cls(
            Sev1=json_data.get("Sev1"),
            Sev2=json_data.get("Sev2"),
            Sev3=json_data.get("Sev3"),
            Sev4=json_data.get("Sev4"),
            Sev5=json_data.get("Sev5"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotifyDefinition = NotifyDefinition


