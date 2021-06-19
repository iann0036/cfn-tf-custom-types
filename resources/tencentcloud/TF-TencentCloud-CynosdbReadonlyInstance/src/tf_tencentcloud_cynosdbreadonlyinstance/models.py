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
    ClusterId: Optional[str]
    ForceDelete: Optional[bool]
    Id: Optional[str]
    InstanceCpuCore: Optional[float]
    InstanceMaintainDuration: Optional[float]
    InstanceMaintainStartTime: Optional[float]
    InstanceMaintainWeekdays: Optional[Sequence[str]]
    InstanceMemorySize: Optional[float]
    InstanceName: Optional[str]
    InstanceStatus: Optional[str]
    InstanceStorageSize: Optional[float]

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
            ClusterId=json_data.get("ClusterId"),
            ForceDelete=json_data.get("ForceDelete"),
            Id=json_data.get("Id"),
            InstanceCpuCore=json_data.get("InstanceCpuCore"),
            InstanceMaintainDuration=json_data.get("InstanceMaintainDuration"),
            InstanceMaintainStartTime=json_data.get("InstanceMaintainStartTime"),
            InstanceMaintainWeekdays=json_data.get("InstanceMaintainWeekdays"),
            InstanceMemorySize=json_data.get("InstanceMemorySize"),
            InstanceName=json_data.get("InstanceName"),
            InstanceStatus=json_data.get("InstanceStatus"),
            InstanceStorageSize=json_data.get("InstanceStorageSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


