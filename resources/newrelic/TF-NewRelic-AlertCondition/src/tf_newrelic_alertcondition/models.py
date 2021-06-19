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
    ConditionScope: Optional[str]
    Enabled: Optional[bool]
    Entities: Optional[Sequence[float]]
    GcMetric: Optional[str]
    Id: Optional[str]
    Metric: Optional[str]
    Name: Optional[str]
    PolicyId: Optional[float]
    RunbookUrl: Optional[str]
    Type: Optional[str]
    UserDefinedMetric: Optional[str]
    UserDefinedValueFunction: Optional[str]
    ViolationCloseTimer: Optional[float]
    Term: Optional[Sequence["_TermDefinition"]]

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
            ConditionScope=json_data.get("ConditionScope"),
            Enabled=json_data.get("Enabled"),
            Entities=json_data.get("Entities"),
            GcMetric=json_data.get("GcMetric"),
            Id=json_data.get("Id"),
            Metric=json_data.get("Metric"),
            Name=json_data.get("Name"),
            PolicyId=json_data.get("PolicyId"),
            RunbookUrl=json_data.get("RunbookUrl"),
            Type=json_data.get("Type"),
            UserDefinedMetric=json_data.get("UserDefinedMetric"),
            UserDefinedValueFunction=json_data.get("UserDefinedValueFunction"),
            ViolationCloseTimer=json_data.get("ViolationCloseTimer"),
            Term=deserialize_list(json_data.get("Term"), TermDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TermDefinition(BaseModel):
    Duration: Optional[float]
    Operator: Optional[str]
    Priority: Optional[str]
    Threshold: Optional[float]
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
            TimeFunction=json_data.get("TimeFunction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TermDefinition = TermDefinition


