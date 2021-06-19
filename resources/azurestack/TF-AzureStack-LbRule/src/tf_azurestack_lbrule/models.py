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
    BackendAddressPoolId: Optional[str]
    BackendPort: Optional[float]
    EnableFloatingIp: Optional[bool]
    FrontendIpConfigurationId: Optional[str]
    FrontendIpConfigurationName: Optional[str]
    FrontendPort: Optional[float]
    Id: Optional[str]
    IdleTimeoutInMinutes: Optional[float]
    LoadDistribution: Optional[str]
    LoadbalancerId: Optional[str]
    Name: Optional[str]
    ProbeId: Optional[str]
    Protocol: Optional[str]
    ResourceGroupName: Optional[str]

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
            BackendAddressPoolId=json_data.get("BackendAddressPoolId"),
            BackendPort=json_data.get("BackendPort"),
            EnableFloatingIp=json_data.get("EnableFloatingIp"),
            FrontendIpConfigurationId=json_data.get("FrontendIpConfigurationId"),
            FrontendIpConfigurationName=json_data.get("FrontendIpConfigurationName"),
            FrontendPort=json_data.get("FrontendPort"),
            Id=json_data.get("Id"),
            IdleTimeoutInMinutes=json_data.get("IdleTimeoutInMinutes"),
            LoadDistribution=json_data.get("LoadDistribution"),
            LoadbalancerId=json_data.get("LoadbalancerId"),
            Name=json_data.get("Name"),
            ProbeId=json_data.get("ProbeId"),
            Protocol=json_data.get("Protocol"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


