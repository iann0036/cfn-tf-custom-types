# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    AllocationIds: Optional[Sequence[str]]
    Datacenters: Optional[Sequence[str]]
    DeploymentId: Optional[str]
    DeploymentStatus: Optional[str]
    DeregisterOnDestroy: Optional[bool]
    DeregisterOnIdChange: Optional[bool]
    Detach: Optional[bool]
    Jobspec: Optional[str]
    Json: Optional[bool]
    ModifyIndex: Optional[str]
    Name: Optional[str]
    Namespace: Optional[str]
    PolicyOverride: Optional[bool]
    Region: Optional[str]
    TaskGroups: Optional[Sequence["_TaskGroups"]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AllocationIds=json_data.get("AllocationIds"),
            Datacenters=json_data.get("Datacenters"),
            DeploymentId=json_data.get("DeploymentId"),
            DeploymentStatus=json_data.get("DeploymentStatus"),
            DeregisterOnDestroy=json_data.get("DeregisterOnDestroy"),
            DeregisterOnIdChange=json_data.get("DeregisterOnIdChange"),
            Detach=json_data.get("Detach"),
            Jobspec=json_data.get("Jobspec"),
            Json=json_data.get("Json"),
            ModifyIndex=json_data.get("ModifyIndex"),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            PolicyOverride=json_data.get("PolicyOverride"),
            Region=json_data.get("Region"),
            TaskGroups=json_data.get("TaskGroups"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TaskGroups:
    Count: Optional[float]
    Meta: Optional[Sequence["_Meta"]]
    Name: Optional[str]
    Task: Optional[Sequence["_Task"]]
    Volumes: Optional[Sequence["_Volumes"]]

    @classmethod
    def _deserialize(
        cls: Type["_TaskGroups"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaskGroups"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
            Meta=json_data.get("Meta"),
            Name=json_data.get("Name"),
            Task=json_data.get("Task"),
            Volumes=json_data.get("Volumes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaskGroups = TaskGroups


@dataclass
class Meta:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Meta"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Meta"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Meta = Meta


@dataclass
class Task:
    Driver: Optional[str]
    Meta: Optional[Sequence["_Meta2"]]
    Name: Optional[str]
    VolumeMounts: Optional[Sequence["_VolumeMounts"]]

    @classmethod
    def _deserialize(
        cls: Type["_Task"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Task"]:
        if not json_data:
            return None
        return cls(
            Driver=json_data.get("Driver"),
            Meta=json_data.get("Meta"),
            Name=json_data.get("Name"),
            VolumeMounts=json_data.get("VolumeMounts"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Task = Task


@dataclass
class Meta2:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Meta2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Meta2"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Meta2 = Meta2


@dataclass
class VolumeMounts:
    Destination: Optional[str]
    ReadOnly: Optional[bool]
    Volume: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VolumeMounts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VolumeMounts"]:
        if not json_data:
            return None
        return cls(
            Destination=json_data.get("Destination"),
            ReadOnly=json_data.get("ReadOnly"),
            Volume=json_data.get("Volume"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VolumeMounts = VolumeMounts


@dataclass
class Volumes:
    Name: Optional[str]
    ReadOnly: Optional[bool]
    Source: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Volumes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Volumes"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            ReadOnly=json_data.get("ReadOnly"),
            Source=json_data.get("Source"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Volumes = Volumes


