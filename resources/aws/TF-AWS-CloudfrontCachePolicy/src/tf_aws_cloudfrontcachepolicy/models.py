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
    DefaultTtl: Optional[float]
    Etag: Optional[str]
    Id: Optional[str]
    MaxTtl: Optional[float]
    MinTtl: Optional[float]
    Name: Optional[str]
    ParametersInCacheKeyAndForwardedToOrigin: Optional[Sequence["_ParametersInCacheKeyAndForwardedToOriginDefinition"]]

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
            DefaultTtl=json_data.get("DefaultTtl"),
            Etag=json_data.get("Etag"),
            Id=json_data.get("Id"),
            MaxTtl=json_data.get("MaxTtl"),
            MinTtl=json_data.get("MinTtl"),
            Name=json_data.get("Name"),
            ParametersInCacheKeyAndForwardedToOrigin=deserialize_list(json_data.get("ParametersInCacheKeyAndForwardedToOrigin"), ParametersInCacheKeyAndForwardedToOriginDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ParametersInCacheKeyAndForwardedToOriginDefinition(BaseModel):
    EnableAcceptEncodingBrotli: Optional[bool]
    EnableAcceptEncodingGzip: Optional[bool]
    CookiesConfig: Optional[Sequence["_CookiesConfigDefinition"]]
    HeadersConfig: Optional[Sequence["_HeadersConfigDefinition"]]
    QueryStringsConfig: Optional[Sequence["_QueryStringsConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ParametersInCacheKeyAndForwardedToOriginDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParametersInCacheKeyAndForwardedToOriginDefinition"]:
        if not json_data:
            return None
        return cls(
            EnableAcceptEncodingBrotli=json_data.get("EnableAcceptEncodingBrotli"),
            EnableAcceptEncodingGzip=json_data.get("EnableAcceptEncodingGzip"),
            CookiesConfig=deserialize_list(json_data.get("CookiesConfig"), CookiesConfigDefinition),
            HeadersConfig=deserialize_list(json_data.get("HeadersConfig"), HeadersConfigDefinition),
            QueryStringsConfig=deserialize_list(json_data.get("QueryStringsConfig"), QueryStringsConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParametersInCacheKeyAndForwardedToOriginDefinition = ParametersInCacheKeyAndForwardedToOriginDefinition


@dataclass
class CookiesConfigDefinition(BaseModel):
    CookieBehavior: Optional[str]
    Cookies: Optional[Sequence["_CookiesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CookiesConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CookiesConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CookieBehavior=json_data.get("CookieBehavior"),
            Cookies=deserialize_list(json_data.get("Cookies"), CookiesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CookiesConfigDefinition = CookiesConfigDefinition


@dataclass
class CookiesDefinition(BaseModel):
    Items: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CookiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CookiesDefinition"]:
        if not json_data:
            return None
        return cls(
            Items=json_data.get("Items"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CookiesDefinition = CookiesDefinition


@dataclass
class HeadersConfigDefinition(BaseModel):
    HeaderBehavior: Optional[str]
    Headers: Optional[Sequence["_HeadersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            HeaderBehavior=json_data.get("HeaderBehavior"),
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersConfigDefinition = HeadersConfigDefinition


@dataclass
class HeadersDefinition(BaseModel):
    Items: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersDefinition"]:
        if not json_data:
            return None
        return cls(
            Items=json_data.get("Items"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersDefinition = HeadersDefinition


@dataclass
class QueryStringsConfigDefinition(BaseModel):
    QueryStringBehavior: Optional[str]
    QueryStrings: Optional[Sequence["_QueryStringsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_QueryStringsConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryStringsConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            QueryStringBehavior=json_data.get("QueryStringBehavior"),
            QueryStrings=deserialize_list(json_data.get("QueryStrings"), QueryStringsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryStringsConfigDefinition = QueryStringsConfigDefinition


@dataclass
class QueryStringsDefinition(BaseModel):
    Items: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_QueryStringsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryStringsDefinition"]:
        if not json_data:
            return None
        return cls(
            Items=json_data.get("Items"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryStringsDefinition = QueryStringsDefinition


