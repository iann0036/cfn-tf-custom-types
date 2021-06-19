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
    ContainerGroupName: Optional[str]
    Cpu: Optional[float]
    Id: Optional[str]
    InstanceType: Optional[str]
    Memory: Optional[float]
    RamRoleName: Optional[str]
    ResourceGroupId: Optional[str]
    RestartPolicy: Optional[str]
    SecurityGroupId: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    VswitchId: Optional[str]
    ZoneId: Optional[str]
    Containers: Optional[Sequence["_ContainersDefinition"]]
    DnsConfig: Optional[Sequence["_DnsConfigDefinition"]]
    EciSecurityContext: Optional[Sequence["_EciSecurityContextDefinition"]]
    HostAliases: Optional[Sequence["_HostAliasesDefinition"]]
    InitContainers: Optional[Sequence["_InitContainersDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    Volumes: Optional[Sequence["_VolumesDefinition"]]

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
            ContainerGroupName=json_data.get("ContainerGroupName"),
            Cpu=json_data.get("Cpu"),
            Id=json_data.get("Id"),
            InstanceType=json_data.get("InstanceType"),
            Memory=json_data.get("Memory"),
            RamRoleName=json_data.get("RamRoleName"),
            ResourceGroupId=json_data.get("ResourceGroupId"),
            RestartPolicy=json_data.get("RestartPolicy"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            Status=json_data.get("Status"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            VswitchId=json_data.get("VswitchId"),
            ZoneId=json_data.get("ZoneId"),
            Containers=deserialize_list(json_data.get("Containers"), ContainersDefinition),
            DnsConfig=deserialize_list(json_data.get("DnsConfig"), DnsConfigDefinition),
            EciSecurityContext=deserialize_list(json_data.get("EciSecurityContext"), EciSecurityContextDefinition),
            HostAliases=deserialize_list(json_data.get("HostAliases"), HostAliasesDefinition),
            InitContainers=deserialize_list(json_data.get("InitContainers"), InitContainersDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            Volumes=deserialize_list(json_data.get("Volumes"), VolumesDefinition),
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
class ContainersDefinition(BaseModel):
    Args: Optional[Sequence[str]]
    Commands: Optional[Sequence[str]]
    Cpu: Optional[float]
    Gpu: Optional[float]
    Image: Optional[str]
    ImagePullPolicy: Optional[str]
    Memory: Optional[float]
    Name: Optional[str]
    WorkingDir: Optional[str]
    EnvironmentVars: Optional[Sequence["_EnvironmentVarsDefinition"]]
    Ports: Optional[Sequence["_PortsDefinition"]]
    VolumeMounts: Optional[Sequence["_VolumeMountsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ContainersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContainersDefinition"]:
        if not json_data:
            return None
        return cls(
            Args=json_data.get("Args"),
            Commands=json_data.get("Commands"),
            Cpu=json_data.get("Cpu"),
            Gpu=json_data.get("Gpu"),
            Image=json_data.get("Image"),
            ImagePullPolicy=json_data.get("ImagePullPolicy"),
            Memory=json_data.get("Memory"),
            Name=json_data.get("Name"),
            WorkingDir=json_data.get("WorkingDir"),
            EnvironmentVars=deserialize_list(json_data.get("EnvironmentVars"), EnvironmentVarsDefinition),
            Ports=deserialize_list(json_data.get("Ports"), PortsDefinition),
            VolumeMounts=deserialize_list(json_data.get("VolumeMounts"), VolumeMountsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContainersDefinition = ContainersDefinition


@dataclass
class EnvironmentVarsDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvironmentVarsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvironmentVarsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvironmentVarsDefinition = EnvironmentVarsDefinition


@dataclass
class PortsDefinition(BaseModel):
    Port: Optional[float]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PortsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortsDefinition"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortsDefinition = PortsDefinition


@dataclass
class VolumeMountsDefinition(BaseModel):
    MountPath: Optional[str]
    Name: Optional[str]
    ReadOnly: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_VolumeMountsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VolumeMountsDefinition"]:
        if not json_data:
            return None
        return cls(
            MountPath=json_data.get("MountPath"),
            Name=json_data.get("Name"),
            ReadOnly=json_data.get("ReadOnly"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VolumeMountsDefinition = VolumeMountsDefinition


@dataclass
class DnsConfigDefinition(BaseModel):
    NameServers: Optional[Sequence[str]]
    Searches: Optional[Sequence[str]]
    Options: Optional[Sequence["_OptionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DnsConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            NameServers=json_data.get("NameServers"),
            Searches=json_data.get("Searches"),
            Options=deserialize_list(json_data.get("Options"), OptionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsConfigDefinition = DnsConfigDefinition


@dataclass
class OptionsDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OptionsDefinition = OptionsDefinition


@dataclass
class EciSecurityContextDefinition(BaseModel):
    Sysctls: Optional[Sequence["_SysctlsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EciSecurityContextDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EciSecurityContextDefinition"]:
        if not json_data:
            return None
        return cls(
            Sysctls=deserialize_list(json_data.get("Sysctls"), SysctlsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EciSecurityContextDefinition = EciSecurityContextDefinition


@dataclass
class SysctlsDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SysctlsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SysctlsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SysctlsDefinition = SysctlsDefinition


@dataclass
class HostAliasesDefinition(BaseModel):
    Hostnames: Optional[Sequence[str]]
    Ip: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HostAliasesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostAliasesDefinition"]:
        if not json_data:
            return None
        return cls(
            Hostnames=json_data.get("Hostnames"),
            Ip=json_data.get("Ip"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostAliasesDefinition = HostAliasesDefinition


@dataclass
class InitContainersDefinition(BaseModel):
    Args: Optional[Sequence[str]]
    Commands: Optional[Sequence[str]]
    Cpu: Optional[float]
    Gpu: Optional[float]
    Image: Optional[str]
    ImagePullPolicy: Optional[str]
    Memory: Optional[float]
    Name: Optional[str]
    WorkingDir: Optional[str]
    EnvironmentVars: Optional[Sequence["_EnvironmentVarsDefinition"]]
    Ports: Optional[Sequence["_PortsDefinition"]]
    VolumeMounts: Optional[Sequence["_VolumeMountsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InitContainersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InitContainersDefinition"]:
        if not json_data:
            return None
        return cls(
            Args=json_data.get("Args"),
            Commands=json_data.get("Commands"),
            Cpu=json_data.get("Cpu"),
            Gpu=json_data.get("Gpu"),
            Image=json_data.get("Image"),
            ImagePullPolicy=json_data.get("ImagePullPolicy"),
            Memory=json_data.get("Memory"),
            Name=json_data.get("Name"),
            WorkingDir=json_data.get("WorkingDir"),
            EnvironmentVars=deserialize_list(json_data.get("EnvironmentVars"), EnvironmentVarsDefinition),
            Ports=deserialize_list(json_data.get("Ports"), PortsDefinition),
            VolumeMounts=deserialize_list(json_data.get("VolumeMounts"), VolumeMountsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InitContainersDefinition = InitContainersDefinition


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


@dataclass
class VolumesDefinition(BaseModel):
    DiskVolumeDiskId: Optional[str]
    DiskVolumeFsType: Optional[str]
    FlexVolumeDriver: Optional[str]
    FlexVolumeFsType: Optional[str]
    FlexVolumeOptions: Optional[str]
    Name: Optional[str]
    NfsVolumePath: Optional[str]
    NfsVolumeReadOnly: Optional[bool]
    NfsVolumeServer: Optional[str]
    Type: Optional[str]
    ConfigFileVolumeConfigFileToPaths: Optional[Sequence["_ConfigFileVolumeConfigFileToPathsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VolumesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VolumesDefinition"]:
        if not json_data:
            return None
        return cls(
            DiskVolumeDiskId=json_data.get("DiskVolumeDiskId"),
            DiskVolumeFsType=json_data.get("DiskVolumeFsType"),
            FlexVolumeDriver=json_data.get("FlexVolumeDriver"),
            FlexVolumeFsType=json_data.get("FlexVolumeFsType"),
            FlexVolumeOptions=json_data.get("FlexVolumeOptions"),
            Name=json_data.get("Name"),
            NfsVolumePath=json_data.get("NfsVolumePath"),
            NfsVolumeReadOnly=json_data.get("NfsVolumeReadOnly"),
            NfsVolumeServer=json_data.get("NfsVolumeServer"),
            Type=json_data.get("Type"),
            ConfigFileVolumeConfigFileToPaths=deserialize_list(json_data.get("ConfigFileVolumeConfigFileToPaths"), ConfigFileVolumeConfigFileToPathsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VolumesDefinition = VolumesDefinition


@dataclass
class ConfigFileVolumeConfigFileToPathsDefinition(BaseModel):
    Content: Optional[str]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigFileVolumeConfigFileToPathsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigFileVolumeConfigFileToPathsDefinition"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigFileVolumeConfigFileToPathsDefinition = ConfigFileVolumeConfigFileToPathsDefinition


