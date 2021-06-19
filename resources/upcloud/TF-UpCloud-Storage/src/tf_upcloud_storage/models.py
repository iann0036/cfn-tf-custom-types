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
    Id: Optional[str]
    Size: Optional[float]
    Tier: Optional[str]
    Title: Optional[str]
    Zone: Optional[str]
    BackupRule: Optional[Sequence["_BackupRuleDefinition"]]
    Clone: Optional[Sequence["_CloneDefinition"]]
    Import: Optional[Sequence["_ImportDefinition"]]

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
            Id=json_data.get("Id"),
            Size=json_data.get("Size"),
            Tier=json_data.get("Tier"),
            Title=json_data.get("Title"),
            Zone=json_data.get("Zone"),
            BackupRule=deserialize_list(json_data.get("BackupRule"), BackupRuleDefinition),
            Clone=deserialize_list(json_data.get("Clone"), CloneDefinition),
            Import=deserialize_list(json_data.get("Import"), ImportDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BackupRuleDefinition(BaseModel):
    Interval: Optional[str]
    Retention: Optional[float]
    Time: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BackupRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackupRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Interval=json_data.get("Interval"),
            Retention=json_data.get("Retention"),
            Time=json_data.get("Time"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackupRuleDefinition = BackupRuleDefinition


@dataclass
class CloneDefinition(BaseModel):
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloneDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloneDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloneDefinition = CloneDefinition


@dataclass
class ImportDefinition(BaseModel):
    Source: Optional[str]
    SourceHash: Optional[str]
    SourceLocation: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ImportDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImportDefinition"]:
        if not json_data:
            return None
        return cls(
            Source=json_data.get("Source"),
            SourceHash=json_data.get("SourceHash"),
            SourceLocation=json_data.get("SourceLocation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImportDefinition = ImportDefinition


