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
    ApiEndpoint: Optional[str]
    Applications: Optional[str]
    BuiltAt: Optional[str]
    CreatedAt: Optional[str]
    DnsEntry: Optional[str]
    Id: Optional[str]
    InstalledApplications: Optional[Sequence["_InstalledApplicationsDefinition"]]
    Instances: Optional[Sequence["_InstancesDefinition"]]
    Kubeconfig: Optional[str]
    KubernetesVersion: Optional[str]
    MasterIp: Optional[str]
    Name: Optional[str]
    NetworkId: Optional[str]
    NumTargetNodes: Optional[float]
    Pools: Optional[Sequence["_PoolsDefinition2"]]
    Ready: Optional[bool]
    Region: Optional[str]
    Status: Optional[str]
    Tags: Optional[str]
    TargetNodesSize: Optional[str]

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
            ApiEndpoint=json_data.get("ApiEndpoint"),
            Applications=json_data.get("Applications"),
            BuiltAt=json_data.get("BuiltAt"),
            CreatedAt=json_data.get("CreatedAt"),
            DnsEntry=json_data.get("DnsEntry"),
            Id=json_data.get("Id"),
            InstalledApplications=deserialize_list(json_data.get("InstalledApplications"), InstalledApplicationsDefinition),
            Instances=deserialize_list(json_data.get("Instances"), InstancesDefinition),
            Kubeconfig=json_data.get("Kubeconfig"),
            KubernetesVersion=json_data.get("KubernetesVersion"),
            MasterIp=json_data.get("MasterIp"),
            Name=json_data.get("Name"),
            NetworkId=json_data.get("NetworkId"),
            NumTargetNodes=json_data.get("NumTargetNodes"),
            Pools=deserialize_list(json_data.get("Pools"), PoolsDefinition2),
            Ready=json_data.get("Ready"),
            Region=json_data.get("Region"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
            TargetNodesSize=json_data.get("TargetNodesSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InstalledApplicationsDefinition(BaseModel):
    Application: Optional[str]
    Category: Optional[str]
    Installed: Optional[bool]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InstalledApplicationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstalledApplicationsDefinition"]:
        if not json_data:
            return None
        return cls(
            Application=json_data.get("Application"),
            Category=json_data.get("Category"),
            Installed=json_data.get("Installed"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstalledApplicationsDefinition = InstalledApplicationsDefinition


@dataclass
class InstancesDefinition(BaseModel):
    CpuCores: Optional[float]
    DiskGb: Optional[float]
    Hostname: Optional[str]
    RamMb: Optional[float]
    Size: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_InstancesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstancesDefinition"]:
        if not json_data:
            return None
        return cls(
            CpuCores=json_data.get("CpuCores"),
            DiskGb=json_data.get("DiskGb"),
            Hostname=json_data.get("Hostname"),
            RamMb=json_data.get("RamMb"),
            Size=json_data.get("Size"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstancesDefinition = InstancesDefinition


@dataclass
class PoolsDefinition2(BaseModel):
    Count: Optional[float]
    Id: Optional[str]
    InstanceNames: Optional[Sequence[str]]
    Instances: Optional[Sequence["_PoolsDefinition"]]
    Size: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PoolsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PoolsDefinition2"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
            Id=json_data.get("Id"),
            InstanceNames=json_data.get("InstanceNames"),
            Instances=deserialize_list(json_data.get("Instances"), PoolsDefinition),
            Size=json_data.get("Size"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PoolsDefinition2 = PoolsDefinition2


@dataclass
class PoolsDefinition(BaseModel):
    CpuCores: Optional[float]
    DiskGb: Optional[float]
    Hostname: Optional[str]
    RamMb: Optional[float]
    Size: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PoolsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PoolsDefinition"]:
        if not json_data:
            return None
        return cls(
            CpuCores=json_data.get("CpuCores"),
            DiskGb=json_data.get("DiskGb"),
            Hostname=json_data.get("Hostname"),
            RamMb=json_data.get("RamMb"),
            Size=json_data.get("Size"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PoolsDefinition = PoolsDefinition


