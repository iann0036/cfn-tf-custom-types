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
    AllocationModel: Optional[str]
    AllowOverCommit: Optional[bool]
    CpuGuaranteed: Optional[float]
    CpuSpeed: Optional[float]
    DefaultVmSizingPolicyId: Optional[str]
    DeleteForce: Optional[bool]
    DeleteRecursive: Optional[bool]
    Description: Optional[str]
    Elasticity: Optional[bool]
    EnableFastProvisioning: Optional[bool]
    EnableThinProvisioning: Optional[bool]
    EnableVmDiscovery: Optional[bool]
    Enabled: Optional[bool]
    Id: Optional[str]
    IncludeVmMemoryOverhead: Optional[bool]
    MemoryGuaranteed: Optional[float]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Name: Optional[str]
    NetworkPoolName: Optional[str]
    NetworkQuota: Optional[float]
    NicQuota: Optional[float]
    Org: Optional[str]
    ProviderVdcName: Optional[str]
    VmQuota: Optional[float]
    VmSizingPolicyIds: Optional[Sequence[str]]
    ComputeCapacity: Optional[Sequence["_ComputeCapacityDefinition"]]
    StorageProfile: Optional[Sequence["_StorageProfileDefinition"]]

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
            AllocationModel=json_data.get("AllocationModel"),
            AllowOverCommit=json_data.get("AllowOverCommit"),
            CpuGuaranteed=json_data.get("CpuGuaranteed"),
            CpuSpeed=json_data.get("CpuSpeed"),
            DefaultVmSizingPolicyId=json_data.get("DefaultVmSizingPolicyId"),
            DeleteForce=json_data.get("DeleteForce"),
            DeleteRecursive=json_data.get("DeleteRecursive"),
            Description=json_data.get("Description"),
            Elasticity=json_data.get("Elasticity"),
            EnableFastProvisioning=json_data.get("EnableFastProvisioning"),
            EnableThinProvisioning=json_data.get("EnableThinProvisioning"),
            EnableVmDiscovery=json_data.get("EnableVmDiscovery"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            IncludeVmMemoryOverhead=json_data.get("IncludeVmMemoryOverhead"),
            MemoryGuaranteed=json_data.get("MemoryGuaranteed"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Name=json_data.get("Name"),
            NetworkPoolName=json_data.get("NetworkPoolName"),
            NetworkQuota=json_data.get("NetworkQuota"),
            NicQuota=json_data.get("NicQuota"),
            Org=json_data.get("Org"),
            ProviderVdcName=json_data.get("ProviderVdcName"),
            VmQuota=json_data.get("VmQuota"),
            VmSizingPolicyIds=json_data.get("VmSizingPolicyIds"),
            ComputeCapacity=deserialize_list(json_data.get("ComputeCapacity"), ComputeCapacityDefinition),
            StorageProfile=deserialize_list(json_data.get("StorageProfile"), StorageProfileDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class ComputeCapacityDefinition(BaseModel):
    Cpu: Optional[Sequence["_CpuDefinition"]]
    Memory: Optional[Sequence["_MemoryDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ComputeCapacityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComputeCapacityDefinition"]:
        if not json_data:
            return None
        return cls(
            Cpu=deserialize_list(json_data.get("Cpu"), CpuDefinition),
            Memory=deserialize_list(json_data.get("Memory"), MemoryDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComputeCapacityDefinition = ComputeCapacityDefinition


@dataclass
class CpuDefinition(BaseModel):
    Allocated: Optional[float]
    Limit: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CpuDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CpuDefinition"]:
        if not json_data:
            return None
        return cls(
            Allocated=json_data.get("Allocated"),
            Limit=json_data.get("Limit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CpuDefinition = CpuDefinition


@dataclass
class MemoryDefinition(BaseModel):
    Allocated: Optional[float]
    Limit: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MemoryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MemoryDefinition"]:
        if not json_data:
            return None
        return cls(
            Allocated=json_data.get("Allocated"),
            Limit=json_data.get("Limit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MemoryDefinition = MemoryDefinition


@dataclass
class StorageProfileDefinition(BaseModel):
    Default: Optional[bool]
    Enabled: Optional[bool]
    Limit: Optional[float]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StorageProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            Default=json_data.get("Default"),
            Enabled=json_data.get("Enabled"),
            Limit=json_data.get("Limit"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageProfileDefinition = StorageProfileDefinition


