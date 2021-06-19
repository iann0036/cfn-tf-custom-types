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
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    Description: Optional[str]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    InheritedByCompartments: Optional[Sequence[str]]
    LifecyleDetails: Optional[str]
    RecipeCount: Optional[float]
    State: Optional[str]
    SystemTags: Optional[Sequence["_SystemTagsDefinition"]]
    TargetResourceId: Optional[str]
    TargetResourceType: Optional[str]
    TimeCreated: Optional[str]
    TimeUpdated: Optional[str]
    TargetDetectorRecipes: Optional[Sequence["_TargetDetectorRecipesDefinition"]]
    TargetResponderRecipes: Optional[Sequence["_TargetResponderRecipesDefinition"]]
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
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            InheritedByCompartments=json_data.get("InheritedByCompartments"),
            LifecyleDetails=json_data.get("LifecyleDetails"),
            RecipeCount=json_data.get("RecipeCount"),
            State=json_data.get("State"),
            SystemTags=deserialize_list(json_data.get("SystemTags"), SystemTagsDefinition),
            TargetResourceId=json_data.get("TargetResourceId"),
            TargetResourceType=json_data.get("TargetResourceType"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeUpdated=json_data.get("TimeUpdated"),
            TargetDetectorRecipes=deserialize_list(json_data.get("TargetDetectorRecipes"), TargetDetectorRecipesDefinition),
            TargetResponderRecipes=deserialize_list(json_data.get("TargetResponderRecipes"), TargetResponderRecipesDefinition),
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
class SystemTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SystemTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SystemTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SystemTagsDefinition = SystemTagsDefinition


@dataclass
class TargetDetectorRecipesDefinition(BaseModel):
    DetectorRecipeId: Optional[str]
    DetectorRules: Optional[Sequence["_DetectorRulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TargetDetectorRecipesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetDetectorRecipesDefinition"]:
        if not json_data:
            return None
        return cls(
            DetectorRecipeId=json_data.get("DetectorRecipeId"),
            DetectorRules=deserialize_list(json_data.get("DetectorRules"), DetectorRulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetDetectorRecipesDefinition = TargetDetectorRecipesDefinition


@dataclass
class DetectorRulesDefinition(BaseModel):
    DetectorRuleId: Optional[str]
    Details: Optional[Sequence["_DetailsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DetectorRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DetectorRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            DetectorRuleId=json_data.get("DetectorRuleId"),
            Details=deserialize_list(json_data.get("Details"), DetailsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DetectorRulesDefinition = DetectorRulesDefinition


@dataclass
class DetailsDefinition(BaseModel):
    Condition: Optional[str]
    Mode: Optional[str]
    Configurations: Optional[Sequence["_ConfigurationsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            Condition=json_data.get("Condition"),
            Mode=json_data.get("Mode"),
            Configurations=deserialize_list(json_data.get("Configurations"), ConfigurationsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DetailsDefinition = DetailsDefinition


@dataclass
class ConfigurationsDefinition(BaseModel):
    ConfigKey: Optional[str]
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigurationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigurationsDefinition"]:
        if not json_data:
            return None
        return cls(
            ConfigKey=json_data.get("ConfigKey"),
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigurationsDefinition = ConfigurationsDefinition


@dataclass
class TargetResponderRecipesDefinition(BaseModel):
    ResponderRecipeId: Optional[str]
    ResponderRules: Optional[Sequence["_ResponderRulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TargetResponderRecipesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetResponderRecipesDefinition"]:
        if not json_data:
            return None
        return cls(
            ResponderRecipeId=json_data.get("ResponderRecipeId"),
            ResponderRules=deserialize_list(json_data.get("ResponderRules"), ResponderRulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetResponderRecipesDefinition = TargetResponderRecipesDefinition


@dataclass
class ResponderRulesDefinition(BaseModel):
    ResponderRuleId: Optional[str]
    Details: Optional[Sequence["_DetailsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResponderRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResponderRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            ResponderRuleId=json_data.get("ResponderRuleId"),
            Details=deserialize_list(json_data.get("Details"), DetailsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResponderRulesDefinition = ResponderRulesDefinition


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


