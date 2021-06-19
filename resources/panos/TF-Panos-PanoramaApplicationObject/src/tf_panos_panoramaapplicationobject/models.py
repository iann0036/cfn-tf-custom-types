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
    AbleToFileTransfer: Optional[bool]
    AlgDisableCapability: Optional[str]
    Category: Optional[str]
    ContinueScanningForOtherApplications: Optional[bool]
    Description: Optional[str]
    DeviceGroup: Optional[str]
    EvasiveBehavior: Optional[bool]
    ExcessiveBandwidth: Optional[bool]
    HasKnownVulnerability: Optional[bool]
    Id: Optional[str]
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
    Defaults: Optional[Sequence["_DefaultsDefinition"]]
    Scanning: Optional[Sequence["_ScanningDefinition"]]
    TimeoutSettings: Optional[Sequence["_TimeoutSettingsDefinition"]]

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
            AbleToFileTransfer=json_data.get("AbleToFileTransfer"),
            AlgDisableCapability=json_data.get("AlgDisableCapability"),
            Category=json_data.get("Category"),
            ContinueScanningForOtherApplications=json_data.get("ContinueScanningForOtherApplications"),
            Description=json_data.get("Description"),
            DeviceGroup=json_data.get("DeviceGroup"),
            EvasiveBehavior=json_data.get("EvasiveBehavior"),
            ExcessiveBandwidth=json_data.get("ExcessiveBandwidth"),
            HasKnownVulnerability=json_data.get("HasKnownVulnerability"),
            Id=json_data.get("Id"),
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
            Defaults=deserialize_list(json_data.get("Defaults"), DefaultsDefinition),
            Scanning=deserialize_list(json_data.get("Scanning"), ScanningDefinition),
            TimeoutSettings=deserialize_list(json_data.get("TimeoutSettings"), TimeoutSettingsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefaultsDefinition(BaseModel):
    Icmp: Optional[Sequence["_IcmpDefinition"]]
    Icmp6: Optional[Sequence["_Icmp6Definition"]]
    IpProtocol: Optional[Sequence["_IpProtocolDefinition"]]
    Port: Optional[Sequence["_PortDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultsDefinition"]:
        if not json_data:
            return None
        return cls(
            Icmp=deserialize_list(json_data.get("Icmp"), IcmpDefinition),
            Icmp6=deserialize_list(json_data.get("Icmp6"), Icmp6Definition),
            IpProtocol=deserialize_list(json_data.get("IpProtocol"), IpProtocolDefinition),
            Port=deserialize_list(json_data.get("Port"), PortDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultsDefinition = DefaultsDefinition


@dataclass
class IcmpDefinition(BaseModel):
    Code: Optional[float]
    Type: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IcmpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IcmpDefinition"]:
        if not json_data:
            return None
        return cls(
            Code=json_data.get("Code"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IcmpDefinition = IcmpDefinition


@dataclass
class Icmp6Definition(BaseModel):
    Code: Optional[float]
    Type: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Icmp6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Icmp6Definition"]:
        if not json_data:
            return None
        return cls(
            Code=json_data.get("Code"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Icmp6Definition = Icmp6Definition


@dataclass
class IpProtocolDefinition(BaseModel):
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IpProtocolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpProtocolDefinition"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpProtocolDefinition = IpProtocolDefinition


@dataclass
class PortDefinition(BaseModel):
    Ports: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PortDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortDefinition"]:
        if not json_data:
            return None
        return cls(
            Ports=json_data.get("Ports"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortDefinition = PortDefinition


@dataclass
class ScanningDefinition(BaseModel):
    DataPatterns: Optional[bool]
    FileTypes: Optional[bool]
    Viruses: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ScanningDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScanningDefinition"]:
        if not json_data:
            return None
        return cls(
            DataPatterns=json_data.get("DataPatterns"),
            FileTypes=json_data.get("FileTypes"),
            Viruses=json_data.get("Viruses"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScanningDefinition = ScanningDefinition


@dataclass
class TimeoutSettingsDefinition(BaseModel):
    TcpHalfClosed: Optional[float]
    TcpTimeWait: Optional[float]
    TcpTimeout: Optional[float]
    Timeout: Optional[float]
    UdpTimeout: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutSettingsDefinition"]:
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
_TimeoutSettingsDefinition = TimeoutSettingsDefinition


