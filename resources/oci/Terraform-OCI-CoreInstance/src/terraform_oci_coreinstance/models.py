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
    AvailabilityDomain: Optional[str]
    BootVolumeId: Optional[str]
    CompartmentId: Optional[str]
    DedicatedVmHostId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTags"]]
    DisplayName: Optional[str]
    ExtendedMetadata: Optional[Sequence["_ExtendedMetadata"]]
    FaultDomain: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTags"]]
    HostnameLabel: Optional[str]
    Id: Optional[str]
    Image: Optional[str]
    IpxeScript: Optional[str]
    IsPvEncryptionInTransitEnabled: Optional[bool]
    LaunchMode: Optional[str]
    Metadata: Optional[Sequence["_Metadata"]]
    PreserveBootVolume: Optional[bool]
    PrivateIp: Optional[str]
    PublicIp: Optional[str]
    Region: Optional[str]
    Shape: Optional[str]
    State: Optional[str]
    SubnetId: Optional[str]
    SystemTags: Optional[Sequence["_SystemTags"]]
    TimeCreated: Optional[str]
    TimeMaintenanceRebootDue: Optional[str]
    AgentConfig: Optional[Sequence["_AgentConfig"]]
    CreateVnicDetails: Optional[Sequence["_CreateVnicDetails"]]
    LaunchOptions: Optional[Sequence["_LaunchOptions"]]
    SourceDetails: Optional[Sequence["_SourceDetails"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            BootVolumeId=json_data.get("BootVolumeId"),
            CompartmentId=json_data.get("CompartmentId"),
            DedicatedVmHostId=json_data.get("DedicatedVmHostId"),
            DefinedTags=json_data.get("DefinedTags"),
            DisplayName=json_data.get("DisplayName"),
            ExtendedMetadata=json_data.get("ExtendedMetadata"),
            FaultDomain=json_data.get("FaultDomain"),
            FreeformTags=json_data.get("FreeformTags"),
            HostnameLabel=json_data.get("HostnameLabel"),
            Id=json_data.get("Id"),
            Image=json_data.get("Image"),
            IpxeScript=json_data.get("IpxeScript"),
            IsPvEncryptionInTransitEnabled=json_data.get("IsPvEncryptionInTransitEnabled"),
            LaunchMode=json_data.get("LaunchMode"),
            Metadata=json_data.get("Metadata"),
            PreserveBootVolume=json_data.get("PreserveBootVolume"),
            PrivateIp=json_data.get("PrivateIp"),
            PublicIp=json_data.get("PublicIp"),
            Region=json_data.get("Region"),
            Shape=json_data.get("Shape"),
            State=json_data.get("State"),
            SubnetId=json_data.get("SubnetId"),
            SystemTags=json_data.get("SystemTags"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeMaintenanceRebootDue=json_data.get("TimeMaintenanceRebootDue"),
            AgentConfig=json_data.get("AgentConfig"),
            CreateVnicDetails=json_data.get("CreateVnicDetails"),
            LaunchOptions=json_data.get("LaunchOptions"),
            SourceDetails=json_data.get("SourceDetails"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTags = DefinedTags


@dataclass
class ExtendedMetadata:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtendedMetadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtendedMetadata"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtendedMetadata = ExtendedMetadata


@dataclass
class FreeformTags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTags = FreeformTags


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
class SystemTags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SystemTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SystemTags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SystemTags = SystemTags


@dataclass
class AgentConfig:
    IsManagementDisabled: Optional[bool]
    IsMonitoringDisabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AgentConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AgentConfig"]:
        if not json_data:
            return None
        return cls(
            IsManagementDisabled=json_data.get("IsManagementDisabled"),
            IsMonitoringDisabled=json_data.get("IsMonitoringDisabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AgentConfig = AgentConfig


@dataclass
class CreateVnicDetails:
    AssignPublicIp: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTags2"]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTags2"]]
    HostnameLabel: Optional[str]
    NsgIds: Optional[Sequence[str]]
    PrivateIp: Optional[str]
    SkipSourceDestCheck: Optional[bool]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CreateVnicDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CreateVnicDetails"]:
        if not json_data:
            return None
        return cls(
            AssignPublicIp=json_data.get("AssignPublicIp"),
            DefinedTags=json_data.get("DefinedTags"),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=json_data.get("FreeformTags"),
            HostnameLabel=json_data.get("HostnameLabel"),
            NsgIds=json_data.get("NsgIds"),
            PrivateIp=json_data.get("PrivateIp"),
            SkipSourceDestCheck=json_data.get("SkipSourceDestCheck"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CreateVnicDetails = CreateVnicDetails


@dataclass
class DefinedTags2:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTags2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTags2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTags2 = DefinedTags2


@dataclass
class FreeformTags2:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTags2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTags2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTags2 = FreeformTags2


@dataclass
class LaunchOptions:
    BootVolumeType: Optional[str]
    Firmware: Optional[str]
    IsConsistentVolumeNamingEnabled: Optional[bool]
    IsPvEncryptionInTransitEnabled: Optional[bool]
    NetworkType: Optional[str]
    RemoteDataVolumeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchOptions"]:
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
_LaunchOptions = LaunchOptions


@dataclass
class SourceDetails:
    BootVolumeSizeInGbs: Optional[str]
    KmsKeyId: Optional[str]
    SourceId: Optional[str]
    SourceType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceDetails"]:
        if not json_data:
            return None
        return cls(
            BootVolumeSizeInGbs=json_data.get("BootVolumeSizeInGbs"),
            KmsKeyId=json_data.get("KmsKeyId"),
            SourceId=json_data.get("SourceId"),
            SourceType=json_data.get("SourceType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceDetails = SourceDetails


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


