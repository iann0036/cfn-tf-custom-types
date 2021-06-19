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
    BeaconInterval: Optional[float]
    CheckBeacon: Optional[bool]
    Failback: Optional[bool]
    HostSystemId: Optional[str]
    Id: Optional[str]
    LinkDiscoveryOperation: Optional[str]
    LinkDiscoveryProtocol: Optional[str]
    Mtu: Optional[float]
    Name: Optional[str]
    NetworkAdapters: Optional[Sequence[str]]
    NotifySwitches: Optional[bool]
    NumberOfPorts: Optional[float]
    ShapingAverageBandwidth: Optional[float]
    ShapingBurstSize: Optional[float]
    ShapingEnabled: Optional[bool]
    ShapingPeakBandwidth: Optional[float]
    StandbyNics: Optional[Sequence[str]]
    TeamingPolicy: Optional[str]

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
            BeaconInterval=json_data.get("BeaconInterval"),
            CheckBeacon=json_data.get("CheckBeacon"),
            Failback=json_data.get("Failback"),
            HostSystemId=json_data.get("HostSystemId"),
            Id=json_data.get("Id"),
            LinkDiscoveryOperation=json_data.get("LinkDiscoveryOperation"),
            LinkDiscoveryProtocol=json_data.get("LinkDiscoveryProtocol"),
            Mtu=json_data.get("Mtu"),
            Name=json_data.get("Name"),
            NetworkAdapters=json_data.get("NetworkAdapters"),
            NotifySwitches=json_data.get("NotifySwitches"),
            NumberOfPorts=json_data.get("NumberOfPorts"),
            ShapingAverageBandwidth=json_data.get("ShapingAverageBandwidth"),
            ShapingBurstSize=json_data.get("ShapingBurstSize"),
            ShapingEnabled=json_data.get("ShapingEnabled"),
            ShapingPeakBandwidth=json_data.get("ShapingPeakBandwidth"),
            StandbyNics=json_data.get("StandbyNics"),
            TeamingPolicy=json_data.get("TeamingPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


