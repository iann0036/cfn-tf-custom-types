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
    Algorithm: Optional[str]
    AuthSessionCheckSourceIp: Optional[str]
    AuthTimeout: Optional[float]
    AutoTunnelStaticRoute: Optional[str]
    BannedCipher: Optional[str]
    CheckReferer: Optional[str]
    DefaultPortal: Optional[str]
    DeflateCompressionLevel: Optional[float]
    DeflateMinDataSize: Optional[float]
    DnsServer1: Optional[str]
    DnsServer2: Optional[str]
    DnsSuffix: Optional[str]
    DtlsHelloTimeout: Optional[float]
    DtlsMaxProtoVer: Optional[str]
    DtlsMinProtoVer: Optional[str]
    DtlsTunnel: Optional[str]
    DynamicSortSubtable: Optional[str]
    Encode2fSequence: Optional[str]
    EncryptAndStorePassword: Optional[str]
    ForceTwoFactorAuth: Optional[str]
    HeaderXForwardedFor: Optional[str]
    HstsIncludeSubdomains: Optional[str]
    HttpCompression: Optional[str]
    HttpOnlyCookie: Optional[str]
    HttpRequestBodyTimeout: Optional[float]
    HttpRequestHeaderTimeout: Optional[float]
    HttpsRedirect: Optional[str]
    Id: Optional[str]
    IdleTimeout: Optional[float]
    Ipv6DnsServer1: Optional[str]
    Ipv6DnsServer2: Optional[str]
    Ipv6WinsServer1: Optional[str]
    Ipv6WinsServer2: Optional[str]
    LoginAttemptLimit: Optional[float]
    LoginBlockTime: Optional[float]
    LoginTimeout: Optional[float]
    Port: Optional[float]
    PortPrecedence: Optional[str]
    Reqclientcert: Optional[str]
    RouteSourceInterface: Optional[str]
    Servercert: Optional[str]
    SourceAddress6Negate: Optional[str]
    SourceAddressNegate: Optional[str]
    SslClientRenegotiation: Optional[str]
    SslInsertEmptyFragment: Optional[str]
    SslMaxProtoVer: Optional[str]
    SslMinProtoVer: Optional[str]
    Tlsv10: Optional[str]
    Tlsv11: Optional[str]
    Tlsv12: Optional[str]
    Tlsv13: Optional[str]
    TransformBackwardSlashes: Optional[str]
    TunnelConnectWithoutReauth: Optional[str]
    TunnelUserSessionTimeout: Optional[float]
    UnsafeLegacyRenegotiation: Optional[str]
    UrlObscuration: Optional[str]
    UserPeer: Optional[str]
    Vdomparam: Optional[str]
    WinsServer1: Optional[str]
    WinsServer2: Optional[str]
    XContentTypeOptions: Optional[str]
    AuthenticationRule: Optional[Sequence["_AuthenticationRuleDefinition"]]
    SourceAddress: Optional[Sequence["_SourceAddressDefinition"]]
    SourceAddress6: Optional[Sequence["_SourceAddress6Definition"]]
    SourceInterface: Optional[Sequence["_SourceInterfaceDefinition"]]
    TunnelIpPools: Optional[Sequence["_TunnelIpPoolsDefinition"]]
    TunnelIpv6Pools: Optional[Sequence["_TunnelIpv6PoolsDefinition"]]

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
            Algorithm=json_data.get("Algorithm"),
            AuthSessionCheckSourceIp=json_data.get("AuthSessionCheckSourceIp"),
            AuthTimeout=json_data.get("AuthTimeout"),
            AutoTunnelStaticRoute=json_data.get("AutoTunnelStaticRoute"),
            BannedCipher=json_data.get("BannedCipher"),
            CheckReferer=json_data.get("CheckReferer"),
            DefaultPortal=json_data.get("DefaultPortal"),
            DeflateCompressionLevel=json_data.get("DeflateCompressionLevel"),
            DeflateMinDataSize=json_data.get("DeflateMinDataSize"),
            DnsServer1=json_data.get("DnsServer1"),
            DnsServer2=json_data.get("DnsServer2"),
            DnsSuffix=json_data.get("DnsSuffix"),
            DtlsHelloTimeout=json_data.get("DtlsHelloTimeout"),
            DtlsMaxProtoVer=json_data.get("DtlsMaxProtoVer"),
            DtlsMinProtoVer=json_data.get("DtlsMinProtoVer"),
            DtlsTunnel=json_data.get("DtlsTunnel"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Encode2fSequence=json_data.get("Encode2fSequence"),
            EncryptAndStorePassword=json_data.get("EncryptAndStorePassword"),
            ForceTwoFactorAuth=json_data.get("ForceTwoFactorAuth"),
            HeaderXForwardedFor=json_data.get("HeaderXForwardedFor"),
            HstsIncludeSubdomains=json_data.get("HstsIncludeSubdomains"),
            HttpCompression=json_data.get("HttpCompression"),
            HttpOnlyCookie=json_data.get("HttpOnlyCookie"),
            HttpRequestBodyTimeout=json_data.get("HttpRequestBodyTimeout"),
            HttpRequestHeaderTimeout=json_data.get("HttpRequestHeaderTimeout"),
            HttpsRedirect=json_data.get("HttpsRedirect"),
            Id=json_data.get("Id"),
            IdleTimeout=json_data.get("IdleTimeout"),
            Ipv6DnsServer1=json_data.get("Ipv6DnsServer1"),
            Ipv6DnsServer2=json_data.get("Ipv6DnsServer2"),
            Ipv6WinsServer1=json_data.get("Ipv6WinsServer1"),
            Ipv6WinsServer2=json_data.get("Ipv6WinsServer2"),
            LoginAttemptLimit=json_data.get("LoginAttemptLimit"),
            LoginBlockTime=json_data.get("LoginBlockTime"),
            LoginTimeout=json_data.get("LoginTimeout"),
            Port=json_data.get("Port"),
            PortPrecedence=json_data.get("PortPrecedence"),
            Reqclientcert=json_data.get("Reqclientcert"),
            RouteSourceInterface=json_data.get("RouteSourceInterface"),
            Servercert=json_data.get("Servercert"),
            SourceAddress6Negate=json_data.get("SourceAddress6Negate"),
            SourceAddressNegate=json_data.get("SourceAddressNegate"),
            SslClientRenegotiation=json_data.get("SslClientRenegotiation"),
            SslInsertEmptyFragment=json_data.get("SslInsertEmptyFragment"),
            SslMaxProtoVer=json_data.get("SslMaxProtoVer"),
            SslMinProtoVer=json_data.get("SslMinProtoVer"),
            Tlsv10=json_data.get("Tlsv10"),
            Tlsv11=json_data.get("Tlsv11"),
            Tlsv12=json_data.get("Tlsv12"),
            Tlsv13=json_data.get("Tlsv13"),
            TransformBackwardSlashes=json_data.get("TransformBackwardSlashes"),
            TunnelConnectWithoutReauth=json_data.get("TunnelConnectWithoutReauth"),
            TunnelUserSessionTimeout=json_data.get("TunnelUserSessionTimeout"),
            UnsafeLegacyRenegotiation=json_data.get("UnsafeLegacyRenegotiation"),
            UrlObscuration=json_data.get("UrlObscuration"),
            UserPeer=json_data.get("UserPeer"),
            Vdomparam=json_data.get("Vdomparam"),
            WinsServer1=json_data.get("WinsServer1"),
            WinsServer2=json_data.get("WinsServer2"),
            XContentTypeOptions=json_data.get("XContentTypeOptions"),
            AuthenticationRule=deserialize_list(json_data.get("AuthenticationRule"), AuthenticationRuleDefinition),
            SourceAddress=deserialize_list(json_data.get("SourceAddress"), SourceAddressDefinition),
            SourceAddress6=deserialize_list(json_data.get("SourceAddress6"), SourceAddress6Definition),
            SourceInterface=deserialize_list(json_data.get("SourceInterface"), SourceInterfaceDefinition),
            TunnelIpPools=deserialize_list(json_data.get("TunnelIpPools"), TunnelIpPoolsDefinition),
            TunnelIpv6Pools=deserialize_list(json_data.get("TunnelIpv6Pools"), TunnelIpv6PoolsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AuthenticationRuleDefinition(BaseModel):
    Auth: Optional[str]
    Cipher: Optional[str]
    ClientCert: Optional[str]
    Id: Optional[float]
    Portal: Optional[str]
    Realm: Optional[str]
    SourceAddress6Negate: Optional[str]
    SourceAddressNegate: Optional[str]
    UserPeer: Optional[str]
    Groups: Optional[Sequence["_GroupsDefinition"]]
    SourceAddress: Optional[Sequence["_SourceAddressDefinition"]]
    SourceAddress6: Optional[Sequence["_SourceAddress6Definition"]]
    SourceInterface: Optional[Sequence["_SourceInterfaceDefinition"]]
    Users: Optional[Sequence["_UsersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AuthenticationRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthenticationRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Auth=json_data.get("Auth"),
            Cipher=json_data.get("Cipher"),
            ClientCert=json_data.get("ClientCert"),
            Id=json_data.get("Id"),
            Portal=json_data.get("Portal"),
            Realm=json_data.get("Realm"),
            SourceAddress6Negate=json_data.get("SourceAddress6Negate"),
            SourceAddressNegate=json_data.get("SourceAddressNegate"),
            UserPeer=json_data.get("UserPeer"),
            Groups=deserialize_list(json_data.get("Groups"), GroupsDefinition),
            SourceAddress=deserialize_list(json_data.get("SourceAddress"), SourceAddressDefinition),
            SourceAddress6=deserialize_list(json_data.get("SourceAddress6"), SourceAddress6Definition),
            SourceInterface=deserialize_list(json_data.get("SourceInterface"), SourceInterfaceDefinition),
            Users=deserialize_list(json_data.get("Users"), UsersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthenticationRuleDefinition = AuthenticationRuleDefinition


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
class SourceAddressDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceAddressDefinition = SourceAddressDefinition


@dataclass
class SourceAddress6Definition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceAddress6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceAddress6Definition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceAddress6Definition = SourceAddress6Definition


@dataclass
class SourceInterfaceDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceInterfaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceInterfaceDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceInterfaceDefinition = SourceInterfaceDefinition


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


@dataclass
class TunnelIpPoolsDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TunnelIpPoolsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TunnelIpPoolsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TunnelIpPoolsDefinition = TunnelIpPoolsDefinition


@dataclass
class TunnelIpv6PoolsDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TunnelIpv6PoolsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TunnelIpv6PoolsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TunnelIpv6PoolsDefinition = TunnelIpv6PoolsDefinition


