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
    CreateTime: Optional[str]
    Description: Optional[str]
    Duration: Optional[str]
    Id: Optional[str]
    LastExecuteTime: Optional[str]
    Name: Optional[str]
    PatchDeploymentId: Optional[str]
    Project: Optional[str]
    UpdateTime: Optional[str]
    InstanceFilter: Optional[Sequence["_InstanceFilterDefinition"]]
    OneTimeSchedule: Optional[Sequence["_OneTimeScheduleDefinition"]]
    PatchConfig: Optional[Sequence["_PatchConfigDefinition"]]
    RecurringSchedule: Optional[Sequence["_RecurringScheduleDefinition"]]
    Rollout: Optional[Sequence["_RolloutDefinition"]]
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
            CreateTime=json_data.get("CreateTime"),
            Description=json_data.get("Description"),
            Duration=json_data.get("Duration"),
            Id=json_data.get("Id"),
            LastExecuteTime=json_data.get("LastExecuteTime"),
            Name=json_data.get("Name"),
            PatchDeploymentId=json_data.get("PatchDeploymentId"),
            Project=json_data.get("Project"),
            UpdateTime=json_data.get("UpdateTime"),
            InstanceFilter=deserialize_list(json_data.get("InstanceFilter"), InstanceFilterDefinition),
            OneTimeSchedule=deserialize_list(json_data.get("OneTimeSchedule"), OneTimeScheduleDefinition),
            PatchConfig=deserialize_list(json_data.get("PatchConfig"), PatchConfigDefinition),
            RecurringSchedule=deserialize_list(json_data.get("RecurringSchedule"), RecurringScheduleDefinition),
            Rollout=deserialize_list(json_data.get("Rollout"), RolloutDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InstanceFilterDefinition(BaseModel):
    All: Optional[bool]
    InstanceNamePrefixes: Optional[Sequence[str]]
    Instances: Optional[Sequence[str]]
    Zones: Optional[Sequence[str]]
    GroupLabels: Optional[Sequence["_GroupLabelsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceFilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceFilterDefinition"]:
        if not json_data:
            return None
        return cls(
            All=json_data.get("All"),
            InstanceNamePrefixes=json_data.get("InstanceNamePrefixes"),
            Instances=json_data.get("Instances"),
            Zones=json_data.get("Zones"),
            GroupLabels=deserialize_list(json_data.get("GroupLabels"), GroupLabelsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceFilterDefinition = InstanceFilterDefinition


@dataclass
class GroupLabelsDefinition(BaseModel):
    Labels: Optional[Sequence["_LabelsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_GroupLabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GroupLabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_GroupLabelsDefinition = GroupLabelsDefinition


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class OneTimeScheduleDefinition(BaseModel):
    ExecuteTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OneTimeScheduleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OneTimeScheduleDefinition"]:
        if not json_data:
            return None
        return cls(
            ExecuteTime=json_data.get("ExecuteTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OneTimeScheduleDefinition = OneTimeScheduleDefinition


@dataclass
class PatchConfigDefinition(BaseModel):
    RebootConfig: Optional[str]
    Apt: Optional[Sequence["_AptDefinition"]]
    Goo: Optional[Sequence["_GooDefinition"]]
    PostStep: Optional[Sequence["_PostStepDefinition"]]
    PreStep: Optional[Sequence["_PreStepDefinition"]]
    WindowsUpdate: Optional[Sequence["_WindowsUpdateDefinition"]]
    Yum: Optional[Sequence["_YumDefinition"]]
    Zypper: Optional[Sequence["_ZypperDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PatchConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PatchConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            RebootConfig=json_data.get("RebootConfig"),
            Apt=deserialize_list(json_data.get("Apt"), AptDefinition),
            Goo=deserialize_list(json_data.get("Goo"), GooDefinition),
            PostStep=deserialize_list(json_data.get("PostStep"), PostStepDefinition),
            PreStep=deserialize_list(json_data.get("PreStep"), PreStepDefinition),
            WindowsUpdate=deserialize_list(json_data.get("WindowsUpdate"), WindowsUpdateDefinition),
            Yum=deserialize_list(json_data.get("Yum"), YumDefinition),
            Zypper=deserialize_list(json_data.get("Zypper"), ZypperDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PatchConfigDefinition = PatchConfigDefinition


@dataclass
class AptDefinition(BaseModel):
    Excludes: Optional[Sequence[str]]
    ExclusivePackages: Optional[Sequence[str]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AptDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AptDefinition"]:
        if not json_data:
            return None
        return cls(
            Excludes=json_data.get("Excludes"),
            ExclusivePackages=json_data.get("ExclusivePackages"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AptDefinition = AptDefinition


@dataclass
class GooDefinition(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_GooDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GooDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GooDefinition = GooDefinition


@dataclass
class PostStepDefinition(BaseModel):
    LinuxExecStepConfig: Optional[Sequence["_LinuxExecStepConfigDefinition"]]
    WindowsExecStepConfig: Optional[Sequence["_WindowsExecStepConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PostStepDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PostStepDefinition"]:
        if not json_data:
            return None
        return cls(
            LinuxExecStepConfig=deserialize_list(json_data.get("LinuxExecStepConfig"), LinuxExecStepConfigDefinition),
            WindowsExecStepConfig=deserialize_list(json_data.get("WindowsExecStepConfig"), WindowsExecStepConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PostStepDefinition = PostStepDefinition


@dataclass
class LinuxExecStepConfigDefinition(BaseModel):
    AllowedSuccessCodes: Optional[Sequence[float]]
    Interpreter: Optional[str]
    LocalPath: Optional[str]
    GcsObject: Optional[Sequence["_GcsObjectDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LinuxExecStepConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LinuxExecStepConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowedSuccessCodes=json_data.get("AllowedSuccessCodes"),
            Interpreter=json_data.get("Interpreter"),
            LocalPath=json_data.get("LocalPath"),
            GcsObject=deserialize_list(json_data.get("GcsObject"), GcsObjectDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LinuxExecStepConfigDefinition = LinuxExecStepConfigDefinition


@dataclass
class GcsObjectDefinition(BaseModel):
    Bucket: Optional[str]
    GenerationNumber: Optional[str]
    Object: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GcsObjectDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GcsObjectDefinition"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            GenerationNumber=json_data.get("GenerationNumber"),
            Object=json_data.get("Object"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GcsObjectDefinition = GcsObjectDefinition


@dataclass
class WindowsExecStepConfigDefinition(BaseModel):
    AllowedSuccessCodes: Optional[Sequence[float]]
    Interpreter: Optional[str]
    LocalPath: Optional[str]
    GcsObject: Optional[Sequence["_GcsObjectDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WindowsExecStepConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WindowsExecStepConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowedSuccessCodes=json_data.get("AllowedSuccessCodes"),
            Interpreter=json_data.get("Interpreter"),
            LocalPath=json_data.get("LocalPath"),
            GcsObject=deserialize_list(json_data.get("GcsObject"), GcsObjectDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WindowsExecStepConfigDefinition = WindowsExecStepConfigDefinition


@dataclass
class PreStepDefinition(BaseModel):
    LinuxExecStepConfig: Optional[Sequence["_LinuxExecStepConfigDefinition"]]
    WindowsExecStepConfig: Optional[Sequence["_WindowsExecStepConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PreStepDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PreStepDefinition"]:
        if not json_data:
            return None
        return cls(
            LinuxExecStepConfig=deserialize_list(json_data.get("LinuxExecStepConfig"), LinuxExecStepConfigDefinition),
            WindowsExecStepConfig=deserialize_list(json_data.get("WindowsExecStepConfig"), WindowsExecStepConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PreStepDefinition = PreStepDefinition


@dataclass
class WindowsUpdateDefinition(BaseModel):
    Classifications: Optional[Sequence[str]]
    Excludes: Optional[Sequence[str]]
    ExclusivePatches: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_WindowsUpdateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WindowsUpdateDefinition"]:
        if not json_data:
            return None
        return cls(
            Classifications=json_data.get("Classifications"),
            Excludes=json_data.get("Excludes"),
            ExclusivePatches=json_data.get("ExclusivePatches"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WindowsUpdateDefinition = WindowsUpdateDefinition


@dataclass
class YumDefinition(BaseModel):
    Excludes: Optional[Sequence[str]]
    ExclusivePackages: Optional[Sequence[str]]
    Minimal: Optional[bool]
    Security: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_YumDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_YumDefinition"]:
        if not json_data:
            return None
        return cls(
            Excludes=json_data.get("Excludes"),
            ExclusivePackages=json_data.get("ExclusivePackages"),
            Minimal=json_data.get("Minimal"),
            Security=json_data.get("Security"),
        )


# work around possible type aliasing issues when variable has same name as a model
_YumDefinition = YumDefinition


@dataclass
class ZypperDefinition(BaseModel):
    Categories: Optional[Sequence[str]]
    Excludes: Optional[Sequence[str]]
    ExclusivePatches: Optional[Sequence[str]]
    Severities: Optional[Sequence[str]]
    WithOptional: Optional[bool]
    WithUpdate: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ZypperDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ZypperDefinition"]:
        if not json_data:
            return None
        return cls(
            Categories=json_data.get("Categories"),
            Excludes=json_data.get("Excludes"),
            ExclusivePatches=json_data.get("ExclusivePatches"),
            Severities=json_data.get("Severities"),
            WithOptional=json_data.get("WithOptional"),
            WithUpdate=json_data.get("WithUpdate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ZypperDefinition = ZypperDefinition


@dataclass
class RecurringScheduleDefinition(BaseModel):
    EndTime: Optional[str]
    StartTime: Optional[str]
    Monthly: Optional[Sequence["_MonthlyDefinition"]]
    TimeOfDay: Optional[Sequence["_TimeOfDayDefinition"]]
    TimeZone: Optional[Sequence["_TimeZoneDefinition"]]
    Weekly: Optional[Sequence["_WeeklyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RecurringScheduleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecurringScheduleDefinition"]:
        if not json_data:
            return None
        return cls(
            EndTime=json_data.get("EndTime"),
            StartTime=json_data.get("StartTime"),
            Monthly=deserialize_list(json_data.get("Monthly"), MonthlyDefinition),
            TimeOfDay=deserialize_list(json_data.get("TimeOfDay"), TimeOfDayDefinition),
            TimeZone=deserialize_list(json_data.get("TimeZone"), TimeZoneDefinition),
            Weekly=deserialize_list(json_data.get("Weekly"), WeeklyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecurringScheduleDefinition = RecurringScheduleDefinition


@dataclass
class MonthlyDefinition(BaseModel):
    MonthDay: Optional[float]
    WeekDayOfMonth: Optional[Sequence["_WeekDayOfMonthDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MonthlyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MonthlyDefinition"]:
        if not json_data:
            return None
        return cls(
            MonthDay=json_data.get("MonthDay"),
            WeekDayOfMonth=deserialize_list(json_data.get("WeekDayOfMonth"), WeekDayOfMonthDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MonthlyDefinition = MonthlyDefinition


@dataclass
class WeekDayOfMonthDefinition(BaseModel):
    DayOfWeek: Optional[str]
    WeekOrdinal: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_WeekDayOfMonthDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WeekDayOfMonthDefinition"]:
        if not json_data:
            return None
        return cls(
            DayOfWeek=json_data.get("DayOfWeek"),
            WeekOrdinal=json_data.get("WeekOrdinal"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WeekDayOfMonthDefinition = WeekDayOfMonthDefinition


@dataclass
class TimeOfDayDefinition(BaseModel):
    Hours: Optional[float]
    Minutes: Optional[float]
    Nanos: Optional[float]
    Seconds: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TimeOfDayDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeOfDayDefinition"]:
        if not json_data:
            return None
        return cls(
            Hours=json_data.get("Hours"),
            Minutes=json_data.get("Minutes"),
            Nanos=json_data.get("Nanos"),
            Seconds=json_data.get("Seconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeOfDayDefinition = TimeOfDayDefinition


@dataclass
class TimeZoneDefinition(BaseModel):
    Id: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeZoneDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeZoneDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeZoneDefinition = TimeZoneDefinition


@dataclass
class WeeklyDefinition(BaseModel):
    DayOfWeek: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WeeklyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WeeklyDefinition"]:
        if not json_data:
            return None
        return cls(
            DayOfWeek=json_data.get("DayOfWeek"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WeeklyDefinition = WeeklyDefinition


@dataclass
class RolloutDefinition(BaseModel):
    Mode: Optional[str]
    DisruptionBudget: Optional[Sequence["_DisruptionBudgetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RolloutDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RolloutDefinition"]:
        if not json_data:
            return None
        return cls(
            Mode=json_data.get("Mode"),
            DisruptionBudget=deserialize_list(json_data.get("DisruptionBudget"), DisruptionBudgetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RolloutDefinition = RolloutDefinition


@dataclass
class DisruptionBudgetDefinition(BaseModel):
    Fixed: Optional[float]
    Percentage: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DisruptionBudgetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DisruptionBudgetDefinition"]:
        if not json_data:
            return None
        return cls(
            Fixed=json_data.get("Fixed"),
            Percentage=json_data.get("Percentage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DisruptionBudgetDefinition = DisruptionBudgetDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


