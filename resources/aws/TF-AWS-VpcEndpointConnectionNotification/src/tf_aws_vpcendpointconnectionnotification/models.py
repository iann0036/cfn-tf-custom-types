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
    ConnectionEvents: Optional[Sequence[str]]
    ConnectionNotificationArn: Optional[str]
    Id: Optional[str]
    NotificationType: Optional[str]
    State: Optional[str]
    VpcEndpointId: Optional[str]
    VpcEndpointServiceId: Optional[str]

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
            ConnectionEvents=json_data.get("ConnectionEvents"),
            ConnectionNotificationArn=json_data.get("ConnectionNotificationArn"),
            Id=json_data.get("Id"),
            NotificationType=json_data.get("NotificationType"),
            State=json_data.get("State"),
            VpcEndpointId=json_data.get("VpcEndpointId"),
            VpcEndpointServiceId=json_data.get("VpcEndpointServiceId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


