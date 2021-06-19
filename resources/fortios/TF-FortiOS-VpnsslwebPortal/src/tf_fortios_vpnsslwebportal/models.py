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
    AllowUserAccess: Optional[str]
    AutoConnect: Optional[str]
    CustomLang: Optional[str]
    CustomizeForticlientDownloadUrl: Optional[str]
    DisplayBookmark: Optional[str]
    DisplayConnectionTools: Optional[str]
    DisplayHistory: Optional[str]
    DisplayStatus: Optional[str]
    DnsServer1: Optional[str]
    DnsServer2: Optional[str]
    DnsSuffix: Optional[str]
    DynamicSortSubtable: Optional[str]
    ExclusiveRouting: Optional[str]
    ForticlientDownload: Optional[str]
    ForticlientDownloadMethod: Optional[str]
    Heading: Optional[str]
    HideSsoCredential: Optional[str]
    HostCheck: Optional[str]
    HostCheckInterval: Optional[float]
    Id: Optional[str]
    IpMode: Optional[str]
    Ipv6DnsServer1: Optional[str]
    Ipv6DnsServer2: Optional[str]
    Ipv6ExclusiveRouting: Optional[str]
    Ipv6ServiceRestriction: Optional[str]
    Ipv6SplitTunneling: Optional[str]
    Ipv6SplitTunnelingRoutingNegate: Optional[str]
    Ipv6TunnelMode: Optional[str]
    Ipv6WinsServer1: Optional[str]
    Ipv6WinsServer2: Optional[str]
    KeepAlive: Optional[str]
    LimitUserLogins: Optional[str]
    MacAddrAction: Optional[str]
    MacAddrCheck: Optional[str]
    MacosForticlientDownloadUrl: Optional[str]
    Name: Optional[str]
    OsCheck: Optional[str]
    RedirUrl: Optional[str]
    SavePassword: Optional[str]
    ServiceRestriction: Optional[str]
    SkipCheckForBrowser: Optional[str]
    SkipCheckForUnsupportedOs: Optional[str]
    SmbMaxVersion: Optional[str]
    SmbMinVersion: Optional[str]
    SmbNtlmv1Auth: Optional[str]
    Smbv1: Optional[str]
    SplitTunneling: Optional[str]
    SplitTunnelingRoutingNegate: Optional[str]
    Theme: Optional[str]
    TransformBackwardSlashes: Optional[str]
    TunnelMode: Optional[str]
    UseSdwan: Optional[str]
    UserBookmark: Optional[str]
    UserGroupBookmark: Optional[str]
    Vdomparam: Optional[str]
    WebMode: Optional[str]
    WindowsForticlientDownloadUrl: Optional[str]
    WinsServer1: Optional[str]
    WinsServer2: Optional[str]
    BookmarkGroup: Optional[Sequence["_BookmarkGroupDefinition"]]
    HostCheckPolicy: Optional[Sequence["_HostCheckPolicyDefinition"]]
    IpPools: Optional[Sequence["_IpPoolsDefinition"]]
    Ipv6Pools: Optional[Sequence["_Ipv6PoolsDefinition"]]
    Ipv6SplitTunnelingRoutingAddress: Optional[Sequence["_Ipv6SplitTunnelingRoutingAddressDefinition"]]
    MacAddrCheckRule: Optional[Sequence["_MacAddrCheckRuleDefinition"]]
    OsCheckList: Optional[Sequence["_OsCheckListDefinition"]]
    SplitDns: Optional[Sequence["_SplitDnsDefinition"]]
    SplitTunnelingRoutingAddress: Optional[Sequence["_SplitTunnelingRoutingAddressDefinition"]]

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
            AllowUserAccess=json_data.get("AllowUserAccess"),
            AutoConnect=json_data.get("AutoConnect"),
            CustomLang=json_data.get("CustomLang"),
            CustomizeForticlientDownloadUrl=json_data.get("CustomizeForticlientDownloadUrl"),
            DisplayBookmark=json_data.get("DisplayBookmark"),
            DisplayConnectionTools=json_data.get("DisplayConnectionTools"),
            DisplayHistory=json_data.get("DisplayHistory"),
            DisplayStatus=json_data.get("DisplayStatus"),
            DnsServer1=json_data.get("DnsServer1"),
            DnsServer2=json_data.get("DnsServer2"),
            DnsSuffix=json_data.get("DnsSuffix"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            ExclusiveRouting=json_data.get("ExclusiveRouting"),
            ForticlientDownload=json_data.get("ForticlientDownload"),
            ForticlientDownloadMethod=json_data.get("ForticlientDownloadMethod"),
            Heading=json_data.get("Heading"),
            HideSsoCredential=json_data.get("HideSsoCredential"),
            HostCheck=json_data.get("HostCheck"),
            HostCheckInterval=json_data.get("HostCheckInterval"),
            Id=json_data.get("Id"),
            IpMode=json_data.get("IpMode"),
            Ipv6DnsServer1=json_data.get("Ipv6DnsServer1"),
            Ipv6DnsServer2=json_data.get("Ipv6DnsServer2"),
            Ipv6ExclusiveRouting=json_data.get("Ipv6ExclusiveRouting"),
            Ipv6ServiceRestriction=json_data.get("Ipv6ServiceRestriction"),
            Ipv6SplitTunneling=json_data.get("Ipv6SplitTunneling"),
            Ipv6SplitTunnelingRoutingNegate=json_data.get("Ipv6SplitTunnelingRoutingNegate"),
            Ipv6TunnelMode=json_data.get("Ipv6TunnelMode"),
            Ipv6WinsServer1=json_data.get("Ipv6WinsServer1"),
            Ipv6WinsServer2=json_data.get("Ipv6WinsServer2"),
            KeepAlive=json_data.get("KeepAlive"),
            LimitUserLogins=json_data.get("LimitUserLogins"),
            MacAddrAction=json_data.get("MacAddrAction"),
            MacAddrCheck=json_data.get("MacAddrCheck"),
            MacosForticlientDownloadUrl=json_data.get("MacosForticlientDownloadUrl"),
            Name=json_data.get("Name"),
            OsCheck=json_data.get("OsCheck"),
            RedirUrl=json_data.get("RedirUrl"),
            SavePassword=json_data.get("SavePassword"),
            ServiceRestriction=json_data.get("ServiceRestriction"),
            SkipCheckForBrowser=json_data.get("SkipCheckForBrowser"),
            SkipCheckForUnsupportedOs=json_data.get("SkipCheckForUnsupportedOs"),
            SmbMaxVersion=json_data.get("SmbMaxVersion"),
            SmbMinVersion=json_data.get("SmbMinVersion"),
            SmbNtlmv1Auth=json_data.get("SmbNtlmv1Auth"),
            Smbv1=json_data.get("Smbv1"),
            SplitTunneling=json_data.get("SplitTunneling"),
            SplitTunnelingRoutingNegate=json_data.get("SplitTunnelingRoutingNegate"),
            Theme=json_data.get("Theme"),
            TransformBackwardSlashes=json_data.get("TransformBackwardSlashes"),
            TunnelMode=json_data.get("TunnelMode"),
            UseSdwan=json_data.get("UseSdwan"),
            UserBookmark=json_data.get("UserBookmark"),
            UserGroupBookmark=json_data.get("UserGroupBookmark"),
            Vdomparam=json_data.get("Vdomparam"),
            WebMode=json_data.get("WebMode"),
            WindowsForticlientDownloadUrl=json_data.get("WindowsForticlientDownloadUrl"),
            WinsServer1=json_data.get("WinsServer1"),
            WinsServer2=json_data.get("WinsServer2"),
            BookmarkGroup=deserialize_list(json_data.get("BookmarkGroup"), BookmarkGroupDefinition),
            HostCheckPolicy=deserialize_list(json_data.get("HostCheckPolicy"), HostCheckPolicyDefinition),
            IpPools=deserialize_list(json_data.get("IpPools"), IpPoolsDefinition),
            Ipv6Pools=deserialize_list(json_data.get("Ipv6Pools"), Ipv6PoolsDefinition),
            Ipv6SplitTunnelingRoutingAddress=deserialize_list(json_data.get("Ipv6SplitTunnelingRoutingAddress"), Ipv6SplitTunnelingRoutingAddressDefinition),
            MacAddrCheckRule=deserialize_list(json_data.get("MacAddrCheckRule"), MacAddrCheckRuleDefinition),
            OsCheckList=deserialize_list(json_data.get("OsCheckList"), OsCheckListDefinition),
            SplitDns=deserialize_list(json_data.get("SplitDns"), SplitDnsDefinition),
            SplitTunnelingRoutingAddress=deserialize_list(json_data.get("SplitTunnelingRoutingAddress"), SplitTunnelingRoutingAddressDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BookmarkGroupDefinition(BaseModel):
    Name: Optional[str]
    Bookmarks: Optional[Sequence["_BookmarksDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BookmarkGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BookmarkGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Bookmarks=deserialize_list(json_data.get("Bookmarks"), BookmarksDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BookmarkGroupDefinition = BookmarkGroupDefinition


@dataclass
class BookmarksDefinition(BaseModel):
    AdditionalParams: Optional[str]
    Apptype: Optional[str]
    Description: Optional[str]
    Domain: Optional[str]
    Folder: Optional[str]
    Host: Optional[str]
    ListeningPort: Optional[float]
    LoadBalancingInfo: Optional[str]
    LogonPassword: Optional[str]
    LogonUser: Optional[str]
    Name: Optional[str]
    Port: Optional[float]
    PreconnectionBlob: Optional[str]
    PreconnectionId: Optional[float]
    RemotePort: Optional[float]
    Security: Optional[str]
    ServerLayout: Optional[str]
    ShowStatusWindow: Optional[str]
    Sso: Optional[str]
    SsoCredential: Optional[str]
    SsoCredentialSentOnce: Optional[str]
    SsoPassword: Optional[str]
    SsoUsername: Optional[str]
    Url: Optional[str]
    FormData: Optional[Sequence["_FormDataDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BookmarksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BookmarksDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalParams=json_data.get("AdditionalParams"),
            Apptype=json_data.get("Apptype"),
            Description=json_data.get("Description"),
            Domain=json_data.get("Domain"),
            Folder=json_data.get("Folder"),
            Host=json_data.get("Host"),
            ListeningPort=json_data.get("ListeningPort"),
            LoadBalancingInfo=json_data.get("LoadBalancingInfo"),
            LogonPassword=json_data.get("LogonPassword"),
            LogonUser=json_data.get("LogonUser"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            PreconnectionBlob=json_data.get("PreconnectionBlob"),
            PreconnectionId=json_data.get("PreconnectionId"),
            RemotePort=json_data.get("RemotePort"),
            Security=json_data.get("Security"),
            ServerLayout=json_data.get("ServerLayout"),
            ShowStatusWindow=json_data.get("ShowStatusWindow"),
            Sso=json_data.get("Sso"),
            SsoCredential=json_data.get("SsoCredential"),
            SsoCredentialSentOnce=json_data.get("SsoCredentialSentOnce"),
            SsoPassword=json_data.get("SsoPassword"),
            SsoUsername=json_data.get("SsoUsername"),
            Url=json_data.get("Url"),
            FormData=deserialize_list(json_data.get("FormData"), FormDataDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BookmarksDefinition = BookmarksDefinition


@dataclass
class FormDataDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FormDataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FormDataDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FormDataDefinition = FormDataDefinition


@dataclass
class HostCheckPolicyDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HostCheckPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostCheckPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostCheckPolicyDefinition = HostCheckPolicyDefinition


@dataclass
class IpPoolsDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpPoolsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpPoolsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpPoolsDefinition = IpPoolsDefinition


@dataclass
class Ipv6PoolsDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv6PoolsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv6PoolsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv6PoolsDefinition = Ipv6PoolsDefinition


@dataclass
class Ipv6SplitTunnelingRoutingAddressDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv6SplitTunnelingRoutingAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv6SplitTunnelingRoutingAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv6SplitTunnelingRoutingAddressDefinition = Ipv6SplitTunnelingRoutingAddressDefinition


@dataclass
class MacAddrCheckRuleDefinition(BaseModel):
    MacAddrMask: Optional[float]
    Name: Optional[str]
    MacAddrList: Optional[Sequence["_MacAddrListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MacAddrCheckRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MacAddrCheckRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            MacAddrMask=json_data.get("MacAddrMask"),
            Name=json_data.get("Name"),
            MacAddrList=deserialize_list(json_data.get("MacAddrList"), MacAddrListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MacAddrCheckRuleDefinition = MacAddrCheckRuleDefinition


@dataclass
class MacAddrListDefinition(BaseModel):
    Addr: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MacAddrListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MacAddrListDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MacAddrListDefinition = MacAddrListDefinition


@dataclass
class OsCheckListDefinition(BaseModel):
    Action: Optional[str]
    LatestPatchLevel: Optional[str]
    Name: Optional[str]
    Tolerance: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_OsCheckListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OsCheckListDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            LatestPatchLevel=json_data.get("LatestPatchLevel"),
            Name=json_data.get("Name"),
            Tolerance=json_data.get("Tolerance"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OsCheckListDefinition = OsCheckListDefinition


@dataclass
class SplitDnsDefinition(BaseModel):
    DnsServer1: Optional[str]
    DnsServer2: Optional[str]
    Domains: Optional[str]
    Id: Optional[float]
    Ipv6DnsServer1: Optional[str]
    Ipv6DnsServer2: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SplitDnsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SplitDnsDefinition"]:
        if not json_data:
            return None
        return cls(
            DnsServer1=json_data.get("DnsServer1"),
            DnsServer2=json_data.get("DnsServer2"),
            Domains=json_data.get("Domains"),
            Id=json_data.get("Id"),
            Ipv6DnsServer1=json_data.get("Ipv6DnsServer1"),
            Ipv6DnsServer2=json_data.get("Ipv6DnsServer2"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SplitDnsDefinition = SplitDnsDefinition


@dataclass
class SplitTunnelingRoutingAddressDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SplitTunnelingRoutingAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SplitTunnelingRoutingAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SplitTunnelingRoutingAddressDefinition = SplitTunnelingRoutingAddressDefinition


