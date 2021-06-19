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
    ArpReply: Optional[str]
    Color: Optional[float]
    Comment: Optional[str]
    DynamicSortSubtable: Optional[str]
    Extip: Optional[str]
    Extport: Optional[str]
    Fosid: Optional[float]
    HttpCookieAge: Optional[float]
    HttpCookieDomain: Optional[str]
    HttpCookieDomainFromHost: Optional[str]
    HttpCookieGeneration: Optional[float]
    HttpCookiePath: Optional[str]
    HttpCookieShare: Optional[str]
    HttpIpHeader: Optional[str]
    HttpIpHeaderName: Optional[str]
    HttpMultiplex: Optional[str]
    HttpRedirect: Optional[str]
    HttpsCookieSecure: Optional[str]
    Id: Optional[str]
    LdbMethod: Optional[str]
    Mappedip: Optional[str]
    Mappedport: Optional[str]
    MaxEmbryonicConnections: Optional[float]
    Name: Optional[str]
    NatSourceVip: Optional[str]
    OutlookWebAccess: Optional[str]
    Persistence: Optional[str]
    Portforward: Optional[str]
    Protocol: Optional[str]
    ServerType: Optional[str]
    SslAlgorithm: Optional[str]
    SslCertificate: Optional[str]
    SslClientFallback: Optional[str]
    SslClientRekeyCount: Optional[float]
    SslClientRenegotiation: Optional[str]
    SslClientSessionStateMax: Optional[float]
    SslClientSessionStateTimeout: Optional[float]
    SslClientSessionStateType: Optional[str]
    SslDhBits: Optional[str]
    SslHpkp: Optional[str]
    SslHpkpAge: Optional[float]
    SslHpkpBackup: Optional[str]
    SslHpkpIncludeSubdomains: Optional[str]
    SslHpkpPrimary: Optional[str]
    SslHpkpReportUri: Optional[str]
    SslHsts: Optional[str]
    SslHstsAge: Optional[float]
    SslHstsIncludeSubdomains: Optional[str]
    SslHttpLocationConversion: Optional[str]
    SslHttpMatchHost: Optional[str]
    SslMaxVersion: Optional[str]
    SslMinVersion: Optional[str]
    SslMode: Optional[str]
    SslPfs: Optional[str]
    SslSendEmptyFrags: Optional[str]
    SslServerAlgorithm: Optional[str]
    SslServerMaxVersion: Optional[str]
    SslServerMinVersion: Optional[str]
    SslServerSessionStateMax: Optional[float]
    SslServerSessionStateTimeout: Optional[float]
    SslServerSessionStateType: Optional[str]
    Type: Optional[str]
    Uuid: Optional[str]
    Vdomparam: Optional[str]
    WeblogicServer: Optional[str]
    WebsphereServer: Optional[str]
    Monitor: Optional[Sequence["_MonitorDefinition"]]
    Realservers: Optional[Sequence["_RealserversDefinition"]]
    SrcFilter: Optional[Sequence["_SrcFilterDefinition"]]
    SslCipherSuites: Optional[Sequence["_SslCipherSuitesDefinition"]]
    SslServerCipherSuites: Optional[Sequence["_SslServerCipherSuitesDefinition"]]

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
            ArpReply=json_data.get("ArpReply"),
            Color=json_data.get("Color"),
            Comment=json_data.get("Comment"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Extip=json_data.get("Extip"),
            Extport=json_data.get("Extport"),
            Fosid=json_data.get("Fosid"),
            HttpCookieAge=json_data.get("HttpCookieAge"),
            HttpCookieDomain=json_data.get("HttpCookieDomain"),
            HttpCookieDomainFromHost=json_data.get("HttpCookieDomainFromHost"),
            HttpCookieGeneration=json_data.get("HttpCookieGeneration"),
            HttpCookiePath=json_data.get("HttpCookiePath"),
            HttpCookieShare=json_data.get("HttpCookieShare"),
            HttpIpHeader=json_data.get("HttpIpHeader"),
            HttpIpHeaderName=json_data.get("HttpIpHeaderName"),
            HttpMultiplex=json_data.get("HttpMultiplex"),
            HttpRedirect=json_data.get("HttpRedirect"),
            HttpsCookieSecure=json_data.get("HttpsCookieSecure"),
            Id=json_data.get("Id"),
            LdbMethod=json_data.get("LdbMethod"),
            Mappedip=json_data.get("Mappedip"),
            Mappedport=json_data.get("Mappedport"),
            MaxEmbryonicConnections=json_data.get("MaxEmbryonicConnections"),
            Name=json_data.get("Name"),
            NatSourceVip=json_data.get("NatSourceVip"),
            OutlookWebAccess=json_data.get("OutlookWebAccess"),
            Persistence=json_data.get("Persistence"),
            Portforward=json_data.get("Portforward"),
            Protocol=json_data.get("Protocol"),
            ServerType=json_data.get("ServerType"),
            SslAlgorithm=json_data.get("SslAlgorithm"),
            SslCertificate=json_data.get("SslCertificate"),
            SslClientFallback=json_data.get("SslClientFallback"),
            SslClientRekeyCount=json_data.get("SslClientRekeyCount"),
            SslClientRenegotiation=json_data.get("SslClientRenegotiation"),
            SslClientSessionStateMax=json_data.get("SslClientSessionStateMax"),
            SslClientSessionStateTimeout=json_data.get("SslClientSessionStateTimeout"),
            SslClientSessionStateType=json_data.get("SslClientSessionStateType"),
            SslDhBits=json_data.get("SslDhBits"),
            SslHpkp=json_data.get("SslHpkp"),
            SslHpkpAge=json_data.get("SslHpkpAge"),
            SslHpkpBackup=json_data.get("SslHpkpBackup"),
            SslHpkpIncludeSubdomains=json_data.get("SslHpkpIncludeSubdomains"),
            SslHpkpPrimary=json_data.get("SslHpkpPrimary"),
            SslHpkpReportUri=json_data.get("SslHpkpReportUri"),
            SslHsts=json_data.get("SslHsts"),
            SslHstsAge=json_data.get("SslHstsAge"),
            SslHstsIncludeSubdomains=json_data.get("SslHstsIncludeSubdomains"),
            SslHttpLocationConversion=json_data.get("SslHttpLocationConversion"),
            SslHttpMatchHost=json_data.get("SslHttpMatchHost"),
            SslMaxVersion=json_data.get("SslMaxVersion"),
            SslMinVersion=json_data.get("SslMinVersion"),
            SslMode=json_data.get("SslMode"),
            SslPfs=json_data.get("SslPfs"),
            SslSendEmptyFrags=json_data.get("SslSendEmptyFrags"),
            SslServerAlgorithm=json_data.get("SslServerAlgorithm"),
            SslServerMaxVersion=json_data.get("SslServerMaxVersion"),
            SslServerMinVersion=json_data.get("SslServerMinVersion"),
            SslServerSessionStateMax=json_data.get("SslServerSessionStateMax"),
            SslServerSessionStateTimeout=json_data.get("SslServerSessionStateTimeout"),
            SslServerSessionStateType=json_data.get("SslServerSessionStateType"),
            Type=json_data.get("Type"),
            Uuid=json_data.get("Uuid"),
            Vdomparam=json_data.get("Vdomparam"),
            WeblogicServer=json_data.get("WeblogicServer"),
            WebsphereServer=json_data.get("WebsphereServer"),
            Monitor=deserialize_list(json_data.get("Monitor"), MonitorDefinition),
            Realservers=deserialize_list(json_data.get("Realservers"), RealserversDefinition),
            SrcFilter=deserialize_list(json_data.get("SrcFilter"), SrcFilterDefinition),
            SslCipherSuites=deserialize_list(json_data.get("SslCipherSuites"), SslCipherSuitesDefinition),
            SslServerCipherSuites=deserialize_list(json_data.get("SslServerCipherSuites"), SslServerCipherSuitesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MonitorDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MonitorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MonitorDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MonitorDefinition = MonitorDefinition


@dataclass
class RealserversDefinition(BaseModel):
    ClientIp: Optional[str]
    Healthcheck: Optional[str]
    HolddownInterval: Optional[float]
    HttpHost: Optional[str]
    Id: Optional[float]
    Ip: Optional[str]
    MaxConnections: Optional[float]
    Monitor: Optional[str]
    Port: Optional[float]
    Status: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RealserversDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RealserversDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientIp=json_data.get("ClientIp"),
            Healthcheck=json_data.get("Healthcheck"),
            HolddownInterval=json_data.get("HolddownInterval"),
            HttpHost=json_data.get("HttpHost"),
            Id=json_data.get("Id"),
            Ip=json_data.get("Ip"),
            MaxConnections=json_data.get("MaxConnections"),
            Monitor=json_data.get("Monitor"),
            Port=json_data.get("Port"),
            Status=json_data.get("Status"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RealserversDefinition = RealserversDefinition


@dataclass
class SrcFilterDefinition(BaseModel):
    Range: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SrcFilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SrcFilterDefinition"]:
        if not json_data:
            return None
        return cls(
            Range=json_data.get("Range"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SrcFilterDefinition = SrcFilterDefinition


@dataclass
class SslCipherSuitesDefinition(BaseModel):
    Cipher: Optional[str]
    Priority: Optional[float]
    Versions: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SslCipherSuitesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SslCipherSuitesDefinition"]:
        if not json_data:
            return None
        return cls(
            Cipher=json_data.get("Cipher"),
            Priority=json_data.get("Priority"),
            Versions=json_data.get("Versions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SslCipherSuitesDefinition = SslCipherSuitesDefinition


@dataclass
class SslServerCipherSuitesDefinition(BaseModel):
    Cipher: Optional[str]
    Priority: Optional[float]
    Versions: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SslServerCipherSuitesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SslServerCipherSuitesDefinition"]:
        if not json_data:
            return None
        return cls(
            Cipher=json_data.get("Cipher"),
            Priority=json_data.get("Priority"),
            Versions=json_data.get("Versions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SslServerCipherSuitesDefinition = SslServerCipherSuitesDefinition


