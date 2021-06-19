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
    ApiKeyRequired: Optional[bool]
    Authorization: Optional[str]
    AuthorizationScopes: Optional[Sequence[str]]
    AuthorizerId: Optional[str]
    HttpMethod: Optional[str]
    Id: Optional[str]
    OperationName: Optional[str]
    RequestModels: Optional[Sequence["_RequestModelsDefinition"]]
    RequestParameters: Optional[Sequence["_RequestParametersDefinition"]]
    RequestValidatorId: Optional[str]
    ResourceId: Optional[str]
    RestApiId: Optional[str]

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
            ApiKeyRequired=json_data.get("ApiKeyRequired"),
            Authorization=json_data.get("Authorization"),
            AuthorizationScopes=json_data.get("AuthorizationScopes"),
            AuthorizerId=json_data.get("AuthorizerId"),
            HttpMethod=json_data.get("HttpMethod"),
            Id=json_data.get("Id"),
            OperationName=json_data.get("OperationName"),
            RequestModels=deserialize_list(json_data.get("RequestModels"), RequestModelsDefinition),
            RequestParameters=deserialize_list(json_data.get("RequestParameters"), RequestParametersDefinition),
            RequestValidatorId=json_data.get("RequestValidatorId"),
            ResourceId=json_data.get("ResourceId"),
            RestApiId=json_data.get("RestApiId"),
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
class RequestParametersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[bool]

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


