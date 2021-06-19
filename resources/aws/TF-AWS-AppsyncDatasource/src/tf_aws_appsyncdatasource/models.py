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
    Arn: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    ServiceRoleArn: Optional[str]
    Type: Optional[str]
    DynamodbConfig: Optional[Sequence["_DynamodbConfigDefinition"]]
    ElasticsearchConfig: Optional[Sequence["_ElasticsearchConfigDefinition"]]
    HttpConfig: Optional[Sequence["_HttpConfigDefinition"]]
    LambdaConfig: Optional[Sequence["_LambdaConfigDefinition"]]

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
            Arn=json_data.get("Arn"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ServiceRoleArn=json_data.get("ServiceRoleArn"),
            Type=json_data.get("Type"),
            DynamodbConfig=deserialize_list(json_data.get("DynamodbConfig"), DynamodbConfigDefinition),
            ElasticsearchConfig=deserialize_list(json_data.get("ElasticsearchConfig"), ElasticsearchConfigDefinition),
            HttpConfig=deserialize_list(json_data.get("HttpConfig"), HttpConfigDefinition),
            LambdaConfig=deserialize_list(json_data.get("LambdaConfig"), LambdaConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DynamodbConfigDefinition(BaseModel):
    Region: Optional[str]
    TableName: Optional[str]
    UseCallerCredentials: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DynamodbConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynamodbConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Region=json_data.get("Region"),
            TableName=json_data.get("TableName"),
            UseCallerCredentials=json_data.get("UseCallerCredentials"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynamodbConfigDefinition = DynamodbConfigDefinition


@dataclass
class ElasticsearchConfigDefinition(BaseModel):
    Endpoint: Optional[str]
    Region: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ElasticsearchConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ElasticsearchConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Endpoint=json_data.get("Endpoint"),
            Region=json_data.get("Region"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ElasticsearchConfigDefinition = ElasticsearchConfigDefinition


@dataclass
class HttpConfigDefinition(BaseModel):
    Endpoint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Endpoint=json_data.get("Endpoint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpConfigDefinition = HttpConfigDefinition


@dataclass
class LambdaConfigDefinition(BaseModel):
    FunctionArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            FunctionArn=json_data.get("FunctionArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaConfigDefinition = LambdaConfigDefinition


