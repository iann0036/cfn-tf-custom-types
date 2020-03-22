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
    AllowStoppingForUpdate: Optional[bool]
    CanIpForward: Optional[bool]
    CpuPlatform: Optional[str]
    DeletionProtection: Optional[bool]
    Description: Optional[str]
    DesiredStatus: Optional[str]
    EnableDisplay: Optional[bool]
    GuestAccelerator: Optional[Sequence["_GuestAccelerator"]]
    Hostname: Optional[str]
    Id: Optional[str]
    InstanceId: Optional[str]
    LabelFingerprint: Optional[str]
    Labels: Optional[Sequence["_Labels"]]
    MachineType: Optional[str]
    Metadata: Optional[Sequence["_Metadata"]]
    MetadataFingerprint: Optional[str]
    MetadataStartupScript: Optional[str]
    MinCpuPlatform: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    SelfLink: Optional[str]
    Tags: Optional[Sequence[str]]
    TagsFingerprint: Optional[str]
    Zone: Optional[str]
    AttachedDisk: Optional[Sequence["_AttachedDisk"]]
    BootDisk: Optional[Sequence["_BootDisk"]]
    NetworkInterface: Optional[Sequence["_NetworkInterface"]]
    Scheduling: Optional[Sequence["_Scheduling"]]
    ScratchDisk: Optional[Sequence["_ScratchDisk"]]
    ServiceAccount: Optional[Sequence["_ServiceAccount"]]
    ShieldedInstanceConfig: Optional[Sequence["_ShieldedInstanceConfig"]]
    Timeouts: Optional["_Timeouts"]
    InitializeParams: Optional[Sequence["_InitializeParams"]]
    AccessConfig: Optional[Sequence["_AccessConfig"]]
    AliasIpRange: Optional[Sequence["_AliasIpRange"]]
    NodeAffinities: Optional[Sequence["_NodeAffinities"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AllowStoppingForUpdate=json_data.get("AllowStoppingForUpdate"),
            CanIpForward=json_data.get("CanIpForward"),
            CpuPlatform=json_data.get("CpuPlatform"),
            DeletionProtection=json_data.get("DeletionProtection"),
            Description=json_data.get("Description"),
            DesiredStatus=json_data.get("DesiredStatus"),
            EnableDisplay=json_data.get("EnableDisplay"),
            GuestAccelerator=json_data.get("GuestAccelerator"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            InstanceId=json_data.get("InstanceId"),
            LabelFingerprint=json_data.get("LabelFingerprint"),
            Labels=json_data.get("Labels"),
            MachineType=json_data.get("MachineType"),
            Metadata=json_data.get("Metadata"),
            MetadataFingerprint=json_data.get("MetadataFingerprint"),
            MetadataStartupScript=json_data.get("MetadataStartupScript"),
            MinCpuPlatform=json_data.get("MinCpuPlatform"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            SelfLink=json_data.get("SelfLink"),
            Tags=json_data.get("Tags"),
            TagsFingerprint=json_data.get("TagsFingerprint"),
            Zone=json_data.get("Zone"),
            AttachedDisk=json_data.get("AttachedDisk"),
            BootDisk=json_data.get("BootDisk"),
            NetworkInterface=json_data.get("NetworkInterface"),
            Scheduling=json_data.get("Scheduling"),
            ScratchDisk=json_data.get("ScratchDisk"),
            ServiceAccount=json_data.get("ServiceAccount"),
            ShieldedInstanceConfig=json_data.get("ShieldedInstanceConfig"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            InitializeParams=json_data.get("InitializeParams"),
            AccessConfig=json_data.get("AccessConfig"),
            AliasIpRange=json_data.get("AliasIpRange"),
            NodeAffinities=json_data.get("NodeAffinities"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class AttachedDisk:
    DeviceName: Optional[str]
    DiskEncryptionKeyRaw: Optional[str]
    KmsKeySelfLink: Optional[str]
    Mode: Optional[str]
    Source: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AttachedDisk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttachedDisk"]:
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
_AttachedDisk = AttachedDisk


@dataclass
class BootDisk:
    AutoDelete: Optional[bool]
    DeviceName: Optional[str]
    DiskEncryptionKeyRaw: Optional[str]
    KmsKeySelfLink: Optional[str]
    Mode: Optional[str]
    Source: Optional[str]
    InitializeParams: Optional[Sequence["_InitializeParams"]]

    @classmethod
    def _deserialize(
        cls: Type["_BootDisk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BootDisk"]:
        if not json_data:
            return None
        return cls(
            AutoDelete=json_data.get("AutoDelete"),
            DeviceName=json_data.get("DeviceName"),
            DiskEncryptionKeyRaw=json_data.get("DiskEncryptionKeyRaw"),
            KmsKeySelfLink=json_data.get("KmsKeySelfLink"),
            Mode=json_data.get("Mode"),
            Source=json_data.get("Source"),
            InitializeParams=json_data.get("InitializeParams"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BootDisk = BootDisk


@dataclass
class InitializeParams:
    Image: Optional[str]
    Labels: Optional[Sequence["_Labels2"]]
    Size: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InitializeParams"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InitializeParams"]:
        if not json_data:
            return None
        return cls(
            Image=json_data.get("Image"),
            Labels=json_data.get("Labels"),
            Size=json_data.get("Size"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InitializeParams = InitializeParams


@dataclass
class Labels2:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels2 = Labels2


@dataclass
class NetworkInterface:
    Network: Optional[str]
    NetworkIp: Optional[str]
    Subnetwork: Optional[str]
    SubnetworkProject: Optional[str]
    AccessConfig: Optional[Sequence["_AccessConfig"]]
    AliasIpRange: Optional[Sequence["_AliasIpRange"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInterface"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterface"]:
        if not json_data:
            return None
        return cls(
            Network=json_data.get("Network"),
            NetworkIp=json_data.get("NetworkIp"),
            Subnetwork=json_data.get("Subnetwork"),
            SubnetworkProject=json_data.get("SubnetworkProject"),
            AccessConfig=json_data.get("AccessConfig"),
            AliasIpRange=json_data.get("AliasIpRange"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInterface = NetworkInterface


@dataclass
class AccessConfig:
    NatIp: Optional[str]
    NetworkTier: Optional[str]
    PublicPtrDomainName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessConfig"]:
        if not json_data:
            return None
        return cls(
            NatIp=json_data.get("NatIp"),
            NetworkTier=json_data.get("NetworkTier"),
            PublicPtrDomainName=json_data.get("PublicPtrDomainName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessConfig = AccessConfig


@dataclass
class AliasIpRange:
    IpCidrRange: Optional[str]
    SubnetworkRangeName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AliasIpRange"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AliasIpRange"]:
        if not json_data:
            return None
        return cls(
            IpCidrRange=json_data.get("IpCidrRange"),
            SubnetworkRangeName=json_data.get("SubnetworkRangeName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AliasIpRange = AliasIpRange


@dataclass
class Scheduling:
    AutomaticRestart: Optional[bool]
    OnHostMaintenance: Optional[str]
    Preemptible: Optional[bool]
    NodeAffinities: Optional[Sequence["_NodeAffinities"]]

    @classmethod
    def _deserialize(
        cls: Type["_Scheduling"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Scheduling"]:
        if not json_data:
            return None
        return cls(
            AutomaticRestart=json_data.get("AutomaticRestart"),
            OnHostMaintenance=json_data.get("OnHostMaintenance"),
            Preemptible=json_data.get("Preemptible"),
            NodeAffinities=json_data.get("NodeAffinities"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Scheduling = Scheduling


@dataclass
class NodeAffinities:
    Key: Optional[str]
    Operator: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_NodeAffinities"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeAffinities"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Operator=json_data.get("Operator"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeAffinities = NodeAffinities


@dataclass
class ScratchDisk:
    Interface: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScratchDisk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScratchDisk"]:
        if not json_data:
            return None
        return cls(
            Interface=json_data.get("Interface"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScratchDisk = ScratchDisk


@dataclass
class ServiceAccount:
    Email: Optional[str]
    Scopes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceAccount"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceAccount"]:
        if not json_data:
            return None
        return cls(
            Email=json_data.get("Email"),
            Scopes=json_data.get("Scopes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceAccount = ServiceAccount


@dataclass
class ShieldedInstanceConfig:
    EnableIntegrityMonitoring: Optional[bool]
    EnableSecureBoot: Optional[bool]
    EnableVtpm: Optional[bool]

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
            EnableVtpm=json_data.get("EnableVtpm"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ShieldedInstanceConfig = ShieldedInstanceConfig


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


