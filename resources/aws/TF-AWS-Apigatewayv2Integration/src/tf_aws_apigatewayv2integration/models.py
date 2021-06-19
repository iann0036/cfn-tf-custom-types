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
    ConnectionId: Optional[str]
    ConnectionType: Optional[str]
    ContentHandlingStrategy: Optional[str]
    CredentialsArn: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    IntegrationMethod: Optional[str]
    IntegrationResponseSelectionExpression: Optional[str]
    IntegrationSubtype: Optional[str]
    IntegrationType: Optional[str]
    IntegrationUri: Optional[str]
    PassthroughBehavior: Optional[str]
    PayloadFormatVersion: Optional[str]
    RequestParameters: Optional[Sequence["_RequestParametersDefinition"]]
    RequestTemplates: Optional[Sequence["_RequestTemplatesDefinition"]]
    TemplateSelectionExpression: Optional[str]
    TimeoutMilliseconds: Optional[float]
    ResponseParameters: Optional[Sequence["_ResponseParametersDefinition"]]
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
            ApiId=json_data.get("ApiId"),
            ConnectionId=json_data.get("ConnectionId"),
            ConnectionType=json_data.get("ConnectionType"),
            ContentHandlingStrategy=json_data.get("ContentHandlingStrategy"),
            CredentialsArn=json_data.get("CredentialsArn"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            IntegrationMethod=json_data.get("IntegrationMethod"),
            IntegrationResponseSelectionExpression=json_data.get("IntegrationResponseSelectionExpression"),
            IntegrationSubtype=json_data.get("IntegrationSubtype"),
            IntegrationType=json_data.get("IntegrationType"),
            IntegrationUri=json_data.get("IntegrationUri"),
            PassthroughBehavior=json_data.get("PassthroughBehavior"),
            PayloadFormatVersion=json_data.get("PayloadFormatVersion"),
            RequestParameters=deserialize_list(json_data.get("RequestParameters"), RequestParametersDefinition),
            RequestTemplates=deserialize_list(json_data.get("RequestTemplates"), RequestTemplatesDefinition),
            TemplateSelectionExpression=json_data.get("TemplateSelectionExpression"),
            TimeoutMilliseconds=json_data.get("TimeoutMilliseconds"),
            ResponseParameters=deserialize_list(json_data.get("ResponseParameters"), ResponseParametersDefinition),
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
class ResponseParametersDefinition(BaseModel):
    Mappings: Optional[Sequence["_MappingsDefinition"]]
    StatusCode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResponseParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResponseParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            Mappings=deserialize_list(json_data.get("Mappings"), MappingsDefinition),
            StatusCode=json_data.get("StatusCode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResponseParametersDefinition = ResponseParametersDefinition


@dataclass
class MappingsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MappingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MappingsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MappingsDefinition = MappingsDefinition


@dataclass
class TlsConfigDefinition(BaseModel):
    ServerNameToVerify: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TlsConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TlsConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ServerNameToVerify=json_data.get("ServerNameToVerify"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TlsConfigDefinition = TlsConfigDefinition


