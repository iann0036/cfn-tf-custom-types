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
    Fingerprint: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    SelfLink: Optional[str]
    Rule: Optional[Sequence["_RuleDefinition"]]
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
            Fingerprint=json_data.get("Fingerprint"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            SelfLink=json_data.get("SelfLink"),
            Rule=deserialize_list(json_data.get("Rule"), RuleDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RuleDefinition(BaseModel):
    Action: Optional[str]
    Description: Optional[str]
    Preview: Optional[bool]
    Priority: Optional[float]
    Match: Optional[Sequence["_MatchDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Description=json_data.get("Description"),
            Preview=json_data.get("Preview"),
            Priority=json_data.get("Priority"),
            Match=deserialize_list(json_data.get("Match"), MatchDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleDefinition = RuleDefinition


@dataclass
class MatchDefinition(BaseModel):
    VersionedExpr: Optional[str]
    Config: Optional[Sequence["_ConfigDefinition"]]
    Expr: Optional[Sequence["_ExprDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchDefinition"]:
        if not json_data:
            return None
        return cls(
            VersionedExpr=json_data.get("VersionedExpr"),
            Config=deserialize_list(json_data.get("Config"), ConfigDefinition),
            Expr=deserialize_list(json_data.get("Expr"), ExprDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchDefinition = MatchDefinition


@dataclass
class ConfigDefinition(BaseModel):
    SrcIpRanges: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            SrcIpRanges=json_data.get("SrcIpRanges"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigDefinition = ConfigDefinition


@dataclass
class ExprDefinition(BaseModel):
    Expression: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExprDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExprDefinition"]:
        if not json_data:
            return None
        return cls(
            Expression=json_data.get("Expression"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExprDefinition = ExprDefinition


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


