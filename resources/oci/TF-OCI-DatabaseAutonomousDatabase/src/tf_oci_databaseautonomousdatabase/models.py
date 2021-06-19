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
    AdminPassword: Optional[str]
    ApexDetails: Optional[Sequence["_ApexDetailsDefinition"]]
    ArePrimaryWhitelistedIpsUsed: Optional[bool]
    AutonomousContainerDatabaseId: Optional[str]
    AutonomousDatabaseBackupId: Optional[str]
    AutonomousDatabaseId: Optional[str]
    AvailableUpgradeVersions: Optional[Sequence[str]]
    BackupConfig: Optional[Sequence["_BackupConfigDefinition"]]
    CloneType: Optional[str]
    CompartmentId: Optional[str]
    ConnectionStrings: Optional[Sequence["_ConnectionStringsDefinition2"]]
    ConnectionUrls: Optional[Sequence["_ConnectionUrlsDefinition"]]
    CpuCoreCount: Optional[float]
    DataSafeStatus: Optional[str]
    DataStorageSizeInGb: Optional[float]
    DataStorageSizeInTbs: Optional[float]
    DbName: Optional[str]
    DbVersion: Optional[str]
    DbWorkload: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    DisplayName: Optional[str]
    FailedDataRecoveryInSeconds: Optional[float]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    InfrastructureType: Optional[str]
    IsAccessControlEnabled: Optional[bool]
    IsAutoScalingEnabled: Optional[bool]
    IsDataGuardEnabled: Optional[bool]
    IsDedicated: Optional[bool]
    IsFreeTier: Optional[bool]
    IsPreview: Optional[bool]
    IsPreviewVersionWithServiceTermsAccepted: Optional[bool]
    IsRefreshableClone: Optional[bool]
    KeyHistoryEntry: Optional[Sequence["_KeyHistoryEntryDefinition"]]
    KeyStoreId: Optional[str]
    KeyStoreWalletName: Optional[str]
    KmsKeyId: Optional[str]
    KmsKeyLifecycleDetails: Optional[str]
    LicenseModel: Optional[str]
    LifecycleDetails: Optional[str]
    NsgIds: Optional[Sequence[str]]
    OpenMode: Optional[str]
    OperationsInsightsStatus: Optional[str]
    PermissionLevel: Optional[str]
    PrivateEndpoint: Optional[str]
    PrivateEndpointIp: Optional[str]
    PrivateEndpointLabel: Optional[str]
    RefreshableMode: Optional[str]
    RefreshableStatus: Optional[str]
    Role: Optional[str]
    RotateKeyTrigger: Optional[bool]
    ServiceConsoleUrl: Optional[str]
    Source: Optional[str]
    SourceId: Optional[str]
    StandbyDb: Optional[Sequence["_StandbyDbDefinition"]]
    StandbyWhitelistedIps: Optional[Sequence[str]]
    State: Optional[str]
    SubnetId: Optional[str]
    SwitchoverTo: Optional[str]
    SystemTags: Optional[Sequence["_SystemTagsDefinition"]]
    TimeCreated: Optional[str]
    TimeDeletionOfFreeAutonomousDatabase: Optional[str]
    TimeMaintenanceBegin: Optional[str]
    TimeMaintenanceEnd: Optional[str]
    TimeOfLastFailover: Optional[str]
    TimeOfLastRefresh: Optional[str]
    TimeOfLastRefreshPoint: Optional[str]
    TimeOfLastSwitchover: Optional[str]
    TimeOfNextRefresh: Optional[str]
    TimeReclamationOfFreeAutonomousDatabase: Optional[str]
    Timestamp: Optional[str]
    UsedDataStorageSizeInTbs: Optional[float]
    VaultId: Optional[str]
    WhitelistedIps: Optional[Sequence[str]]
    CustomerContacts: Optional[Sequence["_CustomerContactsDefinition"]]
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
            AdminPassword=json_data.get("AdminPassword"),
            ApexDetails=deserialize_list(json_data.get("ApexDetails"), ApexDetailsDefinition),
            ArePrimaryWhitelistedIpsUsed=json_data.get("ArePrimaryWhitelistedIpsUsed"),
            AutonomousContainerDatabaseId=json_data.get("AutonomousContainerDatabaseId"),
            AutonomousDatabaseBackupId=json_data.get("AutonomousDatabaseBackupId"),
            AutonomousDatabaseId=json_data.get("AutonomousDatabaseId"),
            AvailableUpgradeVersions=json_data.get("AvailableUpgradeVersions"),
            BackupConfig=deserialize_list(json_data.get("BackupConfig"), BackupConfigDefinition),
            CloneType=json_data.get("CloneType"),
            CompartmentId=json_data.get("CompartmentId"),
            ConnectionStrings=deserialize_list(json_data.get("ConnectionStrings"), ConnectionStringsDefinition2),
            ConnectionUrls=deserialize_list(json_data.get("ConnectionUrls"), ConnectionUrlsDefinition),
            CpuCoreCount=json_data.get("CpuCoreCount"),
            DataSafeStatus=json_data.get("DataSafeStatus"),
            DataStorageSizeInGb=json_data.get("DataStorageSizeInGb"),
            DataStorageSizeInTbs=json_data.get("DataStorageSizeInTbs"),
            DbName=json_data.get("DbName"),
            DbVersion=json_data.get("DbVersion"),
            DbWorkload=json_data.get("DbWorkload"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            DisplayName=json_data.get("DisplayName"),
            FailedDataRecoveryInSeconds=json_data.get("FailedDataRecoveryInSeconds"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            InfrastructureType=json_data.get("InfrastructureType"),
            IsAccessControlEnabled=json_data.get("IsAccessControlEnabled"),
            IsAutoScalingEnabled=json_data.get("IsAutoScalingEnabled"),
            IsDataGuardEnabled=json_data.get("IsDataGuardEnabled"),
            IsDedicated=json_data.get("IsDedicated"),
            IsFreeTier=json_data.get("IsFreeTier"),
            IsPreview=json_data.get("IsPreview"),
            IsPreviewVersionWithServiceTermsAccepted=json_data.get("IsPreviewVersionWithServiceTermsAccepted"),
            IsRefreshableClone=json_data.get("IsRefreshableClone"),
            KeyHistoryEntry=deserialize_list(json_data.get("KeyHistoryEntry"), KeyHistoryEntryDefinition),
            KeyStoreId=json_data.get("KeyStoreId"),
            KeyStoreWalletName=json_data.get("KeyStoreWalletName"),
            KmsKeyId=json_data.get("KmsKeyId"),
            KmsKeyLifecycleDetails=json_data.get("KmsKeyLifecycleDetails"),
            LicenseModel=json_data.get("LicenseModel"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            NsgIds=json_data.get("NsgIds"),
            OpenMode=json_data.get("OpenMode"),
            OperationsInsightsStatus=json_data.get("OperationsInsightsStatus"),
            PermissionLevel=json_data.get("PermissionLevel"),
            PrivateEndpoint=json_data.get("PrivateEndpoint"),
            PrivateEndpointIp=json_data.get("PrivateEndpointIp"),
            PrivateEndpointLabel=json_data.get("PrivateEndpointLabel"),
            RefreshableMode=json_data.get("RefreshableMode"),
            RefreshableStatus=json_data.get("RefreshableStatus"),
            Role=json_data.get("Role"),
            RotateKeyTrigger=json_data.get("RotateKeyTrigger"),
            ServiceConsoleUrl=json_data.get("ServiceConsoleUrl"),
            Source=json_data.get("Source"),
            SourceId=json_data.get("SourceId"),
            StandbyDb=deserialize_list(json_data.get("StandbyDb"), StandbyDbDefinition),
            StandbyWhitelistedIps=json_data.get("StandbyWhitelistedIps"),
            State=json_data.get("State"),
            SubnetId=json_data.get("SubnetId"),
            SwitchoverTo=json_data.get("SwitchoverTo"),
            SystemTags=deserialize_list(json_data.get("SystemTags"), SystemTagsDefinition),
            TimeCreated=json_data.get("TimeCreated"),
            TimeDeletionOfFreeAutonomousDatabase=json_data.get("TimeDeletionOfFreeAutonomousDatabase"),
            TimeMaintenanceBegin=json_data.get("TimeMaintenanceBegin"),
            TimeMaintenanceEnd=json_data.get("TimeMaintenanceEnd"),
            TimeOfLastFailover=json_data.get("TimeOfLastFailover"),
            TimeOfLastRefresh=json_data.get("TimeOfLastRefresh"),
            TimeOfLastRefreshPoint=json_data.get("TimeOfLastRefreshPoint"),
            TimeOfLastSwitchover=json_data.get("TimeOfLastSwitchover"),
            TimeOfNextRefresh=json_data.get("TimeOfNextRefresh"),
            TimeReclamationOfFreeAutonomousDatabase=json_data.get("TimeReclamationOfFreeAutonomousDatabase"),
            Timestamp=json_data.get("Timestamp"),
            UsedDataStorageSizeInTbs=json_data.get("UsedDataStorageSizeInTbs"),
            VaultId=json_data.get("VaultId"),
            WhitelistedIps=json_data.get("WhitelistedIps"),
            CustomerContacts=deserialize_list(json_data.get("CustomerContacts"), CustomerContactsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ApexDetailsDefinition(BaseModel):
    ApexVersion: Optional[str]
    OrdsVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApexDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApexDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            ApexVersion=json_data.get("ApexVersion"),
            OrdsVersion=json_data.get("OrdsVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApexDetailsDefinition = ApexDetailsDefinition


@dataclass
class BackupConfigDefinition(BaseModel):
    ManualBackupBucketName: Optional[str]
    ManualBackupType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BackupConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackupConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ManualBackupBucketName=json_data.get("ManualBackupBucketName"),
            ManualBackupType=json_data.get("ManualBackupType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackupConfigDefinition = BackupConfigDefinition


@dataclass
class ConnectionStringsDefinition2(BaseModel):
    AllConnectionStrings: Optional[Sequence["_ConnectionStringsDefinition"]]
    Dedicated: Optional[str]
    High: Optional[str]
    Low: Optional[str]
    Medium: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionStringsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionStringsDefinition2"]:
        if not json_data:
            return None
        return cls(
            AllConnectionStrings=deserialize_list(json_data.get("AllConnectionStrings"), ConnectionStringsDefinition),
            Dedicated=json_data.get("Dedicated"),
            High=json_data.get("High"),
            Low=json_data.get("Low"),
            Medium=json_data.get("Medium"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionStringsDefinition2 = ConnectionStringsDefinition2


@dataclass
class ConnectionStringsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionStringsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionStringsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionStringsDefinition = ConnectionStringsDefinition


@dataclass
class ConnectionUrlsDefinition(BaseModel):
    ApexUrl: Optional[str]
    GraphStudioUrl: Optional[str]
    MachineLearningUserManagementUrl: Optional[str]
    SqlDevWebUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionUrlsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionUrlsDefinition"]:
        if not json_data:
            return None
        return cls(
            ApexUrl=json_data.get("ApexUrl"),
            GraphStudioUrl=json_data.get("GraphStudioUrl"),
            MachineLearningUserManagementUrl=json_data.get("MachineLearningUserManagementUrl"),
            SqlDevWebUrl=json_data.get("SqlDevWebUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionUrlsDefinition = ConnectionUrlsDefinition


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
class KeyHistoryEntryDefinition(BaseModel):
    Id: Optional[str]
    TimeActivated: Optional[str]
    VaultId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KeyHistoryEntryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyHistoryEntryDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            TimeActivated=json_data.get("TimeActivated"),
            VaultId=json_data.get("VaultId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyHistoryEntryDefinition = KeyHistoryEntryDefinition


@dataclass
class StandbyDbDefinition(BaseModel):
    LagTimeInSeconds: Optional[float]
    LifecycleDetails: Optional[str]
    State: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StandbyDbDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StandbyDbDefinition"]:
        if not json_data:
            return None
        return cls(
            LagTimeInSeconds=json_data.get("LagTimeInSeconds"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            State=json_data.get("State"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StandbyDbDefinition = StandbyDbDefinition


@dataclass
class SystemTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SystemTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SystemTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SystemTagsDefinition = SystemTagsDefinition


@dataclass
class CustomerContactsDefinition(BaseModel):
    Email: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomerContactsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomerContactsDefinition"]:
        if not json_data:
            return None
        return cls(
            Email=json_data.get("Email"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomerContactsDefinition = CustomerContactsDefinition


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


