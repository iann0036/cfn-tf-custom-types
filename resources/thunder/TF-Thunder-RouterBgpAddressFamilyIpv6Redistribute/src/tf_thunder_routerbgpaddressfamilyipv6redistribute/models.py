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
    AsNumber: Optional[str]
    Id: Optional[str]
    ProcessId: Optional[str]
    Sequence: Optional[str]
    Uuid: Optional[str]
    ConnectedCfg: Optional[Sequence["_ConnectedCfgDefinition"]]
    FloatingIpCfg: Optional[Sequence["_FloatingIpCfgDefinition"]]
    IpNatCfg: Optional[Sequence["_IpNatCfgDefinition"]]
    IpNatListCfg: Optional[Sequence["_IpNatListCfgDefinition"]]
    IsisCfg: Optional[Sequence["_IsisCfgDefinition"]]
    Lw4o6Cfg: Optional[Sequence["_Lw4o6CfgDefinition"]]
    Nat64Cfg: Optional[Sequence["_Nat64CfgDefinition"]]
    NatMapCfg: Optional[Sequence["_NatMapCfgDefinition"]]
    OspfCfg: Optional[Sequence["_OspfCfgDefinition"]]
    RipCfg: Optional[Sequence["_RipCfgDefinition"]]
    StaticCfg: Optional[Sequence["_StaticCfgDefinition"]]
    StaticNatCfg: Optional[Sequence["_StaticNatCfgDefinition"]]
    Vip: Optional[Sequence["_VipDefinition"]]

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
            AsNumber=json_data.get("AsNumber"),
            Id=json_data.get("Id"),
            ProcessId=json_data.get("ProcessId"),
            Sequence=json_data.get("Sequence"),
            Uuid=json_data.get("Uuid"),
            ConnectedCfg=deserialize_list(json_data.get("ConnectedCfg"), ConnectedCfgDefinition),
            FloatingIpCfg=deserialize_list(json_data.get("FloatingIpCfg"), FloatingIpCfgDefinition),
            IpNatCfg=deserialize_list(json_data.get("IpNatCfg"), IpNatCfgDefinition),
            IpNatListCfg=deserialize_list(json_data.get("IpNatListCfg"), IpNatListCfgDefinition),
            IsisCfg=deserialize_list(json_data.get("IsisCfg"), IsisCfgDefinition),
            Lw4o6Cfg=deserialize_list(json_data.get("Lw4o6Cfg"), Lw4o6CfgDefinition),
            Nat64Cfg=deserialize_list(json_data.get("Nat64Cfg"), Nat64CfgDefinition),
            NatMapCfg=deserialize_list(json_data.get("NatMapCfg"), NatMapCfgDefinition),
            OspfCfg=deserialize_list(json_data.get("OspfCfg"), OspfCfgDefinition),
            RipCfg=deserialize_list(json_data.get("RipCfg"), RipCfgDefinition),
            StaticCfg=deserialize_list(json_data.get("StaticCfg"), StaticCfgDefinition),
            StaticNatCfg=deserialize_list(json_data.get("StaticNatCfg"), StaticNatCfgDefinition),
            Vip=deserialize_list(json_data.get("Vip"), VipDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConnectedCfgDefinition(BaseModel):
    Connected: Optional[float]
    RouteMap: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectedCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectedCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Connected=json_data.get("Connected"),
            RouteMap=json_data.get("RouteMap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectedCfgDefinition = ConnectedCfgDefinition


@dataclass
class FloatingIpCfgDefinition(BaseModel):
    FloatingIp: Optional[float]
    RouteMap: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FloatingIpCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FloatingIpCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            FloatingIp=json_data.get("FloatingIp"),
            RouteMap=json_data.get("RouteMap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FloatingIpCfgDefinition = FloatingIpCfgDefinition


@dataclass
class IpNatCfgDefinition(BaseModel):
    IpNat: Optional[float]
    RouteMap: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpNatCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpNatCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            IpNat=json_data.get("IpNat"),
            RouteMap=json_data.get("RouteMap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpNatCfgDefinition = IpNatCfgDefinition


@dataclass
class IpNatListCfgDefinition(BaseModel):
    IpNatList: Optional[float]
    RouteMap: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpNatListCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpNatListCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            IpNatList=json_data.get("IpNatList"),
            RouteMap=json_data.get("RouteMap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpNatListCfgDefinition = IpNatListCfgDefinition


@dataclass
class IsisCfgDefinition(BaseModel):
    Isis: Optional[float]
    RouteMap: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IsisCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IsisCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Isis=json_data.get("Isis"),
            RouteMap=json_data.get("RouteMap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IsisCfgDefinition = IsisCfgDefinition


@dataclass
class Lw4o6CfgDefinition(BaseModel):
    Lw4o6: Optional[float]
    RouteMap: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Lw4o6CfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Lw4o6CfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Lw4o6=json_data.get("Lw4o6"),
            RouteMap=json_data.get("RouteMap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Lw4o6CfgDefinition = Lw4o6CfgDefinition


@dataclass
class Nat64CfgDefinition(BaseModel):
    Nat64: Optional[float]
    RouteMap: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Nat64CfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Nat64CfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Nat64=json_data.get("Nat64"),
            RouteMap=json_data.get("RouteMap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Nat64CfgDefinition = Nat64CfgDefinition


@dataclass
class NatMapCfgDefinition(BaseModel):
    NatMap: Optional[float]
    RouteMap: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NatMapCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NatMapCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            NatMap=json_data.get("NatMap"),
            RouteMap=json_data.get("RouteMap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NatMapCfgDefinition = NatMapCfgDefinition


@dataclass
class OspfCfgDefinition(BaseModel):
    Ospf: Optional[float]
    RouteMap: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OspfCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OspfCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Ospf=json_data.get("Ospf"),
            RouteMap=json_data.get("RouteMap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OspfCfgDefinition = OspfCfgDefinition


@dataclass
class RipCfgDefinition(BaseModel):
    Rip: Optional[float]
    RouteMap: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RipCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RipCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Rip=json_data.get("Rip"),
            RouteMap=json_data.get("RouteMap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RipCfgDefinition = RipCfgDefinition


@dataclass
class StaticCfgDefinition(BaseModel):
    RouteMap: Optional[str]
    Static: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_StaticCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StaticCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            RouteMap=json_data.get("RouteMap"),
            Static=json_data.get("Static"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StaticCfgDefinition = StaticCfgDefinition


@dataclass
class StaticNatCfgDefinition(BaseModel):
    RouteMap: Optional[str]
    StaticNat: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_StaticNatCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StaticNatCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            RouteMap=json_data.get("RouteMap"),
            StaticNat=json_data.get("StaticNat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StaticNatCfgDefinition = StaticNatCfgDefinition


@dataclass
class VipDefinition(BaseModel):
    OnlyFlaggedCfg: Optional[Sequence["_OnlyFlaggedCfgDefinition"]]
    OnlyNotFlaggedCfg: Optional[Sequence["_OnlyNotFlaggedCfgDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VipDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VipDefinition"]:
        if not json_data:
            return None
        return cls(
            OnlyFlaggedCfg=deserialize_list(json_data.get("OnlyFlaggedCfg"), OnlyFlaggedCfgDefinition),
            OnlyNotFlaggedCfg=deserialize_list(json_data.get("OnlyNotFlaggedCfg"), OnlyNotFlaggedCfgDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VipDefinition = VipDefinition


@dataclass
class OnlyFlaggedCfgDefinition(BaseModel):
    OnlyFlagged: Optional[float]
    RouteMap: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OnlyFlaggedCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnlyFlaggedCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            OnlyFlagged=json_data.get("OnlyFlagged"),
            RouteMap=json_data.get("RouteMap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnlyFlaggedCfgDefinition = OnlyFlaggedCfgDefinition


@dataclass
class OnlyNotFlaggedCfgDefinition(BaseModel):
    OnlyNotFlagged: Optional[float]
    RouteMap: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OnlyNotFlaggedCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnlyNotFlaggedCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            OnlyNotFlagged=json_data.get("OnlyNotFlagged"),
            RouteMap=json_data.get("RouteMap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnlyNotFlaggedCfgDefinition = OnlyNotFlaggedCfgDefinition


