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
    ContactGroups: Optional[Sequence[str]]
    Dimensions: Optional[Sequence["_Dimensions"]]
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

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ContactGroups=json_data.get("ContactGroups"),
            Dimensions=json_data.get("Dimensions"),
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
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Dimensions:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Dimensions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Dimensions"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Dimensions = Dimensions


