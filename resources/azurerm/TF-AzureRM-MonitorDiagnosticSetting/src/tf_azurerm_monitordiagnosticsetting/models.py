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
    EventhubAuthorizationRuleId: Optional[str]
    EventhubName: Optional[str]
    Id: Optional[str]
    LogAnalyticsDestinationType: Optional[str]
    LogAnalyticsWorkspaceId: Optional[str]
    Name: Optional[str]
    StorageAccountId: Optional[str]
    TargetResourceId: Optional[str]
    Log: Optional[Sequence["_LogDefinition"]]
    Metric: Optional[Sequence["_MetricDefinition"]]
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
            EventhubAuthorizationRuleId=json_data.get("EventhubAuthorizationRuleId"),
            EventhubName=json_data.get("EventhubName"),
            Id=json_data.get("Id"),
            LogAnalyticsDestinationType=json_data.get("LogAnalyticsDestinationType"),
            LogAnalyticsWorkspaceId=json_data.get("LogAnalyticsWorkspaceId"),
            Name=json_data.get("Name"),
            StorageAccountId=json_data.get("StorageAccountId"),
            TargetResourceId=json_data.get("TargetResourceId"),
            Log=deserialize_list(json_data.get("Log"), LogDefinition),
            Metric=deserialize_list(json_data.get("Metric"), MetricDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LogDefinition(BaseModel):
    Category: Optional[str]
    Enabled: Optional[bool]
    RetentionPolicy: Optional[Sequence["_RetentionPolicyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LogDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogDefinition"]:
        if not json_data:
            return None
        return cls(
            Category=json_data.get("Category"),
            Enabled=json_data.get("Enabled"),
            RetentionPolicy=deserialize_list(json_data.get("RetentionPolicy"), RetentionPolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogDefinition = LogDefinition


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
class MetricDefinition(BaseModel):
    Category: Optional[str]
    Enabled: Optional[bool]
    RetentionPolicy: Optional[Sequence["_RetentionPolicyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MetricDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricDefinition"]:
        if not json_data:
            return None
        return cls(
            Category=json_data.get("Category"),
            Enabled=json_data.get("Enabled"),
            RetentionPolicy=deserialize_list(json_data.get("RetentionPolicy"), RetentionPolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricDefinition = MetricDefinition


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

