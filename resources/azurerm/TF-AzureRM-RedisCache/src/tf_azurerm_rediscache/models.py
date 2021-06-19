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
    Capacity: Optional[float]
    EnableNonSslPort: Optional[bool]
    Family: Optional[str]
    Hostname: Optional[str]
    Id: Optional[str]
    Location: Optional[str]
    MinimumTlsVersion: Optional[str]
    Name: Optional[str]
    Port: Optional[float]
    PrimaryAccessKey: Optional[str]
    PrimaryConnectionString: Optional[str]
    PrivateStaticIpAddress: Optional[str]
    PublicNetworkAccessEnabled: Optional[bool]
    ReplicasPerMaster: Optional[float]
    ResourceGroupName: Optional[str]
    SecondaryAccessKey: Optional[str]
    SecondaryConnectionString: Optional[str]
    ShardCount: Optional[float]
    SkuName: Optional[str]
    SslPort: Optional[float]
    SubnetId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Zones: Optional[Sequence[str]]
    PatchSchedule: Optional[Sequence["_PatchScheduleDefinition"]]
    RedisConfiguration: Optional[Sequence["_RedisConfigurationDefinition"]]
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
            Capacity=json_data.get("Capacity"),
            EnableNonSslPort=json_data.get("EnableNonSslPort"),
            Family=json_data.get("Family"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            MinimumTlsVersion=json_data.get("MinimumTlsVersion"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            PrimaryAccessKey=json_data.get("PrimaryAccessKey"),
            PrimaryConnectionString=json_data.get("PrimaryConnectionString"),
            PrivateStaticIpAddress=json_data.get("PrivateStaticIpAddress"),
            PublicNetworkAccessEnabled=json_data.get("PublicNetworkAccessEnabled"),
            ReplicasPerMaster=json_data.get("ReplicasPerMaster"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SecondaryAccessKey=json_data.get("SecondaryAccessKey"),
            SecondaryConnectionString=json_data.get("SecondaryConnectionString"),
            ShardCount=json_data.get("ShardCount"),
            SkuName=json_data.get("SkuName"),
            SslPort=json_data.get("SslPort"),
            SubnetId=json_data.get("SubnetId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Zones=json_data.get("Zones"),
            PatchSchedule=deserialize_list(json_data.get("PatchSchedule"), PatchScheduleDefinition),
            RedisConfiguration=deserialize_list(json_data.get("RedisConfiguration"), RedisConfigurationDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class PatchScheduleDefinition(BaseModel):
    DayOfWeek: Optional[str]
    StartHourUtc: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PatchScheduleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PatchScheduleDefinition"]:
        if not json_data:
            return None
        return cls(
            DayOfWeek=json_data.get("DayOfWeek"),
            StartHourUtc=json_data.get("StartHourUtc"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PatchScheduleDefinition = PatchScheduleDefinition


@dataclass
class RedisConfigurationDefinition(BaseModel):
    AofBackupEnabled: Optional[bool]
    AofStorageConnectionString0: Optional[str]
    AofStorageConnectionString1: Optional[str]
    EnableAuthentication: Optional[bool]
    MaxfragmentationmemoryReserved: Optional[float]
    MaxmemoryDelta: Optional[float]
    MaxmemoryPolicy: Optional[str]
    MaxmemoryReserved: Optional[float]
    NotifyKeyspaceEvents: Optional[str]
    RdbBackupEnabled: Optional[bool]
    RdbBackupFrequency: Optional[float]
    RdbBackupMaxSnapshotCount: Optional[float]
    RdbStorageConnectionString: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RedisConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedisConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            AofBackupEnabled=json_data.get("AofBackupEnabled"),
            AofStorageConnectionString0=json_data.get("AofStorageConnectionString0"),
            AofStorageConnectionString1=json_data.get("AofStorageConnectionString1"),
            EnableAuthentication=json_data.get("EnableAuthentication"),
            MaxfragmentationmemoryReserved=json_data.get("MaxfragmentationmemoryReserved"),
            MaxmemoryDelta=json_data.get("MaxmemoryDelta"),
            MaxmemoryPolicy=json_data.get("MaxmemoryPolicy"),
            MaxmemoryReserved=json_data.get("MaxmemoryReserved"),
            NotifyKeyspaceEvents=json_data.get("NotifyKeyspaceEvents"),
            RdbBackupEnabled=json_data.get("RdbBackupEnabled"),
            RdbBackupFrequency=json_data.get("RdbBackupFrequency"),
            RdbBackupMaxSnapshotCount=json_data.get("RdbBackupMaxSnapshotCount"),
            RdbStorageConnectionString=json_data.get("RdbStorageConnectionString"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedisConfigurationDefinition = RedisConfigurationDefinition


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


