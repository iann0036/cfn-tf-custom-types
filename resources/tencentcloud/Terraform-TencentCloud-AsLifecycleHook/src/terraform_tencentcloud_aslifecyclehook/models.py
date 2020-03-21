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
    DefaultResult: Optional[str]
    HeartbeatTimeout: Optional[float]
    Id: Optional[str]
    LifecycleHookName: Optional[str]
    LifecycleTransition: Optional[str]
    NotificationMetadata: Optional[str]
    NotificationQueueName: Optional[str]
    NotificationTargetType: Optional[str]
    NotificationTopicName: Optional[str]
    ScalingGroupId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DefaultResult=json_data.get("DefaultResult"),
            HeartbeatTimeout=json_data.get("HeartbeatTimeout"),
            Id=json_data.get("Id"),
            LifecycleHookName=json_data.get("LifecycleHookName"),
            LifecycleTransition=json_data.get("LifecycleTransition"),
            NotificationMetadata=json_data.get("NotificationMetadata"),
            NotificationQueueName=json_data.get("NotificationQueueName"),
            NotificationTargetType=json_data.get("NotificationTargetType"),
            NotificationTopicName=json_data.get("NotificationTopicName"),
            ScalingGroupId=json_data.get("ScalingGroupId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


