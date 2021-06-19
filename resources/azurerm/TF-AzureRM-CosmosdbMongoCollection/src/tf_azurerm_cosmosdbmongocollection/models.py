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
    AnalyticalStorageTtl: Optional[float]
    DatabaseName: Optional[str]
    DefaultTtlSeconds: Optional[float]
    Id: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    ShardKey: Optional[str]
    SystemIndexes: Optional[Sequence["_SystemIndexesDefinition"]]
    Throughput: Optional[float]
    AutoscaleSettings: Optional[Sequence["_AutoscaleSettingsDefinition"]]
    Index: Optional[Sequence["_IndexDefinition"]]
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
            AccountName=json_data.get("AccountName"),
            AnalyticalStorageTtl=json_data.get("AnalyticalStorageTtl"),
            DatabaseName=json_data.get("DatabaseName"),
            DefaultTtlSeconds=json_data.get("DefaultTtlSeconds"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            ShardKey=json_data.get("ShardKey"),
            SystemIndexes=deserialize_list(json_data.get("SystemIndexes"), SystemIndexesDefinition),
            Throughput=json_data.get("Throughput"),
            AutoscaleSettings=deserialize_list(json_data.get("AutoscaleSettings"), AutoscaleSettingsDefinition),
            Index=deserialize_list(json_data.get("Index"), IndexDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SystemIndexesDefinition(BaseModel):
    Keys: Optional[Sequence[str]]
    Unique: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SystemIndexesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SystemIndexesDefinition"]:
        if not json_data:
            return None
        return cls(
            Keys=json_data.get("Keys"),
            Unique=json_data.get("Unique"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SystemIndexesDefinition = SystemIndexesDefinition


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
class IndexDefinition(BaseModel):
    Keys: Optional[Sequence[str]]
    Unique: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_IndexDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IndexDefinition"]:
        if not json_data:
            return None
        return cls(
            Keys=json_data.get("Keys"),
            Unique=json_data.get("Unique"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IndexDefinition = IndexDefinition


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


