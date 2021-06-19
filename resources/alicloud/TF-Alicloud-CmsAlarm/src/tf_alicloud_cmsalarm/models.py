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
    ContactGroups: Optional[Sequence[str]]
    Dimensions: Optional[Sequence["_DimensionsDefinition"]]
    EffectiveInterval: Optional[str]
    Enabled: Optional[bool]
    EndTime: Optional[float]
    Id: Optional[str]
    Metric: Optional[str]
    Name: Optional[str]
    NotifyType: Optional[float]
    Operator: Optional[str]
    Period: Optional[float]
    Project: Optional[str]
    SilenceTime: Optional[float]
    StartTime: Optional[float]
    Statistics: Optional[str]
    Status: Optional[str]
    Threshold: Optional[str]
    TriggeredCount: Optional[float]
    Webhook: Optional[str]
    EscalationsCritical: Optional[Sequence["_EscalationsCriticalDefinition"]]
    EscalationsInfo: Optional[Sequence["_EscalationsInfoDefinition"]]
    EscalationsWarn: Optional[Sequence["_EscalationsWarnDefinition"]]

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
            ContactGroups=json_data.get("ContactGroups"),
            Dimensions=deserialize_list(json_data.get("Dimensions"), DimensionsDefinition),
            EffectiveInterval=json_data.get("EffectiveInterval"),
            Enabled=json_data.get("Enabled"),
            EndTime=json_data.get("EndTime"),
            Id=json_data.get("Id"),
            Metric=json_data.get("Metric"),
            Name=json_data.get("Name"),
            NotifyType=json_data.get("NotifyType"),
            Operator=json_data.get("Operator"),
            Period=json_data.get("Period"),
            Project=json_data.get("Project"),
            SilenceTime=json_data.get("SilenceTime"),
            StartTime=json_data.get("StartTime"),
            Statistics=json_data.get("Statistics"),
            Status=json_data.get("Status"),
            Threshold=json_data.get("Threshold"),
            TriggeredCount=json_data.get("TriggeredCount"),
            Webhook=json_data.get("Webhook"),
            EscalationsCritical=deserialize_list(json_data.get("EscalationsCritical"), EscalationsCriticalDefinition),
            EscalationsInfo=deserialize_list(json_data.get("EscalationsInfo"), EscalationsInfoDefinition),
            EscalationsWarn=deserialize_list(json_data.get("EscalationsWarn"), EscalationsWarnDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DimensionsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DimensionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DimensionsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DimensionsDefinition = DimensionsDefinition


@dataclass
class EscalationsCriticalDefinition(BaseModel):
    ComparisonOperator: Optional[str]
    Statistics: Optional[str]
    Threshold: Optional[str]
    Times: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_EscalationsCriticalDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EscalationsCriticalDefinition"]:
        if not json_data:
            return None
        return cls(
            ComparisonOperator=json_data.get("ComparisonOperator"),
            Statistics=json_data.get("Statistics"),
            Threshold=json_data.get("Threshold"),
            Times=json_data.get("Times"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EscalationsCriticalDefinition = EscalationsCriticalDefinition


@dataclass
class EscalationsInfoDefinition(BaseModel):
    ComparisonOperator: Optional[str]
    Statistics: Optional[str]
    Threshold: Optional[str]
    Times: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_EscalationsInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EscalationsInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            ComparisonOperator=json_data.get("ComparisonOperator"),
            Statistics=json_data.get("Statistics"),
            Threshold=json_data.get("Threshold"),
            Times=json_data.get("Times"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EscalationsInfoDefinition = EscalationsInfoDefinition


@dataclass
class EscalationsWarnDefinition(BaseModel):
    ComparisonOperator: Optional[str]
    Statistics: Optional[str]
    Threshold: Optional[str]
    Times: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_EscalationsWarnDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EscalationsWarnDefinition"]:
        if not json_data:
            return None
        return cls(
            ComparisonOperator=json_data.get("ComparisonOperator"),
            Statistics=json_data.get("Statistics"),
            Threshold=json_data.get("Threshold"),
            Times=json_data.get("Times"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EscalationsWarnDefinition = EscalationsWarnDefinition


