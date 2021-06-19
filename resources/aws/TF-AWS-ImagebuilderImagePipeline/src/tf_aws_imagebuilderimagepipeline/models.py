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
    DateLastRun: Optional[str]
    DateNextRun: Optional[str]
    DateUpdated: Optional[str]
    Description: Optional[str]
    DistributionConfigurationArn: Optional[str]
    EnhancedImageMetadataEnabled: Optional[bool]
    Id: Optional[str]
    ImageRecipeArn: Optional[str]
    InfrastructureConfigurationArn: Optional[str]
    Name: Optional[str]
    Platform: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    ImageTestsConfiguration: Optional[Sequence["_ImageTestsConfigurationDefinition"]]
    Schedule: Optional[Sequence["_ScheduleDefinition"]]

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
            DateLastRun=json_data.get("DateLastRun"),
            DateNextRun=json_data.get("DateNextRun"),
            DateUpdated=json_data.get("DateUpdated"),
            Description=json_data.get("Description"),
            DistributionConfigurationArn=json_data.get("DistributionConfigurationArn"),
            EnhancedImageMetadataEnabled=json_data.get("EnhancedImageMetadataEnabled"),
            Id=json_data.get("Id"),
            ImageRecipeArn=json_data.get("ImageRecipeArn"),
            InfrastructureConfigurationArn=json_data.get("InfrastructureConfigurationArn"),
            Name=json_data.get("Name"),
            Platform=json_data.get("Platform"),
            Status=json_data.get("Status"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            ImageTestsConfiguration=deserialize_list(json_data.get("ImageTestsConfiguration"), ImageTestsConfigurationDefinition),
            Schedule=deserialize_list(json_data.get("Schedule"), ScheduleDefinition),
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
class ScheduleDefinition(BaseModel):
    PipelineExecutionStartCondition: Optional[str]
    ScheduleExpression: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduleDefinition"]:
        if not json_data:
            return None
        return cls(
            PipelineExecutionStartCondition=json_data.get("PipelineExecutionStartCondition"),
            ScheduleExpression=json_data.get("ScheduleExpression"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduleDefinition = ScheduleDefinition


