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
    AlpnPolicy: Optional[str]
    Arn: Optional[str]
    CertificateArn: Optional[str]
    Id: Optional[str]
    LoadBalancerArn: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]
    SslPolicy: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    DefaultAction: Optional[Sequence["_DefaultActionDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            AlpnPolicy=json_data.get("AlpnPolicy"),
            Arn=json_data.get("Arn"),
            CertificateArn=json_data.get("CertificateArn"),
            Id=json_data.get("Id"),
            LoadBalancerArn=json_data.get("LoadBalancerArn"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            SslPolicy=json_data.get("SslPolicy"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            DefaultAction=deserialize_list(json_data.get("DefaultAction"), DefaultActionDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class DefaultActionDefinition(BaseModel):
    Order: Optional[float]
    TargetGroupArn: Optional[str]
    Type: Optional[str]
    AuthenticateCognito: Optional[Sequence["_AuthenticateCognitoDefinition"]]
    AuthenticateOidc: Optional[Sequence["_AuthenticateOidcDefinition"]]
    FixedResponse: Optional[Sequence["_FixedResponseDefinition"]]
    Forward: Optional[Sequence["_ForwardDefinition"]]
    Redirect: Optional[Sequence["_RedirectDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Order=json_data.get("Order"),
            TargetGroupArn=json_data.get("TargetGroupArn"),
            Type=json_data.get("Type"),
            AuthenticateCognito=deserialize_list(json_data.get("AuthenticateCognito"), AuthenticateCognitoDefinition),
            AuthenticateOidc=deserialize_list(json_data.get("AuthenticateOidc"), AuthenticateOidcDefinition),
            FixedResponse=deserialize_list(json_data.get("FixedResponse"), FixedResponseDefinition),
            Forward=deserialize_list(json_data.get("Forward"), ForwardDefinition),
            Redirect=deserialize_list(json_data.get("Redirect"), RedirectDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultActionDefinition = DefaultActionDefinition


@dataclass
class AuthenticateCognitoDefinition(BaseModel):
    AuthenticationRequestExtraParams: Optional[Sequence["_AuthenticationRequestExtraParamsDefinition"]]
    OnUnauthenticatedRequest: Optional[str]
    Scope: Optional[str]
    SessionCookieName: Optional[str]
    SessionTimeout: Optional[float]
    UserPoolArn: Optional[str]
    UserPoolClientId: Optional[str]
    UserPoolDomain: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthenticateCognitoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthenticateCognitoDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthenticationRequestExtraParams=deserialize_list(json_data.get("AuthenticationRequestExtraParams"), AuthenticationRequestExtraParamsDefinition),
            OnUnauthenticatedRequest=json_data.get("OnUnauthenticatedRequest"),
            Scope=json_data.get("Scope"),
            SessionCookieName=json_data.get("SessionCookieName"),
            SessionTimeout=json_data.get("SessionTimeout"),
            UserPoolArn=json_data.get("UserPoolArn"),
            UserPoolClientId=json_data.get("UserPoolClientId"),
            UserPoolDomain=json_data.get("UserPoolDomain"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthenticateCognitoDefinition = AuthenticateCognitoDefinition


@dataclass
class AuthenticationRequestExtraParamsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthenticationRequestExtraParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthenticationRequestExtraParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthenticationRequestExtraParamsDefinition = AuthenticationRequestExtraParamsDefinition


@dataclass
class AuthenticateOidcDefinition(BaseModel):
    AuthenticationRequestExtraParams: Optional[Sequence["_AuthenticationRequestExtraParamsDefinition2"]]
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
        cls: Type["_AuthenticateOidcDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthenticateOidcDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthenticationRequestExtraParams=deserialize_list(json_data.get("AuthenticationRequestExtraParams"), AuthenticationRequestExtraParamsDefinition2),
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
_AuthenticateOidcDefinition = AuthenticateOidcDefinition


@dataclass
class AuthenticationRequestExtraParamsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthenticationRequestExtraParamsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthenticationRequestExtraParamsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthenticationRequestExtraParamsDefinition2 = AuthenticationRequestExtraParamsDefinition2


@dataclass
class FixedResponseDefinition(BaseModel):
    ContentType: Optional[str]
    MessageBody: Optional[str]
    StatusCode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FixedResponseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FixedResponseDefinition"]:
        if not json_data:
            return None
        return cls(
            ContentType=json_data.get("ContentType"),
            MessageBody=json_data.get("MessageBody"),
            StatusCode=json_data.get("StatusCode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FixedResponseDefinition = FixedResponseDefinition


@dataclass
class ForwardDefinition(BaseModel):
    Stickiness: Optional[Sequence["_StickinessDefinition"]]
    TargetGroup: Optional[Sequence["_TargetGroupDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ForwardDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForwardDefinition"]:
        if not json_data:
            return None
        return cls(
            Stickiness=deserialize_list(json_data.get("Stickiness"), StickinessDefinition),
            TargetGroup=deserialize_list(json_data.get("TargetGroup"), TargetGroupDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForwardDefinition = ForwardDefinition


@dataclass
class StickinessDefinition(BaseModel):
    Duration: Optional[float]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_StickinessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StickinessDefinition"]:
        if not json_data:
            return None
        return cls(
            Duration=json_data.get("Duration"),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StickinessDefinition = StickinessDefinition


@dataclass
class TargetGroupDefinition(BaseModel):
    Arn: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TargetGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetGroupDefinition = TargetGroupDefinition


@dataclass
class RedirectDefinition(BaseModel):
    Host: Optional[str]
    Path: Optional[str]
    Port: Optional[str]
    Protocol: Optional[str]
    Query: Optional[str]
    StatusCode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RedirectDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedirectDefinition"]:
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
_RedirectDefinition = RedirectDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Read: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Read=json_data.get("Read"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


