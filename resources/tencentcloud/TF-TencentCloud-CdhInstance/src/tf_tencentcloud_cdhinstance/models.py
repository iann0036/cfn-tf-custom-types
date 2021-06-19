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
    AvailabilityZone: Optional[str]
    ChargeType: Optional[str]
    CreateTime: Optional[str]
    CvmInstanceIds: Optional[Sequence[str]]
    ExpiredTime: Optional[str]
    HostName: Optional[str]
    HostResource: Optional[Sequence["_HostResourceDefinition"]]
    HostState: Optional[str]
    HostType: Optional[str]
    Id: Optional[str]
    PrepaidPeriod: Optional[float]
    PrepaidRenewFlag: Optional[str]
    ProjectId: Optional[float]

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
            AvailabilityZone=json_data.get("AvailabilityZone"),
            ChargeType=json_data.get("ChargeType"),
            CreateTime=json_data.get("CreateTime"),
            CvmInstanceIds=json_data.get("CvmInstanceIds"),
            ExpiredTime=json_data.get("ExpiredTime"),
            HostName=json_data.get("HostName"),
            HostResource=deserialize_list(json_data.get("HostResource"), HostResourceDefinition),
            HostState=json_data.get("HostState"),
            HostType=json_data.get("HostType"),
            Id=json_data.get("Id"),
            PrepaidPeriod=json_data.get("PrepaidPeriod"),
            PrepaidRenewFlag=json_data.get("PrepaidRenewFlag"),
            ProjectId=json_data.get("ProjectId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class HostResourceDefinition(BaseModel):
    CpuAvailableNum: Optional[float]
    CpuTotalNum: Optional[float]
    DiskAvailableSize: Optional[float]
    DiskTotalSize: Optional[float]
    DiskType: Optional[str]
    MemoryAvailableSize: Optional[float]
    MemoryTotalSize: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HostResourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostResourceDefinition"]:
        if not json_data:
            return None
        return cls(
            CpuAvailableNum=json_data.get("CpuAvailableNum"),
            CpuTotalNum=json_data.get("CpuTotalNum"),
            DiskAvailableSize=json_data.get("DiskAvailableSize"),
            DiskTotalSize=json_data.get("DiskTotalSize"),
            DiskType=json_data.get("DiskType"),
            MemoryAvailableSize=json_data.get("MemoryAvailableSize"),
            MemoryTotalSize=json_data.get("MemoryTotalSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostResourceDefinition = HostResourceDefinition


