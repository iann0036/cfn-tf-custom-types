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
    AvailabilityZones: Optional[Sequence[str]]
    EnableAutoScaling: Optional[bool]
    EnableHostEncryption: Optional[bool]
    EnableNodePublicIp: Optional[bool]
    EvictionPolicy: Optional[str]
    Id: Optional[str]
    KubernetesClusterId: Optional[str]
    MaxCount: Optional[float]
    MaxPods: Optional[float]
    MinCount: Optional[float]
    Mode: Optional[str]
    Name: Optional[str]
    NodeCount: Optional[float]
    NodeLabels: Optional[Sequence["_NodeLabelsDefinition"]]
    NodePublicIpPrefixId: Optional[str]
    NodeTaints: Optional[Sequence[str]]
    OrchestratorVersion: Optional[str]
    OsDiskSizeGb: Optional[float]
    OsDiskType: Optional[str]
    OsType: Optional[str]
    Priority: Optional[str]
    ProximityPlacementGroupId: Optional[str]
    SpotMaxPrice: Optional[float]
    Tags: Optional[Sequence["_TagsDefinition"]]
    VmSize: Optional[str]
    VnetSubnetId: Optional[str]
    KubeletConfig: Optional[Sequence["_KubeletConfigDefinition"]]
    LinuxOsConfig: Optional[Sequence["_LinuxOsConfigDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    UpgradeSettings: Optional[Sequence["_UpgradeSettingsDefinition"]]

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
            AvailabilityZones=json_data.get("AvailabilityZones"),
            EnableAutoScaling=json_data.get("EnableAutoScaling"),
            EnableHostEncryption=json_data.get("EnableHostEncryption"),
            EnableNodePublicIp=json_data.get("EnableNodePublicIp"),
            EvictionPolicy=json_data.get("EvictionPolicy"),
            Id=json_data.get("Id"),
            KubernetesClusterId=json_data.get("KubernetesClusterId"),
            MaxCount=json_data.get("MaxCount"),
            MaxPods=json_data.get("MaxPods"),
            MinCount=json_data.get("MinCount"),
            Mode=json_data.get("Mode"),
            Name=json_data.get("Name"),
            NodeCount=json_data.get("NodeCount"),
            NodeLabels=deserialize_list(json_data.get("NodeLabels"), NodeLabelsDefinition),
            NodePublicIpPrefixId=json_data.get("NodePublicIpPrefixId"),
            NodeTaints=json_data.get("NodeTaints"),
            OrchestratorVersion=json_data.get("OrchestratorVersion"),
            OsDiskSizeGb=json_data.get("OsDiskSizeGb"),
            OsDiskType=json_data.get("OsDiskType"),
            OsType=json_data.get("OsType"),
            Priority=json_data.get("Priority"),
            ProximityPlacementGroupId=json_data.get("ProximityPlacementGroupId"),
            SpotMaxPrice=json_data.get("SpotMaxPrice"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            VmSize=json_data.get("VmSize"),
            VnetSubnetId=json_data.get("VnetSubnetId"),
            KubeletConfig=deserialize_list(json_data.get("KubeletConfig"), KubeletConfigDefinition),
            LinuxOsConfig=deserialize_list(json_data.get("LinuxOsConfig"), LinuxOsConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            UpgradeSettings=deserialize_list(json_data.get("UpgradeSettings"), UpgradeSettingsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class NodeLabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodeLabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeLabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeLabelsDefinition = NodeLabelsDefinition


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class KubeletConfigDefinition(BaseModel):
    AllowedUnsafeSysctls: Optional[Sequence[str]]
    ContainerLogMaxLine: Optional[float]
    ContainerLogMaxSizeMb: Optional[float]
    CpuCfsQuotaEnabled: Optional[bool]
    CpuCfsQuotaPeriod: Optional[str]
    CpuManagerPolicy: Optional[str]
    ImageGcHighThreshold: Optional[float]
    ImageGcLowThreshold: Optional[float]
    PodMaxPid: Optional[float]
    TopologyManagerPolicy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KubeletConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KubeletConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowedUnsafeSysctls=json_data.get("AllowedUnsafeSysctls"),
            ContainerLogMaxLine=json_data.get("ContainerLogMaxLine"),
            ContainerLogMaxSizeMb=json_data.get("ContainerLogMaxSizeMb"),
            CpuCfsQuotaEnabled=json_data.get("CpuCfsQuotaEnabled"),
            CpuCfsQuotaPeriod=json_data.get("CpuCfsQuotaPeriod"),
            CpuManagerPolicy=json_data.get("CpuManagerPolicy"),
            ImageGcHighThreshold=json_data.get("ImageGcHighThreshold"),
            ImageGcLowThreshold=json_data.get("ImageGcLowThreshold"),
            PodMaxPid=json_data.get("PodMaxPid"),
            TopologyManagerPolicy=json_data.get("TopologyManagerPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KubeletConfigDefinition = KubeletConfigDefinition


@dataclass
class LinuxOsConfigDefinition(BaseModel):
    SwapFileSizeMb: Optional[float]
    TransparentHugePageDefrag: Optional[str]
    TransparentHugePageEnabled: Optional[str]
    SysctlConfig: Optional[Sequence["_SysctlConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LinuxOsConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LinuxOsConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            SwapFileSizeMb=json_data.get("SwapFileSizeMb"),
            TransparentHugePageDefrag=json_data.get("TransparentHugePageDefrag"),
            TransparentHugePageEnabled=json_data.get("TransparentHugePageEnabled"),
            SysctlConfig=deserialize_list(json_data.get("SysctlConfig"), SysctlConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LinuxOsConfigDefinition = LinuxOsConfigDefinition


@dataclass
class SysctlConfigDefinition(BaseModel):
    FsAioMaxNr: Optional[float]
    FsFileMax: Optional[float]
    FsInotifyMaxUserWatches: Optional[float]
    FsNrOpen: Optional[float]
    KernelThreadsMax: Optional[float]
    NetCoreNetdevMaxBacklog: Optional[float]
    NetCoreOptmemMax: Optional[float]
    NetCoreRmemDefault: Optional[float]
    NetCoreRmemMax: Optional[float]
    NetCoreSomaxconn: Optional[float]
    NetCoreWmemDefault: Optional[float]
    NetCoreWmemMax: Optional[float]
    NetIpv4IpLocalPortRangeMax: Optional[float]
    NetIpv4IpLocalPortRangeMin: Optional[float]
    NetIpv4NeighDefaultGcThresh1: Optional[float]
    NetIpv4NeighDefaultGcThresh2: Optional[float]
    NetIpv4NeighDefaultGcThresh3: Optional[float]
    NetIpv4TcpFinTimeout: Optional[float]
    NetIpv4TcpKeepaliveIntvl: Optional[float]
    NetIpv4TcpKeepaliveProbes: Optional[float]
    NetIpv4TcpKeepaliveTime: Optional[float]
    NetIpv4TcpMaxSynBacklog: Optional[float]
    NetIpv4TcpMaxTwBuckets: Optional[float]
    NetIpv4TcpTwReuse: Optional[bool]
    NetNetfilterNfConntrackBuckets: Optional[float]
    NetNetfilterNfConntrackMax: Optional[float]
    VmMaxMapCount: Optional[float]
    VmSwappiness: Optional[float]
    VmVfsCachePressure: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SysctlConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SysctlConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            FsAioMaxNr=json_data.get("FsAioMaxNr"),
            FsFileMax=json_data.get("FsFileMax"),
            FsInotifyMaxUserWatches=json_data.get("FsInotifyMaxUserWatches"),
            FsNrOpen=json_data.get("FsNrOpen"),
            KernelThreadsMax=json_data.get("KernelThreadsMax"),
            NetCoreNetdevMaxBacklog=json_data.get("NetCoreNetdevMaxBacklog"),
            NetCoreOptmemMax=json_data.get("NetCoreOptmemMax"),
            NetCoreRmemDefault=json_data.get("NetCoreRmemDefault"),
            NetCoreRmemMax=json_data.get("NetCoreRmemMax"),
            NetCoreSomaxconn=json_data.get("NetCoreSomaxconn"),
            NetCoreWmemDefault=json_data.get("NetCoreWmemDefault"),
            NetCoreWmemMax=json_data.get("NetCoreWmemMax"),
            NetIpv4IpLocalPortRangeMax=json_data.get("NetIpv4IpLocalPortRangeMax"),
            NetIpv4IpLocalPortRangeMin=json_data.get("NetIpv4IpLocalPortRangeMin"),
            NetIpv4NeighDefaultGcThresh1=json_data.get("NetIpv4NeighDefaultGcThresh1"),
            NetIpv4NeighDefaultGcThresh2=json_data.get("NetIpv4NeighDefaultGcThresh2"),
            NetIpv4NeighDefaultGcThresh3=json_data.get("NetIpv4NeighDefaultGcThresh3"),
            NetIpv4TcpFinTimeout=json_data.get("NetIpv4TcpFinTimeout"),
            NetIpv4TcpKeepaliveIntvl=json_data.get("NetIpv4TcpKeepaliveIntvl"),
            NetIpv4TcpKeepaliveProbes=json_data.get("NetIpv4TcpKeepaliveProbes"),
            NetIpv4TcpKeepaliveTime=json_data.get("NetIpv4TcpKeepaliveTime"),
            NetIpv4TcpMaxSynBacklog=json_data.get("NetIpv4TcpMaxSynBacklog"),
            NetIpv4TcpMaxTwBuckets=json_data.get("NetIpv4TcpMaxTwBuckets"),
            NetIpv4TcpTwReuse=json_data.get("NetIpv4TcpTwReuse"),
            NetNetfilterNfConntrackBuckets=json_data.get("NetNetfilterNfConntrackBuckets"),
            NetNetfilterNfConntrackMax=json_data.get("NetNetfilterNfConntrackMax"),
            VmMaxMapCount=json_data.get("VmMaxMapCount"),
            VmSwappiness=json_data.get("VmSwappiness"),
            VmVfsCachePressure=json_data.get("VmVfsCachePressure"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SysctlConfigDefinition = SysctlConfigDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


@dataclass
class UpgradeSettingsDefinition(BaseModel):
    MaxSurge: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UpgradeSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UpgradeSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxSurge=json_data.get("MaxSurge"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UpgradeSettingsDefinition = UpgradeSettingsDefinition


