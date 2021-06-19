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
    ApiEndpoint: Optional[str]
    ApiKeySelectionExpression: Optional[str]
    Arn: Optional[str]
    Body: Optional[str]
    CredentialsArn: Optional[str]
    Description: Optional[str]
    DisableExecuteApiEndpoint: Optional[bool]
    ExecutionArn: Optional[str]
    FailOnWarnings: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    ProtocolType: Optional[str]
    RouteKey: Optional[str]
    RouteSelectionExpression: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Target: Optional[str]
    Version: Optional[str]
    CorsConfiguration: Optional[Sequence["_CorsConfigurationDefinition"]]

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
            ApiEndpoint=json_data.get("ApiEndpoint"),
            ApiKeySelectionExpression=json_data.get("ApiKeySelectionExpression"),
            Arn=json_data.get("Arn"),
            Body=json_data.get("Body"),
            CredentialsArn=json_data.get("CredentialsArn"),
            Description=json_data.get("Description"),
            DisableExecuteApiEndpoint=json_data.get("DisableExecuteApiEndpoint"),
            ExecutionArn=json_data.get("ExecutionArn"),
            FailOnWarnings=json_data.get("FailOnWarnings"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ProtocolType=json_data.get("ProtocolType"),
            RouteKey=json_data.get("RouteKey"),
            RouteSelectionExpression=json_data.get("RouteSelectionExpression"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Target=json_data.get("Target"),
            Version=json_data.get("Version"),
            CorsConfiguration=deserialize_list(json_data.get("CorsConfiguration"), CorsConfigurationDefinition),
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
class CorsConfigurationDefinition(BaseModel):
    AllowCredentials: Optional[bool]
    AllowHeaders: Optional[Sequence[str]]
    AllowMethods: Optional[Sequence[str]]
    AllowOrigins: Optional[Sequence[str]]
    ExposeHeaders: Optional[Sequence[str]]
    MaxAge: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CorsConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CorsConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowCredentials=json_data.get("AllowCredentials"),
            AllowHeaders=json_data.get("AllowHeaders"),
            AllowMethods=json_data.get("AllowMethods"),
            AllowOrigins=json_data.get("AllowOrigins"),
            ExposeHeaders=json_data.get("ExposeHeaders"),
            MaxAge=json_data.get("MaxAge"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CorsConfigurationDefinition = CorsConfigurationDefinition


