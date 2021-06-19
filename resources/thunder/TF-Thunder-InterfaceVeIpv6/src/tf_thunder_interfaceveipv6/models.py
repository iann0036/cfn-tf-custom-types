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
    Id: Optional[str]
    Ifnum: Optional[float]
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
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Id=json_data.get("Id"),
            Ifnum=json_data.get("Ifnum"),
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
_ResourceModel = ResourceModel


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


