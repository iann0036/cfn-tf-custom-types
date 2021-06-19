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
    Description: Optional[str]
    DeviceGroup: Optional[str]
    EnableSessionsProtections: Optional[bool]
    Id: Optional[str]
    MaxConcurrentSessions: Optional[float]
    Name: Optional[str]
    Type: Optional[str]
    Vsys: Optional[str]
    Icmp: Optional[Sequence["_IcmpDefinition"]]
    Icmpv6: Optional[Sequence["_Icmpv6Definition"]]
    Other: Optional[Sequence["_OtherDefinition"]]
    Syn: Optional[Sequence["_SynDefinition"]]
    Udp: Optional[Sequence["_UdpDefinition"]]

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
            Description=json_data.get("Description"),
            DeviceGroup=json_data.get("DeviceGroup"),
            EnableSessionsProtections=json_data.get("EnableSessionsProtections"),
            Id=json_data.get("Id"),
            MaxConcurrentSessions=json_data.get("MaxConcurrentSessions"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            Vsys=json_data.get("Vsys"),
            Icmp=deserialize_list(json_data.get("Icmp"), IcmpDefinition),
            Icmpv6=deserialize_list(json_data.get("Icmpv6"), Icmpv6Definition),
            Other=deserialize_list(json_data.get("Other"), OtherDefinition),
            Syn=deserialize_list(json_data.get("Syn"), SynDefinition),
            Udp=deserialize_list(json_data.get("Udp"), UdpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IcmpDefinition(BaseModel):
    ActivateRate: Optional[float]
    AlarmRate: Optional[float]
    BlockDuration: Optional[float]
    Enable: Optional[bool]
    MaxRate: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IcmpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IcmpDefinition"]:
        if not json_data:
            return None
        return cls(
            ActivateRate=json_data.get("ActivateRate"),
            AlarmRate=json_data.get("AlarmRate"),
            BlockDuration=json_data.get("BlockDuration"),
            Enable=json_data.get("Enable"),
            MaxRate=json_data.get("MaxRate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IcmpDefinition = IcmpDefinition


@dataclass
class Icmpv6Definition(BaseModel):
    ActivateRate: Optional[float]
    AlarmRate: Optional[float]
    BlockDuration: Optional[float]
    Enable: Optional[bool]
    MaxRate: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Icmpv6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Icmpv6Definition"]:
        if not json_data:
            return None
        return cls(
            ActivateRate=json_data.get("ActivateRate"),
            AlarmRate=json_data.get("AlarmRate"),
            BlockDuration=json_data.get("BlockDuration"),
            Enable=json_data.get("Enable"),
            MaxRate=json_data.get("MaxRate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Icmpv6Definition = Icmpv6Definition


@dataclass
class OtherDefinition(BaseModel):
    ActivateRate: Optional[float]
    AlarmRate: Optional[float]
    BlockDuration: Optional[float]
    Enable: Optional[bool]
    MaxRate: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_OtherDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OtherDefinition"]:
        if not json_data:
            return None
        return cls(
            ActivateRate=json_data.get("ActivateRate"),
            AlarmRate=json_data.get("AlarmRate"),
            BlockDuration=json_data.get("BlockDuration"),
            Enable=json_data.get("Enable"),
            MaxRate=json_data.get("MaxRate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OtherDefinition = OtherDefinition


@dataclass
class SynDefinition(BaseModel):
    Action: Optional[str]
    ActivateRate: Optional[float]
    AlarmRate: Optional[float]
    BlockDuration: Optional[float]
    Enable: Optional[bool]
    MaxRate: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SynDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SynDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            ActivateRate=json_data.get("ActivateRate"),
            AlarmRate=json_data.get("AlarmRate"),
            BlockDuration=json_data.get("BlockDuration"),
            Enable=json_data.get("Enable"),
            MaxRate=json_data.get("MaxRate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SynDefinition = SynDefinition


@dataclass
class UdpDefinition(BaseModel):
    ActivateRate: Optional[float]
    AlarmRate: Optional[float]
    BlockDuration: Optional[float]
    Enable: Optional[bool]
    MaxRate: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_UdpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UdpDefinition"]:
        if not json_data:
            return None
        return cls(
            ActivateRate=json_data.get("ActivateRate"),
            AlarmRate=json_data.get("AlarmRate"),
            BlockDuration=json_data.get("BlockDuration"),
            Enable=json_data.get("Enable"),
            MaxRate=json_data.get("MaxRate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UdpDefinition = UdpDefinition


