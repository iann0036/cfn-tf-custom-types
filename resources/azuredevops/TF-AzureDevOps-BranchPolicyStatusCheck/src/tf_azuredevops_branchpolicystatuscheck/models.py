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
    Blocking: Optional[bool]
    Enabled: Optional[bool]
    Id: Optional[str]
    ProjectId: Optional[str]
    Settings: Optional[Sequence["_SettingsDefinition"]]

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
            Blocking=json_data.get("Blocking"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            ProjectId=json_data.get("ProjectId"),
            Settings=deserialize_list(json_data.get("Settings"), SettingsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SettingsDefinition(BaseModel):
    Applicability: Optional[str]
    AuthorId: Optional[str]
    DisplayName: Optional[str]
    FilenamePatterns: Optional[Sequence[str]]
    InvalidateOnUpdate: Optional[bool]
    Name: Optional[str]
    Scope: Optional[Sequence["_ScopeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            Applicability=json_data.get("Applicability"),
            AuthorId=json_data.get("AuthorId"),
            DisplayName=json_data.get("DisplayName"),
            FilenamePatterns=json_data.get("FilenamePatterns"),
            InvalidateOnUpdate=json_data.get("InvalidateOnUpdate"),
            Name=json_data.get("Name"),
            Scope=deserialize_list(json_data.get("Scope"), ScopeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SettingsDefinition = SettingsDefinition


@dataclass
class ScopeDefinition(BaseModel):
    MatchType: Optional[str]
    RepositoryId: Optional[str]
    RepositoryRef: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScopeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScopeDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchType=json_data.get("MatchType"),
            RepositoryId=json_data.get("RepositoryId"),
            RepositoryRef=json_data.get("RepositoryRef"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScopeDefinition = ScopeDefinition

