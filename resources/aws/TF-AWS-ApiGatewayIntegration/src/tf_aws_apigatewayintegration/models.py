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
    CacheKeyParameters: Optional[Sequence[str]]
    CacheNamespace: Optional[str]
    ConnectionId: Optional[str]
    ConnectionType: Optional[str]
    ContentHandling: Optional[str]
    Credentials: Optional[str]
    HttpMethod: Optional[str]
    Id: Optional[str]
    IntegrationHttpMethod: Optional[str]
    PassthroughBehavior: Optional[str]
    RequestParameters: Optional[Sequence["_RequestParametersDefinition"]]
    RequestTemplates: Optional[Sequence["_RequestTemplatesDefinition"]]
    ResourceId: Optional[str]
    RestApiId: Optional[str]
    TimeoutMilliseconds: Optional[float]
    Type: Optional[str]
    Uri: Optional[str]
    TlsConfig: Optional[Sequence["_TlsConfigDefinition"]]

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
            CacheKeyParameters=json_data.get("CacheKeyParameters"),
            CacheNamespace=json_data.get("CacheNamespace"),
            ConnectionId=json_data.get("ConnectionId"),
            ConnectionType=json_data.get("ConnectionType"),
            ContentHandling=json_data.get("ContentHandling"),
            Credentials=json_data.get("Credentials"),
            HttpMethod=json_data.get("HttpMethod"),
            Id=json_data.get("Id"),
            IntegrationHttpMethod=json_data.get("IntegrationHttpMethod"),
            PassthroughBehavior=json_data.get("PassthroughBehavior"),
            RequestParameters=deserialize_list(json_data.get("RequestParameters"), RequestParametersDefinition),
            RequestTemplates=deserialize_list(json_data.get("RequestTemplates"), RequestTemplatesDefinition),
            ResourceId=json_data.get("ResourceId"),
            RestApiId=json_data.get("RestApiId"),
            TimeoutMilliseconds=json_data.get("TimeoutMilliseconds"),
            Type=json_data.get("Type"),
            Uri=json_data.get("Uri"),
            TlsConfig=deserialize_list(json_data.get("TlsConfig"), TlsConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RequestParametersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestParametersDefinition = RequestParametersDefinition


@dataclass
class RequestTemplatesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestTemplatesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestTemplatesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestTemplatesDefinition = RequestTemplatesDefinition


@dataclass
class TlsConfigDefinition(BaseModel):
    InsecureSkipVerification: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_TlsConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TlsConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            InsecureSkipVerification=json_data.get("InsecureSkipVerification"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TlsConfigDefinition = TlsConfigDefinition


