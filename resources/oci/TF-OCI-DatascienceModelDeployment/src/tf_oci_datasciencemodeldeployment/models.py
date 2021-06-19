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
    CompartmentId: Optional[str]
    CreatedBy: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    Description: Optional[str]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    LifecycleDetails: Optional[str]
    ModelDeploymentUrl: Optional[str]
    ProjectId: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    CategoryLogDetails: Optional[Sequence["_CategoryLogDetailsDefinition"]]
    ModelDeploymentConfigurationDetails: Optional[Sequence["_ModelDeploymentConfigurationDetailsDefinition"]]
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
            CompartmentId=json_data.get("CompartmentId"),
            CreatedBy=json_data.get("CreatedBy"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            ModelDeploymentUrl=json_data.get("ModelDeploymentUrl"),
            ProjectId=json_data.get("ProjectId"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            CategoryLogDetails=deserialize_list(json_data.get("CategoryLogDetails"), CategoryLogDetailsDefinition),
            ModelDeploymentConfigurationDetails=deserialize_list(json_data.get("ModelDeploymentConfigurationDetails"), ModelDeploymentConfigurationDetailsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTagsDefinition = DefinedTagsDefinition


@dataclass
class FreeformTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTagsDefinition = FreeformTagsDefinition


@dataclass
class CategoryLogDetailsDefinition(BaseModel):
    Access: Optional[Sequence["_AccessDefinition"]]
    Predict: Optional[Sequence["_PredictDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CategoryLogDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CategoryLogDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            Access=deserialize_list(json_data.get("Access"), AccessDefinition),
            Predict=deserialize_list(json_data.get("Predict"), PredictDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CategoryLogDetailsDefinition = CategoryLogDetailsDefinition


@dataclass
class AccessDefinition(BaseModel):
    LogGroupId: Optional[str]
    LogId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessDefinition"]:
        if not json_data:
            return None
        return cls(
            LogGroupId=json_data.get("LogGroupId"),
            LogId=json_data.get("LogId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessDefinition = AccessDefinition


@dataclass
class PredictDefinition(BaseModel):
    LogGroupId: Optional[str]
    LogId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PredictDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PredictDefinition"]:
        if not json_data:
            return None
        return cls(
            LogGroupId=json_data.get("LogGroupId"),
            LogId=json_data.get("LogId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PredictDefinition = PredictDefinition


@dataclass
class ModelDeploymentConfigurationDetailsDefinition(BaseModel):
    DeploymentType: Optional[str]
    ModelConfigurationDetails: Optional[Sequence["_ModelConfigurationDetailsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ModelDeploymentConfigurationDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ModelDeploymentConfigurationDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            DeploymentType=json_data.get("DeploymentType"),
            ModelConfigurationDetails=deserialize_list(json_data.get("ModelConfigurationDetails"), ModelConfigurationDetailsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ModelDeploymentConfigurationDetailsDefinition = ModelDeploymentConfigurationDetailsDefinition


@dataclass
class ModelConfigurationDetailsDefinition(BaseModel):
    BandwidthMbps: Optional[float]
    ModelId: Optional[str]
    InstanceConfiguration: Optional[Sequence["_InstanceConfigurationDefinition"]]
    ScalingPolicy: Optional[Sequence["_ScalingPolicyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ModelConfigurationDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ModelConfigurationDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            BandwidthMbps=json_data.get("BandwidthMbps"),
            ModelId=json_data.get("ModelId"),
            InstanceConfiguration=deserialize_list(json_data.get("InstanceConfiguration"), InstanceConfigurationDefinition),
            ScalingPolicy=deserialize_list(json_data.get("ScalingPolicy"), ScalingPolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ModelConfigurationDetailsDefinition = ModelConfigurationDetailsDefinition


@dataclass
class InstanceConfigurationDefinition(BaseModel):
    InstanceShapeName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            InstanceShapeName=json_data.get("InstanceShapeName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceConfigurationDefinition = InstanceConfigurationDefinition


@dataclass
class ScalingPolicyDefinition(BaseModel):
    InstanceCount: Optional[float]
    PolicyType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScalingPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScalingPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            InstanceCount=json_data.get("InstanceCount"),
            PolicyType=json_data.get("PolicyType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalingPolicyDefinition = ScalingPolicyDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


