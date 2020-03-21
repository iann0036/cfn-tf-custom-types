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
    Enabled: Optional[bool]
    Id: Optional[str]
    NetworkSecurityGroupId: Optional[str]
    NetworkWatcherName: Optional[str]
    ResourceGroupName: Optional[str]
    StorageAccountId: Optional[str]
    Version: Optional[float]
    RetentionPolicy: Optional[Sequence["_RetentionPolicy"]]
    Timeouts: Optional["_Timeouts"]
    TrafficAnalytics: Optional[Sequence["_TrafficAnalytics"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            NetworkSecurityGroupId=json_data.get("NetworkSecurityGroupId"),
            NetworkWatcherName=json_data.get("NetworkWatcherName"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            StorageAccountId=json_data.get("StorageAccountId"),
            Version=json_data.get("Version"),
            RetentionPolicy=json_data.get("RetentionPolicy"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            TrafficAnalytics=json_data.get("TrafficAnalytics"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RetentionPolicy:
    Days: Optional[float]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RetentionPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetentionPolicy"]:
        if not json_data:
            return None
        return cls(
            Days=json_data.get("Days"),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetentionPolicy = RetentionPolicy


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
class TrafficAnalytics:
    Enabled: Optional[bool]
    IntervalInMinutes: Optional[float]
    WorkspaceId: Optional[str]
    WorkspaceRegion: Optional[str]
    WorkspaceResourceId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TrafficAnalytics"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrafficAnalytics"]:
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
_TrafficAnalytics = TrafficAnalytics


