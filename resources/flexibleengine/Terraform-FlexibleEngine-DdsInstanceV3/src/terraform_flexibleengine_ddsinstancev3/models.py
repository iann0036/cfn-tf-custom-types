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
    AvailabilityZone: Optional[str]
    DbUsername: Optional[str]
    DiskEncryptionId: Optional[str]
    Id: Optional[str]
    Mode: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Region: Optional[str]
    SecurityGroupId: Optional[str]
    SubnetId: Optional[str]
    VpcId: Optional[str]
    BackupStrategy: Optional[Sequence["_BackupStrategy"]]
    Datastore: Optional[Sequence["_Datastore"]]
    Flavor: Optional[Sequence["_Flavor"]]
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
            AvailabilityZone=json_data.get("AvailabilityZone"),
            DbUsername=json_data.get("DbUsername"),
            DiskEncryptionId=json_data.get("DiskEncryptionId"),
            Id=json_data.get("Id"),
            Mode=json_data.get("Mode"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Region=json_data.get("Region"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            SubnetId=json_data.get("SubnetId"),
            VpcId=json_data.get("VpcId"),
            BackupStrategy=json_data.get("BackupStrategy"),
            Datastore=json_data.get("Datastore"),
            Flavor=json_data.get("Flavor"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BackupStrategy:
    KeepDays: Optional[float]
    StartTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BackupStrategy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackupStrategy"]:
        if not json_data:
            return None
        return cls(
            KeepDays=json_data.get("KeepDays"),
            StartTime=json_data.get("StartTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackupStrategy = BackupStrategy


@dataclass
class Datastore:
    StorageEngine: Optional[str]
    Type: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Datastore"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Datastore"]:
        if not json_data:
            return None
        return cls(
            StorageEngine=json_data.get("StorageEngine"),
            Type=json_data.get("Type"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Datastore = Datastore


@dataclass
class Flavor:
    Num: Optional[float]
    Size: Optional[float]
    SpecCode: Optional[str]
    Storage: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Flavor"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Flavor"]:
        if not json_data:
            return None
        return cls(
            Num=json_data.get("Num"),
            Size=json_data.get("Size"),
            SpecCode=json_data.get("SpecCode"),
            Storage=json_data.get("Storage"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Flavor = Flavor


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


