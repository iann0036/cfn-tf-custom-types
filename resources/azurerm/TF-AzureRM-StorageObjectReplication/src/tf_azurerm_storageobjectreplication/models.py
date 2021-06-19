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
    DestinationObjectReplicationId: Optional[str]
    DestinationStorageAccountId: Optional[str]
    Id: Optional[str]
    SourceObjectReplicationId: Optional[str]
    SourceStorageAccountId: Optional[str]
    Rules: Optional[Sequence["_RulesDefinition"]]
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
            DestinationObjectReplicationId=json_data.get("DestinationObjectReplicationId"),
            DestinationStorageAccountId=json_data.get("DestinationStorageAccountId"),
            Id=json_data.get("Id"),
            SourceObjectReplicationId=json_data.get("SourceObjectReplicationId"),
            SourceStorageAccountId=json_data.get("SourceStorageAccountId"),
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RulesDefinition(BaseModel):
    CopyBlobsCreatedAfter: Optional[str]
    DestinationContainerName: Optional[str]
    FilterOutBlobsWithPrefix: Optional[Sequence[str]]
    SourceContainerName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesDefinition"]:
        if not json_data:
            return None
        return cls(
            CopyBlobsCreatedAfter=json_data.get("CopyBlobsCreatedAfter"),
            DestinationContainerName=json_data.get("DestinationContainerName"),
            FilterOutBlobsWithPrefix=json_data.get("FilterOutBlobsWithPrefix"),
            SourceContainerName=json_data.get("SourceContainerName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesDefinition = RulesDefinition


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


