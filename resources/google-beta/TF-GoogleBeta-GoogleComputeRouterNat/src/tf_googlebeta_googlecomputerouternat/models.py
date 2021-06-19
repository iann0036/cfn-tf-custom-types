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
    DrainNatIps: Optional[Sequence[str]]
    EnableEndpointIndependentMapping: Optional[bool]
    IcmpIdleTimeoutSec: Optional[float]
    Id: Optional[str]
    MinPortsPerVm: Optional[float]
    Name: Optional[str]
    NatIpAllocateOption: Optional[str]
    NatIps: Optional[Sequence[str]]
    Project: Optional[str]
    Region: Optional[str]
    Router: Optional[str]
    SourceSubnetworkIpRangesToNat: Optional[str]
    TcpEstablishedIdleTimeoutSec: Optional[float]
    TcpTransitoryIdleTimeoutSec: Optional[float]
    UdpIdleTimeoutSec: Optional[float]
    LogConfig: Optional[Sequence["_LogConfigDefinition"]]
    Subnetwork: Optional[Sequence["_SubnetworkDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            DrainNatIps=json_data.get("DrainNatIps"),
            EnableEndpointIndependentMapping=json_data.get("EnableEndpointIndependentMapping"),
            IcmpIdleTimeoutSec=json_data.get("IcmpIdleTimeoutSec"),
            Id=json_data.get("Id"),
            MinPortsPerVm=json_data.get("MinPortsPerVm"),
            Name=json_data.get("Name"),
            NatIpAllocateOption=json_data.get("NatIpAllocateOption"),
            NatIps=json_data.get("NatIps"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            Router=json_data.get("Router"),
            SourceSubnetworkIpRangesToNat=json_data.get("SourceSubnetworkIpRangesToNat"),
            TcpEstablishedIdleTimeoutSec=json_data.get("TcpEstablishedIdleTimeoutSec"),
            TcpTransitoryIdleTimeoutSec=json_data.get("TcpTransitoryIdleTimeoutSec"),
            UdpIdleTimeoutSec=json_data.get("UdpIdleTimeoutSec"),
            LogConfig=deserialize_list(json_data.get("LogConfig"), LogConfigDefinition),
            Subnetwork=deserialize_list(json_data.get("Subnetwork"), SubnetworkDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LogConfigDefinition(BaseModel):
    Enable: Optional[bool]
    Filter: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Enable=json_data.get("Enable"),
            Filter=json_data.get("Filter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogConfigDefinition = LogConfigDefinition


@dataclass
class SubnetworkDefinition(BaseModel):
    Name: Optional[str]
    SecondaryIpRangeNames: Optional[Sequence[str]]
    SourceIpRangesToNat: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SubnetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubnetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            SecondaryIpRangeNames=json_data.get("SecondaryIpRangeNames"),
            SourceIpRangesToNat=json_data.get("SourceIpRangesToNat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubnetworkDefinition = SubnetworkDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


