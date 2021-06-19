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
    DefaultResult: Optional[str]
    HeartbeatTimeout: Optional[float]
    Id: Optional[str]
    LifecycleTransition: Optional[str]
    Name: Optional[str]
    NotificationArn: Optional[str]
    NotificationMetadata: Optional[str]
    ScalingGroupId: Optional[str]

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
            DefaultResult=json_data.get("DefaultResult"),
            HeartbeatTimeout=json_data.get("HeartbeatTimeout"),
            Id=json_data.get("Id"),
            LifecycleTransition=json_data.get("LifecycleTransition"),
            Name=json_data.get("Name"),
            NotificationArn=json_data.get("NotificationArn"),
            NotificationMetadata=json_data.get("NotificationMetadata"),
            ScalingGroupId=json_data.get("ScalingGroupId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


