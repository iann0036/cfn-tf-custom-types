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
    BootDiskSizeGb: Optional[float]
    BootDiskType: Optional[str]
    CreateTime: Optional[str]
    CustomGpuDriverPath: Optional[str]
    DataDiskSizeGb: Optional[float]
    DataDiskType: Optional[str]
    DiskEncryption: Optional[str]
    Id: Optional[str]
    InstallGpuDriver: Optional[bool]
    InstanceOwners: Optional[Sequence[str]]
    KmsKey: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Location: Optional[str]
    MachineType: Optional[str]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Name: Optional[str]
    Network: Optional[str]
    NoProxyAccess: Optional[bool]
    NoPublicIp: Optional[bool]
    NoRemoveDataDisk: Optional[bool]
    PostStartupScript: Optional[str]
    Project: Optional[str]
    ProxyUri: Optional[str]
    ServiceAccount: Optional[str]
    ServiceAccountScopes: Optional[Sequence[str]]
    State: Optional[str]
    Subnet: Optional[str]
    Tags: Optional[Sequence[str]]
    UpdateTime: Optional[str]
    AcceleratorConfig: Optional[Sequence["_AcceleratorConfigDefinition"]]
    ContainerImage: Optional[Sequence["_ContainerImageDefinition"]]
    ShieldedInstanceConfig: Optional[Sequence["_ShieldedInstanceConfigDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    VmImage: Optional[Sequence["_VmImageDefinition"]]

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
            BootDiskSizeGb=json_data.get("BootDiskSizeGb"),
            BootDiskType=json_data.get("BootDiskType"),
            CreateTime=json_data.get("CreateTime"),
            CustomGpuDriverPath=json_data.get("CustomGpuDriverPath"),
            DataDiskSizeGb=json_data.get("DataDiskSizeGb"),
            DataDiskType=json_data.get("DataDiskType"),
            DiskEncryption=json_data.get("DiskEncryption"),
            Id=json_data.get("Id"),
            InstallGpuDriver=json_data.get("InstallGpuDriver"),
            InstanceOwners=json_data.get("InstanceOwners"),
            KmsKey=json_data.get("KmsKey"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Location=json_data.get("Location"),
            MachineType=json_data.get("MachineType"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Name=json_data.get("Name"),
            Network=json_data.get("Network"),
            NoProxyAccess=json_data.get("NoProxyAccess"),
            NoPublicIp=json_data.get("NoPublicIp"),
            NoRemoveDataDisk=json_data.get("NoRemoveDataDisk"),
            PostStartupScript=json_data.get("PostStartupScript"),
            Project=json_data.get("Project"),
            ProxyUri=json_data.get("ProxyUri"),
            ServiceAccount=json_data.get("ServiceAccount"),
            ServiceAccountScopes=json_data.get("ServiceAccountScopes"),
            State=json_data.get("State"),
            Subnet=json_data.get("Subnet"),
            Tags=json_data.get("Tags"),
            UpdateTime=json_data.get("UpdateTime"),
            AcceleratorConfig=deserialize_list(json_data.get("AcceleratorConfig"), AcceleratorConfigDefinition),
            ContainerImage=deserialize_list(json_data.get("ContainerImage"), ContainerImageDefinition),
            ShieldedInstanceConfig=deserialize_list(json_data.get("ShieldedInstanceConfig"), ShieldedInstanceConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            VmImage=deserialize_list(json_data.get("VmImage"), VmImageDefinition),
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
class AcceleratorConfigDefinition(BaseModel):
    CoreCount: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AcceleratorConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AcceleratorConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CoreCount=json_data.get("CoreCount"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AcceleratorConfigDefinition = AcceleratorConfigDefinition


@dataclass
class ContainerImageDefinition(BaseModel):
    Repository: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ContainerImageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContainerImageDefinition"]:
        if not json_data:
            return None
        return cls(
            Repository=json_data.get("Repository"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContainerImageDefinition = ContainerImageDefinition


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


@dataclass
class VmImageDefinition(BaseModel):
    ImageFamily: Optional[str]
    ImageName: Optional[str]
    Project: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VmImageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VmImageDefinition"]:
        if not json_data:
            return None
        return cls(
            ImageFamily=json_data.get("ImageFamily"),
            ImageName=json_data.get("ImageName"),
            Project=json_data.get("Project"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VmImageDefinition = VmImageDefinition


