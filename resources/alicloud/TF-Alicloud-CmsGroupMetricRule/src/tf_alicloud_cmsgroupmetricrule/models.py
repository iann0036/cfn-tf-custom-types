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
    Category: Optional[str]
    ContactGroups: Optional[str]
    Dimensions: Optional[str]
    EffectiveInterval: Optional[str]
    EmailSubject: Optional[str]
    GroupId: Optional[str]
    GroupMetricRuleName: Optional[str]
    Id: Optional[str]
    Interval: Optional[str]
    MetricName: Optional[str]
    Namespace: Optional[str]
    NoEffectiveInterval: Optional[str]
    Period: Optional[float]
    RuleId: Optional[str]
    SilenceTime: Optional[float]
    Status: Optional[str]
    Webhook: Optional[str]
    Escalations: Optional[Sequence["_EscalationsDefinition"]]
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
            Category=json_data.get("Category"),
            ContactGroups=json_data.get("ContactGroups"),
            Dimensions=json_data.get("Dimensions"),
            EffectiveInterval=json_data.get("EffectiveInterval"),
            EmailSubject=json_data.get("EmailSubject"),
            GroupId=json_data.get("GroupId"),
            GroupMetricRuleName=json_data.get("GroupMetricRuleName"),
            Id=json_data.get("Id"),
            Interval=json_data.get("Interval"),
            MetricName=json_data.get("MetricName"),
            Namespace=json_data.get("Namespace"),
            NoEffectiveInterval=json_data.get("NoEffectiveInterval"),
            Period=json_data.get("Period"),
            RuleId=json_data.get("RuleId"),
            SilenceTime=json_data.get("SilenceTime"),
            Status=json_data.get("Status"),
            Webhook=json_data.get("Webhook"),
            Escalations=deserialize_list(json_data.get("Escalations"), EscalationsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EscalationsDefinition(BaseModel):
    Critical: Optional[Sequence["_CriticalDefinition"]]
    Info: Optional[Sequence["_InfoDefinition"]]
    Warn: Optional[Sequence["_WarnDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EscalationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EscalationsDefinition"]:
        if not json_data:
            return None
        return cls(
            Critical=deserialize_list(json_data.get("Critical"), CriticalDefinition),
            Info=deserialize_list(json_data.get("Info"), InfoDefinition),
            Warn=deserialize_list(json_data.get("Warn"), WarnDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EscalationsDefinition = EscalationsDefinition


@dataclass
class CriticalDefinition(BaseModel):
    ComparisonOperator: Optional[str]
    Statistics: Optional[str]
    Threshold: Optional[str]
    Times: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CriticalDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CriticalDefinition"]:
        if not json_data:
            return None
        return cls(
            ComparisonOperator=json_data.get("ComparisonOperator"),
            Statistics=json_data.get("Statistics"),
            Threshold=json_data.get("Threshold"),
            Times=json_data.get("Times"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CriticalDefinition = CriticalDefinition


@dataclass
class InfoDefinition(BaseModel):
    ComparisonOperator: Optional[str]
    Statistics: Optional[str]
    Threshold: Optional[str]
    Times: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_InfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InfoDefinition"]:
        if not json_data:
            return None
        return cls(
            ComparisonOperator=json_data.get("ComparisonOperator"),
            Statistics=json_data.get("Statistics"),
            Threshold=json_data.get("Threshold"),
            Times=json_data.get("Times"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InfoDefinition = InfoDefinition


@dataclass
class WarnDefinition(BaseModel):
    ComparisonOperator: Optional[str]
    Statistics: Optional[str]
    Threshold: Optional[str]
    Times: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_WarnDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WarnDefinition"]:
        if not json_data:
            return None
        return cls(
            ComparisonOperator=json_data.get("ComparisonOperator"),
            Statistics=json_data.get("Statistics"),
            Threshold=json_data.get("Threshold"),
            Times=json_data.get("Times"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WarnDefinition = WarnDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


