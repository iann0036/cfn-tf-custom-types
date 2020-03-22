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
    Arn: Optional[str]
    ContainerDefinitions: Optional[str]
    Cpu: Optional[str]
    ExecutionRoleArn: Optional[str]
    Family: Optional[str]
    Id: Optional[str]
    IpcMode: Optional[str]
    Memory: Optional[str]
    NetworkMode: Optional[str]
    PidMode: Optional[str]
    RequiresCompatibilities: Optional[Sequence[str]]
    Revision: Optional[float]
    Tags: Optional[Sequence["_Tags"]]
    TaskRoleArn: Optional[str]
    PlacementConstraints: Optional[Sequence["_PlacementConstraints"]]
    ProxyConfiguration: Optional[Sequence["_ProxyConfiguration"]]
    Volume: Optional[Sequence["_Volume"]]
    DockerVolumeConfiguration: Optional[Sequence["_DockerVolumeConfiguration"]]
    EfsVolumeConfiguration: Optional[Sequence["_EfsVolumeConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            ContainerDefinitions=json_data.get("ContainerDefinitions"),
            Cpu=json_data.get("Cpu"),
            ExecutionRoleArn=json_data.get("ExecutionRoleArn"),
            Family=json_data.get("Family"),
            Id=json_data.get("Id"),
            IpcMode=json_data.get("IpcMode"),
            Memory=json_data.get("Memory"),
            NetworkMode=json_data.get("NetworkMode"),
            PidMode=json_data.get("PidMode"),
            RequiresCompatibilities=json_data.get("RequiresCompatibilities"),
            Revision=json_data.get("Revision"),
            Tags=json_data.get("Tags"),
            TaskRoleArn=json_data.get("TaskRoleArn"),
            PlacementConstraints=json_data.get("PlacementConstraints"),
            ProxyConfiguration=json_data.get("ProxyConfiguration"),
            Volume=json_data.get("Volume"),
            DockerVolumeConfiguration=json_data.get("DockerVolumeConfiguration"),
            EfsVolumeConfiguration=json_data.get("EfsVolumeConfiguration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class PlacementConstraints:
    Expression: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlacementConstraints"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlacementConstraints"]:
        if not json_data:
            return None
        return cls(
            Expression=json_data.get("Expression"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlacementConstraints = PlacementConstraints


@dataclass
class ProxyConfiguration:
    ContainerName: Optional[str]
    Properties: Optional[Sequence["_Properties"]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProxyConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProxyConfiguration"]:
        if not json_data:
            return None
        return cls(
            ContainerName=json_data.get("ContainerName"),
            Properties=json_data.get("Properties"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProxyConfiguration = ProxyConfiguration


@dataclass
class Properties:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Properties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Properties"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Properties = Properties


@dataclass
class Volume:
    HostPath: Optional[str]
    Name: Optional[str]
    DockerVolumeConfiguration: Optional[Sequence["_DockerVolumeConfiguration"]]
    EfsVolumeConfiguration: Optional[Sequence["_EfsVolumeConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_Volume"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Volume"]:
        if not json_data:
            return None
        return cls(
            HostPath=json_data.get("HostPath"),
            Name=json_data.get("Name"),
            DockerVolumeConfiguration=json_data.get("DockerVolumeConfiguration"),
            EfsVolumeConfiguration=json_data.get("EfsVolumeConfiguration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Volume = Volume


@dataclass
class DockerVolumeConfiguration:
    Autoprovision: Optional[bool]
    Driver: Optional[str]
    DriverOpts: Optional[Sequence["_DriverOpts"]]
    Labels: Optional[Sequence["_Labels"]]
    Scope: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DockerVolumeConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DockerVolumeConfiguration"]:
        if not json_data:
            return None
        return cls(
            Autoprovision=json_data.get("Autoprovision"),
            Driver=json_data.get("Driver"),
            DriverOpts=json_data.get("DriverOpts"),
            Labels=json_data.get("Labels"),
            Scope=json_data.get("Scope"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DockerVolumeConfiguration = DockerVolumeConfiguration


@dataclass
class DriverOpts:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DriverOpts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DriverOpts"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DriverOpts = DriverOpts


@dataclass
class Labels:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels = Labels


@dataclass
class EfsVolumeConfiguration:
    FileSystemId: Optional[str]
    RootDirectory: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EfsVolumeConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EfsVolumeConfiguration"]:
        if not json_data:
            return None
        return cls(
            FileSystemId=json_data.get("FileSystemId"),
            RootDirectory=json_data.get("RootDirectory"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EfsVolumeConfiguration = EfsVolumeConfiguration


