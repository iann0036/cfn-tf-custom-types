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
    DnsNameLabel: Optional[str]
    ExposedPort: Optional[Sequence["_ExposedPortDefinition"]]
    Fqdn: Optional[str]
    Id: Optional[str]
    IpAddress: Optional[str]
    IpAddressType: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    NetworkProfileId: Optional[str]
    OsType: Optional[str]
    ResourceGroupName: Optional[str]
    RestartPolicy: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Container: Optional[Sequence["_ContainerDefinition"]]
    Diagnostics: Optional[Sequence["_DiagnosticsDefinition"]]
    DnsConfig: Optional[Sequence["_DnsConfigDefinition"]]
    Identity: Optional[Sequence["_IdentityDefinition"]]
    ImageRegistryCredential: Optional[Sequence["_ImageRegistryCredentialDefinition"]]
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
            DnsNameLabel=json_data.get("DnsNameLabel"),
            ExposedPort=deserialize_list(json_data.get("ExposedPort"), ExposedPortDefinition),
            Fqdn=json_data.get("Fqdn"),
            Id=json_data.get("Id"),
            IpAddress=json_data.get("IpAddress"),
            IpAddressType=json_data.get("IpAddressType"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            NetworkProfileId=json_data.get("NetworkProfileId"),
            OsType=json_data.get("OsType"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            RestartPolicy=json_data.get("RestartPolicy"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Container=deserialize_list(json_data.get("Container"), ContainerDefinition),
            Diagnostics=deserialize_list(json_data.get("Diagnostics"), DiagnosticsDefinition),
            DnsConfig=deserialize_list(json_data.get("DnsConfig"), DnsConfigDefinition),
            Identity=deserialize_list(json_data.get("Identity"), IdentityDefinition),
            ImageRegistryCredential=deserialize_list(json_data.get("ImageRegistryCredential"), ImageRegistryCredentialDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ExposedPortDefinition(BaseModel):
    Port: Optional[float]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExposedPortDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExposedPortDefinition"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExposedPortDefinition = ExposedPortDefinition


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
class ContainerDefinition(BaseModel):
    Commands: Optional[Sequence[str]]
    Cpu: Optional[float]
    EnvironmentVariables: Optional[Sequence["_EnvironmentVariablesDefinition"]]
    Image: Optional[str]
    Memory: Optional[float]
    Name: Optional[str]
    SecureEnvironmentVariables: Optional[Sequence["_SecureEnvironmentVariablesDefinition"]]
    Gpu: Optional[Sequence["_GpuDefinition"]]
    LivenessProbe: Optional[Sequence["_LivenessProbeDefinition"]]
    Ports: Optional[Sequence["_PortsDefinition"]]
    ReadinessProbe: Optional[Sequence["_ReadinessProbeDefinition"]]
    Volume: Optional[Sequence["_VolumeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ContainerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContainerDefinition"]:
        if not json_data:
            return None
        return cls(
            Commands=json_data.get("Commands"),
            Cpu=json_data.get("Cpu"),
            EnvironmentVariables=deserialize_list(json_data.get("EnvironmentVariables"), EnvironmentVariablesDefinition),
            Image=json_data.get("Image"),
            Memory=json_data.get("Memory"),
            Name=json_data.get("Name"),
            SecureEnvironmentVariables=deserialize_list(json_data.get("SecureEnvironmentVariables"), SecureEnvironmentVariablesDefinition),
            Gpu=deserialize_list(json_data.get("Gpu"), GpuDefinition),
            LivenessProbe=deserialize_list(json_data.get("LivenessProbe"), LivenessProbeDefinition),
            Ports=deserialize_list(json_data.get("Ports"), PortsDefinition),
            ReadinessProbe=deserialize_list(json_data.get("ReadinessProbe"), ReadinessProbeDefinition),
            Volume=deserialize_list(json_data.get("Volume"), VolumeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContainerDefinition = ContainerDefinition


@dataclass
class EnvironmentVariablesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvironmentVariablesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvironmentVariablesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvironmentVariablesDefinition = EnvironmentVariablesDefinition


@dataclass
class SecureEnvironmentVariablesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecureEnvironmentVariablesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecureEnvironmentVariablesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecureEnvironmentVariablesDefinition = SecureEnvironmentVariablesDefinition


@dataclass
class GpuDefinition(BaseModel):
    Count: Optional[float]
    Sku: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GpuDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GpuDefinition"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
            Sku=json_data.get("Sku"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GpuDefinition = GpuDefinition


@dataclass
class LivenessProbeDefinition(BaseModel):
    Exec: Optional[Sequence[str]]
    FailureThreshold: Optional[float]
    InitialDelaySeconds: Optional[float]
    PeriodSeconds: Optional[float]
    SuccessThreshold: Optional[float]
    TimeoutSeconds: Optional[float]
    HttpGet: Optional[Sequence["_HttpGetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LivenessProbeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LivenessProbeDefinition"]:
        if not json_data:
            return None
        return cls(
            Exec=json_data.get("Exec"),
            FailureThreshold=json_data.get("FailureThreshold"),
            InitialDelaySeconds=json_data.get("InitialDelaySeconds"),
            PeriodSeconds=json_data.get("PeriodSeconds"),
            SuccessThreshold=json_data.get("SuccessThreshold"),
            TimeoutSeconds=json_data.get("TimeoutSeconds"),
            HttpGet=deserialize_list(json_data.get("HttpGet"), HttpGetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LivenessProbeDefinition = LivenessProbeDefinition


@dataclass
class HttpGetDefinition(BaseModel):
    Path: Optional[str]
    Port: Optional[float]
    Scheme: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpGetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpGetDefinition"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            Port=json_data.get("Port"),
            Scheme=json_data.get("Scheme"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpGetDefinition = HttpGetDefinition


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
class ReadinessProbeDefinition(BaseModel):
    Exec: Optional[Sequence[str]]
    FailureThreshold: Optional[float]
    InitialDelaySeconds: Optional[float]
    PeriodSeconds: Optional[float]
    SuccessThreshold: Optional[float]
    TimeoutSeconds: Optional[float]
    HttpGet: Optional[Sequence["_HttpGetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ReadinessProbeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReadinessProbeDefinition"]:
        if not json_data:
            return None
        return cls(
            Exec=json_data.get("Exec"),
            FailureThreshold=json_data.get("FailureThreshold"),
            InitialDelaySeconds=json_data.get("InitialDelaySeconds"),
            PeriodSeconds=json_data.get("PeriodSeconds"),
            SuccessThreshold=json_data.get("SuccessThreshold"),
            TimeoutSeconds=json_data.get("TimeoutSeconds"),
            HttpGet=deserialize_list(json_data.get("HttpGet"), HttpGetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReadinessProbeDefinition = ReadinessProbeDefinition


@dataclass
class VolumeDefinition(BaseModel):
    EmptyDir: Optional[bool]
    MountPath: Optional[str]
    Name: Optional[str]
    ReadOnly: Optional[bool]
    Secret: Optional[Sequence["_SecretDefinition"]]
    ShareName: Optional[str]
    StorageAccountKey: Optional[str]
    StorageAccountName: Optional[str]
    GitRepo: Optional[Sequence["_GitRepoDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VolumeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VolumeDefinition"]:
        if not json_data:
            return None
        return cls(
            EmptyDir=json_data.get("EmptyDir"),
            MountPath=json_data.get("MountPath"),
            Name=json_data.get("Name"),
            ReadOnly=json_data.get("ReadOnly"),
            Secret=deserialize_list(json_data.get("Secret"), SecretDefinition),
            ShareName=json_data.get("ShareName"),
            StorageAccountKey=json_data.get("StorageAccountKey"),
            StorageAccountName=json_data.get("StorageAccountName"),
            GitRepo=deserialize_list(json_data.get("GitRepo"), GitRepoDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VolumeDefinition = VolumeDefinition


@dataclass
class SecretDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecretDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecretDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecretDefinition = SecretDefinition


@dataclass
class GitRepoDefinition(BaseModel):
    Directory: Optional[str]
    Revision: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GitRepoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GitRepoDefinition"]:
        if not json_data:
            return None
        return cls(
            Directory=json_data.get("Directory"),
            Revision=json_data.get("Revision"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GitRepoDefinition = GitRepoDefinition


@dataclass
class DiagnosticsDefinition(BaseModel):
    LogAnalytics: Optional[Sequence["_LogAnalyticsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DiagnosticsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiagnosticsDefinition"]:
        if not json_data:
            return None
        return cls(
            LogAnalytics=deserialize_list(json_data.get("LogAnalytics"), LogAnalyticsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiagnosticsDefinition = DiagnosticsDefinition


@dataclass
class LogAnalyticsDefinition(BaseModel):
    LogType: Optional[str]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    WorkspaceId: Optional[str]
    WorkspaceKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogAnalyticsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogAnalyticsDefinition"]:
        if not json_data:
            return None
        return cls(
            LogType=json_data.get("LogType"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            WorkspaceId=json_data.get("WorkspaceId"),
            WorkspaceKey=json_data.get("WorkspaceKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogAnalyticsDefinition = LogAnalyticsDefinition


@dataclass
class MetadataDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


@dataclass
class DnsConfigDefinition(BaseModel):
    Nameservers: Optional[Sequence[str]]
    Options: Optional[Sequence[str]]
    SearchDomains: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DnsConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Nameservers=json_data.get("Nameservers"),
            Options=json_data.get("Options"),
            SearchDomains=json_data.get("SearchDomains"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsConfigDefinition = DnsConfigDefinition


@dataclass
class IdentityDefinition(BaseModel):
    IdentityIds: Optional[Sequence[str]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IdentityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdentityDefinition"]:
        if not json_data:
            return None
        return cls(
            IdentityIds=json_data.get("IdentityIds"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdentityDefinition = IdentityDefinition


@dataclass
class ImageRegistryCredentialDefinition(BaseModel):
    Password: Optional[str]
    Server: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ImageRegistryCredentialDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImageRegistryCredentialDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Server=json_data.get("Server"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImageRegistryCredentialDefinition = ImageRegistryCredentialDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


