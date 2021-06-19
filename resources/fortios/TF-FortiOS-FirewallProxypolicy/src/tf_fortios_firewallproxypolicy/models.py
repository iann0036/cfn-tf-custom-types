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
    AvProfile: Optional[str]
    CifsProfile: Optional[str]
    Comments: Optional[str]
    DecryptedTrafficMirror: Optional[str]
    Disclaimer: Optional[str]
    DlpSensor: Optional[str]
    DstaddrNegate: Optional[str]
    DynamicSortSubtable: Optional[str]
    EmailfilterProfile: Optional[str]
    FileFilterProfile: Optional[str]
    GlobalLabel: Optional[str]
    HttpTunnelAuth: Optional[str]
    IcapProfile: Optional[str]
    Id: Optional[str]
    InternetService: Optional[str]
    InternetServiceNegate: Optional[str]
    IpsSensor: Optional[str]
    Label: Optional[str]
    Logtraffic: Optional[str]
    LogtrafficStart: Optional[str]
    Name: Optional[str]
    Policyid: Optional[float]
    ProfileGroup: Optional[str]
    ProfileProtocolOptions: Optional[str]
    ProfileType: Optional[str]
    Proxy: Optional[str]
    RedirectUrl: Optional[str]
    ReplacemsgOverrideGroup: Optional[str]
    ScanBotnetConnections: Optional[str]
    Schedule: Optional[str]
    ServiceNegate: Optional[str]
    SessionTtl: Optional[float]
    SpamfilterProfile: Optional[str]
    SrcaddrNegate: Optional[str]
    SshFilterProfile: Optional[str]
    SshPolicyRedirect: Optional[str]
    SslSshProfile: Optional[str]
    Status: Optional[str]
    Transparent: Optional[str]
    UtmStatus: Optional[str]
    Uuid: Optional[str]
    Vdomparam: Optional[str]
    WafProfile: Optional[str]
    Webcache: Optional[str]
    WebcacheHttps: Optional[str]
    WebfilterProfile: Optional[str]
    WebproxyForwardServer: Optional[str]
    WebproxyProfile: Optional[str]
    Dstaddr: Optional[Sequence["_DstaddrDefinition"]]
    Dstaddr6: Optional[Sequence["_Dstaddr6Definition"]]
    Dstintf: Optional[Sequence["_DstintfDefinition"]]
    Groups: Optional[Sequence["_GroupsDefinition"]]
    InternetServiceCustom: Optional[Sequence["_InternetServiceCustomDefinition"]]
    InternetServiceCustomGroup: Optional[Sequence["_InternetServiceCustomGroupDefinition"]]
    InternetServiceGroup: Optional[Sequence["_InternetServiceGroupDefinition"]]
    InternetServiceId: Optional[Sequence["_InternetServiceIdDefinition"]]
    InternetServiceName: Optional[Sequence["_InternetServiceNameDefinition"]]
    Poolname: Optional[Sequence["_PoolnameDefinition"]]
    Service: Optional[Sequence["_ServiceDefinition"]]
    Srcaddr: Optional[Sequence["_SrcaddrDefinition"]]
    Srcaddr6: Optional[Sequence["_Srcaddr6Definition"]]
    Srcintf: Optional[Sequence["_SrcintfDefinition"]]
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
            AvProfile=json_data.get("AvProfile"),
            CifsProfile=json_data.get("CifsProfile"),
            Comments=json_data.get("Comments"),
            DecryptedTrafficMirror=json_data.get("DecryptedTrafficMirror"),
            Disclaimer=json_data.get("Disclaimer"),
            DlpSensor=json_data.get("DlpSensor"),
            DstaddrNegate=json_data.get("DstaddrNegate"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            EmailfilterProfile=json_data.get("EmailfilterProfile"),
            FileFilterProfile=json_data.get("FileFilterProfile"),
            GlobalLabel=json_data.get("GlobalLabel"),
            HttpTunnelAuth=json_data.get("HttpTunnelAuth"),
            IcapProfile=json_data.get("IcapProfile"),
            Id=json_data.get("Id"),
            InternetService=json_data.get("InternetService"),
            InternetServiceNegate=json_data.get("InternetServiceNegate"),
            IpsSensor=json_data.get("IpsSensor"),
            Label=json_data.get("Label"),
            Logtraffic=json_data.get("Logtraffic"),
            LogtrafficStart=json_data.get("LogtrafficStart"),
            Name=json_data.get("Name"),
            Policyid=json_data.get("Policyid"),
            ProfileGroup=json_data.get("ProfileGroup"),
            ProfileProtocolOptions=json_data.get("ProfileProtocolOptions"),
            ProfileType=json_data.get("ProfileType"),
            Proxy=json_data.get("Proxy"),
            RedirectUrl=json_data.get("RedirectUrl"),
            ReplacemsgOverrideGroup=json_data.get("ReplacemsgOverrideGroup"),
            ScanBotnetConnections=json_data.get("ScanBotnetConnections"),
            Schedule=json_data.get("Schedule"),
            ServiceNegate=json_data.get("ServiceNegate"),
            SessionTtl=json_data.get("SessionTtl"),
            SpamfilterProfile=json_data.get("SpamfilterProfile"),
            SrcaddrNegate=json_data.get("SrcaddrNegate"),
            SshFilterProfile=json_data.get("SshFilterProfile"),
            SshPolicyRedirect=json_data.get("SshPolicyRedirect"),
            SslSshProfile=json_data.get("SslSshProfile"),
            Status=json_data.get("Status"),
            Transparent=json_data.get("Transparent"),
            UtmStatus=json_data.get("UtmStatus"),
            Uuid=json_data.get("Uuid"),
            Vdomparam=json_data.get("Vdomparam"),
            WafProfile=json_data.get("WafProfile"),
            Webcache=json_data.get("Webcache"),
            WebcacheHttps=json_data.get("WebcacheHttps"),
            WebfilterProfile=json_data.get("WebfilterProfile"),
            WebproxyForwardServer=json_data.get("WebproxyForwardServer"),
            WebproxyProfile=json_data.get("WebproxyProfile"),
            Dstaddr=deserialize_list(json_data.get("Dstaddr"), DstaddrDefinition),
            Dstaddr6=deserialize_list(json_data.get("Dstaddr6"), Dstaddr6Definition),
            Dstintf=deserialize_list(json_data.get("Dstintf"), DstintfDefinition),
            Groups=deserialize_list(json_data.get("Groups"), GroupsDefinition),
            InternetServiceCustom=deserialize_list(json_data.get("InternetServiceCustom"), InternetServiceCustomDefinition),
            InternetServiceCustomGroup=deserialize_list(json_data.get("InternetServiceCustomGroup"), InternetServiceCustomGroupDefinition),
            InternetServiceGroup=deserialize_list(json_data.get("InternetServiceGroup"), InternetServiceGroupDefinition),
            InternetServiceId=deserialize_list(json_data.get("InternetServiceId"), InternetServiceIdDefinition),
            InternetServiceName=deserialize_list(json_data.get("InternetServiceName"), InternetServiceNameDefinition),
            Poolname=deserialize_list(json_data.get("Poolname"), PoolnameDefinition),
            Service=deserialize_list(json_data.get("Service"), ServiceDefinition),
            Srcaddr=deserialize_list(json_data.get("Srcaddr"), SrcaddrDefinition),
            Srcaddr6=deserialize_list(json_data.get("Srcaddr6"), Srcaddr6Definition),
            Srcintf=deserialize_list(json_data.get("Srcintf"), SrcintfDefinition),
            Users=deserialize_list(json_data.get("Users"), UsersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


