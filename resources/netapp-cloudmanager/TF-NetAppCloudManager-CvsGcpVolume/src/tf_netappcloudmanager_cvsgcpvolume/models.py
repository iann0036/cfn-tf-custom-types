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
    Account: Optional[str]
    ClientId: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Network: Optional[str]
    ProtocolTypes: Optional[Sequence[str]]
    Region: Optional[str]
    ServiceLevel: Optional[str]
    Size: Optional[float]
    SizeUnit: Optional[str]
    VolumePath: Optional[str]
    WorkingEnvironmentName: Optional[str]
    ExportPolicy: Optional[Sequence["_ExportPolicyDefinition"]]
    SnapshotPolicy: Optional[Sequence["_SnapshotPolicyDefinition"]]

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
            Account=json_data.get("Account"),
            ClientId=json_data.get("ClientId"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Network=json_data.get("Network"),
            ProtocolTypes=json_data.get("ProtocolTypes"),
            Region=json_data.get("Region"),
            ServiceLevel=json_data.get("ServiceLevel"),
            Size=json_data.get("Size"),
            SizeUnit=json_data.get("SizeUnit"),
            VolumePath=json_data.get("VolumePath"),
            WorkingEnvironmentName=json_data.get("WorkingEnvironmentName"),
            ExportPolicy=deserialize_list(json_data.get("ExportPolicy"), ExportPolicyDefinition),
            SnapshotPolicy=deserialize_list(json_data.get("SnapshotPolicy"), SnapshotPolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ExportPolicyDefinition(BaseModel):
    Rule: Optional[Sequence["_RuleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ExportPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExportPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Rule=deserialize_list(json_data.get("Rule"), RuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExportPolicyDefinition = ExportPolicyDefinition


@dataclass
class RuleDefinition(BaseModel):
    AllowedClients: Optional[str]
    Nfsv3: Optional[bool]
    Nfsv4: Optional[bool]
    RuleIndex: Optional[float]
    UnixReadOnly: Optional[bool]
    UnixReadWrite: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowedClients=json_data.get("AllowedClients"),
            Nfsv3=json_data.get("Nfsv3"),
            Nfsv4=json_data.get("Nfsv4"),
            RuleIndex=json_data.get("RuleIndex"),
            UnixReadOnly=json_data.get("UnixReadOnly"),
            UnixReadWrite=json_data.get("UnixReadWrite"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleDefinition = RuleDefinition


@dataclass
class SnapshotPolicyDefinition(BaseModel):
    Enabled: Optional[bool]
    DailySchedule: Optional[Sequence["_DailyScheduleDefinition"]]
    HourlySchedule: Optional[Sequence["_HourlyScheduleDefinition"]]
    MonthlySchedule: Optional[Sequence["_MonthlyScheduleDefinition"]]
    WeeklySchedule: Optional[Sequence["_WeeklyScheduleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SnapshotPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnapshotPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            DailySchedule=deserialize_list(json_data.get("DailySchedule"), DailyScheduleDefinition),
            HourlySchedule=deserialize_list(json_data.get("HourlySchedule"), HourlyScheduleDefinition),
            MonthlySchedule=deserialize_list(json_data.get("MonthlySchedule"), MonthlyScheduleDefinition),
            WeeklySchedule=deserialize_list(json_data.get("WeeklySchedule"), WeeklyScheduleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnapshotPolicyDefinition = SnapshotPolicyDefinition


@dataclass
class DailyScheduleDefinition(BaseModel):
    Hour: Optional[float]
    Minute: Optional[float]
    SnapshotsToKeep: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DailyScheduleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DailyScheduleDefinition"]:
        if not json_data:
            return None
        return cls(
            Hour=json_data.get("Hour"),
            Minute=json_data.get("Minute"),
            SnapshotsToKeep=json_data.get("SnapshotsToKeep"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DailyScheduleDefinition = DailyScheduleDefinition


@dataclass
class HourlyScheduleDefinition(BaseModel):
    Minute: Optional[float]
    SnapshotsToKeep: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HourlyScheduleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HourlyScheduleDefinition"]:
        if not json_data:
            return None
        return cls(
            Minute=json_data.get("Minute"),
            SnapshotsToKeep=json_data.get("SnapshotsToKeep"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HourlyScheduleDefinition = HourlyScheduleDefinition


@dataclass
class MonthlyScheduleDefinition(BaseModel):
    DaysOfMonth: Optional[str]
    Hour: Optional[float]
    Minute: Optional[float]
    SnapshotsToKeep: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MonthlyScheduleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MonthlyScheduleDefinition"]:
        if not json_data:
            return None
        return cls(
            DaysOfMonth=json_data.get("DaysOfMonth"),
            Hour=json_data.get("Hour"),
            Minute=json_data.get("Minute"),
            SnapshotsToKeep=json_data.get("SnapshotsToKeep"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MonthlyScheduleDefinition = MonthlyScheduleDefinition


@dataclass
class WeeklyScheduleDefinition(BaseModel):
    Day: Optional[str]
    Hour: Optional[float]
    Minute: Optional[float]
    SnapshotsToKeep: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_WeeklyScheduleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WeeklyScheduleDefinition"]:
        if not json_data:
            return None
        return cls(
            Day=json_data.get("Day"),
            Hour=json_data.get("Hour"),
            Minute=json_data.get("Minute"),
            SnapshotsToKeep=json_data.get("SnapshotsToKeep"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WeeklyScheduleDefinition = WeeklyScheduleDefinition


