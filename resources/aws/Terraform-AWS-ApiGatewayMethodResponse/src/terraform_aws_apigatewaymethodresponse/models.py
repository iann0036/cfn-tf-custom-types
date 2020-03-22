# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    HttpMethod: Optional[str]
    Id: Optional[str]
    ResourceId: Optional[str]
    ResponseModels: Optional[Sequence["_ResponseModels"]]
    ResponseParameters: Optional[Sequence["_ResponseParameters"]]
    ResponseParametersInJson: Optional[str]
    RestApiId: Optional[str]
    StatusCode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            HttpMethod=json_data.get("HttpMethod"),
            Id=json_data.get("Id"),
            ResourceId=json_data.get("ResourceId"),
            ResponseModels=json_data.get("ResponseModels"),
            ResponseParameters=json_data.get("ResponseParameters"),
            ResponseParametersInJson=json_data.get("ResponseParametersInJson"),
            RestApiId=json_data.get("RestApiId"),
            StatusCode=json_data.get("StatusCode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ResponseModels:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResponseModels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResponseModels"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResponseModels = ResponseModels


@dataclass
class ResponseParameters:
    MapKey: Optional[str]
    MapValue: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ResponseParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResponseParameters"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResponseParameters = ResponseParameters


