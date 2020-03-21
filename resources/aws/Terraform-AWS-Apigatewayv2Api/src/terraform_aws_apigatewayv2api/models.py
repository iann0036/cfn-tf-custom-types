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
    ApiEndpoint: Optional[str]
    ApiKeySelectionExpression: Optional[str]
    Arn: Optional[str]
    Description: Optional[str]
    ExecutionArn: Optional[str]
    Name: Optional[str]
    ProtocolType: Optional[str]
    RouteSelectionExpression: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ApiEndpoint=json_data.get("ApiEndpoint"),
            ApiKeySelectionExpression=json_data.get("ApiKeySelectionExpression"),
            Arn=json_data.get("Arn"),
            Description=json_data.get("Description"),
            ExecutionArn=json_data.get("ExecutionArn"),
            Name=json_data.get("Name"),
            ProtocolType=json_data.get("ProtocolType"),
            RouteSelectionExpression=json_data.get("RouteSelectionExpression"),
            Tags=json_data.get("Tags"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


