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
    Id: Optional[str]
    Name: Optional[str]
    PasswordEnc: Optional[Sequence["_PasswordEncDefinition"]]
    PasswordRaw: Optional[Sequence["_PasswordRawDefinition"]]
    TagRegistration: Optional[bool]
    Vsys: Optional[str]
    AuthFormat: Optional[Sequence["_AuthFormatDefinition"]]
    ConfigFormat: Optional[Sequence["_ConfigFormatDefinition"]]
    DataFormat: Optional[Sequence["_DataFormatDefinition"]]
    GtpFormat: Optional[Sequence["_GtpFormatDefinition"]]
    HipMatchFormat: Optional[Sequence["_HipMatchFormatDefinition"]]
    HttpServer: Optional[Sequence["_HttpServerDefinition"]]
    IptagFormat: Optional[Sequence["_IptagFormatDefinition"]]
    SctpFormat: Optional[Sequence["_SctpFormatDefinition"]]
    SystemFormat: Optional[Sequence["_SystemFormatDefinition"]]
    ThreatFormat: Optional[Sequence["_ThreatFormatDefinition"]]
    TrafficFormat: Optional[Sequence["_TrafficFormatDefinition"]]
    TunnelFormat: Optional[Sequence["_TunnelFormatDefinition"]]
    UrlFormat: Optional[Sequence["_UrlFormatDefinition"]]
    UserIdFormat: Optional[Sequence["_UserIdFormatDefinition"]]
    WildfireFormat: Optional[Sequence["_WildfireFormatDefinition"]]

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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PasswordEnc=deserialize_list(json_data.get("PasswordEnc"), PasswordEncDefinition),
            PasswordRaw=deserialize_list(json_data.get("PasswordRaw"), PasswordRawDefinition),
            TagRegistration=json_data.get("TagRegistration"),
            Vsys=json_data.get("Vsys"),
            AuthFormat=deserialize_list(json_data.get("AuthFormat"), AuthFormatDefinition),
            ConfigFormat=deserialize_list(json_data.get("ConfigFormat"), ConfigFormatDefinition),
            DataFormat=deserialize_list(json_data.get("DataFormat"), DataFormatDefinition),
            GtpFormat=deserialize_list(json_data.get("GtpFormat"), GtpFormatDefinition),
            HipMatchFormat=deserialize_list(json_data.get("HipMatchFormat"), HipMatchFormatDefinition),
            HttpServer=deserialize_list(json_data.get("HttpServer"), HttpServerDefinition),
            IptagFormat=deserialize_list(json_data.get("IptagFormat"), IptagFormatDefinition),
            SctpFormat=deserialize_list(json_data.get("SctpFormat"), SctpFormatDefinition),
            SystemFormat=deserialize_list(json_data.get("SystemFormat"), SystemFormatDefinition),
            ThreatFormat=deserialize_list(json_data.get("ThreatFormat"), ThreatFormatDefinition),
            TrafficFormat=deserialize_list(json_data.get("TrafficFormat"), TrafficFormatDefinition),
            TunnelFormat=deserialize_list(json_data.get("TunnelFormat"), TunnelFormatDefinition),
            UrlFormat=deserialize_list(json_data.get("UrlFormat"), UrlFormatDefinition),
            UserIdFormat=deserialize_list(json_data.get("UserIdFormat"), UserIdFormatDefinition),
            WildfireFormat=deserialize_list(json_data.get("WildfireFormat"), WildfireFormatDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PasswordEncDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PasswordEncDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PasswordEncDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PasswordEncDefinition = PasswordEncDefinition


@dataclass
class PasswordRawDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PasswordRawDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PasswordRawDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PasswordRawDefinition = PasswordRawDefinition


@dataclass
class AuthFormatDefinition(BaseModel):
    Headers: Optional[Sequence["_HeadersDefinition"]]
    Name: Optional[str]
    Params: Optional[Sequence["_ParamsDefinition"]]
    Payload: Optional[str]
    UriFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthFormatDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthFormatDefinition"]:
        if not json_data:
            return None
        return cls(
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition),
            Name=json_data.get("Name"),
            Params=deserialize_list(json_data.get("Params"), ParamsDefinition),
            Payload=json_data.get("Payload"),
            UriFormat=json_data.get("UriFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthFormatDefinition = AuthFormatDefinition


@dataclass
class HeadersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersDefinition = HeadersDefinition


@dataclass
class ParamsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParamsDefinition = ParamsDefinition


@dataclass
class ConfigFormatDefinition(BaseModel):
    Headers: Optional[Sequence["_HeadersDefinition2"]]
    Name: Optional[str]
    Params: Optional[Sequence["_ParamsDefinition2"]]
    Payload: Optional[str]
    UriFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigFormatDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigFormatDefinition"]:
        if not json_data:
            return None
        return cls(
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition2),
            Name=json_data.get("Name"),
            Params=deserialize_list(json_data.get("Params"), ParamsDefinition2),
            Payload=json_data.get("Payload"),
            UriFormat=json_data.get("UriFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigFormatDefinition = ConfigFormatDefinition


@dataclass
class HeadersDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersDefinition2 = HeadersDefinition2


@dataclass
class ParamsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParamsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParamsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParamsDefinition2 = ParamsDefinition2


@dataclass
class DataFormatDefinition(BaseModel):
    Headers: Optional[Sequence["_HeadersDefinition3"]]
    Name: Optional[str]
    Params: Optional[Sequence["_ParamsDefinition3"]]
    Payload: Optional[str]
    UriFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataFormatDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataFormatDefinition"]:
        if not json_data:
            return None
        return cls(
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition3),
            Name=json_data.get("Name"),
            Params=deserialize_list(json_data.get("Params"), ParamsDefinition3),
            Payload=json_data.get("Payload"),
            UriFormat=json_data.get("UriFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataFormatDefinition = DataFormatDefinition


@dataclass
class HeadersDefinition3(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersDefinition3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersDefinition3 = HeadersDefinition3


@dataclass
class ParamsDefinition3(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParamsDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParamsDefinition3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParamsDefinition3 = ParamsDefinition3


@dataclass
class GtpFormatDefinition(BaseModel):
    Headers: Optional[Sequence["_HeadersDefinition4"]]
    Name: Optional[str]
    Params: Optional[Sequence["_ParamsDefinition4"]]
    Payload: Optional[str]
    UriFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GtpFormatDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GtpFormatDefinition"]:
        if not json_data:
            return None
        return cls(
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition4),
            Name=json_data.get("Name"),
            Params=deserialize_list(json_data.get("Params"), ParamsDefinition4),
            Payload=json_data.get("Payload"),
            UriFormat=json_data.get("UriFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GtpFormatDefinition = GtpFormatDefinition


@dataclass
class HeadersDefinition4(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersDefinition4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersDefinition4"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersDefinition4 = HeadersDefinition4


@dataclass
class ParamsDefinition4(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParamsDefinition4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParamsDefinition4"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParamsDefinition4 = ParamsDefinition4


@dataclass
class HipMatchFormatDefinition(BaseModel):
    Headers: Optional[Sequence["_HeadersDefinition5"]]
    Name: Optional[str]
    Params: Optional[Sequence["_ParamsDefinition5"]]
    Payload: Optional[str]
    UriFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HipMatchFormatDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HipMatchFormatDefinition"]:
        if not json_data:
            return None
        return cls(
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition5),
            Name=json_data.get("Name"),
            Params=deserialize_list(json_data.get("Params"), ParamsDefinition5),
            Payload=json_data.get("Payload"),
            UriFormat=json_data.get("UriFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HipMatchFormatDefinition = HipMatchFormatDefinition


@dataclass
class HeadersDefinition5(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersDefinition5"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersDefinition5"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersDefinition5 = HeadersDefinition5


@dataclass
class ParamsDefinition5(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParamsDefinition5"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParamsDefinition5"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParamsDefinition5 = ParamsDefinition5


@dataclass
class HttpServerDefinition(BaseModel):
    Address: Optional[str]
    CertificateProfile: Optional[str]
    HttpMethod: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]
    TlsVersion: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpServerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpServerDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            CertificateProfile=json_data.get("CertificateProfile"),
            HttpMethod=json_data.get("HttpMethod"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            TlsVersion=json_data.get("TlsVersion"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpServerDefinition = HttpServerDefinition


@dataclass
class IptagFormatDefinition(BaseModel):
    Headers: Optional[Sequence["_HeadersDefinition6"]]
    Name: Optional[str]
    Params: Optional[Sequence["_ParamsDefinition6"]]
    Payload: Optional[str]
    UriFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IptagFormatDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IptagFormatDefinition"]:
        if not json_data:
            return None
        return cls(
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition6),
            Name=json_data.get("Name"),
            Params=deserialize_list(json_data.get("Params"), ParamsDefinition6),
            Payload=json_data.get("Payload"),
            UriFormat=json_data.get("UriFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IptagFormatDefinition = IptagFormatDefinition


@dataclass
class HeadersDefinition6(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersDefinition6"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersDefinition6"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersDefinition6 = HeadersDefinition6


@dataclass
class ParamsDefinition6(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParamsDefinition6"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParamsDefinition6"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParamsDefinition6 = ParamsDefinition6


@dataclass
class SctpFormatDefinition(BaseModel):
    Headers: Optional[Sequence["_HeadersDefinition7"]]
    Name: Optional[str]
    Params: Optional[Sequence["_ParamsDefinition7"]]
    Payload: Optional[str]
    UriFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SctpFormatDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SctpFormatDefinition"]:
        if not json_data:
            return None
        return cls(
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition7),
            Name=json_data.get("Name"),
            Params=deserialize_list(json_data.get("Params"), ParamsDefinition7),
            Payload=json_data.get("Payload"),
            UriFormat=json_data.get("UriFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SctpFormatDefinition = SctpFormatDefinition


@dataclass
class HeadersDefinition7(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersDefinition7"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersDefinition7"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersDefinition7 = HeadersDefinition7


@dataclass
class ParamsDefinition7(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParamsDefinition7"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParamsDefinition7"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParamsDefinition7 = ParamsDefinition7


@dataclass
class SystemFormatDefinition(BaseModel):
    Headers: Optional[Sequence["_HeadersDefinition8"]]
    Name: Optional[str]
    Params: Optional[Sequence["_ParamsDefinition8"]]
    Payload: Optional[str]
    UriFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SystemFormatDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SystemFormatDefinition"]:
        if not json_data:
            return None
        return cls(
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition8),
            Name=json_data.get("Name"),
            Params=deserialize_list(json_data.get("Params"), ParamsDefinition8),
            Payload=json_data.get("Payload"),
            UriFormat=json_data.get("UriFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SystemFormatDefinition = SystemFormatDefinition


@dataclass
class HeadersDefinition8(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersDefinition8"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersDefinition8"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersDefinition8 = HeadersDefinition8


@dataclass
class ParamsDefinition8(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParamsDefinition8"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParamsDefinition8"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParamsDefinition8 = ParamsDefinition8


@dataclass
class ThreatFormatDefinition(BaseModel):
    Headers: Optional[Sequence["_HeadersDefinition9"]]
    Name: Optional[str]
    Params: Optional[Sequence["_ParamsDefinition9"]]
    Payload: Optional[str]
    UriFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ThreatFormatDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThreatFormatDefinition"]:
        if not json_data:
            return None
        return cls(
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition9),
            Name=json_data.get("Name"),
            Params=deserialize_list(json_data.get("Params"), ParamsDefinition9),
            Payload=json_data.get("Payload"),
            UriFormat=json_data.get("UriFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThreatFormatDefinition = ThreatFormatDefinition


@dataclass
class HeadersDefinition9(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersDefinition9"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersDefinition9"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersDefinition9 = HeadersDefinition9


@dataclass
class ParamsDefinition9(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParamsDefinition9"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParamsDefinition9"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParamsDefinition9 = ParamsDefinition9


@dataclass
class TrafficFormatDefinition(BaseModel):
    Headers: Optional[Sequence["_HeadersDefinition10"]]
    Name: Optional[str]
    Params: Optional[Sequence["_ParamsDefinition10"]]
    Payload: Optional[str]
    UriFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TrafficFormatDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrafficFormatDefinition"]:
        if not json_data:
            return None
        return cls(
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition10),
            Name=json_data.get("Name"),
            Params=deserialize_list(json_data.get("Params"), ParamsDefinition10),
            Payload=json_data.get("Payload"),
            UriFormat=json_data.get("UriFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrafficFormatDefinition = TrafficFormatDefinition


@dataclass
class HeadersDefinition10(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersDefinition10"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersDefinition10"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersDefinition10 = HeadersDefinition10


@dataclass
class ParamsDefinition10(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParamsDefinition10"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParamsDefinition10"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParamsDefinition10 = ParamsDefinition10


@dataclass
class TunnelFormatDefinition(BaseModel):
    Headers: Optional[Sequence["_HeadersDefinition11"]]
    Name: Optional[str]
    Params: Optional[Sequence["_ParamsDefinition11"]]
    Payload: Optional[str]
    UriFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TunnelFormatDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TunnelFormatDefinition"]:
        if not json_data:
            return None
        return cls(
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition11),
            Name=json_data.get("Name"),
            Params=deserialize_list(json_data.get("Params"), ParamsDefinition11),
            Payload=json_data.get("Payload"),
            UriFormat=json_data.get("UriFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TunnelFormatDefinition = TunnelFormatDefinition


@dataclass
class HeadersDefinition11(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersDefinition11"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersDefinition11"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersDefinition11 = HeadersDefinition11


@dataclass
class ParamsDefinition11(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParamsDefinition11"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParamsDefinition11"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParamsDefinition11 = ParamsDefinition11


@dataclass
class UrlFormatDefinition(BaseModel):
    Headers: Optional[Sequence["_HeadersDefinition12"]]
    Name: Optional[str]
    Params: Optional[Sequence["_ParamsDefinition12"]]
    Payload: Optional[str]
    UriFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UrlFormatDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UrlFormatDefinition"]:
        if not json_data:
            return None
        return cls(
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition12),
            Name=json_data.get("Name"),
            Params=deserialize_list(json_data.get("Params"), ParamsDefinition12),
            Payload=json_data.get("Payload"),
            UriFormat=json_data.get("UriFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UrlFormatDefinition = UrlFormatDefinition


@dataclass
class HeadersDefinition12(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersDefinition12"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersDefinition12"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersDefinition12 = HeadersDefinition12


@dataclass
class ParamsDefinition12(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParamsDefinition12"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParamsDefinition12"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParamsDefinition12 = ParamsDefinition12


@dataclass
class UserIdFormatDefinition(BaseModel):
    Headers: Optional[Sequence["_HeadersDefinition13"]]
    Name: Optional[str]
    Params: Optional[Sequence["_ParamsDefinition13"]]
    Payload: Optional[str]
    UriFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserIdFormatDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserIdFormatDefinition"]:
        if not json_data:
            return None
        return cls(
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition13),
            Name=json_data.get("Name"),
            Params=deserialize_list(json_data.get("Params"), ParamsDefinition13),
            Payload=json_data.get("Payload"),
            UriFormat=json_data.get("UriFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserIdFormatDefinition = UserIdFormatDefinition


@dataclass
class HeadersDefinition13(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersDefinition13"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersDefinition13"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersDefinition13 = HeadersDefinition13


@dataclass
class ParamsDefinition13(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParamsDefinition13"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParamsDefinition13"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParamsDefinition13 = ParamsDefinition13


@dataclass
class WildfireFormatDefinition(BaseModel):
    Headers: Optional[Sequence["_HeadersDefinition14"]]
    Name: Optional[str]
    Params: Optional[Sequence["_ParamsDefinition14"]]
    Payload: Optional[str]
    UriFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WildfireFormatDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WildfireFormatDefinition"]:
        if not json_data:
            return None
        return cls(
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition14),
            Name=json_data.get("Name"),
            Params=deserialize_list(json_data.get("Params"), ParamsDefinition14),
            Payload=json_data.get("Payload"),
            UriFormat=json_data.get("UriFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WildfireFormatDefinition = WildfireFormatDefinition


@dataclass
class HeadersDefinition14(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersDefinition14"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersDefinition14"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersDefinition14 = HeadersDefinition14


@dataclass
class ParamsDefinition14(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParamsDefinition14"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParamsDefinition14"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParamsDefinition14 = ParamsDefinition14


