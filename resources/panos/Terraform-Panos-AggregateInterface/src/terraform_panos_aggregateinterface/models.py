# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    AdjustTcpMss: Optional[bool]
    Comment: Optional[str]
    CreateDhcpDefaultRoute: Optional[bool]
    DecryptForward: Optional[bool]
    DhcpDefaultRouteMetric: Optional[float]
    DhcpSendHostnameEnable: Optional[bool]
    DhcpSendHostnameValue: Optional[str]
    EnableDhcp: Optional[bool]
    EnableUntaggedSubinterface: Optional[bool]
    Id: Optional[str]
    Ipv4MssAdjust: Optional[float]
    Ipv6Enabled: Optional[bool]
    Ipv6InterfaceId: Optional[str]
    Ipv6MssAdjust: Optional[float]
    ManagementProfile: Optional[str]
    Mode: Optional[str]
    Mtu: Optional[float]
    Name: Optional[str]
    NetflowProfile: Optional[str]
    StaticIps: Optional[Sequence[str]]
    Vsys: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AdjustTcpMss=json_data.get("AdjustTcpMss"),
            Comment=json_data.get("Comment"),
            CreateDhcpDefaultRoute=json_data.get("CreateDhcpDefaultRoute"),
            DecryptForward=json_data.get("DecryptForward"),
            DhcpDefaultRouteMetric=json_data.get("DhcpDefaultRouteMetric"),
            DhcpSendHostnameEnable=json_data.get("DhcpSendHostnameEnable"),
            DhcpSendHostnameValue=json_data.get("DhcpSendHostnameValue"),
            EnableDhcp=json_data.get("EnableDhcp"),
            EnableUntaggedSubinterface=json_data.get("EnableUntaggedSubinterface"),
            Id=json_data.get("Id"),
            Ipv4MssAdjust=json_data.get("Ipv4MssAdjust"),
            Ipv6Enabled=json_data.get("Ipv6Enabled"),
            Ipv6InterfaceId=json_data.get("Ipv6InterfaceId"),
            Ipv6MssAdjust=json_data.get("Ipv6MssAdjust"),
            ManagementProfile=json_data.get("ManagementProfile"),
            Mode=json_data.get("Mode"),
            Mtu=json_data.get("Mtu"),
            Name=json_data.get("Name"),
            NetflowProfile=json_data.get("NetflowProfile"),
            StaticIps=json_data.get("StaticIps"),
            Vsys=json_data.get("Vsys"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


