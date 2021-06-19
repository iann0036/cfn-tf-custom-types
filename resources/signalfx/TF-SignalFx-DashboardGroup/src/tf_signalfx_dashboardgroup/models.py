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
    AuthorizedWriterTeams: Optional[Sequence[str]]
    AuthorizedWriterUsers: Optional[Sequence[str]]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Teams: Optional[Sequence[str]]
    Dashboard: Optional[Sequence["_DashboardDefinition"]]
    ImportQualifier: Optional[Sequence["_ImportQualifierDefinition"]]

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
            AuthorizedWriterTeams=json_data.get("AuthorizedWriterTeams"),
            AuthorizedWriterUsers=json_data.get("AuthorizedWriterUsers"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Teams=json_data.get("Teams"),
            Dashboard=deserialize_list(json_data.get("Dashboard"), DashboardDefinition),
            ImportQualifier=deserialize_list(json_data.get("ImportQualifier"), ImportQualifierDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DashboardDefinition(BaseModel):
    DashboardId: Optional[str]
    DescriptionOverride: Optional[str]
    NameOverride: Optional[str]
    FilterOverride: Optional[Sequence["_FilterOverrideDefinition"]]
    VariableOverride: Optional[Sequence["_VariableOverrideDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DashboardDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DashboardDefinition"]:
        if not json_data:
            return None
        return cls(
            DashboardId=json_data.get("DashboardId"),
            DescriptionOverride=json_data.get("DescriptionOverride"),
            NameOverride=json_data.get("NameOverride"),
            FilterOverride=deserialize_list(json_data.get("FilterOverride"), FilterOverrideDefinition),
            VariableOverride=deserialize_list(json_data.get("VariableOverride"), VariableOverrideDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DashboardDefinition = DashboardDefinition


@dataclass
class FilterOverrideDefinition(BaseModel):
    Negated: Optional[bool]
    Property: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_FilterOverrideDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterOverrideDefinition"]:
        if not json_data:
            return None
        return cls(
            Negated=json_data.get("Negated"),
            Property=json_data.get("Property"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterOverrideDefinition = FilterOverrideDefinition


@dataclass
class VariableOverrideDefinition(BaseModel):
    Property: Optional[str]
    Values: Optional[Sequence[str]]
    ValuesSuggested: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VariableOverrideDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VariableOverrideDefinition"]:
        if not json_data:
            return None
        return cls(
            Property=json_data.get("Property"),
            Values=json_data.get("Values"),
            ValuesSuggested=json_data.get("ValuesSuggested"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VariableOverrideDefinition = VariableOverrideDefinition


@dataclass
class ImportQualifierDefinition(BaseModel):
    Metric: Optional[str]
    Filters: Optional[Sequence["_FiltersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ImportQualifierDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImportQualifierDefinition"]:
        if not json_data:
            return None
        return cls(
            Metric=json_data.get("Metric"),
            Filters=deserialize_list(json_data.get("Filters"), FiltersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImportQualifierDefinition = ImportQualifierDefinition


@dataclass
class FiltersDefinition(BaseModel):
    Negated: Optional[bool]
    Property: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_FiltersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FiltersDefinition"]:
        if not json_data:
            return None
        return cls(
            Negated=json_data.get("Negated"),
            Property=json_data.get("Property"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FiltersDefinition = FiltersDefinition


