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
    AutoscalingGroupName: Optional[str]
    DefaultResult: Optional[str]
    HeartbeatTimeout: Optional[float]
    LifecycleTransition: Optional[str]
    Name: Optional[str]
    NotificationMetadata: Optional[str]
    NotificationTargetArn: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AutoscalingGroupName=json_data.get("AutoscalingGroupName"),
            DefaultResult=json_data.get("DefaultResult"),
            HeartbeatTimeout=json_data.get("HeartbeatTimeout"),
            LifecycleTransition=json_data.get("LifecycleTransition"),
            Name=json_data.get("Name"),
            NotificationMetadata=json_data.get("NotificationMetadata"),
            NotificationTargetArn=json_data.get("NotificationTargetArn"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


