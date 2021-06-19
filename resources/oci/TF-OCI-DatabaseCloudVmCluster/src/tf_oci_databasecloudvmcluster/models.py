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
    AvailabilityDomain: Optional[str]
    BackupNetworkNsgIds: Optional[Sequence[str]]
    BackupSubnetId: Optional[str]
    CloudExadataInfrastructureId: Optional[str]
    ClusterName: Optional[str]
    CompartmentId: Optional[str]
    CpuCoreCount: Optional[float]
    CreateAsync: Optional[bool]
    DataStoragePercentage: Optional[float]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    DiskRedundancy: Optional[str]
    DisplayName: Optional[str]
    Domain: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    GiVersion: Optional[str]
    Hostname: Optional[str]
    Id: Optional[str]
    IormConfigCache: Optional[Sequence["_IormConfigCacheDefinition2"]]
    IsLocalBackupEnabled: Optional[bool]
    IsSparseDiskgroupEnabled: Optional[bool]
    LastUpdateHistoryEntryId: Optional[str]
    LicenseModel: Optional[str]
    LifecycleDetails: Optional[str]
    ListenerPort: Optional[str]
    NodeCount: Optional[float]
    NsgIds: Optional[Sequence[str]]
    ScanDnsName: Optional[str]
    ScanDnsRecordId: Optional[str]
    ScanIpIds: Optional[Sequence[str]]
    Shape: Optional[str]
    SshPublicKeys: Optional[Sequence[str]]
    State: Optional[str]
    StorageSizeInGbs: Optional[float]
    SubnetId: Optional[str]
    SystemVersion: Optional[str]
    TimeCreated: Optional[str]
    TimeZone: Optional[str]
    VipIds: Optional[Sequence[str]]
    ZoneId: Optional[str]
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
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            BackupNetworkNsgIds=json_data.get("BackupNetworkNsgIds"),
            BackupSubnetId=json_data.get("BackupSubnetId"),
            CloudExadataInfrastructureId=json_data.get("CloudExadataInfrastructureId"),
            ClusterName=json_data.get("ClusterName"),
            CompartmentId=json_data.get("CompartmentId"),
            CpuCoreCount=json_data.get("CpuCoreCount"),
            CreateAsync=json_data.get("CreateAsync"),
            DataStoragePercentage=json_data.get("DataStoragePercentage"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            DiskRedundancy=json_data.get("DiskRedundancy"),
            DisplayName=json_data.get("DisplayName"),
            Domain=json_data.get("Domain"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            GiVersion=json_data.get("GiVersion"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            IormConfigCache=deserialize_list(json_data.get("IormConfigCache"), IormConfigCacheDefinition2),
            IsLocalBackupEnabled=json_data.get("IsLocalBackupEnabled"),
            IsSparseDiskgroupEnabled=json_data.get("IsSparseDiskgroupEnabled"),
            LastUpdateHistoryEntryId=json_data.get("LastUpdateHistoryEntryId"),
            LicenseModel=json_data.get("LicenseModel"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            ListenerPort=json_data.get("ListenerPort"),
            NodeCount=json_data.get("NodeCount"),
            NsgIds=json_data.get("NsgIds"),
            ScanDnsName=json_data.get("ScanDnsName"),
            ScanDnsRecordId=json_data.get("ScanDnsRecordId"),
            ScanIpIds=json_data.get("ScanIpIds"),
            Shape=json_data.get("Shape"),
            SshPublicKeys=json_data.get("SshPublicKeys"),
            State=json_data.get("State"),
            StorageSizeInGbs=json_data.get("StorageSizeInGbs"),
            SubnetId=json_data.get("SubnetId"),
            SystemVersion=json_data.get("SystemVersion"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeZone=json_data.get("TimeZone"),
            VipIds=json_data.get("VipIds"),
            ZoneId=json_data.get("ZoneId"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTagsDefinition = DefinedTagsDefinition


@dataclass
class FreeformTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTagsDefinition = FreeformTagsDefinition


@dataclass
class IormConfigCacheDefinition2(BaseModel):
    DbPlans: Optional[Sequence["_IormConfigCacheDefinition"]]
    LifecycleDetails: Optional[str]
    Objective: Optional[str]
    State: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IormConfigCacheDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IormConfigCacheDefinition2"]:
        if not json_data:
            return None
        return cls(
            DbPlans=deserialize_list(json_data.get("DbPlans"), IormConfigCacheDefinition),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            Objective=json_data.get("Objective"),
            State=json_data.get("State"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IormConfigCacheDefinition2 = IormConfigCacheDefinition2


@dataclass
class IormConfigCacheDefinition(BaseModel):
    DbName: Optional[str]
    FlashCacheLimit: Optional[str]
    Share: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IormConfigCacheDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IormConfigCacheDefinition"]:
        if not json_data:
            return None
        return cls(
            DbName=json_data.get("DbName"),
            FlashCacheLimit=json_data.get("FlashCacheLimit"),
            Share=json_data.get("Share"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IormConfigCacheDefinition = IormConfigCacheDefinition


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


