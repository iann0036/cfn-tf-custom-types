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
    ForceDestroy: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    State: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Configuration: Optional[Sequence["_ConfigurationDefinition"]]

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
            ForceDestroy=json_data.get("ForceDestroy"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            State=json_data.get("State"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Configuration=deserialize_list(json_data.get("Configuration"), ConfigurationDefinition),
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
    BytesScannedCutoffPerQuery: Optional[float]
    EnforceWorkgroupConfiguration: Optional[bool]
    PublishCloudwatchMetricsEnabled: Optional[bool]
    ResultConfiguration: Optional[Sequence["_ResultConfigurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            BytesScannedCutoffPerQuery=json_data.get("BytesScannedCutoffPerQuery"),
            EnforceWorkgroupConfiguration=json_data.get("EnforceWorkgroupConfiguration"),
            PublishCloudwatchMetricsEnabled=json_data.get("PublishCloudwatchMetricsEnabled"),
            ResultConfiguration=deserialize_list(json_data.get("ResultConfiguration"), ResultConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigurationDefinition = ConfigurationDefinition


@dataclass
class ResultConfigurationDefinition(BaseModel):
    OutputLocation: Optional[str]
    EncryptionConfiguration: Optional[Sequence["_EncryptionConfigurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResultConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResultConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            OutputLocation=json_data.get("OutputLocation"),
            EncryptionConfiguration=deserialize_list(json_data.get("EncryptionConfiguration"), EncryptionConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResultConfigurationDefinition = ResultConfigurationDefinition


@dataclass
class EncryptionConfigurationDefinition(BaseModel):
    EncryptionOption: Optional[str]
    KmsKeyArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            EncryptionOption=json_data.get("EncryptionOption"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionConfigurationDefinition = EncryptionConfigurationDefinition


