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
    ApiId: Optional[str]
    Arn: Optional[str]
    Description: Optional[str]
    Name: Optional[str]
    ServiceRoleArn: Optional[str]
    Type: Optional[str]
    DynamodbConfig: Optional[Sequence["_DynamodbConfig"]]
    ElasticsearchConfig: Optional[Sequence["_ElasticsearchConfig"]]
    HttpConfig: Optional[Sequence["_HttpConfig"]]
    LambdaConfig: Optional[Sequence["_LambdaConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ApiId=json_data.get("ApiId"),
            Arn=json_data.get("Arn"),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            ServiceRoleArn=json_data.get("ServiceRoleArn"),
            Type=json_data.get("Type"),
            DynamodbConfig=json_data.get("DynamodbConfig"),
            ElasticsearchConfig=json_data.get("ElasticsearchConfig"),
            HttpConfig=json_data.get("HttpConfig"),
            LambdaConfig=json_data.get("LambdaConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DynamodbConfig:
    Region: Optional[str]
    TableName: Optional[str]
    UseCallerCredentials: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DynamodbConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynamodbConfig"]:
        if not json_data:
            return None
        return cls(
            Region=json_data.get("Region"),
            TableName=json_data.get("TableName"),
            UseCallerCredentials=json_data.get("UseCallerCredentials"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynamodbConfig = DynamodbConfig


@dataclass
class ElasticsearchConfig:
    Endpoint: Optional[str]
    Region: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ElasticsearchConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ElasticsearchConfig"]:
        if not json_data:
            return None
        return cls(
            Endpoint=json_data.get("Endpoint"),
            Region=json_data.get("Region"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ElasticsearchConfig = ElasticsearchConfig


@dataclass
class HttpConfig:
    Endpoint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpConfig"]:
        if not json_data:
            return None
        return cls(
            Endpoint=json_data.get("Endpoint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpConfig = HttpConfig


@dataclass
class LambdaConfig:
    FunctionArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaConfig"]:
        if not json_data:
            return None
        return cls(
            FunctionArn=json_data.get("FunctionArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaConfig = LambdaConfig


