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
    Enabled: Optional[bool]
    Id: Optional[str]
    Location: Optional[str]
    NetworkSecurityGroupId: Optional[str]
    NetworkWatcherName: Optional[str]
    ResourceGroupName: Optional[str]
    StorageAccountId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Version: Optional[float]
    RetentionPolicy: Optional[Sequence["_RetentionPolicyDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    TrafficAnalytics: Optional[Sequence["_TrafficAnalyticsDefinition"]]

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
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            NetworkSecurityGroupId=json_data.get("NetworkSecurityGroupId"),
            NetworkWatcherName=json_data.get("NetworkWatcherName"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            StorageAccountId=json_data.get("StorageAccountId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Version=json_data.get("Version"),
            RetentionPolicy=deserialize_list(json_data.get("RetentionPolicy"), RetentionPolicyDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            TrafficAnalytics=deserialize_list(json_data.get("TrafficAnalytics"), TrafficAnalyticsDefinition),
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
class RetentionPolicyDefinition(BaseModel):
    Days: Optional[float]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RetentionPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetentionPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Days=json_data.get("Days"),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetentionPolicyDefinition = RetentionPolicyDefinition


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
class TrafficAnalyticsDefinition(BaseModel):
    Enabled: Optional[bool]
    IntervalInMinutes: Optional[float]
    WorkspaceId: Optional[str]
    WorkspaceRegion: Optional[str]
    WorkspaceResourceId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TrafficAnalyticsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrafficAnalyticsDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            IntervalInMinutes=json_data.get("IntervalInMinutes"),
            WorkspaceId=json_data.get("WorkspaceId"),
            WorkspaceRegion=json_data.get("WorkspaceRegion"),
            WorkspaceResourceId=json_data.get("WorkspaceResourceId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrafficAnalyticsDefinition = TrafficAnalyticsDefinition


