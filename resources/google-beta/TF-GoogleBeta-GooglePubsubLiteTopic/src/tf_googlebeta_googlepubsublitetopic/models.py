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
    Name: Optional[str]
    Project: Optional[str]
    Region: Optional[str]
    Zone: Optional[str]
    PartitionConfig: Optional[Sequence["_PartitionConfigDefinition"]]
    RetentionConfig: Optional[Sequence["_RetentionConfigDefinition"]]
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
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            Zone=json_data.get("Zone"),
            PartitionConfig=deserialize_list(json_data.get("PartitionConfig"), PartitionConfigDefinition),
            RetentionConfig=deserialize_list(json_data.get("RetentionConfig"), RetentionConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PartitionConfigDefinition(BaseModel):
    Count: Optional[float]
    Capacity: Optional[Sequence["_CapacityDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PartitionConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PartitionConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
            Capacity=deserialize_list(json_data.get("Capacity"), CapacityDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PartitionConfigDefinition = PartitionConfigDefinition


@dataclass
class CapacityDefinition(BaseModel):
    PublishMibPerSec: Optional[float]
    SubscribeMibPerSec: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CapacityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapacityDefinition"]:
        if not json_data:
            return None
        return cls(
            PublishMibPerSec=json_data.get("PublishMibPerSec"),
            SubscribeMibPerSec=json_data.get("SubscribeMibPerSec"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CapacityDefinition = CapacityDefinition


@dataclass
class RetentionConfigDefinition(BaseModel):
    PerPartitionBytes: Optional[str]
    Period: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RetentionConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetentionConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            PerPartitionBytes=json_data.get("PerPartitionBytes"),
            Period=json_data.get("Period"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetentionConfigDefinition = RetentionConfigDefinition


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


