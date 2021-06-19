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
    EnablePatchRollback: Optional[bool]
    EnableRollback: Optional[bool]
    EndTime: Optional[str]
    Id: Optional[str]
    ImageRef: Optional[str]
    Name: Optional[str]
    NodeType: Optional[str]
    ObjCloudRef: Optional[str]
    PatchImageRef: Optional[str]
    StartTime: Optional[str]
    TasksCompleted: Optional[float]
    TenantRef: Optional[str]
    TotalTasks: Optional[float]
    UpgradeOps: Optional[str]
    Uuid: Optional[str]
    Version: Optional[str]
    State: Optional[Sequence["_StateDefinition"]]

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
            EnablePatchRollback=json_data.get("EnablePatchRollback"),
            EnableRollback=json_data.get("EnableRollback"),
            EndTime=json_data.get("EndTime"),
            Id=json_data.get("Id"),
            ImageRef=json_data.get("ImageRef"),
            Name=json_data.get("Name"),
            NodeType=json_data.get("NodeType"),
            ObjCloudRef=json_data.get("ObjCloudRef"),
            PatchImageRef=json_data.get("PatchImageRef"),
            StartTime=json_data.get("StartTime"),
            TasksCompleted=json_data.get("TasksCompleted"),
            TenantRef=json_data.get("TenantRef"),
            TotalTasks=json_data.get("TotalTasks"),
            UpgradeOps=json_data.get("UpgradeOps"),
            Uuid=json_data.get("Uuid"),
            Version=json_data.get("Version"),
            State=deserialize_list(json_data.get("State"), StateDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


