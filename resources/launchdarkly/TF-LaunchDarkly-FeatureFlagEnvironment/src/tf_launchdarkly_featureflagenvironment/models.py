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
    EnvKey: Optional[str]
    FlagId: Optional[str]
    Id: Optional[str]
    OffVariation: Optional[float]
    TargetingEnabled: Optional[bool]
    TrackEvents: Optional[bool]
    FlagFallthrough: Optional[Sequence["_FlagFallthroughDefinition"]]
    Prerequisites: Optional[Sequence["_PrerequisitesDefinition"]]
    Rules: Optional[Sequence["_RulesDefinition"]]
    UserTargets: Optional[Sequence["_UserTargetsDefinition"]]

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
            EnvKey=json_data.get("EnvKey"),
            FlagId=json_data.get("FlagId"),
            Id=json_data.get("Id"),
            OffVariation=json_data.get("OffVariation"),
            TargetingEnabled=json_data.get("TargetingEnabled"),
            TrackEvents=json_data.get("TrackEvents"),
            FlagFallthrough=deserialize_list(json_data.get("FlagFallthrough"), FlagFallthroughDefinition),
            Prerequisites=deserialize_list(json_data.get("Prerequisites"), PrerequisitesDefinition),
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
            UserTargets=deserialize_list(json_data.get("UserTargets"), UserTargetsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FlagFallthroughDefinition(BaseModel):
    BucketBy: Optional[str]
    RolloutWeights: Optional[Sequence[float]]
    Variation: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_FlagFallthroughDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FlagFallthroughDefinition"]:
        if not json_data:
            return None
        return cls(
            BucketBy=json_data.get("BucketBy"),
            RolloutWeights=json_data.get("RolloutWeights"),
            Variation=json_data.get("Variation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FlagFallthroughDefinition = FlagFallthroughDefinition


@dataclass
class PrerequisitesDefinition(BaseModel):
    FlagKey: Optional[str]
    Variation: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PrerequisitesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrerequisitesDefinition"]:
        if not json_data:
            return None
        return cls(
            FlagKey=json_data.get("FlagKey"),
            Variation=json_data.get("Variation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrerequisitesDefinition = PrerequisitesDefinition


@dataclass
class RulesDefinition(BaseModel):
    BucketBy: Optional[str]
    RolloutWeights: Optional[Sequence[float]]
    Variation: Optional[float]
    Clauses: Optional[Sequence["_ClausesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesDefinition"]:
        if not json_data:
            return None
        return cls(
            BucketBy=json_data.get("BucketBy"),
            RolloutWeights=json_data.get("RolloutWeights"),
            Variation=json_data.get("Variation"),
            Clauses=deserialize_list(json_data.get("Clauses"), ClausesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesDefinition = RulesDefinition


@dataclass
class ClausesDefinition(BaseModel):
    Attribute: Optional[str]
    Negate: Optional[bool]
    Op: Optional[str]
    ValueType: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ClausesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClausesDefinition"]:
        if not json_data:
            return None
        return cls(
            Attribute=json_data.get("Attribute"),
            Negate=json_data.get("Negate"),
            Op=json_data.get("Op"),
            ValueType=json_data.get("ValueType"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClausesDefinition = ClausesDefinition


@dataclass
class UserTargetsDefinition(BaseModel):
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_UserTargetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserTargetsDefinition"]:
        if not json_data:
            return None
        return cls(
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserTargetsDefinition = UserTargetsDefinition


