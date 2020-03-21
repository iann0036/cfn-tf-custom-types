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
    CacheKeyParameters: Optional[Sequence[str]]
    CacheNamespace: Optional[str]
    ConnectionId: Optional[str]
    ConnectionType: Optional[str]
    ContentHandling: Optional[str]
    Credentials: Optional[str]
    HttpMethod: Optional[str]
    IntegrationHttpMethod: Optional[str]
    PassthroughBehavior: Optional[str]
    RequestParameters: Optional[Sequence["_RequestParameters"]]
    RequestParametersInJson: Optional[str]
    RequestTemplates: Optional[Sequence["_RequestTemplates"]]
    ResourceId: Optional[str]
    RestApiId: Optional[str]
    TimeoutMilliseconds: Optional[float]
    Type: Optional[str]
    Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CacheKeyParameters=json_data.get("CacheKeyParameters"),
            CacheNamespace=json_data.get("CacheNamespace"),
            ConnectionId=json_data.get("ConnectionId"),
            ConnectionType=json_data.get("ConnectionType"),
            ContentHandling=json_data.get("ContentHandling"),
            Credentials=json_data.get("Credentials"),
            HttpMethod=json_data.get("HttpMethod"),
            IntegrationHttpMethod=json_data.get("IntegrationHttpMethod"),
            PassthroughBehavior=json_data.get("PassthroughBehavior"),
            RequestParameters=json_data.get("RequestParameters"),
            RequestParametersInJson=json_data.get("RequestParametersInJson"),
            RequestTemplates=json_data.get("RequestTemplates"),
            ResourceId=json_data.get("ResourceId"),
            RestApiId=json_data.get("RestApiId"),
            TimeoutMilliseconds=json_data.get("TimeoutMilliseconds"),
            Type=json_data.get("Type"),
            Uri=json_data.get("Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RequestParameters:
    Key: Optional[str]
    Value: Optional[str]

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


@dataclass
class RequestTemplates:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestTemplates"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestTemplates"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestTemplates = RequestTemplates


