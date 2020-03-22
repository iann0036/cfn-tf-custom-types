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
    AdministratorLogin: Optional[str]
    AdministratorLoginPassword: Optional[str]
    Fqdn: Optional[str]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    SkuName: Optional[str]
    SslEnforcement: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Version: Optional[str]
    StorageProfile: Optional[Sequence["_StorageProfile"]]
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
            AdministratorLogin=json_data.get("AdministratorLogin"),
            AdministratorLoginPassword=json_data.get("AdministratorLoginPassword"),
            Fqdn=json_data.get("Fqdn"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SkuName=json_data.get("SkuName"),
            SslEnforcement=json_data.get("SslEnforcement"),
            Tags=json_data.get("Tags"),
            Version=json_data.get("Version"),
            StorageProfile=json_data.get("StorageProfile"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class StorageProfile:
    AutoGrow: Optional[str]
    BackupRetentionDays: Optional[float]
    GeoRedundantBackup: Optional[str]
    StorageMb: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_StorageProfile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageProfile"]:
        if not json_data:
            return None
        return cls(
            AutoGrow=json_data.get("AutoGrow"),
            BackupRetentionDays=json_data.get("BackupRetentionDays"),
            GeoRedundantBackup=json_data.get("GeoRedundantBackup"),
            StorageMb=json_data.get("StorageMb"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageProfile = StorageProfile


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


