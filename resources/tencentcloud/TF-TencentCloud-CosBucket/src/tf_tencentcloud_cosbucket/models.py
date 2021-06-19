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
    Acl: Optional[str]
    Bucket: Optional[str]
    CosBucketUrl: Optional[str]
    EncryptionAlgorithm: Optional[str]
    Id: Optional[str]
    LogEnable: Optional[bool]
    LogPrefix: Optional[str]
    LogTargetBucket: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    VersioningEnable: Optional[bool]
    CorsRules: Optional[Sequence["_CorsRulesDefinition"]]
    LifecycleRules: Optional[Sequence["_LifecycleRulesDefinition"]]
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
            Acl=json_data.get("Acl"),
            Bucket=json_data.get("Bucket"),
            CosBucketUrl=json_data.get("CosBucketUrl"),
            EncryptionAlgorithm=json_data.get("EncryptionAlgorithm"),
            Id=json_data.get("Id"),
            LogEnable=json_data.get("LogEnable"),
            LogPrefix=json_data.get("LogPrefix"),
            LogTargetBucket=json_data.get("LogTargetBucket"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            VersioningEnable=json_data.get("VersioningEnable"),
            CorsRules=deserialize_list(json_data.get("CorsRules"), CorsRulesDefinition),
            LifecycleRules=deserialize_list(json_data.get("LifecycleRules"), LifecycleRulesDefinition),
            Website=deserialize_list(json_data.get("Website"), WebsiteDefinition),
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
class CorsRulesDefinition(BaseModel):
    AllowedHeaders: Optional[Sequence[str]]
    AllowedMethods: Optional[Sequence[str]]
    AllowedOrigins: Optional[Sequence[str]]
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
            AllowedMethods=json_data.get("AllowedMethods"),
            AllowedOrigins=json_data.get("AllowedOrigins"),
            ExposeHeaders=json_data.get("ExposeHeaders"),
            MaxAgeSeconds=json_data.get("MaxAgeSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CorsRulesDefinition = CorsRulesDefinition


@dataclass
class LifecycleRulesDefinition(BaseModel):
    FilterPrefix: Optional[str]
    Expiration: Optional[Sequence["_ExpirationDefinition"]]
    Transition: Optional[Sequence["_TransitionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LifecycleRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LifecycleRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            FilterPrefix=json_data.get("FilterPrefix"),
            Expiration=deserialize_list(json_data.get("Expiration"), ExpirationDefinition),
            Transition=deserialize_list(json_data.get("Transition"), TransitionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LifecycleRulesDefinition = LifecycleRulesDefinition


@dataclass
class ExpirationDefinition(BaseModel):
    Date: Optional[str]
    Days: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ExpirationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExpirationDefinition"]:
        if not json_data:
            return None
        return cls(
            Date=json_data.get("Date"),
            Days=json_data.get("Days"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExpirationDefinition = ExpirationDefinition


@dataclass
class TransitionDefinition(BaseModel):
    Date: Optional[str]
    Days: Optional[float]
    StorageClass: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TransitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TransitionDefinition"]:
        if not json_data:
            return None
        return cls(
            Date=json_data.get("Date"),
            Days=json_data.get("Days"),
            StorageClass=json_data.get("StorageClass"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TransitionDefinition = TransitionDefinition


@dataclass
class WebsiteDefinition(BaseModel):
    ErrorDocument: Optional[str]
    IndexDocument: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WebsiteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebsiteDefinition"]:
        if not json_data:
            return None
        return cls(
            ErrorDocument=json_data.get("ErrorDocument"),
            IndexDocument=json_data.get("IndexDocument"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebsiteDefinition = WebsiteDefinition


