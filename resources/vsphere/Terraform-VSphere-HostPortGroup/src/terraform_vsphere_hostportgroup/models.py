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
    ActiveNics: Optional[Sequence[str]]
    AllowForgedTransmits: Optional[bool]
    AllowMacChanges: Optional[bool]
    AllowPromiscuous: Optional[bool]
    CheckBeacon: Optional[bool]
    ComputedPolicy: Optional[Sequence["_ComputedPolicy"]]
    Failback: Optional[bool]
    HostSystemId: Optional[str]
    Key: Optional[str]
    Name: Optional[str]
    NotifySwitches: Optional[bool]
    Ports: Optional[Sequence["_Ports"]]
    ShapingAverageBandwidth: Optional[float]
    ShapingBurstSize: Optional[float]
    ShapingEnabled: Optional[bool]
    ShapingPeakBandwidth: Optional[float]
    StandbyNics: Optional[Sequence[str]]
    TeamingPolicy: Optional[str]
    VirtualSwitchName: Optional[str]
    VlanId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ActiveNics=json_data.get("ActiveNics"),
            AllowForgedTransmits=json_data.get("AllowForgedTransmits"),
            AllowMacChanges=json_data.get("AllowMacChanges"),
            AllowPromiscuous=json_data.get("AllowPromiscuous"),
            CheckBeacon=json_data.get("CheckBeacon"),
            ComputedPolicy=json_data.get("ComputedPolicy"),
            Failback=json_data.get("Failback"),
            HostSystemId=json_data.get("HostSystemId"),
            Key=json_data.get("Key"),
            Name=json_data.get("Name"),
            NotifySwitches=json_data.get("NotifySwitches"),
            Ports=json_data.get("Ports"),
            ShapingAverageBandwidth=json_data.get("ShapingAverageBandwidth"),
            ShapingBurstSize=json_data.get("ShapingBurstSize"),
            ShapingEnabled=json_data.get("ShapingEnabled"),
            ShapingPeakBandwidth=json_data.get("ShapingPeakBandwidth"),
            StandbyNics=json_data.get("StandbyNics"),
            TeamingPolicy=json_data.get("TeamingPolicy"),
            VirtualSwitchName=json_data.get("VirtualSwitchName"),
            VlanId=json_data.get("VlanId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ComputedPolicy:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ComputedPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComputedPolicy"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComputedPolicy = ComputedPolicy


@dataclass
class Ports:
    Key: Optional[str]
    MacAddresses: Optional[Sequence[str]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ports"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ports"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            MacAddresses=json_data.get("MacAddresses"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ports = Ports


