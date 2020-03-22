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
    ActiveDirectoryId: Optional[str]
    Arn: Optional[str]
    AutomaticBackupRetentionDays: Optional[float]
    CopyTagsToBackups: Optional[bool]
    DailyAutomaticBackupStartTime: Optional[str]
    DnsName: Optional[str]
    Id: Optional[str]
    KmsKeyId: Optional[str]
    NetworkInterfaceIds: Optional[Sequence[str]]
    OwnerId: Optional[str]
    SecurityGroupIds: Optional[Sequence[str]]
    SkipFinalBackup: Optional[bool]
    StorageCapacity: Optional[float]
    SubnetIds: Optional[Sequence[str]]
    Tags: Optional[Sequence["_Tags"]]
    ThroughputCapacity: Optional[float]
    VpcId: Optional[str]
    WeeklyMaintenanceStartTime: Optional[str]
    SelfManagedActiveDirectory: Optional[Sequence["_SelfManagedActiveDirectory"]]
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
            ActiveDirectoryId=json_data.get("ActiveDirectoryId"),
            Arn=json_data.get("Arn"),
            AutomaticBackupRetentionDays=json_data.get("AutomaticBackupRetentionDays"),
            CopyTagsToBackups=json_data.get("CopyTagsToBackups"),
            DailyAutomaticBackupStartTime=json_data.get("DailyAutomaticBackupStartTime"),
            DnsName=json_data.get("DnsName"),
            Id=json_data.get("Id"),
            KmsKeyId=json_data.get("KmsKeyId"),
            NetworkInterfaceIds=json_data.get("NetworkInterfaceIds"),
            OwnerId=json_data.get("OwnerId"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SkipFinalBackup=json_data.get("SkipFinalBackup"),
            StorageCapacity=json_data.get("StorageCapacity"),
            SubnetIds=json_data.get("SubnetIds"),
            Tags=json_data.get("Tags"),
            ThroughputCapacity=json_data.get("ThroughputCapacity"),
            VpcId=json_data.get("VpcId"),
            WeeklyMaintenanceStartTime=json_data.get("WeeklyMaintenanceStartTime"),
            SelfManagedActiveDirectory=json_data.get("SelfManagedActiveDirectory"),
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
class SelfManagedActiveDirectory:
    DnsIps: Optional[Sequence[str]]
    DomainName: Optional[str]
    FileSystemAdministratorsGroup: Optional[str]
    OrganizationalUnitDistinguishedName: Optional[str]
    Password: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SelfManagedActiveDirectory"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SelfManagedActiveDirectory"]:
        if not json_data:
            return None
        return cls(
            DnsIps=json_data.get("DnsIps"),
            DomainName=json_data.get("DomainName"),
            FileSystemAdministratorsGroup=json_data.get("FileSystemAdministratorsGroup"),
            OrganizationalUnitDistinguishedName=json_data.get("OrganizationalUnitDistinguishedName"),
            Password=json_data.get("Password"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SelfManagedActiveDirectory = SelfManagedActiveDirectory


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


