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
    AppliedProfile: Optional[str]
    ApplyOn: Optional[str]
    Color: Optional[str]
    Comments: Optional[str]
    Id: Optional[str]
    IgnoreErrors: Optional[bool]
    IgnoreWarnings: Optional[bool]
    Name: Optional[str]
    Tags: Optional[Sequence[str]]
    AppliedThreatRules: Optional[Sequence["_AppliedThreatRulesDefinition"]]

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
            AppliedProfile=json_data.get("AppliedProfile"),
            ApplyOn=json_data.get("ApplyOn"),
            Color=json_data.get("Color"),
            Comments=json_data.get("Comments"),
            Id=json_data.get("Id"),
            IgnoreErrors=json_data.get("IgnoreErrors"),
            IgnoreWarnings=json_data.get("IgnoreWarnings"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            AppliedThreatRules=deserialize_list(json_data.get("AppliedThreatRules"), AppliedThreatRulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AppliedThreatRulesDefinition(BaseModel):
    Layer: Optional[str]
    Name: Optional[str]
    Position: Optional[Sequence["_PositionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AppliedThreatRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppliedThreatRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Layer=json_data.get("Layer"),
            Name=json_data.get("Name"),
            Position=deserialize_list(json_data.get("Position"), PositionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppliedThreatRulesDefinition = AppliedThreatRulesDefinition


@dataclass
class PositionDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PositionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PositionDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PositionDefinition = PositionDefinition


