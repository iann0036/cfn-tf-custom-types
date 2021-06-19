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
    DisplayName: Optional[str]
    Id: Optional[str]
    MzId: Optional[str]
    Unknowns: Optional[str]
    EventTypeFilters: Optional[Sequence["_EventTypeFiltersDefinition"]]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Rules: Optional[Sequence["_RulesDefinition"]]

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
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            MzId=json_data.get("MzId"),
            Unknowns=json_data.get("Unknowns"),
            EventTypeFilters=deserialize_list(json_data.get("EventTypeFilters"), EventTypeFiltersDefinition),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EventTypeFiltersDefinition(BaseModel):
    Unknowns: Optional[str]
    CustomEventFilter: Optional[Sequence["_CustomEventFilterDefinition"]]
    PredefinedEventFilter: Optional[Sequence["_PredefinedEventFilterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EventTypeFiltersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventTypeFiltersDefinition"]:
        if not json_data:
            return None
        return cls(
            Unknowns=json_data.get("Unknowns"),
            CustomEventFilter=deserialize_list(json_data.get("CustomEventFilter"), CustomEventFilterDefinition),
            PredefinedEventFilter=deserialize_list(json_data.get("PredefinedEventFilter"), PredefinedEventFilterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventTypeFiltersDefinition = EventTypeFiltersDefinition


@dataclass
class CustomEventFilterDefinition(BaseModel):
    Unknowns: Optional[str]
    CustomDescriptionFilter: Optional[Sequence["_CustomDescriptionFilterDefinition"]]
    CustomTitleFilter: Optional[Sequence["_CustomTitleFilterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomEventFilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomEventFilterDefinition"]:
        if not json_data:
            return None
        return cls(
            Unknowns=json_data.get("Unknowns"),
            CustomDescriptionFilter=deserialize_list(json_data.get("CustomDescriptionFilter"), CustomDescriptionFilterDefinition),
            CustomTitleFilter=deserialize_list(json_data.get("CustomTitleFilter"), CustomTitleFilterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomEventFilterDefinition = CustomEventFilterDefinition


@dataclass
class CustomDescriptionFilterDefinition(BaseModel):
    CaseInsensitive: Optional[bool]
    Enabled: Optional[bool]
    Negate: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomDescriptionFilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomDescriptionFilterDefinition"]:
        if not json_data:
            return None
        return cls(
            CaseInsensitive=json_data.get("CaseInsensitive"),
            Enabled=json_data.get("Enabled"),
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomDescriptionFilterDefinition = CustomDescriptionFilterDefinition


@dataclass
class CustomTitleFilterDefinition(BaseModel):
    CaseInsensitive: Optional[bool]
    Enabled: Optional[bool]
    Negate: Optional[bool]
    Operator: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomTitleFilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomTitleFilterDefinition"]:
        if not json_data:
            return None
        return cls(
            CaseInsensitive=json_data.get("CaseInsensitive"),
            Enabled=json_data.get("Enabled"),
            Negate=json_data.get("Negate"),
            Operator=json_data.get("Operator"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomTitleFilterDefinition = CustomTitleFilterDefinition


@dataclass
class PredefinedEventFilterDefinition(BaseModel):
    EventType: Optional[str]
    Negate: Optional[bool]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PredefinedEventFilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PredefinedEventFilterDefinition"]:
        if not json_data:
            return None
        return cls(
            EventType=json_data.get("EventType"),
            Negate=json_data.get("Negate"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PredefinedEventFilterDefinition = PredefinedEventFilterDefinition


@dataclass
class MetadataDefinition(BaseModel):
    ClusterVersion: Optional[str]
    ConfigurationVersions: Optional[Sequence[float]]
    CurrentConfigurationVersions: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            ClusterVersion=json_data.get("ClusterVersion"),
            ConfigurationVersions=json_data.get("ConfigurationVersions"),
            CurrentConfigurationVersions=json_data.get("CurrentConfigurationVersions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


@dataclass
class RulesDefinition(BaseModel):
    DelayInMinutes: Optional[float]
    SeverityLevel: Optional[str]
    Unknowns: Optional[str]
    TagFilter: Optional[Sequence["_TagFilterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesDefinition"]:
        if not json_data:
            return None
        return cls(
            DelayInMinutes=json_data.get("DelayInMinutes"),
            SeverityLevel=json_data.get("SeverityLevel"),
            Unknowns=json_data.get("Unknowns"),
            TagFilter=deserialize_list(json_data.get("TagFilter"), TagFilterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesDefinition = RulesDefinition


@dataclass
class TagFilterDefinition(BaseModel):
    IncludeMode: Optional[str]
    Unknowns: Optional[str]
    TagFilters: Optional[Sequence["_TagFiltersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TagFilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagFilterDefinition"]:
        if not json_data:
            return None
        return cls(
            IncludeMode=json_data.get("IncludeMode"),
            Unknowns=json_data.get("Unknowns"),
            TagFilters=deserialize_list(json_data.get("TagFilters"), TagFiltersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagFilterDefinition = TagFilterDefinition


@dataclass
class TagFiltersDefinition(BaseModel):
    Context: Optional[str]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagFiltersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagFiltersDefinition"]:
        if not json_data:
            return None
        return cls(
            Context=json_data.get("Context"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagFiltersDefinition = TagFiltersDefinition


