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
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    TaskRoleArn: Optional[str]
    EphemeralStorage: Optional[Sequence["_EphemeralStorageDefinition"]]
    InferenceAccelerator: Optional[Sequence["_InferenceAcceleratorDefinition"]]
    PlacementConstraints: Optional[Sequence["_PlacementConstraintsDefinition"]]
    ProxyConfiguration: Optional[Sequence["_ProxyConfigurationDefinition"]]
    Volume: Optional[Sequence["_VolumeDefinition"]]

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
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            TaskRoleArn=json_data.get("TaskRoleArn"),
            EphemeralStorage=deserialize_list(json_data.get("EphemeralStorage"), EphemeralStorageDefinition),
            InferenceAccelerator=deserialize_list(json_data.get("InferenceAccelerator"), InferenceAcceleratorDefinition),
            PlacementConstraints=deserialize_list(json_data.get("PlacementConstraints"), PlacementConstraintsDefinition),
            ProxyConfiguration=deserialize_list(json_data.get("ProxyConfiguration"), ProxyConfigurationDefinition),
            Volume=deserialize_list(json_data.get("Volume"), VolumeDefinition),
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
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class EphemeralStorageDefinition(BaseModel):
    SizeInGib: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_EphemeralStorageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EphemeralStorageDefinition"]:
        if not json_data:
            return None
        return cls(
            SizeInGib=json_data.get("SizeInGib"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EphemeralStorageDefinition = EphemeralStorageDefinition


@dataclass
class InferenceAcceleratorDefinition(BaseModel):
    DeviceName: Optional[str]
    DeviceType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InferenceAcceleratorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InferenceAcceleratorDefinition"]:
        if not json_data:
            return None
        return cls(
            DeviceName=json_data.get("DeviceName"),
            DeviceType=json_data.get("DeviceType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InferenceAcceleratorDefinition = InferenceAcceleratorDefinition


@dataclass
class PlacementConstraintsDefinition(BaseModel):
    Expression: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlacementConstraintsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlacementConstraintsDefinition"]:
        if not json_data:
            return None
        return cls(
            Expression=json_data.get("Expression"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlacementConstraintsDefinition = PlacementConstraintsDefinition


@dataclass
class ProxyConfigurationDefinition(BaseModel):
    ContainerName: Optional[str]
    Properties: Optional[Sequence["_PropertiesDefinition"]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProxyConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProxyConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            ContainerName=json_data.get("ContainerName"),
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProxyConfigurationDefinition = ProxyConfigurationDefinition


@dataclass
class PropertiesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition = PropertiesDefinition


@dataclass
class VolumeDefinition(BaseModel):
    HostPath: Optional[str]
    Name: Optional[str]
    DockerVolumeConfiguration: Optional[Sequence["_DockerVolumeConfigurationDefinition"]]
    EfsVolumeConfiguration: Optional[Sequence["_EfsVolumeConfigurationDefinition"]]
    FsxWindowsFileServerVolumeConfiguration: Optional[Sequence["_FsxWindowsFileServerVolumeConfigurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VolumeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VolumeDefinition"]:
        if not json_data:
            return None
        return cls(
            HostPath=json_data.get("HostPath"),
            Name=json_data.get("Name"),
            DockerVolumeConfiguration=deserialize_list(json_data.get("DockerVolumeConfiguration"), DockerVolumeConfigurationDefinition),
            EfsVolumeConfiguration=deserialize_list(json_data.get("EfsVolumeConfiguration"), EfsVolumeConfigurationDefinition),
            FsxWindowsFileServerVolumeConfiguration=deserialize_list(json_data.get("FsxWindowsFileServerVolumeConfiguration"), FsxWindowsFileServerVolumeConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VolumeDefinition = VolumeDefinition


@dataclass
class DockerVolumeConfigurationDefinition(BaseModel):
    Autoprovision: Optional[bool]
    Driver: Optional[str]
    DriverOpts: Optional[Sequence["_DriverOptsDefinition"]]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Scope: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DockerVolumeConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DockerVolumeConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Autoprovision=json_data.get("Autoprovision"),
            Driver=json_data.get("Driver"),
            DriverOpts=deserialize_list(json_data.get("DriverOpts"), DriverOptsDefinition),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Scope=json_data.get("Scope"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DockerVolumeConfigurationDefinition = DockerVolumeConfigurationDefinition


@dataclass
class DriverOptsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DriverOptsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DriverOptsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DriverOptsDefinition = DriverOptsDefinition


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
class EfsVolumeConfigurationDefinition(BaseModel):
    FileSystemId: Optional[str]
    RootDirectory: Optional[str]
    TransitEncryption: Optional[str]
    TransitEncryptionPort: Optional[float]
    AuthorizationConfig: Optional[Sequence["_AuthorizationConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EfsVolumeConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EfsVolumeConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            FileSystemId=json_data.get("FileSystemId"),
            RootDirectory=json_data.get("RootDirectory"),
            TransitEncryption=json_data.get("TransitEncryption"),
            TransitEncryptionPort=json_data.get("TransitEncryptionPort"),
            AuthorizationConfig=deserialize_list(json_data.get("AuthorizationConfig"), AuthorizationConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EfsVolumeConfigurationDefinition = EfsVolumeConfigurationDefinition


@dataclass
class AuthorizationConfigDefinition(BaseModel):
    CredentialsParameter: Optional[str]
    Domain: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthorizationConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthorizationConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CredentialsParameter=json_data.get("CredentialsParameter"),
            Domain=json_data.get("Domain"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthorizationConfigDefinition = AuthorizationConfigDefinition


@dataclass
class FsxWindowsFileServerVolumeConfigurationDefinition(BaseModel):
    FileSystemId: Optional[str]
    RootDirectory: Optional[str]
    AuthorizationConfig: Optional[Sequence["_AuthorizationConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FsxWindowsFileServerVolumeConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FsxWindowsFileServerVolumeConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            FileSystemId=json_data.get("FileSystemId"),
            RootDirectory=json_data.get("RootDirectory"),
            AuthorizationConfig=deserialize_list(json_data.get("AuthorizationConfig"), AuthorizationConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FsxWindowsFileServerVolumeConfigurationDefinition = FsxWindowsFileServerVolumeConfigurationDefinition


