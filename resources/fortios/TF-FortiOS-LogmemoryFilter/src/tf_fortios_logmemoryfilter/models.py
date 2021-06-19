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
    Admin: Optional[str]
    Anomaly: Optional[str]
    Auth: Optional[str]
    CpuMemoryUsage: Optional[str]
    Dhcp: Optional[str]
    Dns: Optional[str]
    DynamicSortSubtable: Optional[str]
    Event: Optional[str]
    Filter: Optional[str]
    FilterType: Optional[str]
    ForwardTraffic: Optional[str]
    Gtp: Optional[str]
    Ha: Optional[str]
    Id: Optional[str]
    Ipsec: Optional[str]
    LdbMonitor: Optional[str]
    LocalTraffic: Optional[str]
    MulticastTraffic: Optional[str]
    NetscanDiscovery: Optional[str]
    NetscanVulnerability: Optional[str]
    Pattern: Optional[str]
    Ppp: Optional[str]
    Radius: Optional[str]
    Severity: Optional[str]
    SnifferTraffic: Optional[str]
    Ssh: Optional[str]
    SslvpnLogAdm: Optional[str]
    SslvpnLogAuth: Optional[str]
    SslvpnLogSession: Optional[str]
    System: Optional[str]
    Vdomparam: Optional[str]
    VipSsl: Optional[str]
    Voip: Optional[str]
    WanOpt: Optional[str]
    WirelessActivity: Optional[str]
    FreeStyle: Optional[Sequence["_FreeStyleDefinition"]]

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
            Admin=json_data.get("Admin"),
            Anomaly=json_data.get("Anomaly"),
            Auth=json_data.get("Auth"),
            CpuMemoryUsage=json_data.get("CpuMemoryUsage"),
            Dhcp=json_data.get("Dhcp"),
            Dns=json_data.get("Dns"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Event=json_data.get("Event"),
            Filter=json_data.get("Filter"),
            FilterType=json_data.get("FilterType"),
            ForwardTraffic=json_data.get("ForwardTraffic"),
            Gtp=json_data.get("Gtp"),
            Ha=json_data.get("Ha"),
            Id=json_data.get("Id"),
            Ipsec=json_data.get("Ipsec"),
            LdbMonitor=json_data.get("LdbMonitor"),
            LocalTraffic=json_data.get("LocalTraffic"),
            MulticastTraffic=json_data.get("MulticastTraffic"),
            NetscanDiscovery=json_data.get("NetscanDiscovery"),
            NetscanVulnerability=json_data.get("NetscanVulnerability"),
            Pattern=json_data.get("Pattern"),
            Ppp=json_data.get("Ppp"),
            Radius=json_data.get("Radius"),
            Severity=json_data.get("Severity"),
            SnifferTraffic=json_data.get("SnifferTraffic"),
            Ssh=json_data.get("Ssh"),
            SslvpnLogAdm=json_data.get("SslvpnLogAdm"),
            SslvpnLogAuth=json_data.get("SslvpnLogAuth"),
            SslvpnLogSession=json_data.get("SslvpnLogSession"),
            System=json_data.get("System"),
            Vdomparam=json_data.get("Vdomparam"),
            VipSsl=json_data.get("VipSsl"),
            Voip=json_data.get("Voip"),
            WanOpt=json_data.get("WanOpt"),
            WirelessActivity=json_data.get("WirelessActivity"),
            FreeStyle=deserialize_list(json_data.get("FreeStyle"), FreeStyleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FreeStyleDefinition(BaseModel):
    Category: Optional[str]
    Filter: Optional[str]
    FilterType: Optional[str]
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_FreeStyleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeStyleDefinition"]:
        if not json_data:
            return None
        return cls(
            Category=json_data.get("Category"),
            Filter=json_data.get("Filter"),
            FilterType=json_data.get("FilterType"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeStyleDefinition = FreeStyleDefinition


