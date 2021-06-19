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
    Description: Optional[str]
    EventTimeFeatureName: Optional[str]
    FeatureGroupName: Optional[str]
    Id: Optional[str]
    RecordIdentifierFeatureName: Optional[str]
    RoleArn: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    FeatureDefinition: Optional[Sequence["_FeatureDefinitionDefinition"]]
    OfflineStoreConfig: Optional[Sequence["_OfflineStoreConfigDefinition"]]
    OnlineStoreConfig: Optional[Sequence["_OnlineStoreConfigDefinition"]]

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
            Description=json_data.get("Description"),
            EventTimeFeatureName=json_data.get("EventTimeFeatureName"),
            FeatureGroupName=json_data.get("FeatureGroupName"),
            Id=json_data.get("Id"),
            RecordIdentifierFeatureName=json_data.get("RecordIdentifierFeatureName"),
            RoleArn=json_data.get("RoleArn"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            FeatureDefinition=deserialize_list(json_data.get("FeatureDefinition"), FeatureDefinitionDefinition),
            OfflineStoreConfig=deserialize_list(json_data.get("OfflineStoreConfig"), OfflineStoreConfigDefinition),
            OnlineStoreConfig=deserialize_list(json_data.get("OnlineStoreConfig"), OnlineStoreConfigDefinition),
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
class FeatureDefinitionDefinition(BaseModel):
    FeatureName: Optional[str]
    FeatureType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FeatureDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FeatureDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            FeatureName=json_data.get("FeatureName"),
            FeatureType=json_data.get("FeatureType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FeatureDefinitionDefinition = FeatureDefinitionDefinition


@dataclass
class OfflineStoreConfigDefinition(BaseModel):
    DisableGlueTableCreation: Optional[bool]
    DataCatalogConfig: Optional[Sequence["_DataCatalogConfigDefinition"]]
    S3StorageConfig: Optional[Sequence["_S3StorageConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OfflineStoreConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OfflineStoreConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            DisableGlueTableCreation=json_data.get("DisableGlueTableCreation"),
            DataCatalogConfig=deserialize_list(json_data.get("DataCatalogConfig"), DataCatalogConfigDefinition),
            S3StorageConfig=deserialize_list(json_data.get("S3StorageConfig"), S3StorageConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OfflineStoreConfigDefinition = OfflineStoreConfigDefinition


@dataclass
class DataCatalogConfigDefinition(BaseModel):
    Catalog: Optional[str]
    Database: Optional[str]
    TableName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataCatalogConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataCatalogConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Catalog=json_data.get("Catalog"),
            Database=json_data.get("Database"),
            TableName=json_data.get("TableName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataCatalogConfigDefinition = DataCatalogConfigDefinition


@dataclass
class S3StorageConfigDefinition(BaseModel):
    KmsKeyId: Optional[str]
    S3Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3StorageConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3StorageConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            KmsKeyId=json_data.get("KmsKeyId"),
            S3Uri=json_data.get("S3Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3StorageConfigDefinition = S3StorageConfigDefinition


@dataclass
class OnlineStoreConfigDefinition(BaseModel):
    EnableOnlineStore: Optional[bool]
    SecurityConfig: Optional[Sequence["_SecurityConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OnlineStoreConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnlineStoreConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            EnableOnlineStore=json_data.get("EnableOnlineStore"),
            SecurityConfig=deserialize_list(json_data.get("SecurityConfig"), SecurityConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnlineStoreConfigDefinition = OnlineStoreConfigDefinition


@dataclass
class SecurityConfigDefinition(BaseModel):
    KmsKeyId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecurityConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecurityConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            KmsKeyId=json_data.get("KmsKeyId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecurityConfigDefinition = SecurityConfigDefinition


