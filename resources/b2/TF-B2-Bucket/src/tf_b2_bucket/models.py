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
    AccountId: Optional[str]
    BucketId: Optional[str]
    BucketInfo: Optional[Sequence["_BucketInfoDefinition"]]
    BucketName: Optional[str]
    BucketType: Optional[str]
    Id: Optional[str]
    Options: Optional[Sequence[str]]
    Revision: Optional[float]
    CorsRules: Optional[Sequence["_CorsRulesDefinition"]]
    DefaultServerSideEncryption: Optional[Sequence["_DefaultServerSideEncryptionDefinition"]]
    FileLockConfiguration: Optional[Sequence["_FileLockConfigurationDefinition"]]
    LifecycleRules: Optional[Sequence["_LifecycleRulesDefinition"]]

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
            AccountId=json_data.get("AccountId"),
            BucketId=json_data.get("BucketId"),
            BucketInfo=deserialize_list(json_data.get("BucketInfo"), BucketInfoDefinition),
            BucketName=json_data.get("BucketName"),
            BucketType=json_data.get("BucketType"),
            Id=json_data.get("Id"),
            Options=json_data.get("Options"),
            Revision=json_data.get("Revision"),
            CorsRules=deserialize_list(json_data.get("CorsRules"), CorsRulesDefinition),
            DefaultServerSideEncryption=deserialize_list(json_data.get("DefaultServerSideEncryption"), DefaultServerSideEncryptionDefinition),
            FileLockConfiguration=deserialize_list(json_data.get("FileLockConfiguration"), FileLockConfigurationDefinition),
            LifecycleRules=deserialize_list(json_data.get("LifecycleRules"), LifecycleRulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BucketInfoDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BucketInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BucketInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BucketInfoDefinition = BucketInfoDefinition


@dataclass
class CorsRulesDefinition(BaseModel):
    AllowedHeaders: Optional[Sequence[str]]
    AllowedOperations: Optional[Sequence[str]]
    AllowedOrigins: Optional[Sequence[str]]
    CorsRuleName: Optional[str]
    ExposeHeaders: Optional[Sequence[str]]
    MaxAgeSeconds: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CorsRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CorsRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowedHeaders=json_data.get("AllowedHeaders"),
            AllowedOperations=json_data.get("AllowedOperations"),
            AllowedOrigins=json_data.get("AllowedOrigins"),
            CorsRuleName=json_data.get("CorsRuleName"),
            ExposeHeaders=json_data.get("ExposeHeaders"),
            MaxAgeSeconds=json_data.get("MaxAgeSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CorsRulesDefinition = CorsRulesDefinition


@dataclass
class DefaultServerSideEncryptionDefinition(BaseModel):
    Algorithm: Optional[str]
    Mode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultServerSideEncryptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultServerSideEncryptionDefinition"]:
        if not json_data:
            return None
        return cls(
            Algorithm=json_data.get("Algorithm"),
            Mode=json_data.get("Mode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultServerSideEncryptionDefinition = DefaultServerSideEncryptionDefinition


@dataclass
class FileLockConfigurationDefinition(BaseModel):
    IsFileLockEnabled: Optional[bool]
    DefaultRetention: Optional[Sequence["_DefaultRetentionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FileLockConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FileLockConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            IsFileLockEnabled=json_data.get("IsFileLockEnabled"),
            DefaultRetention=deserialize_list(json_data.get("DefaultRetention"), DefaultRetentionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FileLockConfigurationDefinition = FileLockConfigurationDefinition


@dataclass
class DefaultRetentionDefinition(BaseModel):
    Mode: Optional[str]
    Period: Optional[Sequence["_PeriodDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultRetentionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultRetentionDefinition"]:
        if not json_data:
            return None
        return cls(
            Mode=json_data.get("Mode"),
            Period=deserialize_list(json_data.get("Period"), PeriodDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultRetentionDefinition = DefaultRetentionDefinition


@dataclass
class PeriodDefinition(BaseModel):
    Duration: Optional[float]
    Unit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PeriodDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PeriodDefinition"]:
        if not json_data:
            return None
        return cls(
            Duration=json_data.get("Duration"),
            Unit=json_data.get("Unit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PeriodDefinition = PeriodDefinition


@dataclass
class LifecycleRulesDefinition(BaseModel):
    DaysFromHidingToDeleting: Optional[float]
    DaysFromUploadingToHiding: Optional[float]
    FileNamePrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LifecycleRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LifecycleRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            DaysFromHidingToDeleting=json_data.get("DaysFromHidingToDeleting"),
            DaysFromUploadingToHiding=json_data.get("DaysFromUploadingToHiding"),
            FileNamePrefix=json_data.get("FileNamePrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LifecycleRulesDefinition = LifecycleRulesDefinition


