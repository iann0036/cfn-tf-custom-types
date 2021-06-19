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
    AuthGroup: Optional[str]
    Comments: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Transparent: Optional[str]
    Vdomparam: Optional[str]
    Cifs: Optional[Sequence["_CifsDefinition"]]
    Ftp: Optional[Sequence["_FtpDefinition"]]
    Http: Optional[Sequence["_HttpDefinition"]]
    Mapi: Optional[Sequence["_MapiDefinition"]]
    Tcp: Optional[Sequence["_TcpDefinition"]]

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
            AuthGroup=json_data.get("AuthGroup"),
            Comments=json_data.get("Comments"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Transparent=json_data.get("Transparent"),
            Vdomparam=json_data.get("Vdomparam"),
            Cifs=deserialize_list(json_data.get("Cifs"), CifsDefinition),
            Ftp=deserialize_list(json_data.get("Ftp"), FtpDefinition),
            Http=deserialize_list(json_data.get("Http"), HttpDefinition),
            Mapi=deserialize_list(json_data.get("Mapi"), MapiDefinition),
            Tcp=deserialize_list(json_data.get("Tcp"), TcpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CifsDefinition(BaseModel):
    ByteCaching: Optional[str]
    LogTraffic: Optional[str]
    Port: Optional[float]
    PreferChunking: Optional[str]
    ProtocolOpt: Optional[str]
    SecureTunnel: Optional[str]
    Status: Optional[str]
    TunnelSharing: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CifsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CifsDefinition"]:
        if not json_data:
            return None
        return cls(
            ByteCaching=json_data.get("ByteCaching"),
            LogTraffic=json_data.get("LogTraffic"),
            Port=json_data.get("Port"),
            PreferChunking=json_data.get("PreferChunking"),
            ProtocolOpt=json_data.get("ProtocolOpt"),
            SecureTunnel=json_data.get("SecureTunnel"),
            Status=json_data.get("Status"),
            TunnelSharing=json_data.get("TunnelSharing"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CifsDefinition = CifsDefinition


@dataclass
class FtpDefinition(BaseModel):
    ByteCaching: Optional[str]
    LogTraffic: Optional[str]
    Port: Optional[float]
    PreferChunking: Optional[str]
    ProtocolOpt: Optional[str]
    SecureTunnel: Optional[str]
    Ssl: Optional[str]
    Status: Optional[str]
    TunnelSharing: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FtpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FtpDefinition"]:
        if not json_data:
            return None
        return cls(
            ByteCaching=json_data.get("ByteCaching"),
            LogTraffic=json_data.get("LogTraffic"),
            Port=json_data.get("Port"),
            PreferChunking=json_data.get("PreferChunking"),
            ProtocolOpt=json_data.get("ProtocolOpt"),
            SecureTunnel=json_data.get("SecureTunnel"),
            Ssl=json_data.get("Ssl"),
            Status=json_data.get("Status"),
            TunnelSharing=json_data.get("TunnelSharing"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FtpDefinition = FtpDefinition


@dataclass
class HttpDefinition(BaseModel):
    ByteCaching: Optional[str]
    LogTraffic: Optional[str]
    Port: Optional[float]
    PreferChunking: Optional[str]
    ProtocolOpt: Optional[str]
    SecureTunnel: Optional[str]
    Ssl: Optional[str]
    SslPort: Optional[float]
    Status: Optional[str]
    TunnelNonHttp: Optional[str]
    TunnelSharing: Optional[str]
    UnknownHttpVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpDefinition"]:
        if not json_data:
            return None
        return cls(
            ByteCaching=json_data.get("ByteCaching"),
            LogTraffic=json_data.get("LogTraffic"),
            Port=json_data.get("Port"),
            PreferChunking=json_data.get("PreferChunking"),
            ProtocolOpt=json_data.get("ProtocolOpt"),
            SecureTunnel=json_data.get("SecureTunnel"),
            Ssl=json_data.get("Ssl"),
            SslPort=json_data.get("SslPort"),
            Status=json_data.get("Status"),
            TunnelNonHttp=json_data.get("TunnelNonHttp"),
            TunnelSharing=json_data.get("TunnelSharing"),
            UnknownHttpVersion=json_data.get("UnknownHttpVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpDefinition = HttpDefinition


@dataclass
class MapiDefinition(BaseModel):
    ByteCaching: Optional[str]
    LogTraffic: Optional[str]
    Port: Optional[float]
    SecureTunnel: Optional[str]
    Status: Optional[str]
    TunnelSharing: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MapiDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MapiDefinition"]:
        if not json_data:
            return None
        return cls(
            ByteCaching=json_data.get("ByteCaching"),
            LogTraffic=json_data.get("LogTraffic"),
            Port=json_data.get("Port"),
            SecureTunnel=json_data.get("SecureTunnel"),
            Status=json_data.get("Status"),
            TunnelSharing=json_data.get("TunnelSharing"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MapiDefinition = MapiDefinition


@dataclass
class TcpDefinition(BaseModel):
    ByteCaching: Optional[str]
    ByteCachingOpt: Optional[str]
    LogTraffic: Optional[str]
    Port: Optional[str]
    SecureTunnel: Optional[str]
    Ssl: Optional[str]
    SslPort: Optional[float]
    Status: Optional[str]
    TunnelSharing: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TcpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TcpDefinition"]:
        if not json_data:
            return None
        return cls(
            ByteCaching=json_data.get("ByteCaching"),
            ByteCachingOpt=json_data.get("ByteCachingOpt"),
            LogTraffic=json_data.get("LogTraffic"),
            Port=json_data.get("Port"),
            SecureTunnel=json_data.get("SecureTunnel"),
            Ssl=json_data.get("Ssl"),
            SslPort=json_data.get("SslPort"),
            Status=json_data.get("Status"),
            TunnelSharing=json_data.get("TunnelSharing"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TcpDefinition = TcpDefinition


