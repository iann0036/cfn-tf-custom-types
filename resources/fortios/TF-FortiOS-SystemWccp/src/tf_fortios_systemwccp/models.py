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
    AssignmentBucketFormat: Optional[str]
    AssignmentDstaddrMask: Optional[str]
    AssignmentMethod: Optional[str]
    AssignmentSrcaddrMask: Optional[str]
    AssignmentWeight: Optional[float]
    Authentication: Optional[str]
    CacheEngineMethod: Optional[str]
    CacheId: Optional[str]
    ForwardMethod: Optional[str]
    GroupAddress: Optional[str]
    Id: Optional[str]
    Password: Optional[str]
    Ports: Optional[str]
    PortsDefined: Optional[str]
    PrimaryHash: Optional[str]
    Priority: Optional[float]
    Protocol: Optional[float]
    ReturnMethod: Optional[str]
    RouterId: Optional[str]
    RouterList: Optional[str]
    ServerList: Optional[str]
    ServerType: Optional[str]
    ServiceId: Optional[str]
    ServiceType: Optional[str]
    Vdomparam: Optional[str]

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
            AssignmentBucketFormat=json_data.get("AssignmentBucketFormat"),
            AssignmentDstaddrMask=json_data.get("AssignmentDstaddrMask"),
            AssignmentMethod=json_data.get("AssignmentMethod"),
            AssignmentSrcaddrMask=json_data.get("AssignmentSrcaddrMask"),
            AssignmentWeight=json_data.get("AssignmentWeight"),
            Authentication=json_data.get("Authentication"),
            CacheEngineMethod=json_data.get("CacheEngineMethod"),
            CacheId=json_data.get("CacheId"),
            ForwardMethod=json_data.get("ForwardMethod"),
            GroupAddress=json_data.get("GroupAddress"),
            Id=json_data.get("Id"),
            Password=json_data.get("Password"),
            Ports=json_data.get("Ports"),
            PortsDefined=json_data.get("PortsDefined"),
            PrimaryHash=json_data.get("PrimaryHash"),
            Priority=json_data.get("Priority"),
            Protocol=json_data.get("Protocol"),
            ReturnMethod=json_data.get("ReturnMethod"),
            RouterId=json_data.get("RouterId"),
            RouterList=json_data.get("RouterList"),
            ServerList=json_data.get("ServerList"),
            ServerType=json_data.get("ServerType"),
            ServiceId=json_data.get("ServiceId"),
            ServiceType=json_data.get("ServiceType"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


