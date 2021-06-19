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
    BackupSizeInGbs: Optional[float]
    BackupType: Optional[str]
    CompartmentId: Optional[str]
    CreationType: Optional[str]
    DataStorageSizeInGb: Optional[float]
    DbSystemId: Optional[str]
    DbSystemSnapshot: Optional[Sequence["_DbSystemSnapshotDefinition8"]]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    Description: Optional[str]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    LifecycleDetails: Optional[str]
    MysqlVersion: Optional[str]
    RetentionInDays: Optional[float]
    ShapeName: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    TimeUpdated: Optional[str]
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
            BackupSizeInGbs=json_data.get("BackupSizeInGbs"),
            BackupType=json_data.get("BackupType"),
            CompartmentId=json_data.get("CompartmentId"),
            CreationType=json_data.get("CreationType"),
            DataStorageSizeInGb=json_data.get("DataStorageSizeInGb"),
            DbSystemId=json_data.get("DbSystemId"),
            DbSystemSnapshot=deserialize_list(json_data.get("DbSystemSnapshot"), DbSystemSnapshotDefinition8),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            MysqlVersion=json_data.get("MysqlVersion"),
            RetentionInDays=json_data.get("RetentionInDays"),
            ShapeName=json_data.get("ShapeName"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeUpdated=json_data.get("TimeUpdated"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DbSystemSnapshotDefinition8(BaseModel):
    AdminUsername: Optional[str]
    AvailabilityDomain: Optional[str]
    BackupPolicy: Optional[Sequence["_DbSystemSnapshotDefinition3"]]
    CompartmentId: Optional[str]
    ConfigurationId: Optional[str]
    DataStorageSizeInGb: Optional[float]
    DefinedTags: Optional[Sequence["_DbSystemSnapshotDefinition4"]]
    Description: Optional[str]
    DisplayName: Optional[str]
    Endpoints: Optional[Sequence["_DbSystemSnapshotDefinition5"]]
    FaultDomain: Optional[str]
    FreeformTags: Optional[Sequence["_DbSystemSnapshotDefinition6"]]
    HostnameLabel: Optional[str]
    Id: Optional[str]
    IpAddress: Optional[str]
    IsHighlyAvailable: Optional[bool]
    Maintenance: Optional[Sequence["_DbSystemSnapshotDefinition7"]]
    MysqlVersion: Optional[str]
    Port: Optional[float]
    PortX: Optional[float]
    ShapeName: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DbSystemSnapshotDefinition8"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DbSystemSnapshotDefinition8"]:
        if not json_data:
            return None
        return cls(
            AdminUsername=json_data.get("AdminUsername"),
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            BackupPolicy=deserialize_list(json_data.get("BackupPolicy"), DbSystemSnapshotDefinition3),
            CompartmentId=json_data.get("CompartmentId"),
            ConfigurationId=json_data.get("ConfigurationId"),
            DataStorageSizeInGb=json_data.get("DataStorageSizeInGb"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DbSystemSnapshotDefinition4),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Endpoints=deserialize_list(json_data.get("Endpoints"), DbSystemSnapshotDefinition5),
            FaultDomain=json_data.get("FaultDomain"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), DbSystemSnapshotDefinition6),
            HostnameLabel=json_data.get("HostnameLabel"),
            Id=json_data.get("Id"),
            IpAddress=json_data.get("IpAddress"),
            IsHighlyAvailable=json_data.get("IsHighlyAvailable"),
            Maintenance=deserialize_list(json_data.get("Maintenance"), DbSystemSnapshotDefinition7),
            MysqlVersion=json_data.get("MysqlVersion"),
            Port=json_data.get("Port"),
            PortX=json_data.get("PortX"),
            ShapeName=json_data.get("ShapeName"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DbSystemSnapshotDefinition8 = DbSystemSnapshotDefinition8


@dataclass
class DbSystemSnapshotDefinition3(BaseModel):
    DefinedTags: Optional[Sequence["_DbSystemSnapshotDefinition"]]
    FreeformTags: Optional[Sequence["_DbSystemSnapshotDefinition2"]]
    IsEnabled: Optional[bool]
    RetentionInDays: Optional[float]
    WindowStartTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DbSystemSnapshotDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DbSystemSnapshotDefinition3"]:
        if not json_data:
            return None
        return cls(
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DbSystemSnapshotDefinition),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), DbSystemSnapshotDefinition2),
            IsEnabled=json_data.get("IsEnabled"),
            RetentionInDays=json_data.get("RetentionInDays"),
            WindowStartTime=json_data.get("WindowStartTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DbSystemSnapshotDefinition3 = DbSystemSnapshotDefinition3


@dataclass
class DbSystemSnapshotDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DbSystemSnapshotDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DbSystemSnapshotDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DbSystemSnapshotDefinition = DbSystemSnapshotDefinition


@dataclass
class DbSystemSnapshotDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DbSystemSnapshotDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DbSystemSnapshotDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DbSystemSnapshotDefinition2 = DbSystemSnapshotDefinition2


@dataclass
class DbSystemSnapshotDefinition4(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DbSystemSnapshotDefinition4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DbSystemSnapshotDefinition4"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DbSystemSnapshotDefinition4 = DbSystemSnapshotDefinition4


@dataclass
class DbSystemSnapshotDefinition5(BaseModel):
    Hostname: Optional[str]
    IpAddress: Optional[str]
    Modes: Optional[Sequence[str]]
    Port: Optional[float]
    PortX: Optional[float]
    Status: Optional[str]
    StatusDetails: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DbSystemSnapshotDefinition5"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DbSystemSnapshotDefinition5"]:
        if not json_data:
            return None
        return cls(
            Hostname=json_data.get("Hostname"),
            IpAddress=json_data.get("IpAddress"),
            Modes=json_data.get("Modes"),
            Port=json_data.get("Port"),
            PortX=json_data.get("PortX"),
            Status=json_data.get("Status"),
            StatusDetails=json_data.get("StatusDetails"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DbSystemSnapshotDefinition5 = DbSystemSnapshotDefinition5


@dataclass
class DbSystemSnapshotDefinition6(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DbSystemSnapshotDefinition6"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DbSystemSnapshotDefinition6"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DbSystemSnapshotDefinition6 = DbSystemSnapshotDefinition6


@dataclass
class DbSystemSnapshotDefinition7(BaseModel):
    WindowStartTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DbSystemSnapshotDefinition7"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DbSystemSnapshotDefinition7"]:
        if not json_data:
            return None
        return cls(
            WindowStartTime=json_data.get("WindowStartTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DbSystemSnapshotDefinition7 = DbSystemSnapshotDefinition7


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


