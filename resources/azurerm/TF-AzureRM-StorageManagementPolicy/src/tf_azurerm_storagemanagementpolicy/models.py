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
    StorageAccountId: Optional[str]
    Rule: Optional[Sequence["_RuleDefinition"]]
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
            Id=json_data.get("Id"),
            StorageAccountId=json_data.get("StorageAccountId"),
            Rule=deserialize_list(json_data.get("Rule"), RuleDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RuleDefinition(BaseModel):
    Enabled: Optional[bool]
    Name: Optional[str]
    Actions: Optional[Sequence["_ActionsDefinition"]]
    Filters: Optional[Sequence["_FiltersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Name=json_data.get("Name"),
            Actions=deserialize_list(json_data.get("Actions"), ActionsDefinition),
            Filters=deserialize_list(json_data.get("Filters"), FiltersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleDefinition = RuleDefinition


@dataclass
class ActionsDefinition(BaseModel):
    BaseBlob: Optional[Sequence["_BaseBlobDefinition"]]
    Snapshot: Optional[Sequence["_SnapshotDefinition"]]
    Version: Optional[Sequence["_VersionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ActionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionsDefinition"]:
        if not json_data:
            return None
        return cls(
            BaseBlob=deserialize_list(json_data.get("BaseBlob"), BaseBlobDefinition),
            Snapshot=deserialize_list(json_data.get("Snapshot"), SnapshotDefinition),
            Version=deserialize_list(json_data.get("Version"), VersionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionsDefinition = ActionsDefinition


@dataclass
class BaseBlobDefinition(BaseModel):
    DeleteAfterDaysSinceModificationGreaterThan: Optional[float]
    TierToArchiveAfterDaysSinceModificationGreaterThan: Optional[float]
    TierToCoolAfterDaysSinceModificationGreaterThan: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_BaseBlobDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BaseBlobDefinition"]:
        if not json_data:
            return None
        return cls(
            DeleteAfterDaysSinceModificationGreaterThan=json_data.get("DeleteAfterDaysSinceModificationGreaterThan"),
            TierToArchiveAfterDaysSinceModificationGreaterThan=json_data.get("TierToArchiveAfterDaysSinceModificationGreaterThan"),
            TierToCoolAfterDaysSinceModificationGreaterThan=json_data.get("TierToCoolAfterDaysSinceModificationGreaterThan"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BaseBlobDefinition = BaseBlobDefinition


@dataclass
class SnapshotDefinition(BaseModel):
    ChangeTierToArchiveAfterDaysSinceCreation: Optional[float]
    ChangeTierToCoolAfterDaysSinceCreation: Optional[float]
    DeleteAfterDaysSinceCreationGreaterThan: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SnapshotDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnapshotDefinition"]:
        if not json_data:
            return None
        return cls(
            ChangeTierToArchiveAfterDaysSinceCreation=json_data.get("ChangeTierToArchiveAfterDaysSinceCreation"),
            ChangeTierToCoolAfterDaysSinceCreation=json_data.get("ChangeTierToCoolAfterDaysSinceCreation"),
            DeleteAfterDaysSinceCreationGreaterThan=json_data.get("DeleteAfterDaysSinceCreationGreaterThan"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnapshotDefinition = SnapshotDefinition


@dataclass
class VersionDefinition(BaseModel):
    ChangeTierToArchiveAfterDaysSinceCreation: Optional[float]
    ChangeTierToCoolAfterDaysSinceCreation: Optional[float]
    DeleteAfterDaysSinceCreation: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_VersionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersionDefinition"]:
        if not json_data:
            return None
        return cls(
            ChangeTierToArchiveAfterDaysSinceCreation=json_data.get("ChangeTierToArchiveAfterDaysSinceCreation"),
            ChangeTierToCoolAfterDaysSinceCreation=json_data.get("ChangeTierToCoolAfterDaysSinceCreation"),
            DeleteAfterDaysSinceCreation=json_data.get("DeleteAfterDaysSinceCreation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersionDefinition = VersionDefinition


@dataclass
class FiltersDefinition(BaseModel):
    BlobTypes: Optional[Sequence[str]]
    PrefixMatch: Optional[Sequence[str]]
    MatchBlobIndexTag: Optional[Sequence["_MatchBlobIndexTagDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FiltersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FiltersDefinition"]:
        if not json_data:
            return None
        return cls(
            BlobTypes=json_data.get("BlobTypes"),
            PrefixMatch=json_data.get("PrefixMatch"),
            MatchBlobIndexTag=deserialize_list(json_data.get("MatchBlobIndexTag"), MatchBlobIndexTagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FiltersDefinition = FiltersDefinition


@dataclass
class MatchBlobIndexTagDefinition(BaseModel):
    Name: Optional[str]
    Operation: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MatchBlobIndexTagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchBlobIndexTagDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Operation=json_data.get("Operation"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchBlobIndexTagDefinition = MatchBlobIndexTagDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


