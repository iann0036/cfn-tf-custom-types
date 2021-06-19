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
    AlertType: Optional[str]
    Cert: Optional[str]
    CertSharedStr: Optional[str]
    CipherTemplate: Optional[str]
    CloseNotify: Optional[float]
    Dgversion: Optional[float]
    DhType: Optional[str]
    EnableTlsAlertLogging: Optional[float]
    Encrypted: Optional[str]
    ForwardProxyEnable: Optional[float]
    HandshakeLoggingEnable: Optional[float]
    Id: Optional[str]
    Key: Optional[str]
    KeySharedEncrypted: Optional[str]
    KeySharedPassphrase: Optional[str]
    KeySharedStr: Optional[str]
    Name: Optional[str]
    OcspStapling: Optional[float]
    Passphrase: Optional[str]
    RenegotiationDisable: Optional[float]
    SessionCacheSize: Optional[float]
    SessionCacheTimeout: Optional[float]
    SessionTicketEnable: Optional[float]
    SharedPartitionCipherTemplate: Optional[float]
    SsliLogging: Optional[float]
    Sslilogging: Optional[str]
    TemplateCipherShared: Optional[str]
    UseClientSni: Optional[float]
    UserTag: Optional[str]
    Uuid: Optional[str]
    Version: Optional[float]
    CaCerts: Optional[Sequence["_CaCertsDefinition"]]
    CipherWithoutPrioList: Optional[Sequence["_CipherWithoutPrioListDefinition"]]
    CrlCerts: Optional[Sequence["_CrlCertsDefinition"]]
    EcList: Optional[Sequence["_EcListDefinition"]]
    ServerCertificateError: Optional[Sequence["_ServerCertificateErrorDefinition"]]

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
            AlertType=json_data.get("AlertType"),
            Cert=json_data.get("Cert"),
            CertSharedStr=json_data.get("CertSharedStr"),
            CipherTemplate=json_data.get("CipherTemplate"),
            CloseNotify=json_data.get("CloseNotify"),
            Dgversion=json_data.get("Dgversion"),
            DhType=json_data.get("DhType"),
            EnableTlsAlertLogging=json_data.get("EnableTlsAlertLogging"),
            Encrypted=json_data.get("Encrypted"),
            ForwardProxyEnable=json_data.get("ForwardProxyEnable"),
            HandshakeLoggingEnable=json_data.get("HandshakeLoggingEnable"),
            Id=json_data.get("Id"),
            Key=json_data.get("Key"),
            KeySharedEncrypted=json_data.get("KeySharedEncrypted"),
            KeySharedPassphrase=json_data.get("KeySharedPassphrase"),
            KeySharedStr=json_data.get("KeySharedStr"),
            Name=json_data.get("Name"),
            OcspStapling=json_data.get("OcspStapling"),
            Passphrase=json_data.get("Passphrase"),
            RenegotiationDisable=json_data.get("RenegotiationDisable"),
            SessionCacheSize=json_data.get("SessionCacheSize"),
            SessionCacheTimeout=json_data.get("SessionCacheTimeout"),
            SessionTicketEnable=json_data.get("SessionTicketEnable"),
            SharedPartitionCipherTemplate=json_data.get("SharedPartitionCipherTemplate"),
            SsliLogging=json_data.get("SsliLogging"),
            Sslilogging=json_data.get("Sslilogging"),
            TemplateCipherShared=json_data.get("TemplateCipherShared"),
            UseClientSni=json_data.get("UseClientSni"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            Version=json_data.get("Version"),
            CaCerts=deserialize_list(json_data.get("CaCerts"), CaCertsDefinition),
            CipherWithoutPrioList=deserialize_list(json_data.get("CipherWithoutPrioList"), CipherWithoutPrioListDefinition),
            CrlCerts=deserialize_list(json_data.get("CrlCerts"), CrlCertsDefinition),
            EcList=deserialize_list(json_data.get("EcList"), EcListDefinition),
            ServerCertificateError=deserialize_list(json_data.get("ServerCertificateError"), ServerCertificateErrorDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CaCertsDefinition(BaseModel):
    CaCert: Optional[str]
    CaCertPartitionShared: Optional[float]
    ServerOcspSg: Optional[str]
    ServerOcspSrvr: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CaCertsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CaCertsDefinition"]:
        if not json_data:
            return None
        return cls(
            CaCert=json_data.get("CaCert"),
            CaCertPartitionShared=json_data.get("CaCertPartitionShared"),
            ServerOcspSg=json_data.get("ServerOcspSg"),
            ServerOcspSrvr=json_data.get("ServerOcspSrvr"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CaCertsDefinition = CaCertsDefinition


@dataclass
class CipherWithoutPrioListDefinition(BaseModel):
    CipherWoPrio: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CipherWithoutPrioListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CipherWithoutPrioListDefinition"]:
        if not json_data:
            return None
        return cls(
            CipherWoPrio=json_data.get("CipherWoPrio"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CipherWithoutPrioListDefinition = CipherWithoutPrioListDefinition


@dataclass
class CrlCertsDefinition(BaseModel):
    Crl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CrlCertsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CrlCertsDefinition"]:
        if not json_data:
            return None
        return cls(
            Crl=json_data.get("Crl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CrlCertsDefinition = CrlCertsDefinition


@dataclass
class EcListDefinition(BaseModel):
    Ec: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EcListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EcListDefinition"]:
        if not json_data:
            return None
        return cls(
            Ec=json_data.get("Ec"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EcListDefinition = EcListDefinition


@dataclass
class ServerCertificateErrorDefinition(BaseModel):
    ErrorType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerCertificateErrorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerCertificateErrorDefinition"]:
        if not json_data:
            return None
        return cls(
            ErrorType=json_data.get("ErrorType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerCertificateErrorDefinition = ServerCertificateErrorDefinition


