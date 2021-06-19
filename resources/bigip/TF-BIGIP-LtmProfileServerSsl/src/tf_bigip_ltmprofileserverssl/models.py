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
    AlertTimeout: Optional[str]
    Authenticate: Optional[str]
    AuthenticateDepth: Optional[float]
    C3dCaCert: Optional[str]
    C3dCaKey: Optional[str]
    C3dCaPassphrase: Optional[str]
    C3dCertExtensionCustomOids: Optional[Sequence[str]]
    C3dCertExtensionIncludes: Optional[Sequence[str]]
    C3dCertLifespan: Optional[float]
    C3dCertificateExtensions: Optional[str]
    CaFile: Optional[str]
    CacheSize: Optional[float]
    CacheTimeout: Optional[float]
    Cert: Optional[str]
    Chain: Optional[str]
    Ciphers: Optional[str]
    DefaultsFrom: Optional[str]
    ExpireCertResponseControl: Optional[str]
    FullPath: Optional[str]
    Generation: Optional[float]
    GenericAlert: Optional[str]
    HandshakeTimeout: Optional[str]
    Id: Optional[str]
    Key: Optional[str]
    ModSslMethods: Optional[str]
    Mode: Optional[str]
    Name: Optional[str]
    Partition: Optional[str]
    Passphrase: Optional[str]
    PeerCertMode: Optional[str]
    ProxyCaCert: Optional[str]
    ProxyCaKey: Optional[str]
    ProxySsl: Optional[str]
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
    SslC3d: Optional[str]
    SslForwardProxy: Optional[str]
    SslForwardProxyBypass: Optional[str]
    SslSignHash: Optional[str]
    StrictResume: Optional[str]
    TmOptions: Optional[Sequence[str]]
    UncleanShutdown: Optional[str]
    UntrustedCertResponseControl: Optional[str]

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
            AlertTimeout=json_data.get("AlertTimeout"),
            Authenticate=json_data.get("Authenticate"),
            AuthenticateDepth=json_data.get("AuthenticateDepth"),
            C3dCaCert=json_data.get("C3dCaCert"),
            C3dCaKey=json_data.get("C3dCaKey"),
            C3dCaPassphrase=json_data.get("C3dCaPassphrase"),
            C3dCertExtensionCustomOids=json_data.get("C3dCertExtensionCustomOids"),
            C3dCertExtensionIncludes=json_data.get("C3dCertExtensionIncludes"),
            C3dCertLifespan=json_data.get("C3dCertLifespan"),
            C3dCertificateExtensions=json_data.get("C3dCertificateExtensions"),
            CaFile=json_data.get("CaFile"),
            CacheSize=json_data.get("CacheSize"),
            CacheTimeout=json_data.get("CacheTimeout"),
            Cert=json_data.get("Cert"),
            Chain=json_data.get("Chain"),
            Ciphers=json_data.get("Ciphers"),
            DefaultsFrom=json_data.get("DefaultsFrom"),
            ExpireCertResponseControl=json_data.get("ExpireCertResponseControl"),
            FullPath=json_data.get("FullPath"),
            Generation=json_data.get("Generation"),
            GenericAlert=json_data.get("GenericAlert"),
            HandshakeTimeout=json_data.get("HandshakeTimeout"),
            Id=json_data.get("Id"),
            Key=json_data.get("Key"),
            ModSslMethods=json_data.get("ModSslMethods"),
            Mode=json_data.get("Mode"),
            Name=json_data.get("Name"),
            Partition=json_data.get("Partition"),
            Passphrase=json_data.get("Passphrase"),
            PeerCertMode=json_data.get("PeerCertMode"),
            ProxyCaCert=json_data.get("ProxyCaCert"),
            ProxyCaKey=json_data.get("ProxyCaKey"),
            ProxySsl=json_data.get("ProxySsl"),
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
            SslC3d=json_data.get("SslC3d"),
            SslForwardProxy=json_data.get("SslForwardProxy"),
            SslForwardProxyBypass=json_data.get("SslForwardProxyBypass"),
            SslSignHash=json_data.get("SslSignHash"),
            StrictResume=json_data.get("StrictResume"),
            TmOptions=json_data.get("TmOptions"),
            UncleanShutdown=json_data.get("UncleanShutdown"),
            UntrustedCertResponseControl=json_data.get("UntrustedCertResponseControl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


