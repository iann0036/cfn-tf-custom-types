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
    HttpMethod: Optional[str]
    Id: Optional[str]
    ResourceId: Optional[str]
    ResponseModels: Optional[Sequence["_ResponseModelsDefinition"]]
    ResponseParameters: Optional[Sequence["_ResponseParametersDefinition"]]
    RestApiId: Optional[str]
    StatusCode: Optional[str]

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
            HttpMethod=json_data.get("HttpMethod"),
            Id=json_data.get("Id"),
            ResourceId=json_data.get("ResourceId"),
            ResponseModels=deserialize_list(json_data.get("ResponseModels"), ResponseModelsDefinition),
            ResponseParameters=deserialize_list(json_data.get("ResponseParameters"), ResponseParametersDefinition),
            RestApiId=json_data.get("RestApiId"),
            StatusCode=json_data.get("StatusCode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ResponseModelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResponseModelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResponseModelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResponseModelsDefinition = ResponseModelsDefinition


@dataclass
class ResponseParametersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ResponseParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResponseParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResponseParametersDefinition = ResponseParametersDefinition


