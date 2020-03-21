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
    AdminPassword: Optional[str]
    AutonomousContainerDatabaseId: Optional[str]
    AutonomousDatabaseBackupId: Optional[str]
    AutonomousDatabaseId: Optional[str]
    CloneType: Optional[str]
    CompartmentId: Optional[str]
    ConnectionStrings: Optional[Sequence["_ConnectionStrings"]]
    ConnectionUrls: Optional[Sequence["_ConnectionUrls"]]
    CpuCoreCount: Optional[float]
    DataSafeStatus: Optional[str]
    DataStorageSizeInTbs: Optional[float]
    DbName: Optional[str]
    DbVersion: Optional[str]
    DbWorkload: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTags"]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTags"]]
    Id: Optional[str]
    IsAutoScalingEnabled: Optional[bool]
    IsDedicated: Optional[bool]
    IsFreeTier: Optional[bool]
    IsPreview: Optional[bool]
    IsPreviewVersionWithServiceTermsAccepted: Optional[bool]
    LicenseModel: Optional[str]
    LifecycleDetails: Optional[str]
    NsgIds: Optional[Sequence[str]]
    PrivateEndpoint: Optional[str]
    PrivateEndpointLabel: Optional[str]
    ServiceConsoleUrl: Optional[str]
    Source: Optional[str]
    SourceId: Optional[str]
    State: Optional[str]
    SubnetId: Optional[str]
    SystemTags: Optional[Sequence["_SystemTags"]]
    TimeCreated: Optional[str]
    TimeDeletionOfFreeAutonomousDatabase: Optional[str]
    TimeMaintenanceBegin: Optional[str]
    TimeMaintenanceEnd: Optional[str]
    TimeReclamationOfFreeAutonomousDatabase: Optional[str]
    Timestamp: Optional[str]
    UsedDataStorageSizeInTbs: Optional[float]
    WhitelistedIps: Optional[Sequence[str]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AdminPassword=json_data.get("AdminPassword"),
            AutonomousContainerDatabaseId=json_data.get("AutonomousContainerDatabaseId"),
            AutonomousDatabaseBackupId=json_data.get("AutonomousDatabaseBackupId"),
            AutonomousDatabaseId=json_data.get("AutonomousDatabaseId"),
            CloneType=json_data.get("CloneType"),
            CompartmentId=json_data.get("CompartmentId"),
            ConnectionStrings=json_data.get("ConnectionStrings"),
            ConnectionUrls=json_data.get("ConnectionUrls"),
            CpuCoreCount=json_data.get("CpuCoreCount"),
            DataSafeStatus=json_data.get("DataSafeStatus"),
            DataStorageSizeInTbs=json_data.get("DataStorageSizeInTbs"),
            DbName=json_data.get("DbName"),
            DbVersion=json_data.get("DbVersion"),
            DbWorkload=json_data.get("DbWorkload"),
            DefinedTags=json_data.get("DefinedTags"),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=json_data.get("FreeformTags"),
            Id=json_data.get("Id"),
            IsAutoScalingEnabled=json_data.get("IsAutoScalingEnabled"),
            IsDedicated=json_data.get("IsDedicated"),
            IsFreeTier=json_data.get("IsFreeTier"),
            IsPreview=json_data.get("IsPreview"),
            IsPreviewVersionWithServiceTermsAccepted=json_data.get("IsPreviewVersionWithServiceTermsAccepted"),
            LicenseModel=json_data.get("LicenseModel"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            NsgIds=json_data.get("NsgIds"),
            PrivateEndpoint=json_data.get("PrivateEndpoint"),
            PrivateEndpointLabel=json_data.get("PrivateEndpointLabel"),
            ServiceConsoleUrl=json_data.get("ServiceConsoleUrl"),
            Source=json_data.get("Source"),
            SourceId=json_data.get("SourceId"),
            State=json_data.get("State"),
            SubnetId=json_data.get("SubnetId"),
            SystemTags=json_data.get("SystemTags"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeDeletionOfFreeAutonomousDatabase=json_data.get("TimeDeletionOfFreeAutonomousDatabase"),
            TimeMaintenanceBegin=json_data.get("TimeMaintenanceBegin"),
            TimeMaintenanceEnd=json_data.get("TimeMaintenanceEnd"),
            TimeReclamationOfFreeAutonomousDatabase=json_data.get("TimeReclamationOfFreeAutonomousDatabase"),
            Timestamp=json_data.get("Timestamp"),
            UsedDataStorageSizeInTbs=json_data.get("UsedDataStorageSizeInTbs"),
            WhitelistedIps=json_data.get("WhitelistedIps"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConnectionStrings:
    AllConnectionStrings: Optional[Sequence["_AllConnectionStrings"]]
    Dedicated: Optional[str]
    High: Optional[str]
    Low: Optional[str]
    Medium: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionStrings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionStrings"]:
        if not json_data:
            return None
        return cls(
            AllConnectionStrings=json_data.get("AllConnectionStrings"),
            Dedicated=json_data.get("Dedicated"),
            High=json_data.get("High"),
            Low=json_data.get("Low"),
            Medium=json_data.get("Medium"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionStrings = ConnectionStrings


@dataclass
class AllConnectionStrings:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AllConnectionStrings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllConnectionStrings"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllConnectionStrings = AllConnectionStrings


@dataclass
class ConnectionUrls:
    ApexUrl: Optional[str]
    MachineLearningUserManagementUrl: Optional[str]
    SqlDevWebUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionUrls"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionUrls"]:
        if not json_data:
            return None
        return cls(
            ApexUrl=json_data.get("ApexUrl"),
            MachineLearningUserManagementUrl=json_data.get("MachineLearningUserManagementUrl"),
            SqlDevWebUrl=json_data.get("SqlDevWebUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionUrls = ConnectionUrls


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
class SystemTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SystemTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SystemTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SystemTags = SystemTags


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


