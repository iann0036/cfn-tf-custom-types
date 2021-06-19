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
    Description: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Condition: Optional[Sequence["_ConditionDefinition"]]
    Scope: Optional[Sequence["_ScopeDefinition"]]
    Suppression: Optional[Sequence["_SuppressionDefinition"]]
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
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Condition=deserialize_list(json_data.get("Condition"), ConditionDefinition),
            Scope=deserialize_list(json_data.get("Scope"), ScopeDefinition),
            Suppression=deserialize_list(json_data.get("Suppression"), SuppressionDefinition),
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
class ConditionDefinition(BaseModel):
    AlertContext: Optional[Sequence["_AlertContextDefinition"]]
    AlertRuleId: Optional[Sequence["_AlertRuleIdDefinition"]]
    Description: Optional[Sequence["_DescriptionDefinition"]]
    Monitor: Optional[Sequence["_MonitorDefinition"]]
    MonitorService: Optional[Sequence["_MonitorServiceDefinition"]]
    Severity: Optional[Sequence["_SeverityDefinition"]]
    TargetResourceType: Optional[Sequence["_TargetResourceTypeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            AlertContext=deserialize_list(json_data.get("AlertContext"), AlertContextDefinition),
            AlertRuleId=deserialize_list(json_data.get("AlertRuleId"), AlertRuleIdDefinition),
            Description=deserialize_list(json_data.get("Description"), DescriptionDefinition),
            Monitor=deserialize_list(json_data.get("Monitor"), MonitorDefinition),
            MonitorService=deserialize_list(json_data.get("MonitorService"), MonitorServiceDefinition),
            Severity=deserialize_list(json_data.get("Severity"), SeverityDefinition),
            TargetResourceType=deserialize_list(json_data.get("TargetResourceType"), TargetResourceTypeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionDefinition = ConditionDefinition


@dataclass
class AlertContextDefinition(BaseModel):
    Operator: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AlertContextDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlertContextDefinition"]:
        if not json_data:
            return None
        return cls(
            Operator=json_data.get("Operator"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlertContextDefinition = AlertContextDefinition


@dataclass
class AlertRuleIdDefinition(BaseModel):
    Operator: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AlertRuleIdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlertRuleIdDefinition"]:
        if not json_data:
            return None
        return cls(
            Operator=json_data.get("Operator"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlertRuleIdDefinition = AlertRuleIdDefinition


@dataclass
class DescriptionDefinition(BaseModel):
    Operator: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DescriptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DescriptionDefinition"]:
        if not json_data:
            return None
        return cls(
            Operator=json_data.get("Operator"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DescriptionDefinition = DescriptionDefinition


@dataclass
class MonitorDefinition(BaseModel):
    Operator: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MonitorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MonitorDefinition"]:
        if not json_data:
            return None
        return cls(
            Operator=json_data.get("Operator"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MonitorDefinition = MonitorDefinition


@dataclass
class MonitorServiceDefinition(BaseModel):
    Operator: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MonitorServiceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MonitorServiceDefinition"]:
        if not json_data:
            return None
        return cls(
            Operator=json_data.get("Operator"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MonitorServiceDefinition = MonitorServiceDefinition


@dataclass
class SeverityDefinition(BaseModel):
    Operator: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SeverityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SeverityDefinition"]:
        if not json_data:
            return None
        return cls(
            Operator=json_data.get("Operator"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeverityDefinition = SeverityDefinition


@dataclass
class TargetResourceTypeDefinition(BaseModel):
    Operator: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_TargetResourceTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetResourceTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            Operator=json_data.get("Operator"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetResourceTypeDefinition = TargetResourceTypeDefinition


@dataclass
class ScopeDefinition(BaseModel):
    ResourceIds: Optional[Sequence[str]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScopeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScopeDefinition"]:
        if not json_data:
            return None
        return cls(
            ResourceIds=json_data.get("ResourceIds"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScopeDefinition = ScopeDefinition


@dataclass
class SuppressionDefinition(BaseModel):
    RecurrenceType: Optional[str]
    Schedule: Optional[Sequence["_ScheduleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SuppressionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SuppressionDefinition"]:
        if not json_data:
            return None
        return cls(
            RecurrenceType=json_data.get("RecurrenceType"),
            Schedule=deserialize_list(json_data.get("Schedule"), ScheduleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SuppressionDefinition = SuppressionDefinition


@dataclass
class ScheduleDefinition(BaseModel):
    EndDateUtc: Optional[str]
    RecurrenceMonthly: Optional[Sequence[float]]
    RecurrenceWeekly: Optional[Sequence[str]]
    StartDateUtc: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduleDefinition"]:
        if not json_data:
            return None
        return cls(
            EndDateUtc=json_data.get("EndDateUtc"),
            RecurrenceMonthly=json_data.get("RecurrenceMonthly"),
            RecurrenceWeekly=json_data.get("RecurrenceWeekly"),
            StartDateUtc=json_data.get("StartDateUtc"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduleDefinition = ScheduleDefinition


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


