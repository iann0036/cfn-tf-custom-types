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
    AccountName: Optional[str]
    DatabaseName: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    PartitionKeyPath: Optional[str]
    ResourceGroupName: Optional[str]
    Throughput: Optional[float]
    ConflictResolutionPolicy: Optional[Sequence["_ConflictResolutionPolicy"]]
    IndexPolicy: Optional[Sequence["_IndexPolicy"]]
    Timeouts: Optional["_Timeouts"]
    UniqueKey: Optional[Sequence["_UniqueKey"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AccountName=json_data.get("AccountName"),
            DatabaseName=json_data.get("DatabaseName"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PartitionKeyPath=json_data.get("PartitionKeyPath"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Throughput=json_data.get("Throughput"),
            ConflictResolutionPolicy=json_data.get("ConflictResolutionPolicy"),
            IndexPolicy=json_data.get("IndexPolicy"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            UniqueKey=json_data.get("UniqueKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConflictResolutionPolicy:
    ConflictResolutionPath: Optional[str]
    ConflictResolutionProcedure: Optional[str]
    Mode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConflictResolutionPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConflictResolutionPolicy"]:
        if not json_data:
            return None
        return cls(
            ConflictResolutionPath=json_data.get("ConflictResolutionPath"),
            ConflictResolutionProcedure=json_data.get("ConflictResolutionProcedure"),
            Mode=json_data.get("Mode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConflictResolutionPolicy = ConflictResolutionPolicy


@dataclass
class IndexPolicy:
    Automatic: Optional[bool]
    ExcludedPaths: Optional[Sequence[str]]
    IncludedPaths: Optional[Sequence[str]]
    IndexingMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IndexPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IndexPolicy"]:
        if not json_data:
            return None
        return cls(
            Automatic=json_data.get("Automatic"),
            ExcludedPaths=json_data.get("ExcludedPaths"),
            IncludedPaths=json_data.get("IncludedPaths"),
            IndexingMode=json_data.get("IndexingMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IndexPolicy = IndexPolicy


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


@dataclass
class UniqueKey:
    Paths: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_UniqueKey"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UniqueKey"]:
        if not json_data:
            return None
        return cls(
            Paths=json_data.get("Paths"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UniqueKey = UniqueKey


