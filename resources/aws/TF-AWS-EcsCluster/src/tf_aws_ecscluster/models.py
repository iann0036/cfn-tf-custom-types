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
    CapacityProviders: Optional[Sequence[str]]
    Id: Optional[str]
    Name: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Configuration: Optional[Sequence["_ConfigurationDefinition"]]
    DefaultCapacityProviderStrategy: Optional[Sequence["_DefaultCapacityProviderStrategyDefinition"]]
    Setting: Optional[Sequence["_SettingDefinition"]]

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
            CapacityProviders=json_data.get("CapacityProviders"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Configuration=deserialize_list(json_data.get("Configuration"), ConfigurationDefinition),
            DefaultCapacityProviderStrategy=deserialize_list(json_data.get("DefaultCapacityProviderStrategy"), DefaultCapacityProviderStrategyDefinition),
            Setting=deserialize_list(json_data.get("Setting"), SettingDefinition),
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
class ConfigurationDefinition(BaseModel):
    ExecuteCommandConfiguration: Optional[Sequence["_ExecuteCommandConfigurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            ExecuteCommandConfiguration=deserialize_list(json_data.get("ExecuteCommandConfiguration"), ExecuteCommandConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigurationDefinition = ConfigurationDefinition


@dataclass
class ExecuteCommandConfigurationDefinition(BaseModel):
    KmsKeyId: Optional[str]
    Logging: Optional[str]
    LogConfiguration: Optional[Sequence["_LogConfigurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ExecuteCommandConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExecuteCommandConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            KmsKeyId=json_data.get("KmsKeyId"),
            Logging=json_data.get("Logging"),
            LogConfiguration=deserialize_list(json_data.get("LogConfiguration"), LogConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExecuteCommandConfigurationDefinition = ExecuteCommandConfigurationDefinition


@dataclass
class LogConfigurationDefinition(BaseModel):
    CloudWatchEncryptionEnabled: Optional[bool]
    CloudWatchLogGroupName: Optional[str]
    S3BucketEncryptionEnabled: Optional[bool]
    S3BucketName: Optional[str]
    S3KeyPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            CloudWatchEncryptionEnabled=json_data.get("CloudWatchEncryptionEnabled"),
            CloudWatchLogGroupName=json_data.get("CloudWatchLogGroupName"),
            S3BucketEncryptionEnabled=json_data.get("S3BucketEncryptionEnabled"),
            S3BucketName=json_data.get("S3BucketName"),
            S3KeyPrefix=json_data.get("S3KeyPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogConfigurationDefinition = LogConfigurationDefinition


@dataclass
class DefaultCapacityProviderStrategyDefinition(BaseModel):
    Base: Optional[float]
    CapacityProvider: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultCapacityProviderStrategyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultCapacityProviderStrategyDefinition"]:
        if not json_data:
            return None
        return cls(
            Base=json_data.get("Base"),
            CapacityProvider=json_data.get("CapacityProvider"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultCapacityProviderStrategyDefinition = DefaultCapacityProviderStrategyDefinition


@dataclass
class SettingDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SettingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SettingDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SettingDefinition = SettingDefinition


