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
    Arn: Optional[str]
    AuthorizationType: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    SecretArn: Optional[str]
    AuthParameters: Optional[Sequence["_AuthParametersDefinition"]]

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
            Arn=json_data.get("Arn"),
            AuthorizationType=json_data.get("AuthorizationType"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            SecretArn=json_data.get("SecretArn"),
            AuthParameters=deserialize_list(json_data.get("AuthParameters"), AuthParametersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AuthParametersDefinition(BaseModel):
    ApiKey: Optional[Sequence["_ApiKeyDefinition"]]
    Basic: Optional[Sequence["_BasicDefinition"]]
    InvocationHttpParameters: Optional[Sequence["_InvocationHttpParametersDefinition"]]
    Oauth: Optional[Sequence["_OauthDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AuthParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiKey=deserialize_list(json_data.get("ApiKey"), ApiKeyDefinition),
            Basic=deserialize_list(json_data.get("Basic"), BasicDefinition),
            InvocationHttpParameters=deserialize_list(json_data.get("InvocationHttpParameters"), InvocationHttpParametersDefinition),
            Oauth=deserialize_list(json_data.get("Oauth"), OauthDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthParametersDefinition = AuthParametersDefinition


@dataclass
class ApiKeyDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApiKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApiKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApiKeyDefinition = ApiKeyDefinition


@dataclass
class BasicDefinition(BaseModel):
    Password: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BasicDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BasicDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BasicDefinition = BasicDefinition


@dataclass
class InvocationHttpParametersDefinition(BaseModel):
    Body: Optional[Sequence["_BodyDefinition"]]
    Header: Optional[Sequence["_HeaderDefinition"]]
    QueryString: Optional[Sequence["_QueryStringDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InvocationHttpParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InvocationHttpParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            Body=deserialize_list(json_data.get("Body"), BodyDefinition),
            Header=deserialize_list(json_data.get("Header"), HeaderDefinition),
            QueryString=deserialize_list(json_data.get("QueryString"), QueryStringDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InvocationHttpParametersDefinition = InvocationHttpParametersDefinition


@dataclass
class BodyDefinition(BaseModel):
    IsValueSecret: Optional[bool]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BodyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BodyDefinition"]:
        if not json_data:
            return None
        return cls(
            IsValueSecret=json_data.get("IsValueSecret"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BodyDefinition = BodyDefinition


@dataclass
class HeaderDefinition(BaseModel):
    IsValueSecret: Optional[bool]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderDefinition"]:
        if not json_data:
            return None
        return cls(
            IsValueSecret=json_data.get("IsValueSecret"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeaderDefinition = HeaderDefinition


@dataclass
class QueryStringDefinition(BaseModel):
    IsValueSecret: Optional[bool]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_QueryStringDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryStringDefinition"]:
        if not json_data:
            return None
        return cls(
            IsValueSecret=json_data.get("IsValueSecret"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryStringDefinition = QueryStringDefinition


@dataclass
class OauthDefinition(BaseModel):
    AuthorizationEndpoint: Optional[str]
    HttpMethod: Optional[str]
    ClientParameters: Optional[Sequence["_ClientParametersDefinition"]]
    OauthHttpParameters: Optional[Sequence["_OauthHttpParametersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OauthDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OauthDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthorizationEndpoint=json_data.get("AuthorizationEndpoint"),
            HttpMethod=json_data.get("HttpMethod"),
            ClientParameters=deserialize_list(json_data.get("ClientParameters"), ClientParametersDefinition),
            OauthHttpParameters=deserialize_list(json_data.get("OauthHttpParameters"), OauthHttpParametersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OauthDefinition = OauthDefinition


@dataclass
class ClientParametersDefinition(BaseModel):
    ClientId: Optional[str]
    ClientSecret: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClientParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientId=json_data.get("ClientId"),
            ClientSecret=json_data.get("ClientSecret"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientParametersDefinition = ClientParametersDefinition


@dataclass
class OauthHttpParametersDefinition(BaseModel):
    Body: Optional[Sequence["_BodyDefinition"]]
    Header: Optional[Sequence["_HeaderDefinition"]]
    QueryString: Optional[Sequence["_QueryStringDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OauthHttpParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OauthHttpParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            Body=deserialize_list(json_data.get("Body"), BodyDefinition),
            Header=deserialize_list(json_data.get("Header"), HeaderDefinition),
            QueryString=deserialize_list(json_data.get("QueryString"), QueryStringDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OauthHttpParametersDefinition = OauthHttpParametersDefinition


