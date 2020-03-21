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
    DrainNatIps: Optional[Sequence[str]]
    IcmpIdleTimeoutSec: Optional[float]
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
    LogConfig: Optional[Sequence["_LogConfig"]]
    Subnetwork: Optional[Sequence["_Subnetwork"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DrainNatIps=json_data.get("DrainNatIps"),
            IcmpIdleTimeoutSec=json_data.get("IcmpIdleTimeoutSec"),
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
            LogConfig=json_data.get("LogConfig"),
            Subnetwork=json_data.get("Subnetwork"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LogConfig:
    Enable: Optional[bool]
    Filter: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogConfig"]:
        if not json_data:
            return None
        return cls(
            Enable=json_data.get("Enable"),
            Filter=json_data.get("Filter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogConfig = LogConfig


@dataclass
class Subnetwork:
    Name: Optional[str]
    SecondaryIpRangeNames: Optional[Sequence[str]]
    SourceIpRangesToNat: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Subnetwork"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Subnetwork"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            SecondaryIpRangeNames=json_data.get("SecondaryIpRangeNames"),
            SourceIpRangesToNat=json_data.get("SourceIpRangesToNat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Subnetwork = Subnetwork


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


