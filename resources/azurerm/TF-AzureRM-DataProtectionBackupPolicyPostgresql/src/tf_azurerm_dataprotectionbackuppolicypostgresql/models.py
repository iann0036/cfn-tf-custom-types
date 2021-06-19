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
    BackupRepeatingTimeIntervals: Optional[Sequence[str]]
    DefaultRetentionDuration: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    VaultName: Optional[str]
    RetentionRule: Optional[Sequence["_RetentionRuleDefinition"]]
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
            BackupRepeatingTimeIntervals=json_data.get("BackupRepeatingTimeIntervals"),
            DefaultRetentionDuration=json_data.get("DefaultRetentionDuration"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            VaultName=json_data.get("VaultName"),
            RetentionRule=deserialize_list(json_data.get("RetentionRule"), RetentionRuleDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RetentionRuleDefinition(BaseModel):
    Duration: Optional[str]
    Name: Optional[str]
    Priority: Optional[float]
    Criteria: Optional[Sequence["_CriteriaDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RetentionRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetentionRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Duration=json_data.get("Duration"),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            Criteria=deserialize_list(json_data.get("Criteria"), CriteriaDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetentionRuleDefinition = RetentionRuleDefinition


@dataclass
class CriteriaDefinition(BaseModel):
    AbsoluteCriteria: Optional[str]
    DaysOfWeek: Optional[Sequence[str]]
    MonthsOfYear: Optional[Sequence[str]]
    ScheduledBackupTimes: Optional[Sequence[str]]
    WeeksOfMonth: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CriteriaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CriteriaDefinition"]:
        if not json_data:
            return None
        return cls(
            AbsoluteCriteria=json_data.get("AbsoluteCriteria"),
            DaysOfWeek=json_data.get("DaysOfWeek"),
            MonthsOfYear=json_data.get("MonthsOfYear"),
            ScheduledBackupTimes=json_data.get("ScheduledBackupTimes"),
            WeeksOfMonth=json_data.get("WeeksOfMonth"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CriteriaDefinition = CriteriaDefinition


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


