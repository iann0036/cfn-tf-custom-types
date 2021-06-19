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
    AllowDuplicateMonitors: Optional[bool]
    Description: Optional[str]
    DisableQuickstart: Optional[bool]
    FailedChecks: Optional[float]
    Id: Optional[str]
    IsFederated: Optional[bool]
    MonitorPort: Optional[float]
    Name: Optional[str]
    ReceiveTimeout: Optional[float]
    SendInterval: Optional[float]
    SuccessfulChecks: Optional[float]
    TenantRef: Optional[str]
    Type: Optional[str]
    Uuid: Optional[str]
    Authentication: Optional[Sequence["_AuthenticationDefinition"]]
    DnsMonitor: Optional[Sequence["_DnsMonitorDefinition"]]
    ExternalMonitor: Optional[Sequence["_ExternalMonitorDefinition"]]
    HttpMonitor: Optional[Sequence["_HttpMonitorDefinition"]]
    HttpsMonitor: Optional[Sequence["_HttpsMonitorDefinition"]]
    ImapMonitor: Optional[Sequence["_ImapMonitorDefinition"]]
    ImapsMonitor: Optional[Sequence["_ImapsMonitorDefinition"]]
    Markers: Optional[Sequence["_MarkersDefinition"]]
    Pop3Monitor: Optional[Sequence["_Pop3MonitorDefinition"]]
    Pop3sMonitor: Optional[Sequence["_Pop3sMonitorDefinition"]]
    RadiusMonitor: Optional[Sequence["_RadiusMonitorDefinition"]]
    SipMonitor: Optional[Sequence["_SipMonitorDefinition"]]
    SmtpMonitor: Optional[Sequence["_SmtpMonitorDefinition"]]
    SmtpsMonitor: Optional[Sequence["_SmtpsMonitorDefinition"]]
    TcpMonitor: Optional[Sequence["_TcpMonitorDefinition"]]
    UdpMonitor: Optional[Sequence["_UdpMonitorDefinition"]]

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
            AllowDuplicateMonitors=json_data.get("AllowDuplicateMonitors"),
            Description=json_data.get("Description"),
            DisableQuickstart=json_data.get("DisableQuickstart"),
            FailedChecks=json_data.get("FailedChecks"),
            Id=json_data.get("Id"),
            IsFederated=json_data.get("IsFederated"),
            MonitorPort=json_data.get("MonitorPort"),
            Name=json_data.get("Name"),
            ReceiveTimeout=json_data.get("ReceiveTimeout"),
            SendInterval=json_data.get("SendInterval"),
            SuccessfulChecks=json_data.get("SuccessfulChecks"),
            TenantRef=json_data.get("TenantRef"),
            Type=json_data.get("Type"),
            Uuid=json_data.get("Uuid"),
            Authentication=deserialize_list(json_data.get("Authentication"), AuthenticationDefinition),
            DnsMonitor=deserialize_list(json_data.get("DnsMonitor"), DnsMonitorDefinition),
            ExternalMonitor=deserialize_list(json_data.get("ExternalMonitor"), ExternalMonitorDefinition),
            HttpMonitor=deserialize_list(json_data.get("HttpMonitor"), HttpMonitorDefinition),
            HttpsMonitor=deserialize_list(json_data.get("HttpsMonitor"), HttpsMonitorDefinition),
            ImapMonitor=deserialize_list(json_data.get("ImapMonitor"), ImapMonitorDefinition),
            ImapsMonitor=deserialize_list(json_data.get("ImapsMonitor"), ImapsMonitorDefinition),
            Markers=deserialize_list(json_data.get("Markers"), MarkersDefinition),
            Pop3Monitor=deserialize_list(json_data.get("Pop3Monitor"), Pop3MonitorDefinition),
            Pop3sMonitor=deserialize_list(json_data.get("Pop3sMonitor"), Pop3sMonitorDefinition),
            RadiusMonitor=deserialize_list(json_data.get("RadiusMonitor"), RadiusMonitorDefinition),
            SipMonitor=deserialize_list(json_data.get("SipMonitor"), SipMonitorDefinition),
            SmtpMonitor=deserialize_list(json_data.get("SmtpMonitor"), SmtpMonitorDefinition),
            SmtpsMonitor=deserialize_list(json_data.get("SmtpsMonitor"), SmtpsMonitorDefinition),
            TcpMonitor=deserialize_list(json_data.get("TcpMonitor"), TcpMonitorDefinition),
            UdpMonitor=deserialize_list(json_data.get("UdpMonitor"), UdpMonitorDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AuthenticationDefinition(BaseModel):
    Password: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthenticationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthenticationDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthenticationDefinition = AuthenticationDefinition


@dataclass
class DnsMonitorDefinition(BaseModel):
    Qtype: Optional[str]
    QueryName: Optional[str]
    Rcode: Optional[str]
    RecordType: Optional[str]
    ResponseString: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DnsMonitorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsMonitorDefinition"]:
        if not json_data:
            return None
        return cls(
            Qtype=json_data.get("Qtype"),
            QueryName=json_data.get("QueryName"),
            Rcode=json_data.get("Rcode"),
            RecordType=json_data.get("RecordType"),
            ResponseString=json_data.get("ResponseString"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsMonitorDefinition = DnsMonitorDefinition


@dataclass
class ExternalMonitorDefinition(BaseModel):
    CommandCode: Optional[str]
    CommandParameters: Optional[str]
    CommandPath: Optional[str]
    CommandVariables: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExternalMonitorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExternalMonitorDefinition"]:
        if not json_data:
            return None
        return cls(
            CommandCode=json_data.get("CommandCode"),
            CommandParameters=json_data.get("CommandParameters"),
            CommandPath=json_data.get("CommandPath"),
            CommandVariables=json_data.get("CommandVariables"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExternalMonitorDefinition = ExternalMonitorDefinition


@dataclass
class HttpMonitorDefinition(BaseModel):
    AuthType: Optional[str]
    ExactHttpRequest: Optional[bool]
    HttpRequest: Optional[str]
    HttpRequestBody: Optional[str]
    HttpResponse: Optional[str]
    HttpResponseCode: Optional[Sequence[str]]
    MaintenanceCode: Optional[Sequence[float]]
    MaintenanceResponse: Optional[str]
    ResponseSize: Optional[float]
    SslAttributes: Optional[Sequence["_SslAttributesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpMonitorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpMonitorDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthType=json_data.get("AuthType"),
            ExactHttpRequest=json_data.get("ExactHttpRequest"),
            HttpRequest=json_data.get("HttpRequest"),
            HttpRequestBody=json_data.get("HttpRequestBody"),
            HttpResponse=json_data.get("HttpResponse"),
            HttpResponseCode=json_data.get("HttpResponseCode"),
            MaintenanceCode=json_data.get("MaintenanceCode"),
            MaintenanceResponse=json_data.get("MaintenanceResponse"),
            ResponseSize=json_data.get("ResponseSize"),
            SslAttributes=deserialize_list(json_data.get("SslAttributes"), SslAttributesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpMonitorDefinition = HttpMonitorDefinition


@dataclass
class SslAttributesDefinition(BaseModel):
    PkiProfileRef: Optional[str]
    ServerName: Optional[str]
    SslKeyAndCertificateRef: Optional[str]
    SslProfileRef: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SslAttributesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SslAttributesDefinition"]:
        if not json_data:
            return None
        return cls(
            PkiProfileRef=json_data.get("PkiProfileRef"),
            ServerName=json_data.get("ServerName"),
            SslKeyAndCertificateRef=json_data.get("SslKeyAndCertificateRef"),
            SslProfileRef=json_data.get("SslProfileRef"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SslAttributesDefinition = SslAttributesDefinition


@dataclass
class HttpsMonitorDefinition(BaseModel):
    AuthType: Optional[str]
    ExactHttpRequest: Optional[bool]
    HttpRequest: Optional[str]
    HttpRequestBody: Optional[str]
    HttpResponse: Optional[str]
    HttpResponseCode: Optional[Sequence[str]]
    MaintenanceCode: Optional[Sequence[float]]
    MaintenanceResponse: Optional[str]
    ResponseSize: Optional[float]
    SslAttributes: Optional[Sequence["_SslAttributesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpsMonitorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpsMonitorDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthType=json_data.get("AuthType"),
            ExactHttpRequest=json_data.get("ExactHttpRequest"),
            HttpRequest=json_data.get("HttpRequest"),
            HttpRequestBody=json_data.get("HttpRequestBody"),
            HttpResponse=json_data.get("HttpResponse"),
            HttpResponseCode=json_data.get("HttpResponseCode"),
            MaintenanceCode=json_data.get("MaintenanceCode"),
            MaintenanceResponse=json_data.get("MaintenanceResponse"),
            ResponseSize=json_data.get("ResponseSize"),
            SslAttributes=deserialize_list(json_data.get("SslAttributes"), SslAttributesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpsMonitorDefinition = HttpsMonitorDefinition


@dataclass
class ImapMonitorDefinition(BaseModel):
    Folder: Optional[str]
    SslAttributes: Optional[Sequence["_SslAttributesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ImapMonitorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImapMonitorDefinition"]:
        if not json_data:
            return None
        return cls(
            Folder=json_data.get("Folder"),
            SslAttributes=deserialize_list(json_data.get("SslAttributes"), SslAttributesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImapMonitorDefinition = ImapMonitorDefinition


@dataclass
class ImapsMonitorDefinition(BaseModel):
    Folder: Optional[str]
    SslAttributes: Optional[Sequence["_SslAttributesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ImapsMonitorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImapsMonitorDefinition"]:
        if not json_data:
            return None
        return cls(
            Folder=json_data.get("Folder"),
            SslAttributes=deserialize_list(json_data.get("SslAttributes"), SslAttributesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImapsMonitorDefinition = ImapsMonitorDefinition


@dataclass
class MarkersDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MarkersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MarkersDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MarkersDefinition = MarkersDefinition


@dataclass
class Pop3MonitorDefinition(BaseModel):
    SslAttributes: Optional[Sequence["_SslAttributesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_Pop3MonitorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Pop3MonitorDefinition"]:
        if not json_data:
            return None
        return cls(
            SslAttributes=deserialize_list(json_data.get("SslAttributes"), SslAttributesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_Pop3MonitorDefinition = Pop3MonitorDefinition


@dataclass
class Pop3sMonitorDefinition(BaseModel):
    SslAttributes: Optional[Sequence["_SslAttributesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_Pop3sMonitorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Pop3sMonitorDefinition"]:
        if not json_data:
            return None
        return cls(
            SslAttributes=deserialize_list(json_data.get("SslAttributes"), SslAttributesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_Pop3sMonitorDefinition = Pop3sMonitorDefinition


@dataclass
class RadiusMonitorDefinition(BaseModel):
    Password: Optional[str]
    SharedSecret: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RadiusMonitorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RadiusMonitorDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            SharedSecret=json_data.get("SharedSecret"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RadiusMonitorDefinition = RadiusMonitorDefinition


@dataclass
class SipMonitorDefinition(BaseModel):
    SipMonitorTransport: Optional[str]
    SipRequestCode: Optional[str]
    SipResponse: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SipMonitorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SipMonitorDefinition"]:
        if not json_data:
            return None
        return cls(
            SipMonitorTransport=json_data.get("SipMonitorTransport"),
            SipRequestCode=json_data.get("SipRequestCode"),
            SipResponse=json_data.get("SipResponse"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SipMonitorDefinition = SipMonitorDefinition


@dataclass
class SmtpMonitorDefinition(BaseModel):
    Domainname: Optional[str]
    MailData: Optional[str]
    RecipientsIds: Optional[Sequence[str]]
    SenderId: Optional[str]
    SslAttributes: Optional[Sequence["_SslAttributesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SmtpMonitorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SmtpMonitorDefinition"]:
        if not json_data:
            return None
        return cls(
            Domainname=json_data.get("Domainname"),
            MailData=json_data.get("MailData"),
            RecipientsIds=json_data.get("RecipientsIds"),
            SenderId=json_data.get("SenderId"),
            SslAttributes=deserialize_list(json_data.get("SslAttributes"), SslAttributesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SmtpMonitorDefinition = SmtpMonitorDefinition


@dataclass
class SmtpsMonitorDefinition(BaseModel):
    Domainname: Optional[str]
    MailData: Optional[str]
    RecipientsIds: Optional[Sequence[str]]
    SenderId: Optional[str]
    SslAttributes: Optional[Sequence["_SslAttributesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SmtpsMonitorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SmtpsMonitorDefinition"]:
        if not json_data:
            return None
        return cls(
            Domainname=json_data.get("Domainname"),
            MailData=json_data.get("MailData"),
            RecipientsIds=json_data.get("RecipientsIds"),
            SenderId=json_data.get("SenderId"),
            SslAttributes=deserialize_list(json_data.get("SslAttributes"), SslAttributesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SmtpsMonitorDefinition = SmtpsMonitorDefinition


@dataclass
class TcpMonitorDefinition(BaseModel):
    MaintenanceResponse: Optional[str]
    TcpHalfOpen: Optional[bool]
    TcpRequest: Optional[str]
    TcpResponse: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TcpMonitorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TcpMonitorDefinition"]:
        if not json_data:
            return None
        return cls(
            MaintenanceResponse=json_data.get("MaintenanceResponse"),
            TcpHalfOpen=json_data.get("TcpHalfOpen"),
            TcpRequest=json_data.get("TcpRequest"),
            TcpResponse=json_data.get("TcpResponse"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TcpMonitorDefinition = TcpMonitorDefinition


@dataclass
class UdpMonitorDefinition(BaseModel):
    MaintenanceResponse: Optional[str]
    UdpRequest: Optional[str]
    UdpResponse: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UdpMonitorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UdpMonitorDefinition"]:
        if not json_data:
            return None
        return cls(
            MaintenanceResponse=json_data.get("MaintenanceResponse"),
            UdpRequest=json_data.get("UdpRequest"),
            UdpResponse=json_data.get("UdpResponse"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UdpMonitorDefinition = UdpMonitorDefinition


