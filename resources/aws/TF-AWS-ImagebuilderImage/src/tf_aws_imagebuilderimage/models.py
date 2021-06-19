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
    DateCreated: Optional[str]
    DistributionConfigurationArn: Optional[str]
    EnhancedImageMetadataEnabled: Optional[bool]
    Id: Optional[str]
    ImageRecipeArn: Optional[str]
    InfrastructureConfigurationArn: Optional[str]
    Name: Optional[str]
    OsVersion: Optional[str]
    OutputResources: Optional[Sequence["_OutputResourcesDefinition2"]]
    Platform: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Version: Optional[str]
    ImageTestsConfiguration: Optional[Sequence["_ImageTestsConfigurationDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            DateCreated=json_data.get("DateCreated"),
            DistributionConfigurationArn=json_data.get("DistributionConfigurationArn"),
            EnhancedImageMetadataEnabled=json_data.get("EnhancedImageMetadataEnabled"),
            Id=json_data.get("Id"),
            ImageRecipeArn=json_data.get("ImageRecipeArn"),
            InfrastructureConfigurationArn=json_data.get("InfrastructureConfigurationArn"),
            Name=json_data.get("Name"),
            OsVersion=json_data.get("OsVersion"),
            OutputResources=deserialize_list(json_data.get("OutputResources"), OutputResourcesDefinition2),
            Platform=json_data.get("Platform"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Version=json_data.get("Version"),
            ImageTestsConfiguration=deserialize_list(json_data.get("ImageTestsConfiguration"), ImageTestsConfigurationDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class OutputResourcesDefinition2(BaseModel):
    Amis: Optional[Sequence["_OutputResourcesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OutputResourcesDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputResourcesDefinition2"]:
        if not json_data:
            return None
        return cls(
            Amis=deserialize_list(json_data.get("Amis"), OutputResourcesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutputResourcesDefinition2 = OutputResourcesDefinition2


@dataclass
class OutputResourcesDefinition(BaseModel):
    AccountId: Optional[str]
    Description: Optional[str]
    Image: Optional[str]
    Name: Optional[str]
    Region: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OutputResourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputResourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            AccountId=json_data.get("AccountId"),
            Description=json_data.get("Description"),
            Image=json_data.get("Image"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutputResourcesDefinition = OutputResourcesDefinition


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
class ImageTestsConfigurationDefinition(BaseModel):
    ImageTestsEnabled: Optional[bool]
    TimeoutMinutes: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ImageTestsConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImageTestsConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            ImageTestsEnabled=json_data.get("ImageTestsEnabled"),
            TimeoutMinutes=json_data.get("TimeoutMinutes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImageTestsConfigurationDefinition = ImageTestsConfigurationDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


