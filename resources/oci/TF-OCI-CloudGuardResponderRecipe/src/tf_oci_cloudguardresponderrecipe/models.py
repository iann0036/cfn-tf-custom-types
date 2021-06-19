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
    EffectiveResponderRules: Optional[Sequence["_EffectiveResponderRulesDefinition3"]]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    LifecycleDetails: Optional[str]
    Owner: Optional[str]
    SourceResponderRecipeId: Optional[str]
    State: Optional[str]
    SystemTags: Optional[Sequence["_SystemTagsDefinition"]]
    TimeCreated: Optional[str]
    TimeUpdated: Optional[str]
    ResponderRules: Optional[Sequence["_ResponderRulesDefinition"]]
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
            EffectiveResponderRules=deserialize_list(json_data.get("EffectiveResponderRules"), EffectiveResponderRulesDefinition3),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            Owner=json_data.get("Owner"),
            SourceResponderRecipeId=json_data.get("SourceResponderRecipeId"),
            State=json_data.get("State"),
            SystemTags=deserialize_list(json_data.get("SystemTags"), SystemTagsDefinition),
            TimeCreated=json_data.get("TimeCreated"),
            TimeUpdated=json_data.get("TimeUpdated"),
            ResponderRules=deserialize_list(json_data.get("ResponderRules"), ResponderRulesDefinition),
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
class EffectiveResponderRulesDefinition3(BaseModel):
    CompartmentId: Optional[str]
    Description: Optional[str]
    Details: Optional[Sequence["_EffectiveResponderRulesDefinition2"]]
    DisplayName: Optional[str]
    LifecycleDetails: Optional[str]
    Policies: Optional[Sequence[str]]
    ResponderRuleId: Optional[str]
    State: Optional[str]
    SupportedModes: Optional[Sequence[str]]
    TimeCreated: Optional[str]
    TimeUpdated: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EffectiveResponderRulesDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EffectiveResponderRulesDefinition3"]:
        if not json_data:
            return None
        return cls(
            CompartmentId=json_data.get("CompartmentId"),
            Description=json_data.get("Description"),
            Details=deserialize_list(json_data.get("Details"), EffectiveResponderRulesDefinition2),
            DisplayName=json_data.get("DisplayName"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            Policies=json_data.get("Policies"),
            ResponderRuleId=json_data.get("ResponderRuleId"),
            State=json_data.get("State"),
            SupportedModes=json_data.get("SupportedModes"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeUpdated=json_data.get("TimeUpdated"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EffectiveResponderRulesDefinition3 = EffectiveResponderRulesDefinition3


@dataclass
class EffectiveResponderRulesDefinition2(BaseModel):
    Condition: Optional[str]
    Configurations: Optional[Sequence["_EffectiveResponderRulesDefinition"]]
    IsEnabled: Optional[bool]
    Mode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EffectiveResponderRulesDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EffectiveResponderRulesDefinition2"]:
        if not json_data:
            return None
        return cls(
            Condition=json_data.get("Condition"),
            Configurations=deserialize_list(json_data.get("Configurations"), EffectiveResponderRulesDefinition),
            IsEnabled=json_data.get("IsEnabled"),
            Mode=json_data.get("Mode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EffectiveResponderRulesDefinition2 = EffectiveResponderRulesDefinition2


@dataclass
class EffectiveResponderRulesDefinition(BaseModel):
    ConfigKey: Optional[str]
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EffectiveResponderRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EffectiveResponderRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            ConfigKey=json_data.get("ConfigKey"),
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EffectiveResponderRulesDefinition = EffectiveResponderRulesDefinition


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
class ResponderRulesDefinition(BaseModel):
    CompartmentId: Optional[str]
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
            CompartmentId=json_data.get("CompartmentId"),
            ResponderRuleId=json_data.get("ResponderRuleId"),
            Details=deserialize_list(json_data.get("Details"), DetailsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResponderRulesDefinition = ResponderRulesDefinition


@dataclass
class DetailsDefinition(BaseModel):
    IsEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DetailsDefinition = DetailsDefinition


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


