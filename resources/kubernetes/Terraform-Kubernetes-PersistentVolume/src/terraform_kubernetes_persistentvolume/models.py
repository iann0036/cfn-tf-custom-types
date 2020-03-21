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
    Metadata: Optional[Sequence["_Metadata"]]
    Spec: Optional[Sequence["_Spec"]]
    Timeouts: Optional["_Timeouts"]
    NodeAffinity: Optional[Sequence["_NodeAffinity"]]
    PersistentVolumeSource: Optional[Sequence["_PersistentVolumeSource"]]
    Required: Optional[Sequence["_Required"]]
    AwsElasticBlockStore: Optional[Sequence["_AwsElasticBlockStore"]]
    AzureDisk: Optional[Sequence["_AzureDisk"]]
    AzureFile: Optional[Sequence["_AzureFile"]]
    CephFs: Optional[Sequence["_CephFs"]]
    Cinder: Optional[Sequence["_Cinder"]]
    Fc: Optional[Sequence["_Fc"]]
    FlexVolume: Optional[Sequence["_FlexVolume"]]
    Flocker: Optional[Sequence["_Flocker"]]
    GcePersistentDisk: Optional[Sequence["_GcePersistentDisk"]]
    Glusterfs: Optional[Sequence["_Glusterfs"]]
    HostPath: Optional[Sequence["_HostPath"]]
    Iscsi: Optional[Sequence["_Iscsi"]]
    Local: Optional[Sequence["_Local"]]
    Nfs: Optional[Sequence["_Nfs"]]
    PhotonPersistentDisk: Optional[Sequence["_PhotonPersistentDisk"]]
    Quobyte: Optional[Sequence["_Quobyte"]]
    Rbd: Optional[Sequence["_Rbd"]]
    VsphereVolume: Optional[Sequence["_VsphereVolume"]]
    NodeSelectorTerm: Optional[Sequence["_NodeSelectorTerm"]]
    SecretRef: Optional[Sequence["_SecretRef"]]
    MatchExpressions: Optional[Sequence["_MatchExpressions"]]
    MatchFields: Optional[Sequence["_MatchFields"]]

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
            Metadata=json_data.get("Metadata"),
            Spec=json_data.get("Spec"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            NodeAffinity=json_data.get("NodeAffinity"),
            PersistentVolumeSource=json_data.get("PersistentVolumeSource"),
            Required=json_data.get("Required"),
            AwsElasticBlockStore=json_data.get("AwsElasticBlockStore"),
            AzureDisk=json_data.get("AzureDisk"),
            AzureFile=json_data.get("AzureFile"),
            CephFs=json_data.get("CephFs"),
            Cinder=json_data.get("Cinder"),
            Fc=json_data.get("Fc"),
            FlexVolume=json_data.get("FlexVolume"),
            Flocker=json_data.get("Flocker"),
            GcePersistentDisk=json_data.get("GcePersistentDisk"),
            Glusterfs=json_data.get("Glusterfs"),
            HostPath=json_data.get("HostPath"),
            Iscsi=json_data.get("Iscsi"),
            Local=json_data.get("Local"),
            Nfs=json_data.get("Nfs"),
            PhotonPersistentDisk=json_data.get("PhotonPersistentDisk"),
            Quobyte=json_data.get("Quobyte"),
            Rbd=json_data.get("Rbd"),
            VsphereVolume=json_data.get("VsphereVolume"),
            NodeSelectorTerm=json_data.get("NodeSelectorTerm"),
            SecretRef=json_data.get("SecretRef"),
            MatchExpressions=json_data.get("MatchExpressions"),
            MatchFields=json_data.get("MatchFields"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Metadata:
    Annotations: Optional[Sequence["_Annotations"]]
    Labels: Optional[Sequence["_Labels"]]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metadata"]:
        if not json_data:
            return None
        return cls(
            Annotations=json_data.get("Annotations"),
            Labels=json_data.get("Labels"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metadata = Metadata


@dataclass
class Annotations:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Annotations"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Annotations"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Annotations = Annotations


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
class Spec:
    AccessModes: Optional[Sequence[str]]
    Capacity: Optional[Sequence["_Capacity"]]
    MountOptions: Optional[Sequence[str]]
    PersistentVolumeReclaimPolicy: Optional[str]
    StorageClassName: Optional[str]
    NodeAffinity: Optional[Sequence["_NodeAffinity"]]
    PersistentVolumeSource: Optional[Sequence["_PersistentVolumeSource"]]

    @classmethod
    def _deserialize(
        cls: Type["_Spec"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Spec"]:
        if not json_data:
            return None
        return cls(
            AccessModes=json_data.get("AccessModes"),
            Capacity=json_data.get("Capacity"),
            MountOptions=json_data.get("MountOptions"),
            PersistentVolumeReclaimPolicy=json_data.get("PersistentVolumeReclaimPolicy"),
            StorageClassName=json_data.get("StorageClassName"),
            NodeAffinity=json_data.get("NodeAffinity"),
            PersistentVolumeSource=json_data.get("PersistentVolumeSource"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Spec = Spec


@dataclass
class Capacity:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Capacity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Capacity"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Capacity = Capacity


@dataclass
class NodeAffinity:
    Required: Optional[Sequence["_Required"]]

    @classmethod
    def _deserialize(
        cls: Type["_NodeAffinity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeAffinity"]:
        if not json_data:
            return None
        return cls(
            Required=json_data.get("Required"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeAffinity = NodeAffinity


@dataclass
class Required:
    NodeSelectorTerm: Optional[Sequence["_NodeSelectorTerm"]]

    @classmethod
    def _deserialize(
        cls: Type["_Required"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Required"]:
        if not json_data:
            return None
        return cls(
            NodeSelectorTerm=json_data.get("NodeSelectorTerm"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Required = Required


@dataclass
class NodeSelectorTerm:
    MatchExpressions: Optional[Sequence["_MatchExpressions"]]
    MatchFields: Optional[Sequence["_MatchFields"]]

    @classmethod
    def _deserialize(
        cls: Type["_NodeSelectorTerm"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeSelectorTerm"]:
        if not json_data:
            return None
        return cls(
            MatchExpressions=json_data.get("MatchExpressions"),
            MatchFields=json_data.get("MatchFields"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeSelectorTerm = NodeSelectorTerm


@dataclass
class MatchExpressions:
    Key: Optional[str]
    Operator: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchExpressions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchExpressions"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Operator=json_data.get("Operator"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchExpressions = MatchExpressions


@dataclass
class MatchFields:
    Key: Optional[str]
    Operator: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchFields"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchFields"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Operator=json_data.get("Operator"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchFields = MatchFields


@dataclass
class PersistentVolumeSource:
    AwsElasticBlockStore: Optional[Sequence["_AwsElasticBlockStore"]]
    AzureDisk: Optional[Sequence["_AzureDisk"]]
    AzureFile: Optional[Sequence["_AzureFile"]]
    CephFs: Optional[Sequence["_CephFs"]]
    Cinder: Optional[Sequence["_Cinder"]]
    Fc: Optional[Sequence["_Fc"]]
    FlexVolume: Optional[Sequence["_FlexVolume"]]
    Flocker: Optional[Sequence["_Flocker"]]
    GcePersistentDisk: Optional[Sequence["_GcePersistentDisk"]]
    Glusterfs: Optional[Sequence["_Glusterfs"]]
    HostPath: Optional[Sequence["_HostPath"]]
    Iscsi: Optional[Sequence["_Iscsi"]]
    Local: Optional[Sequence["_Local"]]
    Nfs: Optional[Sequence["_Nfs"]]
    PhotonPersistentDisk: Optional[Sequence["_PhotonPersistentDisk"]]
    Quobyte: Optional[Sequence["_Quobyte"]]
    Rbd: Optional[Sequence["_Rbd"]]
    VsphereVolume: Optional[Sequence["_VsphereVolume"]]

    @classmethod
    def _deserialize(
        cls: Type["_PersistentVolumeSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PersistentVolumeSource"]:
        if not json_data:
            return None
        return cls(
            AwsElasticBlockStore=json_data.get("AwsElasticBlockStore"),
            AzureDisk=json_data.get("AzureDisk"),
            AzureFile=json_data.get("AzureFile"),
            CephFs=json_data.get("CephFs"),
            Cinder=json_data.get("Cinder"),
            Fc=json_data.get("Fc"),
            FlexVolume=json_data.get("FlexVolume"),
            Flocker=json_data.get("Flocker"),
            GcePersistentDisk=json_data.get("GcePersistentDisk"),
            Glusterfs=json_data.get("Glusterfs"),
            HostPath=json_data.get("HostPath"),
            Iscsi=json_data.get("Iscsi"),
            Local=json_data.get("Local"),
            Nfs=json_data.get("Nfs"),
            PhotonPersistentDisk=json_data.get("PhotonPersistentDisk"),
            Quobyte=json_data.get("Quobyte"),
            Rbd=json_data.get("Rbd"),
            VsphereVolume=json_data.get("VsphereVolume"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PersistentVolumeSource = PersistentVolumeSource


@dataclass
class AwsElasticBlockStore:
    FsType: Optional[str]
    Partition: Optional[float]
    ReadOnly: Optional[bool]
    VolumeId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsElasticBlockStore"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsElasticBlockStore"]:
        if not json_data:
            return None
        return cls(
            FsType=json_data.get("FsType"),
            Partition=json_data.get("Partition"),
            ReadOnly=json_data.get("ReadOnly"),
            VolumeId=json_data.get("VolumeId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsElasticBlockStore = AwsElasticBlockStore


@dataclass
class AzureDisk:
    CachingMode: Optional[str]
    DataDiskUri: Optional[str]
    DiskName: Optional[str]
    FsType: Optional[str]
    ReadOnly: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AzureDisk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureDisk"]:
        if not json_data:
            return None
        return cls(
            CachingMode=json_data.get("CachingMode"),
            DataDiskUri=json_data.get("DataDiskUri"),
            DiskName=json_data.get("DiskName"),
            FsType=json_data.get("FsType"),
            ReadOnly=json_data.get("ReadOnly"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureDisk = AzureDisk


@dataclass
class AzureFile:
    ReadOnly: Optional[bool]
    SecretName: Optional[str]
    ShareName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureFile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureFile"]:
        if not json_data:
            return None
        return cls(
            ReadOnly=json_data.get("ReadOnly"),
            SecretName=json_data.get("SecretName"),
            ShareName=json_data.get("ShareName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureFile = AzureFile


@dataclass
class CephFs:
    Monitors: Optional[Sequence[str]]
    Path: Optional[str]
    ReadOnly: Optional[bool]
    SecretFile: Optional[str]
    User: Optional[str]
    SecretRef: Optional[Sequence["_SecretRef"]]

    @classmethod
    def _deserialize(
        cls: Type["_CephFs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CephFs"]:
        if not json_data:
            return None
        return cls(
            Monitors=json_data.get("Monitors"),
            Path=json_data.get("Path"),
            ReadOnly=json_data.get("ReadOnly"),
            SecretFile=json_data.get("SecretFile"),
            User=json_data.get("User"),
            SecretRef=json_data.get("SecretRef"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CephFs = CephFs


@dataclass
class SecretRef:
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecretRef"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecretRef"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecretRef = SecretRef


@dataclass
class Cinder:
    FsType: Optional[str]
    ReadOnly: Optional[bool]
    VolumeId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Cinder"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Cinder"]:
        if not json_data:
            return None
        return cls(
            FsType=json_data.get("FsType"),
            ReadOnly=json_data.get("ReadOnly"),
            VolumeId=json_data.get("VolumeId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Cinder = Cinder


@dataclass
class Fc:
    FsType: Optional[str]
    Lun: Optional[float]
    ReadOnly: Optional[bool]
    TargetWwNs: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Fc"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Fc"]:
        if not json_data:
            return None
        return cls(
            FsType=json_data.get("FsType"),
            Lun=json_data.get("Lun"),
            ReadOnly=json_data.get("ReadOnly"),
            TargetWwNs=json_data.get("TargetWwNs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Fc = Fc


@dataclass
class FlexVolume:
    Driver: Optional[str]
    FsType: Optional[str]
    Options: Optional[Sequence["_Options"]]
    ReadOnly: Optional[bool]
    SecretRef: Optional[Sequence["_SecretRef"]]

    @classmethod
    def _deserialize(
        cls: Type["_FlexVolume"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FlexVolume"]:
        if not json_data:
            return None
        return cls(
            Driver=json_data.get("Driver"),
            FsType=json_data.get("FsType"),
            Options=json_data.get("Options"),
            ReadOnly=json_data.get("ReadOnly"),
            SecretRef=json_data.get("SecretRef"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FlexVolume = FlexVolume


@dataclass
class Options:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Options"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Options"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Options = Options


@dataclass
class Flocker:
    DatasetName: Optional[str]
    DatasetUuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Flocker"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Flocker"]:
        if not json_data:
            return None
        return cls(
            DatasetName=json_data.get("DatasetName"),
            DatasetUuid=json_data.get("DatasetUuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Flocker = Flocker


@dataclass
class GcePersistentDisk:
    FsType: Optional[str]
    Partition: Optional[float]
    PdName: Optional[str]
    ReadOnly: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_GcePersistentDisk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GcePersistentDisk"]:
        if not json_data:
            return None
        return cls(
            FsType=json_data.get("FsType"),
            Partition=json_data.get("Partition"),
            PdName=json_data.get("PdName"),
            ReadOnly=json_data.get("ReadOnly"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GcePersistentDisk = GcePersistentDisk


@dataclass
class Glusterfs:
    EndpointsName: Optional[str]
    Path: Optional[str]
    ReadOnly: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Glusterfs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Glusterfs"]:
        if not json_data:
            return None
        return cls(
            EndpointsName=json_data.get("EndpointsName"),
            Path=json_data.get("Path"),
            ReadOnly=json_data.get("ReadOnly"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Glusterfs = Glusterfs


@dataclass
class HostPath:
    Path: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HostPath"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostPath"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostPath = HostPath


@dataclass
class Iscsi:
    FsType: Optional[str]
    Iqn: Optional[str]
    IscsiInterface: Optional[str]
    Lun: Optional[float]
    ReadOnly: Optional[bool]
    TargetPortal: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Iscsi"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Iscsi"]:
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
_Iscsi = Iscsi


@dataclass
class Local:
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Local"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Local"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Local = Local


@dataclass
class Nfs:
    Path: Optional[str]
    ReadOnly: Optional[bool]
    Server: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Nfs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Nfs"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            ReadOnly=json_data.get("ReadOnly"),
            Server=json_data.get("Server"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Nfs = Nfs


@dataclass
class PhotonPersistentDisk:
    FsType: Optional[str]
    PdId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PhotonPersistentDisk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PhotonPersistentDisk"]:
        if not json_data:
            return None
        return cls(
            FsType=json_data.get("FsType"),
            PdId=json_data.get("PdId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PhotonPersistentDisk = PhotonPersistentDisk


@dataclass
class Quobyte:
    Group: Optional[str]
    ReadOnly: Optional[bool]
    Registry: Optional[str]
    User: Optional[str]
    Volume: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Quobyte"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Quobyte"]:
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
_Quobyte = Quobyte


@dataclass
class Rbd:
    CephMonitors: Optional[Sequence[str]]
    FsType: Optional[str]
    Keyring: Optional[str]
    RadosUser: Optional[str]
    RbdImage: Optional[str]
    RbdPool: Optional[str]
    ReadOnly: Optional[bool]
    SecretRef: Optional[Sequence["_SecretRef"]]

    @classmethod
    def _deserialize(
        cls: Type["_Rbd"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rbd"]:
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
            SecretRef=json_data.get("SecretRef"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rbd = Rbd


@dataclass
class VsphereVolume:
    FsType: Optional[str]
    VolumePath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VsphereVolume"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VsphereVolume"]:
        if not json_data:
            return None
        return cls(
            FsType=json_data.get("FsType"),
            VolumePath=json_data.get("VolumePath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VsphereVolume = VsphereVolume


@dataclass
class Timeouts:
    Create: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


