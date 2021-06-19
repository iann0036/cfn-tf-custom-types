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
    Action: Optional[str]
    AntiReplay: Optional[str]
    ApplicationList: Optional[str]
    AuthCert: Optional[str]
    AuthPath: Optional[str]
    AuthRedirectAddr: Optional[str]
    AutoAsicOffload: Optional[str]
    AvProfile: Optional[str]
    BlockNotification: Optional[str]
    CaptivePortalExempt: Optional[str]
    CapturePacket: Optional[str]
    CifsProfile: Optional[str]
    Comments: Optional[str]
    DecryptedTrafficMirror: Optional[str]
    DelayTcpNpuSession: Optional[str]
    DiffservForward: Optional[str]
    DiffservReverse: Optional[str]
    DiffservcodeForward: Optional[str]
    DiffservcodeRev: Optional[str]
    Disclaimer: Optional[str]
    DlpSensor: Optional[str]
    DnsfilterProfile: Optional[str]
    Dsri: Optional[str]
    DstaddrNegate: Optional[str]
    DynamicSortSubtable: Optional[str]
    EmailCollect: Optional[str]
    EmailfilterProfile: Optional[str]
    FileFilterProfile: Optional[str]
    FirewallSessionDirty: Optional[str]
    Fixedport: Optional[str]
    Fsso: Optional[str]
    FssoAgentForNtlm: Optional[str]
    GeoipAnycast: Optional[str]
    GeoipMatch: Optional[str]
    GlobalLabel: Optional[str]
    HttpPolicyRedirect: Optional[str]
    IcapProfile: Optional[str]
    Id: Optional[str]
    IdentityBasedRoute: Optional[str]
    Inbound: Optional[str]
    InspectionMode: Optional[str]
    InternetService: Optional[str]
    InternetServiceNegate: Optional[str]
    InternetServiceSrc: Optional[str]
    InternetServiceSrcNegate: Optional[str]
    Ippool: Optional[str]
    IpsSensor: Optional[str]
    Label: Optional[str]
    LearningMode: Optional[str]
    Logtraffic: Optional[str]
    LogtrafficStart: Optional[str]
    MatchVip: Optional[str]
    MatchVipOnly: Optional[str]
    Name: Optional[str]
    Nat: Optional[str]
    Natinbound: Optional[str]
    Natip: Optional[str]
    Natoutbound: Optional[str]
    Ntlm: Optional[str]
    NtlmGuest: Optional[str]
    Outbound: Optional[str]
    PerIpShaper: Optional[str]
    PermitAnyHost: Optional[str]
    PermitStunHost: Optional[str]
    Policyid: Optional[float]
    ProfileGroup: Optional[str]
    ProfileProtocolOptions: Optional[str]
    ProfileType: Optional[str]
    RadiusMacAuthBypass: Optional[str]
    RedirectUrl: Optional[str]
    ReplacemsgOverrideGroup: Optional[str]
    ReputationDirection: Optional[str]
    ReputationMinimum: Optional[float]
    Rsso: Optional[str]
    RtpNat: Optional[str]
    ScanBotnetConnections: Optional[str]
    Schedule: Optional[str]
    ScheduleTimeout: Optional[str]
    SendDenyPacket: Optional[str]
    ServiceNegate: Optional[str]
    SessionTtl: Optional[float]
    SpamfilterProfile: Optional[str]
    SrcaddrNegate: Optional[str]
    SshFilterProfile: Optional[str]
    SshPolicyRedirect: Optional[str]
    SslMirror: Optional[str]
    SslSshProfile: Optional[str]
    Status: Optional[str]
    TcpMssReceiver: Optional[float]
    TcpMssSender: Optional[float]
    TcpSessionWithoutSyn: Optional[str]
    TimeoutSendRst: Optional[str]
    Tos: Optional[str]
    TosMask: Optional[str]
    TosNegate: Optional[str]
    TrafficShaper: Optional[str]
    TrafficShaperReverse: Optional[str]
    UtmStatus: Optional[str]
    Uuid: Optional[str]
    Vdomparam: Optional[str]
    VlanCosFwd: Optional[float]
    VlanCosRev: Optional[float]
    VlanFilter: Optional[str]
    VoipProfile: Optional[str]
    Vpntunnel: Optional[str]
    WafProfile: Optional[str]
    Wanopt: Optional[str]
    WanoptDetection: Optional[str]
    WanoptPassiveOpt: Optional[str]
    WanoptPeer: Optional[str]
    WanoptProfile: Optional[str]
    Wccp: Optional[str]
    Webcache: Optional[str]
    WebcacheHttps: Optional[str]
    WebfilterProfile: Optional[str]
    WebproxyForwardServer: Optional[str]
    WebproxyProfile: Optional[str]
    Wsso: Optional[str]
    AppCategory: Optional[Sequence["_AppCategoryDefinition"]]
    AppGroup: Optional[Sequence["_AppGroupDefinition"]]
    Application: Optional[Sequence["_ApplicationDefinition"]]
    CustomLogFields: Optional[Sequence["_CustomLogFieldsDefinition"]]
    Devices: Optional[Sequence["_DevicesDefinition"]]
    Dstaddr: Optional[Sequence["_DstaddrDefinition"]]
    Dstaddr6: Optional[Sequence["_Dstaddr6Definition"]]
    Dstintf: Optional[Sequence["_DstintfDefinition"]]
    FssoGroups: Optional[Sequence["_FssoGroupsDefinition"]]
    Groups: Optional[Sequence["_GroupsDefinition"]]
    InternetServiceCustom: Optional[Sequence["_InternetServiceCustomDefinition"]]
    InternetServiceCustomGroup: Optional[Sequence["_InternetServiceCustomGroupDefinition"]]
    InternetServiceGroup: Optional[Sequence["_InternetServiceGroupDefinition"]]
    InternetServiceId: Optional[Sequence["_InternetServiceIdDefinition"]]
    InternetServiceName: Optional[Sequence["_InternetServiceNameDefinition"]]
    InternetServiceSrcCustom: Optional[Sequence["_InternetServiceSrcCustomDefinition"]]
    InternetServiceSrcCustomGroup: Optional[Sequence["_InternetServiceSrcCustomGroupDefinition"]]
    InternetServiceSrcGroup: Optional[Sequence["_InternetServiceSrcGroupDefinition"]]
    InternetServiceSrcId: Optional[Sequence["_InternetServiceSrcIdDefinition"]]
    InternetServiceSrcName: Optional[Sequence["_InternetServiceSrcNameDefinition"]]
    NtlmEnabledBrowsers: Optional[Sequence["_NtlmEnabledBrowsersDefinition"]]
    Poolname: Optional[Sequence["_PoolnameDefinition"]]
    Poolname6: Optional[Sequence["_Poolname6Definition"]]
    RtpAddr: Optional[Sequence["_RtpAddrDefinition"]]
    Service: Optional[Sequence["_ServiceDefinition"]]
    SrcVendorMac: Optional[Sequence["_SrcVendorMacDefinition"]]
    Srcaddr: Optional[Sequence["_SrcaddrDefinition"]]
    Srcaddr6: Optional[Sequence["_Srcaddr6Definition"]]
    Srcintf: Optional[Sequence["_SrcintfDefinition"]]
    SslMirrorIntf: Optional[Sequence["_SslMirrorIntfDefinition"]]
    UrlCategory: Optional[Sequence["_UrlCategoryDefinition"]]
    Users: Optional[Sequence["_UsersDefinition"]]

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
            Action=json_data.get("Action"),
            AntiReplay=json_data.get("AntiReplay"),
            ApplicationList=json_data.get("ApplicationList"),
            AuthCert=json_data.get("AuthCert"),
            AuthPath=json_data.get("AuthPath"),
            AuthRedirectAddr=json_data.get("AuthRedirectAddr"),
            AutoAsicOffload=json_data.get("AutoAsicOffload"),
            AvProfile=json_data.get("AvProfile"),
            BlockNotification=json_data.get("BlockNotification"),
            CaptivePortalExempt=json_data.get("CaptivePortalExempt"),
            CapturePacket=json_data.get("CapturePacket"),
            CifsProfile=json_data.get("CifsProfile"),
            Comments=json_data.get("Comments"),
            DecryptedTrafficMirror=json_data.get("DecryptedTrafficMirror"),
            DelayTcpNpuSession=json_data.get("DelayTcpNpuSession"),
            DiffservForward=json_data.get("DiffservForward"),
            DiffservReverse=json_data.get("DiffservReverse"),
            DiffservcodeForward=json_data.get("DiffservcodeForward"),
            DiffservcodeRev=json_data.get("DiffservcodeRev"),
            Disclaimer=json_data.get("Disclaimer"),
            DlpSensor=json_data.get("DlpSensor"),
            DnsfilterProfile=json_data.get("DnsfilterProfile"),
            Dsri=json_data.get("Dsri"),
            DstaddrNegate=json_data.get("DstaddrNegate"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            EmailCollect=json_data.get("EmailCollect"),
            EmailfilterProfile=json_data.get("EmailfilterProfile"),
            FileFilterProfile=json_data.get("FileFilterProfile"),
            FirewallSessionDirty=json_data.get("FirewallSessionDirty"),
            Fixedport=json_data.get("Fixedport"),
            Fsso=json_data.get("Fsso"),
            FssoAgentForNtlm=json_data.get("FssoAgentForNtlm"),
            GeoipAnycast=json_data.get("GeoipAnycast"),
            GeoipMatch=json_data.get("GeoipMatch"),
            GlobalLabel=json_data.get("GlobalLabel"),
            HttpPolicyRedirect=json_data.get("HttpPolicyRedirect"),
            IcapProfile=json_data.get("IcapProfile"),
            Id=json_data.get("Id"),
            IdentityBasedRoute=json_data.get("IdentityBasedRoute"),
            Inbound=json_data.get("Inbound"),
            InspectionMode=json_data.get("InspectionMode"),
            InternetService=json_data.get("InternetService"),
            InternetServiceNegate=json_data.get("InternetServiceNegate"),
            InternetServiceSrc=json_data.get("InternetServiceSrc"),
            InternetServiceSrcNegate=json_data.get("InternetServiceSrcNegate"),
            Ippool=json_data.get("Ippool"),
            IpsSensor=json_data.get("IpsSensor"),
            Label=json_data.get("Label"),
            LearningMode=json_data.get("LearningMode"),
            Logtraffic=json_data.get("Logtraffic"),
            LogtrafficStart=json_data.get("LogtrafficStart"),
            MatchVip=json_data.get("MatchVip"),
            MatchVipOnly=json_data.get("MatchVipOnly"),
            Name=json_data.get("Name"),
            Nat=json_data.get("Nat"),
            Natinbound=json_data.get("Natinbound"),
            Natip=json_data.get("Natip"),
            Natoutbound=json_data.get("Natoutbound"),
            Ntlm=json_data.get("Ntlm"),
            NtlmGuest=json_data.get("NtlmGuest"),
            Outbound=json_data.get("Outbound"),
            PerIpShaper=json_data.get("PerIpShaper"),
            PermitAnyHost=json_data.get("PermitAnyHost"),
            PermitStunHost=json_data.get("PermitStunHost"),
            Policyid=json_data.get("Policyid"),
            ProfileGroup=json_data.get("ProfileGroup"),
            ProfileProtocolOptions=json_data.get("ProfileProtocolOptions"),
            ProfileType=json_data.get("ProfileType"),
            RadiusMacAuthBypass=json_data.get("RadiusMacAuthBypass"),
            RedirectUrl=json_data.get("RedirectUrl"),
            ReplacemsgOverrideGroup=json_data.get("ReplacemsgOverrideGroup"),
            ReputationDirection=json_data.get("ReputationDirection"),
            ReputationMinimum=json_data.get("ReputationMinimum"),
            Rsso=json_data.get("Rsso"),
            RtpNat=json_data.get("RtpNat"),
            ScanBotnetConnections=json_data.get("ScanBotnetConnections"),
            Schedule=json_data.get("Schedule"),
            ScheduleTimeout=json_data.get("ScheduleTimeout"),
            SendDenyPacket=json_data.get("SendDenyPacket"),
            ServiceNegate=json_data.get("ServiceNegate"),
            SessionTtl=json_data.get("SessionTtl"),
            SpamfilterProfile=json_data.get("SpamfilterProfile"),
            SrcaddrNegate=json_data.get("SrcaddrNegate"),
            SshFilterProfile=json_data.get("SshFilterProfile"),
            SshPolicyRedirect=json_data.get("SshPolicyRedirect"),
            SslMirror=json_data.get("SslMirror"),
            SslSshProfile=json_data.get("SslSshProfile"),
            Status=json_data.get("Status"),
            TcpMssReceiver=json_data.get("TcpMssReceiver"),
            TcpMssSender=json_data.get("TcpMssSender"),
            TcpSessionWithoutSyn=json_data.get("TcpSessionWithoutSyn"),
            TimeoutSendRst=json_data.get("TimeoutSendRst"),
            Tos=json_data.get("Tos"),
            TosMask=json_data.get("TosMask"),
            TosNegate=json_data.get("TosNegate"),
            TrafficShaper=json_data.get("TrafficShaper"),
            TrafficShaperReverse=json_data.get("TrafficShaperReverse"),
            UtmStatus=json_data.get("UtmStatus"),
            Uuid=json_data.get("Uuid"),
            Vdomparam=json_data.get("Vdomparam"),
            VlanCosFwd=json_data.get("VlanCosFwd"),
            VlanCosRev=json_data.get("VlanCosRev"),
            VlanFilter=json_data.get("VlanFilter"),
            VoipProfile=json_data.get("VoipProfile"),
            Vpntunnel=json_data.get("Vpntunnel"),
            WafProfile=json_data.get("WafProfile"),
            Wanopt=json_data.get("Wanopt"),
            WanoptDetection=json_data.get("WanoptDetection"),
            WanoptPassiveOpt=json_data.get("WanoptPassiveOpt"),
            WanoptPeer=json_data.get("WanoptPeer"),
            WanoptProfile=json_data.get("WanoptProfile"),
            Wccp=json_data.get("Wccp"),
            Webcache=json_data.get("Webcache"),
            WebcacheHttps=json_data.get("WebcacheHttps"),
            WebfilterProfile=json_data.get("WebfilterProfile"),
            WebproxyForwardServer=json_data.get("WebproxyForwardServer"),
            WebproxyProfile=json_data.get("WebproxyProfile"),
            Wsso=json_data.get("Wsso"),
            AppCategory=deserialize_list(json_data.get("AppCategory"), AppCategoryDefinition),
            AppGroup=deserialize_list(json_data.get("AppGroup"), AppGroupDefinition),
            Application=deserialize_list(json_data.get("Application"), ApplicationDefinition),
            CustomLogFields=deserialize_list(json_data.get("CustomLogFields"), CustomLogFieldsDefinition),
            Devices=deserialize_list(json_data.get("Devices"), DevicesDefinition),
            Dstaddr=deserialize_list(json_data.get("Dstaddr"), DstaddrDefinition),
            Dstaddr6=deserialize_list(json_data.get("Dstaddr6"), Dstaddr6Definition),
            Dstintf=deserialize_list(json_data.get("Dstintf"), DstintfDefinition),
            FssoGroups=deserialize_list(json_data.get("FssoGroups"), FssoGroupsDefinition),
            Groups=deserialize_list(json_data.get("Groups"), GroupsDefinition),
            InternetServiceCustom=deserialize_list(json_data.get("InternetServiceCustom"), InternetServiceCustomDefinition),
            InternetServiceCustomGroup=deserialize_list(json_data.get("InternetServiceCustomGroup"), InternetServiceCustomGroupDefinition),
            InternetServiceGroup=deserialize_list(json_data.get("InternetServiceGroup"), InternetServiceGroupDefinition),
            InternetServiceId=deserialize_list(json_data.get("InternetServiceId"), InternetServiceIdDefinition),
            InternetServiceName=deserialize_list(json_data.get("InternetServiceName"), InternetServiceNameDefinition),
            InternetServiceSrcCustom=deserialize_list(json_data.get("InternetServiceSrcCustom"), InternetServiceSrcCustomDefinition),
            InternetServiceSrcCustomGroup=deserialize_list(json_data.get("InternetServiceSrcCustomGroup"), InternetServiceSrcCustomGroupDefinition),
            InternetServiceSrcGroup=deserialize_list(json_data.get("InternetServiceSrcGroup"), InternetServiceSrcGroupDefinition),
            InternetServiceSrcId=deserialize_list(json_data.get("InternetServiceSrcId"), InternetServiceSrcIdDefinition),
            InternetServiceSrcName=deserialize_list(json_data.get("InternetServiceSrcName"), InternetServiceSrcNameDefinition),
            NtlmEnabledBrowsers=deserialize_list(json_data.get("NtlmEnabledBrowsers"), NtlmEnabledBrowsersDefinition),
            Poolname=deserialize_list(json_data.get("Poolname"), PoolnameDefinition),
            Poolname6=deserialize_list(json_data.get("Poolname6"), Poolname6Definition),
            RtpAddr=deserialize_list(json_data.get("RtpAddr"), RtpAddrDefinition),
            Service=deserialize_list(json_data.get("Service"), ServiceDefinition),
            SrcVendorMac=deserialize_list(json_data.get("SrcVendorMac"), SrcVendorMacDefinition),
            Srcaddr=deserialize_list(json_data.get("Srcaddr"), SrcaddrDefinition),
            Srcaddr6=deserialize_list(json_data.get("Srcaddr6"), Srcaddr6Definition),
            Srcintf=deserialize_list(json_data.get("Srcintf"), SrcintfDefinition),
            SslMirrorIntf=deserialize_list(json_data.get("SslMirrorIntf"), SslMirrorIntfDefinition),
            UrlCategory=deserialize_list(json_data.get("UrlCategory"), UrlCategoryDefinition),
            Users=deserialize_list(json_data.get("Users"), UsersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AppCategoryDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AppCategoryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppCategoryDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppCategoryDefinition = AppCategoryDefinition


@dataclass
class AppGroupDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AppGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppGroupDefinition = AppGroupDefinition


@dataclass
class ApplicationDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationDefinition = ApplicationDefinition


@dataclass
class CustomLogFieldsDefinition(BaseModel):
    FieldId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomLogFieldsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomLogFieldsDefinition"]:
        if not json_data:
            return None
        return cls(
            FieldId=json_data.get("FieldId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomLogFieldsDefinition = CustomLogFieldsDefinition


@dataclass
class DevicesDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DevicesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DevicesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DevicesDefinition = DevicesDefinition


@dataclass
class DstaddrDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DstaddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DstaddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DstaddrDefinition = DstaddrDefinition


@dataclass
class Dstaddr6Definition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Dstaddr6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Dstaddr6Definition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Dstaddr6Definition = Dstaddr6Definition


@dataclass
class DstintfDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DstintfDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DstintfDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DstintfDefinition = DstintfDefinition


@dataclass
class FssoGroupsDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FssoGroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FssoGroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FssoGroupsDefinition = FssoGroupsDefinition


@dataclass
class GroupsDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GroupsDefinition = GroupsDefinition


@dataclass
class InternetServiceCustomDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InternetServiceCustomDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InternetServiceCustomDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InternetServiceCustomDefinition = InternetServiceCustomDefinition


@dataclass
class InternetServiceCustomGroupDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InternetServiceCustomGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InternetServiceCustomGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InternetServiceCustomGroupDefinition = InternetServiceCustomGroupDefinition


@dataclass
class InternetServiceGroupDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InternetServiceGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InternetServiceGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InternetServiceGroupDefinition = InternetServiceGroupDefinition


@dataclass
class InternetServiceIdDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_InternetServiceIdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InternetServiceIdDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InternetServiceIdDefinition = InternetServiceIdDefinition


@dataclass
class InternetServiceNameDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InternetServiceNameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InternetServiceNameDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InternetServiceNameDefinition = InternetServiceNameDefinition


@dataclass
class InternetServiceSrcCustomDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InternetServiceSrcCustomDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InternetServiceSrcCustomDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InternetServiceSrcCustomDefinition = InternetServiceSrcCustomDefinition


@dataclass
class InternetServiceSrcCustomGroupDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InternetServiceSrcCustomGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InternetServiceSrcCustomGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InternetServiceSrcCustomGroupDefinition = InternetServiceSrcCustomGroupDefinition


@dataclass
class InternetServiceSrcGroupDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InternetServiceSrcGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InternetServiceSrcGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InternetServiceSrcGroupDefinition = InternetServiceSrcGroupDefinition


@dataclass
class InternetServiceSrcIdDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_InternetServiceSrcIdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InternetServiceSrcIdDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InternetServiceSrcIdDefinition = InternetServiceSrcIdDefinition


@dataclass
class InternetServiceSrcNameDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InternetServiceSrcNameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InternetServiceSrcNameDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InternetServiceSrcNameDefinition = InternetServiceSrcNameDefinition


@dataclass
class NtlmEnabledBrowsersDefinition(BaseModel):
    UserAgentString: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NtlmEnabledBrowsersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NtlmEnabledBrowsersDefinition"]:
        if not json_data:
            return None
        return cls(
            UserAgentString=json_data.get("UserAgentString"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NtlmEnabledBrowsersDefinition = NtlmEnabledBrowsersDefinition


@dataclass
class PoolnameDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PoolnameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PoolnameDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PoolnameDefinition = PoolnameDefinition


@dataclass
class Poolname6Definition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Poolname6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Poolname6Definition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Poolname6Definition = Poolname6Definition


@dataclass
class RtpAddrDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RtpAddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RtpAddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RtpAddrDefinition = RtpAddrDefinition


@dataclass
class ServiceDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceDefinition = ServiceDefinition


@dataclass
class SrcVendorMacDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SrcVendorMacDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SrcVendorMacDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SrcVendorMacDefinition = SrcVendorMacDefinition


@dataclass
class SrcaddrDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SrcaddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SrcaddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SrcaddrDefinition = SrcaddrDefinition


@dataclass
class Srcaddr6Definition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Srcaddr6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Srcaddr6Definition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Srcaddr6Definition = Srcaddr6Definition


@dataclass
class SrcintfDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SrcintfDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SrcintfDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SrcintfDefinition = SrcintfDefinition


@dataclass
class SslMirrorIntfDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SslMirrorIntfDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SslMirrorIntfDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SslMirrorIntfDefinition = SslMirrorIntfDefinition


@dataclass
class UrlCategoryDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_UrlCategoryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UrlCategoryDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UrlCategoryDefinition = UrlCategoryDefinition


@dataclass
class UsersDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UsersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UsersDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UsersDefinition = UsersDefinition


