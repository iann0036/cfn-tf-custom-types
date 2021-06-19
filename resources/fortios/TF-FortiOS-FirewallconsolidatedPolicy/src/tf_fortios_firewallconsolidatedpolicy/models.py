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
    ApplicationList: Optional[str]
    AutoAsicOffload: Optional[str]
    AvProfile: Optional[str]
    CaptivePortalExempt: Optional[str]
    CifsProfile: Optional[str]
    Comments: Optional[str]
    DiffservForward: Optional[str]
    DiffservReverse: Optional[str]
    DiffservcodeForward: Optional[str]
    DiffservcodeRev: Optional[str]
    DlpSensor: Optional[str]
    DnsfilterProfile: Optional[str]
    DstaddrNegate: Optional[str]
    DynamicSortSubtable: Optional[str]
    EmailfilterProfile: Optional[str]
    Fixedport: Optional[str]
    HttpPolicyRedirect: Optional[str]
    IcapProfile: Optional[str]
    Id: Optional[str]
    Inbound: Optional[str]
    InspectionMode: Optional[str]
    InternetService: Optional[str]
    InternetServiceNegate: Optional[str]
    InternetServiceSrc: Optional[str]
    InternetServiceSrcNegate: Optional[str]
    Ippool: Optional[str]
    IpsSensor: Optional[str]
    Logtraffic: Optional[str]
    LogtrafficStart: Optional[str]
    Name: Optional[str]
    Nat: Optional[str]
    Outbound: Optional[str]
    PerIpShaper: Optional[str]
    Policyid: Optional[float]
    ProfileGroup: Optional[str]
    ProfileProtocolOptions: Optional[str]
    ProfileType: Optional[str]
    Schedule: Optional[str]
    ServiceNegate: Optional[str]
    SessionTtl: Optional[float]
    SpamfilterProfile: Optional[str]
    SrcaddrNegate: Optional[str]
    SshFilterProfile: Optional[str]
    SshPolicyRedirect: Optional[str]
    SslSshProfile: Optional[str]
    Status: Optional[str]
    TcpMssReceiver: Optional[float]
    TcpMssSender: Optional[float]
    TrafficShaper: Optional[str]
    TrafficShaperReverse: Optional[str]
    UtmStatus: Optional[str]
    Uuid: Optional[str]
    Vdomparam: Optional[str]
    VoipProfile: Optional[str]
    Vpntunnel: Optional[str]
    WafProfile: Optional[str]
    Wanopt: Optional[str]
    WanoptDetection: Optional[str]
    WanoptPassiveOpt: Optional[str]
    WanoptPeer: Optional[str]
    WanoptProfile: Optional[str]
    Webcache: Optional[str]
    WebcacheHttps: Optional[str]
    WebfilterProfile: Optional[str]
    WebproxyForwardServer: Optional[str]
    WebproxyProfile: Optional[str]
    AppCategory: Optional[Sequence["_AppCategoryDefinition"]]
    AppGroup: Optional[Sequence["_AppGroupDefinition"]]
    Application: Optional[Sequence["_ApplicationDefinition"]]
    Dstaddr4: Optional[Sequence["_Dstaddr4Definition"]]
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
    Poolname4: Optional[Sequence["_Poolname4Definition"]]
    Poolname6: Optional[Sequence["_Poolname6Definition"]]
    Service: Optional[Sequence["_ServiceDefinition"]]
    Srcaddr4: Optional[Sequence["_Srcaddr4Definition"]]
    Srcaddr6: Optional[Sequence["_Srcaddr6Definition"]]
    Srcintf: Optional[Sequence["_SrcintfDefinition"]]
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
            ApplicationList=json_data.get("ApplicationList"),
            AutoAsicOffload=json_data.get("AutoAsicOffload"),
            AvProfile=json_data.get("AvProfile"),
            CaptivePortalExempt=json_data.get("CaptivePortalExempt"),
            CifsProfile=json_data.get("CifsProfile"),
            Comments=json_data.get("Comments"),
            DiffservForward=json_data.get("DiffservForward"),
            DiffservReverse=json_data.get("DiffservReverse"),
            DiffservcodeForward=json_data.get("DiffservcodeForward"),
            DiffservcodeRev=json_data.get("DiffservcodeRev"),
            DlpSensor=json_data.get("DlpSensor"),
            DnsfilterProfile=json_data.get("DnsfilterProfile"),
            DstaddrNegate=json_data.get("DstaddrNegate"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            EmailfilterProfile=json_data.get("EmailfilterProfile"),
            Fixedport=json_data.get("Fixedport"),
            HttpPolicyRedirect=json_data.get("HttpPolicyRedirect"),
            IcapProfile=json_data.get("IcapProfile"),
            Id=json_data.get("Id"),
            Inbound=json_data.get("Inbound"),
            InspectionMode=json_data.get("InspectionMode"),
            InternetService=json_data.get("InternetService"),
            InternetServiceNegate=json_data.get("InternetServiceNegate"),
            InternetServiceSrc=json_data.get("InternetServiceSrc"),
            InternetServiceSrcNegate=json_data.get("InternetServiceSrcNegate"),
            Ippool=json_data.get("Ippool"),
            IpsSensor=json_data.get("IpsSensor"),
            Logtraffic=json_data.get("Logtraffic"),
            LogtrafficStart=json_data.get("LogtrafficStart"),
            Name=json_data.get("Name"),
            Nat=json_data.get("Nat"),
            Outbound=json_data.get("Outbound"),
            PerIpShaper=json_data.get("PerIpShaper"),
            Policyid=json_data.get("Policyid"),
            ProfileGroup=json_data.get("ProfileGroup"),
            ProfileProtocolOptions=json_data.get("ProfileProtocolOptions"),
            ProfileType=json_data.get("ProfileType"),
            Schedule=json_data.get("Schedule"),
            ServiceNegate=json_data.get("ServiceNegate"),
            SessionTtl=json_data.get("SessionTtl"),
            SpamfilterProfile=json_data.get("SpamfilterProfile"),
            SrcaddrNegate=json_data.get("SrcaddrNegate"),
            SshFilterProfile=json_data.get("SshFilterProfile"),
            SshPolicyRedirect=json_data.get("SshPolicyRedirect"),
            SslSshProfile=json_data.get("SslSshProfile"),
            Status=json_data.get("Status"),
            TcpMssReceiver=json_data.get("TcpMssReceiver"),
            TcpMssSender=json_data.get("TcpMssSender"),
            TrafficShaper=json_data.get("TrafficShaper"),
            TrafficShaperReverse=json_data.get("TrafficShaperReverse"),
            UtmStatus=json_data.get("UtmStatus"),
            Uuid=json_data.get("Uuid"),
            Vdomparam=json_data.get("Vdomparam"),
            VoipProfile=json_data.get("VoipProfile"),
            Vpntunnel=json_data.get("Vpntunnel"),
            WafProfile=json_data.get("WafProfile"),
            Wanopt=json_data.get("Wanopt"),
            WanoptDetection=json_data.get("WanoptDetection"),
            WanoptPassiveOpt=json_data.get("WanoptPassiveOpt"),
            WanoptPeer=json_data.get("WanoptPeer"),
            WanoptProfile=json_data.get("WanoptProfile"),
            Webcache=json_data.get("Webcache"),
            WebcacheHttps=json_data.get("WebcacheHttps"),
            WebfilterProfile=json_data.get("WebfilterProfile"),
            WebproxyForwardServer=json_data.get("WebproxyForwardServer"),
            WebproxyProfile=json_data.get("WebproxyProfile"),
            AppCategory=deserialize_list(json_data.get("AppCategory"), AppCategoryDefinition),
            AppGroup=deserialize_list(json_data.get("AppGroup"), AppGroupDefinition),
            Application=deserialize_list(json_data.get("Application"), ApplicationDefinition),
            Dstaddr4=deserialize_list(json_data.get("Dstaddr4"), Dstaddr4Definition),
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
            Poolname4=deserialize_list(json_data.get("Poolname4"), Poolname4Definition),
            Poolname6=deserialize_list(json_data.get("Poolname6"), Poolname6Definition),
            Service=deserialize_list(json_data.get("Service"), ServiceDefinition),
            Srcaddr4=deserialize_list(json_data.get("Srcaddr4"), Srcaddr4Definition),
            Srcaddr6=deserialize_list(json_data.get("Srcaddr6"), Srcaddr6Definition),
            Srcintf=deserialize_list(json_data.get("Srcintf"), SrcintfDefinition),
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
class Dstaddr4Definition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Dstaddr4Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Dstaddr4Definition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Dstaddr4Definition = Dstaddr4Definition


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
class Poolname4Definition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Poolname4Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Poolname4Definition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Poolname4Definition = Poolname4Definition


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
class Srcaddr4Definition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Srcaddr4Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Srcaddr4Definition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Srcaddr4Definition = Srcaddr4Definition


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


