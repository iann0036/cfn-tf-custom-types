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
    Admin: Optional[str]
    Allowaccess: Optional[str]
    ApcfgProfile: Optional[str]
    BonjourProfile: Optional[str]
    CoordinateLatitude: Optional[str]
    CoordinateLongitude: Optional[str]
    DynamicSortSubtable: Optional[str]
    FirmwareProvision: Optional[str]
    Id: Optional[str]
    ImageDownload: Optional[str]
    Index: Optional[float]
    IpFragmentPreventing: Optional[str]
    LedState: Optional[str]
    Location: Optional[str]
    LoginPasswd: Optional[str]
    LoginPasswdChange: Optional[str]
    MeshBridgeEnable: Optional[str]
    Name: Optional[str]
    OverrideAllowaccess: Optional[str]
    OverrideIpFragment: Optional[str]
    OverrideLan: Optional[str]
    OverrideLedState: Optional[str]
    OverrideLoginPasswdChange: Optional[str]
    OverrideSplitTunnel: Optional[str]
    OverrideWanPortMode: Optional[str]
    Region: Optional[str]
    RegionX: Optional[str]
    RegionY: Optional[str]
    SplitTunnelingAclLocalApSubnet: Optional[str]
    SplitTunnelingAclPath: Optional[str]
    TunMtuDownlink: Optional[float]
    TunMtuUplink: Optional[float]
    Uuid: Optional[str]
    Vdomparam: Optional[str]
    WanPortMode: Optional[str]
    WtpId: Optional[str]
    WtpMode: Optional[str]
    WtpProfile: Optional[str]
    Lan: Optional[Sequence["_LanDefinition"]]
    Radio1: Optional[Sequence["_Radio1Definition"]]
    Radio2: Optional[Sequence["_Radio2Definition"]]
    Radio3: Optional[Sequence["_Radio3Definition"]]
    Radio4: Optional[Sequence["_Radio4Definition"]]
    SplitTunnelingAcl: Optional[Sequence["_SplitTunnelingAclDefinition"]]

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
            Admin=json_data.get("Admin"),
            Allowaccess=json_data.get("Allowaccess"),
            ApcfgProfile=json_data.get("ApcfgProfile"),
            BonjourProfile=json_data.get("BonjourProfile"),
            CoordinateLatitude=json_data.get("CoordinateLatitude"),
            CoordinateLongitude=json_data.get("CoordinateLongitude"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            FirmwareProvision=json_data.get("FirmwareProvision"),
            Id=json_data.get("Id"),
            ImageDownload=json_data.get("ImageDownload"),
            Index=json_data.get("Index"),
            IpFragmentPreventing=json_data.get("IpFragmentPreventing"),
            LedState=json_data.get("LedState"),
            Location=json_data.get("Location"),
            LoginPasswd=json_data.get("LoginPasswd"),
            LoginPasswdChange=json_data.get("LoginPasswdChange"),
            MeshBridgeEnable=json_data.get("MeshBridgeEnable"),
            Name=json_data.get("Name"),
            OverrideAllowaccess=json_data.get("OverrideAllowaccess"),
            OverrideIpFragment=json_data.get("OverrideIpFragment"),
            OverrideLan=json_data.get("OverrideLan"),
            OverrideLedState=json_data.get("OverrideLedState"),
            OverrideLoginPasswdChange=json_data.get("OverrideLoginPasswdChange"),
            OverrideSplitTunnel=json_data.get("OverrideSplitTunnel"),
            OverrideWanPortMode=json_data.get("OverrideWanPortMode"),
            Region=json_data.get("Region"),
            RegionX=json_data.get("RegionX"),
            RegionY=json_data.get("RegionY"),
            SplitTunnelingAclLocalApSubnet=json_data.get("SplitTunnelingAclLocalApSubnet"),
            SplitTunnelingAclPath=json_data.get("SplitTunnelingAclPath"),
            TunMtuDownlink=json_data.get("TunMtuDownlink"),
            TunMtuUplink=json_data.get("TunMtuUplink"),
            Uuid=json_data.get("Uuid"),
            Vdomparam=json_data.get("Vdomparam"),
            WanPortMode=json_data.get("WanPortMode"),
            WtpId=json_data.get("WtpId"),
            WtpMode=json_data.get("WtpMode"),
            WtpProfile=json_data.get("WtpProfile"),
            Lan=deserialize_list(json_data.get("Lan"), LanDefinition),
            Radio1=deserialize_list(json_data.get("Radio1"), Radio1Definition),
            Radio2=deserialize_list(json_data.get("Radio2"), Radio2Definition),
            Radio3=deserialize_list(json_data.get("Radio3"), Radio3Definition),
            Radio4=deserialize_list(json_data.get("Radio4"), Radio4Definition),
            SplitTunnelingAcl=deserialize_list(json_data.get("SplitTunnelingAcl"), SplitTunnelingAclDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LanDefinition(BaseModel):
    Port1Mode: Optional[str]
    Port1Ssid: Optional[str]
    Port2Mode: Optional[str]
    Port2Ssid: Optional[str]
    Port3Mode: Optional[str]
    Port3Ssid: Optional[str]
    Port4Mode: Optional[str]
    Port4Ssid: Optional[str]
    Port5Mode: Optional[str]
    Port5Ssid: Optional[str]
    Port6Mode: Optional[str]
    Port6Ssid: Optional[str]
    Port7Mode: Optional[str]
    Port7Ssid: Optional[str]
    Port8Mode: Optional[str]
    Port8Ssid: Optional[str]
    PortEslMode: Optional[str]
    PortEslSsid: Optional[str]
    PortMode: Optional[str]
    PortSsid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LanDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LanDefinition"]:
        if not json_data:
            return None
        return cls(
            Port1Mode=json_data.get("Port1Mode"),
            Port1Ssid=json_data.get("Port1Ssid"),
            Port2Mode=json_data.get("Port2Mode"),
            Port2Ssid=json_data.get("Port2Ssid"),
            Port3Mode=json_data.get("Port3Mode"),
            Port3Ssid=json_data.get("Port3Ssid"),
            Port4Mode=json_data.get("Port4Mode"),
            Port4Ssid=json_data.get("Port4Ssid"),
            Port5Mode=json_data.get("Port5Mode"),
            Port5Ssid=json_data.get("Port5Ssid"),
            Port6Mode=json_data.get("Port6Mode"),
            Port6Ssid=json_data.get("Port6Ssid"),
            Port7Mode=json_data.get("Port7Mode"),
            Port7Ssid=json_data.get("Port7Ssid"),
            Port8Mode=json_data.get("Port8Mode"),
            Port8Ssid=json_data.get("Port8Ssid"),
            PortEslMode=json_data.get("PortEslMode"),
            PortEslSsid=json_data.get("PortEslSsid"),
            PortMode=json_data.get("PortMode"),
            PortSsid=json_data.get("PortSsid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LanDefinition = LanDefinition


@dataclass
class Radio1Definition(BaseModel):
    AutoPowerHigh: Optional[float]
    AutoPowerLevel: Optional[str]
    AutoPowerLow: Optional[float]
    AutoPowerTarget: Optional[str]
    Band: Optional[str]
    DrmaManualMode: Optional[str]
    OverrideAnalysis: Optional[str]
    OverrideBand: Optional[str]
    OverrideChannel: Optional[str]
    OverrideTxpower: Optional[str]
    OverrideVaps: Optional[str]
    PowerLevel: Optional[float]
    RadioId: Optional[float]
    SpectrumAnalysis: Optional[str]
    VapAll: Optional[str]
    Channel: Optional[Sequence["_ChannelDefinition"]]
    Vaps: Optional[Sequence["_VapsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_Radio1Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Radio1Definition"]:
        if not json_data:
            return None
        return cls(
            AutoPowerHigh=json_data.get("AutoPowerHigh"),
            AutoPowerLevel=json_data.get("AutoPowerLevel"),
            AutoPowerLow=json_data.get("AutoPowerLow"),
            AutoPowerTarget=json_data.get("AutoPowerTarget"),
            Band=json_data.get("Band"),
            DrmaManualMode=json_data.get("DrmaManualMode"),
            OverrideAnalysis=json_data.get("OverrideAnalysis"),
            OverrideBand=json_data.get("OverrideBand"),
            OverrideChannel=json_data.get("OverrideChannel"),
            OverrideTxpower=json_data.get("OverrideTxpower"),
            OverrideVaps=json_data.get("OverrideVaps"),
            PowerLevel=json_data.get("PowerLevel"),
            RadioId=json_data.get("RadioId"),
            SpectrumAnalysis=json_data.get("SpectrumAnalysis"),
            VapAll=json_data.get("VapAll"),
            Channel=deserialize_list(json_data.get("Channel"), ChannelDefinition),
            Vaps=deserialize_list(json_data.get("Vaps"), VapsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_Radio1Definition = Radio1Definition


@dataclass
class ChannelDefinition(BaseModel):
    Chan: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ChannelDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ChannelDefinition"]:
        if not json_data:
            return None
        return cls(
            Chan=json_data.get("Chan"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ChannelDefinition = ChannelDefinition


@dataclass
class VapsDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VapsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VapsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VapsDefinition = VapsDefinition


@dataclass
class Radio2Definition(BaseModel):
    AutoPowerHigh: Optional[float]
    AutoPowerLevel: Optional[str]
    AutoPowerLow: Optional[float]
    AutoPowerTarget: Optional[str]
    Band: Optional[str]
    DrmaManualMode: Optional[str]
    OverrideAnalysis: Optional[str]
    OverrideBand: Optional[str]
    OverrideChannel: Optional[str]
    OverrideTxpower: Optional[str]
    OverrideVaps: Optional[str]
    PowerLevel: Optional[float]
    RadioId: Optional[float]
    SpectrumAnalysis: Optional[str]
    VapAll: Optional[str]
    Channel: Optional[Sequence["_ChannelDefinition"]]
    Vaps: Optional[Sequence["_VapsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_Radio2Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Radio2Definition"]:
        if not json_data:
            return None
        return cls(
            AutoPowerHigh=json_data.get("AutoPowerHigh"),
            AutoPowerLevel=json_data.get("AutoPowerLevel"),
            AutoPowerLow=json_data.get("AutoPowerLow"),
            AutoPowerTarget=json_data.get("AutoPowerTarget"),
            Band=json_data.get("Band"),
            DrmaManualMode=json_data.get("DrmaManualMode"),
            OverrideAnalysis=json_data.get("OverrideAnalysis"),
            OverrideBand=json_data.get("OverrideBand"),
            OverrideChannel=json_data.get("OverrideChannel"),
            OverrideTxpower=json_data.get("OverrideTxpower"),
            OverrideVaps=json_data.get("OverrideVaps"),
            PowerLevel=json_data.get("PowerLevel"),
            RadioId=json_data.get("RadioId"),
            SpectrumAnalysis=json_data.get("SpectrumAnalysis"),
            VapAll=json_data.get("VapAll"),
            Channel=deserialize_list(json_data.get("Channel"), ChannelDefinition),
            Vaps=deserialize_list(json_data.get("Vaps"), VapsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_Radio2Definition = Radio2Definition


@dataclass
class Radio3Definition(BaseModel):
    AutoPowerHigh: Optional[float]
    AutoPowerLevel: Optional[str]
    AutoPowerLow: Optional[float]
    AutoPowerTarget: Optional[str]
    Band: Optional[str]
    DrmaManualMode: Optional[str]
    OverrideAnalysis: Optional[str]
    OverrideBand: Optional[str]
    OverrideChannel: Optional[str]
    OverrideTxpower: Optional[str]
    OverrideVaps: Optional[str]
    PowerLevel: Optional[float]
    SpectrumAnalysis: Optional[str]
    VapAll: Optional[str]
    Channel: Optional[Sequence["_ChannelDefinition"]]
    Vaps: Optional[Sequence["_VapsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_Radio3Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Radio3Definition"]:
        if not json_data:
            return None
        return cls(
            AutoPowerHigh=json_data.get("AutoPowerHigh"),
            AutoPowerLevel=json_data.get("AutoPowerLevel"),
            AutoPowerLow=json_data.get("AutoPowerLow"),
            AutoPowerTarget=json_data.get("AutoPowerTarget"),
            Band=json_data.get("Band"),
            DrmaManualMode=json_data.get("DrmaManualMode"),
            OverrideAnalysis=json_data.get("OverrideAnalysis"),
            OverrideBand=json_data.get("OverrideBand"),
            OverrideChannel=json_data.get("OverrideChannel"),
            OverrideTxpower=json_data.get("OverrideTxpower"),
            OverrideVaps=json_data.get("OverrideVaps"),
            PowerLevel=json_data.get("PowerLevel"),
            SpectrumAnalysis=json_data.get("SpectrumAnalysis"),
            VapAll=json_data.get("VapAll"),
            Channel=deserialize_list(json_data.get("Channel"), ChannelDefinition),
            Vaps=deserialize_list(json_data.get("Vaps"), VapsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_Radio3Definition = Radio3Definition


@dataclass
class Radio4Definition(BaseModel):
    AutoPowerHigh: Optional[float]
    AutoPowerLevel: Optional[str]
    AutoPowerLow: Optional[float]
    AutoPowerTarget: Optional[str]
    Band: Optional[str]
    DrmaManualMode: Optional[str]
    OverrideAnalysis: Optional[str]
    OverrideBand: Optional[str]
    OverrideChannel: Optional[str]
    OverrideTxpower: Optional[str]
    OverrideVaps: Optional[str]
    PowerLevel: Optional[float]
    SpectrumAnalysis: Optional[str]
    VapAll: Optional[str]
    Channel: Optional[Sequence["_ChannelDefinition"]]
    Vaps: Optional[Sequence["_VapsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_Radio4Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Radio4Definition"]:
        if not json_data:
            return None
        return cls(
            AutoPowerHigh=json_data.get("AutoPowerHigh"),
            AutoPowerLevel=json_data.get("AutoPowerLevel"),
            AutoPowerLow=json_data.get("AutoPowerLow"),
            AutoPowerTarget=json_data.get("AutoPowerTarget"),
            Band=json_data.get("Band"),
            DrmaManualMode=json_data.get("DrmaManualMode"),
            OverrideAnalysis=json_data.get("OverrideAnalysis"),
            OverrideBand=json_data.get("OverrideBand"),
            OverrideChannel=json_data.get("OverrideChannel"),
            OverrideTxpower=json_data.get("OverrideTxpower"),
            OverrideVaps=json_data.get("OverrideVaps"),
            PowerLevel=json_data.get("PowerLevel"),
            SpectrumAnalysis=json_data.get("SpectrumAnalysis"),
            VapAll=json_data.get("VapAll"),
            Channel=deserialize_list(json_data.get("Channel"), ChannelDefinition),
            Vaps=deserialize_list(json_data.get("Vaps"), VapsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_Radio4Definition = Radio4Definition


@dataclass
class SplitTunnelingAclDefinition(BaseModel):
    DestIp: Optional[str]
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SplitTunnelingAclDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SplitTunnelingAclDefinition"]:
        if not json_data:
            return None
        return cls(
            DestIp=json_data.get("DestIp"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SplitTunnelingAclDefinition = SplitTunnelingAclDefinition


