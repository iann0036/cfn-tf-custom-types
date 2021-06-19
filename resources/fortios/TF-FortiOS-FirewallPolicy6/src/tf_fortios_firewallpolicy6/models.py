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
    AutoAsicOffload: Optional[str]
    AvProfile: Optional[str]
    CifsProfile: Optional[str]
    Comments: Optional[str]
    DecryptedTrafficMirror: Optional[str]
    DiffservForward: Optional[str]
    DiffservReverse: Optional[str]
    DiffservcodeForward: Optional[str]
    DiffservcodeRev: Optional[str]
    DlpSensor: Optional[str]
    DnsfilterProfile: Optional[str]
    Dsri: Optional[str]
    DstaddrNegate: Optional[str]
    DynamicSortSubtable: Optional[str]
    EmailfilterProfile: Optional[str]
    FirewallSessionDirty: Optional[str]
    Fixedport: Optional[str]
    GlobalLabel: Optional[str]
    HttpPolicyRedirect: Optional[str]
    IcapProfile: Optional[str]
    Id: Optional[str]
    Inbound: Optional[str]
    InspectionMode: Optional[str]
    Ippool: Optional[str]
    IpsSensor: Optional[str]
    Label: Optional[str]
    Logtraffic: Optional[str]
    LogtrafficStart: Optional[str]
    Name: Optional[str]
    Nat: Optional[str]
    Natinbound: Optional[str]
    Natoutbound: Optional[str]
    Outbound: Optional[str]
    PerIpShaper: Optional[str]
    Policyid: Optional[float]
    ProfileGroup: Optional[str]
    ProfileProtocolOptions: Optional[str]
    ProfileType: Optional[str]
    ReplacemsgOverrideGroup: Optional[str]
    Rsso: Optional[str]
    Schedule: Optional[str]
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
    Webcache: Optional[str]
    WebcacheHttps: Optional[str]
    WebfilterProfile: Optional[str]
    WebproxyForwardServer: Optional[str]
    WebproxyProfile: Optional[str]
    AppCategory: Optional[Sequence["_AppCategoryDefinition"]]
    AppGroup: Optional[Sequence["_AppGroupDefinition"]]
    Application: Optional[Sequence["_ApplicationDefinition"]]
    CustomLogFields: Optional[Sequence["_CustomLogFieldsDefinition"]]
    Devices: Optional[Sequence["_DevicesDefinition"]]
    Dstaddr: Optional[Sequence["_DstaddrDefinition"]]
    Dstintf: Optional[Sequence["_DstintfDefinition"]]
    FssoGroups: Optional[Sequence["_FssoGroupsDefinition"]]
    Groups: Optional[Sequence["_GroupsDefinition"]]
    Poolname: Optional[Sequence["_PoolnameDefinition"]]
    Service: Optional[Sequence["_ServiceDefinition"]]
    Srcaddr: Optional[Sequence["_SrcaddrDefinition"]]
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
            AutoAsicOffload=json_data.get("AutoAsicOffload"),
            AvProfile=json_data.get("AvProfile"),
            CifsProfile=json_data.get("CifsProfile"),
            Comments=json_data.get("Comments"),
            DecryptedTrafficMirror=json_data.get("DecryptedTrafficMirror"),
            DiffservForward=json_data.get("DiffservForward"),
            DiffservReverse=json_data.get("DiffservReverse"),
            DiffservcodeForward=json_data.get("DiffservcodeForward"),
            DiffservcodeRev=json_data.get("DiffservcodeRev"),
            DlpSensor=json_data.get("DlpSensor"),
            DnsfilterProfile=json_data.get("DnsfilterProfile"),
            Dsri=json_data.get("Dsri"),
            DstaddrNegate=json_data.get("DstaddrNegate"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            EmailfilterProfile=json_data.get("EmailfilterProfile"),
            FirewallSessionDirty=json_data.get("FirewallSessionDirty"),
            Fixedport=json_data.get("Fixedport"),
            GlobalLabel=json_data.get("GlobalLabel"),
            HttpPolicyRedirect=json_data.get("HttpPolicyRedirect"),
            IcapProfile=json_data.get("IcapProfile"),
            Id=json_data.get("Id"),
            Inbound=json_data.get("Inbound"),
            InspectionMode=json_data.get("InspectionMode"),
            Ippool=json_data.get("Ippool"),
            IpsSensor=json_data.get("IpsSensor"),
            Label=json_data.get("Label"),
            Logtraffic=json_data.get("Logtraffic"),
            LogtrafficStart=json_data.get("LogtrafficStart"),
            Name=json_data.get("Name"),
            Nat=json_data.get("Nat"),
            Natinbound=json_data.get("Natinbound"),
            Natoutbound=json_data.get("Natoutbound"),
            Outbound=json_data.get("Outbound"),
            PerIpShaper=json_data.get("PerIpShaper"),
            Policyid=json_data.get("Policyid"),
            ProfileGroup=json_data.get("ProfileGroup"),
            ProfileProtocolOptions=json_data.get("ProfileProtocolOptions"),
            ProfileType=json_data.get("ProfileType"),
            ReplacemsgOverrideGroup=json_data.get("ReplacemsgOverrideGroup"),
            Rsso=json_data.get("Rsso"),
            Schedule=json_data.get("Schedule"),
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
            Webcache=json_data.get("Webcache"),
            WebcacheHttps=json_data.get("WebcacheHttps"),
            WebfilterProfile=json_data.get("WebfilterProfile"),
            WebproxyForwardServer=json_data.get("WebproxyForwardServer"),
            WebproxyProfile=json_data.get("WebproxyProfile"),
            AppCategory=deserialize_list(json_data.get("AppCategory"), AppCategoryDefinition),
            AppGroup=deserialize_list(json_data.get("AppGroup"), AppGroupDefinition),
            Application=deserialize_list(json_data.get("Application"), ApplicationDefinition),
            CustomLogFields=deserialize_list(json_data.get("CustomLogFields"), CustomLogFieldsDefinition),
            Devices=deserialize_list(json_data.get("Devices"), DevicesDefinition),
            Dstaddr=deserialize_list(json_data.get("Dstaddr"), DstaddrDefinition),
            Dstintf=deserialize_list(json_data.get("Dstintf"), DstintfDefinition),
            FssoGroups=deserialize_list(json_data.get("FssoGroups"), FssoGroupsDefinition),
            Groups=deserialize_list(json_data.get("Groups"), GroupsDefinition),
            Poolname=deserialize_list(json_data.get("Poolname"), PoolnameDefinition),
            Service=deserialize_list(json_data.get("Service"), ServiceDefinition),
            Srcaddr=deserialize_list(json_data.get("Srcaddr"), SrcaddrDefinition),
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


