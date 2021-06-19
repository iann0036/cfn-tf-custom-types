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
    Id: Optional[str]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Spec: Optional[Sequence["_SpecDefinition"]]
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
            Id=json_data.get("Id"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Spec=deserialize_list(json_data.get("Spec"), SpecDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MetadataDefinition(BaseModel):
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


@dataclass
class AnnotationsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnnotationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnnotationsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnnotationsDefinition = AnnotationsDefinition


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
class SpecDefinition(BaseModel):
    AccessModes: Optional[Sequence[str]]
    Capacity: Optional[Sequence["_CapacityDefinition"]]
    MountOptions: Optional[Sequence[str]]
    PersistentVolumeReclaimPolicy: Optional[str]
    StorageClassName: Optional[str]
    VolumeMode: Optional[str]
    ClaimRef: Optional[Sequence["_ClaimRefDefinition"]]
    NodeAffinity: Optional[Sequence["_NodeAffinityDefinition"]]
    PersistentVolumeSource: Optional[Sequence["_PersistentVolumeSourceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SpecDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpecDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessModes=json_data.get("AccessModes"),
            Capacity=deserialize_list(json_data.get("Capacity"), CapacityDefinition),
            MountOptions=json_data.get("MountOptions"),
            PersistentVolumeReclaimPolicy=json_data.get("PersistentVolumeReclaimPolicy"),
            StorageClassName=json_data.get("StorageClassName"),
            VolumeMode=json_data.get("VolumeMode"),
            ClaimRef=deserialize_list(json_data.get("ClaimRef"), ClaimRefDefinition),
            NodeAffinity=deserialize_list(json_data.get("NodeAffinity"), NodeAffinityDefinition),
            PersistentVolumeSource=deserialize_list(json_data.get("PersistentVolumeSource"), PersistentVolumeSourceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpecDefinition = SpecDefinition


@dataclass
class CapacityDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CapacityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapacityDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CapacityDefinition = CapacityDefinition


@dataclass
class ClaimRefDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClaimRefDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClaimRefDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClaimRefDefinition = ClaimRefDefinition


@dataclass
class NodeAffinityDefinition(BaseModel):
    Required: Optional[Sequence["_RequiredDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NodeAffinityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeAffinityDefinition"]:
        if not json_data:
            return None
        return cls(
            Required=deserialize_list(json_data.get("Required"), RequiredDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeAffinityDefinition = NodeAffinityDefinition


@dataclass
class RequiredDefinition(BaseModel):
    NodeSelectorTerm: Optional[Sequence["_NodeSelectorTermDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RequiredDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequiredDefinition"]:
        if not json_data:
            return None
        return cls(
            NodeSelectorTerm=deserialize_list(json_data.get("NodeSelectorTerm"), NodeSelectorTermDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequiredDefinition = RequiredDefinition


@dataclass
class NodeSelectorTermDefinition(BaseModel):
    MatchExpressions: Optional[Sequence["_MatchExpressionsDefinition"]]
    MatchFields: Optional[Sequence["_MatchFieldsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NodeSelectorTermDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeSelectorTermDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchExpressions=deserialize_list(json_data.get("MatchExpressions"), MatchExpressionsDefinition),
            MatchFields=deserialize_list(json_data.get("MatchFields"), MatchFieldsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeSelectorTermDefinition = NodeSelectorTermDefinition


@dataclass
class MatchExpressionsDefinition(BaseModel):
    Key: Optional[str]
    Operator: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchExpressionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchExpressionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Operator=json_data.get("Operator"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchExpressionsDefinition = MatchExpressionsDefinition


@dataclass
class MatchFieldsDefinition(BaseModel):
    Key: Optional[str]
    Operator: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchFieldsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchFieldsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Operator=json_data.get("Operator"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchFieldsDefinition = MatchFieldsDefinition


@dataclass
class PersistentVolumeSourceDefinition(BaseModel):
    AwsElasticBlockStore: Optional[Sequence["_AwsElasticBlockStoreDefinition"]]
    AzureDisk: Optional[Sequence["_AzureDiskDefinition"]]
    AzureFile: Optional[Sequence["_AzureFileDefinition"]]
    CephFs: Optional[Sequence["_CephFsDefinition"]]
    Cinder: Optional[Sequence["_CinderDefinition"]]
    Csi: Optional[Sequence["_CsiDefinition"]]
    Fc: Optional[Sequence["_FcDefinition"]]
    FlexVolume: Optional[Sequence["_FlexVolumeDefinition"]]
    Flocker: Optional[Sequence["_FlockerDefinition"]]
    GcePersistentDisk: Optional[Sequence["_GcePersistentDiskDefinition"]]
    Glusterfs: Optional[Sequence["_GlusterfsDefinition"]]
    HostPath: Optional[Sequence["_HostPathDefinition"]]
    Iscsi: Optional[Sequence["_IscsiDefinition"]]
    Local: Optional[Sequence["_LocalDefinition"]]
    Nfs: Optional[Sequence["_NfsDefinition"]]
    PhotonPersistentDisk: Optional[Sequence["_PhotonPersistentDiskDefinition"]]
    Quobyte: Optional[Sequence["_QuobyteDefinition"]]
    Rbd: Optional[Sequence["_RbdDefinition"]]
    VsphereVolume: Optional[Sequence["_VsphereVolumeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PersistentVolumeSourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PersistentVolumeSourceDefinition"]:
        if not json_data:
            return None
        return cls(
            AwsElasticBlockStore=deserialize_list(json_data.get("AwsElasticBlockStore"), AwsElasticBlockStoreDefinition),
            AzureDisk=deserialize_list(json_data.get("AzureDisk"), AzureDiskDefinition),
            AzureFile=deserialize_list(json_data.get("AzureFile"), AzureFileDefinition),
            CephFs=deserialize_list(json_data.get("CephFs"), CephFsDefinition),
            Cinder=deserialize_list(json_data.get("Cinder"), CinderDefinition),
            Csi=deserialize_list(json_data.get("Csi"), CsiDefinition),
            Fc=deserialize_list(json_data.get("Fc"), FcDefinition),
            FlexVolume=deserialize_list(json_data.get("FlexVolume"), FlexVolumeDefinition),
            Flocker=deserialize_list(json_data.get("Flocker"), FlockerDefinition),
            GcePersistentDisk=deserialize_list(json_data.get("GcePersistentDisk"), GcePersistentDiskDefinition),
            Glusterfs=deserialize_list(json_data.get("Glusterfs"), GlusterfsDefinition),
            HostPath=deserialize_list(json_data.get("HostPath"), HostPathDefinition),
            Iscsi=deserialize_list(json_data.get("Iscsi"), IscsiDefinition),
            Local=deserialize_list(json_data.get("Local"), LocalDefinition),
            Nfs=deserialize_list(json_data.get("Nfs"), NfsDefinition),
            PhotonPersistentDisk=deserialize_list(json_data.get("PhotonPersistentDisk"), PhotonPersistentDiskDefinition),
            Quobyte=deserialize_list(json_data.get("Quobyte"), QuobyteDefinition),
            Rbd=deserialize_list(json_data.get("Rbd"), RbdDefinition),
            VsphereVolume=deserialize_list(json_data.get("VsphereVolume"), VsphereVolumeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PersistentVolumeSourceDefinition = PersistentVolumeSourceDefinition


@dataclass
class AwsElasticBlockStoreDefinition(BaseModel):
    FsType: Optional[str]
    Partition: Optional[float]
    ReadOnly: Optional[bool]
    VolumeId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsElasticBlockStoreDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsElasticBlockStoreDefinition"]:
        if not json_data:
            return None
        return cls(
            FsType=json_data.get("FsType"),
            Partition=json_data.get("Partition"),
            ReadOnly=json_data.get("ReadOnly"),
            VolumeId=json_data.get("VolumeId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsElasticBlockStoreDefinition = AwsElasticBlockStoreDefinition


@dataclass
class AzureDiskDefinition(BaseModel):
    CachingMode: Optional[str]
    DataDiskUri: Optional[str]
    DiskName: Optional[str]
    FsType: Optional[str]
    Kind: Optional[str]
    ReadOnly: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AzureDiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureDiskDefinition"]:
        if not json_data:
            return None
        return cls(
            CachingMode=json_data.get("CachingMode"),
            DataDiskUri=json_data.get("DataDiskUri"),
            DiskName=json_data.get("DiskName"),
            FsType=json_data.get("FsType"),
            Kind=json_data.get("Kind"),
            ReadOnly=json_data.get("ReadOnly"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureDiskDefinition = AzureDiskDefinition


@dataclass
class AzureFileDefinition(BaseModel):
    ReadOnly: Optional[bool]
    SecretName: Optional[str]
    SecretNamespace: Optional[str]
    ShareName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureFileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureFileDefinition"]:
        if not json_data:
            return None
        return cls(
            ReadOnly=json_data.get("ReadOnly"),
            SecretName=json_data.get("SecretName"),
            SecretNamespace=json_data.get("SecretNamespace"),
            ShareName=json_data.get("ShareName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureFileDefinition = AzureFileDefinition


@dataclass
class CephFsDefinition(BaseModel):
    Monitors: Optional[Sequence[str]]
    Path: Optional[str]
    ReadOnly: Optional[bool]
    SecretFile: Optional[str]
    User: Optional[str]
    SecretRef: Optional[Sequence["_SecretRefDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CephFsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CephFsDefinition"]:
        if not json_data:
            return None
        return cls(
            Monitors=json_data.get("Monitors"),
            Path=json_data.get("Path"),
            ReadOnly=json_data.get("ReadOnly"),
            SecretFile=json_data.get("SecretFile"),
            User=json_data.get("User"),
            SecretRef=deserialize_list(json_data.get("SecretRef"), SecretRefDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CephFsDefinition = CephFsDefinition


@dataclass
class SecretRefDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecretRefDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecretRefDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecretRefDefinition = SecretRefDefinition


@dataclass
class CinderDefinition(BaseModel):
    FsType: Optional[str]
    ReadOnly: Optional[bool]
    VolumeId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CinderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CinderDefinition"]:
        if not json_data:
            return None
        return cls(
            FsType=json_data.get("FsType"),
            ReadOnly=json_data.get("ReadOnly"),
            VolumeId=json_data.get("VolumeId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CinderDefinition = CinderDefinition


@dataclass
class CsiDefinition(BaseModel):
    Driver: Optional[str]
    FsType: Optional[str]
    ReadOnly: Optional[bool]
    VolumeAttributes: Optional[Sequence["_VolumeAttributesDefinition"]]
    VolumeHandle: Optional[str]
    ControllerExpandSecretRef: Optional[Sequence["_ControllerExpandSecretRefDefinition"]]
    ControllerPublishSecretRef: Optional[Sequence["_ControllerPublishSecretRefDefinition"]]
    NodePublishSecretRef: Optional[Sequence["_NodePublishSecretRefDefinition"]]
    NodeStageSecretRef: Optional[Sequence["_NodeStageSecretRefDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CsiDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CsiDefinition"]:
        if not json_data:
            return None
        return cls(
            Driver=json_data.get("Driver"),
            FsType=json_data.get("FsType"),
            ReadOnly=json_data.get("ReadOnly"),
            VolumeAttributes=deserialize_list(json_data.get("VolumeAttributes"), VolumeAttributesDefinition),
            VolumeHandle=json_data.get("VolumeHandle"),
            ControllerExpandSecretRef=deserialize_list(json_data.get("ControllerExpandSecretRef"), ControllerExpandSecretRefDefinition),
            ControllerPublishSecretRef=deserialize_list(json_data.get("ControllerPublishSecretRef"), ControllerPublishSecretRefDefinition),
            NodePublishSecretRef=deserialize_list(json_data.get("NodePublishSecretRef"), NodePublishSecretRefDefinition),
            NodeStageSecretRef=deserialize_list(json_data.get("NodeStageSecretRef"), NodeStageSecretRefDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CsiDefinition = CsiDefinition


@dataclass
class VolumeAttributesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VolumeAttributesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VolumeAttributesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VolumeAttributesDefinition = VolumeAttributesDefinition


@dataclass
class ControllerExpandSecretRefDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ControllerExpandSecretRefDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ControllerExpandSecretRefDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ControllerExpandSecretRefDefinition = ControllerExpandSecretRefDefinition


@dataclass
class ControllerPublishSecretRefDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ControllerPublishSecretRefDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ControllerPublishSecretRefDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ControllerPublishSecretRefDefinition = ControllerPublishSecretRefDefinition


@dataclass
class NodePublishSecretRefDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodePublishSecretRefDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodePublishSecretRefDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodePublishSecretRefDefinition = NodePublishSecretRefDefinition


@dataclass
class NodeStageSecretRefDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodeStageSecretRefDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeStageSecretRefDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeStageSecretRefDefinition = NodeStageSecretRefDefinition


@dataclass
class FcDefinition(BaseModel):
    FsType: Optional[str]
    Lun: Optional[float]
    ReadOnly: Optional[bool]
    TargetWwNs: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_FcDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FcDefinition"]:
        if not json_data:
            return None
        return cls(
            FsType=json_data.get("FsType"),
            Lun=json_data.get("Lun"),
            ReadOnly=json_data.get("ReadOnly"),
            TargetWwNs=json_data.get("TargetWwNs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FcDefinition = FcDefinition


@dataclass
class FlexVolumeDefinition(BaseModel):
    Driver: Optional[str]
    FsType: Optional[str]
    Options: Optional[Sequence["_OptionsDefinition"]]
    ReadOnly: Optional[bool]
    SecretRef: Optional[Sequence["_SecretRefDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FlexVolumeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FlexVolumeDefinition"]:
        if not json_data:
            return None
        return cls(
            Driver=json_data.get("Driver"),
            FsType=json_data.get("FsType"),
            Options=deserialize_list(json_data.get("Options"), OptionsDefinition),
            ReadOnly=json_data.get("ReadOnly"),
            SecretRef=deserialize_list(json_data.get("SecretRef"), SecretRefDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FlexVolumeDefinition = FlexVolumeDefinition


@dataclass
class OptionsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OptionsDefinition = OptionsDefinition


@dataclass
class FlockerDefinition(BaseModel):
    DatasetName: Optional[str]
    DatasetUuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FlockerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FlockerDefinition"]:
        if not json_data:
            return None
        return cls(
            DatasetName=json_data.get("DatasetName"),
            DatasetUuid=json_data.get("DatasetUuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FlockerDefinition = FlockerDefinition


@dataclass
class GcePersistentDiskDefinition(BaseModel):
    FsType: Optional[str]
    Partition: Optional[float]
    PdName: Optional[str]
    ReadOnly: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_GcePersistentDiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GcePersistentDiskDefinition"]:
        if not json_data:
            return None
        return cls(
            FsType=json_data.get("FsType"),
            Partition=json_data.get("Partition"),
            PdName=json_data.get("PdName"),
            ReadOnly=json_data.get("ReadOnly"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GcePersistentDiskDefinition = GcePersistentDiskDefinition


@dataclass
class GlusterfsDefinition(BaseModel):
    EndpointsName: Optional[str]
    Path: Optional[str]
    ReadOnly: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_GlusterfsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GlusterfsDefinition"]:
        if not json_data:
            return None
        return cls(
            EndpointsName=json_data.get("EndpointsName"),
            Path=json_data.get("Path"),
            ReadOnly=json_data.get("ReadOnly"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GlusterfsDefinition = GlusterfsDefinition


@dataclass
class HostPathDefinition(BaseModel):
    Path: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HostPathDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostPathDefinition"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostPathDefinition = HostPathDefinition


@dataclass
class IscsiDefinition(BaseModel):
    FsType: Optional[str]
    Iqn: Optional[str]
    IscsiInterface: Optional[str]
    Lun: Optional[float]
    ReadOnly: Optional[bool]
    TargetPortal: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IscsiDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IscsiDefinition"]:
        if not json_data:
            return None
        return cls(
            FsType=json_data.get("FsType"),
            Iqn=json_data.get("Iqn"),
            IscsiInterface=json_data.get("IscsiInterface"),
            Lun=json_data.get("Lun"),
            ReadOnly=json_data.get("ReadOnly"),
            TargetPortal=json_data.get("TargetPortal"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IscsiDefinition = IscsiDefinition


@dataclass
class LocalDefinition(BaseModel):
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LocalDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocalDefinition"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocalDefinition = LocalDefinition


@dataclass
class NfsDefinition(BaseModel):
    Path: Optional[str]
    ReadOnly: Optional[bool]
    Server: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NfsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NfsDefinition"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            ReadOnly=json_data.get("ReadOnly"),
            Server=json_data.get("Server"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NfsDefinition = NfsDefinition


@dataclass
class PhotonPersistentDiskDefinition(BaseModel):
    FsType: Optional[str]
    PdId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PhotonPersistentDiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PhotonPersistentDiskDefinition"]:
        if not json_data:
            return None
        return cls(
            FsType=json_data.get("FsType"),
            PdId=json_data.get("PdId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PhotonPersistentDiskDefinition = PhotonPersistentDiskDefinition


@dataclass
class QuobyteDefinition(BaseModel):
    Group: Optional[str]
    ReadOnly: Optional[bool]
    Registry: Optional[str]
    User: Optional[str]
    Volume: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_QuobyteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QuobyteDefinition"]:
        if not json_data:
            return None
        return cls(
            Group=json_data.get("Group"),
            ReadOnly=json_data.get("ReadOnly"),
            Registry=json_data.get("Registry"),
            User=json_data.get("User"),
            Volume=json_data.get("Volume"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QuobyteDefinition = QuobyteDefinition


@dataclass
class RbdDefinition(BaseModel):
    CephMonitors: Optional[Sequence[str]]
    FsType: Optional[str]
    Keyring: Optional[str]
    RadosUser: Optional[str]
    RbdImage: Optional[str]
    RbdPool: Optional[str]
    ReadOnly: Optional[bool]
    SecretRef: Optional[Sequence["_SecretRefDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RbdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RbdDefinition"]:
        if not json_data:
            return None
        return cls(
            CephMonitors=json_data.get("CephMonitors"),
            FsType=json_data.get("FsType"),
            Keyring=json_data.get("Keyring"),
            RadosUser=json_data.get("RadosUser"),
            RbdImage=json_data.get("RbdImage"),
            RbdPool=json_data.get("RbdPool"),
            ReadOnly=json_data.get("ReadOnly"),
            SecretRef=deserialize_list(json_data.get("SecretRef"), SecretRefDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RbdDefinition = RbdDefinition


@dataclass
class VsphereVolumeDefinition(BaseModel):
    FsType: Optional[str]
    VolumePath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VsphereVolumeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VsphereVolumeDefinition"]:
        if not json_data:
            return None
        return cls(
            FsType=json_data.get("FsType"),
            VolumePath=json_data.get("VolumePath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VsphereVolumeDefinition = VsphereVolumeDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


