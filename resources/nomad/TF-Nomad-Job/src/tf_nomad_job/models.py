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
    AllocationIds: Optional[Sequence[str]]
    Datacenters: Optional[Sequence[str]]
    DeploymentId: Optional[str]
    DeploymentStatus: Optional[str]
    DeregisterOnDestroy: Optional[bool]
    DeregisterOnIdChange: Optional[bool]
    Detach: Optional[bool]
    Id: Optional[str]
    Jobspec: Optional[str]
    Json: Optional[bool]
    ModifyIndex: Optional[str]
    Name: Optional[str]
    Namespace: Optional[str]
    PolicyOverride: Optional[bool]
    PurgeOnDestroy: Optional[bool]
    Region: Optional[str]
    TaskGroups: Optional[Sequence["_TaskGroupsDefinition6"]]
    Type: Optional[str]
    Hcl2: Optional[Sequence["_Hcl2Definition"]]
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
            AllocationIds=json_data.get("AllocationIds"),
            Datacenters=json_data.get("Datacenters"),
            DeploymentId=json_data.get("DeploymentId"),
            DeploymentStatus=json_data.get("DeploymentStatus"),
            DeregisterOnDestroy=json_data.get("DeregisterOnDestroy"),
            DeregisterOnIdChange=json_data.get("DeregisterOnIdChange"),
            Detach=json_data.get("Detach"),
            Id=json_data.get("Id"),
            Jobspec=json_data.get("Jobspec"),
            Json=json_data.get("Json"),
            ModifyIndex=json_data.get("ModifyIndex"),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            PolicyOverride=json_data.get("PolicyOverride"),
            PurgeOnDestroy=json_data.get("PurgeOnDestroy"),
            Region=json_data.get("Region"),
            TaskGroups=deserialize_list(json_data.get("TaskGroups"), TaskGroupsDefinition6),
            Type=json_data.get("Type"),
            Hcl2=deserialize_list(json_data.get("Hcl2"), Hcl2Definition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TaskGroupsDefinition6(BaseModel):
    Count: Optional[float]
    Meta: Optional[Sequence["_TaskGroupsDefinition"]]
    Name: Optional[str]
    Task: Optional[Sequence["_TaskGroupsDefinition4"]]
    Volumes: Optional[Sequence["_TaskGroupsDefinition5"]]

    @classmethod
    def _deserialize(
        cls: Type["_TaskGroupsDefinition6"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaskGroupsDefinition6"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
            Meta=deserialize_list(json_data.get("Meta"), TaskGroupsDefinition),
            Name=json_data.get("Name"),
            Task=deserialize_list(json_data.get("Task"), TaskGroupsDefinition4),
            Volumes=deserialize_list(json_data.get("Volumes"), TaskGroupsDefinition5),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaskGroupsDefinition6 = TaskGroupsDefinition6


@dataclass
class TaskGroupsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TaskGroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaskGroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaskGroupsDefinition = TaskGroupsDefinition


@dataclass
class TaskGroupsDefinition4(BaseModel):
    Driver: Optional[str]
    Meta: Optional[Sequence["_TaskGroupsDefinition2"]]
    Name: Optional[str]
    VolumeMounts: Optional[Sequence["_TaskGroupsDefinition3"]]

    @classmethod
    def _deserialize(
        cls: Type["_TaskGroupsDefinition4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaskGroupsDefinition4"]:
        if not json_data:
            return None
        return cls(
            Driver=json_data.get("Driver"),
            Meta=deserialize_list(json_data.get("Meta"), TaskGroupsDefinition2),
            Name=json_data.get("Name"),
            VolumeMounts=deserialize_list(json_data.get("VolumeMounts"), TaskGroupsDefinition3),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaskGroupsDefinition4 = TaskGroupsDefinition4


@dataclass
class TaskGroupsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TaskGroupsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaskGroupsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaskGroupsDefinition2 = TaskGroupsDefinition2


@dataclass
class TaskGroupsDefinition3(BaseModel):
    Destination: Optional[str]
    ReadOnly: Optional[bool]
    Volume: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TaskGroupsDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaskGroupsDefinition3"]:
        if not json_data:
            return None
        return cls(
            Destination=json_data.get("Destination"),
            ReadOnly=json_data.get("ReadOnly"),
            Volume=json_data.get("Volume"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaskGroupsDefinition3 = TaskGroupsDefinition3


@dataclass
class TaskGroupsDefinition5(BaseModel):
    Name: Optional[str]
    ReadOnly: Optional[bool]
    Source: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TaskGroupsDefinition5"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaskGroupsDefinition5"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            ReadOnly=json_data.get("ReadOnly"),
            Source=json_data.get("Source"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaskGroupsDefinition5 = TaskGroupsDefinition5


@dataclass
class Hcl2Definition(BaseModel):
    AllowFs: Optional[bool]
    Enabled: Optional[bool]
    Vars: Optional[Sequence["_VarsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_Hcl2Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Hcl2Definition"]:
        if not json_data:
            return None
        return cls(
            AllowFs=json_data.get("AllowFs"),
            Enabled=json_data.get("Enabled"),
            Vars=deserialize_list(json_data.get("Vars"), VarsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_Hcl2Definition = Hcl2Definition


@dataclass
class VarsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VarsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VarsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VarsDefinition = VarsDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


