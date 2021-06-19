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
    AdjustmentType: Optional[str]
    AdjustmentValue: Optional[float]
    ComparisonOperator: Optional[str]
    ContinuousTime: Optional[float]
    Cooldown: Optional[float]
    Id: Optional[str]
    MetricName: Optional[str]
    NotificationUserGroupIds: Optional[Sequence[str]]
    Period: Optional[float]
    PolicyName: Optional[str]
    ScalingGroupId: Optional[str]
    Statistic: Optional[str]
    Threshold: Optional[float]

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
            AdjustmentType=json_data.get("AdjustmentType"),
            AdjustmentValue=json_data.get("AdjustmentValue"),
            ComparisonOperator=json_data.get("ComparisonOperator"),
            ContinuousTime=json_data.get("ContinuousTime"),
            Cooldown=json_data.get("Cooldown"),
            Id=json_data.get("Id"),
            MetricName=json_data.get("MetricName"),
            NotificationUserGroupIds=json_data.get("NotificationUserGroupIds"),
            Period=json_data.get("Period"),
            PolicyName=json_data.get("PolicyName"),
            ScalingGroupId=json_data.get("ScalingGroupId"),
            Statistic=json_data.get("Statistic"),
            Threshold=json_data.get("Threshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


