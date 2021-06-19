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
    AllowStoppingForUpdate: Optional[bool]
    CanIpForward: Optional[bool]
    CpuPlatform: Optional[str]
    CurrentStatus: Optional[str]
    DeletionProtection: Optional[bool]
    Description: Optional[str]
    DesiredStatus: Optional[str]
    EnableDisplay: Optional[bool]
    GuestAccelerator: Optional[Sequence["_GuestAcceleratorDefinition"]]
    Hostname: Optional[str]
    Id: Optional[str]
    InstanceId: Optional[str]
    LabelFingerprint: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    MachineType: Optional[str]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    MetadataFingerprint: Optional[str]
    MetadataStartupScript: Optional[str]
    MinCpuPlatform: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    ResourcePolicies: Optional[Sequence[str]]
    SelfLink: Optional[str]
    Tags: Optional[Sequence[str]]
    TagsFingerprint: Optional[str]
    Zone: Optional[str]
    AttachedDisk: Optional[Sequence["_AttachedDiskDefinition"]]
    BootDisk: Optional[Sequence["_BootDiskDefinition"]]
    ConfidentialInstanceConfig: Optional[Sequence["_ConfidentialInstanceConfigDefinition"]]
    NetworkInterface: Optional[Sequence["_NetworkInterfaceDefinition"]]
    ReservationAffinity: Optional[Sequence["_ReservationAffinityDefinition"]]
    Scheduling: Optional[Sequence["_SchedulingDefinition"]]
    ScratchDisk: Optional[Sequence["_ScratchDiskDefinition"]]
    ServiceAccount: Optional[Sequence["_ServiceAccountDefinition"]]
    ShieldedInstanceConfig: Optional[Sequence["_ShieldedInstanceConfigDefinition"]]
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
            AllowStoppingForUpdate=json_data.get("AllowStoppingForUpdate"),
            CanIpForward=json_data.get("CanIpForward"),
            CpuPlatform=json_data.get("CpuPlatform"),
            CurrentStatus=json_data.get("CurrentStatus"),
            DeletionProtection=json_data.get("DeletionProtection"),
            Description=json_data.get("Description"),
            DesiredStatus=json_data.get("DesiredStatus"),
            EnableDisplay=json_data.get("EnableDisplay"),
            GuestAccelerator=deserialize_list(json_data.get("GuestAccelerator"), GuestAcceleratorDefinition),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            InstanceId=json_data.get("InstanceId"),
            LabelFingerprint=json_data.get("LabelFingerprint"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            MachineType=json_data.get("MachineType"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            MetadataFingerprint=json_data.get("MetadataFingerprint"),
            MetadataStartupScript=json_data.get("MetadataStartupScript"),
            MinCpuPlatform=json_data.get("MinCpuPlatform"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            ResourcePolicies=json_data.get("ResourcePolicies"),
            SelfLink=json_data.get("SelfLink"),
            Tags=json_data.get("Tags"),
            TagsFingerprint=json_data.get("TagsFingerprint"),
            Zone=json_data.get("Zone"),
            AttachedDisk=deserialize_list(json_data.get("AttachedDisk"), AttachedDiskDefinition),
            BootDisk=deserialize_list(json_data.get("BootDisk"), BootDiskDefinition),
            ConfidentialInstanceConfig=deserialize_list(json_data.get("ConfidentialInstanceConfig"), ConfidentialInstanceConfigDefinition),
            NetworkInterface=deserialize_list(json_data.get("NetworkInterface"), NetworkInterfaceDefinition),
            ReservationAffinity=deserialize_list(json_data.get("ReservationAffinity"), ReservationAffinityDefinition),
            Scheduling=deserialize_list(json_data.get("Scheduling"), SchedulingDefinition),
            ScratchDisk=deserialize_list(json_data.get("ScratchDisk"), ScratchDiskDefinition),
            ServiceAccount=deserialize_list(json_data.get("ServiceAccount"), ServiceAccountDefinition),
            ShieldedInstanceConfig=deserialize_list(json_data.get("ShieldedInstanceConfig"), ShieldedInstanceConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class AttachedDiskDefinition(BaseModel):
    DeviceName: Optional[str]
    DiskEncryptionKeyRaw: Optional[str]
    KmsKeySelfLink: Optional[str]
    Mode: Optional[str]
    Source: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AttachedDiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttachedDiskDefinition"]:
        if not json_data:
            return None
        return cls(
            DeviceName=json_data.get("DeviceName"),
            DiskEncryptionKeyRaw=json_data.get("DiskEncryptionKeyRaw"),
            KmsKeySelfLink=json_data.get("KmsKeySelfLink"),
            Mode=json_data.get("Mode"),
            Source=json_data.get("Source"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttachedDiskDefinition = AttachedDiskDefinition


@dataclass
class BootDiskDefinition(BaseModel):
    AutoDelete: Optional[bool]
    DeviceName: Optional[str]
    DiskEncryptionKeyRaw: Optional[str]
    KmsKeySelfLink: Optional[str]
    Mode: Optional[str]
    Source: Optional[str]
    InitializeParams: Optional[Sequence["_InitializeParamsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BootDiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BootDiskDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoDelete=json_data.get("AutoDelete"),
            DeviceName=json_data.get("DeviceName"),
            DiskEncryptionKeyRaw=json_data.get("DiskEncryptionKeyRaw"),
            KmsKeySelfLink=json_data.get("KmsKeySelfLink"),
            Mode=json_data.get("Mode"),
            Source=json_data.get("Source"),
            InitializeParams=deserialize_list(json_data.get("InitializeParams"), InitializeParamsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BootDiskDefinition = BootDiskDefinition


@dataclass
class InitializeParamsDefinition(BaseModel):
    Image: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition2"]]
    Size: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InitializeParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InitializeParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            Image=json_data.get("Image"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition2),
            Size=json_data.get("Size"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InitializeParamsDefinition = InitializeParamsDefinition


@dataclass
class LabelsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition2 = LabelsDefinition2


@dataclass
class ConfidentialInstanceConfigDefinition(BaseModel):
    EnableConfidentialCompute: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ConfidentialInstanceConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfidentialInstanceConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            EnableConfidentialCompute=json_data.get("EnableConfidentialCompute"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfidentialInstanceConfigDefinition = ConfidentialInstanceConfigDefinition


@dataclass
class NetworkInterfaceDefinition(BaseModel):
    Network: Optional[str]
    NetworkIp: Optional[str]
    NicType: Optional[str]
    Subnetwork: Optional[str]
    SubnetworkProject: Optional[str]
    AccessConfig: Optional[Sequence["_AccessConfigDefinition"]]
    AliasIpRange: Optional[Sequence["_AliasIpRangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInterfaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterfaceDefinition"]:
        if not json_data:
            return None
        return cls(
            Network=json_data.get("Network"),
            NetworkIp=json_data.get("NetworkIp"),
            NicType=json_data.get("NicType"),
            Subnetwork=json_data.get("Subnetwork"),
            SubnetworkProject=json_data.get("SubnetworkProject"),
            AccessConfig=deserialize_list(json_data.get("AccessConfig"), AccessConfigDefinition),
            AliasIpRange=deserialize_list(json_data.get("AliasIpRange"), AliasIpRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInterfaceDefinition = NetworkInterfaceDefinition


@dataclass
class AccessConfigDefinition(BaseModel):
    NatIp: Optional[str]
    NetworkTier: Optional[str]
    PublicPtrDomainName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            NatIp=json_data.get("NatIp"),
            NetworkTier=json_data.get("NetworkTier"),
            PublicPtrDomainName=json_data.get("PublicPtrDomainName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessConfigDefinition = AccessConfigDefinition


@dataclass
class AliasIpRangeDefinition(BaseModel):
    IpCidrRange: Optional[str]
    SubnetworkRangeName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AliasIpRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AliasIpRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            IpCidrRange=json_data.get("IpCidrRange"),
            SubnetworkRangeName=json_data.get("SubnetworkRangeName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AliasIpRangeDefinition = AliasIpRangeDefinition


@dataclass
class ReservationAffinityDefinition(BaseModel):
    Type: Optional[str]
    SpecificReservation: Optional[Sequence["_SpecificReservationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ReservationAffinityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReservationAffinityDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            SpecificReservation=deserialize_list(json_data.get("SpecificReservation"), SpecificReservationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReservationAffinityDefinition = ReservationAffinityDefinition


@dataclass
class SpecificReservationDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SpecificReservationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpecificReservationDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpecificReservationDefinition = SpecificReservationDefinition


@dataclass
class SchedulingDefinition(BaseModel):
    AutomaticRestart: Optional[bool]
    MinNodeCpus: Optional[float]
    OnHostMaintenance: Optional[str]
    Preemptible: Optional[bool]
    NodeAffinities: Optional[Sequence["_NodeAffinitiesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SchedulingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SchedulingDefinition"]:
        if not json_data:
            return None
        return cls(
            AutomaticRestart=json_data.get("AutomaticRestart"),
            MinNodeCpus=json_data.get("MinNodeCpus"),
            OnHostMaintenance=json_data.get("OnHostMaintenance"),
            Preemptible=json_data.get("Preemptible"),
            NodeAffinities=deserialize_list(json_data.get("NodeAffinities"), NodeAffinitiesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SchedulingDefinition = SchedulingDefinition


@dataclass
class NodeAffinitiesDefinition(BaseModel):
    Key: Optional[str]
    Operator: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_NodeAffinitiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeAffinitiesDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Operator=json_data.get("Operator"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeAffinitiesDefinition = NodeAffinitiesDefinition


@dataclass
class ScratchDiskDefinition(BaseModel):
    Interface: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScratchDiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScratchDiskDefinition"]:
        if not json_data:
            return None
        return cls(
            Interface=json_data.get("Interface"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScratchDiskDefinition = ScratchDiskDefinition


@dataclass
class ServiceAccountDefinition(BaseModel):
    Email: Optional[str]
    Scopes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceAccountDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceAccountDefinition"]:
        if not json_data:
            return None
        return cls(
            Email=json_data.get("Email"),
            Scopes=json_data.get("Scopes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceAccountDefinition = ServiceAccountDefinition


@dataclass
class ShieldedInstanceConfigDefinition(BaseModel):
    EnableIntegrityMonitoring: Optional[bool]
    EnableSecureBoot: Optional[bool]
    EnableVtpm: Optional[bool]

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
            EnableVtpm=json_data.get("EnableVtpm"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ShieldedInstanceConfigDefinition = ShieldedInstanceConfigDefinition


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


