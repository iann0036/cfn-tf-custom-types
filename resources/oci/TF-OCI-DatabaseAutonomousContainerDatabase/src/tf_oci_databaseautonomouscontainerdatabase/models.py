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
    AutonomousExadataInfrastructureId: Optional[str]
    AutonomousVmClusterId: Optional[str]
    AvailabilityDomain: Optional[str]
    CompartmentId: Optional[str]
    DbUniqueName: Optional[str]
    DbVersion: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    InfrastructureType: Optional[str]
    KeyStoreId: Optional[str]
    KeyStoreWalletName: Optional[str]
    KmsKeyId: Optional[str]
    LastMaintenanceRunId: Optional[str]
    LifecycleDetails: Optional[str]
    MaintenanceWindow: Optional[Sequence["_MaintenanceWindowDefinition3"]]
    NextMaintenanceRunId: Optional[str]
    PatchId: Optional[str]
    PatchModel: Optional[str]
    PeerAutonomousContainerDatabaseCompartmentId: Optional[str]
    PeerAutonomousContainerDatabaseDisplayName: Optional[str]
    PeerAutonomousExadataInfrastructureId: Optional[str]
    PeerAutonomousVmClusterId: Optional[str]
    PeerDbUniqueName: Optional[str]
    ProtectionMode: Optional[str]
    Role: Optional[str]
    RotateKeyTrigger: Optional[bool]
    ServiceLevelAgreementType: Optional[str]
    StandbyMaintenanceBufferInDays: Optional[float]
    State: Optional[str]
    TimeCreated: Optional[str]
    VaultId: Optional[str]
    BackupConfig: Optional[Sequence["_BackupConfigDefinition"]]
    MaintenanceWindowDetails: Optional[Sequence["_MaintenanceWindowDetailsDefinition"]]
    PeerAutonomousContainerDatabaseBackupConfig: Optional[Sequence["_PeerAutonomousContainerDatabaseBackupConfigDefinition"]]
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
            AutonomousExadataInfrastructureId=json_data.get("AutonomousExadataInfrastructureId"),
            AutonomousVmClusterId=json_data.get("AutonomousVmClusterId"),
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            CompartmentId=json_data.get("CompartmentId"),
            DbUniqueName=json_data.get("DbUniqueName"),
            DbVersion=json_data.get("DbVersion"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            InfrastructureType=json_data.get("InfrastructureType"),
            KeyStoreId=json_data.get("KeyStoreId"),
            KeyStoreWalletName=json_data.get("KeyStoreWalletName"),
            KmsKeyId=json_data.get("KmsKeyId"),
            LastMaintenanceRunId=json_data.get("LastMaintenanceRunId"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            MaintenanceWindow=deserialize_list(json_data.get("MaintenanceWindow"), MaintenanceWindowDefinition3),
            NextMaintenanceRunId=json_data.get("NextMaintenanceRunId"),
            PatchId=json_data.get("PatchId"),
            PatchModel=json_data.get("PatchModel"),
            PeerAutonomousContainerDatabaseCompartmentId=json_data.get("PeerAutonomousContainerDatabaseCompartmentId"),
            PeerAutonomousContainerDatabaseDisplayName=json_data.get("PeerAutonomousContainerDatabaseDisplayName"),
            PeerAutonomousExadataInfrastructureId=json_data.get("PeerAutonomousExadataInfrastructureId"),
            PeerAutonomousVmClusterId=json_data.get("PeerAutonomousVmClusterId"),
            PeerDbUniqueName=json_data.get("PeerDbUniqueName"),
            ProtectionMode=json_data.get("ProtectionMode"),
            Role=json_data.get("Role"),
            RotateKeyTrigger=json_data.get("RotateKeyTrigger"),
            ServiceLevelAgreementType=json_data.get("ServiceLevelAgreementType"),
            StandbyMaintenanceBufferInDays=json_data.get("StandbyMaintenanceBufferInDays"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            VaultId=json_data.get("VaultId"),
            BackupConfig=deserialize_list(json_data.get("BackupConfig"), BackupConfigDefinition),
            MaintenanceWindowDetails=deserialize_list(json_data.get("MaintenanceWindowDetails"), MaintenanceWindowDetailsDefinition),
            PeerAutonomousContainerDatabaseBackupConfig=deserialize_list(json_data.get("PeerAutonomousContainerDatabaseBackupConfig"), PeerAutonomousContainerDatabaseBackupConfigDefinition),
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
class BackupConfigDefinition(BaseModel):
    RecoveryWindowInDays: Optional[float]
    BackupDestinationDetails: Optional[Sequence["_BackupDestinationDetailsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BackupConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackupConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            RecoveryWindowInDays=json_data.get("RecoveryWindowInDays"),
            BackupDestinationDetails=deserialize_list(json_data.get("BackupDestinationDetails"), BackupDestinationDetailsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackupConfigDefinition = BackupConfigDefinition


@dataclass
class BackupDestinationDetailsDefinition(BaseModel):
    Id: Optional[str]
    InternetProxy: Optional[str]
    Type: Optional[str]
    VpcPassword: Optional[str]
    VpcUser: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BackupDestinationDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackupDestinationDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            InternetProxy=json_data.get("InternetProxy"),
            Type=json_data.get("Type"),
            VpcPassword=json_data.get("VpcPassword"),
            VpcUser=json_data.get("VpcUser"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackupDestinationDetailsDefinition = BackupDestinationDetailsDefinition


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
class PeerAutonomousContainerDatabaseBackupConfigDefinition(BaseModel):
    RecoveryWindowInDays: Optional[float]
    BackupDestinationDetails: Optional[Sequence["_BackupDestinationDetailsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PeerAutonomousContainerDatabaseBackupConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PeerAutonomousContainerDatabaseBackupConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            RecoveryWindowInDays=json_data.get("RecoveryWindowInDays"),
            BackupDestinationDetails=deserialize_list(json_data.get("BackupDestinationDetails"), BackupDestinationDetailsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PeerAutonomousContainerDatabaseBackupConfigDefinition = PeerAutonomousContainerDatabaseBackupConfigDefinition


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


