# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    Id: Optional[str]
    StorageAccountId: Optional[str]
    Rule: Optional[Sequence["_Rule"]]
    Timeouts: Optional["_Timeouts"]
    Actions: Optional[Sequence["_Actions"]]
    Filters: Optional[Sequence["_Filters"]]
    BaseBlob: Optional[Sequence["_BaseBlob"]]
    Snapshot: Optional[Sequence["_Snapshot"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Id=json_data.get("Id"),
            StorageAccountId=json_data.get("StorageAccountId"),
            Rule=json_data.get("Rule"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Actions=json_data.get("Actions"),
            Filters=json_data.get("Filters"),
            BaseBlob=json_data.get("BaseBlob"),
            Snapshot=json_data.get("Snapshot"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Rule:
    Enabled: Optional[bool]
    Name: Optional[str]
    Actions: Optional[Sequence["_Actions"]]
    Filters: Optional[Sequence["_Filters"]]

    @classmethod
    def _deserialize(
        cls: Type["_Rule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rule"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Name=json_data.get("Name"),
            Actions=json_data.get("Actions"),
            Filters=json_data.get("Filters"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rule = Rule


@dataclass
class Actions:
    BaseBlob: Optional[Sequence["_BaseBlob"]]
    Snapshot: Optional[Sequence["_Snapshot"]]

    @classmethod
    def _deserialize(
        cls: Type["_Actions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Actions"]:
        if not json_data:
            return None
        return cls(
            BaseBlob=json_data.get("BaseBlob"),
            Snapshot=json_data.get("Snapshot"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Actions = Actions


@dataclass
class BaseBlob:
    DeleteAfterDaysSinceModificationGreaterThan: Optional[float]
    TierToArchiveAfterDaysSinceModificationGreaterThan: Optional[float]
    TierToCoolAfterDaysSinceModificationGreaterThan: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_BaseBlob"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BaseBlob"]:
        if not json_data:
            return None
        return cls(
            DeleteAfterDaysSinceModificationGreaterThan=json_data.get("DeleteAfterDaysSinceModificationGreaterThan"),
            TierToArchiveAfterDaysSinceModificationGreaterThan=json_data.get("TierToArchiveAfterDaysSinceModificationGreaterThan"),
            TierToCoolAfterDaysSinceModificationGreaterThan=json_data.get("TierToCoolAfterDaysSinceModificationGreaterThan"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BaseBlob = BaseBlob


@dataclass
class Snapshot:
    DeleteAfterDaysSinceCreationGreaterThan: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Snapshot"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Snapshot"]:
        if not json_data:
            return None
        return cls(
            DeleteAfterDaysSinceCreationGreaterThan=json_data.get("DeleteAfterDaysSinceCreationGreaterThan"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Snapshot = Snapshot


@dataclass
class Filters:
    BlobTypes: Optional[Sequence[str]]
    PrefixMatch: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Filters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Filters"]:
        if not json_data:
            return None
        return cls(
            BlobTypes=json_data.get("BlobTypes"),
            PrefixMatch=json_data.get("PrefixMatch"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Filters = Filters


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


