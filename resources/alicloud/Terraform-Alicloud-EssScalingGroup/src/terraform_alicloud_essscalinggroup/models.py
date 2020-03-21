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
    DbInstanceIds: Optional[Sequence[str]]
    DefaultCooldown: Optional[float]
    Id: Optional[str]
    LoadbalancerIds: Optional[Sequence[str]]
    MaxSize: Optional[float]
    MinSize: Optional[float]
    MultiAzPolicy: Optional[str]
    OnDemandBaseCapacity: Optional[float]
    OnDemandPercentageAboveBaseCapacity: Optional[float]
    RemovalPolicies: Optional[Sequence[str]]
    ScalingGroupName: Optional[str]
    SpotInstancePools: Optional[float]
    SpotInstanceRemedy: Optional[bool]
    VswitchId: Optional[str]
    VswitchIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DbInstanceIds=json_data.get("DbInstanceIds"),
            DefaultCooldown=json_data.get("DefaultCooldown"),
            Id=json_data.get("Id"),
            LoadbalancerIds=json_data.get("LoadbalancerIds"),
            MaxSize=json_data.get("MaxSize"),
            MinSize=json_data.get("MinSize"),
            MultiAzPolicy=json_data.get("MultiAzPolicy"),
            OnDemandBaseCapacity=json_data.get("OnDemandBaseCapacity"),
            OnDemandPercentageAboveBaseCapacity=json_data.get("OnDemandPercentageAboveBaseCapacity"),
            RemovalPolicies=json_data.get("RemovalPolicies"),
            ScalingGroupName=json_data.get("ScalingGroupName"),
            SpotInstancePools=json_data.get("SpotInstancePools"),
            SpotInstanceRemedy=json_data.get("SpotInstanceRemedy"),
            VswitchId=json_data.get("VswitchId"),
            VswitchIds=json_data.get("VswitchIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


