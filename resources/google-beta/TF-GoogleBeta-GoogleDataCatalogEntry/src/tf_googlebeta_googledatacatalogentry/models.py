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
    BigqueryDateShardedSpec: Optional[Sequence["_BigqueryDateShardedSpecDefinition"]]
    BigqueryTableSpec: Optional[Sequence["_BigqueryTableSpecDefinition3"]]
    Description: Optional[str]
    DisplayName: Optional[str]
    EntryGroup: Optional[str]
    EntryId: Optional[str]
    Id: Optional[str]
    IntegratedSystem: Optional[str]
    LinkedResource: Optional[str]
    Name: Optional[str]
    Schema: Optional[str]
    Type: Optional[str]
    UserSpecifiedSystem: Optional[str]
    UserSpecifiedType: Optional[str]
    GcsFilesetSpec: Optional[Sequence["_GcsFilesetSpecDefinition"]]
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
            BigqueryDateShardedSpec=deserialize_list(json_data.get("BigqueryDateShardedSpec"), BigqueryDateShardedSpecDefinition),
            BigqueryTableSpec=deserialize_list(json_data.get("BigqueryTableSpec"), BigqueryTableSpecDefinition3),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            EntryGroup=json_data.get("EntryGroup"),
            EntryId=json_data.get("EntryId"),
            Id=json_data.get("Id"),
            IntegratedSystem=json_data.get("IntegratedSystem"),
            LinkedResource=json_data.get("LinkedResource"),
            Name=json_data.get("Name"),
            Schema=json_data.get("Schema"),
            Type=json_data.get("Type"),
            UserSpecifiedSystem=json_data.get("UserSpecifiedSystem"),
            UserSpecifiedType=json_data.get("UserSpecifiedType"),
            GcsFilesetSpec=deserialize_list(json_data.get("GcsFilesetSpec"), GcsFilesetSpecDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BigqueryDateShardedSpecDefinition(BaseModel):
    Dataset: Optional[str]
    ShardCount: Optional[float]
    TablePrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BigqueryDateShardedSpecDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BigqueryDateShardedSpecDefinition"]:
        if not json_data:
            return None
        return cls(
            Dataset=json_data.get("Dataset"),
            ShardCount=json_data.get("ShardCount"),
            TablePrefix=json_data.get("TablePrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BigqueryDateShardedSpecDefinition = BigqueryDateShardedSpecDefinition


@dataclass
class BigqueryTableSpecDefinition3(BaseModel):
    TableSourceType: Optional[str]
    TableSpec: Optional[Sequence["_BigqueryTableSpecDefinition"]]
    ViewSpec: Optional[Sequence["_BigqueryTableSpecDefinition2"]]

    @classmethod
    def _deserialize(
        cls: Type["_BigqueryTableSpecDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BigqueryTableSpecDefinition3"]:
        if not json_data:
            return None
        return cls(
            TableSourceType=json_data.get("TableSourceType"),
            TableSpec=deserialize_list(json_data.get("TableSpec"), BigqueryTableSpecDefinition),
            ViewSpec=deserialize_list(json_data.get("ViewSpec"), BigqueryTableSpecDefinition2),
        )


# work around possible type aliasing issues when variable has same name as a model
_BigqueryTableSpecDefinition3 = BigqueryTableSpecDefinition3


@dataclass
class BigqueryTableSpecDefinition(BaseModel):
    GroupedEntry: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BigqueryTableSpecDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BigqueryTableSpecDefinition"]:
        if not json_data:
            return None
        return cls(
            GroupedEntry=json_data.get("GroupedEntry"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BigqueryTableSpecDefinition = BigqueryTableSpecDefinition


@dataclass
class BigqueryTableSpecDefinition2(BaseModel):
    ViewQuery: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BigqueryTableSpecDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BigqueryTableSpecDefinition2"]:
        if not json_data:
            return None
        return cls(
            ViewQuery=json_data.get("ViewQuery"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BigqueryTableSpecDefinition2 = BigqueryTableSpecDefinition2


@dataclass
class GcsFilesetSpecDefinition(BaseModel):
    FilePatterns: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_GcsFilesetSpecDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GcsFilesetSpecDefinition"]:
        if not json_data:
            return None
        return cls(
            FilePatterns=json_data.get("FilePatterns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GcsFilesetSpecDefinition = GcsFilesetSpecDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


