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
    AccountName: Optional[str]
    DatabaseName: Optional[str]
    DefaultTtl: Optional[float]
    Id: Optional[str]
    Name: Optional[str]
    PartitionKeyPath: Optional[str]
    PartitionKeyVersion: Optional[float]
    ResourceGroupName: Optional[str]
    Throughput: Optional[float]
    AutoscaleSettings: Optional[Sequence["_AutoscaleSettingsDefinition"]]
    ConflictResolutionPolicy: Optional[Sequence["_ConflictResolutionPolicyDefinition"]]
    IndexPolicy: Optional[Sequence["_IndexPolicyDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    UniqueKey: Optional[Sequence["_UniqueKeyDefinition"]]

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
            AccountName=json_data.get("AccountName"),
            DatabaseName=json_data.get("DatabaseName"),
            DefaultTtl=json_data.get("DefaultTtl"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PartitionKeyPath=json_data.get("PartitionKeyPath"),
            PartitionKeyVersion=json_data.get("PartitionKeyVersion"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Throughput=json_data.get("Throughput"),
            AutoscaleSettings=deserialize_list(json_data.get("AutoscaleSettings"), AutoscaleSettingsDefinition),
            ConflictResolutionPolicy=deserialize_list(json_data.get("ConflictResolutionPolicy"), ConflictResolutionPolicyDefinition),
            IndexPolicy=deserialize_list(json_data.get("IndexPolicy"), IndexPolicyDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            UniqueKey=deserialize_list(json_data.get("UniqueKey"), UniqueKeyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AutoscaleSettingsDefinition(BaseModel):
    MaxThroughput: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscaleSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscaleSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxThroughput=json_data.get("MaxThroughput"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscaleSettingsDefinition = AutoscaleSettingsDefinition


@dataclass
class ConflictResolutionPolicyDefinition(BaseModel):
    ConflictResolutionPath: Optional[str]
    ConflictResolutionProcedure: Optional[str]
    Mode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConflictResolutionPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConflictResolutionPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            ConflictResolutionPath=json_data.get("ConflictResolutionPath"),
            ConflictResolutionProcedure=json_data.get("ConflictResolutionProcedure"),
            Mode=json_data.get("Mode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConflictResolutionPolicyDefinition = ConflictResolutionPolicyDefinition


@dataclass
class IndexPolicyDefinition(BaseModel):
    Automatic: Optional[bool]
    ExcludedPaths: Optional[Sequence[str]]
    IncludedPaths: Optional[Sequence[str]]
    IndexingMode: Optional[str]
    CompositeIndex: Optional[Sequence["_CompositeIndexDefinition"]]
    SpatialIndex: Optional[Sequence["_SpatialIndexDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IndexPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IndexPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Automatic=json_data.get("Automatic"),
            ExcludedPaths=json_data.get("ExcludedPaths"),
            IncludedPaths=json_data.get("IncludedPaths"),
            IndexingMode=json_data.get("IndexingMode"),
            CompositeIndex=deserialize_list(json_data.get("CompositeIndex"), CompositeIndexDefinition),
            SpatialIndex=deserialize_list(json_data.get("SpatialIndex"), SpatialIndexDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IndexPolicyDefinition = IndexPolicyDefinition


@dataclass
class CompositeIndexDefinition(BaseModel):
    Index: Optional[Sequence["_IndexDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CompositeIndexDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CompositeIndexDefinition"]:
        if not json_data:
            return None
        return cls(
            Index=deserialize_list(json_data.get("Index"), IndexDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CompositeIndexDefinition = CompositeIndexDefinition


@dataclass
class IndexDefinition(BaseModel):
    Order: Optional[str]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IndexDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IndexDefinition"]:
        if not json_data:
            return None
        return cls(
            Order=json_data.get("Order"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IndexDefinition = IndexDefinition


@dataclass
class SpatialIndexDefinition(BaseModel):
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SpatialIndexDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpatialIndexDefinition"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpatialIndexDefinition = SpatialIndexDefinition


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


@dataclass
class UniqueKeyDefinition(BaseModel):
    Paths: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_UniqueKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UniqueKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            Paths=json_data.get("Paths"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UniqueKeyDefinition = UniqueKeyDefinition


