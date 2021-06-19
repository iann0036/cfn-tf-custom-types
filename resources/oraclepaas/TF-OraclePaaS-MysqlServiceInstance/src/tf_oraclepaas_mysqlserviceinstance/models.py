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
    AvailabilityDomain: Optional[str]
    BackupDestination: Optional[str]
    BaseReleaseVersion: Optional[str]
    Description: Optional[str]
    EmUrl: Optional[str]
    Id: Optional[str]
    IpNetwork: Optional[str]
    MeteringFrequency: Optional[str]
    Name: Optional[str]
    NotificationEmail: Optional[str]
    Region: Optional[str]
    ReleaseVersion: Optional[str]
    ServiceVersion: Optional[str]
    Shape: Optional[str]
    SshPublicKey: Optional[str]
    Subnet: Optional[str]
    VmUser: Optional[str]
    Backups: Optional[Sequence["_BackupsDefinition"]]
    MysqlConfiguration: Optional[Sequence["_MysqlConfigurationDefinition"]]
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
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            BackupDestination=json_data.get("BackupDestination"),
            BaseReleaseVersion=json_data.get("BaseReleaseVersion"),
            Description=json_data.get("Description"),
            EmUrl=json_data.get("EmUrl"),
            Id=json_data.get("Id"),
            IpNetwork=json_data.get("IpNetwork"),
            MeteringFrequency=json_data.get("MeteringFrequency"),
            Name=json_data.get("Name"),
            NotificationEmail=json_data.get("NotificationEmail"),
            Region=json_data.get("Region"),
            ReleaseVersion=json_data.get("ReleaseVersion"),
            ServiceVersion=json_data.get("ServiceVersion"),
            Shape=json_data.get("Shape"),
            SshPublicKey=json_data.get("SshPublicKey"),
            Subnet=json_data.get("Subnet"),
            VmUser=json_data.get("VmUser"),
            Backups=deserialize_list(json_data.get("Backups"), BackupsDefinition),
            MysqlConfiguration=deserialize_list(json_data.get("MysqlConfiguration"), MysqlConfigurationDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BackupsDefinition(BaseModel):
    CloudStorageContainer: Optional[str]
    CloudStoragePassword: Optional[str]
    CloudStorageUsername: Optional[str]
    CreateIfMissing: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_BackupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackupsDefinition"]:
        if not json_data:
            return None
        return cls(
            CloudStorageContainer=json_data.get("CloudStorageContainer"),
            CloudStoragePassword=json_data.get("CloudStoragePassword"),
            CloudStorageUsername=json_data.get("CloudStorageUsername"),
            CreateIfMissing=json_data.get("CreateIfMissing"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackupsDefinition = BackupsDefinition


@dataclass
class MysqlConfigurationDefinition(BaseModel):
    DbName: Optional[str]
    DbStorage: Optional[float]
    MysqlCharset: Optional[str]
    MysqlCollation: Optional[str]
    MysqlPassword: Optional[str]
    MysqlPort: Optional[float]
    MysqlUsername: Optional[str]
    SnapshotName: Optional[str]
    SourceServiceName: Optional[str]
    EnterpriseMonitorConfiguration: Optional[Sequence["_EnterpriseMonitorConfigurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MysqlConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MysqlConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            DbName=json_data.get("DbName"),
            DbStorage=json_data.get("DbStorage"),
            MysqlCharset=json_data.get("MysqlCharset"),
            MysqlCollation=json_data.get("MysqlCollation"),
            MysqlPassword=json_data.get("MysqlPassword"),
            MysqlPort=json_data.get("MysqlPort"),
            MysqlUsername=json_data.get("MysqlUsername"),
            SnapshotName=json_data.get("SnapshotName"),
            SourceServiceName=json_data.get("SourceServiceName"),
            EnterpriseMonitorConfiguration=deserialize_list(json_data.get("EnterpriseMonitorConfiguration"), EnterpriseMonitorConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MysqlConfigurationDefinition = MysqlConfigurationDefinition


@dataclass
class EnterpriseMonitorConfigurationDefinition(BaseModel):
    EmAgentPassword: Optional[str]
    EmAgentUsername: Optional[str]
    EmPassword: Optional[str]
    EmPort: Optional[float]
    EmUsername: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnterpriseMonitorConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnterpriseMonitorConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            EmAgentPassword=json_data.get("EmAgentPassword"),
            EmAgentUsername=json_data.get("EmAgentUsername"),
            EmPassword=json_data.get("EmPassword"),
            EmPort=json_data.get("EmPort"),
            EmUsername=json_data.get("EmUsername"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnterpriseMonitorConfigurationDefinition = EnterpriseMonitorConfigurationDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


