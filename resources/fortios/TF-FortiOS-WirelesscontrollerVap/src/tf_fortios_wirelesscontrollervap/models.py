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
    AccessControlList: Optional[str]
    AcctInterimInterval: Optional[float]
    AdditionalAkms: Optional[str]
    AddressGroup: Optional[str]
    Alias: Optional[str]
    AtfWeight: Optional[float]
    Auth: Optional[str]
    BroadcastSsid: Optional[str]
    BroadcastSuppression: Optional[str]
    BssColorPartial: Optional[str]
    CaptivePortalAcName: Optional[str]
    CaptivePortalAuthTimeout: Optional[float]
    CaptivePortalMacauthRadiusSecret: Optional[str]
    CaptivePortalMacauthRadiusServer: Optional[str]
    CaptivePortalRadiusSecret: Optional[str]
    CaptivePortalRadiusServer: Optional[str]
    CaptivePortalSessionTimeoutInterval: Optional[float]
    DhcpLeaseTime: Optional[float]
    DhcpOption43Insertion: Optional[str]
    DhcpOption82CircuitIdInsertion: Optional[str]
    DhcpOption82Insertion: Optional[str]
    DhcpOption82RemoteIdInsertion: Optional[str]
    DynamicSortSubtable: Optional[str]
    DynamicVlan: Optional[str]
    EapReauth: Optional[str]
    EapReauthIntv: Optional[float]
    EapolKeyRetries: Optional[str]
    Encrypt: Optional[str]
    ExternalFastRoaming: Optional[str]
    ExternalLogout: Optional[str]
    ExternalWeb: Optional[str]
    ExternalWebFormat: Optional[str]
    FastBssTransition: Optional[str]
    FastRoaming: Optional[str]
    FtMobilityDomain: Optional[float]
    FtOverDs: Optional[str]
    FtR0KeyLifetime: Optional[float]
    GtkRekey: Optional[str]
    GtkRekeyIntv: Optional[float]
    HighEfficiency: Optional[str]
    Hotspot20Profile: Optional[str]
    Id: Optional[str]
    IgmpSnooping: Optional[str]
    IntraVapPrivacy: Optional[str]
    Ip: Optional[str]
    Ipv6Rules: Optional[str]
    Key: Optional[str]
    Keyindex: Optional[float]
    Ldpc: Optional[str]
    LocalAuthentication: Optional[str]
    LocalBridging: Optional[str]
    LocalLan: Optional[str]
    LocalStandalone: Optional[str]
    LocalStandaloneNat: Optional[str]
    MacAuthBypass: Optional[str]
    MacFilter: Optional[str]
    MacFilterPolicyOther: Optional[str]
    MaxClients: Optional[float]
    MaxClientsAp: Optional[float]
    MeDisableThresh: Optional[float]
    MeshBackhaul: Optional[str]
    Mpsk: Optional[str]
    MpskConcurrentClients: Optional[float]
    MpskProfile: Optional[str]
    MuMimo: Optional[str]
    MulticastEnhance: Optional[str]
    MulticastRate: Optional[str]
    Name: Optional[str]
    Okc: Optional[str]
    OweGroups: Optional[str]
    OweTransition: Optional[str]
    OweTransitionSsid: Optional[str]
    Passphrase: Optional[str]
    Pmf: Optional[str]
    PmfAssocComebackTimeout: Optional[float]
    PmfSaQueryRetryTimeout: Optional[float]
    PortMacauth: Optional[str]
    PortMacauthReauthTimeout: Optional[float]
    PortMacauthTimeout: Optional[float]
    PortalMessageOverrideGroup: Optional[str]
    PortalType: Optional[str]
    PrimaryWagProfile: Optional[str]
    ProbeRespSuppression: Optional[str]
    ProbeRespThreshold: Optional[str]
    PtkRekey: Optional[str]
    PtkRekeyIntv: Optional[float]
    QosProfile: Optional[str]
    Quarantine: Optional[str]
    Radio2gThreshold: Optional[str]
    Radio5gThreshold: Optional[str]
    RadioSensitivity: Optional[str]
    RadiusMacAuth: Optional[str]
    RadiusMacAuthServer: Optional[str]
    RadiusServer: Optional[str]
    Rates11a: Optional[str]
    Rates11acSs12: Optional[str]
    Rates11acSs34: Optional[str]
    Rates11bg: Optional[str]
    Rates11nSs12: Optional[str]
    Rates11nSs34: Optional[str]
    SaeGroups: Optional[str]
    SaePassword: Optional[str]
    Schedule: Optional[str]
    SecondaryWagProfile: Optional[str]
    Security: Optional[str]
    SecurityExemptList: Optional[str]
    SecurityObsoleteOption: Optional[str]
    SecurityRedirectUrl: Optional[str]
    SplitTunneling: Optional[str]
    Ssid: Optional[str]
    StickyClientRemove: Optional[str]
    StickyClientThreshold2g: Optional[str]
    StickyClientThreshold5g: Optional[str]
    TargetWakeTime: Optional[str]
    TkipCounterMeasure: Optional[str]
    TunnelEchoInterval: Optional[float]
    TunnelFallbackInterval: Optional[float]
    UtmProfile: Optional[str]
    Vdomparam: Optional[str]
    VlanAuto: Optional[str]
    VlanPooling: Optional[str]
    Vlanid: Optional[float]
    VoiceEnterprise: Optional[str]
    MacFilterList: Optional[Sequence["_MacFilterListDefinition"]]
    MpskKey: Optional[Sequence["_MpskKeyDefinition"]]
    PortalMessageOverrides: Optional[Sequence["_PortalMessageOverridesDefinition"]]
    RadiusMacAuthUsergroups: Optional[Sequence["_RadiusMacAuthUsergroupsDefinition"]]
    SelectedUsergroups: Optional[Sequence["_SelectedUsergroupsDefinition"]]
    Usergroup: Optional[Sequence["_UsergroupDefinition"]]
    VlanPool: Optional[Sequence["_VlanPoolDefinition"]]

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
            AccessControlList=json_data.get("AccessControlList"),
            AcctInterimInterval=json_data.get("AcctInterimInterval"),
            AdditionalAkms=json_data.get("AdditionalAkms"),
            AddressGroup=json_data.get("AddressGroup"),
            Alias=json_data.get("Alias"),
            AtfWeight=json_data.get("AtfWeight"),
            Auth=json_data.get("Auth"),
            BroadcastSsid=json_data.get("BroadcastSsid"),
            BroadcastSuppression=json_data.get("BroadcastSuppression"),
            BssColorPartial=json_data.get("BssColorPartial"),
            CaptivePortalAcName=json_data.get("CaptivePortalAcName"),
            CaptivePortalAuthTimeout=json_data.get("CaptivePortalAuthTimeout"),
            CaptivePortalMacauthRadiusSecret=json_data.get("CaptivePortalMacauthRadiusSecret"),
            CaptivePortalMacauthRadiusServer=json_data.get("CaptivePortalMacauthRadiusServer"),
            CaptivePortalRadiusSecret=json_data.get("CaptivePortalRadiusSecret"),
            CaptivePortalRadiusServer=json_data.get("CaptivePortalRadiusServer"),
            CaptivePortalSessionTimeoutInterval=json_data.get("CaptivePortalSessionTimeoutInterval"),
            DhcpLeaseTime=json_data.get("DhcpLeaseTime"),
            DhcpOption43Insertion=json_data.get("DhcpOption43Insertion"),
            DhcpOption82CircuitIdInsertion=json_data.get("DhcpOption82CircuitIdInsertion"),
            DhcpOption82Insertion=json_data.get("DhcpOption82Insertion"),
            DhcpOption82RemoteIdInsertion=json_data.get("DhcpOption82RemoteIdInsertion"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            DynamicVlan=json_data.get("DynamicVlan"),
            EapReauth=json_data.get("EapReauth"),
            EapReauthIntv=json_data.get("EapReauthIntv"),
            EapolKeyRetries=json_data.get("EapolKeyRetries"),
            Encrypt=json_data.get("Encrypt"),
            ExternalFastRoaming=json_data.get("ExternalFastRoaming"),
            ExternalLogout=json_data.get("ExternalLogout"),
            ExternalWeb=json_data.get("ExternalWeb"),
            ExternalWebFormat=json_data.get("ExternalWebFormat"),
            FastBssTransition=json_data.get("FastBssTransition"),
            FastRoaming=json_data.get("FastRoaming"),
            FtMobilityDomain=json_data.get("FtMobilityDomain"),
            FtOverDs=json_data.get("FtOverDs"),
            FtR0KeyLifetime=json_data.get("FtR0KeyLifetime"),
            GtkRekey=json_data.get("GtkRekey"),
            GtkRekeyIntv=json_data.get("GtkRekeyIntv"),
            HighEfficiency=json_data.get("HighEfficiency"),
            Hotspot20Profile=json_data.get("Hotspot20Profile"),
            Id=json_data.get("Id"),
            IgmpSnooping=json_data.get("IgmpSnooping"),
            IntraVapPrivacy=json_data.get("IntraVapPrivacy"),
            Ip=json_data.get("Ip"),
            Ipv6Rules=json_data.get("Ipv6Rules"),
            Key=json_data.get("Key"),
            Keyindex=json_data.get("Keyindex"),
            Ldpc=json_data.get("Ldpc"),
            LocalAuthentication=json_data.get("LocalAuthentication"),
            LocalBridging=json_data.get("LocalBridging"),
            LocalLan=json_data.get("LocalLan"),
            LocalStandalone=json_data.get("LocalStandalone"),
            LocalStandaloneNat=json_data.get("LocalStandaloneNat"),
            MacAuthBypass=json_data.get("MacAuthBypass"),
            MacFilter=json_data.get("MacFilter"),
            MacFilterPolicyOther=json_data.get("MacFilterPolicyOther"),
            MaxClients=json_data.get("MaxClients"),
            MaxClientsAp=json_data.get("MaxClientsAp"),
            MeDisableThresh=json_data.get("MeDisableThresh"),
            MeshBackhaul=json_data.get("MeshBackhaul"),
            Mpsk=json_data.get("Mpsk"),
            MpskConcurrentClients=json_data.get("MpskConcurrentClients"),
            MpskProfile=json_data.get("MpskProfile"),
            MuMimo=json_data.get("MuMimo"),
            MulticastEnhance=json_data.get("MulticastEnhance"),
            MulticastRate=json_data.get("MulticastRate"),
            Name=json_data.get("Name"),
            Okc=json_data.get("Okc"),
            OweGroups=json_data.get("OweGroups"),
            OweTransition=json_data.get("OweTransition"),
            OweTransitionSsid=json_data.get("OweTransitionSsid"),
            Passphrase=json_data.get("Passphrase"),
            Pmf=json_data.get("Pmf"),
            PmfAssocComebackTimeout=json_data.get("PmfAssocComebackTimeout"),
            PmfSaQueryRetryTimeout=json_data.get("PmfSaQueryRetryTimeout"),
            PortMacauth=json_data.get("PortMacauth"),
            PortMacauthReauthTimeout=json_data.get("PortMacauthReauthTimeout"),
            PortMacauthTimeout=json_data.get("PortMacauthTimeout"),
            PortalMessageOverrideGroup=json_data.get("PortalMessageOverrideGroup"),
            PortalType=json_data.get("PortalType"),
            PrimaryWagProfile=json_data.get("PrimaryWagProfile"),
            ProbeRespSuppression=json_data.get("ProbeRespSuppression"),
            ProbeRespThreshold=json_data.get("ProbeRespThreshold"),
            PtkRekey=json_data.get("PtkRekey"),
            PtkRekeyIntv=json_data.get("PtkRekeyIntv"),
            QosProfile=json_data.get("QosProfile"),
            Quarantine=json_data.get("Quarantine"),
            Radio2gThreshold=json_data.get("Radio2gThreshold"),
            Radio5gThreshold=json_data.get("Radio5gThreshold"),
            RadioSensitivity=json_data.get("RadioSensitivity"),
            RadiusMacAuth=json_data.get("RadiusMacAuth"),
            RadiusMacAuthServer=json_data.get("RadiusMacAuthServer"),
            RadiusServer=json_data.get("RadiusServer"),
            Rates11a=json_data.get("Rates11a"),
            Rates11acSs12=json_data.get("Rates11acSs12"),
            Rates11acSs34=json_data.get("Rates11acSs34"),
            Rates11bg=json_data.get("Rates11bg"),
            Rates11nSs12=json_data.get("Rates11nSs12"),
            Rates11nSs34=json_data.get("Rates11nSs34"),
            SaeGroups=json_data.get("SaeGroups"),
            SaePassword=json_data.get("SaePassword"),
            Schedule=json_data.get("Schedule"),
            SecondaryWagProfile=json_data.get("SecondaryWagProfile"),
            Security=json_data.get("Security"),
            SecurityExemptList=json_data.get("SecurityExemptList"),
            SecurityObsoleteOption=json_data.get("SecurityObsoleteOption"),
            SecurityRedirectUrl=json_data.get("SecurityRedirectUrl"),
            SplitTunneling=json_data.get("SplitTunneling"),
            Ssid=json_data.get("Ssid"),
            StickyClientRemove=json_data.get("StickyClientRemove"),
            StickyClientThreshold2g=json_data.get("StickyClientThreshold2g"),
            StickyClientThreshold5g=json_data.get("StickyClientThreshold5g"),
            TargetWakeTime=json_data.get("TargetWakeTime"),
            TkipCounterMeasure=json_data.get("TkipCounterMeasure"),
            TunnelEchoInterval=json_data.get("TunnelEchoInterval"),
            TunnelFallbackInterval=json_data.get("TunnelFallbackInterval"),
            UtmProfile=json_data.get("UtmProfile"),
            Vdomparam=json_data.get("Vdomparam"),
            VlanAuto=json_data.get("VlanAuto"),
            VlanPooling=json_data.get("VlanPooling"),
            Vlanid=json_data.get("Vlanid"),
            VoiceEnterprise=json_data.get("VoiceEnterprise"),
            MacFilterList=deserialize_list(json_data.get("MacFilterList"), MacFilterListDefinition),
            MpskKey=deserialize_list(json_data.get("MpskKey"), MpskKeyDefinition),
            PortalMessageOverrides=deserialize_list(json_data.get("PortalMessageOverrides"), PortalMessageOverridesDefinition),
            RadiusMacAuthUsergroups=deserialize_list(json_data.get("RadiusMacAuthUsergroups"), RadiusMacAuthUsergroupsDefinition),
            SelectedUsergroups=deserialize_list(json_data.get("SelectedUsergroups"), SelectedUsergroupsDefinition),
            Usergroup=deserialize_list(json_data.get("Usergroup"), UsergroupDefinition),
            VlanPool=deserialize_list(json_data.get("VlanPool"), VlanPoolDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MacFilterListDefinition(BaseModel):
    Id: Optional[float]
    Mac: Optional[str]
    MacFilterPolicy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MacFilterListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MacFilterListDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Mac=json_data.get("Mac"),
            MacFilterPolicy=json_data.get("MacFilterPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MacFilterListDefinition = MacFilterListDefinition


@dataclass
class MpskKeyDefinition(BaseModel):
    Comment: Optional[str]
    ConcurrentClients: Optional[str]
    KeyName: Optional[str]
    Passphrase: Optional[str]
    MpskSchedules: Optional[Sequence["_MpskSchedulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MpskKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MpskKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            Comment=json_data.get("Comment"),
            ConcurrentClients=json_data.get("ConcurrentClients"),
            KeyName=json_data.get("KeyName"),
            Passphrase=json_data.get("Passphrase"),
            MpskSchedules=deserialize_list(json_data.get("MpskSchedules"), MpskSchedulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MpskKeyDefinition = MpskKeyDefinition


@dataclass
class MpskSchedulesDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MpskSchedulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MpskSchedulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MpskSchedulesDefinition = MpskSchedulesDefinition


@dataclass
class PortalMessageOverridesDefinition(BaseModel):
    AuthDisclaimerPage: Optional[str]
    AuthLoginFailedPage: Optional[str]
    AuthLoginPage: Optional[str]
    AuthRejectPage: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PortalMessageOverridesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortalMessageOverridesDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthDisclaimerPage=json_data.get("AuthDisclaimerPage"),
            AuthLoginFailedPage=json_data.get("AuthLoginFailedPage"),
            AuthLoginPage=json_data.get("AuthLoginPage"),
            AuthRejectPage=json_data.get("AuthRejectPage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortalMessageOverridesDefinition = PortalMessageOverridesDefinition


@dataclass
class RadiusMacAuthUsergroupsDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RadiusMacAuthUsergroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RadiusMacAuthUsergroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RadiusMacAuthUsergroupsDefinition = RadiusMacAuthUsergroupsDefinition


@dataclass
class SelectedUsergroupsDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SelectedUsergroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SelectedUsergroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SelectedUsergroupsDefinition = SelectedUsergroupsDefinition


@dataclass
class UsergroupDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UsergroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UsergroupDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UsergroupDefinition = UsergroupDefinition


@dataclass
class VlanPoolDefinition(BaseModel):
    Id: Optional[float]
    WtpGroup: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VlanPoolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VlanPoolDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            WtpGroup=json_data.get("WtpGroup"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VlanPoolDefinition = VlanPoolDefinition


