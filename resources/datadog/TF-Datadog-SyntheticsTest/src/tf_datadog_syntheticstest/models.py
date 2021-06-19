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
    DeviceIds: Optional[Sequence[str]]
    Id: Optional[str]
    Locations: Optional[Sequence[str]]
    Message: Optional[str]
    MonitorId: Optional[float]
    Name: Optional[str]
    RequestHeaders: Optional[Sequence["_RequestHeadersDefinition"]]
    RequestQuery: Optional[Sequence["_RequestQueryDefinition"]]
    SetCookie: Optional[str]
    Status: Optional[str]
    Subtype: Optional[str]
    Tags: Optional[Sequence[str]]
    Type: Optional[str]
    ApiStep: Optional[Sequence["_ApiStepDefinition"]]
    Assertion: Optional[Sequence["_AssertionDefinition"]]
    BrowserStep: Optional[Sequence["_BrowserStepDefinition"]]
    BrowserVariable: Optional[Sequence["_BrowserVariableDefinition"]]
    ConfigVariable: Optional[Sequence["_ConfigVariableDefinition"]]
    OptionsList: Optional[Sequence["_OptionsListDefinition"]]
    RequestBasicauth: Optional[Sequence["_RequestBasicauthDefinition"]]
    RequestClientCertificate: Optional[Sequence["_RequestClientCertificateDefinition"]]
    RequestDefinition: Optional[Sequence["_RequestDefinitionDefinition"]]

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
            DeviceIds=json_data.get("DeviceIds"),
            Id=json_data.get("Id"),
            Locations=json_data.get("Locations"),
            Message=json_data.get("Message"),
            MonitorId=json_data.get("MonitorId"),
            Name=json_data.get("Name"),
            RequestHeaders=deserialize_list(json_data.get("RequestHeaders"), RequestHeadersDefinition),
            RequestQuery=deserialize_list(json_data.get("RequestQuery"), RequestQueryDefinition),
            SetCookie=json_data.get("SetCookie"),
            Status=json_data.get("Status"),
            Subtype=json_data.get("Subtype"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
            ApiStep=deserialize_list(json_data.get("ApiStep"), ApiStepDefinition),
            Assertion=deserialize_list(json_data.get("Assertion"), AssertionDefinition),
            BrowserStep=deserialize_list(json_data.get("BrowserStep"), BrowserStepDefinition),
            BrowserVariable=deserialize_list(json_data.get("BrowserVariable"), BrowserVariableDefinition),
            ConfigVariable=deserialize_list(json_data.get("ConfigVariable"), ConfigVariableDefinition),
            OptionsList=deserialize_list(json_data.get("OptionsList"), OptionsListDefinition),
            RequestBasicauth=deserialize_list(json_data.get("RequestBasicauth"), RequestBasicauthDefinition),
            RequestClientCertificate=deserialize_list(json_data.get("RequestClientCertificate"), RequestClientCertificateDefinition),
            RequestDefinition=deserialize_list(json_data.get("RequestDefinition"), RequestDefinitionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RequestHeadersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestHeadersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestHeadersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestHeadersDefinition = RequestHeadersDefinition


@dataclass
class RequestQueryDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestQueryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestQueryDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestQueryDefinition = RequestQueryDefinition


@dataclass
class ApiStepDefinition(BaseModel):
    AllowFailure: Optional[bool]
    IsCritical: Optional[bool]
    Name: Optional[str]
    RequestHeaders: Optional[Sequence["_RequestHeadersDefinition2"]]
    RequestQuery: Optional[Sequence["_RequestQueryDefinition2"]]
    Subtype: Optional[str]
    Assertion: Optional[Sequence["_AssertionDefinition"]]
    ExtractedValue: Optional[Sequence["_ExtractedValueDefinition"]]
    RequestBasicauth: Optional[Sequence["_RequestBasicauthDefinition"]]
    RequestClientCertificate: Optional[Sequence["_RequestClientCertificateDefinition"]]
    RequestDefinition: Optional[Sequence["_RequestDefinitionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ApiStepDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApiStepDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowFailure=json_data.get("AllowFailure"),
            IsCritical=json_data.get("IsCritical"),
            Name=json_data.get("Name"),
            RequestHeaders=deserialize_list(json_data.get("RequestHeaders"), RequestHeadersDefinition2),
            RequestQuery=deserialize_list(json_data.get("RequestQuery"), RequestQueryDefinition2),
            Subtype=json_data.get("Subtype"),
            Assertion=deserialize_list(json_data.get("Assertion"), AssertionDefinition),
            ExtractedValue=deserialize_list(json_data.get("ExtractedValue"), ExtractedValueDefinition),
            RequestBasicauth=deserialize_list(json_data.get("RequestBasicauth"), RequestBasicauthDefinition),
            RequestClientCertificate=deserialize_list(json_data.get("RequestClientCertificate"), RequestClientCertificateDefinition),
            RequestDefinition=deserialize_list(json_data.get("RequestDefinition"), RequestDefinitionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApiStepDefinition = ApiStepDefinition


@dataclass
class RequestHeadersDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestHeadersDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestHeadersDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestHeadersDefinition2 = RequestHeadersDefinition2


@dataclass
class RequestQueryDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestQueryDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestQueryDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestQueryDefinition2 = RequestQueryDefinition2


@dataclass
class AssertionDefinition(BaseModel):
    Operator: Optional[str]
    Property: Optional[str]
    Target: Optional[str]
    Type: Optional[str]
    Targetjsonpath: Optional[Sequence["_TargetjsonpathDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AssertionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AssertionDefinition"]:
        if not json_data:
            return None
        return cls(
            Operator=json_data.get("Operator"),
            Property=json_data.get("Property"),
            Target=json_data.get("Target"),
            Type=json_data.get("Type"),
            Targetjsonpath=deserialize_list(json_data.get("Targetjsonpath"), TargetjsonpathDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AssertionDefinition = AssertionDefinition


@dataclass
class TargetjsonpathDefinition(BaseModel):
    Jsonpath: Optional[str]
    Operator: Optional[str]
    Targetvalue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TargetjsonpathDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetjsonpathDefinition"]:
        if not json_data:
            return None
        return cls(
            Jsonpath=json_data.get("Jsonpath"),
            Operator=json_data.get("Operator"),
            Targetvalue=json_data.get("Targetvalue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetjsonpathDefinition = TargetjsonpathDefinition


@dataclass
class ExtractedValueDefinition(BaseModel):
    Field: Optional[str]
    Name: Optional[str]
    Type: Optional[str]
    Parser: Optional[Sequence["_ParserDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ExtractedValueDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtractedValueDefinition"]:
        if not json_data:
            return None
        return cls(
            Field=json_data.get("Field"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            Parser=deserialize_list(json_data.get("Parser"), ParserDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtractedValueDefinition = ExtractedValueDefinition


@dataclass
class ParserDefinition(BaseModel):
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParserDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParserDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParserDefinition = ParserDefinition


@dataclass
class RequestBasicauthDefinition(BaseModel):
    Password: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestBasicauthDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestBasicauthDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestBasicauthDefinition = RequestBasicauthDefinition


@dataclass
class RequestClientCertificateDefinition(BaseModel):
    Cert: Optional[Sequence["_CertDefinition"]]
    Key: Optional[Sequence["_KeyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RequestClientCertificateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestClientCertificateDefinition"]:
        if not json_data:
            return None
        return cls(
            Cert=deserialize_list(json_data.get("Cert"), CertDefinition),
            Key=deserialize_list(json_data.get("Key"), KeyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestClientCertificateDefinition = RequestClientCertificateDefinition


@dataclass
class CertDefinition(BaseModel):
    Content: Optional[str]
    Filename: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertDefinition"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
            Filename=json_data.get("Filename"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertDefinition = CertDefinition


@dataclass
class KeyDefinition(BaseModel):
    Content: Optional[str]
    Filename: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyDefinition"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
            Filename=json_data.get("Filename"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyDefinition = KeyDefinition


@dataclass
class RequestDefinitionDefinition(BaseModel):
    Body: Optional[str]
    DnsServer: Optional[str]
    DnsServerPort: Optional[float]
    Host: Optional[str]
    Method: Optional[str]
    NoSavingResponseBody: Optional[bool]
    NumberOfPackets: Optional[float]
    Port: Optional[float]
    ShouldTrackHops: Optional[bool]
    Timeout: Optional[float]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            Body=json_data.get("Body"),
            DnsServer=json_data.get("DnsServer"),
            DnsServerPort=json_data.get("DnsServerPort"),
            Host=json_data.get("Host"),
            Method=json_data.get("Method"),
            NoSavingResponseBody=json_data.get("NoSavingResponseBody"),
            NumberOfPackets=json_data.get("NumberOfPackets"),
            Port=json_data.get("Port"),
            ShouldTrackHops=json_data.get("ShouldTrackHops"),
            Timeout=json_data.get("Timeout"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestDefinitionDefinition = RequestDefinitionDefinition


@dataclass
class BrowserStepDefinition(BaseModel):
    AllowFailure: Optional[bool]
    ForceElementUpdate: Optional[bool]
    Name: Optional[str]
    Timeout: Optional[float]
    Type: Optional[str]
    Params: Optional[Sequence["_ParamsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BrowserStepDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BrowserStepDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowFailure=json_data.get("AllowFailure"),
            ForceElementUpdate=json_data.get("ForceElementUpdate"),
            Name=json_data.get("Name"),
            Timeout=json_data.get("Timeout"),
            Type=json_data.get("Type"),
            Params=deserialize_list(json_data.get("Params"), ParamsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BrowserStepDefinition = BrowserStepDefinition


@dataclass
class ParamsDefinition(BaseModel):
    Attribute: Optional[str]
    Check: Optional[str]
    ClickType: Optional[str]
    Code: Optional[str]
    Delay: Optional[float]
    Element: Optional[str]
    Email: Optional[str]
    File: Optional[str]
    Files: Optional[str]
    Modifiers: Optional[Sequence[str]]
    PlayingTabId: Optional[str]
    Request: Optional[str]
    SubtestPublicId: Optional[str]
    Value: Optional[str]
    WithClick: Optional[bool]
    X: Optional[float]
    Y: Optional[float]
    Variable: Optional[Sequence["_VariableDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            Attribute=json_data.get("Attribute"),
            Check=json_data.get("Check"),
            ClickType=json_data.get("ClickType"),
            Code=json_data.get("Code"),
            Delay=json_data.get("Delay"),
            Element=json_data.get("Element"),
            Email=json_data.get("Email"),
            File=json_data.get("File"),
            Files=json_data.get("Files"),
            Modifiers=json_data.get("Modifiers"),
            PlayingTabId=json_data.get("PlayingTabId"),
            Request=json_data.get("Request"),
            SubtestPublicId=json_data.get("SubtestPublicId"),
            Value=json_data.get("Value"),
            WithClick=json_data.get("WithClick"),
            X=json_data.get("X"),
            Y=json_data.get("Y"),
            Variable=deserialize_list(json_data.get("Variable"), VariableDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParamsDefinition = ParamsDefinition


@dataclass
class VariableDefinition(BaseModel):
    Example: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VariableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VariableDefinition"]:
        if not json_data:
            return None
        return cls(
            Example=json_data.get("Example"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VariableDefinition = VariableDefinition


@dataclass
class BrowserVariableDefinition(BaseModel):
    Example: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Pattern: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BrowserVariableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BrowserVariableDefinition"]:
        if not json_data:
            return None
        return cls(
            Example=json_data.get("Example"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Pattern=json_data.get("Pattern"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BrowserVariableDefinition = BrowserVariableDefinition


@dataclass
class ConfigVariableDefinition(BaseModel):
    Example: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Pattern: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigVariableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigVariableDefinition"]:
        if not json_data:
            return None
        return cls(
            Example=json_data.get("Example"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Pattern=json_data.get("Pattern"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigVariableDefinition = ConfigVariableDefinition


@dataclass
class OptionsListDefinition(BaseModel):
    AcceptSelfSigned: Optional[bool]
    AllowInsecure: Optional[bool]
    FollowRedirects: Optional[bool]
    MinFailureDuration: Optional[float]
    MinLocationFailed: Optional[float]
    MonitorName: Optional[str]
    MonitorPriority: Optional[float]
    NoScreenshot: Optional[bool]
    TickEvery: Optional[float]
    MonitorOptions: Optional[Sequence["_MonitorOptionsDefinition"]]
    Retry: Optional[Sequence["_RetryDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OptionsListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OptionsListDefinition"]:
        if not json_data:
            return None
        return cls(
            AcceptSelfSigned=json_data.get("AcceptSelfSigned"),
            AllowInsecure=json_data.get("AllowInsecure"),
            FollowRedirects=json_data.get("FollowRedirects"),
            MinFailureDuration=json_data.get("MinFailureDuration"),
            MinLocationFailed=json_data.get("MinLocationFailed"),
            MonitorName=json_data.get("MonitorName"),
            MonitorPriority=json_data.get("MonitorPriority"),
            NoScreenshot=json_data.get("NoScreenshot"),
            TickEvery=json_data.get("TickEvery"),
            MonitorOptions=deserialize_list(json_data.get("MonitorOptions"), MonitorOptionsDefinition),
            Retry=deserialize_list(json_data.get("Retry"), RetryDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OptionsListDefinition = OptionsListDefinition


@dataclass
class MonitorOptionsDefinition(BaseModel):
    RenotifyInterval: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MonitorOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MonitorOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            RenotifyInterval=json_data.get("RenotifyInterval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MonitorOptionsDefinition = MonitorOptionsDefinition


@dataclass
class RetryDefinition(BaseModel):
    Count: Optional[float]
    Interval: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RetryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetryDefinition"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
            Interval=json_data.get("Interval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetryDefinition = RetryDefinition


