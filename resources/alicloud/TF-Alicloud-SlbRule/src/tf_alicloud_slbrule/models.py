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
    Cookie: Optional[str]
    CookieTimeout: Optional[float]
    DeleteProtectionValidation: Optional[bool]
    Domain: Optional[str]
    FrontendPort: Optional[float]
    HealthCheck: Optional[str]
    HealthCheckConnectPort: Optional[float]
    HealthCheckDomain: Optional[str]
    HealthCheckHttpCode: Optional[str]
    HealthCheckInterval: Optional[float]
    HealthCheckTimeout: Optional[float]
    HealthCheckUri: Optional[str]
    HealthyThreshold: Optional[float]
    Id: Optional[str]
    ListenerSync: Optional[str]
    LoadBalancerId: Optional[str]
    Name: Optional[str]
    Scheduler: Optional[str]
    ServerGroupId: Optional[str]
    StickySession: Optional[str]
    StickySessionType: Optional[str]
    UnhealthyThreshold: Optional[float]
    Url: Optional[str]

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
            Cookie=json_data.get("Cookie"),
            CookieTimeout=json_data.get("CookieTimeout"),
            DeleteProtectionValidation=json_data.get("DeleteProtectionValidation"),
            Domain=json_data.get("Domain"),
            FrontendPort=json_data.get("FrontendPort"),
            HealthCheck=json_data.get("HealthCheck"),
            HealthCheckConnectPort=json_data.get("HealthCheckConnectPort"),
            HealthCheckDomain=json_data.get("HealthCheckDomain"),
            HealthCheckHttpCode=json_data.get("HealthCheckHttpCode"),
            HealthCheckInterval=json_data.get("HealthCheckInterval"),
            HealthCheckTimeout=json_data.get("HealthCheckTimeout"),
            HealthCheckUri=json_data.get("HealthCheckUri"),
            HealthyThreshold=json_data.get("HealthyThreshold"),
            Id=json_data.get("Id"),
            ListenerSync=json_data.get("ListenerSync"),
            LoadBalancerId=json_data.get("LoadBalancerId"),
            Name=json_data.get("Name"),
            Scheduler=json_data.get("Scheduler"),
            ServerGroupId=json_data.get("ServerGroupId"),
            StickySession=json_data.get("StickySession"),
            StickySessionType=json_data.get("StickySessionType"),
            UnhealthyThreshold=json_data.get("UnhealthyThreshold"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


