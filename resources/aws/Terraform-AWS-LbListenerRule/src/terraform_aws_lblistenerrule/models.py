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
    Arn: Optional[str]
    Id: Optional[str]
    ListenerArn: Optional[str]
    Priority: Optional[float]
    Action: Optional[Sequence["_Action"]]
    Condition: Optional[Sequence["_Condition"]]
    AuthenticateCognito: Optional[Sequence["_AuthenticateCognito"]]
    AuthenticateOidc: Optional[Sequence["_AuthenticateOidc"]]
    FixedResponse: Optional[Sequence["_FixedResponse"]]
    Redirect: Optional[Sequence["_Redirect"]]
    HostHeader: Optional[Sequence["_HostHeader"]]
    HttpHeader: Optional[Sequence["_HttpHeader"]]
    HttpRequestMethod: Optional[Sequence["_HttpRequestMethod"]]
    PathPattern: Optional[Sequence["_PathPattern"]]
    QueryString: Optional[Sequence["_QueryString"]]
    SourceIp: Optional[Sequence["_SourceIp"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            Id=json_data.get("Id"),
            ListenerArn=json_data.get("ListenerArn"),
            Priority=json_data.get("Priority"),
            Action=json_data.get("Action"),
            Condition=json_data.get("Condition"),
            AuthenticateCognito=json_data.get("AuthenticateCognito"),
            AuthenticateOidc=json_data.get("AuthenticateOidc"),
            FixedResponse=json_data.get("FixedResponse"),
            Redirect=json_data.get("Redirect"),
            HostHeader=json_data.get("HostHeader"),
            HttpHeader=json_data.get("HttpHeader"),
            HttpRequestMethod=json_data.get("HttpRequestMethod"),
            PathPattern=json_data.get("PathPattern"),
            QueryString=json_data.get("QueryString"),
            SourceIp=json_data.get("SourceIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Action:
    Order: Optional[float]
    TargetGroupArn: Optional[str]
    Type: Optional[str]
    AuthenticateCognito: Optional[Sequence["_AuthenticateCognito"]]
    AuthenticateOidc: Optional[Sequence["_AuthenticateOidc"]]
    FixedResponse: Optional[Sequence["_FixedResponse"]]
    Redirect: Optional[Sequence["_Redirect"]]

    @classmethod
    def _deserialize(
        cls: Type["_Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Action"]:
        if not json_data:
            return None
        return cls(
            Order=json_data.get("Order"),
            TargetGroupArn=json_data.get("TargetGroupArn"),
            Type=json_data.get("Type"),
            AuthenticateCognito=json_data.get("AuthenticateCognito"),
            AuthenticateOidc=json_data.get("AuthenticateOidc"),
            FixedResponse=json_data.get("FixedResponse"),
            Redirect=json_data.get("Redirect"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Action = Action


@dataclass
class AuthenticateCognito:
    AuthenticationRequestExtraParams: Optional[Sequence["_AuthenticationRequestExtraParams"]]
    OnUnauthenticatedRequest: Optional[str]
    Scope: Optional[str]
    SessionCookieName: Optional[str]
    SessionTimeout: Optional[float]
    UserPoolArn: Optional[str]
    UserPoolClientId: Optional[str]
    UserPoolDomain: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthenticateCognito"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthenticateCognito"]:
        if not json_data:
            return None
        return cls(
            AuthenticationRequestExtraParams=json_data.get("AuthenticationRequestExtraParams"),
            OnUnauthenticatedRequest=json_data.get("OnUnauthenticatedRequest"),
            Scope=json_data.get("Scope"),
            SessionCookieName=json_data.get("SessionCookieName"),
            SessionTimeout=json_data.get("SessionTimeout"),
            UserPoolArn=json_data.get("UserPoolArn"),
            UserPoolClientId=json_data.get("UserPoolClientId"),
            UserPoolDomain=json_data.get("UserPoolDomain"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthenticateCognito = AuthenticateCognito


@dataclass
class AuthenticationRequestExtraParams:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthenticationRequestExtraParams"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthenticationRequestExtraParams"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthenticationRequestExtraParams = AuthenticationRequestExtraParams


@dataclass
class AuthenticateOidc:
    AuthenticationRequestExtraParams: Optional[Sequence["_AuthenticationRequestExtraParams2"]]
    AuthorizationEndpoint: Optional[str]
    ClientId: Optional[str]
    ClientSecret: Optional[str]
    Issuer: Optional[str]
    OnUnauthenticatedRequest: Optional[str]
    Scope: Optional[str]
    SessionCookieName: Optional[str]
    SessionTimeout: Optional[float]
    TokenEndpoint: Optional[str]
    UserInfoEndpoint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthenticateOidc"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthenticateOidc"]:
        if not json_data:
            return None
        return cls(
            AuthenticationRequestExtraParams=json_data.get("AuthenticationRequestExtraParams"),
            AuthorizationEndpoint=json_data.get("AuthorizationEndpoint"),
            ClientId=json_data.get("ClientId"),
            ClientSecret=json_data.get("ClientSecret"),
            Issuer=json_data.get("Issuer"),
            OnUnauthenticatedRequest=json_data.get("OnUnauthenticatedRequest"),
            Scope=json_data.get("Scope"),
            SessionCookieName=json_data.get("SessionCookieName"),
            SessionTimeout=json_data.get("SessionTimeout"),
            TokenEndpoint=json_data.get("TokenEndpoint"),
            UserInfoEndpoint=json_data.get("UserInfoEndpoint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthenticateOidc = AuthenticateOidc


@dataclass
class AuthenticationRequestExtraParams2:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthenticationRequestExtraParams2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthenticationRequestExtraParams2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthenticationRequestExtraParams2 = AuthenticationRequestExtraParams2


@dataclass
class FixedResponse:
    ContentType: Optional[str]
    MessageBody: Optional[str]
    StatusCode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FixedResponse"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FixedResponse"]:
        if not json_data:
            return None
        return cls(
            ContentType=json_data.get("ContentType"),
            MessageBody=json_data.get("MessageBody"),
            StatusCode=json_data.get("StatusCode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FixedResponse = FixedResponse


@dataclass
class Redirect:
    Host: Optional[str]
    Path: Optional[str]
    Port: Optional[str]
    Protocol: Optional[str]
    Query: Optional[str]
    StatusCode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Redirect"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Redirect"]:
        if not json_data:
            return None
        return cls(
            Host=json_data.get("Host"),
            Path=json_data.get("Path"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            Query=json_data.get("Query"),
            StatusCode=json_data.get("StatusCode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Redirect = Redirect


@dataclass
class Condition:
    Field: Optional[str]
    Values: Optional[Sequence[str]]
    HostHeader: Optional[Sequence["_HostHeader"]]
    HttpHeader: Optional[Sequence["_HttpHeader"]]
    HttpRequestMethod: Optional[Sequence["_HttpRequestMethod"]]
    PathPattern: Optional[Sequence["_PathPattern"]]
    QueryString: Optional[Sequence["_QueryString"]]
    SourceIp: Optional[Sequence["_SourceIp"]]

    @classmethod
    def _deserialize(
        cls: Type["_Condition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Condition"]:
        if not json_data:
            return None
        return cls(
            Field=json_data.get("Field"),
            Values=json_data.get("Values"),
            HostHeader=json_data.get("HostHeader"),
            HttpHeader=json_data.get("HttpHeader"),
            HttpRequestMethod=json_data.get("HttpRequestMethod"),
            PathPattern=json_data.get("PathPattern"),
            QueryString=json_data.get("QueryString"),
            SourceIp=json_data.get("SourceIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Condition = Condition


@dataclass
class HostHeader:
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_HostHeader"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostHeader"]:
        if not json_data:
            return None
        return cls(
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostHeader = HostHeader


@dataclass
class HttpHeader:
    HttpHeaderName: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpHeader"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpHeader"]:
        if not json_data:
            return None
        return cls(
            HttpHeaderName=json_data.get("HttpHeaderName"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpHeader = HttpHeader


@dataclass
class HttpRequestMethod:
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpRequestMethod"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpRequestMethod"]:
        if not json_data:
            return None
        return cls(
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpRequestMethod = HttpRequestMethod


@dataclass
class PathPattern:
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PathPattern"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PathPattern"]:
        if not json_data:
            return None
        return cls(
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PathPattern = PathPattern


@dataclass
class QueryString:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_QueryString"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryString"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryString = QueryString


@dataclass
class SourceIp:
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SourceIp"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceIp"]:
        if not json_data:
            return None
        return cls(
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceIp = SourceIp


