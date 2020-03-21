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
    Auth: Optional[Sequence["_Auth"]]
    Id: Optional[str]
    Name: Optional[str]
    ConvergeConfig: Optional[Sequence["_ConvergeConfig"]]
    EndpointSpec: Optional[Sequence["_EndpointSpec"]]
    Labels: Optional[Sequence["_Labels"]]
    Mode: Optional[Sequence["_Mode"]]
    RollbackConfig: Optional[Sequence["_RollbackConfig"]]
    TaskSpec: Optional[Sequence["_TaskSpec"]]
    UpdateConfig: Optional[Sequence["_UpdateConfig"]]
    Ports: Optional[Sequence["_Ports"]]
    Replicated: Optional[Sequence["_Replicated"]]
    ContainerSpec: Optional[Sequence["_ContainerSpec"]]
    LogDriver: Optional[Sequence["_LogDriver"]]
    Placement: Optional[Sequence["_Placement"]]
    Resources: Optional[Sequence["_Resources"]]
    Configs: Optional[Sequence["_Configs"]]
    DnsConfig: Optional[Sequence["_DnsConfig"]]
    Healthcheck: Optional[Sequence["_Healthcheck"]]
    Hosts: Optional[Sequence["_Hosts"]]
    Mounts: Optional[Sequence["_Mounts"]]
    Privileges: Optional[Sequence["_Privileges"]]
    Secrets: Optional[Sequence["_Secrets"]]
    Platforms: Optional[Sequence["_Platforms"]]
    Limits: Optional[Sequence["_Limits"]]
    Reservation: Optional[Sequence["_Reservation"]]
    BindOptions: Optional[Sequence["_BindOptions"]]
    TmpfsOptions: Optional[Sequence["_TmpfsOptions"]]
    VolumeOptions: Optional[Sequence["_VolumeOptions"]]
    CredentialSpec: Optional[Sequence["_CredentialSpec"]]
    SeLinuxContext: Optional[Sequence["_SeLinuxContext"]]
    GenericResources: Optional[Sequence["_GenericResources"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Auth=json_data.get("Auth"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ConvergeConfig=json_data.get("ConvergeConfig"),
            EndpointSpec=json_data.get("EndpointSpec"),
            Labels=json_data.get("Labels"),
            Mode=json_data.get("Mode"),
            RollbackConfig=json_data.get("RollbackConfig"),
            TaskSpec=json_data.get("TaskSpec"),
            UpdateConfig=json_data.get("UpdateConfig"),
            Ports=json_data.get("Ports"),
            Replicated=json_data.get("Replicated"),
            ContainerSpec=json_data.get("ContainerSpec"),
            LogDriver=json_data.get("LogDriver"),
            Placement=json_data.get("Placement"),
            Resources=json_data.get("Resources"),
            Configs=json_data.get("Configs"),
            DnsConfig=json_data.get("DnsConfig"),
            Healthcheck=json_data.get("Healthcheck"),
            Hosts=json_data.get("Hosts"),
            Mounts=json_data.get("Mounts"),
            Privileges=json_data.get("Privileges"),
            Secrets=json_data.get("Secrets"),
            Platforms=json_data.get("Platforms"),
            Limits=json_data.get("Limits"),
            Reservation=json_data.get("Reservation"),
            BindOptions=json_data.get("BindOptions"),
            TmpfsOptions=json_data.get("TmpfsOptions"),
            VolumeOptions=json_data.get("VolumeOptions"),
            CredentialSpec=json_data.get("CredentialSpec"),
            SeLinuxContext=json_data.get("SeLinuxContext"),
            GenericResources=json_data.get("GenericResources"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Auth:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Auth"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Auth"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Auth = Auth


@dataclass
class ConvergeConfig:
    Delay: Optional[str]
    Timeout: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConvergeConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConvergeConfig"]:
        if not json_data:
            return None
        return cls(
            Delay=json_data.get("Delay"),
            Timeout=json_data.get("Timeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConvergeConfig = ConvergeConfig


@dataclass
class EndpointSpec:
    Mode: Optional[str]
    Ports: Optional[Sequence["_Ports"]]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointSpec"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointSpec"]:
        if not json_data:
            return None
        return cls(
            Mode=json_data.get("Mode"),
            Ports=json_data.get("Ports"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointSpec = EndpointSpec


@dataclass
class Ports:
    Name: Optional[str]
    Protocol: Optional[str]
    PublishMode: Optional[str]
    PublishedPort: Optional[float]
    TargetPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Ports"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ports"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Protocol=json_data.get("Protocol"),
            PublishMode=json_data.get("PublishMode"),
            PublishedPort=json_data.get("PublishedPort"),
            TargetPort=json_data.get("TargetPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ports = Ports


@dataclass
class Labels:
    Label: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels"]:
        if not json_data:
            return None
        return cls(
            Label=json_data.get("Label"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels = Labels


@dataclass
class Mode:
    Global: Optional[bool]
    Replicated: Optional[Sequence["_Replicated"]]

    @classmethod
    def _deserialize(
        cls: Type["_Mode"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Mode"]:
        if not json_data:
            return None
        return cls(
            Global=json_data.get("Global"),
            Replicated=json_data.get("Replicated"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Mode = Mode


@dataclass
class Replicated:
    Replicas: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Replicated"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Replicated"]:
        if not json_data:
            return None
        return cls(
            Replicas=json_data.get("Replicas"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Replicated = Replicated


@dataclass
class RollbackConfig:
    Delay: Optional[str]
    FailureAction: Optional[str]
    MaxFailureRatio: Optional[str]
    Monitor: Optional[str]
    Order: Optional[str]
    Parallelism: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RollbackConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RollbackConfig"]:
        if not json_data:
            return None
        return cls(
            Delay=json_data.get("Delay"),
            FailureAction=json_data.get("FailureAction"),
            MaxFailureRatio=json_data.get("MaxFailureRatio"),
            Monitor=json_data.get("Monitor"),
            Order=json_data.get("Order"),
            Parallelism=json_data.get("Parallelism"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RollbackConfig = RollbackConfig


@dataclass
class TaskSpec:
    ForceUpdate: Optional[float]
    Networks: Optional[Sequence[str]]
    RestartPolicy: Optional[Sequence["_RestartPolicy"]]
    Runtime: Optional[str]
    ContainerSpec: Optional[Sequence["_ContainerSpec"]]
    LogDriver: Optional[Sequence["_LogDriver"]]
    Placement: Optional[Sequence["_Placement"]]
    Resources: Optional[Sequence["_Resources"]]

    @classmethod
    def _deserialize(
        cls: Type["_TaskSpec"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaskSpec"]:
        if not json_data:
            return None
        return cls(
            ForceUpdate=json_data.get("ForceUpdate"),
            Networks=json_data.get("Networks"),
            RestartPolicy=json_data.get("RestartPolicy"),
            Runtime=json_data.get("Runtime"),
            ContainerSpec=json_data.get("ContainerSpec"),
            LogDriver=json_data.get("LogDriver"),
            Placement=json_data.get("Placement"),
            Resources=json_data.get("Resources"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaskSpec = TaskSpec


@dataclass
class RestartPolicy:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RestartPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RestartPolicy"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RestartPolicy = RestartPolicy


@dataclass
class ContainerSpec:
    Args: Optional[Sequence[str]]
    Command: Optional[Sequence[str]]
    Dir: Optional[str]
    Env: Optional[Sequence["_Env"]]
    Groups: Optional[Sequence[str]]
    Hostname: Optional[str]
    Image: Optional[str]
    Isolation: Optional[str]
    ReadOnly: Optional[bool]
    StopGracePeriod: Optional[str]
    StopSignal: Optional[str]
    User: Optional[str]
    Configs: Optional[Sequence["_Configs"]]
    DnsConfig: Optional[Sequence["_DnsConfig"]]
    Healthcheck: Optional[Sequence["_Healthcheck"]]
    Hosts: Optional[Sequence["_Hosts"]]
    Labels: Optional[Sequence["_Labels"]]
    Mounts: Optional[Sequence["_Mounts"]]
    Privileges: Optional[Sequence["_Privileges"]]
    Secrets: Optional[Sequence["_Secrets"]]

    @classmethod
    def _deserialize(
        cls: Type["_ContainerSpec"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContainerSpec"]:
        if not json_data:
            return None
        return cls(
            Args=json_data.get("Args"),
            Command=json_data.get("Command"),
            Dir=json_data.get("Dir"),
            Env=json_data.get("Env"),
            Groups=json_data.get("Groups"),
            Hostname=json_data.get("Hostname"),
            Image=json_data.get("Image"),
            Isolation=json_data.get("Isolation"),
            ReadOnly=json_data.get("ReadOnly"),
            StopGracePeriod=json_data.get("StopGracePeriod"),
            StopSignal=json_data.get("StopSignal"),
            User=json_data.get("User"),
            Configs=json_data.get("Configs"),
            DnsConfig=json_data.get("DnsConfig"),
            Healthcheck=json_data.get("Healthcheck"),
            Hosts=json_data.get("Hosts"),
            Labels=json_data.get("Labels"),
            Mounts=json_data.get("Mounts"),
            Privileges=json_data.get("Privileges"),
            Secrets=json_data.get("Secrets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContainerSpec = ContainerSpec


@dataclass
class Env:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Env"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Env"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Env = Env


@dataclass
class Configs:
    ConfigId: Optional[str]
    ConfigName: Optional[str]
    FileGid: Optional[str]
    FileMode: Optional[float]
    FileName: Optional[str]
    FileUid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Configs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Configs"]:
        if not json_data:
            return None
        return cls(
            ConfigId=json_data.get("ConfigId"),
            ConfigName=json_data.get("ConfigName"),
            FileGid=json_data.get("FileGid"),
            FileMode=json_data.get("FileMode"),
            FileName=json_data.get("FileName"),
            FileUid=json_data.get("FileUid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Configs = Configs


@dataclass
class DnsConfig:
    Nameservers: Optional[Sequence[str]]
    Options: Optional[Sequence[str]]
    Search: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DnsConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsConfig"]:
        if not json_data:
            return None
        return cls(
            Nameservers=json_data.get("Nameservers"),
            Options=json_data.get("Options"),
            Search=json_data.get("Search"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsConfig = DnsConfig


@dataclass
class Healthcheck:
    Interval: Optional[str]
    Retries: Optional[float]
    StartPeriod: Optional[str]
    Test: Optional[Sequence[str]]
    Timeout: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Healthcheck"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Healthcheck"]:
        if not json_data:
            return None
        return cls(
            Interval=json_data.get("Interval"),
            Retries=json_data.get("Retries"),
            StartPeriod=json_data.get("StartPeriod"),
            Test=json_data.get("Test"),
            Timeout=json_data.get("Timeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Healthcheck = Healthcheck


@dataclass
class Hosts:
    Host: Optional[str]
    Ip: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Hosts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Hosts"]:
        if not json_data:
            return None
        return cls(
            Host=json_data.get("Host"),
            Ip=json_data.get("Ip"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Hosts = Hosts


@dataclass
class Mounts:
    ReadOnly: Optional[bool]
    Source: Optional[str]
    Target: Optional[str]
    Type: Optional[str]
    BindOptions: Optional[Sequence["_BindOptions"]]
    TmpfsOptions: Optional[Sequence["_TmpfsOptions"]]
    VolumeOptions: Optional[Sequence["_VolumeOptions"]]

    @classmethod
    def _deserialize(
        cls: Type["_Mounts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Mounts"]:
        if not json_data:
            return None
        return cls(
            ReadOnly=json_data.get("ReadOnly"),
            Source=json_data.get("Source"),
            Target=json_data.get("Target"),
            Type=json_data.get("Type"),
            BindOptions=json_data.get("BindOptions"),
            TmpfsOptions=json_data.get("TmpfsOptions"),
            VolumeOptions=json_data.get("VolumeOptions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Mounts = Mounts


@dataclass
class BindOptions:
    Propagation: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BindOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BindOptions"]:
        if not json_data:
            return None
        return cls(
            Propagation=json_data.get("Propagation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BindOptions = BindOptions


@dataclass
class TmpfsOptions:
    Mode: Optional[float]
    SizeBytes: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TmpfsOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TmpfsOptions"]:
        if not json_data:
            return None
        return cls(
            Mode=json_data.get("Mode"),
            SizeBytes=json_data.get("SizeBytes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TmpfsOptions = TmpfsOptions


@dataclass
class VolumeOptions:
    DriverName: Optional[str]
    DriverOptions: Optional[Sequence["_DriverOptions"]]
    NoCopy: Optional[bool]
    Labels: Optional[Sequence["_Labels"]]

    @classmethod
    def _deserialize(
        cls: Type["_VolumeOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VolumeOptions"]:
        if not json_data:
            return None
        return cls(
            DriverName=json_data.get("DriverName"),
            DriverOptions=json_data.get("DriverOptions"),
            NoCopy=json_data.get("NoCopy"),
            Labels=json_data.get("Labels"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VolumeOptions = VolumeOptions


@dataclass
class DriverOptions:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DriverOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DriverOptions"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DriverOptions = DriverOptions


@dataclass
class Privileges:
    CredentialSpec: Optional[Sequence["_CredentialSpec"]]
    SeLinuxContext: Optional[Sequence["_SeLinuxContext"]]

    @classmethod
    def _deserialize(
        cls: Type["_Privileges"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Privileges"]:
        if not json_data:
            return None
        return cls(
            CredentialSpec=json_data.get("CredentialSpec"),
            SeLinuxContext=json_data.get("SeLinuxContext"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Privileges = Privileges


@dataclass
class CredentialSpec:
    File: Optional[str]
    Registry: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CredentialSpec"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CredentialSpec"]:
        if not json_data:
            return None
        return cls(
            File=json_data.get("File"),
            Registry=json_data.get("Registry"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CredentialSpec = CredentialSpec


@dataclass
class SeLinuxContext:
    Disable: Optional[bool]
    Level: Optional[str]
    Role: Optional[str]
    Type: Optional[str]
    User: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SeLinuxContext"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SeLinuxContext"]:
        if not json_data:
            return None
        return cls(
            Disable=json_data.get("Disable"),
            Level=json_data.get("Level"),
            Role=json_data.get("Role"),
            Type=json_data.get("Type"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeLinuxContext = SeLinuxContext


@dataclass
class Secrets:
    FileGid: Optional[str]
    FileMode: Optional[float]
    FileName: Optional[str]
    FileUid: Optional[str]
    SecretId: Optional[str]
    SecretName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Secrets"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Secrets"]:
        if not json_data:
            return None
        return cls(
            FileGid=json_data.get("FileGid"),
            FileMode=json_data.get("FileMode"),
            FileName=json_data.get("FileName"),
            FileUid=json_data.get("FileUid"),
            SecretId=json_data.get("SecretId"),
            SecretName=json_data.get("SecretName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Secrets = Secrets


@dataclass
class LogDriver:
    Name: Optional[str]
    Options: Optional[Sequence["_Options"]]

    @classmethod
    def _deserialize(
        cls: Type["_LogDriver"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogDriver"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Options=json_data.get("Options"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogDriver = LogDriver


@dataclass
class Options:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Options"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Options"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Options = Options


@dataclass
class Placement:
    Constraints: Optional[Sequence[str]]
    Prefs: Optional[Sequence[str]]
    Platforms: Optional[Sequence["_Platforms"]]

    @classmethod
    def _deserialize(
        cls: Type["_Placement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Placement"]:
        if not json_data:
            return None
        return cls(
            Constraints=json_data.get("Constraints"),
            Prefs=json_data.get("Prefs"),
            Platforms=json_data.get("Platforms"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Placement = Placement


@dataclass
class Platforms:
    Architecture: Optional[str]
    Os: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Platforms"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Platforms"]:
        if not json_data:
            return None
        return cls(
            Architecture=json_data.get("Architecture"),
            Os=json_data.get("Os"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Platforms = Platforms


@dataclass
class Resources:
    Limits: Optional[Sequence["_Limits"]]
    Reservation: Optional[Sequence["_Reservation"]]

    @classmethod
    def _deserialize(
        cls: Type["_Resources"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Resources"]:
        if not json_data:
            return None
        return cls(
            Limits=json_data.get("Limits"),
            Reservation=json_data.get("Reservation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Resources = Resources


@dataclass
class Limits:
    MemoryBytes: Optional[float]
    NanoCpus: Optional[float]
    GenericResources: Optional[Sequence["_GenericResources"]]

    @classmethod
    def _deserialize(
        cls: Type["_Limits"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Limits"]:
        if not json_data:
            return None
        return cls(
            MemoryBytes=json_data.get("MemoryBytes"),
            NanoCpus=json_data.get("NanoCpus"),
            GenericResources=json_data.get("GenericResources"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Limits = Limits


@dataclass
class GenericResources:
    DiscreteResourcesSpec: Optional[Sequence[str]]
    NamedResourcesSpec: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_GenericResources"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GenericResources"]:
        if not json_data:
            return None
        return cls(
            DiscreteResourcesSpec=json_data.get("DiscreteResourcesSpec"),
            NamedResourcesSpec=json_data.get("NamedResourcesSpec"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GenericResources = GenericResources


@dataclass
class Reservation:
    MemoryBytes: Optional[float]
    NanoCpus: Optional[float]
    GenericResources: Optional[Sequence["_GenericResources"]]

    @classmethod
    def _deserialize(
        cls: Type["_Reservation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Reservation"]:
        if not json_data:
            return None
        return cls(
            MemoryBytes=json_data.get("MemoryBytes"),
            NanoCpus=json_data.get("NanoCpus"),
            GenericResources=json_data.get("GenericResources"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Reservation = Reservation


@dataclass
class UpdateConfig:
    Delay: Optional[str]
    FailureAction: Optional[str]
    MaxFailureRatio: Optional[str]
    Monitor: Optional[str]
    Order: Optional[str]
    Parallelism: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_UpdateConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UpdateConfig"]:
        if not json_data:
            return None
        return cls(
            Delay=json_data.get("Delay"),
            FailureAction=json_data.get("FailureAction"),
            MaxFailureRatio=json_data.get("MaxFailureRatio"),
            Monitor=json_data.get("Monitor"),
            Order=json_data.get("Order"),
            Parallelism=json_data.get("Parallelism"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UpdateConfig = UpdateConfig


