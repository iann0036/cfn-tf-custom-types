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
    AggregateGroup: Optional[str]
    Comment: Optional[str]
    CreateDhcpDefaultRoute: Optional[bool]
    DecryptForward: Optional[bool]
    DhcpDefaultRouteMetric: Optional[float]
    DhcpSendHostnameEnable: Optional[bool]
    DhcpSendHostnameValue: Optional[str]
    EnableDhcp: Optional[bool]
    Id: Optional[str]
    Ipv4MssAdjust: Optional[float]
    Ipv6Enabled: Optional[bool]
    Ipv6MssAdjust: Optional[float]
    LacpHaPassivePreNegotiation: Optional[bool]
    LacpPortPriority: Optional[float]
    LinkDuplex: Optional[str]
    LinkSpeed: Optional[str]
    LinkState: Optional[str]
    LldpEnabled: Optional[bool]
    LldpHaPassivePreNegotiation: Optional[bool]
    LldpProfile: Optional[str]
    ManagementProfile: Optional[str]
    Mode: Optional[str]
    Mtu: Optional[float]
    Name: Optional[str]
    NetflowProfile: Optional[str]
    RxPolicingRate: Optional[float]
    StaticIps: Optional[Sequence[str]]
    Template: Optional[str]
    TxPolicingRate: Optional[float]
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
            AggregateGroup=json_data.get("AggregateGroup"),
            Comment=json_data.get("Comment"),
            CreateDhcpDefaultRoute=json_data.get("CreateDhcpDefaultRoute"),
            DecryptForward=json_data.get("DecryptForward"),
            DhcpDefaultRouteMetric=json_data.get("DhcpDefaultRouteMetric"),
            DhcpSendHostnameEnable=json_data.get("DhcpSendHostnameEnable"),
            DhcpSendHostnameValue=json_data.get("DhcpSendHostnameValue"),
            EnableDhcp=json_data.get("EnableDhcp"),
            Id=json_data.get("Id"),
            Ipv4MssAdjust=json_data.get("Ipv4MssAdjust"),
            Ipv6Enabled=json_data.get("Ipv6Enabled"),
            Ipv6MssAdjust=json_data.get("Ipv6MssAdjust"),
            LacpHaPassivePreNegotiation=json_data.get("LacpHaPassivePreNegotiation"),
            LacpPortPriority=json_data.get("LacpPortPriority"),
            LinkDuplex=json_data.get("LinkDuplex"),
            LinkSpeed=json_data.get("LinkSpeed"),
            LinkState=json_data.get("LinkState"),
            LldpEnabled=json_data.get("LldpEnabled"),
            LldpHaPassivePreNegotiation=json_data.get("LldpHaPassivePreNegotiation"),
            LldpProfile=json_data.get("LldpProfile"),
            ManagementProfile=json_data.get("ManagementProfile"),
            Mode=json_data.get("Mode"),
            Mtu=json_data.get("Mtu"),
            Name=json_data.get("Name"),
            NetflowProfile=json_data.get("NetflowProfile"),
            RxPolicingRate=json_data.get("RxPolicingRate"),
            StaticIps=json_data.get("StaticIps"),
            Template=json_data.get("Template"),
            TxPolicingRate=json_data.get("TxPolicingRate"),
            Vsys=json_data.get("Vsys"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


