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
    AlarmId: Optional[str]
    CoolDownTime: Optional[float]
    Id: Optional[str]
    Region: Optional[str]
    ScalingGroupId: Optional[str]
    ScalingPolicyName: Optional[str]
    ScalingPolicyType: Optional[str]
    ScalingPolicyAction: Optional[Sequence["_ScalingPolicyAction"]]
    ScheduledPolicy: Optional[Sequence["_ScheduledPolicy"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AlarmId=json_data.get("AlarmId"),
            CoolDownTime=json_data.get("CoolDownTime"),
            Id=json_data.get("Id"),
            Region=json_data.get("Region"),
            ScalingGroupId=json_data.get("ScalingGroupId"),
            ScalingPolicyName=json_data.get("ScalingPolicyName"),
            ScalingPolicyType=json_data.get("ScalingPolicyType"),
            ScalingPolicyAction=json_data.get("ScalingPolicyAction"),
            ScheduledPolicy=json_data.get("ScheduledPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ScalingPolicyAction:
    InstanceNumber: Optional[float]
    Operation: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScalingPolicyAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScalingPolicyAction"]:
        if not json_data:
            return None
        return cls(
            InstanceNumber=json_data.get("InstanceNumber"),
            Operation=json_data.get("Operation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalingPolicyAction = ScalingPolicyAction


@dataclass
class ScheduledPolicy:
    EndTime: Optional[str]
    LaunchTime: Optional[str]
    RecurrenceType: Optional[str]
    RecurrenceValue: Optional[str]
    StartTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduledPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduledPolicy"]:
        if not json_data:
            return None
        return cls(
            EndTime=json_data.get("EndTime"),
            LaunchTime=json_data.get("LaunchTime"),
            RecurrenceType=json_data.get("RecurrenceType"),
            RecurrenceValue=json_data.get("RecurrenceValue"),
            StartTime=json_data.get("StartTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduledPolicy = ScheduledPolicy


