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
    ApiKeyRequired: Optional[bool]
    Authorization: Optional[str]
    AuthorizationScopes: Optional[Sequence[str]]
    AuthorizerId: Optional[str]
    HttpMethod: Optional[str]
    Id: Optional[str]
    RequestModels: Optional[Sequence["_RequestModels"]]
    RequestParameters: Optional[Sequence["_RequestParameters"]]
    RequestParametersInJson: Optional[str]
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
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ApiKeyRequired=json_data.get("ApiKeyRequired"),
            Authorization=json_data.get("Authorization"),
            AuthorizationScopes=json_data.get("AuthorizationScopes"),
            AuthorizerId=json_data.get("AuthorizerId"),
            HttpMethod=json_data.get("HttpMethod"),
            Id=json_data.get("Id"),
            RequestModels=json_data.get("RequestModels"),
            RequestParameters=json_data.get("RequestParameters"),
            RequestParametersInJson=json_data.get("RequestParametersInJson"),
            RequestValidatorId=json_data.get("RequestValidatorId"),
            ResourceId=json_data.get("ResourceId"),
            RestApiId=json_data.get("RestApiId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RequestModels:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestModels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestModels"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestModels = RequestModels


@dataclass
class RequestParameters:
    Key: Optional[str]
    Value: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RequestParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestParameters"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestParameters = RequestParameters


