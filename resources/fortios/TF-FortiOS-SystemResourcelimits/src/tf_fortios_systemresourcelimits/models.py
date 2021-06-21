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
    CustomService: Optional[float]
    DialupTunnel: Optional[float]
    FirewallAddress: Optional[float]
    FirewallAddrgrp: Optional[float]
    FirewallPolicy: Optional[float]
    Id: Optional[str]
    IpsecPhase1: Optional[float]
    IpsecPhase1Interface: Optional[float]
    IpsecPhase2: Optional[float]
    IpsecPhase2Interface: Optional[float]
    LogDiskQuota: Optional[float]
    OnetimeSchedule: Optional[float]
    Proxy: Optional[float]
    RecurringSchedule: Optional[float]
    ServiceGroup: Optional[float]
    Session: Optional[float]
    Sslvpn: Optional[float]
    User: Optional[float]
    UserGroup: Optional[float]
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
            CustomService=json_data.get("CustomService"),
            DialupTunnel=json_data.get("DialupTunnel"),
            FirewallAddress=json_data.get("FirewallAddress"),
            FirewallAddrgrp=json_data.get("FirewallAddrgrp"),
            FirewallPolicy=json_data.get("FirewallPolicy"),
            Id=json_data.get("Id"),
            IpsecPhase1=json_data.get("IpsecPhase1"),
            IpsecPhase1Interface=json_data.get("IpsecPhase1Interface"),
            IpsecPhase2=json_data.get("IpsecPhase2"),
            IpsecPhase2Interface=json_data.get("IpsecPhase2Interface"),
            LogDiskQuota=json_data.get("LogDiskQuota"),
            OnetimeSchedule=json_data.get("OnetimeSchedule"),
            Proxy=json_data.get("Proxy"),
            RecurringSchedule=json_data.get("RecurringSchedule"),
            ServiceGroup=json_data.get("ServiceGroup"),
            Session=json_data.get("Session"),
            Sslvpn=json_data.get("Sslvpn"),
            User=json_data.get("User"),
            UserGroup=json_data.get("UserGroup"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel

