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
    CharacterSet: Optional[str]
    CompartmentId: Optional[str]
    ConnectionStrings: Optional[Sequence["_ConnectionStrings"]]
    DbBackupConfig: Optional[Sequence["_DbBackupConfig"]]
    DbHomeId: Optional[str]
    DbName: Optional[str]
    DbSystemId: Optional[str]
    DbUniqueName: Optional[str]
    DbVersion: Optional[str]
    DbWorkload: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTags"]]
    FreeformTags: Optional[Sequence["_FreeformTags"]]
    LifecycleDetails: Optional[str]
    NcharacterSet: Optional[str]
    PdbName: Optional[str]
    Source: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    VmClusterId: Optional[str]
    Database: Optional[Sequence["_Database"]]
    Timeouts: Optional["_Timeouts"]
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
            CharacterSet=json_data.get("CharacterSet"),
            CompartmentId=json_data.get("CompartmentId"),
            ConnectionStrings=json_data.get("ConnectionStrings"),
            DbBackupConfig=json_data.get("DbBackupConfig"),
            DbHomeId=json_data.get("DbHomeId"),
            DbName=json_data.get("DbName"),
            DbSystemId=json_data.get("DbSystemId"),
            DbUniqueName=json_data.get("DbUniqueName"),
            DbVersion=json_data.get("DbVersion"),
            DbWorkload=json_data.get("DbWorkload"),
            DefinedTags=json_data.get("DefinedTags"),
            FreeformTags=json_data.get("FreeformTags"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            NcharacterSet=json_data.get("NcharacterSet"),
            PdbName=json_data.get("PdbName"),
            Source=json_data.get("Source"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            VmClusterId=json_data.get("VmClusterId"),
            Database=json_data.get("Database"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            BackupDestinationDetails=json_data.get("BackupDestinationDetails"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConnectionStrings:
    AllConnectionStrings: Optional[Sequence["_AllConnectionStrings"]]
    CdbDefault: Optional[str]
    CdbIpDefault: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionStrings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionStrings"]:
        if not json_data:
            return None
        return cls(
            AllConnectionStrings=json_data.get("AllConnectionStrings"),
            CdbDefault=json_data.get("CdbDefault"),
            CdbIpDefault=json_data.get("CdbIpDefault"),
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
class Database:
    AdminPassword: Optional[str]
    CharacterSet: Optional[str]
    DbName: Optional[str]
    DbUniqueName: Optional[str]
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
            CharacterSet=json_data.get("CharacterSet"),
            DbName=json_data.get("DbName"),
            DbUniqueName=json_data.get("DbUniqueName"),
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


