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
    Cluster: Optional[str]
    Id: Optional[str]
    InitialNodeCount: Optional[float]
    InstanceGroupUrls: Optional[Sequence[str]]
    Location: Optional[str]
    MaxPodsPerNode: Optional[float]
    Name: Optional[str]
    NamePrefix: Optional[str]
    NodeCount: Optional[float]
    Project: Optional[str]
    Region: Optional[str]
    Version: Optional[str]
    Zone: Optional[str]
    Autoscaling: Optional[Sequence["_Autoscaling"]]
    Management: Optional[Sequence["_Management"]]
    NodeConfig: Optional[Sequence["_NodeConfig"]]
    Timeouts: Optional["_Timeouts"]
    SandboxConfig: Optional[Sequence["_SandboxConfig"]]
    ShieldedInstanceConfig: Optional[Sequence["_ShieldedInstanceConfig"]]
    WorkloadMetadataConfig: Optional[Sequence["_WorkloadMetadataConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Cluster=json_data.get("Cluster"),
            Id=json_data.get("Id"),
            InitialNodeCount=json_data.get("InitialNodeCount"),
            InstanceGroupUrls=json_data.get("InstanceGroupUrls"),
            Location=json_data.get("Location"),
            MaxPodsPerNode=json_data.get("MaxPodsPerNode"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            NodeCount=json_data.get("NodeCount"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            Version=json_data.get("Version"),
            Zone=json_data.get("Zone"),
            Autoscaling=json_data.get("Autoscaling"),
            Management=json_data.get("Management"),
            NodeConfig=json_data.get("NodeConfig"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            SandboxConfig=json_data.get("SandboxConfig"),
            ShieldedInstanceConfig=json_data.get("ShieldedInstanceConfig"),
            WorkloadMetadataConfig=json_data.get("WorkloadMetadataConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Autoscaling:
    MaxNodeCount: Optional[float]
    MinNodeCount: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Autoscaling"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Autoscaling"]:
        if not json_data:
            return None
        return cls(
            MaxNodeCount=json_data.get("MaxNodeCount"),
            MinNodeCount=json_data.get("MinNodeCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Autoscaling = Autoscaling


@dataclass
class Management:
    AutoRepair: Optional[bool]
    AutoUpgrade: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Management"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Management"]:
        if not json_data:
            return None
        return cls(
            AutoRepair=json_data.get("AutoRepair"),
            AutoUpgrade=json_data.get("AutoUpgrade"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Management = Management


@dataclass
class NodeConfig:
    DiskSizeGb: Optional[float]
    DiskType: Optional[str]
    GuestAccelerator: Optional[Sequence["_GuestAccelerator"]]
    ImageType: Optional[str]
    Labels: Optional[Sequence["_Labels"]]
    LocalSsdCount: Optional[float]
    MachineType: Optional[str]
    Metadata: Optional[Sequence["_Metadata"]]
    MinCpuPlatform: Optional[str]
    OauthScopes: Optional[Sequence[str]]
    Preemptible: Optional[bool]
    ServiceAccount: Optional[str]
    Tags: Optional[Sequence[str]]
    Taint: Optional[Sequence["_Taint"]]
    SandboxConfig: Optional[Sequence["_SandboxConfig"]]
    ShieldedInstanceConfig: Optional[Sequence["_ShieldedInstanceConfig"]]
    WorkloadMetadataConfig: Optional[Sequence["_WorkloadMetadataConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_NodeConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeConfig"]:
        if not json_data:
            return None
        return cls(
            DiskSizeGb=json_data.get("DiskSizeGb"),
            DiskType=json_data.get("DiskType"),
            GuestAccelerator=json_data.get("GuestAccelerator"),
            ImageType=json_data.get("ImageType"),
            Labels=json_data.get("Labels"),
            LocalSsdCount=json_data.get("LocalSsdCount"),
            MachineType=json_data.get("MachineType"),
            Metadata=json_data.get("Metadata"),
            MinCpuPlatform=json_data.get("MinCpuPlatform"),
            OauthScopes=json_data.get("OauthScopes"),
            Preemptible=json_data.get("Preemptible"),
            ServiceAccount=json_data.get("ServiceAccount"),
            Tags=json_data.get("Tags"),
            Taint=json_data.get("Taint"),
            SandboxConfig=json_data.get("SandboxConfig"),
            ShieldedInstanceConfig=json_data.get("ShieldedInstanceConfig"),
            WorkloadMetadataConfig=json_data.get("WorkloadMetadataConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeConfig = NodeConfig


@dataclass
class GuestAccelerator:
    Count: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GuestAccelerator"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GuestAccelerator"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GuestAccelerator = GuestAccelerator


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
class Metadata:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metadata"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metadata = Metadata


@dataclass
class Taint:
    Effect: Optional[str]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Taint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Taint"]:
        if not json_data:
            return None
        return cls(
            Effect=json_data.get("Effect"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Taint = Taint


@dataclass
class SandboxConfig:
    SandboxType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SandboxConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SandboxConfig"]:
        if not json_data:
            return None
        return cls(
            SandboxType=json_data.get("SandboxType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SandboxConfig = SandboxConfig


@dataclass
class ShieldedInstanceConfig:
    EnableIntegrityMonitoring: Optional[bool]
    EnableSecureBoot: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ShieldedInstanceConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ShieldedInstanceConfig"]:
        if not json_data:
            return None
        return cls(
            EnableIntegrityMonitoring=json_data.get("EnableIntegrityMonitoring"),
            EnableSecureBoot=json_data.get("EnableSecureBoot"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ShieldedInstanceConfig = ShieldedInstanceConfig


@dataclass
class WorkloadMetadataConfig:
    NodeMetadata: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkloadMetadataConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkloadMetadataConfig"]:
        if not json_data:
            return None
        return cls(
            NodeMetadata=json_data.get("NodeMetadata"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkloadMetadataConfig = WorkloadMetadataConfig


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


