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
    Id: Optional[str]
    Ifnum: Optional[float]
    L3VlanFwdDisable: Optional[float]
    Mtu: Optional[float]
    Name: Optional[str]
    TrapSource: Optional[float]
    UserTag: Optional[str]
    Uuid: Optional[str]
    AccessList: Optional[Sequence["_AccessListDefinition"]]
    Bfd: Optional[Sequence["_BfdDefinition"]]
    Ddos: Optional[Sequence["_DdosDefinition"]]
    IcmpRateLimit: Optional[Sequence["_IcmpRateLimitDefinition"]]
    Icmpv6RateLimit: Optional[Sequence["_Icmpv6RateLimitDefinition"]]
    Ip: Optional[Sequence["_IpDefinition"]]
    Ipv6: Optional[Sequence["_Ipv6Definition"]]
    Isis: Optional[Sequence["_IsisDefinition"]]
    Lw4o6: Optional[Sequence["_Lw4o6Definition"]]
    Map: Optional[Sequence["_MapDefinition"]]
    Nptv6: Optional[Sequence["_Nptv6Definition"]]
    SamplingEnable: Optional[Sequence["_SamplingEnableDefinition"]]

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
            Id=json_data.get("Id"),
            Ifnum=json_data.get("Ifnum"),
            L3VlanFwdDisable=json_data.get("L3VlanFwdDisable"),
            Mtu=json_data.get("Mtu"),
            Name=json_data.get("Name"),
            TrapSource=json_data.get("TrapSource"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            AccessList=deserialize_list(json_data.get("AccessList"), AccessListDefinition),
            Bfd=deserialize_list(json_data.get("Bfd"), BfdDefinition),
            Ddos=deserialize_list(json_data.get("Ddos"), DdosDefinition),
            IcmpRateLimit=deserialize_list(json_data.get("IcmpRateLimit"), IcmpRateLimitDefinition),
            Icmpv6RateLimit=deserialize_list(json_data.get("Icmpv6RateLimit"), Icmpv6RateLimitDefinition),
            Ip=deserialize_list(json_data.get("Ip"), IpDefinition),
            Ipv6=deserialize_list(json_data.get("Ipv6"), Ipv6Definition),
            Isis=deserialize_list(json_data.get("Isis"), IsisDefinition),
            Lw4o6=deserialize_list(json_data.get("Lw4o6"), Lw4o6Definition),
            Map=deserialize_list(json_data.get("Map"), MapDefinition),
            Nptv6=deserialize_list(json_data.get("Nptv6"), Nptv6Definition),
            SamplingEnable=deserialize_list(json_data.get("SamplingEnable"), SamplingEnableDefinition),
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
class BfdDefinition(BaseModel):
    Demand: Optional[float]
    Echo: Optional[float]
    Uuid: Optional[str]
    Authentication: Optional[Sequence["_AuthenticationDefinition"]]
    IntervalCfg: Optional[Sequence["_IntervalCfgDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BfdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BfdDefinition"]:
        if not json_data:
            return None
        return cls(
            Demand=json_data.get("Demand"),
            Echo=json_data.get("Echo"),
            Uuid=json_data.get("Uuid"),
            Authentication=deserialize_list(json_data.get("Authentication"), AuthenticationDefinition),
            IntervalCfg=deserialize_list(json_data.get("IntervalCfg"), IntervalCfgDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BfdDefinition = BfdDefinition


@dataclass
class AuthenticationDefinition(BaseModel):
    KeyChainList: Optional[Sequence["_KeyChainListDefinition"]]
    ModeList: Optional[Sequence["_ModeListDefinition"]]
    SendOnlyList: Optional[Sequence["_SendOnlyListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AuthenticationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthenticationDefinition"]:
        if not json_data:
            return None
        return cls(
            KeyChainList=deserialize_list(json_data.get("KeyChainList"), KeyChainListDefinition),
            ModeList=deserialize_list(json_data.get("ModeList"), ModeListDefinition),
            SendOnlyList=deserialize_list(json_data.get("SendOnlyList"), SendOnlyListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthenticationDefinition = AuthenticationDefinition


@dataclass
class KeyChainListDefinition(BaseModel):
    KeyChain: Optional[str]
    Level: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KeyChainListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyChainListDefinition"]:
        if not json_data:
            return None
        return cls(
            KeyChain=json_data.get("KeyChain"),
            Level=json_data.get("Level"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyChainListDefinition = KeyChainListDefinition


@dataclass
class ModeListDefinition(BaseModel):
    Level: Optional[str]
    Mode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ModeListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ModeListDefinition"]:
        if not json_data:
            return None
        return cls(
            Level=json_data.get("Level"),
            Mode=json_data.get("Mode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ModeListDefinition = ModeListDefinition


@dataclass
class SendOnlyListDefinition(BaseModel):
    Level: Optional[str]
    SendOnly: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SendOnlyListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SendOnlyListDefinition"]:
        if not json_data:
            return None
        return cls(
            Level=json_data.get("Level"),
            SendOnly=json_data.get("SendOnly"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SendOnlyListDefinition = SendOnlyListDefinition


@dataclass
class IntervalCfgDefinition(BaseModel):
    Interval: Optional[float]
    MinRx: Optional[float]
    Multiplier: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IntervalCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntervalCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Interval=json_data.get("Interval"),
            MinRx=json_data.get("MinRx"),
            Multiplier=json_data.get("Multiplier"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntervalCfgDefinition = IntervalCfgDefinition


@dataclass
class DdosDefinition(BaseModel):
    Inside: Optional[float]
    Outside: Optional[float]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DdosDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DdosDefinition"]:
        if not json_data:
            return None
        return cls(
            Inside=json_data.get("Inside"),
            Outside=json_data.get("Outside"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DdosDefinition = DdosDefinition


@dataclass
class IcmpRateLimitDefinition(BaseModel):
    Lockup: Optional[float]
    LockupPeriod: Optional[float]
    Normal: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IcmpRateLimitDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IcmpRateLimitDefinition"]:
        if not json_data:
            return None
        return cls(
            Lockup=json_data.get("Lockup"),
            LockupPeriod=json_data.get("LockupPeriod"),
            Normal=json_data.get("Normal"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IcmpRateLimitDefinition = IcmpRateLimitDefinition


@dataclass
class Icmpv6RateLimitDefinition(BaseModel):
    LockupPeriodV6: Optional[float]
    LockupV6: Optional[float]
    NormalV6: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Icmpv6RateLimitDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Icmpv6RateLimitDefinition"]:
        if not json_data:
            return None
        return cls(
            LockupPeriodV6=json_data.get("LockupPeriodV6"),
            LockupV6=json_data.get("LockupV6"),
            NormalV6=json_data.get("NormalV6"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Icmpv6RateLimitDefinition = Icmpv6RateLimitDefinition


@dataclass
class IpDefinition(BaseModel):
    AllowPromiscuousVip: Optional[float]
    Client: Optional[float]
    Dhcp: Optional[float]
    GenerateMembershipQuery: Optional[float]
    Inside: Optional[float]
    MaxRespTime: Optional[float]
    Outside: Optional[float]
    QueryInterval: Optional[float]
    Server: Optional[float]
    SlbPartitionRedirect: Optional[float]
    TtlIgnore: Optional[float]
    Uuid: Optional[str]
    AddressList: Optional[Sequence["_AddressListDefinition"]]
    HelperAddressList: Optional[Sequence["_HelperAddressListDefinition"]]
    Ospf: Optional[Sequence["_OspfDefinition"]]
    Rip: Optional[Sequence["_RipDefinition"]]
    Router: Optional[Sequence["_RouterDefinition"]]
    StatefulFirewall: Optional[Sequence["_StatefulFirewallDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowPromiscuousVip=json_data.get("AllowPromiscuousVip"),
            Client=json_data.get("Client"),
            Dhcp=json_data.get("Dhcp"),
            GenerateMembershipQuery=json_data.get("GenerateMembershipQuery"),
            Inside=json_data.get("Inside"),
            MaxRespTime=json_data.get("MaxRespTime"),
            Outside=json_data.get("Outside"),
            QueryInterval=json_data.get("QueryInterval"),
            Server=json_data.get("Server"),
            SlbPartitionRedirect=json_data.get("SlbPartitionRedirect"),
            TtlIgnore=json_data.get("TtlIgnore"),
            Uuid=json_data.get("Uuid"),
            AddressList=deserialize_list(json_data.get("AddressList"), AddressListDefinition),
            HelperAddressList=deserialize_list(json_data.get("HelperAddressList"), HelperAddressListDefinition),
            Ospf=deserialize_list(json_data.get("Ospf"), OspfDefinition),
            Rip=deserialize_list(json_data.get("Rip"), RipDefinition),
            Router=deserialize_list(json_data.get("Router"), RouterDefinition),
            StatefulFirewall=deserialize_list(json_data.get("StatefulFirewall"), StatefulFirewallDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpDefinition = IpDefinition


@dataclass
class AddressListDefinition(BaseModel):
    AddressType: Optional[str]
    Ipv6Addr: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AddressListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddressListDefinition"]:
        if not json_data:
            return None
        return cls(
            AddressType=json_data.get("AddressType"),
            Ipv6Addr=json_data.get("Ipv6Addr"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddressListDefinition = AddressListDefinition


@dataclass
class HelperAddressListDefinition(BaseModel):
    HelperAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HelperAddressListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HelperAddressListDefinition"]:
        if not json_data:
            return None
        return cls(
            HelperAddress=json_data.get("HelperAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HelperAddressListDefinition = HelperAddressListDefinition


@dataclass
class OspfDefinition(BaseModel):
    Uuid: Optional[str]
    AreaList: Optional[Sequence["_AreaListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OspfDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OspfDefinition"]:
        if not json_data:
            return None
        return cls(
            Uuid=json_data.get("Uuid"),
            AreaList=deserialize_list(json_data.get("AreaList"), AreaListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OspfDefinition = OspfDefinition


@dataclass
class AreaListDefinition(BaseModel):
    AreaIdAddr: Optional[str]
    AreaIdNum: Optional[float]
    InstanceId: Optional[float]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AreaListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AreaListDefinition"]:
        if not json_data:
            return None
        return cls(
            AreaIdAddr=json_data.get("AreaIdAddr"),
            AreaIdNum=json_data.get("AreaIdNum"),
            InstanceId=json_data.get("InstanceId"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AreaListDefinition = AreaListDefinition


@dataclass
class RipDefinition(BaseModel):
    Uuid: Optional[str]
    SplitHorizonCfg: Optional[Sequence["_SplitHorizonCfgDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RipDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RipDefinition"]:
        if not json_data:
            return None
        return cls(
            Uuid=json_data.get("Uuid"),
            SplitHorizonCfg=deserialize_list(json_data.get("SplitHorizonCfg"), SplitHorizonCfgDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RipDefinition = RipDefinition


@dataclass
class SplitHorizonCfgDefinition(BaseModel):
    State: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SplitHorizonCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SplitHorizonCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            State=json_data.get("State"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SplitHorizonCfgDefinition = SplitHorizonCfgDefinition


@dataclass
class RouterDefinition(BaseModel):
    Isis: Optional[Sequence["_IsisDefinition"]]
    Ospf: Optional[Sequence["_OspfDefinition"]]
    Ripng: Optional[Sequence["_RipngDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RouterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RouterDefinition"]:
        if not json_data:
            return None
        return cls(
            Isis=deserialize_list(json_data.get("Isis"), IsisDefinition),
            Ospf=deserialize_list(json_data.get("Ospf"), OspfDefinition),
            Ripng=deserialize_list(json_data.get("Ripng"), RipngDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RouterDefinition = RouterDefinition


@dataclass
class IsisDefinition(BaseModel):
    Tag: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IsisDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IsisDefinition"]:
        if not json_data:
            return None
        return cls(
            Tag=json_data.get("Tag"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IsisDefinition = IsisDefinition


@dataclass
class RipngDefinition(BaseModel):
    Rip: Optional[float]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RipngDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RipngDefinition"]:
        if not json_data:
            return None
        return cls(
            Rip=json_data.get("Rip"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RipngDefinition = RipngDefinition


@dataclass
class StatefulFirewallDefinition(BaseModel):
    AccessList: Optional[float]
    AclName: Optional[str]
    ClassList: Optional[str]
    Inside: Optional[float]
    Outside: Optional[float]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StatefulFirewallDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatefulFirewallDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessList=json_data.get("AccessList"),
            AclName=json_data.get("AclName"),
            ClassList=json_data.get("ClassList"),
            Inside=json_data.get("Inside"),
            Outside=json_data.get("Outside"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatefulFirewallDefinition = StatefulFirewallDefinition


@dataclass
class Ipv6Definition(BaseModel):
    Inbound: Optional[float]
    Inside: Optional[float]
    Ipv6Enable: Optional[float]
    Outside: Optional[float]
    TtlIgnore: Optional[float]
    Uuid: Optional[str]
    V6AclName: Optional[str]
    AddressList: Optional[Sequence["_AddressListDefinition"]]
    Ospf: Optional[Sequence["_OspfDefinition"]]
    Rip: Optional[Sequence["_RipDefinition"]]
    Router: Optional[Sequence["_RouterDefinition"]]
    RouterAdver: Optional[Sequence["_RouterAdverDefinition"]]
    StatefulFirewall: Optional[Sequence["_StatefulFirewallDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv6Definition"]:
        if not json_data:
            return None
        return cls(
            Inbound=json_data.get("Inbound"),
            Inside=json_data.get("Inside"),
            Ipv6Enable=json_data.get("Ipv6Enable"),
            Outside=json_data.get("Outside"),
            TtlIgnore=json_data.get("TtlIgnore"),
            Uuid=json_data.get("Uuid"),
            V6AclName=json_data.get("V6AclName"),
            AddressList=deserialize_list(json_data.get("AddressList"), AddressListDefinition),
            Ospf=deserialize_list(json_data.get("Ospf"), OspfDefinition),
            Rip=deserialize_list(json_data.get("Rip"), RipDefinition),
            Router=deserialize_list(json_data.get("Router"), RouterDefinition),
            RouterAdver=deserialize_list(json_data.get("RouterAdver"), RouterAdverDefinition),
            StatefulFirewall=deserialize_list(json_data.get("StatefulFirewall"), StatefulFirewallDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv6Definition = Ipv6Definition


@dataclass
class RouterAdverDefinition(BaseModel):
    Action: Optional[str]
    AdverMtu: Optional[float]
    AdverMtuDisable: Optional[float]
    AdverVrid: Optional[float]
    AdverVridDefault: Optional[float]
    DefaultLifetime: Optional[float]
    FloatingIp: Optional[str]
    FloatingIpDefaultVrid: Optional[str]
    HopLimit: Optional[float]
    ManagedConfigAction: Optional[str]
    MaxInterval: Optional[float]
    MinInterval: Optional[float]
    OtherConfigAction: Optional[str]
    RateLimit: Optional[float]
    ReachableTime: Optional[float]
    RetransmitTimer: Optional[float]
    UseFloatingIp: Optional[float]
    UseFloatingIpDefaultVrid: Optional[float]
    PrefixList: Optional[Sequence["_PrefixListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RouterAdverDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RouterAdverDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            AdverMtu=json_data.get("AdverMtu"),
            AdverMtuDisable=json_data.get("AdverMtuDisable"),
            AdverVrid=json_data.get("AdverVrid"),
            AdverVridDefault=json_data.get("AdverVridDefault"),
            DefaultLifetime=json_data.get("DefaultLifetime"),
            FloatingIp=json_data.get("FloatingIp"),
            FloatingIpDefaultVrid=json_data.get("FloatingIpDefaultVrid"),
            HopLimit=json_data.get("HopLimit"),
            ManagedConfigAction=json_data.get("ManagedConfigAction"),
            MaxInterval=json_data.get("MaxInterval"),
            MinInterval=json_data.get("MinInterval"),
            OtherConfigAction=json_data.get("OtherConfigAction"),
            RateLimit=json_data.get("RateLimit"),
            ReachableTime=json_data.get("ReachableTime"),
            RetransmitTimer=json_data.get("RetransmitTimer"),
            UseFloatingIp=json_data.get("UseFloatingIp"),
            UseFloatingIpDefaultVrid=json_data.get("UseFloatingIpDefaultVrid"),
            PrefixList=deserialize_list(json_data.get("PrefixList"), PrefixListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RouterAdverDefinition = RouterAdverDefinition


@dataclass
class PrefixListDefinition(BaseModel):
    NotAutonomous: Optional[float]
    NotOnLink: Optional[float]
    PreferredLifetime: Optional[float]
    Prefix: Optional[str]
    ValidLifetime: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PrefixListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrefixListDefinition"]:
        if not json_data:
            return None
        return cls(
            NotAutonomous=json_data.get("NotAutonomous"),
            NotOnLink=json_data.get("NotOnLink"),
            PreferredLifetime=json_data.get("PreferredLifetime"),
            Prefix=json_data.get("Prefix"),
            ValidLifetime=json_data.get("ValidLifetime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrefixListDefinition = PrefixListDefinition


@dataclass
class Lw4o6Definition(BaseModel):
    Inside: Optional[float]
    Outside: Optional[float]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Lw4o6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Lw4o6Definition"]:
        if not json_data:
            return None
        return cls(
            Inside=json_data.get("Inside"),
            Outside=json_data.get("Outside"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Lw4o6Definition = Lw4o6Definition


@dataclass
class MapDefinition(BaseModel):
    Inside: Optional[float]
    MapTInside: Optional[float]
    MapTOutside: Optional[float]
    Outside: Optional[float]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MapDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MapDefinition"]:
        if not json_data:
            return None
        return cls(
            Inside=json_data.get("Inside"),
            MapTInside=json_data.get("MapTInside"),
            MapTOutside=json_data.get("MapTOutside"),
            Outside=json_data.get("Outside"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MapDefinition = MapDefinition


@dataclass
class Nptv6Definition(BaseModel):
    DomainList: Optional[Sequence["_DomainListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_Nptv6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Nptv6Definition"]:
        if not json_data:
            return None
        return cls(
            DomainList=deserialize_list(json_data.get("DomainList"), DomainListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_Nptv6Definition = Nptv6Definition


@dataclass
class DomainListDefinition(BaseModel):
    BindType: Optional[str]
    DomainName: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DomainListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DomainListDefinition"]:
        if not json_data:
            return None
        return cls(
            BindType=json_data.get("BindType"),
            DomainName=json_data.get("DomainName"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DomainListDefinition = DomainListDefinition


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


