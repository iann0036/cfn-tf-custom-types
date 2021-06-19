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
    CompartmentId: Optional[str]
    DeferredFields: Optional[Sequence[str]]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    InstanceId: Optional[str]
    Source: Optional[str]
    TimeCreated: Optional[str]
    InstanceDetails: Optional[Sequence["_InstanceDetailsDefinition"]]
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
            CompartmentId=json_data.get("CompartmentId"),
            DeferredFields=json_data.get("DeferredFields"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            InstanceId=json_data.get("InstanceId"),
            Source=json_data.get("Source"),
            TimeCreated=json_data.get("TimeCreated"),
            InstanceDetails=deserialize_list(json_data.get("InstanceDetails"), InstanceDetailsDefinition),
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
class InstanceDetailsDefinition(BaseModel):
    InstanceType: Optional[str]
    BlockVolumes: Optional[Sequence["_BlockVolumesDefinition"]]
    LaunchDetails: Optional[Sequence["_LaunchDetailsDefinition"]]
    SecondaryVnics: Optional[Sequence["_SecondaryVnicsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            InstanceType=json_data.get("InstanceType"),
            BlockVolumes=deserialize_list(json_data.get("BlockVolumes"), BlockVolumesDefinition),
            LaunchDetails=deserialize_list(json_data.get("LaunchDetails"), LaunchDetailsDefinition),
            SecondaryVnics=deserialize_list(json_data.get("SecondaryVnics"), SecondaryVnicsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceDetailsDefinition = InstanceDetailsDefinition


@dataclass
class BlockVolumesDefinition(BaseModel):
    VolumeId: Optional[str]
    AttachDetails: Optional[Sequence["_AttachDetailsDefinition"]]
    CreateDetails: Optional[Sequence["_CreateDetailsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BlockVolumesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlockVolumesDefinition"]:
        if not json_data:
            return None
        return cls(
            VolumeId=json_data.get("VolumeId"),
            AttachDetails=deserialize_list(json_data.get("AttachDetails"), AttachDetailsDefinition),
            CreateDetails=deserialize_list(json_data.get("CreateDetails"), CreateDetailsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlockVolumesDefinition = BlockVolumesDefinition


@dataclass
class AttachDetailsDefinition(BaseModel):
    Device: Optional[str]
    DisplayName: Optional[str]
    IsPvEncryptionInTransitEnabled: Optional[bool]
    IsReadOnly: Optional[bool]
    IsShareable: Optional[bool]
    Type: Optional[str]
    UseChap: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AttachDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttachDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            Device=json_data.get("Device"),
            DisplayName=json_data.get("DisplayName"),
            IsPvEncryptionInTransitEnabled=json_data.get("IsPvEncryptionInTransitEnabled"),
            IsReadOnly=json_data.get("IsReadOnly"),
            IsShareable=json_data.get("IsShareable"),
            Type=json_data.get("Type"),
            UseChap=json_data.get("UseChap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttachDetailsDefinition = AttachDetailsDefinition


@dataclass
class CreateDetailsDefinition(BaseModel):
    AvailabilityDomain: Optional[str]
    BackupPolicyId: Optional[str]
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition3"]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition3"]]
    KmsKeyId: Optional[str]
    SizeInGbs: Optional[str]
    VpusPerGb: Optional[str]
    SourceDetails: Optional[Sequence["_SourceDetailsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CreateDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CreateDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            BackupPolicyId=json_data.get("BackupPolicyId"),
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition3),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition3),
            KmsKeyId=json_data.get("KmsKeyId"),
            SizeInGbs=json_data.get("SizeInGbs"),
            VpusPerGb=json_data.get("VpusPerGb"),
            SourceDetails=deserialize_list(json_data.get("SourceDetails"), SourceDetailsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CreateDetailsDefinition = CreateDetailsDefinition


@dataclass
class DefinedTagsDefinition3(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTagsDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTagsDefinition3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTagsDefinition3 = DefinedTagsDefinition3


@dataclass
class FreeformTagsDefinition3(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTagsDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTagsDefinition3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTagsDefinition3 = FreeformTagsDefinition3


@dataclass
class SourceDetailsDefinition(BaseModel):
    Id: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceDetailsDefinition = SourceDetailsDefinition


@dataclass
class LaunchDetailsDefinition(BaseModel):
    AvailabilityDomain: Optional[str]
    CapacityReservationId: Optional[str]
    CompartmentId: Optional[str]
    DedicatedVmHostId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition2"]]
    DisplayName: Optional[str]
    ExtendedMetadata: Optional[Sequence["_ExtendedMetadataDefinition"]]
    FaultDomain: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition2"]]
    IpxeScript: Optional[str]
    IsPvEncryptionInTransitEnabled: Optional[bool]
    LaunchMode: Optional[str]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    PreferredMaintenanceAction: Optional[str]
    Shape: Optional[str]
    AgentConfig: Optional[Sequence["_AgentConfigDefinition"]]
    AvailabilityConfig: Optional[Sequence["_AvailabilityConfigDefinition"]]
    CreateVnicDetails: Optional[Sequence["_CreateVnicDetailsDefinition"]]
    InstanceOptions: Optional[Sequence["_InstanceOptionsDefinition"]]
    LaunchOptions: Optional[Sequence["_LaunchOptionsDefinition"]]
    PlatformConfig: Optional[Sequence["_PlatformConfigDefinition"]]
    PreemptibleInstanceConfig: Optional[Sequence["_PreemptibleInstanceConfigDefinition"]]
    ShapeConfig: Optional[Sequence["_ShapeConfigDefinition"]]
    SourceDetails: Optional[Sequence["_SourceDetailsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            CapacityReservationId=json_data.get("CapacityReservationId"),
            CompartmentId=json_data.get("CompartmentId"),
            DedicatedVmHostId=json_data.get("DedicatedVmHostId"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition2),
            DisplayName=json_data.get("DisplayName"),
            ExtendedMetadata=deserialize_list(json_data.get("ExtendedMetadata"), ExtendedMetadataDefinition),
            FaultDomain=json_data.get("FaultDomain"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition2),
            IpxeScript=json_data.get("IpxeScript"),
            IsPvEncryptionInTransitEnabled=json_data.get("IsPvEncryptionInTransitEnabled"),
            LaunchMode=json_data.get("LaunchMode"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            PreferredMaintenanceAction=json_data.get("PreferredMaintenanceAction"),
            Shape=json_data.get("Shape"),
            AgentConfig=deserialize_list(json_data.get("AgentConfig"), AgentConfigDefinition),
            AvailabilityConfig=deserialize_list(json_data.get("AvailabilityConfig"), AvailabilityConfigDefinition),
            CreateVnicDetails=deserialize_list(json_data.get("CreateVnicDetails"), CreateVnicDetailsDefinition),
            InstanceOptions=deserialize_list(json_data.get("InstanceOptions"), InstanceOptionsDefinition),
            LaunchOptions=deserialize_list(json_data.get("LaunchOptions"), LaunchOptionsDefinition),
            PlatformConfig=deserialize_list(json_data.get("PlatformConfig"), PlatformConfigDefinition),
            PreemptibleInstanceConfig=deserialize_list(json_data.get("PreemptibleInstanceConfig"), PreemptibleInstanceConfigDefinition),
            ShapeConfig=deserialize_list(json_data.get("ShapeConfig"), ShapeConfigDefinition),
            SourceDetails=deserialize_list(json_data.get("SourceDetails"), SourceDetailsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchDetailsDefinition = LaunchDetailsDefinition


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
    RecoveryAction: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AvailabilityConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AvailabilityConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            RecoveryAction=json_data.get("RecoveryAction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AvailabilityConfigDefinition = AvailabilityConfigDefinition


@dataclass
class CreateVnicDetailsDefinition(BaseModel):
    AssignPrivateDnsRecord: Optional[bool]
    AssignPublicIp: Optional[bool]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition4"]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition4"]]
    HostnameLabel: Optional[str]
    NsgIds: Optional[Sequence[str]]
    PrivateIp: Optional[str]
    SkipSourceDestCheck: Optional[bool]
    SubnetId: Optional[str]

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
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition4),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition4),
            HostnameLabel=json_data.get("HostnameLabel"),
            NsgIds=json_data.get("NsgIds"),
            PrivateIp=json_data.get("PrivateIp"),
            SkipSourceDestCheck=json_data.get("SkipSourceDestCheck"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CreateVnicDetailsDefinition = CreateVnicDetailsDefinition


@dataclass
class DefinedTagsDefinition4(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTagsDefinition4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTagsDefinition4"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTagsDefinition4 = DefinedTagsDefinition4


@dataclass
class FreeformTagsDefinition4(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTagsDefinition4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTagsDefinition4"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTagsDefinition4 = FreeformTagsDefinition4


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
class SecondaryVnicsDefinition(BaseModel):
    DisplayName: Optional[str]
    NicIndex: Optional[float]
    CreateVnicDetails: Optional[Sequence["_CreateVnicDetailsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SecondaryVnicsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecondaryVnicsDefinition"]:
        if not json_data:
            return None
        return cls(
            DisplayName=json_data.get("DisplayName"),
            NicIndex=json_data.get("NicIndex"),
            CreateVnicDetails=deserialize_list(json_data.get("CreateVnicDetails"), CreateVnicDetailsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecondaryVnicsDefinition = SecondaryVnicsDefinition


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


