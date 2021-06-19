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
    Comment: Optional[str]
    FeatureSet: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    OversizeLog: Optional[str]
    ReplacemsgGroup: Optional[str]
    RpcOverHttp: Optional[str]
    SwitchingProtocolsLog: Optional[str]
    Vdomparam: Optional[str]
    Cifs: Optional[Sequence["_CifsDefinition"]]
    Dns: Optional[Sequence["_DnsDefinition"]]
    Ftp: Optional[Sequence["_FtpDefinition"]]
    Http: Optional[Sequence["_HttpDefinition"]]
    Imap: Optional[Sequence["_ImapDefinition"]]
    MailSignature: Optional[Sequence["_MailSignatureDefinition"]]
    Mapi: Optional[Sequence["_MapiDefinition"]]
    Nntp: Optional[Sequence["_NntpDefinition"]]
    Pop3: Optional[Sequence["_Pop3Definition"]]
    Smtp: Optional[Sequence["_SmtpDefinition"]]
    Ssh: Optional[Sequence["_SshDefinition"]]

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
            Comment=json_data.get("Comment"),
            FeatureSet=json_data.get("FeatureSet"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            OversizeLog=json_data.get("OversizeLog"),
            ReplacemsgGroup=json_data.get("ReplacemsgGroup"),
            RpcOverHttp=json_data.get("RpcOverHttp"),
            SwitchingProtocolsLog=json_data.get("SwitchingProtocolsLog"),
            Vdomparam=json_data.get("Vdomparam"),
            Cifs=deserialize_list(json_data.get("Cifs"), CifsDefinition),
            Dns=deserialize_list(json_data.get("Dns"), DnsDefinition),
            Ftp=deserialize_list(json_data.get("Ftp"), FtpDefinition),
            Http=deserialize_list(json_data.get("Http"), HttpDefinition),
            Imap=deserialize_list(json_data.get("Imap"), ImapDefinition),
            MailSignature=deserialize_list(json_data.get("MailSignature"), MailSignatureDefinition),
            Mapi=deserialize_list(json_data.get("Mapi"), MapiDefinition),
            Nntp=deserialize_list(json_data.get("Nntp"), NntpDefinition),
            Pop3=deserialize_list(json_data.get("Pop3"), Pop3Definition),
            Smtp=deserialize_list(json_data.get("Smtp"), SmtpDefinition),
            Ssh=deserialize_list(json_data.get("Ssh"), SshDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CifsDefinition(BaseModel):
    DomainController: Optional[str]
    Options: Optional[str]
    OversizeLimit: Optional[float]
    Ports: Optional[float]
    ScanBzip2: Optional[str]
    ServerCredentialType: Optional[str]
    Status: Optional[str]
    TcpWindowMaximum: Optional[float]
    TcpWindowMinimum: Optional[float]
    TcpWindowSize: Optional[float]
    TcpWindowType: Optional[str]
    UncompressedNestLimit: Optional[float]
    UncompressedOversizeLimit: Optional[float]
    ServerKeytab: Optional[Sequence["_ServerKeytabDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CifsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CifsDefinition"]:
        if not json_data:
            return None
        return cls(
            DomainController=json_data.get("DomainController"),
            Options=json_data.get("Options"),
            OversizeLimit=json_data.get("OversizeLimit"),
            Ports=json_data.get("Ports"),
            ScanBzip2=json_data.get("ScanBzip2"),
            ServerCredentialType=json_data.get("ServerCredentialType"),
            Status=json_data.get("Status"),
            TcpWindowMaximum=json_data.get("TcpWindowMaximum"),
            TcpWindowMinimum=json_data.get("TcpWindowMinimum"),
            TcpWindowSize=json_data.get("TcpWindowSize"),
            TcpWindowType=json_data.get("TcpWindowType"),
            UncompressedNestLimit=json_data.get("UncompressedNestLimit"),
            UncompressedOversizeLimit=json_data.get("UncompressedOversizeLimit"),
            ServerKeytab=deserialize_list(json_data.get("ServerKeytab"), ServerKeytabDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CifsDefinition = CifsDefinition


@dataclass
class ServerKeytabDefinition(BaseModel):
    Keytab: Optional[str]
    Principal: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerKeytabDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerKeytabDefinition"]:
        if not json_data:
            return None
        return cls(
            Keytab=json_data.get("Keytab"),
            Principal=json_data.get("Principal"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerKeytabDefinition = ServerKeytabDefinition


@dataclass
class DnsDefinition(BaseModel):
    Ports: Optional[float]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DnsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsDefinition"]:
        if not json_data:
            return None
        return cls(
            Ports=json_data.get("Ports"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsDefinition = DnsDefinition


@dataclass
class FtpDefinition(BaseModel):
    ComfortAmount: Optional[float]
    ComfortInterval: Optional[float]
    InspectAll: Optional[str]
    Options: Optional[str]
    OversizeLimit: Optional[float]
    Ports: Optional[float]
    ScanBzip2: Optional[str]
    SslOffloaded: Optional[str]
    Status: Optional[str]
    StreamBasedUncompressedLimit: Optional[float]
    TcpWindowMaximum: Optional[float]
    TcpWindowMinimum: Optional[float]
    TcpWindowSize: Optional[float]
    TcpWindowType: Optional[str]
    UncompressedNestLimit: Optional[float]
    UncompressedOversizeLimit: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_FtpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FtpDefinition"]:
        if not json_data:
            return None
        return cls(
            ComfortAmount=json_data.get("ComfortAmount"),
            ComfortInterval=json_data.get("ComfortInterval"),
            InspectAll=json_data.get("InspectAll"),
            Options=json_data.get("Options"),
            OversizeLimit=json_data.get("OversizeLimit"),
            Ports=json_data.get("Ports"),
            ScanBzip2=json_data.get("ScanBzip2"),
            SslOffloaded=json_data.get("SslOffloaded"),
            Status=json_data.get("Status"),
            StreamBasedUncompressedLimit=json_data.get("StreamBasedUncompressedLimit"),
            TcpWindowMaximum=json_data.get("TcpWindowMaximum"),
            TcpWindowMinimum=json_data.get("TcpWindowMinimum"),
            TcpWindowSize=json_data.get("TcpWindowSize"),
            TcpWindowType=json_data.get("TcpWindowType"),
            UncompressedNestLimit=json_data.get("UncompressedNestLimit"),
            UncompressedOversizeLimit=json_data.get("UncompressedOversizeLimit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FtpDefinition = FtpDefinition


@dataclass
class HttpDefinition(BaseModel):
    BlockPageStatusCode: Optional[float]
    ComfortAmount: Optional[float]
    ComfortInterval: Optional[float]
    FortinetBar: Optional[str]
    FortinetBarPort: Optional[float]
    HttpPolicy: Optional[str]
    InspectAll: Optional[str]
    Options: Optional[str]
    OversizeLimit: Optional[float]
    Ports: Optional[float]
    PostLang: Optional[str]
    ProxyAfterTcpHandshake: Optional[str]
    RangeBlock: Optional[str]
    RetryCount: Optional[float]
    ScanBzip2: Optional[str]
    SslOffloaded: Optional[str]
    Status: Optional[str]
    StreamBasedUncompressedLimit: Optional[float]
    StreamingContentBypass: Optional[str]
    StripXForwardedFor: Optional[str]
    SwitchingProtocols: Optional[str]
    TcpWindowMaximum: Optional[float]
    TcpWindowMinimum: Optional[float]
    TcpWindowSize: Optional[float]
    TcpWindowType: Optional[str]
    TunnelNonHttp: Optional[str]
    UncompressedNestLimit: Optional[float]
    UncompressedOversizeLimit: Optional[float]
    UnknownHttpVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpDefinition"]:
        if not json_data:
            return None
        return cls(
            BlockPageStatusCode=json_data.get("BlockPageStatusCode"),
            ComfortAmount=json_data.get("ComfortAmount"),
            ComfortInterval=json_data.get("ComfortInterval"),
            FortinetBar=json_data.get("FortinetBar"),
            FortinetBarPort=json_data.get("FortinetBarPort"),
            HttpPolicy=json_data.get("HttpPolicy"),
            InspectAll=json_data.get("InspectAll"),
            Options=json_data.get("Options"),
            OversizeLimit=json_data.get("OversizeLimit"),
            Ports=json_data.get("Ports"),
            PostLang=json_data.get("PostLang"),
            ProxyAfterTcpHandshake=json_data.get("ProxyAfterTcpHandshake"),
            RangeBlock=json_data.get("RangeBlock"),
            RetryCount=json_data.get("RetryCount"),
            ScanBzip2=json_data.get("ScanBzip2"),
            SslOffloaded=json_data.get("SslOffloaded"),
            Status=json_data.get("Status"),
            StreamBasedUncompressedLimit=json_data.get("StreamBasedUncompressedLimit"),
            StreamingContentBypass=json_data.get("StreamingContentBypass"),
            StripXForwardedFor=json_data.get("StripXForwardedFor"),
            SwitchingProtocols=json_data.get("SwitchingProtocols"),
            TcpWindowMaximum=json_data.get("TcpWindowMaximum"),
            TcpWindowMinimum=json_data.get("TcpWindowMinimum"),
            TcpWindowSize=json_data.get("TcpWindowSize"),
            TcpWindowType=json_data.get("TcpWindowType"),
            TunnelNonHttp=json_data.get("TunnelNonHttp"),
            UncompressedNestLimit=json_data.get("UncompressedNestLimit"),
            UncompressedOversizeLimit=json_data.get("UncompressedOversizeLimit"),
            UnknownHttpVersion=json_data.get("UnknownHttpVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpDefinition = HttpDefinition


@dataclass
class ImapDefinition(BaseModel):
    InspectAll: Optional[str]
    Options: Optional[str]
    OversizeLimit: Optional[float]
    Ports: Optional[float]
    ProxyAfterTcpHandshake: Optional[str]
    ScanBzip2: Optional[str]
    SslOffloaded: Optional[str]
    Status: Optional[str]
    UncompressedNestLimit: Optional[float]
    UncompressedOversizeLimit: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ImapDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImapDefinition"]:
        if not json_data:
            return None
        return cls(
            InspectAll=json_data.get("InspectAll"),
            Options=json_data.get("Options"),
            OversizeLimit=json_data.get("OversizeLimit"),
            Ports=json_data.get("Ports"),
            ProxyAfterTcpHandshake=json_data.get("ProxyAfterTcpHandshake"),
            ScanBzip2=json_data.get("ScanBzip2"),
            SslOffloaded=json_data.get("SslOffloaded"),
            Status=json_data.get("Status"),
            UncompressedNestLimit=json_data.get("UncompressedNestLimit"),
            UncompressedOversizeLimit=json_data.get("UncompressedOversizeLimit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImapDefinition = ImapDefinition


@dataclass
class MailSignatureDefinition(BaseModel):
    Signature: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MailSignatureDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MailSignatureDefinition"]:
        if not json_data:
            return None
        return cls(
            Signature=json_data.get("Signature"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MailSignatureDefinition = MailSignatureDefinition


@dataclass
class MapiDefinition(BaseModel):
    Options: Optional[str]
    OversizeLimit: Optional[float]
    Ports: Optional[float]
    ScanBzip2: Optional[str]
    Status: Optional[str]
    UncompressedNestLimit: Optional[float]
    UncompressedOversizeLimit: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MapiDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MapiDefinition"]:
        if not json_data:
            return None
        return cls(
            Options=json_data.get("Options"),
            OversizeLimit=json_data.get("OversizeLimit"),
            Ports=json_data.get("Ports"),
            ScanBzip2=json_data.get("ScanBzip2"),
            Status=json_data.get("Status"),
            UncompressedNestLimit=json_data.get("UncompressedNestLimit"),
            UncompressedOversizeLimit=json_data.get("UncompressedOversizeLimit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MapiDefinition = MapiDefinition


@dataclass
class NntpDefinition(BaseModel):
    InspectAll: Optional[str]
    Options: Optional[str]
    OversizeLimit: Optional[float]
    Ports: Optional[float]
    ProxyAfterTcpHandshake: Optional[str]
    ScanBzip2: Optional[str]
    Status: Optional[str]
    UncompressedNestLimit: Optional[float]
    UncompressedOversizeLimit: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NntpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NntpDefinition"]:
        if not json_data:
            return None
        return cls(
            InspectAll=json_data.get("InspectAll"),
            Options=json_data.get("Options"),
            OversizeLimit=json_data.get("OversizeLimit"),
            Ports=json_data.get("Ports"),
            ProxyAfterTcpHandshake=json_data.get("ProxyAfterTcpHandshake"),
            ScanBzip2=json_data.get("ScanBzip2"),
            Status=json_data.get("Status"),
            UncompressedNestLimit=json_data.get("UncompressedNestLimit"),
            UncompressedOversizeLimit=json_data.get("UncompressedOversizeLimit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NntpDefinition = NntpDefinition


@dataclass
class Pop3Definition(BaseModel):
    InspectAll: Optional[str]
    Options: Optional[str]
    OversizeLimit: Optional[float]
    Ports: Optional[float]
    ProxyAfterTcpHandshake: Optional[str]
    ScanBzip2: Optional[str]
    SslOffloaded: Optional[str]
    Status: Optional[str]
    UncompressedNestLimit: Optional[float]
    UncompressedOversizeLimit: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Pop3Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Pop3Definition"]:
        if not json_data:
            return None
        return cls(
            InspectAll=json_data.get("InspectAll"),
            Options=json_data.get("Options"),
            OversizeLimit=json_data.get("OversizeLimit"),
            Ports=json_data.get("Ports"),
            ProxyAfterTcpHandshake=json_data.get("ProxyAfterTcpHandshake"),
            ScanBzip2=json_data.get("ScanBzip2"),
            SslOffloaded=json_data.get("SslOffloaded"),
            Status=json_data.get("Status"),
            UncompressedNestLimit=json_data.get("UncompressedNestLimit"),
            UncompressedOversizeLimit=json_data.get("UncompressedOversizeLimit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Pop3Definition = Pop3Definition


@dataclass
class SmtpDefinition(BaseModel):
    InspectAll: Optional[str]
    Options: Optional[str]
    OversizeLimit: Optional[float]
    Ports: Optional[float]
    ProxyAfterTcpHandshake: Optional[str]
    ScanBzip2: Optional[str]
    ServerBusy: Optional[str]
    SslOffloaded: Optional[str]
    Status: Optional[str]
    UncompressedNestLimit: Optional[float]
    UncompressedOversizeLimit: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SmtpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SmtpDefinition"]:
        if not json_data:
            return None
        return cls(
            InspectAll=json_data.get("InspectAll"),
            Options=json_data.get("Options"),
            OversizeLimit=json_data.get("OversizeLimit"),
            Ports=json_data.get("Ports"),
            ProxyAfterTcpHandshake=json_data.get("ProxyAfterTcpHandshake"),
            ScanBzip2=json_data.get("ScanBzip2"),
            ServerBusy=json_data.get("ServerBusy"),
            SslOffloaded=json_data.get("SslOffloaded"),
            Status=json_data.get("Status"),
            UncompressedNestLimit=json_data.get("UncompressedNestLimit"),
            UncompressedOversizeLimit=json_data.get("UncompressedOversizeLimit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SmtpDefinition = SmtpDefinition


@dataclass
class SshDefinition(BaseModel):
    ComfortAmount: Optional[float]
    ComfortInterval: Optional[float]
    Options: Optional[str]
    OversizeLimit: Optional[float]
    ScanBzip2: Optional[str]
    SslOffloaded: Optional[str]
    StreamBasedUncompressedLimit: Optional[float]
    TcpWindowMaximum: Optional[float]
    TcpWindowMinimum: Optional[float]
    TcpWindowSize: Optional[float]
    TcpWindowType: Optional[str]
    UncompressedNestLimit: Optional[float]
    UncompressedOversizeLimit: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SshDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SshDefinition"]:
        if not json_data:
            return None
        return cls(
            ComfortAmount=json_data.get("ComfortAmount"),
            ComfortInterval=json_data.get("ComfortInterval"),
            Options=json_data.get("Options"),
            OversizeLimit=json_data.get("OversizeLimit"),
            ScanBzip2=json_data.get("ScanBzip2"),
            SslOffloaded=json_data.get("SslOffloaded"),
            StreamBasedUncompressedLimit=json_data.get("StreamBasedUncompressedLimit"),
            TcpWindowMaximum=json_data.get("TcpWindowMaximum"),
            TcpWindowMinimum=json_data.get("TcpWindowMinimum"),
            TcpWindowSize=json_data.get("TcpWindowSize"),
            TcpWindowType=json_data.get("TcpWindowType"),
            UncompressedNestLimit=json_data.get("UncompressedNestLimit"),
            UncompressedOversizeLimit=json_data.get("UncompressedOversizeLimit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SshDefinition = SshDefinition


