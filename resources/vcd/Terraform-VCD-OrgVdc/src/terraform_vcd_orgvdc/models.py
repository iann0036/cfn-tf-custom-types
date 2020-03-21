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
    AllocationModel: Optional[str]
    AllowOverCommit: Optional[bool]
    CpuGuaranteed: Optional[float]
    CpuSpeed: Optional[float]
    DeleteForce: Optional[bool]
    DeleteRecursive: Optional[bool]
    Description: Optional[str]
    Elasticity: Optional[bool]
    EnableFastProvisioning: Optional[bool]
    EnableThinProvisioning: Optional[bool]
    EnableVmDiscovery: Optional[bool]
    Enabled: Optional[bool]
    IncludeVmMemoryOverhead: Optional[bool]
    MemoryGuaranteed: Optional[float]
    Metadata: Optional[Sequence["_Metadata"]]
    Name: Optional[str]
    NetworkPoolName: Optional[str]
    NetworkQuota: Optional[float]
    NicQuota: Optional[float]
    Org: Optional[str]
    ProviderVdcName: Optional[str]
    VmQuota: Optional[float]
    ComputeCapacity: Optional[Sequence["_ComputeCapacity"]]
    StorageProfile: Optional[Sequence["_StorageProfile"]]
    Cpu: Optional[Sequence["_Cpu"]]
    Memory: Optional[Sequence["_Memory"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AllocationModel=json_data.get("AllocationModel"),
            AllowOverCommit=json_data.get("AllowOverCommit"),
            CpuGuaranteed=json_data.get("CpuGuaranteed"),
            CpuSpeed=json_data.get("CpuSpeed"),
            DeleteForce=json_data.get("DeleteForce"),
            DeleteRecursive=json_data.get("DeleteRecursive"),
            Description=json_data.get("Description"),
            Elasticity=json_data.get("Elasticity"),
            EnableFastProvisioning=json_data.get("EnableFastProvisioning"),
            EnableThinProvisioning=json_data.get("EnableThinProvisioning"),
            EnableVmDiscovery=json_data.get("EnableVmDiscovery"),
            Enabled=json_data.get("Enabled"),
            IncludeVmMemoryOverhead=json_data.get("IncludeVmMemoryOverhead"),
            MemoryGuaranteed=json_data.get("MemoryGuaranteed"),
            Metadata=json_data.get("Metadata"),
            Name=json_data.get("Name"),
            NetworkPoolName=json_data.get("NetworkPoolName"),
            NetworkQuota=json_data.get("NetworkQuota"),
            NicQuota=json_data.get("NicQuota"),
            Org=json_data.get("Org"),
            ProviderVdcName=json_data.get("ProviderVdcName"),
            VmQuota=json_data.get("VmQuota"),
            ComputeCapacity=json_data.get("ComputeCapacity"),
            StorageProfile=json_data.get("StorageProfile"),
            Cpu=json_data.get("Cpu"),
            Memory=json_data.get("Memory"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class ComputeCapacity:
    Cpu: Optional[Sequence["_Cpu"]]
    Memory: Optional[Sequence["_Memory"]]

    @classmethod
    def _deserialize(
        cls: Type["_ComputeCapacity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComputeCapacity"]:
        if not json_data:
            return None
        return cls(
            Cpu=json_data.get("Cpu"),
            Memory=json_data.get("Memory"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComputeCapacity = ComputeCapacity


@dataclass
class Cpu:
    Allocated: Optional[float]
    Limit: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Cpu"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Cpu"]:
        if not json_data:
            return None
        return cls(
            Allocated=json_data.get("Allocated"),
            Limit=json_data.get("Limit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Cpu = Cpu


@dataclass
class Memory:
    Allocated: Optional[float]
    Limit: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Memory"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Memory"]:
        if not json_data:
            return None
        return cls(
            Allocated=json_data.get("Allocated"),
            Limit=json_data.get("Limit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Memory = Memory


@dataclass
class StorageProfile:
    Default: Optional[bool]
    Enabled: Optional[bool]
    Limit: Optional[float]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StorageProfile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageProfile"]:
        if not json_data:
            return None
        return cls(
            Default=json_data.get("Default"),
            Enabled=json_data.get("Enabled"),
            Limit=json_data.get("Limit"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageProfile = StorageProfile


