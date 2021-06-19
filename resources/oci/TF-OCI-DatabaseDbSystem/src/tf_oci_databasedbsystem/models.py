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
    ClusterName: Optional[str]
    CompartmentId: Optional[str]
    CpuCoreCount: Optional[float]
    DataStoragePercentage: Optional[float]
    DataStorageSizeInGb: Optional[float]
    DatabaseEdition: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    DiskRedundancy: Optional[str]
    DisplayName: Optional[str]
    Domain: Optional[str]
    FaultDomains: Optional[Sequence[str]]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Hostname: Optional[str]
    Id: Optional[str]
    IormConfigCache: Optional[Sequence["_IormConfigCacheDefinition2"]]
    KmsKeyId: Optional[str]
    KmsKeyVersionId: Optional[str]
    LastMaintenanceRunId: Optional[str]
    LastPatchHistoryEntryId: Optional[str]
    LicenseModel: Optional[str]
    LifecycleDetails: Optional[str]
    ListenerPort: Optional[float]
    MaintenanceWindow: Optional[Sequence["_MaintenanceWindowDefinition3"]]
    NextMaintenanceRunId: Optional[str]
    NodeCount: Optional[float]
    NsgIds: Optional[Sequence[str]]
    PointInTimeDataDiskCloneTimestamp: Optional[str]
    PrivateIp: Optional[str]
    RecoStorageSizeInGb: Optional[float]
    ScanDnsName: Optional[str]
    ScanDnsRecordId: Optional[str]
    ScanIpIds: Optional[Sequence[str]]
    Shape: Optional[str]
    Source: Optional[str]
    SourceDbSystemId: Optional[str]
    SparseDiskgroup: Optional[bool]
    SshPublicKeys: Optional[Sequence[str]]
    State: Optional[str]
    SubnetId: Optional[str]
    TimeCreated: Optional[str]
    TimeZone: Optional[str]
    Version: Optional[str]
    VipIds: Optional[Sequence[str]]
    ZoneId: Optional[str]
    DbHome: Optional[Sequence["_DbHomeDefinition"]]
    DbSystemOptions: Optional[Sequence["_DbSystemOptionsDefinition"]]
    MaintenanceWindowDetails: Optional[Sequence["_MaintenanceWindowDetailsDefinition"]]
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
            ClusterName=json_data.get("ClusterName"),
            CompartmentId=json_data.get("CompartmentId"),
            CpuCoreCount=json_data.get("CpuCoreCount"),
            DataStoragePercentage=json_data.get("DataStoragePercentage"),
            DataStorageSizeInGb=json_data.get("DataStorageSizeInGb"),
            DatabaseEdition=json_data.get("DatabaseEdition"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            DiskRedundancy=json_data.get("DiskRedundancy"),
            DisplayName=json_data.get("DisplayName"),
            Domain=json_data.get("Domain"),
            FaultDomains=json_data.get("FaultDomains"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            IormConfigCache=deserialize_list(json_data.get("IormConfigCache"), IormConfigCacheDefinition2),
            KmsKeyId=json_data.get("KmsKeyId"),
            KmsKeyVersionId=json_data.get("KmsKeyVersionId"),
            LastMaintenanceRunId=json_data.get("LastMaintenanceRunId"),
            LastPatchHistoryEntryId=json_data.get("LastPatchHistoryEntryId"),
            LicenseModel=json_data.get("LicenseModel"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            ListenerPort=json_data.get("ListenerPort"),
            MaintenanceWindow=deserialize_list(json_data.get("MaintenanceWindow"), MaintenanceWindowDefinition3),
            NextMaintenanceRunId=json_data.get("NextMaintenanceRunId"),
            NodeCount=json_data.get("NodeCount"),
            NsgIds=json_data.get("NsgIds"),
            PointInTimeDataDiskCloneTimestamp=json_data.get("PointInTimeDataDiskCloneTimestamp"),
            PrivateIp=json_data.get("PrivateIp"),
            RecoStorageSizeInGb=json_data.get("RecoStorageSizeInGb"),
            ScanDnsName=json_data.get("ScanDnsName"),
            ScanDnsRecordId=json_data.get("ScanDnsRecordId"),
            ScanIpIds=json_data.get("ScanIpIds"),
            Shape=json_data.get("Shape"),
            Source=json_data.get("Source"),
            SourceDbSystemId=json_data.get("SourceDbSystemId"),
            SparseDiskgroup=json_data.get("SparseDiskgroup"),
            SshPublicKeys=json_data.get("SshPublicKeys"),
            State=json_data.get("State"),
            SubnetId=json_data.get("SubnetId"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeZone=json_data.get("TimeZone"),
            Version=json_data.get("Version"),
            VipIds=json_data.get("VipIds"),
            ZoneId=json_data.get("ZoneId"),
            DbHome=deserialize_list(json_data.get("DbHome"), DbHomeDefinition),
            DbSystemOptions=deserialize_list(json_data.get("DbSystemOptions"), DbSystemOptionsDefinition),
            MaintenanceWindowDetails=deserialize_list(json_data.get("MaintenanceWindowDetails"), MaintenanceWindowDetailsDefinition),
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
    DbSystemId: Optional[str]
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
            DbSystemId=json_data.get("DbSystemId"),
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
class MaintenanceWindowDefinition3(BaseModel):
    DaysOfWeek: Optional[Sequence["_MaintenanceWindowDefinition"]]
    HoursOfDay: Optional[Sequence[float]]
    LeadTimeInWeeks: Optional[float]
    Months: Optional[Sequence["_MaintenanceWindowDefinition2"]]
    Preference: Optional[str]
    WeeksOfMonth: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_MaintenanceWindowDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaintenanceWindowDefinition3"]:
        if not json_data:
            return None
        return cls(
            DaysOfWeek=deserialize_list(json_data.get("DaysOfWeek"), MaintenanceWindowDefinition),
            HoursOfDay=json_data.get("HoursOfDay"),
            LeadTimeInWeeks=json_data.get("LeadTimeInWeeks"),
            Months=deserialize_list(json_data.get("Months"), MaintenanceWindowDefinition2),
            Preference=json_data.get("Preference"),
            WeeksOfMonth=json_data.get("WeeksOfMonth"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaintenanceWindowDefinition3 = MaintenanceWindowDefinition3


@dataclass
class MaintenanceWindowDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MaintenanceWindowDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaintenanceWindowDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaintenanceWindowDefinition = MaintenanceWindowDefinition


@dataclass
class MaintenanceWindowDefinition2(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MaintenanceWindowDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaintenanceWindowDefinition2"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaintenanceWindowDefinition2 = MaintenanceWindowDefinition2


@dataclass
class DbHomeDefinition(BaseModel):
    CreateAsync: Optional[bool]
    DatabaseSoftwareImageId: Optional[str]
    DbVersion: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition2"]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition2"]]
    Database: Optional[Sequence["_DatabaseDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DbHomeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DbHomeDefinition"]:
        if not json_data:
            return None
        return cls(
            CreateAsync=json_data.get("CreateAsync"),
            DatabaseSoftwareImageId=json_data.get("DatabaseSoftwareImageId"),
            DbVersion=json_data.get("DbVersion"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition2),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition2),
            Database=deserialize_list(json_data.get("Database"), DatabaseDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DbHomeDefinition = DbHomeDefinition


@dataclass
class DefinedTagsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTagsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTagsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTagsDefinition2 = DefinedTagsDefinition2


@dataclass
class FreeformTagsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTagsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTagsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTagsDefinition2 = FreeformTagsDefinition2


@dataclass
class DatabaseDefinition(BaseModel):
    AdminPassword: Optional[str]
    BackupId: Optional[str]
    BackupTdePassword: Optional[str]
    CharacterSet: Optional[str]
    DatabaseId: Optional[str]
    DatabaseSoftwareImageId: Optional[str]
    DbDomain: Optional[str]
    DbName: Optional[str]
    DbWorkload: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition3"]]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition3"]]
    NcharacterSet: Optional[str]
    PdbName: Optional[str]
    TdeWalletPassword: Optional[str]
    TimeStampForPointInTimeRecovery: Optional[str]
    DbBackupConfig: Optional[Sequence["_DbBackupConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DatabaseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatabaseDefinition"]:
        if not json_data:
            return None
        return cls(
            AdminPassword=json_data.get("AdminPassword"),
            BackupId=json_data.get("BackupId"),
            BackupTdePassword=json_data.get("BackupTdePassword"),
            CharacterSet=json_data.get("CharacterSet"),
            DatabaseId=json_data.get("DatabaseId"),
            DatabaseSoftwareImageId=json_data.get("DatabaseSoftwareImageId"),
            DbDomain=json_data.get("DbDomain"),
            DbName=json_data.get("DbName"),
            DbWorkload=json_data.get("DbWorkload"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition3),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition3),
            NcharacterSet=json_data.get("NcharacterSet"),
            PdbName=json_data.get("PdbName"),
            TdeWalletPassword=json_data.get("TdeWalletPassword"),
            TimeStampForPointInTimeRecovery=json_data.get("TimeStampForPointInTimeRecovery"),
            DbBackupConfig=deserialize_list(json_data.get("DbBackupConfig"), DbBackupConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatabaseDefinition = DatabaseDefinition


@dataclass
class DefinedTagsDefinition3(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTagsDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTagsDefinition3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTagsDefinition3 = DefinedTagsDefinition3


@dataclass
class FreeformTagsDefinition3(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTagsDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTagsDefinition3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTagsDefinition3 = FreeformTagsDefinition3


@dataclass
class DbBackupConfigDefinition(BaseModel):
    AutoBackupEnabled: Optional[bool]
    AutoBackupWindow: Optional[str]
    RecoveryWindowInDays: Optional[float]
    BackupDestinationDetails: Optional[Sequence["_BackupDestinationDetailsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DbBackupConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DbBackupConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoBackupEnabled=json_data.get("AutoBackupEnabled"),
            AutoBackupWindow=json_data.get("AutoBackupWindow"),
            RecoveryWindowInDays=json_data.get("RecoveryWindowInDays"),
            BackupDestinationDetails=deserialize_list(json_data.get("BackupDestinationDetails"), BackupDestinationDetailsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DbBackupConfigDefinition = DbBackupConfigDefinition


@dataclass
class BackupDestinationDetailsDefinition(BaseModel):
    Id: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BackupDestinationDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackupDestinationDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackupDestinationDetailsDefinition = BackupDestinationDetailsDefinition


@dataclass
class DbSystemOptionsDefinition(BaseModel):
    StorageManagement: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DbSystemOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DbSystemOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            StorageManagement=json_data.get("StorageManagement"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DbSystemOptionsDefinition = DbSystemOptionsDefinition


@dataclass
class MaintenanceWindowDetailsDefinition(BaseModel):
    HoursOfDay: Optional[Sequence[float]]
    LeadTimeInWeeks: Optional[float]
    Preference: Optional[str]
    WeeksOfMonth: Optional[Sequence[float]]
    DaysOfWeek: Optional[Sequence["_DaysOfWeekDefinition"]]
    Months: Optional[Sequence["_MonthsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MaintenanceWindowDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaintenanceWindowDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            HoursOfDay=json_data.get("HoursOfDay"),
            LeadTimeInWeeks=json_data.get("LeadTimeInWeeks"),
            Preference=json_data.get("Preference"),
            WeeksOfMonth=json_data.get("WeeksOfMonth"),
            DaysOfWeek=deserialize_list(json_data.get("DaysOfWeek"), DaysOfWeekDefinition),
            Months=deserialize_list(json_data.get("Months"), MonthsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaintenanceWindowDetailsDefinition = MaintenanceWindowDetailsDefinition


@dataclass
class DaysOfWeekDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DaysOfWeekDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DaysOfWeekDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DaysOfWeekDefinition = DaysOfWeekDefinition


@dataclass
class MonthsDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MonthsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MonthsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MonthsDefinition = MonthsDefinition


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


