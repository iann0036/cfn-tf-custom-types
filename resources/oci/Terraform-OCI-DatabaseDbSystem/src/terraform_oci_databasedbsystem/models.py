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
    AvailabilityDomain: Optional[str]
    BackupNetworkNsgIds: Optional[Sequence[str]]
    BackupSubnetId: Optional[str]
    ClusterName: Optional[str]
    CompartmentId: Optional[str]
    CpuCoreCount: Optional[float]
    DataStoragePercentage: Optional[float]
    DataStorageSizeInGb: Optional[float]
    DatabaseEdition: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTags"]]
    DiskRedundancy: Optional[str]
    DisplayName: Optional[str]
    Domain: Optional[str]
    FaultDomains: Optional[Sequence[str]]
    FreeformTags: Optional[Sequence["_FreeformTags"]]
    Hostname: Optional[str]
    IormConfigCache: Optional[Sequence["_IormConfigCache"]]
    LastPatchHistoryEntryId: Optional[str]
    LicenseModel: Optional[str]
    LifecycleDetails: Optional[str]
    ListenerPort: Optional[float]
    NodeCount: Optional[float]
    NsgIds: Optional[Sequence[str]]
    RecoStorageSizeInGb: Optional[float]
    ScanDnsRecordId: Optional[str]
    ScanIpIds: Optional[Sequence[str]]
    Shape: Optional[str]
    Source: Optional[str]
    SparseDiskgroup: Optional[bool]
    SshPublicKeys: Optional[Sequence[str]]
    State: Optional[str]
    SubnetId: Optional[str]
    TimeCreated: Optional[str]
    TimeZone: Optional[str]
    Version: Optional[str]
    VipIds: Optional[Sequence[str]]
    DbHome: Optional[Sequence["_DbHome"]]
    DbSystemOptions: Optional[Sequence["_DbSystemOptions"]]
    Timeouts: Optional["_Timeouts"]
    Database: Optional[Sequence["_Database"]]
    DbBackupConfig: Optional[Sequence["_DbBackupConfig"]]
    BackupDestinationDetails: Optional[Sequence["_BackupDestinationDetails"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
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
            DefinedTags=json_data.get("DefinedTags"),
            DiskRedundancy=json_data.get("DiskRedundancy"),
            DisplayName=json_data.get("DisplayName"),
            Domain=json_data.get("Domain"),
            FaultDomains=json_data.get("FaultDomains"),
            FreeformTags=json_data.get("FreeformTags"),
            Hostname=json_data.get("Hostname"),
            IormConfigCache=json_data.get("IormConfigCache"),
            LastPatchHistoryEntryId=json_data.get("LastPatchHistoryEntryId"),
            LicenseModel=json_data.get("LicenseModel"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            ListenerPort=json_data.get("ListenerPort"),
            NodeCount=json_data.get("NodeCount"),
            NsgIds=json_data.get("NsgIds"),
            RecoStorageSizeInGb=json_data.get("RecoStorageSizeInGb"),
            ScanDnsRecordId=json_data.get("ScanDnsRecordId"),
            ScanIpIds=json_data.get("ScanIpIds"),
            Shape=json_data.get("Shape"),
            Source=json_data.get("Source"),
            SparseDiskgroup=json_data.get("SparseDiskgroup"),
            SshPublicKeys=json_data.get("SshPublicKeys"),
            State=json_data.get("State"),
            SubnetId=json_data.get("SubnetId"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeZone=json_data.get("TimeZone"),
            Version=json_data.get("Version"),
            VipIds=json_data.get("VipIds"),
            DbHome=json_data.get("DbHome"),
            DbSystemOptions=json_data.get("DbSystemOptions"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Database=json_data.get("Database"),
            DbBackupConfig=json_data.get("DbBackupConfig"),
            BackupDestinationDetails=json_data.get("BackupDestinationDetails"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTags = DefinedTags


@dataclass
class FreeformTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTags = FreeformTags


@dataclass
class IormConfigCache:
    DbPlans: Optional[Sequence["_DbPlans"]]
    DbSystemId: Optional[str]
    LifecycleDetails: Optional[str]
    Objective: Optional[str]
    State: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IormConfigCache"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IormConfigCache"]:
        if not json_data:
            return None
        return cls(
            DbPlans=json_data.get("DbPlans"),
            DbSystemId=json_data.get("DbSystemId"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            Objective=json_data.get("Objective"),
            State=json_data.get("State"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IormConfigCache = IormConfigCache


@dataclass
class DbPlans:
    DbName: Optional[str]
    FlashCacheLimit: Optional[str]
    Share: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DbPlans"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DbPlans"]:
        if not json_data:
            return None
        return cls(
            DbName=json_data.get("DbName"),
            FlashCacheLimit=json_data.get("FlashCacheLimit"),
            Share=json_data.get("Share"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DbPlans = DbPlans


@dataclass
class DbHome:
    DbVersion: Optional[str]
    DisplayName: Optional[str]
    Database: Optional[Sequence["_Database"]]

    @classmethod
    def _deserialize(
        cls: Type["_DbHome"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DbHome"]:
        if not json_data:
            return None
        return cls(
            DbVersion=json_data.get("DbVersion"),
            DisplayName=json_data.get("DisplayName"),
            Database=json_data.get("Database"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DbHome = DbHome


@dataclass
class Database:
    AdminPassword: Optional[str]
    BackupId: Optional[str]
    BackupTdePassword: Optional[str]
    CharacterSet: Optional[str]
    DbName: Optional[str]
    DbWorkload: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTags2"]]
    FreeformTags: Optional[Sequence["_FreeformTags2"]]
    NcharacterSet: Optional[str]
    PdbName: Optional[str]
    DbBackupConfig: Optional[Sequence["_DbBackupConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_Database"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Database"]:
        if not json_data:
            return None
        return cls(
            AdminPassword=json_data.get("AdminPassword"),
            BackupId=json_data.get("BackupId"),
            BackupTdePassword=json_data.get("BackupTdePassword"),
            CharacterSet=json_data.get("CharacterSet"),
            DbName=json_data.get("DbName"),
            DbWorkload=json_data.get("DbWorkload"),
            DefinedTags=json_data.get("DefinedTags"),
            FreeformTags=json_data.get("FreeformTags"),
            NcharacterSet=json_data.get("NcharacterSet"),
            PdbName=json_data.get("PdbName"),
            DbBackupConfig=json_data.get("DbBackupConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Database = Database


@dataclass
class DefinedTags2:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTags2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTags2"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTags2 = DefinedTags2


@dataclass
class FreeformTags2:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTags2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTags2"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTags2 = FreeformTags2


@dataclass
class DbBackupConfig:
    AutoBackupEnabled: Optional[bool]
    AutoBackupWindow: Optional[str]
    RecoveryWindowInDays: Optional[float]
    BackupDestinationDetails: Optional[Sequence["_BackupDestinationDetails"]]

    @classmethod
    def _deserialize(
        cls: Type["_DbBackupConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DbBackupConfig"]:
        if not json_data:
            return None
        return cls(
            AutoBackupEnabled=json_data.get("AutoBackupEnabled"),
            AutoBackupWindow=json_data.get("AutoBackupWindow"),
            RecoveryWindowInDays=json_data.get("RecoveryWindowInDays"),
            BackupDestinationDetails=json_data.get("BackupDestinationDetails"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DbBackupConfig = DbBackupConfig


@dataclass
class BackupDestinationDetails:
    Id: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BackupDestinationDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackupDestinationDetails"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackupDestinationDetails = BackupDestinationDetails


@dataclass
class DbSystemOptions:
    StorageManagement: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DbSystemOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DbSystemOptions"]:
        if not json_data:
            return None
        return cls(
            StorageManagement=json_data.get("StorageManagement"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DbSystemOptions = DbSystemOptions


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


