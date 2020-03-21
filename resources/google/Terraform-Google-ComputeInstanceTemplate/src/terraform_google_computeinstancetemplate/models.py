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
    CanIpForward: Optional[bool]
    Description: Optional[str]
    EnableDisplay: Optional[bool]
    InstanceDescription: Optional[str]
    Labels: Optional[Sequence["_Labels"]]
    MachineType: Optional[str]
    Metadata: Optional[Sequence["_Metadata"]]
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
    Disk: Optional[Sequence["_Disk"]]
    GuestAccelerator: Optional[Sequence["_GuestAccelerator"]]
    NetworkInterface: Optional[Sequence["_NetworkInterface"]]
    Scheduling: Optional[Sequence["_Scheduling"]]
    ServiceAccount: Optional[Sequence["_ServiceAccount"]]
    ShieldedInstanceConfig: Optional[Sequence["_ShieldedInstanceConfig"]]
    DiskEncryptionKey: Optional[Sequence["_DiskEncryptionKey"]]
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
            CanIpForward=json_data.get("CanIpForward"),
            Description=json_data.get("Description"),
            EnableDisplay=json_data.get("EnableDisplay"),
            InstanceDescription=json_data.get("InstanceDescription"),
            Labels=json_data.get("Labels"),
            MachineType=json_data.get("MachineType"),
            Metadata=json_data.get("Metadata"),
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
            Disk=json_data.get("Disk"),
            GuestAccelerator=json_data.get("GuestAccelerator"),
            NetworkInterface=json_data.get("NetworkInterface"),
            Scheduling=json_data.get("Scheduling"),
            ServiceAccount=json_data.get("ServiceAccount"),
            ShieldedInstanceConfig=json_data.get("ShieldedInstanceConfig"),
            DiskEncryptionKey=json_data.get("DiskEncryptionKey"),
            AccessConfig=json_data.get("AccessConfig"),
            AliasIpRange=json_data.get("AliasIpRange"),
            NodeAffinities=json_data.get("NodeAffinities"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Labels:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels = Labels


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
class Disk:
    AutoDelete: Optional[bool]
    Boot: Optional[bool]
    DeviceName: Optional[str]
    DiskName: Optional[str]
    DiskSizeGb: Optional[float]
    DiskType: Optional[str]
    Interface: Optional[str]
    Labels: Optional[Sequence["_Labels2"]]
    Mode: Optional[str]
    Source: Optional[str]
    SourceImage: Optional[str]
    Type: Optional[str]
    DiskEncryptionKey: Optional[Sequence["_DiskEncryptionKey"]]

    @classmethod
    def _deserialize(
        cls: Type["_Disk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Disk"]:
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
            Labels=json_data.get("Labels"),
            Mode=json_data.get("Mode"),
            Source=json_data.get("Source"),
            SourceImage=json_data.get("SourceImage"),
            Type=json_data.get("Type"),
            DiskEncryptionKey=json_data.get("DiskEncryptionKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Disk = Disk


@dataclass
class Labels2:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels2"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels2 = Labels2


@dataclass
class DiskEncryptionKey:
    KmsKeySelfLink: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DiskEncryptionKey"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskEncryptionKey"]:
        if not json_data:
            return None
        return cls(
            KmsKeySelfLink=json_data.get("KmsKeySelfLink"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskEncryptionKey = DiskEncryptionKey


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


