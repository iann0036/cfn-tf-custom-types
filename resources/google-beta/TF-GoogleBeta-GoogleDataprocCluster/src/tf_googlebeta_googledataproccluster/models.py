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
    GracefulDecommissionTimeout: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    Project: Optional[str]
    Region: Optional[str]
    ClusterConfig: Optional[Sequence["_ClusterConfigDefinition"]]
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
            GracefulDecommissionTimeout=json_data.get("GracefulDecommissionTimeout"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            ClusterConfig=deserialize_list(json_data.get("ClusterConfig"), ClusterConfigDefinition),
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
class ClusterConfigDefinition(BaseModel):
    StagingBucket: Optional[str]
    TempBucket: Optional[str]
    AutoscalingConfig: Optional[Sequence["_AutoscalingConfigDefinition"]]
    EncryptionConfig: Optional[Sequence["_EncryptionConfigDefinition"]]
    EndpointConfig: Optional[Sequence["_EndpointConfigDefinition"]]
    GceClusterConfig: Optional[Sequence["_GceClusterConfigDefinition"]]
    InitializationAction: Optional[Sequence["_InitializationActionDefinition"]]
    LifecycleConfig: Optional[Sequence["_LifecycleConfigDefinition"]]
    MasterConfig: Optional[Sequence["_MasterConfigDefinition"]]
    PreemptibleWorkerConfig: Optional[Sequence["_PreemptibleWorkerConfigDefinition"]]
    SecurityConfig: Optional[Sequence["_SecurityConfigDefinition"]]
    SoftwareConfig: Optional[Sequence["_SoftwareConfigDefinition"]]
    WorkerConfig: Optional[Sequence["_WorkerConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            StagingBucket=json_data.get("StagingBucket"),
            TempBucket=json_data.get("TempBucket"),
            AutoscalingConfig=deserialize_list(json_data.get("AutoscalingConfig"), AutoscalingConfigDefinition),
            EncryptionConfig=deserialize_list(json_data.get("EncryptionConfig"), EncryptionConfigDefinition),
            EndpointConfig=deserialize_list(json_data.get("EndpointConfig"), EndpointConfigDefinition),
            GceClusterConfig=deserialize_list(json_data.get("GceClusterConfig"), GceClusterConfigDefinition),
            InitializationAction=deserialize_list(json_data.get("InitializationAction"), InitializationActionDefinition),
            LifecycleConfig=deserialize_list(json_data.get("LifecycleConfig"), LifecycleConfigDefinition),
            MasterConfig=deserialize_list(json_data.get("MasterConfig"), MasterConfigDefinition),
            PreemptibleWorkerConfig=deserialize_list(json_data.get("PreemptibleWorkerConfig"), PreemptibleWorkerConfigDefinition),
            SecurityConfig=deserialize_list(json_data.get("SecurityConfig"), SecurityConfigDefinition),
            SoftwareConfig=deserialize_list(json_data.get("SoftwareConfig"), SoftwareConfigDefinition),
            WorkerConfig=deserialize_list(json_data.get("WorkerConfig"), WorkerConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterConfigDefinition = ClusterConfigDefinition


@dataclass
class AutoscalingConfigDefinition(BaseModel):
    PolicyUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscalingConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscalingConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            PolicyUri=json_data.get("PolicyUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscalingConfigDefinition = AutoscalingConfigDefinition


@dataclass
class EncryptionConfigDefinition(BaseModel):
    KmsKeyName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            KmsKeyName=json_data.get("KmsKeyName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionConfigDefinition = EncryptionConfigDefinition


@dataclass
class EndpointConfigDefinition(BaseModel):
    EnableHttpPortAccess: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            EnableHttpPortAccess=json_data.get("EnableHttpPortAccess"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointConfigDefinition = EndpointConfigDefinition


@dataclass
class GceClusterConfigDefinition(BaseModel):
    InternalIpOnly: Optional[bool]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Network: Optional[str]
    ServiceAccount: Optional[str]
    ServiceAccountScopes: Optional[Sequence[str]]
    Subnetwork: Optional[str]
    Tags: Optional[Sequence[str]]
    Zone: Optional[str]
    ShieldedInstanceConfig: Optional[Sequence["_ShieldedInstanceConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_GceClusterConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GceClusterConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            InternalIpOnly=json_data.get("InternalIpOnly"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Network=json_data.get("Network"),
            ServiceAccount=json_data.get("ServiceAccount"),
            ServiceAccountScopes=json_data.get("ServiceAccountScopes"),
            Subnetwork=json_data.get("Subnetwork"),
            Tags=json_data.get("Tags"),
            Zone=json_data.get("Zone"),
            ShieldedInstanceConfig=deserialize_list(json_data.get("ShieldedInstanceConfig"), ShieldedInstanceConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_GceClusterConfigDefinition = GceClusterConfigDefinition


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
class InitializationActionDefinition(BaseModel):
    Script: Optional[str]
    TimeoutSec: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_InitializationActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InitializationActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Script=json_data.get("Script"),
            TimeoutSec=json_data.get("TimeoutSec"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InitializationActionDefinition = InitializationActionDefinition


@dataclass
class LifecycleConfigDefinition(BaseModel):
    AutoDeleteTime: Optional[str]
    IdleDeleteTtl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LifecycleConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LifecycleConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoDeleteTime=json_data.get("AutoDeleteTime"),
            IdleDeleteTtl=json_data.get("IdleDeleteTtl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LifecycleConfigDefinition = LifecycleConfigDefinition


@dataclass
class MasterConfigDefinition(BaseModel):
    ImageUri: Optional[str]
    MachineType: Optional[str]
    MinCpuPlatform: Optional[str]
    NumInstances: Optional[float]
    Accelerators: Optional[Sequence["_AcceleratorsDefinition"]]
    DiskConfig: Optional[Sequence["_DiskConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MasterConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MasterConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ImageUri=json_data.get("ImageUri"),
            MachineType=json_data.get("MachineType"),
            MinCpuPlatform=json_data.get("MinCpuPlatform"),
            NumInstances=json_data.get("NumInstances"),
            Accelerators=deserialize_list(json_data.get("Accelerators"), AcceleratorsDefinition),
            DiskConfig=deserialize_list(json_data.get("DiskConfig"), DiskConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MasterConfigDefinition = MasterConfigDefinition


@dataclass
class AcceleratorsDefinition(BaseModel):
    AcceleratorCount: Optional[float]
    AcceleratorType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AcceleratorsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AcceleratorsDefinition"]:
        if not json_data:
            return None
        return cls(
            AcceleratorCount=json_data.get("AcceleratorCount"),
            AcceleratorType=json_data.get("AcceleratorType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AcceleratorsDefinition = AcceleratorsDefinition


@dataclass
class DiskConfigDefinition(BaseModel):
    BootDiskSizeGb: Optional[float]
    BootDiskType: Optional[str]
    NumLocalSsds: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DiskConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            BootDiskSizeGb=json_data.get("BootDiskSizeGb"),
            BootDiskType=json_data.get("BootDiskType"),
            NumLocalSsds=json_data.get("NumLocalSsds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskConfigDefinition = DiskConfigDefinition


@dataclass
class PreemptibleWorkerConfigDefinition(BaseModel):
    NumInstances: Optional[float]
    DiskConfig: Optional[Sequence["_DiskConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PreemptibleWorkerConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PreemptibleWorkerConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            NumInstances=json_data.get("NumInstances"),
            DiskConfig=deserialize_list(json_data.get("DiskConfig"), DiskConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PreemptibleWorkerConfigDefinition = PreemptibleWorkerConfigDefinition


@dataclass
class SecurityConfigDefinition(BaseModel):
    KerberosConfig: Optional[Sequence["_KerberosConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SecurityConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecurityConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            KerberosConfig=deserialize_list(json_data.get("KerberosConfig"), KerberosConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecurityConfigDefinition = SecurityConfigDefinition


@dataclass
class KerberosConfigDefinition(BaseModel):
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
        cls: Type["_KerberosConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KerberosConfigDefinition"]:
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
_KerberosConfigDefinition = KerberosConfigDefinition


@dataclass
class SoftwareConfigDefinition(BaseModel):
    ImageVersion: Optional[str]
    OptionalComponents: Optional[Sequence[str]]
    OverrideProperties: Optional[Sequence["_OverridePropertiesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SoftwareConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SoftwareConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ImageVersion=json_data.get("ImageVersion"),
            OptionalComponents=json_data.get("OptionalComponents"),
            OverrideProperties=deserialize_list(json_data.get("OverrideProperties"), OverridePropertiesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SoftwareConfigDefinition = SoftwareConfigDefinition


@dataclass
class OverridePropertiesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OverridePropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OverridePropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OverridePropertiesDefinition = OverridePropertiesDefinition


@dataclass
class WorkerConfigDefinition(BaseModel):
    ImageUri: Optional[str]
    MachineType: Optional[str]
    MinCpuPlatform: Optional[str]
    NumInstances: Optional[float]
    Accelerators: Optional[Sequence["_AcceleratorsDefinition"]]
    DiskConfig: Optional[Sequence["_DiskConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WorkerConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkerConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ImageUri=json_data.get("ImageUri"),
            MachineType=json_data.get("MachineType"),
            MinCpuPlatform=json_data.get("MinCpuPlatform"),
            NumInstances=json_data.get("NumInstances"),
            Accelerators=deserialize_list(json_data.get("Accelerators"), AcceleratorsDefinition),
            DiskConfig=deserialize_list(json_data.get("DiskConfig"), DiskConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkerConfigDefinition = WorkerConfigDefinition


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


