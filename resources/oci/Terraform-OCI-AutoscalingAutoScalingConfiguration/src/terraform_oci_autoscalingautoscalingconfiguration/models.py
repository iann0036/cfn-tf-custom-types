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
    CompartmentId: Optional[str]
    CoolDownInSeconds: Optional[float]
    DefinedTags: Optional[Sequence["_DefinedTags"]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTags"]]
    Id: Optional[str]
    IsEnabled: Optional[bool]
    TimeCreated: Optional[str]
    AutoScalingResources: Optional[Sequence["_AutoScalingResources"]]
    Policies: Optional[Sequence["_Policies"]]
    Timeouts: Optional["_Timeouts"]
    Capacity: Optional[Sequence["_Capacity"]]
    Rules: Optional[Sequence["_Rules"]]
    Action: Optional[Sequence["_Action"]]
    Metric: Optional[Sequence["_Metric"]]
    Threshold: Optional[Sequence["_Threshold"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CompartmentId=json_data.get("CompartmentId"),
            CoolDownInSeconds=json_data.get("CoolDownInSeconds"),
            DefinedTags=json_data.get("DefinedTags"),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=json_data.get("FreeformTags"),
            Id=json_data.get("Id"),
            IsEnabled=json_data.get("IsEnabled"),
            TimeCreated=json_data.get("TimeCreated"),
            AutoScalingResources=json_data.get("AutoScalingResources"),
            Policies=json_data.get("Policies"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Capacity=json_data.get("Capacity"),
            Rules=json_data.get("Rules"),
            Action=json_data.get("Action"),
            Metric=json_data.get("Metric"),
            Threshold=json_data.get("Threshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTags = DefinedTags


@dataclass
class FreeformTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTags = FreeformTags


@dataclass
class AutoScalingResources:
    Id: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AutoScalingResources"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoScalingResources"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoScalingResources = AutoScalingResources


@dataclass
class Policies:
    DisplayName: Optional[str]
    PolicyType: Optional[str]
    Capacity: Optional[Sequence["_Capacity"]]
    Rules: Optional[Sequence["_Rules"]]

    @classmethod
    def _deserialize(
        cls: Type["_Policies"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Policies"]:
        if not json_data:
            return None
        return cls(
            DisplayName=json_data.get("DisplayName"),
            PolicyType=json_data.get("PolicyType"),
            Capacity=json_data.get("Capacity"),
            Rules=json_data.get("Rules"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Policies = Policies


@dataclass
class Capacity:
    Initial: Optional[float]
    Max: Optional[float]
    Min: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Capacity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Capacity"]:
        if not json_data:
            return None
        return cls(
            Initial=json_data.get("Initial"),
            Max=json_data.get("Max"),
            Min=json_data.get("Min"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Capacity = Capacity


@dataclass
class Rules:
    DisplayName: Optional[str]
    Action: Optional[Sequence["_Action"]]
    Metric: Optional[Sequence["_Metric"]]

    @classmethod
    def _deserialize(
        cls: Type["_Rules"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rules"]:
        if not json_data:
            return None
        return cls(
            DisplayName=json_data.get("DisplayName"),
            Action=json_data.get("Action"),
            Metric=json_data.get("Metric"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rules = Rules


@dataclass
class Action:
    Type: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Action"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Action = Action


@dataclass
class Metric:
    MetricType: Optional[str]
    Threshold: Optional[Sequence["_Threshold"]]

    @classmethod
    def _deserialize(
        cls: Type["_Metric"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metric"]:
        if not json_data:
            return None
        return cls(
            MetricType=json_data.get("MetricType"),
            Threshold=json_data.get("Threshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metric = Metric


@dataclass
class Threshold:
    Operator: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Threshold"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Threshold"]:
        if not json_data:
            return None
        return cls(
            Operator=json_data.get("Operator"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Threshold = Threshold


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


