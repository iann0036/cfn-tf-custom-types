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
    Arn: Optional[str]
    Classifiers: Optional[Sequence[str]]
    Configuration: Optional[str]
    DatabaseName: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Role: Optional[str]
    Schedule: Optional[str]
    SecurityConfiguration: Optional[str]
    TablePrefix: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    CatalogTarget: Optional[Sequence["_CatalogTarget"]]
    DynamodbTarget: Optional[Sequence["_DynamodbTarget"]]
    JdbcTarget: Optional[Sequence["_JdbcTarget"]]
    S3Target: Optional[Sequence["_S3Target"]]
    SchemaChangePolicy: Optional[Sequence["_SchemaChangePolicy"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            Classifiers=json_data.get("Classifiers"),
            Configuration=json_data.get("Configuration"),
            DatabaseName=json_data.get("DatabaseName"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Role=json_data.get("Role"),
            Schedule=json_data.get("Schedule"),
            SecurityConfiguration=json_data.get("SecurityConfiguration"),
            TablePrefix=json_data.get("TablePrefix"),
            Tags=json_data.get("Tags"),
            CatalogTarget=json_data.get("CatalogTarget"),
            DynamodbTarget=json_data.get("DynamodbTarget"),
            JdbcTarget=json_data.get("JdbcTarget"),
            S3Target=json_data.get("S3Target"),
            SchemaChangePolicy=json_data.get("SchemaChangePolicy"),
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
class CatalogTarget:
    DatabaseName: Optional[str]
    Tables: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CatalogTarget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CatalogTarget"]:
        if not json_data:
            return None
        return cls(
            DatabaseName=json_data.get("DatabaseName"),
            Tables=json_data.get("Tables"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CatalogTarget = CatalogTarget


@dataclass
class DynamodbTarget:
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DynamodbTarget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynamodbTarget"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynamodbTarget = DynamodbTarget


@dataclass
class JdbcTarget:
    ConnectionName: Optional[str]
    Exclusions: Optional[Sequence[str]]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JdbcTarget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JdbcTarget"]:
        if not json_data:
            return None
        return cls(
            ConnectionName=json_data.get("ConnectionName"),
            Exclusions=json_data.get("Exclusions"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JdbcTarget = JdbcTarget


@dataclass
class S3Target:
    Exclusions: Optional[Sequence[str]]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Target"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Target"]:
        if not json_data:
            return None
        return cls(
            Exclusions=json_data.get("Exclusions"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Target = S3Target


@dataclass
class SchemaChangePolicy:
    DeleteBehavior: Optional[str]
    UpdateBehavior: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SchemaChangePolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SchemaChangePolicy"]:
        if not json_data:
            return None
        return cls(
            DeleteBehavior=json_data.get("DeleteBehavior"),
            UpdateBehavior=json_data.get("UpdateBehavior"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SchemaChangePolicy = SchemaChangePolicy


