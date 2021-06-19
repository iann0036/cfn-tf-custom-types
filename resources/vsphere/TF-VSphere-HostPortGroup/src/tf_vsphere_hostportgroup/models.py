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
    ActiveNics: Optional[Sequence[str]]
    AllowForgedTransmits: Optional[bool]
    AllowMacChanges: Optional[bool]
    AllowPromiscuous: Optional[bool]
    CheckBeacon: Optional[bool]
    ComputedPolicy: Optional[Sequence["_ComputedPolicyDefinition"]]
    Failback: Optional[bool]
    HostSystemId: Optional[str]
    Id: Optional[str]
    Key: Optional[str]
    Name: Optional[str]
    NotifySwitches: Optional[bool]
    Ports: Optional[Sequence["_PortsDefinition"]]
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
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ActiveNics=json_data.get("ActiveNics"),
            AllowForgedTransmits=json_data.get("AllowForgedTransmits"),
            AllowMacChanges=json_data.get("AllowMacChanges"),
            AllowPromiscuous=json_data.get("AllowPromiscuous"),
            CheckBeacon=json_data.get("CheckBeacon"),
            ComputedPolicy=deserialize_list(json_data.get("ComputedPolicy"), ComputedPolicyDefinition),
            Failback=json_data.get("Failback"),
            HostSystemId=json_data.get("HostSystemId"),
            Id=json_data.get("Id"),
            Key=json_data.get("Key"),
            Name=json_data.get("Name"),
            NotifySwitches=json_data.get("NotifySwitches"),
            Ports=deserialize_list(json_data.get("Ports"), PortsDefinition),
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
class ComputedPolicyDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ComputedPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComputedPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComputedPolicyDefinition = ComputedPolicyDefinition


@dataclass
class PortsDefinition(BaseModel):
    Key: Optional[str]
    MacAddresses: Optional[Sequence[str]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PortsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            MacAddresses=json_data.get("MacAddresses"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortsDefinition = PortsDefinition


