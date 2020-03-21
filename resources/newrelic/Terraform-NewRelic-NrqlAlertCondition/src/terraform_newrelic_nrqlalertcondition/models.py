# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    Enabled: Optional[bool]
    ExpectedGroups: Optional[float]
    IgnoreOverlap: Optional[bool]
    Name: Optional[str]
    PolicyId: Optional[float]
    RunbookUrl: Optional[str]
    Type: Optional[str]
    ValueFunction: Optional[str]
    ViolationTimeLimitSeconds: Optional[float]
    Nrql: Optional[Sequence["_Nrql"]]
    Term: Optional[Sequence["_Term"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Enabled=json_data.get("Enabled"),
            ExpectedGroups=json_data.get("ExpectedGroups"),
            IgnoreOverlap=json_data.get("IgnoreOverlap"),
            Name=json_data.get("Name"),
            PolicyId=json_data.get("PolicyId"),
            RunbookUrl=json_data.get("RunbookUrl"),
            Type=json_data.get("Type"),
            ValueFunction=json_data.get("ValueFunction"),
            ViolationTimeLimitSeconds=json_data.get("ViolationTimeLimitSeconds"),
            Nrql=json_data.get("Nrql"),
            Term=json_data.get("Term"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Nrql:
    Query: Optional[str]
    SinceValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Nrql"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Nrql"]:
        if not json_data:
            return None
        return cls(
            Query=json_data.get("Query"),
            SinceValue=json_data.get("SinceValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Nrql = Nrql


@dataclass
class Term:
    Duration: Optional[float]
    Operator: Optional[str]
    Priority: Optional[str]
    Threshold: Optional[float]
    TimeFunction: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Term"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Term"]:
        if not json_data:
            return None
        return cls(
            Duration=json_data.get("Duration"),
            Operator=json_data.get("Operator"),
            Priority=json_data.get("Priority"),
            Threshold=json_data.get("Threshold"),
            TimeFunction=json_data.get("TimeFunction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Term = Term


