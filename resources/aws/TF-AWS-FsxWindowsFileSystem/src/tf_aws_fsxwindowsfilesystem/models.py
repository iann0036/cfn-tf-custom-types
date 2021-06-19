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
    ActiveDirectoryId: Optional[str]
    Arn: Optional[str]
    AutomaticBackupRetentionDays: Optional[float]
    CopyTagsToBackups: Optional[bool]
    DailyAutomaticBackupStartTime: Optional[str]
    DeploymentType: Optional[str]
    DnsName: Optional[str]
    Id: Optional[str]
    KmsKeyId: Optional[str]
    NetworkInterfaceIds: Optional[Sequence[str]]
    OwnerId: Optional[str]
    PreferredFileServerIp: Optional[str]
    PreferredSubnetId: Optional[str]
    RemoteAdministrationEndpoint: Optional[str]
    SecurityGroupIds: Optional[Sequence[str]]
    SkipFinalBackup: Optional[bool]
    StorageCapacity: Optional[float]
    StorageType: Optional[str]
    SubnetIds: Optional[Sequence[str]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    ThroughputCapacity: Optional[float]
    VpcId: Optional[str]
    WeeklyMaintenanceStartTime: Optional[str]
    SelfManagedActiveDirectory: Optional[Sequence["_SelfManagedActiveDirectoryDefinition"]]
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
            ActiveDirectoryId=json_data.get("ActiveDirectoryId"),
            Arn=json_data.get("Arn"),
            AutomaticBackupRetentionDays=json_data.get("AutomaticBackupRetentionDays"),
            CopyTagsToBackups=json_data.get("CopyTagsToBackups"),
            DailyAutomaticBackupStartTime=json_data.get("DailyAutomaticBackupStartTime"),
            DeploymentType=json_data.get("DeploymentType"),
            DnsName=json_data.get("DnsName"),
            Id=json_data.get("Id"),
            KmsKeyId=json_data.get("KmsKeyId"),
            NetworkInterfaceIds=json_data.get("NetworkInterfaceIds"),
            OwnerId=json_data.get("OwnerId"),
            PreferredFileServerIp=json_data.get("PreferredFileServerIp"),
            PreferredSubnetId=json_data.get("PreferredSubnetId"),
            RemoteAdministrationEndpoint=json_data.get("RemoteAdministrationEndpoint"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SkipFinalBackup=json_data.get("SkipFinalBackup"),
            StorageCapacity=json_data.get("StorageCapacity"),
            StorageType=json_data.get("StorageType"),
            SubnetIds=json_data.get("SubnetIds"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            ThroughputCapacity=json_data.get("ThroughputCapacity"),
            VpcId=json_data.get("VpcId"),
            WeeklyMaintenanceStartTime=json_data.get("WeeklyMaintenanceStartTime"),
            SelfManagedActiveDirectory=deserialize_list(json_data.get("SelfManagedActiveDirectory"), SelfManagedActiveDirectoryDefinition),
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
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class SelfManagedActiveDirectoryDefinition(BaseModel):
    DnsIps: Optional[Sequence[str]]
    DomainName: Optional[str]
    FileSystemAdministratorsGroup: Optional[str]
    OrganizationalUnitDistinguishedName: Optional[str]
    Password: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SelfManagedActiveDirectoryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SelfManagedActiveDirectoryDefinition"]:
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
_SelfManagedActiveDirectoryDefinition = SelfManagedActiveDirectoryDefinition


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


