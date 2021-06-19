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
    Allowaccess: Optional[str]
    ApCountry: Optional[str]
    ApHandoff: Optional[str]
    ApcfgProfile: Optional[str]
    BleProfile: Optional[str]
    Comment: Optional[str]
    ControlMessageOffload: Optional[str]
    DtlsInKernel: Optional[str]
    DtlsPolicy: Optional[str]
    DynamicSortSubtable: Optional[str]
    EnergyEfficientEthernet: Optional[str]
    ExtInfoEnable: Optional[str]
    FrequencyHandoff: Optional[str]
    HandoffRoaming: Optional[str]
    HandoffRssi: Optional[float]
    HandoffStaThresh: Optional[float]
    Id: Optional[str]
    IpFragmentPreventing: Optional[str]
    LedState: Optional[str]
    Lldp: Optional[str]
    LoginPasswd: Optional[str]
    LoginPasswdChange: Optional[str]
    MaxClients: Optional[float]
    Name: Optional[str]
    PoeMode: Optional[str]
    SplitTunnelingAclLocalApSubnet: Optional[str]
    SplitTunnelingAclPath: Optional[str]
    TunMtuDownlink: Optional[float]
    TunMtuUplink: Optional[float]
    Vdomparam: Optional[str]
    WanPortMode: Optional[str]
    DenyMacList: Optional[Sequence["_DenyMacListDefinition"]]
    Lan: Optional[Sequence["_LanDefinition"]]
    Lbs: Optional[Sequence["_LbsDefinition"]]
    LedSchedules: Optional[Sequence["_LedSchedulesDefinition"]]
    Platform: Optional[Sequence["_PlatformDefinition"]]
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
            Allowaccess=json_data.get("Allowaccess"),
            ApCountry=json_data.get("ApCountry"),
            ApHandoff=json_data.get("ApHandoff"),
            ApcfgProfile=json_data.get("ApcfgProfile"),
            BleProfile=json_data.get("BleProfile"),
            Comment=json_data.get("Comment"),
            ControlMessageOffload=json_data.get("ControlMessageOffload"),
            DtlsInKernel=json_data.get("DtlsInKernel"),
            DtlsPolicy=json_data.get("DtlsPolicy"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            EnergyEfficientEthernet=json_data.get("EnergyEfficientEthernet"),
            ExtInfoEnable=json_data.get("ExtInfoEnable"),
            FrequencyHandoff=json_data.get("FrequencyHandoff"),
            HandoffRoaming=json_data.get("HandoffRoaming"),
            HandoffRssi=json_data.get("HandoffRssi"),
            HandoffStaThresh=json_data.get("HandoffStaThresh"),
            Id=json_data.get("Id"),
            IpFragmentPreventing=json_data.get("IpFragmentPreventing"),
            LedState=json_data.get("LedState"),
            Lldp=json_data.get("Lldp"),
            LoginPasswd=json_data.get("LoginPasswd"),
            LoginPasswdChange=json_data.get("LoginPasswdChange"),
            MaxClients=json_data.get("MaxClients"),
            Name=json_data.get("Name"),
            PoeMode=json_data.get("PoeMode"),
            SplitTunnelingAclLocalApSubnet=json_data.get("SplitTunnelingAclLocalApSubnet"),
            SplitTunnelingAclPath=json_data.get("SplitTunnelingAclPath"),
            TunMtuDownlink=json_data.get("TunMtuDownlink"),
            TunMtuUplink=json_data.get("TunMtuUplink"),
            Vdomparam=json_data.get("Vdomparam"),
            WanPortMode=json_data.get("WanPortMode"),
            DenyMacList=deserialize_list(json_data.get("DenyMacList"), DenyMacListDefinition),
            Lan=deserialize_list(json_data.get("Lan"), LanDefinition),
            Lbs=deserialize_list(json_data.get("Lbs"), LbsDefinition),
            LedSchedules=deserialize_list(json_data.get("LedSchedules"), LedSchedulesDefinition),
            Platform=deserialize_list(json_data.get("Platform"), PlatformDefinition),
            Radio1=deserialize_list(json_data.get("Radio1"), Radio1Definition),
            Radio2=deserialize_list(json_data.get("Radio2"), Radio2Definition),
            Radio3=deserialize_list(json_data.get("Radio3"), Radio3Definition),
            Radio4=deserialize_list(json_data.get("Radio4"), Radio4Definition),
            SplitTunnelingAcl=deserialize_list(json_data.get("SplitTunnelingAcl"), SplitTunnelingAclDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DenyMacListDefinition(BaseModel):
    Id: Optional[float]
    Mac: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DenyMacListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DenyMacListDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Mac=json_data.get("Mac"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DenyMacListDefinition = DenyMacListDefinition


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
class LbsDefinition(BaseModel):
    Aeroscout: Optional[str]
    AeroscoutApMac: Optional[str]
    AeroscoutMmuReport: Optional[str]
    AeroscoutMu: Optional[str]
    AeroscoutMuFactor: Optional[float]
    AeroscoutMuTimeout: Optional[float]
    AeroscoutServerIp: Optional[str]
    AeroscoutServerPort: Optional[float]
    EkahauBlinkMode: Optional[str]
    EkahauTag: Optional[str]
    ErcServerIp: Optional[str]
    ErcServerPort: Optional[float]
    Fortipresence: Optional[str]
    FortipresenceBle: Optional[str]
    FortipresenceFrequency: Optional[float]
    FortipresencePort: Optional[float]
    FortipresenceProject: Optional[str]
    FortipresenceRogue: Optional[str]
    FortipresenceSecret: Optional[str]
    FortipresenceServer: Optional[str]
    FortipresenceUnassoc: Optional[str]
    StationLocate: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LbsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LbsDefinition"]:
        if not json_data:
            return None
        return cls(
            Aeroscout=json_data.get("Aeroscout"),
            AeroscoutApMac=json_data.get("AeroscoutApMac"),
            AeroscoutMmuReport=json_data.get("AeroscoutMmuReport"),
            AeroscoutMu=json_data.get("AeroscoutMu"),
            AeroscoutMuFactor=json_data.get("AeroscoutMuFactor"),
            AeroscoutMuTimeout=json_data.get("AeroscoutMuTimeout"),
            AeroscoutServerIp=json_data.get("AeroscoutServerIp"),
            AeroscoutServerPort=json_data.get("AeroscoutServerPort"),
            EkahauBlinkMode=json_data.get("EkahauBlinkMode"),
            EkahauTag=json_data.get("EkahauTag"),
            ErcServerIp=json_data.get("ErcServerIp"),
            ErcServerPort=json_data.get("ErcServerPort"),
            Fortipresence=json_data.get("Fortipresence"),
            FortipresenceBle=json_data.get("FortipresenceBle"),
            FortipresenceFrequency=json_data.get("FortipresenceFrequency"),
            FortipresencePort=json_data.get("FortipresencePort"),
            FortipresenceProject=json_data.get("FortipresenceProject"),
            FortipresenceRogue=json_data.get("FortipresenceRogue"),
            FortipresenceSecret=json_data.get("FortipresenceSecret"),
            FortipresenceServer=json_data.get("FortipresenceServer"),
            FortipresenceUnassoc=json_data.get("FortipresenceUnassoc"),
            StationLocate=json_data.get("StationLocate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LbsDefinition = LbsDefinition


@dataclass
class LedSchedulesDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LedSchedulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LedSchedulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LedSchedulesDefinition = LedSchedulesDefinition


@dataclass
class PlatformDefinition(BaseModel):
    Ddscan: Optional[str]
    Mode: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlatformDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlatformDefinition"]:
        if not json_data:
            return None
        return cls(
            Ddscan=json_data.get("Ddscan"),
            Mode=json_data.get("Mode"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlatformDefinition = PlatformDefinition


@dataclass
class Radio1Definition(BaseModel):
    AirtimeFairness: Optional[str]
    Amsdu: Optional[str]
    ApHandoff: Optional[str]
    ApSnifferAddr: Optional[str]
    ApSnifferBufsize: Optional[float]
    ApSnifferChan: Optional[float]
    ApSnifferCtl: Optional[str]
    ApSnifferData: Optional[str]
    ApSnifferMgmtBeacon: Optional[str]
    ApSnifferMgmtOther: Optional[str]
    ApSnifferMgmtProbe: Optional[str]
    AutoPowerHigh: Optional[float]
    AutoPowerLevel: Optional[str]
    AutoPowerLow: Optional[float]
    AutoPowerTarget: Optional[str]
    Band: Optional[str]
    Band5gType: Optional[str]
    BandwidthAdmissionControl: Optional[str]
    BandwidthCapacity: Optional[float]
    BeaconInterval: Optional[float]
    BssColor: Optional[float]
    CallAdmissionControl: Optional[str]
    CallCapacity: Optional[float]
    ChannelBonding: Optional[str]
    ChannelUtilization: Optional[str]
    Coexistence: Optional[str]
    Darrp: Optional[str]
    Drma: Optional[str]
    DrmaSensitivity: Optional[str]
    Dtim: Optional[float]
    FragThreshold: Optional[float]
    FrequencyHandoff: Optional[str]
    MaxClients: Optional[float]
    MaxDistance: Optional[float]
    Mode: Optional[str]
    PowerLevel: Optional[float]
    PowersaveOptimize: Optional[str]
    ProtectionMode: Optional[str]
    RadioId: Optional[float]
    RtsThreshold: Optional[float]
    ShortGuardInterval: Optional[str]
    SpectrumAnalysis: Optional[str]
    TransmitOptimize: Optional[str]
    VapAll: Optional[str]
    WidsProfile: Optional[str]
    ZeroWaitDfs: Optional[str]
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
            AirtimeFairness=json_data.get("AirtimeFairness"),
            Amsdu=json_data.get("Amsdu"),
            ApHandoff=json_data.get("ApHandoff"),
            ApSnifferAddr=json_data.get("ApSnifferAddr"),
            ApSnifferBufsize=json_data.get("ApSnifferBufsize"),
            ApSnifferChan=json_data.get("ApSnifferChan"),
            ApSnifferCtl=json_data.get("ApSnifferCtl"),
            ApSnifferData=json_data.get("ApSnifferData"),
            ApSnifferMgmtBeacon=json_data.get("ApSnifferMgmtBeacon"),
            ApSnifferMgmtOther=json_data.get("ApSnifferMgmtOther"),
            ApSnifferMgmtProbe=json_data.get("ApSnifferMgmtProbe"),
            AutoPowerHigh=json_data.get("AutoPowerHigh"),
            AutoPowerLevel=json_data.get("AutoPowerLevel"),
            AutoPowerLow=json_data.get("AutoPowerLow"),
            AutoPowerTarget=json_data.get("AutoPowerTarget"),
            Band=json_data.get("Band"),
            Band5gType=json_data.get("Band5gType"),
            BandwidthAdmissionControl=json_data.get("BandwidthAdmissionControl"),
            BandwidthCapacity=json_data.get("BandwidthCapacity"),
            BeaconInterval=json_data.get("BeaconInterval"),
            BssColor=json_data.get("BssColor"),
            CallAdmissionControl=json_data.get("CallAdmissionControl"),
            CallCapacity=json_data.get("CallCapacity"),
            ChannelBonding=json_data.get("ChannelBonding"),
            ChannelUtilization=json_data.get("ChannelUtilization"),
            Coexistence=json_data.get("Coexistence"),
            Darrp=json_data.get("Darrp"),
            Drma=json_data.get("Drma"),
            DrmaSensitivity=json_data.get("DrmaSensitivity"),
            Dtim=json_data.get("Dtim"),
            FragThreshold=json_data.get("FragThreshold"),
            FrequencyHandoff=json_data.get("FrequencyHandoff"),
            MaxClients=json_data.get("MaxClients"),
            MaxDistance=json_data.get("MaxDistance"),
            Mode=json_data.get("Mode"),
            PowerLevel=json_data.get("PowerLevel"),
            PowersaveOptimize=json_data.get("PowersaveOptimize"),
            ProtectionMode=json_data.get("ProtectionMode"),
            RadioId=json_data.get("RadioId"),
            RtsThreshold=json_data.get("RtsThreshold"),
            ShortGuardInterval=json_data.get("ShortGuardInterval"),
            SpectrumAnalysis=json_data.get("SpectrumAnalysis"),
            TransmitOptimize=json_data.get("TransmitOptimize"),
            VapAll=json_data.get("VapAll"),
            WidsProfile=json_data.get("WidsProfile"),
            ZeroWaitDfs=json_data.get("ZeroWaitDfs"),
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
    AirtimeFairness: Optional[str]
    Amsdu: Optional[str]
    ApHandoff: Optional[str]
    ApSnifferAddr: Optional[str]
    ApSnifferBufsize: Optional[float]
    ApSnifferChan: Optional[float]
    ApSnifferCtl: Optional[str]
    ApSnifferData: Optional[str]
    ApSnifferMgmtBeacon: Optional[str]
    ApSnifferMgmtOther: Optional[str]
    ApSnifferMgmtProbe: Optional[str]
    AutoPowerHigh: Optional[float]
    AutoPowerLevel: Optional[str]
    AutoPowerLow: Optional[float]
    AutoPowerTarget: Optional[str]
    Band: Optional[str]
    Band5gType: Optional[str]
    BandwidthAdmissionControl: Optional[str]
    BandwidthCapacity: Optional[float]
    BeaconInterval: Optional[float]
    BssColor: Optional[float]
    CallAdmissionControl: Optional[str]
    CallCapacity: Optional[float]
    ChannelBonding: Optional[str]
    ChannelUtilization: Optional[str]
    Coexistence: Optional[str]
    Darrp: Optional[str]
    Drma: Optional[str]
    DrmaSensitivity: Optional[str]
    Dtim: Optional[float]
    FragThreshold: Optional[float]
    FrequencyHandoff: Optional[str]
    MaxClients: Optional[float]
    MaxDistance: Optional[float]
    Mode: Optional[str]
    PowerLevel: Optional[float]
    PowersaveOptimize: Optional[str]
    ProtectionMode: Optional[str]
    RadioId: Optional[float]
    RtsThreshold: Optional[float]
    ShortGuardInterval: Optional[str]
    SpectrumAnalysis: Optional[str]
    TransmitOptimize: Optional[str]
    VapAll: Optional[str]
    WidsProfile: Optional[str]
    ZeroWaitDfs: Optional[str]
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
            AirtimeFairness=json_data.get("AirtimeFairness"),
            Amsdu=json_data.get("Amsdu"),
            ApHandoff=json_data.get("ApHandoff"),
            ApSnifferAddr=json_data.get("ApSnifferAddr"),
            ApSnifferBufsize=json_data.get("ApSnifferBufsize"),
            ApSnifferChan=json_data.get("ApSnifferChan"),
            ApSnifferCtl=json_data.get("ApSnifferCtl"),
            ApSnifferData=json_data.get("ApSnifferData"),
            ApSnifferMgmtBeacon=json_data.get("ApSnifferMgmtBeacon"),
            ApSnifferMgmtOther=json_data.get("ApSnifferMgmtOther"),
            ApSnifferMgmtProbe=json_data.get("ApSnifferMgmtProbe"),
            AutoPowerHigh=json_data.get("AutoPowerHigh"),
            AutoPowerLevel=json_data.get("AutoPowerLevel"),
            AutoPowerLow=json_data.get("AutoPowerLow"),
            AutoPowerTarget=json_data.get("AutoPowerTarget"),
            Band=json_data.get("Band"),
            Band5gType=json_data.get("Band5gType"),
            BandwidthAdmissionControl=json_data.get("BandwidthAdmissionControl"),
            BandwidthCapacity=json_data.get("BandwidthCapacity"),
            BeaconInterval=json_data.get("BeaconInterval"),
            BssColor=json_data.get("BssColor"),
            CallAdmissionControl=json_data.get("CallAdmissionControl"),
            CallCapacity=json_data.get("CallCapacity"),
            ChannelBonding=json_data.get("ChannelBonding"),
            ChannelUtilization=json_data.get("ChannelUtilization"),
            Coexistence=json_data.get("Coexistence"),
            Darrp=json_data.get("Darrp"),
            Drma=json_data.get("Drma"),
            DrmaSensitivity=json_data.get("DrmaSensitivity"),
            Dtim=json_data.get("Dtim"),
            FragThreshold=json_data.get("FragThreshold"),
            FrequencyHandoff=json_data.get("FrequencyHandoff"),
            MaxClients=json_data.get("MaxClients"),
            MaxDistance=json_data.get("MaxDistance"),
            Mode=json_data.get("Mode"),
            PowerLevel=json_data.get("PowerLevel"),
            PowersaveOptimize=json_data.get("PowersaveOptimize"),
            ProtectionMode=json_data.get("ProtectionMode"),
            RadioId=json_data.get("RadioId"),
            RtsThreshold=json_data.get("RtsThreshold"),
            ShortGuardInterval=json_data.get("ShortGuardInterval"),
            SpectrumAnalysis=json_data.get("SpectrumAnalysis"),
            TransmitOptimize=json_data.get("TransmitOptimize"),
            VapAll=json_data.get("VapAll"),
            WidsProfile=json_data.get("WidsProfile"),
            ZeroWaitDfs=json_data.get("ZeroWaitDfs"),
            Channel=deserialize_list(json_data.get("Channel"), ChannelDefinition),
            Vaps=deserialize_list(json_data.get("Vaps"), VapsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_Radio2Definition = Radio2Definition


@dataclass
class Radio3Definition(BaseModel):
    AirtimeFairness: Optional[str]
    Amsdu: Optional[str]
    ApHandoff: Optional[str]
    ApSnifferAddr: Optional[str]
    ApSnifferBufsize: Optional[float]
    ApSnifferChan: Optional[float]
    ApSnifferCtl: Optional[str]
    ApSnifferData: Optional[str]
    ApSnifferMgmtBeacon: Optional[str]
    ApSnifferMgmtOther: Optional[str]
    ApSnifferMgmtProbe: Optional[str]
    AutoPowerHigh: Optional[float]
    AutoPowerLevel: Optional[str]
    AutoPowerLow: Optional[float]
    AutoPowerTarget: Optional[str]
    Band: Optional[str]
    Band5gType: Optional[str]
    BandwidthAdmissionControl: Optional[str]
    BandwidthCapacity: Optional[float]
    BeaconInterval: Optional[float]
    BssColor: Optional[float]
    CallAdmissionControl: Optional[str]
    CallCapacity: Optional[float]
    ChannelBonding: Optional[str]
    ChannelUtilization: Optional[str]
    Coexistence: Optional[str]
    Darrp: Optional[str]
    Drma: Optional[str]
    DrmaSensitivity: Optional[str]
    Dtim: Optional[float]
    FragThreshold: Optional[float]
    FrequencyHandoff: Optional[str]
    MaxClients: Optional[float]
    MaxDistance: Optional[float]
    Mode: Optional[str]
    PowerLevel: Optional[float]
    PowersaveOptimize: Optional[str]
    ProtectionMode: Optional[str]
    RtsThreshold: Optional[float]
    ShortGuardInterval: Optional[str]
    SpectrumAnalysis: Optional[str]
    TransmitOptimize: Optional[str]
    VapAll: Optional[str]
    WidsProfile: Optional[str]
    ZeroWaitDfs: Optional[str]
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
            AirtimeFairness=json_data.get("AirtimeFairness"),
            Amsdu=json_data.get("Amsdu"),
            ApHandoff=json_data.get("ApHandoff"),
            ApSnifferAddr=json_data.get("ApSnifferAddr"),
            ApSnifferBufsize=json_data.get("ApSnifferBufsize"),
            ApSnifferChan=json_data.get("ApSnifferChan"),
            ApSnifferCtl=json_data.get("ApSnifferCtl"),
            ApSnifferData=json_data.get("ApSnifferData"),
            ApSnifferMgmtBeacon=json_data.get("ApSnifferMgmtBeacon"),
            ApSnifferMgmtOther=json_data.get("ApSnifferMgmtOther"),
            ApSnifferMgmtProbe=json_data.get("ApSnifferMgmtProbe"),
            AutoPowerHigh=json_data.get("AutoPowerHigh"),
            AutoPowerLevel=json_data.get("AutoPowerLevel"),
            AutoPowerLow=json_data.get("AutoPowerLow"),
            AutoPowerTarget=json_data.get("AutoPowerTarget"),
            Band=json_data.get("Band"),
            Band5gType=json_data.get("Band5gType"),
            BandwidthAdmissionControl=json_data.get("BandwidthAdmissionControl"),
            BandwidthCapacity=json_data.get("BandwidthCapacity"),
            BeaconInterval=json_data.get("BeaconInterval"),
            BssColor=json_data.get("BssColor"),
            CallAdmissionControl=json_data.get("CallAdmissionControl"),
            CallCapacity=json_data.get("CallCapacity"),
            ChannelBonding=json_data.get("ChannelBonding"),
            ChannelUtilization=json_data.get("ChannelUtilization"),
            Coexistence=json_data.get("Coexistence"),
            Darrp=json_data.get("Darrp"),
            Drma=json_data.get("Drma"),
            DrmaSensitivity=json_data.get("DrmaSensitivity"),
            Dtim=json_data.get("Dtim"),
            FragThreshold=json_data.get("FragThreshold"),
            FrequencyHandoff=json_data.get("FrequencyHandoff"),
            MaxClients=json_data.get("MaxClients"),
            MaxDistance=json_data.get("MaxDistance"),
            Mode=json_data.get("Mode"),
            PowerLevel=json_data.get("PowerLevel"),
            PowersaveOptimize=json_data.get("PowersaveOptimize"),
            ProtectionMode=json_data.get("ProtectionMode"),
            RtsThreshold=json_data.get("RtsThreshold"),
            ShortGuardInterval=json_data.get("ShortGuardInterval"),
            SpectrumAnalysis=json_data.get("SpectrumAnalysis"),
            TransmitOptimize=json_data.get("TransmitOptimize"),
            VapAll=json_data.get("VapAll"),
            WidsProfile=json_data.get("WidsProfile"),
            ZeroWaitDfs=json_data.get("ZeroWaitDfs"),
            Channel=deserialize_list(json_data.get("Channel"), ChannelDefinition),
            Vaps=deserialize_list(json_data.get("Vaps"), VapsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_Radio3Definition = Radio3Definition


@dataclass
class Radio4Definition(BaseModel):
    AirtimeFairness: Optional[str]
    Amsdu: Optional[str]
    ApHandoff: Optional[str]
    ApSnifferAddr: Optional[str]
    ApSnifferBufsize: Optional[float]
    ApSnifferChan: Optional[float]
    ApSnifferCtl: Optional[str]
    ApSnifferData: Optional[str]
    ApSnifferMgmtBeacon: Optional[str]
    ApSnifferMgmtOther: Optional[str]
    ApSnifferMgmtProbe: Optional[str]
    AutoPowerHigh: Optional[float]
    AutoPowerLevel: Optional[str]
    AutoPowerLow: Optional[float]
    AutoPowerTarget: Optional[str]
    Band: Optional[str]
    Band5gType: Optional[str]
    BandwidthAdmissionControl: Optional[str]
    BandwidthCapacity: Optional[float]
    BeaconInterval: Optional[float]
    BssColor: Optional[float]
    CallAdmissionControl: Optional[str]
    CallCapacity: Optional[float]
    ChannelBonding: Optional[str]
    ChannelUtilization: Optional[str]
    Coexistence: Optional[str]
    Darrp: Optional[str]
    Drma: Optional[str]
    DrmaSensitivity: Optional[str]
    Dtim: Optional[float]
    FragThreshold: Optional[float]
    FrequencyHandoff: Optional[str]
    MaxClients: Optional[float]
    MaxDistance: Optional[float]
    Mode: Optional[str]
    PowerLevel: Optional[float]
    PowersaveOptimize: Optional[str]
    ProtectionMode: Optional[str]
    RtsThreshold: Optional[float]
    ShortGuardInterval: Optional[str]
    SpectrumAnalysis: Optional[str]
    TransmitOptimize: Optional[str]
    VapAll: Optional[str]
    WidsProfile: Optional[str]
    ZeroWaitDfs: Optional[str]
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
            AirtimeFairness=json_data.get("AirtimeFairness"),
            Amsdu=json_data.get("Amsdu"),
            ApHandoff=json_data.get("ApHandoff"),
            ApSnifferAddr=json_data.get("ApSnifferAddr"),
            ApSnifferBufsize=json_data.get("ApSnifferBufsize"),
            ApSnifferChan=json_data.get("ApSnifferChan"),
            ApSnifferCtl=json_data.get("ApSnifferCtl"),
            ApSnifferData=json_data.get("ApSnifferData"),
            ApSnifferMgmtBeacon=json_data.get("ApSnifferMgmtBeacon"),
            ApSnifferMgmtOther=json_data.get("ApSnifferMgmtOther"),
            ApSnifferMgmtProbe=json_data.get("ApSnifferMgmtProbe"),
            AutoPowerHigh=json_data.get("AutoPowerHigh"),
            AutoPowerLevel=json_data.get("AutoPowerLevel"),
            AutoPowerLow=json_data.get("AutoPowerLow"),
            AutoPowerTarget=json_data.get("AutoPowerTarget"),
            Band=json_data.get("Band"),
            Band5gType=json_data.get("Band5gType"),
            BandwidthAdmissionControl=json_data.get("BandwidthAdmissionControl"),
            BandwidthCapacity=json_data.get("BandwidthCapacity"),
            BeaconInterval=json_data.get("BeaconInterval"),
            BssColor=json_data.get("BssColor"),
            CallAdmissionControl=json_data.get("CallAdmissionControl"),
            CallCapacity=json_data.get("CallCapacity"),
            ChannelBonding=json_data.get("ChannelBonding"),
            ChannelUtilization=json_data.get("ChannelUtilization"),
            Coexistence=json_data.get("Coexistence"),
            Darrp=json_data.get("Darrp"),
            Drma=json_data.get("Drma"),
            DrmaSensitivity=json_data.get("DrmaSensitivity"),
            Dtim=json_data.get("Dtim"),
            FragThreshold=json_data.get("FragThreshold"),
            FrequencyHandoff=json_data.get("FrequencyHandoff"),
            MaxClients=json_data.get("MaxClients"),
            MaxDistance=json_data.get("MaxDistance"),
            Mode=json_data.get("Mode"),
            PowerLevel=json_data.get("PowerLevel"),
            PowersaveOptimize=json_data.get("PowersaveOptimize"),
            ProtectionMode=json_data.get("ProtectionMode"),
            RtsThreshold=json_data.get("RtsThreshold"),
            ShortGuardInterval=json_data.get("ShortGuardInterval"),
            SpectrumAnalysis=json_data.get("SpectrumAnalysis"),
            TransmitOptimize=json_data.get("TransmitOptimize"),
            VapAll=json_data.get("VapAll"),
            WidsProfile=json_data.get("WidsProfile"),
            ZeroWaitDfs=json_data.get("ZeroWaitDfs"),
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


