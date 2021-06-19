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
    AfterRebootRollbackFnc: Optional[str]
    AfterRebootTaskName: Optional[str]
    Clean: Optional[bool]
    Duration: Optional[float]
    EnablePatchRollback: Optional[bool]
    EnableRollback: Optional[bool]
    EndTime: Optional[str]
    EnqueueTime: Optional[str]
    FipsMode: Optional[bool]
    Id: Optional[str]
    ImagePath: Optional[str]
    ImageRef: Optional[str]
    Name: Optional[str]
    NodeType: Optional[str]
    ObjCloudRef: Optional[str]
    PatchImagePath: Optional[str]
    PatchImageRef: Optional[str]
    PatchReboot: Optional[bool]
    PatchVersion: Optional[str]
    PrevImagePath: Optional[str]
    PrevPatchImagePath: Optional[str]
    PreviousImageRef: Optional[str]
    PreviousPatchImageRef: Optional[str]
    PreviousPatchVersion: Optional[str]
    PreviousVersion: Optional[str]
    Progress: Optional[float]
    SePatchImagePath: Optional[str]
    SePatchImageRef: Optional[str]
    StartTime: Optional[str]
    System: Optional[bool]
    TasksCompleted: Optional[float]
    TenantRef: Optional[str]
    TotalTasks: Optional[float]
    UpgradeOps: Optional[str]
    Uuid: Optional[str]
    Version: Optional[str]
    History: Optional[Sequence["_HistoryDefinition"]]
    Params: Optional[Sequence["_ParamsDefinition"]]
    PatchList: Optional[Sequence["_PatchListDefinition"]]
    PreviousPatchList: Optional[Sequence["_PreviousPatchListDefinition"]]
    SeUpgradeEvents: Optional[Sequence["_SeUpgradeEventsDefinition"]]
    SegParams: Optional[Sequence["_SegParamsDefinition"]]
    SegStatus: Optional[Sequence["_SegStatusDefinition"]]
    State: Optional[Sequence["_StateDefinition"]]
    UpgradeEvents: Optional[Sequence["_UpgradeEventsDefinition"]]

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
            AfterRebootRollbackFnc=json_data.get("AfterRebootRollbackFnc"),
            AfterRebootTaskName=json_data.get("AfterRebootTaskName"),
            Clean=json_data.get("Clean"),
            Duration=json_data.get("Duration"),
            EnablePatchRollback=json_data.get("EnablePatchRollback"),
            EnableRollback=json_data.get("EnableRollback"),
            EndTime=json_data.get("EndTime"),
            EnqueueTime=json_data.get("EnqueueTime"),
            FipsMode=json_data.get("FipsMode"),
            Id=json_data.get("Id"),
            ImagePath=json_data.get("ImagePath"),
            ImageRef=json_data.get("ImageRef"),
            Name=json_data.get("Name"),
            NodeType=json_data.get("NodeType"),
            ObjCloudRef=json_data.get("ObjCloudRef"),
            PatchImagePath=json_data.get("PatchImagePath"),
            PatchImageRef=json_data.get("PatchImageRef"),
            PatchReboot=json_data.get("PatchReboot"),
            PatchVersion=json_data.get("PatchVersion"),
            PrevImagePath=json_data.get("PrevImagePath"),
            PrevPatchImagePath=json_data.get("PrevPatchImagePath"),
            PreviousImageRef=json_data.get("PreviousImageRef"),
            PreviousPatchImageRef=json_data.get("PreviousPatchImageRef"),
            PreviousPatchVersion=json_data.get("PreviousPatchVersion"),
            PreviousVersion=json_data.get("PreviousVersion"),
            Progress=json_data.get("Progress"),
            SePatchImagePath=json_data.get("SePatchImagePath"),
            SePatchImageRef=json_data.get("SePatchImageRef"),
            StartTime=json_data.get("StartTime"),
            System=json_data.get("System"),
            TasksCompleted=json_data.get("TasksCompleted"),
            TenantRef=json_data.get("TenantRef"),
            TotalTasks=json_data.get("TotalTasks"),
            UpgradeOps=json_data.get("UpgradeOps"),
            Uuid=json_data.get("Uuid"),
            Version=json_data.get("Version"),
            History=deserialize_list(json_data.get("History"), HistoryDefinition),
            Params=deserialize_list(json_data.get("Params"), ParamsDefinition),
            PatchList=deserialize_list(json_data.get("PatchList"), PatchListDefinition),
            PreviousPatchList=deserialize_list(json_data.get("PreviousPatchList"), PreviousPatchListDefinition),
            SeUpgradeEvents=deserialize_list(json_data.get("SeUpgradeEvents"), SeUpgradeEventsDefinition),
            SegParams=deserialize_list(json_data.get("SegParams"), SegParamsDefinition),
            SegStatus=deserialize_list(json_data.get("SegStatus"), SegStatusDefinition),
            State=deserialize_list(json_data.get("State"), StateDefinition),
            UpgradeEvents=deserialize_list(json_data.get("UpgradeEvents"), UpgradeEventsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class HistoryDefinition(BaseModel):
    Duration: Optional[float]
    EndTime: Optional[str]
    Ops: Optional[str]
    PatchVersion: Optional[str]
    StartTime: Optional[str]
    Version: Optional[str]
    SeUpgradeEvents: Optional[Sequence["_SeUpgradeEventsDefinition"]]
    SegStatus: Optional[Sequence["_SegStatusDefinition"]]
    State: Optional[Sequence["_StateDefinition"]]
    UpgradeEvents: Optional[Sequence["_UpgradeEventsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HistoryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HistoryDefinition"]:
        if not json_data:
            return None
        return cls(
            Duration=json_data.get("Duration"),
            EndTime=json_data.get("EndTime"),
            Ops=json_data.get("Ops"),
            PatchVersion=json_data.get("PatchVersion"),
            StartTime=json_data.get("StartTime"),
            Version=json_data.get("Version"),
            SeUpgradeEvents=deserialize_list(json_data.get("SeUpgradeEvents"), SeUpgradeEventsDefinition),
            SegStatus=deserialize_list(json_data.get("SegStatus"), SegStatusDefinition),
            State=deserialize_list(json_data.get("State"), StateDefinition),
            UpgradeEvents=deserialize_list(json_data.get("UpgradeEvents"), UpgradeEventsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HistoryDefinition = HistoryDefinition


@dataclass
class SeUpgradeEventsDefinition(BaseModel):
    FromSeRef: Optional[str]
    NumSe: Optional[float]
    NumSeGroup: Optional[float]
    NumVs: Optional[float]
    Reason: Optional[Sequence[str]]
    SeGroupHaMode: Optional[str]
    SeGroupRef: Optional[str]
    SeRef: Optional[str]
    SubTasks: Optional[Sequence[str]]
    Task: Optional[str]
    ToSeRef: Optional[str]
    TrafficStatus: Optional[str]
    VsRef: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SeUpgradeEventsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SeUpgradeEventsDefinition"]:
        if not json_data:
            return None
        return cls(
            FromSeRef=json_data.get("FromSeRef"),
            NumSe=json_data.get("NumSe"),
            NumSeGroup=json_data.get("NumSeGroup"),
            NumVs=json_data.get("NumVs"),
            Reason=json_data.get("Reason"),
            SeGroupHaMode=json_data.get("SeGroupHaMode"),
            SeGroupRef=json_data.get("SeGroupRef"),
            SeRef=json_data.get("SeRef"),
            SubTasks=json_data.get("SubTasks"),
            Task=json_data.get("Task"),
            ToSeRef=json_data.get("ToSeRef"),
            TrafficStatus=json_data.get("TrafficStatus"),
            VsRef=json_data.get("VsRef"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeUpgradeEventsDefinition = SeUpgradeEventsDefinition


@dataclass
class SegStatusDefinition(BaseModel):
    ControllerVersion: Optional[str]
    DisruptedVsRef: Optional[Sequence[str]]
    Duration: Optional[str]
    EndTime: Optional[str]
    EnqueueTime: Optional[str]
    HaMode: Optional[str]
    InProgress: Optional[bool]
    Notes: Optional[Sequence[str]]
    NumSe: Optional[float]
    NumSeWithNoVs: Optional[float]
    NumSeWithVsNotScaledout: Optional[float]
    NumSeWithVsScaledout: Optional[float]
    NumVs: Optional[float]
    NumVsDisrupted: Optional[float]
    Progress: Optional[float]
    Reason: Optional[Sequence[str]]
    RequestTime: Optional[str]
    SeAlreadyUpgradedAtStart: Optional[Sequence[str]]
    SeDisconnectedAtStart: Optional[Sequence[str]]
    SeGroupName: Optional[str]
    SeGroupUuid: Optional[str]
    SeIpMissingAtStart: Optional[Sequence[str]]
    SePoweredoffAtStart: Optional[Sequence[str]]
    SeRebootInProgressRef: Optional[str]
    SeUpgradeCompleted: Optional[Sequence[str]]
    SeUpgradeFailed: Optional[Sequence[str]]
    SeUpgradeInProgress: Optional[Sequence[str]]
    SeUpgradeNotStarted: Optional[Sequence[str]]
    SeUpgradeSkipSuspended: Optional[Sequence[str]]
    SeUpgradeSuspended: Optional[Sequence[str]]
    SeWithNoVs: Optional[Sequence[str]]
    SeWithVsNotScaledout: Optional[Sequence[str]]
    SeWithVsScaledout: Optional[Sequence[str]]
    StartTime: Optional[str]
    State: Optional[str]
    TenantRef: Optional[str]
    Thread: Optional[str]
    TrafficStatus: Optional[str]
    VsMigrateInProgressRef: Optional[Sequence[str]]
    VsScaleinInProgressRef: Optional[Sequence[str]]
    VsScaleoutInProgressRef: Optional[Sequence[str]]
    Worker: Optional[str]
    SeUpgradeErrors: Optional[Sequence["_SeUpgradeErrorsDefinition"]]
    VsErrors: Optional[Sequence["_VsErrorsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SegStatusDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SegStatusDefinition"]:
        if not json_data:
            return None
        return cls(
            ControllerVersion=json_data.get("ControllerVersion"),
            DisruptedVsRef=json_data.get("DisruptedVsRef"),
            Duration=json_data.get("Duration"),
            EndTime=json_data.get("EndTime"),
            EnqueueTime=json_data.get("EnqueueTime"),
            HaMode=json_data.get("HaMode"),
            InProgress=json_data.get("InProgress"),
            Notes=json_data.get("Notes"),
            NumSe=json_data.get("NumSe"),
            NumSeWithNoVs=json_data.get("NumSeWithNoVs"),
            NumSeWithVsNotScaledout=json_data.get("NumSeWithVsNotScaledout"),
            NumSeWithVsScaledout=json_data.get("NumSeWithVsScaledout"),
            NumVs=json_data.get("NumVs"),
            NumVsDisrupted=json_data.get("NumVsDisrupted"),
            Progress=json_data.get("Progress"),
            Reason=json_data.get("Reason"),
            RequestTime=json_data.get("RequestTime"),
            SeAlreadyUpgradedAtStart=json_data.get("SeAlreadyUpgradedAtStart"),
            SeDisconnectedAtStart=json_data.get("SeDisconnectedAtStart"),
            SeGroupName=json_data.get("SeGroupName"),
            SeGroupUuid=json_data.get("SeGroupUuid"),
            SeIpMissingAtStart=json_data.get("SeIpMissingAtStart"),
            SePoweredoffAtStart=json_data.get("SePoweredoffAtStart"),
            SeRebootInProgressRef=json_data.get("SeRebootInProgressRef"),
            SeUpgradeCompleted=json_data.get("SeUpgradeCompleted"),
            SeUpgradeFailed=json_data.get("SeUpgradeFailed"),
            SeUpgradeInProgress=json_data.get("SeUpgradeInProgress"),
            SeUpgradeNotStarted=json_data.get("SeUpgradeNotStarted"),
            SeUpgradeSkipSuspended=json_data.get("SeUpgradeSkipSuspended"),
            SeUpgradeSuspended=json_data.get("SeUpgradeSuspended"),
            SeWithNoVs=json_data.get("SeWithNoVs"),
            SeWithVsNotScaledout=json_data.get("SeWithVsNotScaledout"),
            SeWithVsScaledout=json_data.get("SeWithVsScaledout"),
            StartTime=json_data.get("StartTime"),
            State=json_data.get("State"),
            TenantRef=json_data.get("TenantRef"),
            Thread=json_data.get("Thread"),
            TrafficStatus=json_data.get("TrafficStatus"),
            VsMigrateInProgressRef=json_data.get("VsMigrateInProgressRef"),
            VsScaleinInProgressRef=json_data.get("VsScaleinInProgressRef"),
            VsScaleoutInProgressRef=json_data.get("VsScaleoutInProgressRef"),
            Worker=json_data.get("Worker"),
            SeUpgradeErrors=deserialize_list(json_data.get("SeUpgradeErrors"), SeUpgradeErrorsDefinition),
            VsErrors=deserialize_list(json_data.get("VsErrors"), VsErrorsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SegStatusDefinition = SegStatusDefinition


@dataclass
class SeUpgradeErrorsDefinition(BaseModel):
    FromSeRef: Optional[str]
    NumSe: Optional[float]
    NumSeGroup: Optional[float]
    NumVs: Optional[float]
    Reason: Optional[Sequence[str]]
    SeGroupHaMode: Optional[str]
    SeGroupRef: Optional[str]
    SeRef: Optional[str]
    SubTasks: Optional[Sequence[str]]
    Task: Optional[str]
    ToSeRef: Optional[str]
    TrafficStatus: Optional[str]
    VsRef: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SeUpgradeErrorsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SeUpgradeErrorsDefinition"]:
        if not json_data:
            return None
        return cls(
            FromSeRef=json_data.get("FromSeRef"),
            NumSe=json_data.get("NumSe"),
            NumSeGroup=json_data.get("NumSeGroup"),
            NumVs=json_data.get("NumVs"),
            Reason=json_data.get("Reason"),
            SeGroupHaMode=json_data.get("SeGroupHaMode"),
            SeGroupRef=json_data.get("SeGroupRef"),
            SeRef=json_data.get("SeRef"),
            SubTasks=json_data.get("SubTasks"),
            Task=json_data.get("Task"),
            ToSeRef=json_data.get("ToSeRef"),
            TrafficStatus=json_data.get("TrafficStatus"),
            VsRef=json_data.get("VsRef"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeUpgradeErrorsDefinition = SeUpgradeErrorsDefinition


@dataclass
class VsErrorsDefinition(BaseModel):
    Reason: Optional[Sequence[str]]
    SeGroupHaMode: Optional[str]
    SeGroupRef: Optional[str]
    SeRef: Optional[str]
    TenantRef: Optional[str]
    TrafficStatus: Optional[str]
    VipId: Optional[str]
    VsRef: Optional[str]
    EventTimestamp: Optional[Sequence["_EventTimestampDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VsErrorsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VsErrorsDefinition"]:
        if not json_data:
            return None
        return cls(
            Reason=json_data.get("Reason"),
            SeGroupHaMode=json_data.get("SeGroupHaMode"),
            SeGroupRef=json_data.get("SeGroupRef"),
            SeRef=json_data.get("SeRef"),
            TenantRef=json_data.get("TenantRef"),
            TrafficStatus=json_data.get("TrafficStatus"),
            VipId=json_data.get("VipId"),
            VsRef=json_data.get("VsRef"),
            EventTimestamp=deserialize_list(json_data.get("EventTimestamp"), EventTimestampDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VsErrorsDefinition = VsErrorsDefinition


@dataclass
class EventTimestampDefinition(BaseModel):
    Secs: Optional[float]
    Usecs: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_EventTimestampDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventTimestampDefinition"]:
        if not json_data:
            return None
        return cls(
            Secs=json_data.get("Secs"),
            Usecs=json_data.get("Usecs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventTimestampDefinition = EventTimestampDefinition


@dataclass
class StateDefinition(BaseModel):
    Reason: Optional[str]
    Rebooted: Optional[bool]
    State: Optional[str]
    LastChangedTime: Optional[Sequence["_LastChangedTimeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StateDefinition"]:
        if not json_data:
            return None
        return cls(
            Reason=json_data.get("Reason"),
            Rebooted=json_data.get("Rebooted"),
            State=json_data.get("State"),
            LastChangedTime=deserialize_list(json_data.get("LastChangedTime"), LastChangedTimeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StateDefinition = StateDefinition


@dataclass
class LastChangedTimeDefinition(BaseModel):
    Secs: Optional[float]
    Usecs: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_LastChangedTimeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LastChangedTimeDefinition"]:
        if not json_data:
            return None
        return cls(
            Secs=json_data.get("Secs"),
            Usecs=json_data.get("Usecs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LastChangedTimeDefinition = LastChangedTimeDefinition


@dataclass
class UpgradeEventsDefinition(BaseModel):
    Task: Optional[str]
    TaskName: Optional[str]
    NodesEvents: Optional[Sequence["_NodesEventsDefinition"]]
    SubEvents: Optional[Sequence["_SubEventsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_UpgradeEventsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UpgradeEventsDefinition"]:
        if not json_data:
            return None
        return cls(
            Task=json_data.get("Task"),
            TaskName=json_data.get("TaskName"),
            NodesEvents=deserialize_list(json_data.get("NodesEvents"), NodesEventsDefinition),
            SubEvents=deserialize_list(json_data.get("SubEvents"), SubEventsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_UpgradeEventsDefinition = UpgradeEventsDefinition


@dataclass
class NodesEventsDefinition(BaseModel):
    Duration: Optional[float]
    EndTime: Optional[str]
    Message: Optional[str]
    StartTime: Optional[str]
    Status: Optional[bool]
    SubTasks: Optional[Sequence[str]]
    Ip: Optional[Sequence["_IpDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NodesEventsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodesEventsDefinition"]:
        if not json_data:
            return None
        return cls(
            Duration=json_data.get("Duration"),
            EndTime=json_data.get("EndTime"),
            Message=json_data.get("Message"),
            StartTime=json_data.get("StartTime"),
            Status=json_data.get("Status"),
            SubTasks=json_data.get("SubTasks"),
            Ip=deserialize_list(json_data.get("Ip"), IpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodesEventsDefinition = NodesEventsDefinition


@dataclass
class IpDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpDefinition = IpDefinition


@dataclass
class SubEventsDefinition(BaseModel):
    Duration: Optional[float]
    EndTime: Optional[str]
    Message: Optional[str]
    StartTime: Optional[str]
    Status: Optional[bool]
    SubTasks: Optional[Sequence[str]]
    Ip: Optional[Sequence["_IpDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SubEventsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubEventsDefinition"]:
        if not json_data:
            return None
        return cls(
            Duration=json_data.get("Duration"),
            EndTime=json_data.get("EndTime"),
            Message=json_data.get("Message"),
            StartTime=json_data.get("StartTime"),
            Status=json_data.get("Status"),
            SubTasks=json_data.get("SubTasks"),
            Ip=deserialize_list(json_data.get("Ip"), IpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubEventsDefinition = SubEventsDefinition


@dataclass
class ParamsDefinition(BaseModel):
    ImageRef: Optional[str]
    PatchRef: Optional[str]
    SeGroupOptions: Optional[Sequence["_SeGroupOptionsDefinition"]]
    SeGroupResumeOptions: Optional[Sequence["_SeGroupResumeOptionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            ImageRef=json_data.get("ImageRef"),
            PatchRef=json_data.get("PatchRef"),
            SeGroupOptions=deserialize_list(json_data.get("SeGroupOptions"), SeGroupOptionsDefinition),
            SeGroupResumeOptions=deserialize_list(json_data.get("SeGroupResumeOptions"), SeGroupResumeOptionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParamsDefinition = ParamsDefinition


@dataclass
class SeGroupOptionsDefinition(BaseModel):
    ActionOnError: Optional[str]
    Disruptive: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SeGroupOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SeGroupOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            ActionOnError=json_data.get("ActionOnError"),
            Disruptive=json_data.get("Disruptive"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeGroupOptionsDefinition = SeGroupOptionsDefinition


@dataclass
class SeGroupResumeOptionsDefinition(BaseModel):
    ActionOnError: Optional[str]
    Disruptive: Optional[bool]
    SkipSuspended: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SeGroupResumeOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SeGroupResumeOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            ActionOnError=json_data.get("ActionOnError"),
            Disruptive=json_data.get("Disruptive"),
            SkipSuspended=json_data.get("SkipSuspended"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeGroupResumeOptionsDefinition = SeGroupResumeOptionsDefinition


@dataclass
class PatchListDefinition(BaseModel):
    PatchImagePath: Optional[str]
    PatchImageRef: Optional[str]
    PatchVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PatchListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PatchListDefinition"]:
        if not json_data:
            return None
        return cls(
            PatchImagePath=json_data.get("PatchImagePath"),
            PatchImageRef=json_data.get("PatchImageRef"),
            PatchVersion=json_data.get("PatchVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PatchListDefinition = PatchListDefinition


@dataclass
class PreviousPatchListDefinition(BaseModel):
    PatchImagePath: Optional[str]
    PatchImageRef: Optional[str]
    PatchVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PreviousPatchListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PreviousPatchListDefinition"]:
        if not json_data:
            return None
        return cls(
            PatchImagePath=json_data.get("PatchImagePath"),
            PatchImageRef=json_data.get("PatchImageRef"),
            PatchVersion=json_data.get("PatchVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PreviousPatchListDefinition = PreviousPatchListDefinition


@dataclass
class SegParamsDefinition(BaseModel):
    ImageRef: Optional[str]
    PatchRef: Optional[str]
    SeGroupOptions: Optional[Sequence["_SeGroupOptionsDefinition"]]
    SeGroupResumeOptions: Optional[Sequence["_SeGroupResumeOptionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SegParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SegParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            ImageRef=json_data.get("ImageRef"),
            PatchRef=json_data.get("PatchRef"),
            SeGroupOptions=deserialize_list(json_data.get("SeGroupOptions"), SeGroupOptionsDefinition),
            SeGroupResumeOptions=deserialize_list(json_data.get("SeGroupResumeOptions"), SeGroupResumeOptionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SegParamsDefinition = SegParamsDefinition


