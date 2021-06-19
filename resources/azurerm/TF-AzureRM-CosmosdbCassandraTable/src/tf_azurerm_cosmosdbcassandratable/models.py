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
    AnalyticalStorageTtl: Optional[float]
    CassandraKeyspaceId: Optional[str]
    DefaultTtl: Optional[float]
    Id: Optional[str]
    Name: Optional[str]
    Throughput: Optional[float]
    AutoscaleSettings: Optional[Sequence["_AutoscaleSettingsDefinition"]]
    Schema: Optional[Sequence["_SchemaDefinition"]]
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
            AnalyticalStorageTtl=json_data.get("AnalyticalStorageTtl"),
            CassandraKeyspaceId=json_data.get("CassandraKeyspaceId"),
            DefaultTtl=json_data.get("DefaultTtl"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Throughput=json_data.get("Throughput"),
            AutoscaleSettings=deserialize_list(json_data.get("AutoscaleSettings"), AutoscaleSettingsDefinition),
            Schema=deserialize_list(json_data.get("Schema"), SchemaDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
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
class SchemaDefinition(BaseModel):
    ClusterKey: Optional[Sequence["_ClusterKeyDefinition"]]
    Column: Optional[Sequence["_ColumnDefinition"]]
    PartitionKey: Optional[Sequence["_PartitionKeyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SchemaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SchemaDefinition"]:
        if not json_data:
            return None
        return cls(
            ClusterKey=deserialize_list(json_data.get("ClusterKey"), ClusterKeyDefinition),
            Column=deserialize_list(json_data.get("Column"), ColumnDefinition),
            PartitionKey=deserialize_list(json_data.get("PartitionKey"), PartitionKeyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SchemaDefinition = SchemaDefinition


@dataclass
class ClusterKeyDefinition(BaseModel):
    Name: Optional[str]
    OrderBy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            OrderBy=json_data.get("OrderBy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterKeyDefinition = ClusterKeyDefinition


@dataclass
class ColumnDefinition(BaseModel):
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ColumnDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ColumnDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ColumnDefinition = ColumnDefinition


@dataclass
class PartitionKeyDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PartitionKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PartitionKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PartitionKeyDefinition = PartitionKeyDefinition


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


