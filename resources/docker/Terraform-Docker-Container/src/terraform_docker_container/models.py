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
    Attach: Optional[bool]
    Bridge: Optional[str]
    Command: Optional[Sequence[str]]
    ContainerLogs: Optional[str]
    CpuSet: Optional[str]
    CpuShares: Optional[float]
    DestroyGraceSeconds: Optional[float]
    Dns: Optional[Sequence[str]]
    DnsOpts: Optional[Sequence[str]]
    DnsSearch: Optional[Sequence[str]]
    Domainname: Optional[str]
    Entrypoint: Optional[Sequence[str]]
    Env: Optional[Sequence[str]]
    ExitCode: Optional[float]
    Gateway: Optional[str]
    GroupAdd: Optional[Sequence[str]]
    Hostname: Optional[str]
    Id: Optional[str]
    Image: Optional[str]
    IpAddress: Optional[str]
    IpPrefixLength: Optional[float]
    IpcMode: Optional[str]
    Links: Optional[Sequence[str]]
    LogDriver: Optional[str]
    LogOpts: Optional[Sequence["_LogOpts"]]
    Logs: Optional[bool]
    MaxRetryCount: Optional[float]
    Memory: Optional[float]
    MemorySwap: Optional[float]
    MustRun: Optional[bool]
    Name: Optional[str]
    NetworkAlias: Optional[Sequence[str]]
    NetworkData: Optional[Sequence["_NetworkData"]]
    NetworkMode: Optional[str]
    Networks: Optional[Sequence[str]]
    PidMode: Optional[str]
    Privileged: Optional[bool]
    PublishAllPorts: Optional[bool]
    ReadOnly: Optional[bool]
    Restart: Optional[str]
    Rm: Optional[bool]
    ShmSize: Optional[float]
    Start: Optional[bool]
    Sysctls: Optional[Sequence["_Sysctls"]]
    Tmpfs: Optional[Sequence["_Tmpfs"]]
    User: Optional[str]
    UsernsMode: Optional[str]
    WorkingDir: Optional[str]
    Capabilities: Optional[Sequence["_Capabilities"]]
    Devices: Optional[Sequence["_Devices"]]
    Healthcheck: Optional[Sequence["_Healthcheck"]]
    Host: Optional[Sequence["_Host"]]
    Labels: Optional[Sequence["_Labels"]]
    Mounts: Optional[Sequence["_Mounts"]]
    NetworksAdvanced: Optional[Sequence["_NetworksAdvanced"]]
    Ports: Optional[Sequence["_Ports"]]
    Ulimit: Optional[Sequence["_Ulimit"]]
    Upload: Optional[Sequence["_Upload"]]
    Volumes: Optional[Sequence["_Volumes"]]
    BindOptions: Optional[Sequence["_BindOptions"]]
    TmpfsOptions: Optional[Sequence["_TmpfsOptions"]]
    VolumeOptions: Optional[Sequence["_VolumeOptions"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Attach=json_data.get("Attach"),
            Bridge=json_data.get("Bridge"),
            Command=json_data.get("Command"),
            ContainerLogs=json_data.get("ContainerLogs"),
            CpuSet=json_data.get("CpuSet"),
            CpuShares=json_data.get("CpuShares"),
            DestroyGraceSeconds=json_data.get("DestroyGraceSeconds"),
            Dns=json_data.get("Dns"),
            DnsOpts=json_data.get("DnsOpts"),
            DnsSearch=json_data.get("DnsSearch"),
            Domainname=json_data.get("Domainname"),
            Entrypoint=json_data.get("Entrypoint"),
            Env=json_data.get("Env"),
            ExitCode=json_data.get("ExitCode"),
            Gateway=json_data.get("Gateway"),
            GroupAdd=json_data.get("GroupAdd"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            Image=json_data.get("Image"),
            IpAddress=json_data.get("IpAddress"),
            IpPrefixLength=json_data.get("IpPrefixLength"),
            IpcMode=json_data.get("IpcMode"),
            Links=json_data.get("Links"),
            LogDriver=json_data.get("LogDriver"),
            LogOpts=json_data.get("LogOpts"),
            Logs=json_data.get("Logs"),
            MaxRetryCount=json_data.get("MaxRetryCount"),
            Memory=json_data.get("Memory"),
            MemorySwap=json_data.get("MemorySwap"),
            MustRun=json_data.get("MustRun"),
            Name=json_data.get("Name"),
            NetworkAlias=json_data.get("NetworkAlias"),
            NetworkData=json_data.get("NetworkData"),
            NetworkMode=json_data.get("NetworkMode"),
            Networks=json_data.get("Networks"),
            PidMode=json_data.get("PidMode"),
            Privileged=json_data.get("Privileged"),
            PublishAllPorts=json_data.get("PublishAllPorts"),
            ReadOnly=json_data.get("ReadOnly"),
            Restart=json_data.get("Restart"),
            Rm=json_data.get("Rm"),
            ShmSize=json_data.get("ShmSize"),
            Start=json_data.get("Start"),
            Sysctls=json_data.get("Sysctls"),
            Tmpfs=json_data.get("Tmpfs"),
            User=json_data.get("User"),
            UsernsMode=json_data.get("UsernsMode"),
            WorkingDir=json_data.get("WorkingDir"),
            Capabilities=json_data.get("Capabilities"),
            Devices=json_data.get("Devices"),
            Healthcheck=json_data.get("Healthcheck"),
            Host=json_data.get("Host"),
            Labels=json_data.get("Labels"),
            Mounts=json_data.get("Mounts"),
            NetworksAdvanced=json_data.get("NetworksAdvanced"),
            Ports=json_data.get("Ports"),
            Ulimit=json_data.get("Ulimit"),
            Upload=json_data.get("Upload"),
            Volumes=json_data.get("Volumes"),
            BindOptions=json_data.get("BindOptions"),
            TmpfsOptions=json_data.get("TmpfsOptions"),
            VolumeOptions=json_data.get("VolumeOptions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LogOpts:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogOpts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogOpts"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogOpts = LogOpts


@dataclass
class NetworkData:
    Gateway: Optional[str]
    IpAddress: Optional[str]
    IpPrefixLength: Optional[float]
    NetworkName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkData"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkData"]:
        if not json_data:
            return None
        return cls(
            Gateway=json_data.get("Gateway"),
            IpAddress=json_data.get("IpAddress"),
            IpPrefixLength=json_data.get("IpPrefixLength"),
            NetworkName=json_data.get("NetworkName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkData = NetworkData


@dataclass
class Sysctls:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Sysctls"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Sysctls"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Sysctls = Sysctls


@dataclass
class Tmpfs:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tmpfs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tmpfs"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tmpfs = Tmpfs


@dataclass
class Capabilities:
    Add: Optional[Sequence[str]]
    Drop: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Capabilities"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Capabilities"]:
        if not json_data:
            return None
        return cls(
            Add=json_data.get("Add"),
            Drop=json_data.get("Drop"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Capabilities = Capabilities


@dataclass
class Devices:
    ContainerPath: Optional[str]
    HostPath: Optional[str]
    Permissions: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Devices"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Devices"]:
        if not json_data:
            return None
        return cls(
            ContainerPath=json_data.get("ContainerPath"),
            HostPath=json_data.get("HostPath"),
            Permissions=json_data.get("Permissions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Devices = Devices


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
class Host:
    Host: Optional[str]
    Ip: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Host"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Host"]:
        if not json_data:
            return None
        return cls(
            Host=json_data.get("Host"),
            Ip=json_data.get("Ip"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Host = Host


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
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DriverOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DriverOptions"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DriverOptions = DriverOptions


@dataclass
class NetworksAdvanced:
    Aliases: Optional[Sequence[str]]
    Ipv4Address: Optional[str]
    Ipv6Address: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworksAdvanced"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworksAdvanced"]:
        if not json_data:
            return None
        return cls(
            Aliases=json_data.get("Aliases"),
            Ipv4Address=json_data.get("Ipv4Address"),
            Ipv6Address=json_data.get("Ipv6Address"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworksAdvanced = NetworksAdvanced


@dataclass
class Ports:
    External: Optional[float]
    Internal: Optional[float]
    Ip: Optional[str]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ports"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ports"]:
        if not json_data:
            return None
        return cls(
            External=json_data.get("External"),
            Internal=json_data.get("Internal"),
            Ip=json_data.get("Ip"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ports = Ports


@dataclass
class Ulimit:
    Hard: Optional[float]
    Name: Optional[str]
    Soft: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Ulimit"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ulimit"]:
        if not json_data:
            return None
        return cls(
            Hard=json_data.get("Hard"),
            Name=json_data.get("Name"),
            Soft=json_data.get("Soft"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ulimit = Ulimit


@dataclass
class Upload:
    Content: Optional[str]
    ContentBase64: Optional[str]
    Executable: Optional[bool]
    File: Optional[str]
    Source: Optional[str]
    SourceHash: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Upload"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Upload"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
            ContentBase64=json_data.get("ContentBase64"),
            Executable=json_data.get("Executable"),
            File=json_data.get("File"),
            Source=json_data.get("Source"),
            SourceHash=json_data.get("SourceHash"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Upload = Upload


@dataclass
class Volumes:
    ContainerPath: Optional[str]
    FromContainer: Optional[str]
    HostPath: Optional[str]
    ReadOnly: Optional[bool]
    VolumeName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Volumes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Volumes"]:
        if not json_data:
            return None
        return cls(
            ContainerPath=json_data.get("ContainerPath"),
            FromContainer=json_data.get("FromContainer"),
            HostPath=json_data.get("HostPath"),
            ReadOnly=json_data.get("ReadOnly"),
            VolumeName=json_data.get("VolumeName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Volumes = Volumes


