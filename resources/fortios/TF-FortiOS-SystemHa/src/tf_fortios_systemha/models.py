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
    Arps: Optional[float]
    ArpsInterval: Optional[float]
    Authentication: Optional[str]
    CpuThreshold: Optional[str]
    DynamicSortSubtable: Optional[str]
    Encryption: Optional[str]
    FtpProxyThreshold: Optional[str]
    GratuitousArps: Optional[str]
    GroupId: Optional[float]
    GroupName: Optional[str]
    HaDirect: Optional[str]
    HaEthType: Optional[str]
    HaMgmtStatus: Optional[str]
    HaUptimeDiffMargin: Optional[float]
    HbInterval: Optional[float]
    HbLostThreshold: Optional[float]
    Hbdev: Optional[str]
    HcEthType: Optional[str]
    HelloHolddown: Optional[float]
    HttpProxyThreshold: Optional[str]
    Id: Optional[str]
    ImapProxyThreshold: Optional[str]
    InterClusterSessionSync: Optional[str]
    Key: Optional[str]
    L2epEthType: Optional[str]
    LinkFailedSignal: Optional[str]
    LoadBalanceAll: Optional[str]
    LogicalSn: Optional[str]
    MemoryCompatibleMode: Optional[str]
    MemoryThreshold: Optional[str]
    Mode: Optional[str]
    Monitor: Optional[str]
    MulticastTtl: Optional[float]
    NntpProxyThreshold: Optional[str]
    Override: Optional[str]
    OverrideWaitTime: Optional[float]
    Password: Optional[str]
    PingserverFailoverThreshold: Optional[float]
    PingserverFlipTimeout: Optional[float]
    PingserverMonitorInterface: Optional[str]
    PingserverSecondaryForceReset: Optional[str]
    PingserverSlaveForceReset: Optional[str]
    Pop3ProxyThreshold: Optional[str]
    Priority: Optional[float]
    RouteHold: Optional[float]
    RouteTtl: Optional[float]
    RouteWait: Optional[float]
    Schedule: Optional[str]
    SessionPickup: Optional[str]
    SessionPickupConnectionless: Optional[str]
    SessionPickupDelay: Optional[str]
    SessionPickupExpectation: Optional[str]
    SessionPickupNat: Optional[str]
    SessionSyncDev: Optional[str]
    SmtpProxyThreshold: Optional[str]
    SsdFailover: Optional[str]
    StandaloneConfigSync: Optional[str]
    StandaloneMgmtVdom: Optional[str]
    SyncConfig: Optional[str]
    SyncPacketBalance: Optional[str]
    UnicastHb: Optional[str]
    UnicastHbNetmask: Optional[str]
    UnicastHbPeerip: Optional[str]
    UninterruptibleUpgrade: Optional[str]
    Vcluster2: Optional[str]
    VclusterId: Optional[float]
    Vdom: Optional[str]
    Vdomparam: Optional[str]
    Weight: Optional[str]
    HaMgmtInterfaces: Optional[Sequence["_HaMgmtInterfacesDefinition"]]
    SecondaryVcluster: Optional[Sequence["_SecondaryVclusterDefinition"]]

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
            Arps=json_data.get("Arps"),
            ArpsInterval=json_data.get("ArpsInterval"),
            Authentication=json_data.get("Authentication"),
            CpuThreshold=json_data.get("CpuThreshold"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Encryption=json_data.get("Encryption"),
            FtpProxyThreshold=json_data.get("FtpProxyThreshold"),
            GratuitousArps=json_data.get("GratuitousArps"),
            GroupId=json_data.get("GroupId"),
            GroupName=json_data.get("GroupName"),
            HaDirect=json_data.get("HaDirect"),
            HaEthType=json_data.get("HaEthType"),
            HaMgmtStatus=json_data.get("HaMgmtStatus"),
            HaUptimeDiffMargin=json_data.get("HaUptimeDiffMargin"),
            HbInterval=json_data.get("HbInterval"),
            HbLostThreshold=json_data.get("HbLostThreshold"),
            Hbdev=json_data.get("Hbdev"),
            HcEthType=json_data.get("HcEthType"),
            HelloHolddown=json_data.get("HelloHolddown"),
            HttpProxyThreshold=json_data.get("HttpProxyThreshold"),
            Id=json_data.get("Id"),
            ImapProxyThreshold=json_data.get("ImapProxyThreshold"),
            InterClusterSessionSync=json_data.get("InterClusterSessionSync"),
            Key=json_data.get("Key"),
            L2epEthType=json_data.get("L2epEthType"),
            LinkFailedSignal=json_data.get("LinkFailedSignal"),
            LoadBalanceAll=json_data.get("LoadBalanceAll"),
            LogicalSn=json_data.get("LogicalSn"),
            MemoryCompatibleMode=json_data.get("MemoryCompatibleMode"),
            MemoryThreshold=json_data.get("MemoryThreshold"),
            Mode=json_data.get("Mode"),
            Monitor=json_data.get("Monitor"),
            MulticastTtl=json_data.get("MulticastTtl"),
            NntpProxyThreshold=json_data.get("NntpProxyThreshold"),
            Override=json_data.get("Override"),
            OverrideWaitTime=json_data.get("OverrideWaitTime"),
            Password=json_data.get("Password"),
            PingserverFailoverThreshold=json_data.get("PingserverFailoverThreshold"),
            PingserverFlipTimeout=json_data.get("PingserverFlipTimeout"),
            PingserverMonitorInterface=json_data.get("PingserverMonitorInterface"),
            PingserverSecondaryForceReset=json_data.get("PingserverSecondaryForceReset"),
            PingserverSlaveForceReset=json_data.get("PingserverSlaveForceReset"),
            Pop3ProxyThreshold=json_data.get("Pop3ProxyThreshold"),
            Priority=json_data.get("Priority"),
            RouteHold=json_data.get("RouteHold"),
            RouteTtl=json_data.get("RouteTtl"),
            RouteWait=json_data.get("RouteWait"),
            Schedule=json_data.get("Schedule"),
            SessionPickup=json_data.get("SessionPickup"),
            SessionPickupConnectionless=json_data.get("SessionPickupConnectionless"),
            SessionPickupDelay=json_data.get("SessionPickupDelay"),
            SessionPickupExpectation=json_data.get("SessionPickupExpectation"),
            SessionPickupNat=json_data.get("SessionPickupNat"),
            SessionSyncDev=json_data.get("SessionSyncDev"),
            SmtpProxyThreshold=json_data.get("SmtpProxyThreshold"),
            SsdFailover=json_data.get("SsdFailover"),
            StandaloneConfigSync=json_data.get("StandaloneConfigSync"),
            StandaloneMgmtVdom=json_data.get("StandaloneMgmtVdom"),
            SyncConfig=json_data.get("SyncConfig"),
            SyncPacketBalance=json_data.get("SyncPacketBalance"),
            UnicastHb=json_data.get("UnicastHb"),
            UnicastHbNetmask=json_data.get("UnicastHbNetmask"),
            UnicastHbPeerip=json_data.get("UnicastHbPeerip"),
            UninterruptibleUpgrade=json_data.get("UninterruptibleUpgrade"),
            Vcluster2=json_data.get("Vcluster2"),
            VclusterId=json_data.get("VclusterId"),
            Vdom=json_data.get("Vdom"),
            Vdomparam=json_data.get("Vdomparam"),
            Weight=json_data.get("Weight"),
            HaMgmtInterfaces=deserialize_list(json_data.get("HaMgmtInterfaces"), HaMgmtInterfacesDefinition),
            SecondaryVcluster=deserialize_list(json_data.get("SecondaryVcluster"), SecondaryVclusterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class HaMgmtInterfacesDefinition(BaseModel):
    Dst: Optional[str]
    Gateway: Optional[str]
    Gateway6: Optional[str]
    Id: Optional[float]
    Interface: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HaMgmtInterfacesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HaMgmtInterfacesDefinition"]:
        if not json_data:
            return None
        return cls(
            Dst=json_data.get("Dst"),
            Gateway=json_data.get("Gateway"),
            Gateway6=json_data.get("Gateway6"),
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HaMgmtInterfacesDefinition = HaMgmtInterfacesDefinition


@dataclass
class SecondaryVclusterDefinition(BaseModel):
    Monitor: Optional[str]
    Override: Optional[str]
    OverrideWaitTime: Optional[float]
    PingserverFailoverThreshold: Optional[float]
    PingserverMonitorInterface: Optional[str]
    PingserverSecondaryForceReset: Optional[str]
    PingserverSlaveForceReset: Optional[str]
    Priority: Optional[float]
    VclusterId: Optional[float]
    Vdom: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecondaryVclusterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecondaryVclusterDefinition"]:
        if not json_data:
            return None
        return cls(
            Monitor=json_data.get("Monitor"),
            Override=json_data.get("Override"),
            OverrideWaitTime=json_data.get("OverrideWaitTime"),
            PingserverFailoverThreshold=json_data.get("PingserverFailoverThreshold"),
            PingserverMonitorInterface=json_data.get("PingserverMonitorInterface"),
            PingserverSecondaryForceReset=json_data.get("PingserverSecondaryForceReset"),
            PingserverSlaveForceReset=json_data.get("PingserverSlaveForceReset"),
            Priority=json_data.get("Priority"),
            VclusterId=json_data.get("VclusterId"),
            Vdom=json_data.get("Vdom"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecondaryVclusterDefinition = SecondaryVclusterDefinition


