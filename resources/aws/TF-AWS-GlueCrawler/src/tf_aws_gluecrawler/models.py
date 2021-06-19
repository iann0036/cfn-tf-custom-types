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
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    CatalogTarget: Optional[Sequence["_CatalogTargetDefinition"]]
    DynamodbTarget: Optional[Sequence["_DynamodbTargetDefinition"]]
    JdbcTarget: Optional[Sequence["_JdbcTargetDefinition"]]
    LineageConfiguration: Optional[Sequence["_LineageConfigurationDefinition"]]
    MongodbTarget: Optional[Sequence["_MongodbTargetDefinition"]]
    RecrawlPolicy: Optional[Sequence["_RecrawlPolicyDefinition"]]
    S3Target: Optional[Sequence["_S3TargetDefinition"]]
    SchemaChangePolicy: Optional[Sequence["_SchemaChangePolicyDefinition"]]

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
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            CatalogTarget=deserialize_list(json_data.get("CatalogTarget"), CatalogTargetDefinition),
            DynamodbTarget=deserialize_list(json_data.get("DynamodbTarget"), DynamodbTargetDefinition),
            JdbcTarget=deserialize_list(json_data.get("JdbcTarget"), JdbcTargetDefinition),
            LineageConfiguration=deserialize_list(json_data.get("LineageConfiguration"), LineageConfigurationDefinition),
            MongodbTarget=deserialize_list(json_data.get("MongodbTarget"), MongodbTargetDefinition),
            RecrawlPolicy=deserialize_list(json_data.get("RecrawlPolicy"), RecrawlPolicyDefinition),
            S3Target=deserialize_list(json_data.get("S3Target"), S3TargetDefinition),
            SchemaChangePolicy=deserialize_list(json_data.get("SchemaChangePolicy"), SchemaChangePolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class CatalogTargetDefinition(BaseModel):
    DatabaseName: Optional[str]
    Tables: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CatalogTargetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CatalogTargetDefinition"]:
        if not json_data:
            return None
        return cls(
            DatabaseName=json_data.get("DatabaseName"),
            Tables=json_data.get("Tables"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CatalogTargetDefinition = CatalogTargetDefinition


@dataclass
class DynamodbTargetDefinition(BaseModel):
    Path: Optional[str]
    ScanAll: Optional[bool]
    ScanRate: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DynamodbTargetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynamodbTargetDefinition"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            ScanAll=json_data.get("ScanAll"),
            ScanRate=json_data.get("ScanRate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynamodbTargetDefinition = DynamodbTargetDefinition


@dataclass
class JdbcTargetDefinition(BaseModel):
    ConnectionName: Optional[str]
    Exclusions: Optional[Sequence[str]]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JdbcTargetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JdbcTargetDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnectionName=json_data.get("ConnectionName"),
            Exclusions=json_data.get("Exclusions"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JdbcTargetDefinition = JdbcTargetDefinition


@dataclass
class LineageConfigurationDefinition(BaseModel):
    CrawlerLineageSettings: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LineageConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LineageConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            CrawlerLineageSettings=json_data.get("CrawlerLineageSettings"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LineageConfigurationDefinition = LineageConfigurationDefinition


@dataclass
class MongodbTargetDefinition(BaseModel):
    ConnectionName: Optional[str]
    Path: Optional[str]
    ScanAll: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_MongodbTargetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MongodbTargetDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnectionName=json_data.get("ConnectionName"),
            Path=json_data.get("Path"),
            ScanAll=json_data.get("ScanAll"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MongodbTargetDefinition = MongodbTargetDefinition


@dataclass
class RecrawlPolicyDefinition(BaseModel):
    RecrawlBehavior: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RecrawlPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecrawlPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            RecrawlBehavior=json_data.get("RecrawlBehavior"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecrawlPolicyDefinition = RecrawlPolicyDefinition


@dataclass
class S3TargetDefinition(BaseModel):
    ConnectionName: Optional[str]
    Exclusions: Optional[Sequence[str]]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3TargetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3TargetDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnectionName=json_data.get("ConnectionName"),
            Exclusions=json_data.get("Exclusions"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3TargetDefinition = S3TargetDefinition


@dataclass
class SchemaChangePolicyDefinition(BaseModel):
    DeleteBehavior: Optional[str]
    UpdateBehavior: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SchemaChangePolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SchemaChangePolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            DeleteBehavior=json_data.get("DeleteBehavior"),
            UpdateBehavior=json_data.get("UpdateBehavior"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SchemaChangePolicyDefinition = SchemaChangePolicyDefinition


