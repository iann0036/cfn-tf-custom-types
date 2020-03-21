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
    DnsNameLabel: Optional[str]
    Fqdn: Optional[str]
    IpAddress: Optional[str]
    IpAddressType: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    NetworkProfileId: Optional[str]
    OsType: Optional[str]
    ResourceGroupName: Optional[str]
    RestartPolicy: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Container: Optional[Sequence["_Container"]]
    Diagnostics: Optional[Sequence["_Diagnostics"]]
    Identity: Optional[Sequence["_Identity"]]
    ImageRegistryCredential: Optional[Sequence["_ImageRegistryCredential"]]
    Timeouts: Optional["_Timeouts"]
    Gpu: Optional[Sequence["_Gpu"]]
    LivenessProbe: Optional[Sequence["_LivenessProbe"]]
    Ports: Optional[Sequence["_Ports"]]
    ReadinessProbe: Optional[Sequence["_ReadinessProbe"]]
    Volume: Optional[Sequence["_Volume"]]
    LogAnalytics: Optional[Sequence["_LogAnalytics"]]
    HttpGet: Optional[Sequence["_HttpGet"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DnsNameLabel=json_data.get("DnsNameLabel"),
            Fqdn=json_data.get("Fqdn"),
            IpAddress=json_data.get("IpAddress"),
            IpAddressType=json_data.get("IpAddressType"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            NetworkProfileId=json_data.get("NetworkProfileId"),
            OsType=json_data.get("OsType"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            RestartPolicy=json_data.get("RestartPolicy"),
            Tags=json_data.get("Tags"),
            Container=json_data.get("Container"),
            Diagnostics=json_data.get("Diagnostics"),
            Identity=json_data.get("Identity"),
            ImageRegistryCredential=json_data.get("ImageRegistryCredential"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Gpu=json_data.get("Gpu"),
            LivenessProbe=json_data.get("LivenessProbe"),
            Ports=json_data.get("Ports"),
            ReadinessProbe=json_data.get("ReadinessProbe"),
            Volume=json_data.get("Volume"),
            LogAnalytics=json_data.get("LogAnalytics"),
            HttpGet=json_data.get("HttpGet"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Container:
    Commands: Optional[Sequence[str]]
    Cpu: Optional[float]
    EnvironmentVariables: Optional[Sequence["_EnvironmentVariables"]]
    Image: Optional[str]
    Memory: Optional[float]
    Name: Optional[str]
    SecureEnvironmentVariables: Optional[Sequence["_SecureEnvironmentVariables"]]
    Gpu: Optional[Sequence["_Gpu"]]
    LivenessProbe: Optional[Sequence["_LivenessProbe"]]
    Ports: Optional[Sequence["_Ports"]]
    ReadinessProbe: Optional[Sequence["_ReadinessProbe"]]
    Volume: Optional[Sequence["_Volume"]]

    @classmethod
    def _deserialize(
        cls: Type["_Container"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Container"]:
        if not json_data:
            return None
        return cls(
            Commands=json_data.get("Commands"),
            Cpu=json_data.get("Cpu"),
            EnvironmentVariables=json_data.get("EnvironmentVariables"),
            Image=json_data.get("Image"),
            Memory=json_data.get("Memory"),
            Name=json_data.get("Name"),
            SecureEnvironmentVariables=json_data.get("SecureEnvironmentVariables"),
            Gpu=json_data.get("Gpu"),
            LivenessProbe=json_data.get("LivenessProbe"),
            Ports=json_data.get("Ports"),
            ReadinessProbe=json_data.get("ReadinessProbe"),
            Volume=json_data.get("Volume"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Container = Container


@dataclass
class EnvironmentVariables:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvironmentVariables"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvironmentVariables"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvironmentVariables = EnvironmentVariables


@dataclass
class SecureEnvironmentVariables:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecureEnvironmentVariables"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecureEnvironmentVariables"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecureEnvironmentVariables = SecureEnvironmentVariables


@dataclass
class Gpu:
    Count: Optional[float]
    Sku: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Gpu"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Gpu"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
            Sku=json_data.get("Sku"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Gpu = Gpu


@dataclass
class LivenessProbe:
    Exec: Optional[Sequence[str]]
    FailureThreshold: Optional[float]
    InitialDelaySeconds: Optional[float]
    PeriodSeconds: Optional[float]
    SuccessThreshold: Optional[float]
    TimeoutSeconds: Optional[float]
    HttpGet: Optional[Sequence["_HttpGet"]]

    @classmethod
    def _deserialize(
        cls: Type["_LivenessProbe"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LivenessProbe"]:
        if not json_data:
            return None
        return cls(
            Exec=json_data.get("Exec"),
            FailureThreshold=json_data.get("FailureThreshold"),
            InitialDelaySeconds=json_data.get("InitialDelaySeconds"),
            PeriodSeconds=json_data.get("PeriodSeconds"),
            SuccessThreshold=json_data.get("SuccessThreshold"),
            TimeoutSeconds=json_data.get("TimeoutSeconds"),
            HttpGet=json_data.get("HttpGet"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LivenessProbe = LivenessProbe


@dataclass
class HttpGet:
    Path: Optional[str]
    Port: Optional[float]
    Scheme: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpGet"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpGet"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            Port=json_data.get("Port"),
            Scheme=json_data.get("Scheme"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpGet = HttpGet


@dataclass
class Ports:
    Port: Optional[float]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ports"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ports"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ports = Ports


@dataclass
class ReadinessProbe:
    Exec: Optional[Sequence[str]]
    FailureThreshold: Optional[float]
    InitialDelaySeconds: Optional[float]
    PeriodSeconds: Optional[float]
    SuccessThreshold: Optional[float]
    TimeoutSeconds: Optional[float]
    HttpGet: Optional[Sequence["_HttpGet"]]

    @classmethod
    def _deserialize(
        cls: Type["_ReadinessProbe"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReadinessProbe"]:
        if not json_data:
            return None
        return cls(
            Exec=json_data.get("Exec"),
            FailureThreshold=json_data.get("FailureThreshold"),
            InitialDelaySeconds=json_data.get("InitialDelaySeconds"),
            PeriodSeconds=json_data.get("PeriodSeconds"),
            SuccessThreshold=json_data.get("SuccessThreshold"),
            TimeoutSeconds=json_data.get("TimeoutSeconds"),
            HttpGet=json_data.get("HttpGet"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReadinessProbe = ReadinessProbe


@dataclass
class Volume:
    MountPath: Optional[str]
    Name: Optional[str]
    ReadOnly: Optional[bool]
    ShareName: Optional[str]
    StorageAccountKey: Optional[str]
    StorageAccountName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Volume"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Volume"]:
        if not json_data:
            return None
        return cls(
            MountPath=json_data.get("MountPath"),
            Name=json_data.get("Name"),
            ReadOnly=json_data.get("ReadOnly"),
            ShareName=json_data.get("ShareName"),
            StorageAccountKey=json_data.get("StorageAccountKey"),
            StorageAccountName=json_data.get("StorageAccountName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Volume = Volume


@dataclass
class Diagnostics:
    LogAnalytics: Optional[Sequence["_LogAnalytics"]]

    @classmethod
    def _deserialize(
        cls: Type["_Diagnostics"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Diagnostics"]:
        if not json_data:
            return None
        return cls(
            LogAnalytics=json_data.get("LogAnalytics"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Diagnostics = Diagnostics


@dataclass
class LogAnalytics:
    LogType: Optional[str]
    Metadata: Optional[Sequence["_Metadata"]]
    WorkspaceId: Optional[str]
    WorkspaceKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogAnalytics"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogAnalytics"]:
        if not json_data:
            return None
        return cls(
            LogType=json_data.get("LogType"),
            Metadata=json_data.get("Metadata"),
            WorkspaceId=json_data.get("WorkspaceId"),
            WorkspaceKey=json_data.get("WorkspaceKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogAnalytics = LogAnalytics


@dataclass
class Metadata:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metadata"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metadata = Metadata


@dataclass
class Identity:
    IdentityIds: Optional[Sequence[str]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Identity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Identity"]:
        if not json_data:
            return None
        return cls(
            IdentityIds=json_data.get("IdentityIds"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Identity = Identity


@dataclass
class ImageRegistryCredential:
    Password: Optional[str]
    Server: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ImageRegistryCredential"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImageRegistryCredential"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Server=json_data.get("Server"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImageRegistryCredential = ImageRegistryCredential


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


