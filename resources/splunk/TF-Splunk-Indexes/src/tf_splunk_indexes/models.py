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
    BlockSignSize: Optional[float]
    BucketRebuildMemoryHint: Optional[str]
    ColdPath: Optional[str]
    ColdToFrozenDir: Optional[str]
    ColdToFrozenScript: Optional[str]
    CompressRawdata: Optional[bool]
    Datatype: Optional[str]
    EnableOnlineBucketRepair: Optional[bool]
    FrozenTimePeriodInSecs: Optional[float]
    HomePath: Optional[str]
    Id: Optional[str]
    MaxBloomBackfillBucketAge: Optional[str]
    MaxConcurrentOptimizes: Optional[float]
    MaxDataSize: Optional[str]
    MaxHotBuckets: Optional[float]
    MaxHotIdleSecs: Optional[float]
    MaxHotSpanSecs: Optional[float]
    MaxMemMb: Optional[float]
    MaxMetaEntries: Optional[float]
    MaxTimeUnreplicatedNoAcks: Optional[float]
    MaxTimeUnreplicatedWithAcks: Optional[float]
    MaxTotalDataSizeMb: Optional[float]
    MaxWarmDbCount: Optional[float]
    MinRawFileSyncSecs: Optional[str]
    MinStreamGroupQueueSize: Optional[float]
    Name: Optional[str]
    PartialServiceMetaPeriod: Optional[float]
    ProcessTrackerServiceInterval: Optional[float]
    QuarantineFutureSecs: Optional[float]
    QuarantinePastSecs: Optional[float]
    RawChunkSizeBytes: Optional[float]
    RepFactor: Optional[str]
    RotatePeriodInSecs: Optional[float]
    ServiceMetaPeriod: Optional[float]
    SyncMeta: Optional[bool]
    ThawedPath: Optional[str]
    ThrottleCheckPeriod: Optional[float]
    TstatsHomePath: Optional[str]
    WarmToColdScript: Optional[str]
    Acl: Optional[Sequence["_AclDefinition"]]

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
            BlockSignSize=json_data.get("BlockSignSize"),
            BucketRebuildMemoryHint=json_data.get("BucketRebuildMemoryHint"),
            ColdPath=json_data.get("ColdPath"),
            ColdToFrozenDir=json_data.get("ColdToFrozenDir"),
            ColdToFrozenScript=json_data.get("ColdToFrozenScript"),
            CompressRawdata=json_data.get("CompressRawdata"),
            Datatype=json_data.get("Datatype"),
            EnableOnlineBucketRepair=json_data.get("EnableOnlineBucketRepair"),
            FrozenTimePeriodInSecs=json_data.get("FrozenTimePeriodInSecs"),
            HomePath=json_data.get("HomePath"),
            Id=json_data.get("Id"),
            MaxBloomBackfillBucketAge=json_data.get("MaxBloomBackfillBucketAge"),
            MaxConcurrentOptimizes=json_data.get("MaxConcurrentOptimizes"),
            MaxDataSize=json_data.get("MaxDataSize"),
            MaxHotBuckets=json_data.get("MaxHotBuckets"),
            MaxHotIdleSecs=json_data.get("MaxHotIdleSecs"),
            MaxHotSpanSecs=json_data.get("MaxHotSpanSecs"),
            MaxMemMb=json_data.get("MaxMemMb"),
            MaxMetaEntries=json_data.get("MaxMetaEntries"),
            MaxTimeUnreplicatedNoAcks=json_data.get("MaxTimeUnreplicatedNoAcks"),
            MaxTimeUnreplicatedWithAcks=json_data.get("MaxTimeUnreplicatedWithAcks"),
            MaxTotalDataSizeMb=json_data.get("MaxTotalDataSizeMb"),
            MaxWarmDbCount=json_data.get("MaxWarmDbCount"),
            MinRawFileSyncSecs=json_data.get("MinRawFileSyncSecs"),
            MinStreamGroupQueueSize=json_data.get("MinStreamGroupQueueSize"),
            Name=json_data.get("Name"),
            PartialServiceMetaPeriod=json_data.get("PartialServiceMetaPeriod"),
            ProcessTrackerServiceInterval=json_data.get("ProcessTrackerServiceInterval"),
            QuarantineFutureSecs=json_data.get("QuarantineFutureSecs"),
            QuarantinePastSecs=json_data.get("QuarantinePastSecs"),
            RawChunkSizeBytes=json_data.get("RawChunkSizeBytes"),
            RepFactor=json_data.get("RepFactor"),
            RotatePeriodInSecs=json_data.get("RotatePeriodInSecs"),
            ServiceMetaPeriod=json_data.get("ServiceMetaPeriod"),
            SyncMeta=json_data.get("SyncMeta"),
            ThawedPath=json_data.get("ThawedPath"),
            ThrottleCheckPeriod=json_data.get("ThrottleCheckPeriod"),
            TstatsHomePath=json_data.get("TstatsHomePath"),
            WarmToColdScript=json_data.get("WarmToColdScript"),
            Acl=deserialize_list(json_data.get("Acl"), AclDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AclDefinition(BaseModel):
    App: Optional[str]
    CanChangePerms: Optional[bool]
    CanShareApp: Optional[bool]
    CanShareGlobal: Optional[bool]
    CanShareUser: Optional[bool]
    CanWrite: Optional[bool]
    Owner: Optional[str]
    Read: Optional[Sequence[str]]
    Removable: Optional[bool]
    Sharing: Optional[str]
    Write: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AclDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AclDefinition"]:
        if not json_data:
            return None
        return cls(
            App=json_data.get("App"),
            CanChangePerms=json_data.get("CanChangePerms"),
            CanShareApp=json_data.get("CanShareApp"),
            CanShareGlobal=json_data.get("CanShareGlobal"),
            CanShareUser=json_data.get("CanShareUser"),
            CanWrite=json_data.get("CanWrite"),
            Owner=json_data.get("Owner"),
            Read=json_data.get("Read"),
            Removable=json_data.get("Removable"),
            Sharing=json_data.get("Sharing"),
            Write=json_data.get("Write"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AclDefinition = AclDefinition


