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
    ApiKeySource: Optional[str]
    Arn: Optional[str]
    BinaryMediaTypes: Optional[Sequence[str]]
    Body: Optional[str]
    CreatedDate: Optional[str]
    Description: Optional[str]
    ExecutionArn: Optional[str]
    Id: Optional[str]
    MinimumCompressionSize: Optional[float]
    Name: Optional[str]
    Policy: Optional[str]
    RootResourceId: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    EndpointConfiguration: Optional[Sequence["_EndpointConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ApiKeySource=json_data.get("ApiKeySource"),
            Arn=json_data.get("Arn"),
            BinaryMediaTypes=json_data.get("BinaryMediaTypes"),
            Body=json_data.get("Body"),
            CreatedDate=json_data.get("CreatedDate"),
            Description=json_data.get("Description"),
            ExecutionArn=json_data.get("ExecutionArn"),
            Id=json_data.get("Id"),
            MinimumCompressionSize=json_data.get("MinimumCompressionSize"),
            Name=json_data.get("Name"),
            Policy=json_data.get("Policy"),
            RootResourceId=json_data.get("RootResourceId"),
            Tags=json_data.get("Tags"),
            EndpointConfiguration=json_data.get("EndpointConfiguration"),
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


@dataclass
class EndpointConfiguration:
    Types: Optional[Sequence[str]]
    VpcEndpointIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointConfiguration"]:
        if not json_data:
            return None
        return cls(
            Types=json_data.get("Types"),
            VpcEndpointIds=json_data.get("VpcEndpointIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointConfiguration = EndpointConfiguration


