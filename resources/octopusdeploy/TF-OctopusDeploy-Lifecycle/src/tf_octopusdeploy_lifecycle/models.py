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
    Id: Optional[str]
    Name: Optional[str]
    SpaceId: Optional[str]
    Phase: Optional[Sequence["_PhaseDefinition"]]
    ReleaseRetentionPolicy: Optional[Sequence["_ReleaseRetentionPolicyDefinition"]]
    TentacleRetentionPolicy: Optional[Sequence["_TentacleRetentionPolicyDefinition"]]

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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            SpaceId=json_data.get("SpaceId"),
            Phase=deserialize_list(json_data.get("Phase"), PhaseDefinition),
            ReleaseRetentionPolicy=deserialize_list(json_data.get("ReleaseRetentionPolicy"), ReleaseRetentionPolicyDefinition),
            TentacleRetentionPolicy=deserialize_list(json_data.get("TentacleRetentionPolicy"), TentacleRetentionPolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PhaseDefinition(BaseModel):
    AutomaticDeploymentTargets: Optional[Sequence[str]]
    Id: Optional[str]
    IsOptionalPhase: Optional[bool]
    MinimumEnvironmentsBeforePromotion: Optional[float]
    Name: Optional[str]
    OptionalDeploymentTargets: Optional[Sequence[str]]
    ReleaseRetentionPolicy: Optional[Sequence["_ReleaseRetentionPolicyDefinition"]]
    TentacleRetentionPolicy: Optional[Sequence["_TentacleRetentionPolicyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PhaseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PhaseDefinition"]:
        if not json_data:
            return None
        return cls(
            AutomaticDeploymentTargets=json_data.get("AutomaticDeploymentTargets"),
            Id=json_data.get("Id"),
            IsOptionalPhase=json_data.get("IsOptionalPhase"),
            MinimumEnvironmentsBeforePromotion=json_data.get("MinimumEnvironmentsBeforePromotion"),
            Name=json_data.get("Name"),
            OptionalDeploymentTargets=json_data.get("OptionalDeploymentTargets"),
            ReleaseRetentionPolicy=deserialize_list(json_data.get("ReleaseRetentionPolicy"), ReleaseRetentionPolicyDefinition),
            TentacleRetentionPolicy=deserialize_list(json_data.get("TentacleRetentionPolicy"), TentacleRetentionPolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PhaseDefinition = PhaseDefinition


@dataclass
class ReleaseRetentionPolicyDefinition(BaseModel):
    QuantityToKeep: Optional[float]
    ShouldKeepForever: Optional[bool]
    Unit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReleaseRetentionPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReleaseRetentionPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            QuantityToKeep=json_data.get("QuantityToKeep"),
            ShouldKeepForever=json_data.get("ShouldKeepForever"),
            Unit=json_data.get("Unit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReleaseRetentionPolicyDefinition = ReleaseRetentionPolicyDefinition


@dataclass
class TentacleRetentionPolicyDefinition(BaseModel):
    QuantityToKeep: Optional[float]
    ShouldKeepForever: Optional[bool]
    Unit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TentacleRetentionPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TentacleRetentionPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            QuantityToKeep=json_data.get("QuantityToKeep"),
            ShouldKeepForever=json_data.get("ShouldKeepForever"),
            Unit=json_data.get("Unit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TentacleRetentionPolicyDefinition = TentacleRetentionPolicyDefinition


