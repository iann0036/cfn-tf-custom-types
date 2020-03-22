# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    AlertTimeout: Optional[str]
    AllowNonSsl: Optional[str]
    Authenticate: Optional[str]
    AuthenticateDepth: Optional[float]
    CaFile: Optional[str]
    CacheSize: Optional[float]
    CacheTimeout: Optional[float]
    Cert: Optional[str]
    CertExtensionIncludes: Optional[Sequence[str]]
    CertLifeSpan: Optional[float]
    CertLookupByIpaddrPort: Optional[str]
    Chain: Optional[str]
    Ciphers: Optional[str]
    ClientCertCa: Optional[str]
    CrlFile: Optional[str]
    DefaultsFrom: Optional[str]
    ForwardProxyBypassDefaultAction: Optional[str]
    FullPath: Optional[str]
    Generation: Optional[float]
    GenericAlert: Optional[str]
    HandshakeTimeout: Optional[str]
    Id: Optional[str]
    InheritCertKeychain: Optional[str]
    Key: Optional[str]
    ModSslMethods: Optional[str]
    Mode: Optional[str]
    Name: Optional[str]
    Partition: Optional[str]
    Passphrase: Optional[str]
    PeerCertMode: Optional[str]
    ProxyCaCert: Optional[str]
    ProxyCaKey: Optional[str]
    ProxyCaPassphrase: Optional[str]
    ProxySsl: Optional[str]
    ProxySslPassthrough: Optional[str]
    RenegotiatePeriod: Optional[str]
    RenegotiateSize: Optional[str]
    Renegotiation: Optional[str]
    RetainCertificate: Optional[str]
    SecureRenegotiation: Optional[str]
    ServerName: Optional[str]
    SessionMirroring: Optional[str]
    SessionTicket: Optional[str]
    SniDefault: Optional[str]
    SniRequire: Optional[str]
    SslForwardProxy: Optional[str]
    SslForwardProxyBypass: Optional[str]
    SslSignHash: Optional[str]
    StrictResume: Optional[str]
    TmOptions: Optional[Sequence[str]]
    UncleanShutdown: Optional[str]
    CertKeyChain: Optional[Sequence["_CertKeyChain"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AlertTimeout=json_data.get("AlertTimeout"),
            AllowNonSsl=json_data.get("AllowNonSsl"),
            Authenticate=json_data.get("Authenticate"),
            AuthenticateDepth=json_data.get("AuthenticateDepth"),
            CaFile=json_data.get("CaFile"),
            CacheSize=json_data.get("CacheSize"),
            CacheTimeout=json_data.get("CacheTimeout"),
            Cert=json_data.get("Cert"),
            CertExtensionIncludes=json_data.get("CertExtensionIncludes"),
            CertLifeSpan=json_data.get("CertLifeSpan"),
            CertLookupByIpaddrPort=json_data.get("CertLookupByIpaddrPort"),
            Chain=json_data.get("Chain"),
            Ciphers=json_data.get("Ciphers"),
            ClientCertCa=json_data.get("ClientCertCa"),
            CrlFile=json_data.get("CrlFile"),
            DefaultsFrom=json_data.get("DefaultsFrom"),
            ForwardProxyBypassDefaultAction=json_data.get("ForwardProxyBypassDefaultAction"),
            FullPath=json_data.get("FullPath"),
            Generation=json_data.get("Generation"),
            GenericAlert=json_data.get("GenericAlert"),
            HandshakeTimeout=json_data.get("HandshakeTimeout"),
            Id=json_data.get("Id"),
            InheritCertKeychain=json_data.get("InheritCertKeychain"),
            Key=json_data.get("Key"),
            ModSslMethods=json_data.get("ModSslMethods"),
            Mode=json_data.get("Mode"),
            Name=json_data.get("Name"),
            Partition=json_data.get("Partition"),
            Passphrase=json_data.get("Passphrase"),
            PeerCertMode=json_data.get("PeerCertMode"),
            ProxyCaCert=json_data.get("ProxyCaCert"),
            ProxyCaKey=json_data.get("ProxyCaKey"),
            ProxyCaPassphrase=json_data.get("ProxyCaPassphrase"),
            ProxySsl=json_data.get("ProxySsl"),
            ProxySslPassthrough=json_data.get("ProxySslPassthrough"),
            RenegotiatePeriod=json_data.get("RenegotiatePeriod"),
            RenegotiateSize=json_data.get("RenegotiateSize"),
            Renegotiation=json_data.get("Renegotiation"),
            RetainCertificate=json_data.get("RetainCertificate"),
            SecureRenegotiation=json_data.get("SecureRenegotiation"),
            ServerName=json_data.get("ServerName"),
            SessionMirroring=json_data.get("SessionMirroring"),
            SessionTicket=json_data.get("SessionTicket"),
            SniDefault=json_data.get("SniDefault"),
            SniRequire=json_data.get("SniRequire"),
            SslForwardProxy=json_data.get("SslForwardProxy"),
            SslForwardProxyBypass=json_data.get("SslForwardProxyBypass"),
            SslSignHash=json_data.get("SslSignHash"),
            StrictResume=json_data.get("StrictResume"),
            TmOptions=json_data.get("TmOptions"),
            UncleanShutdown=json_data.get("UncleanShutdown"),
            CertKeyChain=json_data.get("CertKeyChain"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CertKeyChain:
    Cert: Optional[str]
    Chain: Optional[str]
    Key: Optional[str]
    Name: Optional[str]
    Passphrase: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertKeyChain"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertKeyChain"]:
        if not json_data:
            return None
        return cls(
            Cert=json_data.get("Cert"),
            Chain=json_data.get("Chain"),
            Key=json_data.get("Key"),
            Name=json_data.get("Name"),
            Passphrase=json_data.get("Passphrase"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertKeyChain = CertKeyChain


