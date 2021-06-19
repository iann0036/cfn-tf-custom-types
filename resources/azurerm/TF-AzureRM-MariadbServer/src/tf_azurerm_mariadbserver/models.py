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
    AdministratorLoginPassword: Optional[str]
    AutoGrowEnabled: Optional[bool]
    BackupRetentionDays: Optional[float]
    CreateMode: Optional[str]
    CreationSourceServerId: Optional[str]
    Fqdn: Optional[str]
    GeoRedundantBackupEnabled: Optional[bool]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    PublicNetworkAccessEnabled: Optional[bool]
    ResourceGroupName: Optional[str]
    RestorePointInTime: Optional[str]
    SkuName: Optional[str]
    SslEnforcement: Optional[str]
    SslEnforcementEnabled: Optional[bool]
    StorageMb: Optional[float]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Version: Optional[str]
    StorageProfile: Optional[Sequence["_StorageProfileDefinition"]]
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
            AdministratorLoginPassword=json_data.get("AdministratorLoginPassword"),
            AutoGrowEnabled=json_data.get("AutoGrowEnabled"),
            BackupRetentionDays=json_data.get("BackupRetentionDays"),
            CreateMode=json_data.get("CreateMode"),
            CreationSourceServerId=json_data.get("CreationSourceServerId"),
            Fqdn=json_data.get("Fqdn"),
            GeoRedundantBackupEnabled=json_data.get("GeoRedundantBackupEnabled"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            PublicNetworkAccessEnabled=json_data.get("PublicNetworkAccessEnabled"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            RestorePointInTime=json_data.get("RestorePointInTime"),
            SkuName=json_data.get("SkuName"),
            SslEnforcement=json_data.get("SslEnforcement"),
            SslEnforcementEnabled=json_data.get("SslEnforcementEnabled"),
            StorageMb=json_data.get("StorageMb"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Version=json_data.get("Version"),
            StorageProfile=deserialize_list(json_data.get("StorageProfile"), StorageProfileDefinition),
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
class StorageProfileDefinition(BaseModel):
    AutoGrow: Optional[str]
    BackupRetentionDays: Optional[float]
    GeoRedundantBackup: Optional[str]
    StorageMb: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_StorageProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoGrow=json_data.get("AutoGrow"),
            BackupRetentionDays=json_data.get("BackupRetentionDays"),
            GeoRedundantBackup=json_data.get("GeoRedundantBackup"),
            StorageMb=json_data.get("StorageMb"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageProfileDefinition = StorageProfileDefinition


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


