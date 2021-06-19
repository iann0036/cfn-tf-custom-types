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
    CanIpForward: Optional[bool]
    Description: Optional[str]
    EnableDisplay: Optional[bool]
    Id: Optional[str]
    InstanceDescription: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    MachineType: Optional[str]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    MetadataFingerprint: Optional[str]
    MetadataStartupScript: Optional[str]
    MinCpuPlatform: Optional[str]
    Name: Optional[str]
    NamePrefix: Optional[str]
    Project: Optional[str]
    Region: Optional[str]
    SelfLink: Optional[str]
    Tags: Optional[Sequence[str]]
    TagsFingerprint: Optional[str]
    ConfidentialInstanceConfig: Optional[Sequence["_ConfidentialInstanceConfigDefinition"]]
    Disk: Optional[Sequence["_DiskDefinition"]]
    GuestAccelerator: Optional[Sequence["_GuestAcceleratorDefinition"]]
    NetworkInterface: Optional[Sequence["_NetworkInterfaceDefinition"]]
    ReservationAffinity: Optional[Sequence["_ReservationAffinityDefinition"]]
    Scheduling: Optional[Sequence["_SchedulingDefinition"]]
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
            CanIpForward=json_data.get("CanIpForward"),
            Description=json_data.get("Description"),
            EnableDisplay=json_data.get("EnableDisplay"),
            Id=json_data.get("Id"),
            InstanceDescription=json_data.get("InstanceDescription"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            MachineType=json_data.get("MachineType"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            MetadataFingerprint=json_data.get("MetadataFingerprint"),
            MetadataStartupScript=json_data.get("MetadataStartupScript"),
            MinCpuPlatform=json_data.get("MinCpuPlatform"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            SelfLink=json_data.get("SelfLink"),
            Tags=json_data.get("Tags"),
            TagsFingerprint=json_data.get("TagsFingerprint"),
            ConfidentialInstanceConfig=deserialize_list(json_data.get("ConfidentialInstanceConfig"), ConfidentialInstanceConfigDefinition),
            Disk=deserialize_list(json_data.get("Disk"), DiskDefinition),
            GuestAccelerator=deserialize_list(json_data.get("GuestAccelerator"), GuestAcceleratorDefinition),
            NetworkInterface=deserialize_list(json_data.get("NetworkInterface"), NetworkInterfaceDefinition),
            ReservationAffinity=deserialize_list(json_data.get("ReservationAffinity"), ReservationAffinityDefinition),
            Scheduling=deserialize_list(json_data.get("Scheduling"), SchedulingDefinition),
            ServiceAccount=deserialize_list(json_data.get("ServiceAccount"), ServiceAccountDefinition),
            ShieldedInstanceConfig=deserialize_list(json_data.get("ShieldedInstanceConfig"), ShieldedInstanceConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class DiskDefinition(BaseModel):
    AutoDelete: Optional[bool]
    Boot: Optional[bool]
    DeviceName: Optional[str]
    DiskName: Optional[str]
    DiskSizeGb: Optional[float]
    DiskType: Optional[str]
    Interface: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition2"]]
    Mode: Optional[str]
    ResourcePolicies: Optional[Sequence[str]]
    Source: Optional[str]
    SourceImage: Optional[str]
    Type: Optional[str]
    DiskEncryptionKey: Optional[Sequence["_DiskEncryptionKeyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoDelete=json_data.get("AutoDelete"),
            Boot=json_data.get("Boot"),
            DeviceName=json_data.get("DeviceName"),
            DiskName=json_data.get("DiskName"),
            DiskSizeGb=json_data.get("DiskSizeGb"),
            DiskType=json_data.get("DiskType"),
            Interface=json_data.get("Interface"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition2),
            Mode=json_data.get("Mode"),
            ResourcePolicies=json_data.get("ResourcePolicies"),
            Source=json_data.get("Source"),
            SourceImage=json_data.get("SourceImage"),
            Type=json_data.get("Type"),
            DiskEncryptionKey=deserialize_list(json_data.get("DiskEncryptionKey"), DiskEncryptionKeyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskDefinition = DiskDefinition


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
class DiskEncryptionKeyDefinition(BaseModel):
    KmsKeySelfLink: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DiskEncryptionKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskEncryptionKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            KmsKeySelfLink=json_data.get("KmsKeySelfLink"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskEncryptionKeyDefinition = DiskEncryptionKeyDefinition


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
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


