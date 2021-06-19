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
    BucketPolicyOnly: Optional[bool]
    DefaultEventBasedHold: Optional[bool]
    ForceDestroy: Optional[bool]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Location: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    RequesterPays: Optional[bool]
    SelfLink: Optional[str]
    StorageClass: Optional[str]
    UniformBucketLevelAccess: Optional[bool]
    Url: Optional[str]
    Cors: Optional[Sequence["_CorsDefinition"]]
    Encryption: Optional[Sequence["_EncryptionDefinition"]]
    LifecycleRule: Optional[Sequence["_LifecycleRuleDefinition"]]
    Logging: Optional[Sequence["_LoggingDefinition"]]
    RetentionPolicy: Optional[Sequence["_RetentionPolicyDefinition"]]
    Versioning: Optional[Sequence["_VersioningDefinition"]]
    Website: Optional[Sequence["_WebsiteDefinition"]]

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
            BucketPolicyOnly=json_data.get("BucketPolicyOnly"),
            DefaultEventBasedHold=json_data.get("DefaultEventBasedHold"),
            ForceDestroy=json_data.get("ForceDestroy"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            RequesterPays=json_data.get("RequesterPays"),
            SelfLink=json_data.get("SelfLink"),
            StorageClass=json_data.get("StorageClass"),
            UniformBucketLevelAccess=json_data.get("UniformBucketLevelAccess"),
            Url=json_data.get("Url"),
            Cors=deserialize_list(json_data.get("Cors"), CorsDefinition),
            Encryption=deserialize_list(json_data.get("Encryption"), EncryptionDefinition),
            LifecycleRule=deserialize_list(json_data.get("LifecycleRule"), LifecycleRuleDefinition),
            Logging=deserialize_list(json_data.get("Logging"), LoggingDefinition),
            RetentionPolicy=deserialize_list(json_data.get("RetentionPolicy"), RetentionPolicyDefinition),
            Versioning=deserialize_list(json_data.get("Versioning"), VersioningDefinition),
            Website=deserialize_list(json_data.get("Website"), WebsiteDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class CorsDefinition(BaseModel):
    MaxAgeSeconds: Optional[float]
    Method: Optional[Sequence[str]]
    Origin: Optional[Sequence[str]]
    ResponseHeader: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CorsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CorsDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxAgeSeconds=json_data.get("MaxAgeSeconds"),
            Method=json_data.get("Method"),
            Origin=json_data.get("Origin"),
            ResponseHeader=json_data.get("ResponseHeader"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CorsDefinition = CorsDefinition


@dataclass
class EncryptionDefinition(BaseModel):
    DefaultKmsKeyName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultKmsKeyName=json_data.get("DefaultKmsKeyName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionDefinition = EncryptionDefinition


@dataclass
class LifecycleRuleDefinition(BaseModel):
    Action: Optional[Sequence["_ActionDefinition"]]
    Condition: Optional[Sequence["_ConditionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LifecycleRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LifecycleRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=deserialize_list(json_data.get("Action"), ActionDefinition),
            Condition=deserialize_list(json_data.get("Condition"), ConditionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LifecycleRuleDefinition = LifecycleRuleDefinition


@dataclass
class ActionDefinition(BaseModel):
    StorageClass: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionDefinition"]:
        if not json_data:
            return None
        return cls(
            StorageClass=json_data.get("StorageClass"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionDefinition = ActionDefinition


@dataclass
class ConditionDefinition(BaseModel):
    Age: Optional[float]
    CreatedBefore: Optional[str]
    CustomTimeBefore: Optional[str]
    DaysSinceCustomTime: Optional[float]
    DaysSinceNoncurrentTime: Optional[float]
    MatchesStorageClass: Optional[Sequence[str]]
    NoncurrentTimeBefore: Optional[str]
    NumNewerVersions: Optional[float]
    WithState: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            Age=json_data.get("Age"),
            CreatedBefore=json_data.get("CreatedBefore"),
            CustomTimeBefore=json_data.get("CustomTimeBefore"),
            DaysSinceCustomTime=json_data.get("DaysSinceCustomTime"),
            DaysSinceNoncurrentTime=json_data.get("DaysSinceNoncurrentTime"),
            MatchesStorageClass=json_data.get("MatchesStorageClass"),
            NoncurrentTimeBefore=json_data.get("NoncurrentTimeBefore"),
            NumNewerVersions=json_data.get("NumNewerVersions"),
            WithState=json_data.get("WithState"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionDefinition = ConditionDefinition


@dataclass
class LoggingDefinition(BaseModel):
    LogBucket: Optional[str]
    LogObjectPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingDefinition"]:
        if not json_data:
            return None
        return cls(
            LogBucket=json_data.get("LogBucket"),
            LogObjectPrefix=json_data.get("LogObjectPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingDefinition = LoggingDefinition


@dataclass
class RetentionPolicyDefinition(BaseModel):
    IsLocked: Optional[bool]
    RetentionPeriod: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RetentionPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetentionPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            IsLocked=json_data.get("IsLocked"),
            RetentionPeriod=json_data.get("RetentionPeriod"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetentionPolicyDefinition = RetentionPolicyDefinition


@dataclass
class VersioningDefinition(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_VersioningDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersioningDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersioningDefinition = VersioningDefinition


@dataclass
class WebsiteDefinition(BaseModel):
    MainPageSuffix: Optional[str]
    NotFoundPage: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WebsiteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebsiteDefinition"]:
        if not json_data:
            return None
        return cls(
            MainPageSuffix=json_data.get("MainPageSuffix"),
            NotFoundPage=json_data.get("NotFoundPage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebsiteDefinition = WebsiteDefinition


