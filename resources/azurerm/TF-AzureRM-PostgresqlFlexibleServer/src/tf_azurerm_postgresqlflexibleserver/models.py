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
    AdministratorLogin: Optional[str]
    AdministratorPassword: Optional[str]
    BackupRetentionDays: Optional[float]
    CmkEnabled: Optional[str]
    CreateMode: Optional[str]
    DelegatedSubnetId: Optional[str]
    Fqdn: Optional[str]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    PointInTimeRestoreTimeInUtc: Optional[str]
    PublicNetworkAccessEnabled: Optional[bool]
    ResourceGroupName: Optional[str]
    SkuName: Optional[str]
    SourceServerId: Optional[str]
    StorageMb: Optional[float]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Version: Optional[str]
    Zone: Optional[str]
    MaintenanceWindow: Optional[Sequence["_MaintenanceWindowDefinition"]]
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
            AdministratorLogin=json_data.get("AdministratorLogin"),
            AdministratorPassword=json_data.get("AdministratorPassword"),
            BackupRetentionDays=json_data.get("BackupRetentionDays"),
            CmkEnabled=json_data.get("CmkEnabled"),
            CreateMode=json_data.get("CreateMode"),
            DelegatedSubnetId=json_data.get("DelegatedSubnetId"),
            Fqdn=json_data.get("Fqdn"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            PointInTimeRestoreTimeInUtc=json_data.get("PointInTimeRestoreTimeInUtc"),
            PublicNetworkAccessEnabled=json_data.get("PublicNetworkAccessEnabled"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SkuName=json_data.get("SkuName"),
            SourceServerId=json_data.get("SourceServerId"),
            StorageMb=json_data.get("StorageMb"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Version=json_data.get("Version"),
            Zone=json_data.get("Zone"),
            MaintenanceWindow=deserialize_list(json_data.get("MaintenanceWindow"), MaintenanceWindowDefinition),
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
class MaintenanceWindowDefinition(BaseModel):
    DayOfWeek: Optional[float]
    StartHour: Optional[float]
    StartMinute: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MaintenanceWindowDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaintenanceWindowDefinition"]:
        if not json_data:
            return None
        return cls(
            DayOfWeek=json_data.get("DayOfWeek"),
            StartHour=json_data.get("StartHour"),
            StartMinute=json_data.get("StartMinute"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaintenanceWindowDefinition = MaintenanceWindowDefinition


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


