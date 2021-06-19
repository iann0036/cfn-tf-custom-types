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
    ApiKeyRequired: Optional[bool]
    AuthorizationScopes: Optional[Sequence[str]]
    AuthorizationType: Optional[str]
    AuthorizerId: Optional[str]
    Id: Optional[str]
    ModelSelectionExpression: Optional[str]
    OperationName: Optional[str]
    RequestModels: Optional[Sequence["_RequestModelsDefinition"]]
    RouteKey: Optional[str]
    RouteResponseSelectionExpression: Optional[str]
    Target: Optional[str]
    RequestParameter: Optional[Sequence["_RequestParameterDefinition"]]

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
            ApiKeyRequired=json_data.get("ApiKeyRequired"),
            AuthorizationScopes=json_data.get("AuthorizationScopes"),
            AuthorizationType=json_data.get("AuthorizationType"),
            AuthorizerId=json_data.get("AuthorizerId"),
            Id=json_data.get("Id"),
            ModelSelectionExpression=json_data.get("ModelSelectionExpression"),
            OperationName=json_data.get("OperationName"),
            RequestModels=deserialize_list(json_data.get("RequestModels"), RequestModelsDefinition),
            RouteKey=json_data.get("RouteKey"),
            RouteResponseSelectionExpression=json_data.get("RouteResponseSelectionExpression"),
            Target=json_data.get("Target"),
            RequestParameter=deserialize_list(json_data.get("RequestParameter"), RequestParameterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RequestModelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestModelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestModelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestModelsDefinition = RequestModelsDefinition


@dataclass
class RequestParameterDefinition(BaseModel):
    RequestParameterKey: Optional[str]
    Required: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RequestParameterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestParameterDefinition"]:
        if not json_data:
            return None
        return cls(
            RequestParameterKey=json_data.get("RequestParameterKey"),
            Required=json_data.get("Required"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestParameterDefinition = RequestParameterDefinition


