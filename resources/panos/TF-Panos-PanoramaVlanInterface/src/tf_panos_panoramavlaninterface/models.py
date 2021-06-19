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
    AdjustTcpMss: Optional[bool]
    Comment: Optional[str]
    CreateDhcpDefaultRoute: Optional[bool]
    DhcpDefaultRouteMetric: Optional[float]
    EnableDhcp: Optional[bool]
    Id: Optional[str]
    Ipv4MssAdjust: Optional[float]
    Ipv6MssAdjust: Optional[float]
    ManagementProfile: Optional[str]
    Mtu: Optional[float]
    Name: Optional[str]
    NetflowProfile: Optional[str]
    StaticIps: Optional[Sequence[str]]
    Template: Optional[str]
    Vsys: Optional[str]

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
            AdjustTcpMss=json_data.get("AdjustTcpMss"),
            Comment=json_data.get("Comment"),
            CreateDhcpDefaultRoute=json_data.get("CreateDhcpDefaultRoute"),
            DhcpDefaultRouteMetric=json_data.get("DhcpDefaultRouteMetric"),
            EnableDhcp=json_data.get("EnableDhcp"),
            Id=json_data.get("Id"),
            Ipv4MssAdjust=json_data.get("Ipv4MssAdjust"),
            Ipv6MssAdjust=json_data.get("Ipv6MssAdjust"),
            ManagementProfile=json_data.get("ManagementProfile"),
            Mtu=json_data.get("Mtu"),
            Name=json_data.get("Name"),
            NetflowProfile=json_data.get("NetflowProfile"),
            StaticIps=json_data.get("StaticIps"),
            Template=json_data.get("Template"),
            Vsys=json_data.get("Vsys"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


