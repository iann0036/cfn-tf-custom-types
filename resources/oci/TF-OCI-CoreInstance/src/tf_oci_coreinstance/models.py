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
    AvailabilityDomain: Optional[str]
    BootVolumeId: Optional[str]
    CapacityReservationId: Optional[str]
    CompartmentId: Optional[str]
    DedicatedVmHostId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    DisplayName: Optional[str]
    ExtendedMetadata: Optional[Sequence["_ExtendedMetadataDefinition"]]
    FaultDomain: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    HostnameLabel: Optional[str]
    Id: Optional[str]
    Image: Optional[str]
    IpxeScript: Optional[str]
    IsPvEncryptionInTransitEnabled: Optional[bool]
    LaunchMode: Optional[str]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    PreserveBootVolume: Optional[bool]
    PrivateIp: Optional[str]
    PublicIp: Optional[str]
    Region: Optional[str]
    Shape: Optional[str]
    State: Optional[str]
    SubnetId: Optional[str]
    SystemTags: Optional[Sequence["_SystemTagsDefinition"]]
    TimeCreated: Optional[str]
    TimeMaintenanceRebootDue: Optional[str]
    AgentConfig: Optional[Sequence["_AgentConfigDefinition"]]
    AvailabilityConfig: Optional[Sequence["_AvailabilityConfigDefinition"]]
    CreateVnicDetails: Optional[Sequence["_CreateVnicDetailsDefinition"]]
    InstanceOptions: Optional[Sequence["_InstanceOptionsDefinition"]]
    LaunchOptions: Optional[Sequence["_LaunchOptionsDefinition"]]
    PlatformConfig: Optional[Sequence["_PlatformConfigDefinition"]]
    PreemptibleInstanceConfig: Optional[Sequence["_PreemptibleInstanceConfigDefinition"]]
    ShapeConfig: Optional[Sequence["_ShapeConfigDefinition"]]
    SourceDetails: Optional[Sequence["_SourceDetailsDefinition"]]
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
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            BootVolumeId=json_data.get("BootVolumeId"),
            CapacityReservationId=json_data.get("CapacityReservationId"),
            CompartmentId=json_data.get("CompartmentId"),
            DedicatedVmHostId=json_data.get("DedicatedVmHostId"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            DisplayName=json_data.get("DisplayName"),
            ExtendedMetadata=deserialize_list(json_data.get("ExtendedMetadata"), ExtendedMetadataDefinition),
            FaultDomain=json_data.get("FaultDomain"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            HostnameLabel=json_data.get("HostnameLabel"),
            Id=json_data.get("Id"),
            Image=json_data.get("Image"),
            IpxeScript=json_data.get("IpxeScript"),
            IsPvEncryptionInTransitEnabled=json_data.get("IsPvEncryptionInTransitEnabled"),
            LaunchMode=json_data.get("LaunchMode"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            PreserveBootVolume=json_data.get("PreserveBootVolume"),
            PrivateIp=json_data.get("PrivateIp"),
            PublicIp=json_data.get("PublicIp"),
            Region=json_data.get("Region"),
            Shape=json_data.get("Shape"),
            State=json_data.get("State"),
            SubnetId=json_data.get("SubnetId"),
            SystemTags=deserialize_list(json_data.get("SystemTags"), SystemTagsDefinition),
            TimeCreated=json_data.get("TimeCreated"),
            TimeMaintenanceRebootDue=json_data.get("TimeMaintenanceRebootDue"),
            AgentConfig=deserialize_list(json_data.get("AgentConfig"), AgentConfigDefinition),
            AvailabilityConfig=deserialize_list(json_data.get("AvailabilityConfig"), AvailabilityConfigDefinition),
            CreateVnicDetails=deserialize_list(json_data.get("CreateVnicDetails"), CreateVnicDetailsDefinition),
            InstanceOptions=deserialize_list(json_data.get("InstanceOptions"), InstanceOptionsDefinition),
            LaunchOptions=deserialize_list(json_data.get("LaunchOptions"), LaunchOptionsDefinition),
            PlatformConfig=deserialize_list(json_data.get("PlatformConfig"), PlatformConfigDefinition),
            PreemptibleInstanceConfig=deserialize_list(json_data.get("PreemptibleInstanceConfig"), PreemptibleInstanceConfigDefinition),
            ShapeConfig=deserialize_list(json_data.get("ShapeConfig"), ShapeConfigDefinition),
            SourceDetails=deserialize_list(json_data.get("SourceDetails"), SourceDetailsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTagsDefinition = DefinedTagsDefinition


@dataclass
class ExtendedMetadataDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtendedMetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtendedMetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtendedMetadataDefinition = ExtendedMetadataDefinition


@dataclass
class FreeformTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTagsDefinition = FreeformTagsDefinition


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
class SystemTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SystemTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SystemTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SystemTagsDefinition = SystemTagsDefinition


@dataclass
class AgentConfigDefinition(BaseModel):
    AreAllPluginsDisabled: Optional[bool]
    IsManagementDisabled: Optional[bool]
    IsMonitoringDisabled: Optional[bool]
    PluginsConfig: Optional[Sequence["_PluginsConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AgentConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AgentConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AreAllPluginsDisabled=json_data.get("AreAllPluginsDisabled"),
            IsManagementDisabled=json_data.get("IsManagementDisabled"),
            IsMonitoringDisabled=json_data.get("IsMonitoringDisabled"),
            PluginsConfig=deserialize_list(json_data.get("PluginsConfig"), PluginsConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AgentConfigDefinition = AgentConfigDefinition


@dataclass
class PluginsConfigDefinition(BaseModel):
    DesiredState: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PluginsConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PluginsConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            DesiredState=json_data.get("DesiredState"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PluginsConfigDefinition = PluginsConfigDefinition


@dataclass
class AvailabilityConfigDefinition(BaseModel):
    IsLiveMigrationPreferred: Optional[bool]
    RecoveryAction: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AvailabilityConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AvailabilityConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            IsLiveMigrationPreferred=json_data.get("IsLiveMigrationPreferred"),
            RecoveryAction=json_data.get("RecoveryAction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AvailabilityConfigDefinition = AvailabilityConfigDefinition


@dataclass
class CreateVnicDetailsDefinition(BaseModel):
    AssignPrivateDnsRecord: Optional[bool]
    AssignPublicIp: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition2"]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition2"]]
    HostnameLabel: Optional[str]
    NsgIds: Optional[Sequence[str]]
    PrivateIp: Optional[str]
    SkipSourceDestCheck: Optional[bool]
    SubnetId: Optional[str]
    VlanId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CreateVnicDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CreateVnicDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            AssignPrivateDnsRecord=json_data.get("AssignPrivateDnsRecord"),
            AssignPublicIp=json_data.get("AssignPublicIp"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition2),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition2),
            HostnameLabel=json_data.get("HostnameLabel"),
            NsgIds=json_data.get("NsgIds"),
            PrivateIp=json_data.get("PrivateIp"),
            SkipSourceDestCheck=json_data.get("SkipSourceDestCheck"),
            SubnetId=json_data.get("SubnetId"),
            VlanId=json_data.get("VlanId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CreateVnicDetailsDefinition = CreateVnicDetailsDefinition


@dataclass
class DefinedTagsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTagsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTagsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTagsDefinition2 = DefinedTagsDefinition2


@dataclass
class FreeformTagsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTagsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTagsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTagsDefinition2 = FreeformTagsDefinition2


@dataclass
class InstanceOptionsDefinition(BaseModel):
    AreLegacyImdsEndpointsDisabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            AreLegacyImdsEndpointsDisabled=json_data.get("AreLegacyImdsEndpointsDisabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceOptionsDefinition = InstanceOptionsDefinition


@dataclass
class LaunchOptionsDefinition(BaseModel):
    BootVolumeType: Optional[str]
    Firmware: Optional[str]
    IsConsistentVolumeNamingEnabled: Optional[bool]
    IsPvEncryptionInTransitEnabled: Optional[bool]
    NetworkType: Optional[str]
    RemoteDataVolumeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            BootVolumeType=json_data.get("BootVolumeType"),
            Firmware=json_data.get("Firmware"),
            IsConsistentVolumeNamingEnabled=json_data.get("IsConsistentVolumeNamingEnabled"),
            IsPvEncryptionInTransitEnabled=json_data.get("IsPvEncryptionInTransitEnabled"),
            NetworkType=json_data.get("NetworkType"),
            RemoteDataVolumeType=json_data.get("RemoteDataVolumeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchOptionsDefinition = LaunchOptionsDefinition


@dataclass
class PlatformConfigDefinition(BaseModel):
    NumaNodesPerSocket: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlatformConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlatformConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            NumaNodesPerSocket=json_data.get("NumaNodesPerSocket"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlatformConfigDefinition = PlatformConfigDefinition


@dataclass
class PreemptibleInstanceConfigDefinition(BaseModel):
    PreemptionAction: Optional[Sequence["_PreemptionActionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PreemptibleInstanceConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PreemptibleInstanceConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            PreemptionAction=deserialize_list(json_data.get("PreemptionAction"), PreemptionActionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PreemptibleInstanceConfigDefinition = PreemptibleInstanceConfigDefinition


@dataclass
class PreemptionActionDefinition(BaseModel):
    PreserveBootVolume: Optional[bool]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PreemptionActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PreemptionActionDefinition"]:
        if not json_data:
            return None
        return cls(
            PreserveBootVolume=json_data.get("PreserveBootVolume"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PreemptionActionDefinition = PreemptionActionDefinition


@dataclass
class ShapeConfigDefinition(BaseModel):
    BaselineOcpuUtilization: Optional[str]
    MemoryInGbs: Optional[float]
    Ocpus: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ShapeConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ShapeConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            BaselineOcpuUtilization=json_data.get("BaselineOcpuUtilization"),
            MemoryInGbs=json_data.get("MemoryInGbs"),
            Ocpus=json_data.get("Ocpus"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ShapeConfigDefinition = ShapeConfigDefinition


@dataclass
class SourceDetailsDefinition(BaseModel):
    BootVolumeSizeInGbs: Optional[str]
    KmsKeyId: Optional[str]
    SourceId: Optional[str]
    SourceType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            BootVolumeSizeInGbs=json_data.get("BootVolumeSizeInGbs"),
            KmsKeyId=json_data.get("KmsKeyId"),
            SourceId=json_data.get("SourceId"),
            SourceType=json_data.get("SourceType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceDetailsDefinition = SourceDetailsDefinition


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


