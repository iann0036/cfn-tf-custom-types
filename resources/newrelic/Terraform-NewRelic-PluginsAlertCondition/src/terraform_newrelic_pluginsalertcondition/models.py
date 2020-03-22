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
    Entities: Optional[Sequence[float]]
    Id: Optional[str]
    Metric: Optional[str]
    MetricDescription: Optional[str]
    Name: Optional[str]
    PluginGuid: Optional[str]
    PluginId: Optional[str]
    PolicyId: Optional[float]
    RunbookUrl: Optional[str]
    ValueFunction: Optional[str]
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
            Entities=json_data.get("Entities"),
            Id=json_data.get("Id"),
            Metric=json_data.get("Metric"),
            MetricDescription=json_data.get("MetricDescription"),
            Name=json_data.get("Name"),
            PluginGuid=json_data.get("PluginGuid"),
            PluginId=json_data.get("PluginId"),
            PolicyId=json_data.get("PolicyId"),
            RunbookUrl=json_data.get("RunbookUrl"),
            ValueFunction=json_data.get("ValueFunction"),
            Term=json_data.get("Term"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


