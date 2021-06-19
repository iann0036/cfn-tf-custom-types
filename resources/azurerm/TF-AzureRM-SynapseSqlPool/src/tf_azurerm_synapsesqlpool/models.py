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
    Collation: Optional[str]
    CreateMode: Optional[str]
    DataEncrypted: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    RecoveryDatabaseId: Optional[str]
    SkuName: Optional[str]
    SynapseWorkspaceId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Restore: Optional[Sequence["_RestoreDefinition"]]
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
            Collation=json_data.get("Collation"),
            CreateMode=json_data.get("CreateMode"),
            DataEncrypted=json_data.get("DataEncrypted"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            RecoveryDatabaseId=json_data.get("RecoveryDatabaseId"),
            SkuName=json_data.get("SkuName"),
            SynapseWorkspaceId=json_data.get("SynapseWorkspaceId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Restore=deserialize_list(json_data.get("Restore"), RestoreDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class RestoreDefinition(BaseModel):
    PointInTime: Optional[str]
    SourceDatabaseId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RestoreDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RestoreDefinition"]:
        if not json_data:
            return None
        return cls(
            PointInTime=json_data.get("PointInTime"),
            SourceDatabaseId=json_data.get("SourceDatabaseId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RestoreDefinition = RestoreDefinition


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


