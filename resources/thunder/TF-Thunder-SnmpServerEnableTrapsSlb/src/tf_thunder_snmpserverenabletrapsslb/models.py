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
    All: Optional[float]
    ApplicationBufferLimit: Optional[float]
    BwRateLimitExceed: Optional[float]
    BwRateLimitResume: Optional[float]
    GatewayDown: Optional[float]
    GatewayUp: Optional[float]
    Id: Optional[str]
    ServerConnLimit: Optional[float]
    ServerConnResume: Optional[float]
    ServerDisabled: Optional[float]
    ServerDown: Optional[float]
    ServerSelectionFailure: Optional[float]
    ServerUp: Optional[float]
    ServiceConnLimit: Optional[float]
    ServiceConnResume: Optional[float]
    ServiceDown: Optional[float]
    ServiceGroupDown: Optional[float]
    ServiceGroupMemberDown: Optional[float]
    ServiceGroupMemberUp: Optional[float]
    ServiceGroupUp: Optional[float]
    ServiceUp: Optional[float]
    Uuid: Optional[str]
    VipConnlimit: Optional[float]
    VipConnratelimit: Optional[float]
    VipDown: Optional[float]
    VipPortConnlimit: Optional[float]
    VipPortConnratelimit: Optional[float]
    VipPortDown: Optional[float]
    VipPortUp: Optional[float]
    VipUp: Optional[float]

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
            All=json_data.get("All"),
            ApplicationBufferLimit=json_data.get("ApplicationBufferLimit"),
            BwRateLimitExceed=json_data.get("BwRateLimitExceed"),
            BwRateLimitResume=json_data.get("BwRateLimitResume"),
            GatewayDown=json_data.get("GatewayDown"),
            GatewayUp=json_data.get("GatewayUp"),
            Id=json_data.get("Id"),
            ServerConnLimit=json_data.get("ServerConnLimit"),
            ServerConnResume=json_data.get("ServerConnResume"),
            ServerDisabled=json_data.get("ServerDisabled"),
            ServerDown=json_data.get("ServerDown"),
            ServerSelectionFailure=json_data.get("ServerSelectionFailure"),
            ServerUp=json_data.get("ServerUp"),
            ServiceConnLimit=json_data.get("ServiceConnLimit"),
            ServiceConnResume=json_data.get("ServiceConnResume"),
            ServiceDown=json_data.get("ServiceDown"),
            ServiceGroupDown=json_data.get("ServiceGroupDown"),
            ServiceGroupMemberDown=json_data.get("ServiceGroupMemberDown"),
            ServiceGroupMemberUp=json_data.get("ServiceGroupMemberUp"),
            ServiceGroupUp=json_data.get("ServiceGroupUp"),
            ServiceUp=json_data.get("ServiceUp"),
            Uuid=json_data.get("Uuid"),
            VipConnlimit=json_data.get("VipConnlimit"),
            VipConnratelimit=json_data.get("VipConnratelimit"),
            VipDown=json_data.get("VipDown"),
            VipPortConnlimit=json_data.get("VipPortConnlimit"),
            VipPortConnratelimit=json_data.get("VipPortConnratelimit"),
            VipPortDown=json_data.get("VipPortDown"),
            VipPortUp=json_data.get("VipPortUp"),
            VipUp=json_data.get("VipUp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


