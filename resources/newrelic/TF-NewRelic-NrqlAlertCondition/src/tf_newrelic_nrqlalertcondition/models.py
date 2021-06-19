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
    AccountId: Optional[float]
    AggregationWindow: Optional[float]
    BaselineDirection: Optional[str]
    CloseViolationsOnExpiration: Optional[bool]
    Description: Optional[str]
    Enabled: Optional[bool]
    ExpectedGroups: Optional[float]
    ExpirationDuration: Optional[float]
    FillOption: Optional[str]
    FillValue: Optional[float]
    Id: Optional[str]
    IgnoreOverlap: Optional[bool]
    Name: Optional[str]
    OpenViolationOnExpiration: Optional[bool]
    OpenViolationOnGroupOverlap: Optional[bool]
    PolicyId: Optional[float]
    RunbookUrl: Optional[str]
    Type: Optional[str]
    ValueFunction: Optional[str]
    ViolationTimeLimit: Optional[str]
    ViolationTimeLimitSeconds: Optional[float]
    Critical: Optional[Sequence["_CriticalDefinition"]]
    Nrql: Optional[Sequence["_NrqlDefinition"]]
    Term: Optional[Sequence["_TermDefinition"]]
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
            AccountId=json_data.get("AccountId"),
            AggregationWindow=json_data.get("AggregationWindow"),
            BaselineDirection=json_data.get("BaselineDirection"),
            CloseViolationsOnExpiration=json_data.get("CloseViolationsOnExpiration"),
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            ExpectedGroups=json_data.get("ExpectedGroups"),
            ExpirationDuration=json_data.get("ExpirationDuration"),
            FillOption=json_data.get("FillOption"),
            FillValue=json_data.get("FillValue"),
            Id=json_data.get("Id"),
            IgnoreOverlap=json_data.get("IgnoreOverlap"),
            Name=json_data.get("Name"),
            OpenViolationOnExpiration=json_data.get("OpenViolationOnExpiration"),
            OpenViolationOnGroupOverlap=json_data.get("OpenViolationOnGroupOverlap"),
            PolicyId=json_data.get("PolicyId"),
            RunbookUrl=json_data.get("RunbookUrl"),
            Type=json_data.get("Type"),
            ValueFunction=json_data.get("ValueFunction"),
            ViolationTimeLimit=json_data.get("ViolationTimeLimit"),
            ViolationTimeLimitSeconds=json_data.get("ViolationTimeLimitSeconds"),
            Critical=deserialize_list(json_data.get("Critical"), CriticalDefinition),
            Nrql=deserialize_list(json_data.get("Nrql"), NrqlDefinition),
            Term=deserialize_list(json_data.get("Term"), TermDefinition),
            Warning=deserialize_list(json_data.get("Warning"), WarningDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CriticalDefinition(BaseModel):
    Duration: Optional[float]
    Operator: Optional[str]
    Threshold: Optional[float]
    ThresholdDuration: Optional[float]
    ThresholdOccurrences: Optional[str]
    TimeFunction: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CriticalDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CriticalDefinition"]:
        if not json_data:
            return None
        return cls(
            Duration=json_data.get("Duration"),
            Operator=json_data.get("Operator"),
            Threshold=json_data.get("Threshold"),
            ThresholdDuration=json_data.get("ThresholdDuration"),
            ThresholdOccurrences=json_data.get("ThresholdOccurrences"),
            TimeFunction=json_data.get("TimeFunction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CriticalDefinition = CriticalDefinition


@dataclass
class NrqlDefinition(BaseModel):
    EvaluationOffset: Optional[float]
    Query: Optional[str]
    SinceValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NrqlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NrqlDefinition"]:
        if not json_data:
            return None
        return cls(
            EvaluationOffset=json_data.get("EvaluationOffset"),
            Query=json_data.get("Query"),
            SinceValue=json_data.get("SinceValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NrqlDefinition = NrqlDefinition


@dataclass
class TermDefinition(BaseModel):
    Duration: Optional[float]
    Operator: Optional[str]
    Priority: Optional[str]
    Threshold: Optional[float]
    ThresholdDuration: Optional[float]
    ThresholdOccurrences: Optional[str]
    TimeFunction: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TermDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TermDefinition"]:
        if not json_data:
            return None
        return cls(
            Duration=json_data.get("Duration"),
            Operator=json_data.get("Operator"),
            Priority=json_data.get("Priority"),
            Threshold=json_data.get("Threshold"),
            ThresholdDuration=json_data.get("ThresholdDuration"),
            ThresholdOccurrences=json_data.get("ThresholdOccurrences"),
            TimeFunction=json_data.get("TimeFunction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TermDefinition = TermDefinition


@dataclass
class WarningDefinition(BaseModel):
    Duration: Optional[float]
    Operator: Optional[str]
    Threshold: Optional[float]
    ThresholdDuration: Optional[float]
    ThresholdOccurrences: Optional[str]
    TimeFunction: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WarningDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WarningDefinition"]:
        if not json_data:
            return None
        return cls(
            Duration=json_data.get("Duration"),
            Operator=json_data.get("Operator"),
            Threshold=json_data.get("Threshold"),
            ThresholdDuration=json_data.get("ThresholdDuration"),
            ThresholdOccurrences=json_data.get("ThresholdOccurrences"),
            TimeFunction=json_data.get("TimeFunction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WarningDefinition = WarningDefinition


