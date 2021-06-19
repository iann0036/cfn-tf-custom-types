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
    ApiId: Optional[str]
    AuthorizerCredentialsArn: Optional[str]
    AuthorizerPayloadFormatVersion: Optional[str]
    AuthorizerResultTtlInSeconds: Optional[float]
    AuthorizerType: Optional[str]
    AuthorizerUri: Optional[str]
    EnableSimpleResponses: Optional[bool]
    Id: Optional[str]
    IdentitySources: Optional[Sequence[str]]
    Name: Optional[str]
    JwtConfiguration: Optional[Sequence["_JwtConfigurationDefinition"]]

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
            ApiId=json_data.get("ApiId"),
            AuthorizerCredentialsArn=json_data.get("AuthorizerCredentialsArn"),
            AuthorizerPayloadFormatVersion=json_data.get("AuthorizerPayloadFormatVersion"),
            AuthorizerResultTtlInSeconds=json_data.get("AuthorizerResultTtlInSeconds"),
            AuthorizerType=json_data.get("AuthorizerType"),
            AuthorizerUri=json_data.get("AuthorizerUri"),
            EnableSimpleResponses=json_data.get("EnableSimpleResponses"),
            Id=json_data.get("Id"),
            IdentitySources=json_data.get("IdentitySources"),
            Name=json_data.get("Name"),
            JwtConfiguration=deserialize_list(json_data.get("JwtConfiguration"), JwtConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class JwtConfigurationDefinition(BaseModel):
    Audience: Optional[Sequence[str]]
    Issuer: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JwtConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JwtConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Audience=json_data.get("Audience"),
            Issuer=json_data.get("Issuer"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JwtConfigurationDefinition = JwtConfigurationDefinition


