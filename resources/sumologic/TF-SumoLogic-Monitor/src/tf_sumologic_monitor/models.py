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
    ContentType: Optional[str]
    CreatedAt: Optional[str]
    CreatedBy: Optional[str]
    Description: Optional[str]
    GroupNotifications: Optional[bool]
    Id: Optional[str]
    IsDisabled: Optional[bool]
    IsLocked: Optional[bool]
    IsMutable: Optional[bool]
    IsSystem: Optional[bool]
    ModifiedAt: Optional[str]
    ModifiedBy: Optional[str]
    MonitorType: Optional[str]
    Name: Optional[str]
    ParentId: Optional[str]
    PostRequestMap: Optional[Sequence["_PostRequestMapDefinition"]]
    Status: Optional[Sequence[str]]
    Type: Optional[str]
    Version: Optional[float]
    Notifications: Optional[Sequence["_NotificationsDefinition"]]
    Queries: Optional[Sequence["_QueriesDefinition"]]
    Triggers: Optional[Sequence["_TriggersDefinition"]]

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
            ContentType=json_data.get("ContentType"),
            CreatedAt=json_data.get("CreatedAt"),
            CreatedBy=json_data.get("CreatedBy"),
            Description=json_data.get("Description"),
            GroupNotifications=json_data.get("GroupNotifications"),
            Id=json_data.get("Id"),
            IsDisabled=json_data.get("IsDisabled"),
            IsLocked=json_data.get("IsLocked"),
            IsMutable=json_data.get("IsMutable"),
            IsSystem=json_data.get("IsSystem"),
            ModifiedAt=json_data.get("ModifiedAt"),
            ModifiedBy=json_data.get("ModifiedBy"),
            MonitorType=json_data.get("MonitorType"),
            Name=json_data.get("Name"),
            ParentId=json_data.get("ParentId"),
            PostRequestMap=deserialize_list(json_data.get("PostRequestMap"), PostRequestMapDefinition),
            Status=json_data.get("Status"),
            Type=json_data.get("Type"),
            Version=json_data.get("Version"),
            Notifications=deserialize_list(json_data.get("Notifications"), NotificationsDefinition),
            Queries=deserialize_list(json_data.get("Queries"), QueriesDefinition),
            Triggers=deserialize_list(json_data.get("Triggers"), TriggersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PostRequestMapDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PostRequestMapDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PostRequestMapDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PostRequestMapDefinition = PostRequestMapDefinition


@dataclass
class NotificationsDefinition(BaseModel):
    RunForTriggerTypes: Optional[Sequence[str]]
    Notification: Optional[Sequence["_NotificationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationsDefinition"]:
        if not json_data:
            return None
        return cls(
            RunForTriggerTypes=json_data.get("RunForTriggerTypes"),
            Notification=deserialize_list(json_data.get("Notification"), NotificationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationsDefinition = NotificationsDefinition


@dataclass
class NotificationDefinition(BaseModel):
    ActionType: Optional[str]
    ConnectionId: Optional[str]
    ConnectionType: Optional[str]
    MessageBody: Optional[str]
    PayloadOverride: Optional[str]
    Recipients: Optional[Sequence[str]]
    Subject: Optional[str]
    TimeZone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationDefinition"]:
        if not json_data:
            return None
        return cls(
            ActionType=json_data.get("ActionType"),
            ConnectionId=json_data.get("ConnectionId"),
            ConnectionType=json_data.get("ConnectionType"),
            MessageBody=json_data.get("MessageBody"),
            PayloadOverride=json_data.get("PayloadOverride"),
            Recipients=json_data.get("Recipients"),
            Subject=json_data.get("Subject"),
            TimeZone=json_data.get("TimeZone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationDefinition = NotificationDefinition


@dataclass
class QueriesDefinition(BaseModel):
    Query: Optional[str]
    RowId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_QueriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueriesDefinition"]:
        if not json_data:
            return None
        return cls(
            Query=json_data.get("Query"),
            RowId=json_data.get("RowId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueriesDefinition = QueriesDefinition


@dataclass
class TriggersDefinition(BaseModel):
    DetectionMethod: Optional[str]
    OccurrenceType: Optional[str]
    Threshold: Optional[float]
    ThresholdType: Optional[str]
    TimeRange: Optional[str]
    TriggerSource: Optional[str]
    TriggerType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TriggersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TriggersDefinition"]:
        if not json_data:
            return None
        return cls(
            DetectionMethod=json_data.get("DetectionMethod"),
            OccurrenceType=json_data.get("OccurrenceType"),
            Threshold=json_data.get("Threshold"),
            ThresholdType=json_data.get("ThresholdType"),
            TimeRange=json_data.get("TimeRange"),
            TriggerSource=json_data.get("TriggerSource"),
            TriggerType=json_data.get("TriggerType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TriggersDefinition = TriggersDefinition


