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
    AbleToFileTransfer: Optional[bool]
    AlgDisableCapability: Optional[str]
    Category: Optional[str]
    ContinueScanningForOtherApplications: Optional[bool]
    Description: Optional[str]
    DeviceGroup: Optional[str]
    EvasiveBehavior: Optional[bool]
    ExcessiveBandwidth: Optional[bool]
    HasKnownVulnerability: Optional[bool]
    Name: Optional[str]
    NoAppIdCaching: Optional[bool]
    ParentApp: Optional[str]
    PervasiveUse: Optional[bool]
    ProneToMisuse: Optional[bool]
    Risk: Optional[float]
    Subcategory: Optional[str]
    Technology: Optional[str]
    TunnelsOtherApplications: Optional[bool]
    UsedByMalware: Optional[bool]
    Defaults: Optional[Sequence["_Defaults"]]
    Scanning: Optional[Sequence["_Scanning"]]
    TimeoutSettings: Optional[Sequence["_TimeoutSettings"]]
    Icmp: Optional[Sequence["_Icmp"]]
    Icmp6: Optional[Sequence["_Icmp6"]]
    IpProtocol: Optional[Sequence["_IpProtocol"]]
    Port: Optional[Sequence["_Port"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AbleToFileTransfer=json_data.get("AbleToFileTransfer"),
            AlgDisableCapability=json_data.get("AlgDisableCapability"),
            Category=json_data.get("Category"),
            ContinueScanningForOtherApplications=json_data.get("ContinueScanningForOtherApplications"),
            Description=json_data.get("Description"),
            DeviceGroup=json_data.get("DeviceGroup"),
            EvasiveBehavior=json_data.get("EvasiveBehavior"),
            ExcessiveBandwidth=json_data.get("ExcessiveBandwidth"),
            HasKnownVulnerability=json_data.get("HasKnownVulnerability"),
            Name=json_data.get("Name"),
            NoAppIdCaching=json_data.get("NoAppIdCaching"),
            ParentApp=json_data.get("ParentApp"),
            PervasiveUse=json_data.get("PervasiveUse"),
            ProneToMisuse=json_data.get("ProneToMisuse"),
            Risk=json_data.get("Risk"),
            Subcategory=json_data.get("Subcategory"),
            Technology=json_data.get("Technology"),
            TunnelsOtherApplications=json_data.get("TunnelsOtherApplications"),
            UsedByMalware=json_data.get("UsedByMalware"),
            Defaults=json_data.get("Defaults"),
            Scanning=json_data.get("Scanning"),
            TimeoutSettings=json_data.get("TimeoutSettings"),
            Icmp=json_data.get("Icmp"),
            Icmp6=json_data.get("Icmp6"),
            IpProtocol=json_data.get("IpProtocol"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Defaults:
    Icmp: Optional[Sequence["_Icmp"]]
    Icmp6: Optional[Sequence["_Icmp6"]]
    IpProtocol: Optional[Sequence["_IpProtocol"]]
    Port: Optional[Sequence["_Port"]]

    @classmethod
    def _deserialize(
        cls: Type["_Defaults"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Defaults"]:
        if not json_data:
            return None
        return cls(
            Icmp=json_data.get("Icmp"),
            Icmp6=json_data.get("Icmp6"),
            IpProtocol=json_data.get("IpProtocol"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Defaults = Defaults


@dataclass
class Icmp:
    Code: Optional[float]
    Type: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Icmp"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Icmp"]:
        if not json_data:
            return None
        return cls(
            Code=json_data.get("Code"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Icmp = Icmp


@dataclass
class Icmp6:
    Code: Optional[float]
    Type: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Icmp6"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Icmp6"]:
        if not json_data:
            return None
        return cls(
            Code=json_data.get("Code"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Icmp6 = Icmp6


@dataclass
class IpProtocol:
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IpProtocol"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpProtocol"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpProtocol = IpProtocol


@dataclass
class Port:
    Ports: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Port"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Port"]:
        if not json_data:
            return None
        return cls(
            Ports=json_data.get("Ports"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Port = Port


@dataclass
class Scanning:
    DataPatterns: Optional[bool]
    FileTypes: Optional[bool]
    Viruses: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Scanning"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Scanning"]:
        if not json_data:
            return None
        return cls(
            DataPatterns=json_data.get("DataPatterns"),
            FileTypes=json_data.get("FileTypes"),
            Viruses=json_data.get("Viruses"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Scanning = Scanning


@dataclass
class TimeoutSettings:
    TcpHalfClosed: Optional[float]
    TcpTimeWait: Optional[float]
    TcpTimeout: Optional[float]
    Timeout: Optional[float]
    UdpTimeout: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutSettings"]:
        if not json_data:
            return None
        return cls(
            TcpHalfClosed=json_data.get("TcpHalfClosed"),
            TcpTimeWait=json_data.get("TcpTimeWait"),
            TcpTimeout=json_data.get("TcpTimeout"),
            Timeout=json_data.get("Timeout"),
            UdpTimeout=json_data.get("UdpTimeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutSettings = TimeoutSettings


