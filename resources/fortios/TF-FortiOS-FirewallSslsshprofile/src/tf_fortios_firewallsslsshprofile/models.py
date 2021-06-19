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
    Allowlist: Optional[str]
    BlockBlacklistedCertificates: Optional[str]
    BlockBlocklistedCertificates: Optional[str]
    Caname: Optional[str]
    Comment: Optional[str]
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    MapiOverHttps: Optional[str]
    Name: Optional[str]
    RpcOverHttps: Optional[str]
    ServerCert: Optional[str]
    ServerCertMode: Optional[str]
    SslAnomaliesLog: Optional[str]
    SslExemptionsLog: Optional[str]
    SslNegotiationLog: Optional[str]
    SupportedAlpn: Optional[str]
    UntrustedCaname: Optional[str]
    UseSslServer: Optional[str]
    Vdomparam: Optional[str]
    Whitelist: Optional[str]
    Ftps: Optional[Sequence["_FtpsDefinition"]]
    Https: Optional[Sequence["_HttpsDefinition"]]
    Imaps: Optional[Sequence["_ImapsDefinition"]]
    Pop3s: Optional[Sequence["_Pop3sDefinition"]]
    Smtps: Optional[Sequence["_SmtpsDefinition"]]
    Ssh: Optional[Sequence["_SshDefinition"]]
    Ssl: Optional[Sequence["_SslDefinition"]]
    SslExempt: Optional[Sequence["_SslExemptDefinition"]]
    SslServer: Optional[Sequence["_SslServerDefinition"]]

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
            Allowlist=json_data.get("Allowlist"),
            BlockBlacklistedCertificates=json_data.get("BlockBlacklistedCertificates"),
            BlockBlocklistedCertificates=json_data.get("BlockBlocklistedCertificates"),
            Caname=json_data.get("Caname"),
            Comment=json_data.get("Comment"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            MapiOverHttps=json_data.get("MapiOverHttps"),
            Name=json_data.get("Name"),
            RpcOverHttps=json_data.get("RpcOverHttps"),
            ServerCert=json_data.get("ServerCert"),
            ServerCertMode=json_data.get("ServerCertMode"),
            SslAnomaliesLog=json_data.get("SslAnomaliesLog"),
            SslExemptionsLog=json_data.get("SslExemptionsLog"),
            SslNegotiationLog=json_data.get("SslNegotiationLog"),
            SupportedAlpn=json_data.get("SupportedAlpn"),
            UntrustedCaname=json_data.get("UntrustedCaname"),
            UseSslServer=json_data.get("UseSslServer"),
            Vdomparam=json_data.get("Vdomparam"),
            Whitelist=json_data.get("Whitelist"),
            Ftps=deserialize_list(json_data.get("Ftps"), FtpsDefinition),
            Https=deserialize_list(json_data.get("Https"), HttpsDefinition),
            Imaps=deserialize_list(json_data.get("Imaps"), ImapsDefinition),
            Pop3s=deserialize_list(json_data.get("Pop3s"), Pop3sDefinition),
            Smtps=deserialize_list(json_data.get("Smtps"), SmtpsDefinition),
            Ssh=deserialize_list(json_data.get("Ssh"), SshDefinition),
            Ssl=deserialize_list(json_data.get("Ssl"), SslDefinition),
            SslExempt=deserialize_list(json_data.get("SslExempt"), SslExemptDefinition),
            SslServer=deserialize_list(json_data.get("SslServer"), SslServerDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FtpsDefinition(BaseModel):
    CertValidationFailure: Optional[str]
    CertValidationTimeout: Optional[str]
    ClientCertRequest: Optional[str]
    ClientCertificate: Optional[str]
    ExpiredServerCert: Optional[str]
    InvalidServerCert: Optional[str]
    Ports: Optional[str]
    RevokedServerCert: Optional[str]
    SniServerCertCheck: Optional[str]
    Status: Optional[str]
    UnsupportedSsl: Optional[str]
    UnsupportedSslCipher: Optional[str]
    UnsupportedSslNegotiation: Optional[str]
    UntrustedServerCert: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FtpsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FtpsDefinition"]:
        if not json_data:
            return None
        return cls(
            CertValidationFailure=json_data.get("CertValidationFailure"),
            CertValidationTimeout=json_data.get("CertValidationTimeout"),
            ClientCertRequest=json_data.get("ClientCertRequest"),
            ClientCertificate=json_data.get("ClientCertificate"),
            ExpiredServerCert=json_data.get("ExpiredServerCert"),
            InvalidServerCert=json_data.get("InvalidServerCert"),
            Ports=json_data.get("Ports"),
            RevokedServerCert=json_data.get("RevokedServerCert"),
            SniServerCertCheck=json_data.get("SniServerCertCheck"),
            Status=json_data.get("Status"),
            UnsupportedSsl=json_data.get("UnsupportedSsl"),
            UnsupportedSslCipher=json_data.get("UnsupportedSslCipher"),
            UnsupportedSslNegotiation=json_data.get("UnsupportedSslNegotiation"),
            UntrustedServerCert=json_data.get("UntrustedServerCert"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FtpsDefinition = FtpsDefinition


@dataclass
class HttpsDefinition(BaseModel):
    CertValidationFailure: Optional[str]
    CertValidationTimeout: Optional[str]
    ClientCertRequest: Optional[str]
    ClientCertificate: Optional[str]
    ExpiredServerCert: Optional[str]
    InvalidServerCert: Optional[str]
    Ports: Optional[str]
    ProxyAfterTcpHandshake: Optional[str]
    RevokedServerCert: Optional[str]
    SniServerCertCheck: Optional[str]
    Status: Optional[str]
    UnsupportedSsl: Optional[str]
    UnsupportedSslCipher: Optional[str]
    UnsupportedSslNegotiation: Optional[str]
    UntrustedServerCert: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpsDefinition"]:
        if not json_data:
            return None
        return cls(
            CertValidationFailure=json_data.get("CertValidationFailure"),
            CertValidationTimeout=json_data.get("CertValidationTimeout"),
            ClientCertRequest=json_data.get("ClientCertRequest"),
            ClientCertificate=json_data.get("ClientCertificate"),
            ExpiredServerCert=json_data.get("ExpiredServerCert"),
            InvalidServerCert=json_data.get("InvalidServerCert"),
            Ports=json_data.get("Ports"),
            ProxyAfterTcpHandshake=json_data.get("ProxyAfterTcpHandshake"),
            RevokedServerCert=json_data.get("RevokedServerCert"),
            SniServerCertCheck=json_data.get("SniServerCertCheck"),
            Status=json_data.get("Status"),
            UnsupportedSsl=json_data.get("UnsupportedSsl"),
            UnsupportedSslCipher=json_data.get("UnsupportedSslCipher"),
            UnsupportedSslNegotiation=json_data.get("UnsupportedSslNegotiation"),
            UntrustedServerCert=json_data.get("UntrustedServerCert"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpsDefinition = HttpsDefinition


@dataclass
class ImapsDefinition(BaseModel):
    CertValidationFailure: Optional[str]
    CertValidationTimeout: Optional[str]
    ClientCertRequest: Optional[str]
    ClientCertificate: Optional[str]
    ExpiredServerCert: Optional[str]
    InvalidServerCert: Optional[str]
    Ports: Optional[str]
    ProxyAfterTcpHandshake: Optional[str]
    RevokedServerCert: Optional[str]
    SniServerCertCheck: Optional[str]
    Status: Optional[str]
    UnsupportedSsl: Optional[str]
    UnsupportedSslCipher: Optional[str]
    UnsupportedSslNegotiation: Optional[str]
    UntrustedServerCert: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ImapsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImapsDefinition"]:
        if not json_data:
            return None
        return cls(
            CertValidationFailure=json_data.get("CertValidationFailure"),
            CertValidationTimeout=json_data.get("CertValidationTimeout"),
            ClientCertRequest=json_data.get("ClientCertRequest"),
            ClientCertificate=json_data.get("ClientCertificate"),
            ExpiredServerCert=json_data.get("ExpiredServerCert"),
            InvalidServerCert=json_data.get("InvalidServerCert"),
            Ports=json_data.get("Ports"),
            ProxyAfterTcpHandshake=json_data.get("ProxyAfterTcpHandshake"),
            RevokedServerCert=json_data.get("RevokedServerCert"),
            SniServerCertCheck=json_data.get("SniServerCertCheck"),
            Status=json_data.get("Status"),
            UnsupportedSsl=json_data.get("UnsupportedSsl"),
            UnsupportedSslCipher=json_data.get("UnsupportedSslCipher"),
            UnsupportedSslNegotiation=json_data.get("UnsupportedSslNegotiation"),
            UntrustedServerCert=json_data.get("UntrustedServerCert"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImapsDefinition = ImapsDefinition


@dataclass
class Pop3sDefinition(BaseModel):
    CertValidationFailure: Optional[str]
    CertValidationTimeout: Optional[str]
    ClientCertRequest: Optional[str]
    ClientCertificate: Optional[str]
    ExpiredServerCert: Optional[str]
    InvalidServerCert: Optional[str]
    Ports: Optional[str]
    ProxyAfterTcpHandshake: Optional[str]
    RevokedServerCert: Optional[str]
    SniServerCertCheck: Optional[str]
    Status: Optional[str]
    UnsupportedSsl: Optional[str]
    UnsupportedSslCipher: Optional[str]
    UnsupportedSslNegotiation: Optional[str]
    UntrustedServerCert: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Pop3sDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Pop3sDefinition"]:
        if not json_data:
            return None
        return cls(
            CertValidationFailure=json_data.get("CertValidationFailure"),
            CertValidationTimeout=json_data.get("CertValidationTimeout"),
            ClientCertRequest=json_data.get("ClientCertRequest"),
            ClientCertificate=json_data.get("ClientCertificate"),
            ExpiredServerCert=json_data.get("ExpiredServerCert"),
            InvalidServerCert=json_data.get("InvalidServerCert"),
            Ports=json_data.get("Ports"),
            ProxyAfterTcpHandshake=json_data.get("ProxyAfterTcpHandshake"),
            RevokedServerCert=json_data.get("RevokedServerCert"),
            SniServerCertCheck=json_data.get("SniServerCertCheck"),
            Status=json_data.get("Status"),
            UnsupportedSsl=json_data.get("UnsupportedSsl"),
            UnsupportedSslCipher=json_data.get("UnsupportedSslCipher"),
            UnsupportedSslNegotiation=json_data.get("UnsupportedSslNegotiation"),
            UntrustedServerCert=json_data.get("UntrustedServerCert"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Pop3sDefinition = Pop3sDefinition


@dataclass
class SmtpsDefinition(BaseModel):
    CertValidationFailure: Optional[str]
    CertValidationTimeout: Optional[str]
    ClientCertRequest: Optional[str]
    ClientCertificate: Optional[str]
    ExpiredServerCert: Optional[str]
    InvalidServerCert: Optional[str]
    Ports: Optional[str]
    ProxyAfterTcpHandshake: Optional[str]
    RevokedServerCert: Optional[str]
    SniServerCertCheck: Optional[str]
    Status: Optional[str]
    UnsupportedSsl: Optional[str]
    UnsupportedSslCipher: Optional[str]
    UnsupportedSslNegotiation: Optional[str]
    UntrustedServerCert: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SmtpsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SmtpsDefinition"]:
        if not json_data:
            return None
        return cls(
            CertValidationFailure=json_data.get("CertValidationFailure"),
            CertValidationTimeout=json_data.get("CertValidationTimeout"),
            ClientCertRequest=json_data.get("ClientCertRequest"),
            ClientCertificate=json_data.get("ClientCertificate"),
            ExpiredServerCert=json_data.get("ExpiredServerCert"),
            InvalidServerCert=json_data.get("InvalidServerCert"),
            Ports=json_data.get("Ports"),
            ProxyAfterTcpHandshake=json_data.get("ProxyAfterTcpHandshake"),
            RevokedServerCert=json_data.get("RevokedServerCert"),
            SniServerCertCheck=json_data.get("SniServerCertCheck"),
            Status=json_data.get("Status"),
            UnsupportedSsl=json_data.get("UnsupportedSsl"),
            UnsupportedSslCipher=json_data.get("UnsupportedSslCipher"),
            UnsupportedSslNegotiation=json_data.get("UnsupportedSslNegotiation"),
            UntrustedServerCert=json_data.get("UntrustedServerCert"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SmtpsDefinition = SmtpsDefinition


@dataclass
class SshDefinition(BaseModel):
    InspectAll: Optional[str]
    Ports: Optional[str]
    ProxyAfterTcpHandshake: Optional[str]
    SshAlgorithm: Optional[str]
    SshPolicyCheck: Optional[str]
    SshTunPolicyCheck: Optional[str]
    Status: Optional[str]
    UnsupportedVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SshDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SshDefinition"]:
        if not json_data:
            return None
        return cls(
            InspectAll=json_data.get("InspectAll"),
            Ports=json_data.get("Ports"),
            ProxyAfterTcpHandshake=json_data.get("ProxyAfterTcpHandshake"),
            SshAlgorithm=json_data.get("SshAlgorithm"),
            SshPolicyCheck=json_data.get("SshPolicyCheck"),
            SshTunPolicyCheck=json_data.get("SshTunPolicyCheck"),
            Status=json_data.get("Status"),
            UnsupportedVersion=json_data.get("UnsupportedVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SshDefinition = SshDefinition


@dataclass
class SslDefinition(BaseModel):
    CertValidationFailure: Optional[str]
    CertValidationTimeout: Optional[str]
    ClientCertRequest: Optional[str]
    ClientCertificate: Optional[str]
    ExpiredServerCert: Optional[str]
    InspectAll: Optional[str]
    InvalidServerCert: Optional[str]
    RevokedServerCert: Optional[str]
    SniServerCertCheck: Optional[str]
    UnsupportedSsl: Optional[str]
    UnsupportedSslCipher: Optional[str]
    UnsupportedSslNegotiation: Optional[str]
    UntrustedServerCert: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SslDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SslDefinition"]:
        if not json_data:
            return None
        return cls(
            CertValidationFailure=json_data.get("CertValidationFailure"),
            CertValidationTimeout=json_data.get("CertValidationTimeout"),
            ClientCertRequest=json_data.get("ClientCertRequest"),
            ClientCertificate=json_data.get("ClientCertificate"),
            ExpiredServerCert=json_data.get("ExpiredServerCert"),
            InspectAll=json_data.get("InspectAll"),
            InvalidServerCert=json_data.get("InvalidServerCert"),
            RevokedServerCert=json_data.get("RevokedServerCert"),
            SniServerCertCheck=json_data.get("SniServerCertCheck"),
            UnsupportedSsl=json_data.get("UnsupportedSsl"),
            UnsupportedSslCipher=json_data.get("UnsupportedSslCipher"),
            UnsupportedSslNegotiation=json_data.get("UnsupportedSslNegotiation"),
            UntrustedServerCert=json_data.get("UntrustedServerCert"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SslDefinition = SslDefinition


@dataclass
class SslExemptDefinition(BaseModel):
    Address: Optional[str]
    Address6: Optional[str]
    FortiguardCategory: Optional[float]
    Id: Optional[float]
    Regex: Optional[str]
    Type: Optional[str]
    WildcardFqdn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SslExemptDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SslExemptDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Address6=json_data.get("Address6"),
            FortiguardCategory=json_data.get("FortiguardCategory"),
            Id=json_data.get("Id"),
            Regex=json_data.get("Regex"),
            Type=json_data.get("Type"),
            WildcardFqdn=json_data.get("WildcardFqdn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SslExemptDefinition = SslExemptDefinition


@dataclass
class SslServerDefinition(BaseModel):
    FtpsClientCertRequest: Optional[str]
    FtpsClientCertificate: Optional[str]
    HttpsClientCertRequest: Optional[str]
    HttpsClientCertificate: Optional[str]
    Id: Optional[float]
    ImapsClientCertRequest: Optional[str]
    ImapsClientCertificate: Optional[str]
    Ip: Optional[str]
    Pop3sClientCertRequest: Optional[str]
    Pop3sClientCertificate: Optional[str]
    SmtpsClientCertRequest: Optional[str]
    SmtpsClientCertificate: Optional[str]
    SslOtherClientCertRequest: Optional[str]
    SslOtherClientCertificate: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SslServerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SslServerDefinition"]:
        if not json_data:
            return None
        return cls(
            FtpsClientCertRequest=json_data.get("FtpsClientCertRequest"),
            FtpsClientCertificate=json_data.get("FtpsClientCertificate"),
            HttpsClientCertRequest=json_data.get("HttpsClientCertRequest"),
            HttpsClientCertificate=json_data.get("HttpsClientCertificate"),
            Id=json_data.get("Id"),
            ImapsClientCertRequest=json_data.get("ImapsClientCertRequest"),
            ImapsClientCertificate=json_data.get("ImapsClientCertificate"),
            Ip=json_data.get("Ip"),
            Pop3sClientCertRequest=json_data.get("Pop3sClientCertRequest"),
            Pop3sClientCertificate=json_data.get("Pop3sClientCertificate"),
            SmtpsClientCertRequest=json_data.get("SmtpsClientCertRequest"),
            SmtpsClientCertificate=json_data.get("SmtpsClientCertificate"),
            SslOtherClientCertRequest=json_data.get("SslOtherClientCertRequest"),
            SslOtherClientCertificate=json_data.get("SslOtherClientCertificate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SslServerDefinition = SslServerDefinition


