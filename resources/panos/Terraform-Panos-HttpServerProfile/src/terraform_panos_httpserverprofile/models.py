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
    Id: Optional[str]
    Name: Optional[str]
    PasswordEnc: Optional[Sequence["_PasswordEnc"]]
    PasswordRaw: Optional[Sequence["_PasswordRaw"]]
    TagRegistration: Optional[bool]
    Vsys: Optional[str]
    AuthFormat: Optional[Sequence["_AuthFormat"]]
    ConfigFormat: Optional[Sequence["_ConfigFormat"]]
    DataFormat: Optional[Sequence["_DataFormat"]]
    GtpFormat: Optional[Sequence["_GtpFormat"]]
    HipMatchFormat: Optional[Sequence["_HipMatchFormat"]]
    HttpServer: Optional[Sequence["_HttpServer"]]
    IptagFormat: Optional[Sequence["_IptagFormat"]]
    SctpFormat: Optional[Sequence["_SctpFormat"]]
    SystemFormat: Optional[Sequence["_SystemFormat"]]
    ThreatFormat: Optional[Sequence["_ThreatFormat"]]
    TrafficFormat: Optional[Sequence["_TrafficFormat"]]
    TunnelFormat: Optional[Sequence["_TunnelFormat"]]
    UrlFormat: Optional[Sequence["_UrlFormat"]]
    UserIdFormat: Optional[Sequence["_UserIdFormat"]]
    WildfireFormat: Optional[Sequence["_WildfireFormat"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PasswordEnc=json_data.get("PasswordEnc"),
            PasswordRaw=json_data.get("PasswordRaw"),
            TagRegistration=json_data.get("TagRegistration"),
            Vsys=json_data.get("Vsys"),
            AuthFormat=json_data.get("AuthFormat"),
            ConfigFormat=json_data.get("ConfigFormat"),
            DataFormat=json_data.get("DataFormat"),
            GtpFormat=json_data.get("GtpFormat"),
            HipMatchFormat=json_data.get("HipMatchFormat"),
            HttpServer=json_data.get("HttpServer"),
            IptagFormat=json_data.get("IptagFormat"),
            SctpFormat=json_data.get("SctpFormat"),
            SystemFormat=json_data.get("SystemFormat"),
            ThreatFormat=json_data.get("ThreatFormat"),
            TrafficFormat=json_data.get("TrafficFormat"),
            TunnelFormat=json_data.get("TunnelFormat"),
            UrlFormat=json_data.get("UrlFormat"),
            UserIdFormat=json_data.get("UserIdFormat"),
            WildfireFormat=json_data.get("WildfireFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PasswordEnc:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PasswordEnc"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PasswordEnc"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PasswordEnc = PasswordEnc


@dataclass
class PasswordRaw:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PasswordRaw"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PasswordRaw"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PasswordRaw = PasswordRaw


@dataclass
class AuthFormat:
    Headers: Optional[Sequence["_Headers"]]
    Name: Optional[str]
    Params: Optional[Sequence["_Params"]]
    Payload: Optional[str]
    UriFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthFormat"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthFormat"]:
        if not json_data:
            return None
        return cls(
            Headers=json_data.get("Headers"),
            Name=json_data.get("Name"),
            Params=json_data.get("Params"),
            Payload=json_data.get("Payload"),
            UriFormat=json_data.get("UriFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthFormat = AuthFormat


@dataclass
class Headers:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Headers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Headers"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Headers = Headers


@dataclass
class Params:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Params"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Params"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Params = Params


@dataclass
class ConfigFormat:
    Headers: Optional[Sequence["_Headers2"]]
    Name: Optional[str]
    Params: Optional[Sequence["_Params2"]]
    Payload: Optional[str]
    UriFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigFormat"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigFormat"]:
        if not json_data:
            return None
        return cls(
            Headers=json_data.get("Headers"),
            Name=json_data.get("Name"),
            Params=json_data.get("Params"),
            Payload=json_data.get("Payload"),
            UriFormat=json_data.get("UriFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigFormat = ConfigFormat


@dataclass
class Headers2:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Headers2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Headers2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Headers2 = Headers2


@dataclass
class Params2:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Params2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Params2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Params2 = Params2


@dataclass
class DataFormat:
    Headers: Optional[Sequence["_Headers3"]]
    Name: Optional[str]
    Params: Optional[Sequence["_Params3"]]
    Payload: Optional[str]
    UriFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataFormat"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataFormat"]:
        if not json_data:
            return None
        return cls(
            Headers=json_data.get("Headers"),
            Name=json_data.get("Name"),
            Params=json_data.get("Params"),
            Payload=json_data.get("Payload"),
            UriFormat=json_data.get("UriFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataFormat = DataFormat


@dataclass
class Headers3:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Headers3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Headers3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Headers3 = Headers3


@dataclass
class Params3:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Params3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Params3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Params3 = Params3


@dataclass
class GtpFormat:
    Headers: Optional[Sequence["_Headers4"]]
    Name: Optional[str]
    Params: Optional[Sequence["_Params4"]]
    Payload: Optional[str]
    UriFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GtpFormat"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GtpFormat"]:
        if not json_data:
            return None
        return cls(
            Headers=json_data.get("Headers"),
            Name=json_data.get("Name"),
            Params=json_data.get("Params"),
            Payload=json_data.get("Payload"),
            UriFormat=json_data.get("UriFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GtpFormat = GtpFormat


@dataclass
class Headers4:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Headers4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Headers4"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Headers4 = Headers4


@dataclass
class Params4:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Params4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Params4"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Params4 = Params4


@dataclass
class HipMatchFormat:
    Headers: Optional[Sequence["_Headers5"]]
    Name: Optional[str]
    Params: Optional[Sequence["_Params5"]]
    Payload: Optional[str]
    UriFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HipMatchFormat"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HipMatchFormat"]:
        if not json_data:
            return None
        return cls(
            Headers=json_data.get("Headers"),
            Name=json_data.get("Name"),
            Params=json_data.get("Params"),
            Payload=json_data.get("Payload"),
            UriFormat=json_data.get("UriFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HipMatchFormat = HipMatchFormat


@dataclass
class Headers5:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Headers5"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Headers5"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Headers5 = Headers5


@dataclass
class Params5:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Params5"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Params5"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Params5 = Params5


@dataclass
class HttpServer:
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
        cls: Type["_HttpServer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpServer"]:
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
_HttpServer = HttpServer


@dataclass
class IptagFormat:
    Headers: Optional[Sequence["_Headers6"]]
    Name: Optional[str]
    Params: Optional[Sequence["_Params6"]]
    Payload: Optional[str]
    UriFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IptagFormat"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IptagFormat"]:
        if not json_data:
            return None
        return cls(
            Headers=json_data.get("Headers"),
            Name=json_data.get("Name"),
            Params=json_data.get("Params"),
            Payload=json_data.get("Payload"),
            UriFormat=json_data.get("UriFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IptagFormat = IptagFormat


@dataclass
class Headers6:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Headers6"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Headers6"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Headers6 = Headers6


@dataclass
class Params6:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Params6"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Params6"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Params6 = Params6


@dataclass
class SctpFormat:
    Headers: Optional[Sequence["_Headers7"]]
    Name: Optional[str]
    Params: Optional[Sequence["_Params7"]]
    Payload: Optional[str]
    UriFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SctpFormat"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SctpFormat"]:
        if not json_data:
            return None
        return cls(
            Headers=json_data.get("Headers"),
            Name=json_data.get("Name"),
            Params=json_data.get("Params"),
            Payload=json_data.get("Payload"),
            UriFormat=json_data.get("UriFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SctpFormat = SctpFormat


@dataclass
class Headers7:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Headers7"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Headers7"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Headers7 = Headers7


@dataclass
class Params7:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Params7"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Params7"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Params7 = Params7


@dataclass
class SystemFormat:
    Headers: Optional[Sequence["_Headers8"]]
    Name: Optional[str]
    Params: Optional[Sequence["_Params8"]]
    Payload: Optional[str]
    UriFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SystemFormat"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SystemFormat"]:
        if not json_data:
            return None
        return cls(
            Headers=json_data.get("Headers"),
            Name=json_data.get("Name"),
            Params=json_data.get("Params"),
            Payload=json_data.get("Payload"),
            UriFormat=json_data.get("UriFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SystemFormat = SystemFormat


@dataclass
class Headers8:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Headers8"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Headers8"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Headers8 = Headers8


@dataclass
class Params8:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Params8"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Params8"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Params8 = Params8


@dataclass
class ThreatFormat:
    Headers: Optional[Sequence["_Headers9"]]
    Name: Optional[str]
    Params: Optional[Sequence["_Params9"]]
    Payload: Optional[str]
    UriFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ThreatFormat"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThreatFormat"]:
        if not json_data:
            return None
        return cls(
            Headers=json_data.get("Headers"),
            Name=json_data.get("Name"),
            Params=json_data.get("Params"),
            Payload=json_data.get("Payload"),
            UriFormat=json_data.get("UriFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThreatFormat = ThreatFormat


@dataclass
class Headers9:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Headers9"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Headers9"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Headers9 = Headers9


@dataclass
class Params9:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Params9"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Params9"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Params9 = Params9


@dataclass
class TrafficFormat:
    Headers: Optional[Sequence["_Headers10"]]
    Name: Optional[str]
    Params: Optional[Sequence["_Params10"]]
    Payload: Optional[str]
    UriFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TrafficFormat"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrafficFormat"]:
        if not json_data:
            return None
        return cls(
            Headers=json_data.get("Headers"),
            Name=json_data.get("Name"),
            Params=json_data.get("Params"),
            Payload=json_data.get("Payload"),
            UriFormat=json_data.get("UriFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrafficFormat = TrafficFormat


@dataclass
class Headers10:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Headers10"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Headers10"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Headers10 = Headers10


@dataclass
class Params10:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Params10"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Params10"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Params10 = Params10


@dataclass
class TunnelFormat:
    Headers: Optional[Sequence["_Headers11"]]
    Name: Optional[str]
    Params: Optional[Sequence["_Params11"]]
    Payload: Optional[str]
    UriFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TunnelFormat"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TunnelFormat"]:
        if not json_data:
            return None
        return cls(
            Headers=json_data.get("Headers"),
            Name=json_data.get("Name"),
            Params=json_data.get("Params"),
            Payload=json_data.get("Payload"),
            UriFormat=json_data.get("UriFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TunnelFormat = TunnelFormat


@dataclass
class Headers11:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Headers11"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Headers11"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Headers11 = Headers11


@dataclass
class Params11:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Params11"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Params11"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Params11 = Params11


@dataclass
class UrlFormat:
    Headers: Optional[Sequence["_Headers12"]]
    Name: Optional[str]
    Params: Optional[Sequence["_Params12"]]
    Payload: Optional[str]
    UriFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UrlFormat"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UrlFormat"]:
        if not json_data:
            return None
        return cls(
            Headers=json_data.get("Headers"),
            Name=json_data.get("Name"),
            Params=json_data.get("Params"),
            Payload=json_data.get("Payload"),
            UriFormat=json_data.get("UriFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UrlFormat = UrlFormat


@dataclass
class Headers12:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Headers12"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Headers12"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Headers12 = Headers12


@dataclass
class Params12:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Params12"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Params12"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Params12 = Params12


@dataclass
class UserIdFormat:
    Headers: Optional[Sequence["_Headers13"]]
    Name: Optional[str]
    Params: Optional[Sequence["_Params13"]]
    Payload: Optional[str]
    UriFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserIdFormat"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserIdFormat"]:
        if not json_data:
            return None
        return cls(
            Headers=json_data.get("Headers"),
            Name=json_data.get("Name"),
            Params=json_data.get("Params"),
            Payload=json_data.get("Payload"),
            UriFormat=json_data.get("UriFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserIdFormat = UserIdFormat


@dataclass
class Headers13:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Headers13"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Headers13"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Headers13 = Headers13


@dataclass
class Params13:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Params13"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Params13"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Params13 = Params13


@dataclass
class WildfireFormat:
    Headers: Optional[Sequence["_Headers14"]]
    Name: Optional[str]
    Params: Optional[Sequence["_Params14"]]
    Payload: Optional[str]
    UriFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WildfireFormat"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WildfireFormat"]:
        if not json_data:
            return None
        return cls(
            Headers=json_data.get("Headers"),
            Name=json_data.get("Name"),
            Params=json_data.get("Params"),
            Payload=json_data.get("Payload"),
            UriFormat=json_data.get("UriFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WildfireFormat = WildfireFormat


@dataclass
class Headers14:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Headers14"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Headers14"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Headers14 = Headers14


@dataclass
class Params14:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Params14"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Params14"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Params14 = Params14


