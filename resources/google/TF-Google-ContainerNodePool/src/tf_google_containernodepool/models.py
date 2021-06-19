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
    Cluster: Optional[str]
    Id: Optional[str]
    InitialNodeCount: Optional[float]
    InstanceGroupUrls: Optional[Sequence[str]]
    Location: Optional[str]
    MaxPodsPerNode: Optional[float]
    Name: Optional[str]
    NamePrefix: Optional[str]
    NodeCount: Optional[float]
    NodeLocations: Optional[Sequence[str]]
    Operation: Optional[str]
    Project: Optional[str]
    Version: Optional[str]
    Autoscaling: Optional[Sequence["_AutoscalingDefinition"]]
    Management: Optional[Sequence["_ManagementDefinition"]]
    NodeConfig: Optional[Sequence["_NodeConfigDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    UpgradeSettings: Optional[Sequence["_UpgradeSettingsDefinition"]]

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
            Cluster=json_data.get("Cluster"),
            Id=json_data.get("Id"),
            InitialNodeCount=json_data.get("InitialNodeCount"),
            InstanceGroupUrls=json_data.get("InstanceGroupUrls"),
            Location=json_data.get("Location"),
            MaxPodsPerNode=json_data.get("MaxPodsPerNode"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            NodeCount=json_data.get("NodeCount"),
            NodeLocations=json_data.get("NodeLocations"),
            Operation=json_data.get("Operation"),
            Project=json_data.get("Project"),
            Version=json_data.get("Version"),
            Autoscaling=deserialize_list(json_data.get("Autoscaling"), AutoscalingDefinition),
            Management=deserialize_list(json_data.get("Management"), ManagementDefinition),
            NodeConfig=deserialize_list(json_data.get("NodeConfig"), NodeConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            UpgradeSettings=deserialize_list(json_data.get("UpgradeSettings"), UpgradeSettingsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AutoscalingDefinition(BaseModel):
    MaxNodeCount: Optional[float]
    MinNodeCount: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscalingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscalingDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxNodeCount=json_data.get("MaxNodeCount"),
            MinNodeCount=json_data.get("MinNodeCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscalingDefinition = AutoscalingDefinition


@dataclass
class ManagementDefinition(BaseModel):
    AutoRepair: Optional[bool]
    AutoUpgrade: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ManagementDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagementDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoRepair=json_data.get("AutoRepair"),
            AutoUpgrade=json_data.get("AutoUpgrade"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManagementDefinition = ManagementDefinition


@dataclass
class NodeConfigDefinition(BaseModel):
    DiskSizeGb: Optional[float]
    DiskType: Optional[str]
    GuestAccelerator: Optional[Sequence["_GuestAcceleratorDefinition"]]
    ImageType: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    LocalSsdCount: Optional[float]
    MachineType: Optional[str]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    MinCpuPlatform: Optional[str]
    OauthScopes: Optional[Sequence[str]]
    Preemptible: Optional[bool]
    ServiceAccount: Optional[str]
    Tags: Optional[Sequence[str]]
    Taint: Optional[Sequence["_TaintDefinition"]]
    ShieldedInstanceConfig: Optional[Sequence["_ShieldedInstanceConfigDefinition"]]
    WorkloadMetadataConfig: Optional[Sequence["_WorkloadMetadataConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NodeConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            DiskSizeGb=json_data.get("DiskSizeGb"),
            DiskType=json_data.get("DiskType"),
            GuestAccelerator=deserialize_list(json_data.get("GuestAccelerator"), GuestAcceleratorDefinition),
            ImageType=json_data.get("ImageType"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            LocalSsdCount=json_data.get("LocalSsdCount"),
            MachineType=json_data.get("MachineType"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            MinCpuPlatform=json_data.get("MinCpuPlatform"),
            OauthScopes=json_data.get("OauthScopes"),
            Preemptible=json_data.get("Preemptible"),
            ServiceAccount=json_data.get("ServiceAccount"),
            Tags=json_data.get("Tags"),
            Taint=deserialize_list(json_data.get("Taint"), TaintDefinition),
            ShieldedInstanceConfig=deserialize_list(json_data.get("ShieldedInstanceConfig"), ShieldedInstanceConfigDefinition),
            WorkloadMetadataConfig=deserialize_list(json_data.get("WorkloadMetadataConfig"), WorkloadMetadataConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeConfigDefinition = NodeConfigDefinition


@dataclass
class GuestAcceleratorDefinition(BaseModel):
    Count: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GuestAcceleratorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GuestAcceleratorDefinition"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GuestAcceleratorDefinition = GuestAcceleratorDefinition


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
class TaintDefinition(BaseModel):
    Effect: Optional[str]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TaintDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaintDefinition"]:
        if not json_data:
            return None
        return cls(
            Effect=json_data.get("Effect"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaintDefinition = TaintDefinition


@dataclass
class ShieldedInstanceConfigDefinition(BaseModel):
    EnableIntegrityMonitoring: Optional[bool]
    EnableSecureBoot: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ShieldedInstanceConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ShieldedInstanceConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            EnableIntegrityMonitoring=json_data.get("EnableIntegrityMonitoring"),
            EnableSecureBoot=json_data.get("EnableSecureBoot"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ShieldedInstanceConfigDefinition = ShieldedInstanceConfigDefinition


@dataclass
class WorkloadMetadataConfigDefinition(BaseModel):
    NodeMetadata: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkloadMetadataConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkloadMetadataConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            NodeMetadata=json_data.get("NodeMetadata"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkloadMetadataConfigDefinition = WorkloadMetadataConfigDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


@dataclass
class UpgradeSettingsDefinition(BaseModel):
    MaxSurge: Optional[float]
    MaxUnavailable: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_UpgradeSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UpgradeSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxSurge=json_data.get("MaxSurge"),
            MaxUnavailable=json_data.get("MaxUnavailable"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UpgradeSettingsDefinition = UpgradeSettingsDefinition


