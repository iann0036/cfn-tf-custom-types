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
    Detector: Optional[str]
    DisplayName: Optional[str]
    EffectiveDetectorRules: Optional[Sequence["_EffectiveDetectorRulesDefinition5"]]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    Owner: Optional[str]
    SourceDetectorRecipeId: Optional[str]
    State: Optional[str]
    SystemTags: Optional[Sequence["_SystemTagsDefinition"]]
    TimeCreated: Optional[str]
    TimeUpdated: Optional[str]
    DetectorRules: Optional[Sequence["_DetectorRulesDefinition"]]
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
            Detector=json_data.get("Detector"),
            DisplayName=json_data.get("DisplayName"),
            EffectiveDetectorRules=deserialize_list(json_data.get("EffectiveDetectorRules"), EffectiveDetectorRulesDefinition5),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            Owner=json_data.get("Owner"),
            SourceDetectorRecipeId=json_data.get("SourceDetectorRecipeId"),
            State=json_data.get("State"),
            SystemTags=deserialize_list(json_data.get("SystemTags"), SystemTagsDefinition),
            TimeCreated=json_data.get("TimeCreated"),
            TimeUpdated=json_data.get("TimeUpdated"),
            DetectorRules=deserialize_list(json_data.get("DetectorRules"), DetectorRulesDefinition),
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
class EffectiveDetectorRulesDefinition5(BaseModel):
    CandidateResponderRules: Optional[Sequence["_EffectiveDetectorRulesDefinition"]]
    Description: Optional[str]
    Details: Optional[Sequence["_EffectiveDetectorRulesDefinition4"]]
    Detector: Optional[str]
    DetectorRuleId: Optional[str]
    DisplayName: Optional[str]
    LifecycleDetails: Optional[str]
    ManagedListTypes: Optional[Sequence[str]]
    Recommendation: Optional[str]
    ResourceType: Optional[str]
    ServiceType: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    TimeUpdated: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EffectiveDetectorRulesDefinition5"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EffectiveDetectorRulesDefinition5"]:
        if not json_data:
            return None
        return cls(
            CandidateResponderRules=deserialize_list(json_data.get("CandidateResponderRules"), EffectiveDetectorRulesDefinition),
            Description=json_data.get("Description"),
            Details=deserialize_list(json_data.get("Details"), EffectiveDetectorRulesDefinition4),
            Detector=json_data.get("Detector"),
            DetectorRuleId=json_data.get("DetectorRuleId"),
            DisplayName=json_data.get("DisplayName"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            ManagedListTypes=json_data.get("ManagedListTypes"),
            Recommendation=json_data.get("Recommendation"),
            ResourceType=json_data.get("ResourceType"),
            ServiceType=json_data.get("ServiceType"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeUpdated=json_data.get("TimeUpdated"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EffectiveDetectorRulesDefinition5 = EffectiveDetectorRulesDefinition5


@dataclass
class EffectiveDetectorRulesDefinition(BaseModel):
    DisplayName: Optional[str]
    Id: Optional[str]
    IsPreferred: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_EffectiveDetectorRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EffectiveDetectorRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            IsPreferred=json_data.get("IsPreferred"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EffectiveDetectorRulesDefinition = EffectiveDetectorRulesDefinition


@dataclass
class EffectiveDetectorRulesDefinition4(BaseModel):
    Condition: Optional[str]
    Configurations: Optional[Sequence["_EffectiveDetectorRulesDefinition3"]]
    IsConfigurationAllowed: Optional[bool]
    IsEnabled: Optional[bool]
    Labels: Optional[Sequence[str]]
    RiskLevel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EffectiveDetectorRulesDefinition4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EffectiveDetectorRulesDefinition4"]:
        if not json_data:
            return None
        return cls(
            Condition=json_data.get("Condition"),
            Configurations=deserialize_list(json_data.get("Configurations"), EffectiveDetectorRulesDefinition3),
            IsConfigurationAllowed=json_data.get("IsConfigurationAllowed"),
            IsEnabled=json_data.get("IsEnabled"),
            Labels=json_data.get("Labels"),
            RiskLevel=json_data.get("RiskLevel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EffectiveDetectorRulesDefinition4 = EffectiveDetectorRulesDefinition4


@dataclass
class EffectiveDetectorRulesDefinition3(BaseModel):
    ConfigKey: Optional[str]
    DataType: Optional[str]
    Name: Optional[str]
    Value: Optional[str]
    Values: Optional[Sequence["_EffectiveDetectorRulesDefinition2"]]

    @classmethod
    def _deserialize(
        cls: Type["_EffectiveDetectorRulesDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EffectiveDetectorRulesDefinition3"]:
        if not json_data:
            return None
        return cls(
            ConfigKey=json_data.get("ConfigKey"),
            DataType=json_data.get("DataType"),
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
            Values=deserialize_list(json_data.get("Values"), EffectiveDetectorRulesDefinition2),
        )


# work around possible type aliasing issues when variable has same name as a model
_EffectiveDetectorRulesDefinition3 = EffectiveDetectorRulesDefinition3


@dataclass
class EffectiveDetectorRulesDefinition2(BaseModel):
    ListType: Optional[str]
    ManagedListType: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EffectiveDetectorRulesDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EffectiveDetectorRulesDefinition2"]:
        if not json_data:
            return None
        return cls(
            ListType=json_data.get("ListType"),
            ManagedListType=json_data.get("ManagedListType"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EffectiveDetectorRulesDefinition2 = EffectiveDetectorRulesDefinition2


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
    IsEnabled: Optional[bool]
    Labels: Optional[Sequence[str]]
    RiskLevel: Optional[str]
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
            IsEnabled=json_data.get("IsEnabled"),
            Labels=json_data.get("Labels"),
            RiskLevel=json_data.get("RiskLevel"),
            Configurations=deserialize_list(json_data.get("Configurations"), ConfigurationsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DetailsDefinition = DetailsDefinition


@dataclass
class ConfigurationsDefinition(BaseModel):
    ConfigKey: Optional[str]
    DataType: Optional[str]
    Name: Optional[str]
    Value: Optional[str]
    Values: Optional[Sequence["_ValuesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigurationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigurationsDefinition"]:
        if not json_data:
            return None
        return cls(
            ConfigKey=json_data.get("ConfigKey"),
            DataType=json_data.get("DataType"),
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
            Values=deserialize_list(json_data.get("Values"), ValuesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigurationsDefinition = ConfigurationsDefinition


@dataclass
class ValuesDefinition(BaseModel):
    ListType: Optional[str]
    ManagedListType: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ValuesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValuesDefinition"]:
        if not json_data:
            return None
        return cls(
            ListType=json_data.get("ListType"),
            ManagedListType=json_data.get("ManagedListType"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValuesDefinition = ValuesDefinition


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


