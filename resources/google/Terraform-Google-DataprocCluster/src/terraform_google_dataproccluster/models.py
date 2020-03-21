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
    Id: Optional[str]
    Labels: Optional[Sequence["_Labels"]]
    Name: Optional[str]
    Project: Optional[str]
    Region: Optional[str]
    ClusterConfig: Optional[Sequence["_ClusterConfig"]]
    Timeouts: Optional["_Timeouts"]
    AutoscalingConfig: Optional[Sequence["_AutoscalingConfig"]]
    EncryptionConfig: Optional[Sequence["_EncryptionConfig"]]
    GceClusterConfig: Optional[Sequence["_GceClusterConfig"]]
    InitializationAction: Optional[Sequence["_InitializationAction"]]
    MasterConfig: Optional[Sequence["_MasterConfig"]]
    PreemptibleWorkerConfig: Optional[Sequence["_PreemptibleWorkerConfig"]]
    SecurityConfig: Optional[Sequence["_SecurityConfig"]]
    SoftwareConfig: Optional[Sequence["_SoftwareConfig"]]
    WorkerConfig: Optional[Sequence["_WorkerConfig"]]
    Accelerators: Optional[Sequence["_Accelerators"]]
    DiskConfig: Optional[Sequence["_DiskConfig"]]
    KerberosConfig: Optional[Sequence["_KerberosConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Id=json_data.get("Id"),
            Labels=json_data.get("Labels"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            ClusterConfig=json_data.get("ClusterConfig"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            AutoscalingConfig=json_data.get("AutoscalingConfig"),
            EncryptionConfig=json_data.get("EncryptionConfig"),
            GceClusterConfig=json_data.get("GceClusterConfig"),
            InitializationAction=json_data.get("InitializationAction"),
            MasterConfig=json_data.get("MasterConfig"),
            PreemptibleWorkerConfig=json_data.get("PreemptibleWorkerConfig"),
            SecurityConfig=json_data.get("SecurityConfig"),
            SoftwareConfig=json_data.get("SoftwareConfig"),
            WorkerConfig=json_data.get("WorkerConfig"),
            Accelerators=json_data.get("Accelerators"),
            DiskConfig=json_data.get("DiskConfig"),
            KerberosConfig=json_data.get("KerberosConfig"),
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
class ClusterConfig:
    StagingBucket: Optional[str]
    AutoscalingConfig: Optional[Sequence["_AutoscalingConfig"]]
    EncryptionConfig: Optional[Sequence["_EncryptionConfig"]]
    GceClusterConfig: Optional[Sequence["_GceClusterConfig"]]
    InitializationAction: Optional[Sequence["_InitializationAction"]]
    MasterConfig: Optional[Sequence["_MasterConfig"]]
    PreemptibleWorkerConfig: Optional[Sequence["_PreemptibleWorkerConfig"]]
    SecurityConfig: Optional[Sequence["_SecurityConfig"]]
    SoftwareConfig: Optional[Sequence["_SoftwareConfig"]]
    WorkerConfig: Optional[Sequence["_WorkerConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterConfig"]:
        if not json_data:
            return None
        return cls(
            StagingBucket=json_data.get("StagingBucket"),
            AutoscalingConfig=json_data.get("AutoscalingConfig"),
            EncryptionConfig=json_data.get("EncryptionConfig"),
            GceClusterConfig=json_data.get("GceClusterConfig"),
            InitializationAction=json_data.get("InitializationAction"),
            MasterConfig=json_data.get("MasterConfig"),
            PreemptibleWorkerConfig=json_data.get("PreemptibleWorkerConfig"),
            SecurityConfig=json_data.get("SecurityConfig"),
            SoftwareConfig=json_data.get("SoftwareConfig"),
            WorkerConfig=json_data.get("WorkerConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterConfig = ClusterConfig


@dataclass
class AutoscalingConfig:
    PolicyUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscalingConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscalingConfig"]:
        if not json_data:
            return None
        return cls(
            PolicyUri=json_data.get("PolicyUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscalingConfig = AutoscalingConfig


@dataclass
class EncryptionConfig:
    KmsKeyName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionConfig"]:
        if not json_data:
            return None
        return cls(
            KmsKeyName=json_data.get("KmsKeyName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionConfig = EncryptionConfig


@dataclass
class GceClusterConfig:
    InternalIpOnly: Optional[bool]
    Metadata: Optional[Sequence["_Metadata"]]
    Network: Optional[str]
    ServiceAccount: Optional[str]
    ServiceAccountScopes: Optional[Sequence[str]]
    Subnetwork: Optional[str]
    Tags: Optional[Sequence[str]]
    Zone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GceClusterConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GceClusterConfig"]:
        if not json_data:
            return None
        return cls(
            InternalIpOnly=json_data.get("InternalIpOnly"),
            Metadata=json_data.get("Metadata"),
            Network=json_data.get("Network"),
            ServiceAccount=json_data.get("ServiceAccount"),
            ServiceAccountScopes=json_data.get("ServiceAccountScopes"),
            Subnetwork=json_data.get("Subnetwork"),
            Tags=json_data.get("Tags"),
            Zone=json_data.get("Zone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GceClusterConfig = GceClusterConfig


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
class InitializationAction:
    Script: Optional[str]
    TimeoutSec: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_InitializationAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InitializationAction"]:
        if not json_data:
            return None
        return cls(
            Script=json_data.get("Script"),
            TimeoutSec=json_data.get("TimeoutSec"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InitializationAction = InitializationAction


@dataclass
class MasterConfig:
    ImageUri: Optional[str]
    MachineType: Optional[str]
    MinCpuPlatform: Optional[str]
    NumInstances: Optional[float]
    Accelerators: Optional[Sequence["_Accelerators"]]
    DiskConfig: Optional[Sequence["_DiskConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_MasterConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MasterConfig"]:
        if not json_data:
            return None
        return cls(
            ImageUri=json_data.get("ImageUri"),
            MachineType=json_data.get("MachineType"),
            MinCpuPlatform=json_data.get("MinCpuPlatform"),
            NumInstances=json_data.get("NumInstances"),
            Accelerators=json_data.get("Accelerators"),
            DiskConfig=json_data.get("DiskConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MasterConfig = MasterConfig


@dataclass
class Accelerators:
    AcceleratorCount: Optional[float]
    AcceleratorType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Accelerators"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Accelerators"]:
        if not json_data:
            return None
        return cls(
            AcceleratorCount=json_data.get("AcceleratorCount"),
            AcceleratorType=json_data.get("AcceleratorType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Accelerators = Accelerators


@dataclass
class DiskConfig:
    BootDiskSizeGb: Optional[float]
    BootDiskType: Optional[str]
    NumLocalSsds: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DiskConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskConfig"]:
        if not json_data:
            return None
        return cls(
            BootDiskSizeGb=json_data.get("BootDiskSizeGb"),
            BootDiskType=json_data.get("BootDiskType"),
            NumLocalSsds=json_data.get("NumLocalSsds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskConfig = DiskConfig


@dataclass
class PreemptibleWorkerConfig:
    NumInstances: Optional[float]
    DiskConfig: Optional[Sequence["_DiskConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_PreemptibleWorkerConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PreemptibleWorkerConfig"]:
        if not json_data:
            return None
        return cls(
            NumInstances=json_data.get("NumInstances"),
            DiskConfig=json_data.get("DiskConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PreemptibleWorkerConfig = PreemptibleWorkerConfig


@dataclass
class SecurityConfig:
    KerberosConfig: Optional[Sequence["_KerberosConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_SecurityConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecurityConfig"]:
        if not json_data:
            return None
        return cls(
            KerberosConfig=json_data.get("KerberosConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecurityConfig = SecurityConfig


@dataclass
class KerberosConfig:
    CrossRealmTrustAdminServer: Optional[str]
    CrossRealmTrustKdc: Optional[str]
    CrossRealmTrustRealm: Optional[str]
    CrossRealmTrustSharedPasswordUri: Optional[str]
    EnableKerberos: Optional[bool]
    KdcDbKeyUri: Optional[str]
    KeyPasswordUri: Optional[str]
    KeystorePasswordUri: Optional[str]
    KeystoreUri: Optional[str]
    KmsKeyUri: Optional[str]
    Realm: Optional[str]
    RootPrincipalPasswordUri: Optional[str]
    TgtLifetimeHours: Optional[float]
    TruststorePasswordUri: Optional[str]
    TruststoreUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KerberosConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KerberosConfig"]:
        if not json_data:
            return None
        return cls(
            CrossRealmTrustAdminServer=json_data.get("CrossRealmTrustAdminServer"),
            CrossRealmTrustKdc=json_data.get("CrossRealmTrustKdc"),
            CrossRealmTrustRealm=json_data.get("CrossRealmTrustRealm"),
            CrossRealmTrustSharedPasswordUri=json_data.get("CrossRealmTrustSharedPasswordUri"),
            EnableKerberos=json_data.get("EnableKerberos"),
            KdcDbKeyUri=json_data.get("KdcDbKeyUri"),
            KeyPasswordUri=json_data.get("KeyPasswordUri"),
            KeystorePasswordUri=json_data.get("KeystorePasswordUri"),
            KeystoreUri=json_data.get("KeystoreUri"),
            KmsKeyUri=json_data.get("KmsKeyUri"),
            Realm=json_data.get("Realm"),
            RootPrincipalPasswordUri=json_data.get("RootPrincipalPasswordUri"),
            TgtLifetimeHours=json_data.get("TgtLifetimeHours"),
            TruststorePasswordUri=json_data.get("TruststorePasswordUri"),
            TruststoreUri=json_data.get("TruststoreUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KerberosConfig = KerberosConfig


@dataclass
class SoftwareConfig:
    ImageVersion: Optional[str]
    OptionalComponents: Optional[Sequence[str]]
    OverrideProperties: Optional[Sequence["_OverrideProperties"]]

    @classmethod
    def _deserialize(
        cls: Type["_SoftwareConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SoftwareConfig"]:
        if not json_data:
            return None
        return cls(
            ImageVersion=json_data.get("ImageVersion"),
            OptionalComponents=json_data.get("OptionalComponents"),
            OverrideProperties=json_data.get("OverrideProperties"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SoftwareConfig = SoftwareConfig


@dataclass
class OverrideProperties:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OverrideProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OverrideProperties"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OverrideProperties = OverrideProperties


@dataclass
class WorkerConfig:
    ImageUri: Optional[str]
    MachineType: Optional[str]
    MinCpuPlatform: Optional[str]
    NumInstances: Optional[float]
    Accelerators: Optional[Sequence["_Accelerators"]]
    DiskConfig: Optional[Sequence["_DiskConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_WorkerConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkerConfig"]:
        if not json_data:
            return None
        return cls(
            ImageUri=json_data.get("ImageUri"),
            MachineType=json_data.get("MachineType"),
            MinCpuPlatform=json_data.get("MinCpuPlatform"),
            NumInstances=json_data.get("NumInstances"),
            Accelerators=json_data.get("Accelerators"),
            DiskConfig=json_data.get("DiskConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkerConfig = WorkerConfig


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


