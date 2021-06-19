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
    ClusterId: Optional[str]
    Hostname: Optional[str]
    Id: Optional[str]
    InstanceId: Optional[str]
    KeyIds: Optional[Sequence[str]]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Password: Optional[str]
    SecurityGroups: Optional[Sequence[str]]
    State: Optional[str]
    Unschedulable: Optional[float]
    WorkerConfig: Optional[Sequence["_WorkerConfigDefinition"]]
    WorkerConfigOverrides: Optional[Sequence["_WorkerConfigOverridesDefinition"]]

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
            ClusterId=json_data.get("ClusterId"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            InstanceId=json_data.get("InstanceId"),
            KeyIds=json_data.get("KeyIds"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Password=json_data.get("Password"),
            SecurityGroups=json_data.get("SecurityGroups"),
            State=json_data.get("State"),
            Unschedulable=json_data.get("Unschedulable"),
            WorkerConfig=deserialize_list(json_data.get("WorkerConfig"), WorkerConfigDefinition),
            WorkerConfigOverrides=deserialize_list(json_data.get("WorkerConfigOverrides"), WorkerConfigOverridesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class WorkerConfigDefinition(BaseModel):
    DesiredPodNum: Optional[float]
    DockerGraphPath: Optional[str]
    ExtraArgs: Optional[Sequence[str]]
    IsSchedule: Optional[bool]
    MountTarget: Optional[str]
    UserData: Optional[str]
    DataDisk: Optional[Sequence["_DataDiskDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WorkerConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkerConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            DesiredPodNum=json_data.get("DesiredPodNum"),
            DockerGraphPath=json_data.get("DockerGraphPath"),
            ExtraArgs=json_data.get("ExtraArgs"),
            IsSchedule=json_data.get("IsSchedule"),
            MountTarget=json_data.get("MountTarget"),
            UserData=json_data.get("UserData"),
            DataDisk=deserialize_list(json_data.get("DataDisk"), DataDiskDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkerConfigDefinition = WorkerConfigDefinition


@dataclass
class DataDiskDefinition(BaseModel):
    AutoFormatAndMount: Optional[bool]
    DiskSize: Optional[float]
    DiskType: Optional[str]
    FileSystem: Optional[str]
    MountTarget: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataDiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataDiskDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoFormatAndMount=json_data.get("AutoFormatAndMount"),
            DiskSize=json_data.get("DiskSize"),
            DiskType=json_data.get("DiskType"),
            FileSystem=json_data.get("FileSystem"),
            MountTarget=json_data.get("MountTarget"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataDiskDefinition = DataDiskDefinition


@dataclass
class WorkerConfigOverridesDefinition(BaseModel):
    DesiredPodNum: Optional[float]
    DockerGraphPath: Optional[str]
    ExtraArgs: Optional[Sequence[str]]
    IsSchedule: Optional[bool]
    MountTarget: Optional[str]
    UserData: Optional[str]
    DataDisk: Optional[Sequence["_DataDiskDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WorkerConfigOverridesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkerConfigOverridesDefinition"]:
        if not json_data:
            return None
        return cls(
            DesiredPodNum=json_data.get("DesiredPodNum"),
            DockerGraphPath=json_data.get("DockerGraphPath"),
            ExtraArgs=json_data.get("ExtraArgs"),
            IsSchedule=json_data.get("IsSchedule"),
            MountTarget=json_data.get("MountTarget"),
            UserData=json_data.get("UserData"),
            DataDisk=deserialize_list(json_data.get("DataDisk"), DataDiskDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkerConfigOverridesDefinition = WorkerConfigOverridesDefinition


