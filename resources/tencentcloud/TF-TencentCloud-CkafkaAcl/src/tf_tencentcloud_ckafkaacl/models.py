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
    Host: Optional[str]
    Id: Optional[str]
    InstanceId: Optional[str]
    OperationType: Optional[str]
    PermissionType: Optional[str]
    Principal: Optional[str]
    ResourceName: Optional[str]
    ResourceType: Optional[str]

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
            Host=json_data.get("Host"),
            Id=json_data.get("Id"),
            InstanceId=json_data.get("InstanceId"),
            OperationType=json_data.get("OperationType"),
            PermissionType=json_data.get("PermissionType"),
            Principal=json_data.get("Principal"),
            ResourceName=json_data.get("ResourceName"),
            ResourceType=json_data.get("ResourceType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


