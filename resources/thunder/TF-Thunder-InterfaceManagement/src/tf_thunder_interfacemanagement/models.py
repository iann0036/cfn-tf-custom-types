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
    Action: Optional[str]
    Duplexity: Optional[str]
    FlowControl: Optional[float]
    Id: Optional[str]
    Speed: Optional[str]
    Uuid: Optional[str]
    AccessList: Optional[Sequence["_AccessListDefinition"]]
    BroadcastRateLimit: Optional[Sequence["_BroadcastRateLimitDefinition"]]
    Ip: Optional[Sequence["_IpDefinition"]]
    Ipv6: Optional[Sequence["_Ipv6Definition"]]
    Lldp: Optional[Sequence["_LldpDefinition"]]
    SamplingEnable: Optional[Sequence["_SamplingEnableDefinition"]]
    SecondaryIp: Optional[Sequence["_SecondaryIpDefinition"]]

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
            Action=json_data.get("Action"),
            Duplexity=json_data.get("Duplexity"),
            FlowControl=json_data.get("FlowControl"),
            Id=json_data.get("Id"),
            Speed=json_data.get("Speed"),
            Uuid=json_data.get("Uuid"),
            AccessList=deserialize_list(json_data.get("AccessList"), AccessListDefinition),
            BroadcastRateLimit=deserialize_list(json_data.get("BroadcastRateLimit"), BroadcastRateLimitDefinition),
            Ip=deserialize_list(json_data.get("Ip"), IpDefinition),
            Ipv6=deserialize_list(json_data.get("Ipv6"), Ipv6Definition),
            Lldp=deserialize_list(json_data.get("Lldp"), LldpDefinition),
            SamplingEnable=deserialize_list(json_data.get("SamplingEnable"), SamplingEnableDefinition),
            SecondaryIp=deserialize_list(json_data.get("SecondaryIp"), SecondaryIpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AccessListDefinition(BaseModel):
    AclId: Optional[float]
    AclName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessListDefinition"]:
        if not json_data:
            return None
        return cls(
            AclId=json_data.get("AclId"),
            AclName=json_data.get("AclName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessListDefinition = AccessListDefinition


@dataclass
class BroadcastRateLimitDefinition(BaseModel):
    BcastRateLimitEnable: Optional[float]
    Rate: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_BroadcastRateLimitDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BroadcastRateLimitDefinition"]:
        if not json_data:
            return None
        return cls(
            BcastRateLimitEnable=json_data.get("BcastRateLimitEnable"),
            Rate=json_data.get("Rate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BroadcastRateLimitDefinition = BroadcastRateLimitDefinition


@dataclass
class IpDefinition(BaseModel):
    ControlAppsUseMgmtPort: Optional[float]
    DefaultGateway: Optional[str]
    Dhcp: Optional[float]
    Ipv4Address: Optional[str]
    Ipv4Netmask: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpDefinition"]:
        if not json_data:
            return None
        return cls(
            ControlAppsUseMgmtPort=json_data.get("ControlAppsUseMgmtPort"),
            DefaultGateway=json_data.get("DefaultGateway"),
            Dhcp=json_data.get("Dhcp"),
            Ipv4Address=json_data.get("Ipv4Address"),
            Ipv4Netmask=json_data.get("Ipv4Netmask"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpDefinition = IpDefinition


@dataclass
class Ipv6Definition(BaseModel):
    AddressType: Optional[str]
    DefaultIpv6Gateway: Optional[str]
    Inbound: Optional[float]
    Ipv6Addr: Optional[str]
    V6AclName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv6Definition"]:
        if not json_data:
            return None
        return cls(
            AddressType=json_data.get("AddressType"),
            DefaultIpv6Gateway=json_data.get("DefaultIpv6Gateway"),
            Inbound=json_data.get("Inbound"),
            Ipv6Addr=json_data.get("Ipv6Addr"),
            V6AclName=json_data.get("V6AclName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv6Definition = Ipv6Definition


@dataclass
class LldpDefinition(BaseModel):
    Uuid: Optional[str]
    EnableCfg: Optional[Sequence["_EnableCfgDefinition"]]
    NotificationCfg: Optional[Sequence["_NotificationCfgDefinition"]]
    TxDot1Cfg: Optional[Sequence["_TxDot1CfgDefinition"]]
    TxTlvsCfg: Optional[Sequence["_TxTlvsCfgDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LldpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LldpDefinition"]:
        if not json_data:
            return None
        return cls(
            Uuid=json_data.get("Uuid"),
            EnableCfg=deserialize_list(json_data.get("EnableCfg"), EnableCfgDefinition),
            NotificationCfg=deserialize_list(json_data.get("NotificationCfg"), NotificationCfgDefinition),
            TxDot1Cfg=deserialize_list(json_data.get("TxDot1Cfg"), TxDot1CfgDefinition),
            TxTlvsCfg=deserialize_list(json_data.get("TxTlvsCfg"), TxTlvsCfgDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LldpDefinition = LldpDefinition


@dataclass
class EnableCfgDefinition(BaseModel):
    RtEnable: Optional[float]
    Rx: Optional[float]
    Tx: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_EnableCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnableCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            RtEnable=json_data.get("RtEnable"),
            Rx=json_data.get("Rx"),
            Tx=json_data.get("Tx"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnableCfgDefinition = EnableCfgDefinition


@dataclass
class NotificationCfgDefinition(BaseModel):
    NotifEnable: Optional[float]
    Notification: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            NotifEnable=json_data.get("NotifEnable"),
            Notification=json_data.get("Notification"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationCfgDefinition = NotificationCfgDefinition


@dataclass
class TxDot1CfgDefinition(BaseModel):
    LinkAggregation: Optional[float]
    TxDot1Tlvs: Optional[float]
    Vlan: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TxDot1CfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TxDot1CfgDefinition"]:
        if not json_data:
            return None
        return cls(
            LinkAggregation=json_data.get("LinkAggregation"),
            TxDot1Tlvs=json_data.get("TxDot1Tlvs"),
            Vlan=json_data.get("Vlan"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TxDot1CfgDefinition = TxDot1CfgDefinition


@dataclass
class TxTlvsCfgDefinition(BaseModel):
    Exclude: Optional[float]
    ManagementAddress: Optional[float]
    PortDescription: Optional[float]
    SystemCapabilities: Optional[float]
    SystemDescription: Optional[float]
    SystemName: Optional[float]
    TxTlvs: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TxTlvsCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TxTlvsCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Exclude=json_data.get("Exclude"),
            ManagementAddress=json_data.get("ManagementAddress"),
            PortDescription=json_data.get("PortDescription"),
            SystemCapabilities=json_data.get("SystemCapabilities"),
            SystemDescription=json_data.get("SystemDescription"),
            SystemName=json_data.get("SystemName"),
            TxTlvs=json_data.get("TxTlvs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TxTlvsCfgDefinition = TxTlvsCfgDefinition


@dataclass
class SamplingEnableDefinition(BaseModel):
    Counters1: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SamplingEnableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SamplingEnableDefinition"]:
        if not json_data:
            return None
        return cls(
            Counters1=json_data.get("Counters1"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SamplingEnableDefinition = SamplingEnableDefinition


@dataclass
class SecondaryIpDefinition(BaseModel):
    ControlAppsUseMgmtPort: Optional[float]
    DefaultGateway: Optional[str]
    Dhcp: Optional[float]
    Ipv4Address: Optional[str]
    Ipv4Netmask: Optional[str]
    SecondaryIp: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SecondaryIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecondaryIpDefinition"]:
        if not json_data:
            return None
        return cls(
            ControlAppsUseMgmtPort=json_data.get("ControlAppsUseMgmtPort"),
            DefaultGateway=json_data.get("DefaultGateway"),
            Dhcp=json_data.get("Dhcp"),
            Ipv4Address=json_data.get("Ipv4Address"),
            Ipv4Netmask=json_data.get("Ipv4Netmask"),
            SecondaryIp=json_data.get("SecondaryIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecondaryIpDefinition = SecondaryIpDefinition


