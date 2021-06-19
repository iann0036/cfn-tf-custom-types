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
    AlertDescription: Optional[str]
    AlertDisplayname: Optional[str]
    AlertName: Optional[str]
    Condition: Optional[str]
    Dashboard: Optional[str]
    Id: Optional[str]
    MuteUntil: Optional[float]
    NotifyThreshold: Optional[float]
    ProjectName: Optional[str]
    ScheduleInterval: Optional[str]
    ScheduleType: Optional[str]
    Throttling: Optional[str]
    NotificationList: Optional[Sequence["_NotificationListDefinition"]]
    QueryList: Optional[Sequence["_QueryListDefinition"]]

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
            AlertDescription=json_data.get("AlertDescription"),
            AlertDisplayname=json_data.get("AlertDisplayname"),
            AlertName=json_data.get("AlertName"),
            Condition=json_data.get("Condition"),
            Dashboard=json_data.get("Dashboard"),
            Id=json_data.get("Id"),
            MuteUntil=json_data.get("MuteUntil"),
            NotifyThreshold=json_data.get("NotifyThreshold"),
            ProjectName=json_data.get("ProjectName"),
            ScheduleInterval=json_data.get("ScheduleInterval"),
            ScheduleType=json_data.get("ScheduleType"),
            Throttling=json_data.get("Throttling"),
            NotificationList=deserialize_list(json_data.get("NotificationList"), NotificationListDefinition),
            QueryList=deserialize_list(json_data.get("QueryList"), QueryListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class NotificationListDefinition(BaseModel):
    Content: Optional[str]
    EmailList: Optional[Sequence[str]]
    MobileList: Optional[Sequence[str]]
    ServiceUri: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationListDefinition"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
            EmailList=json_data.get("EmailList"),
            MobileList=json_data.get("MobileList"),
            ServiceUri=json_data.get("ServiceUri"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationListDefinition = NotificationListDefinition


@dataclass
class QueryListDefinition(BaseModel):
    ChartTitle: Optional[str]
    End: Optional[str]
    Logstore: Optional[str]
    Query: Optional[str]
    Start: Optional[str]
    TimeSpanType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_QueryListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryListDefinition"]:
        if not json_data:
            return None
        return cls(
            ChartTitle=json_data.get("ChartTitle"),
            End=json_data.get("End"),
            Logstore=json_data.get("Logstore"),
            Query=json_data.get("Query"),
            Start=json_data.get("Start"),
            TimeSpanType=json_data.get("TimeSpanType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryListDefinition = QueryListDefinition


