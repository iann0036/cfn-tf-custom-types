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
    Collation: Optional[str]
    CreateMode: Optional[str]
    CreationDate: Optional[str]
    DefaultSecondaryLocation: Optional[str]
    Edition: Optional[str]
    ElasticPoolName: Optional[str]
    Encryption: Optional[str]
    ExtendedAuditingPolicy: Optional[Sequence["_ExtendedAuditingPolicyDefinition"]]
    Id: Optional[str]
    Location: Optional[str]
    MaxSizeBytes: Optional[str]
    MaxSizeGb: Optional[str]
    Name: Optional[str]
    ReadScale: Optional[bool]
    RequestedServiceObjectiveId: Optional[str]
    RequestedServiceObjectiveName: Optional[str]
    ResourceGroupName: Optional[str]
    RestorePointInTime: Optional[str]
    ServerName: Optional[str]
    SourceDatabaseDeletionDate: Optional[str]
    SourceDatabaseId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    ZoneRedundant: Optional[bool]
    Import: Optional[Sequence["_ImportDefinition"]]
    ThreatDetectionPolicy: Optional[Sequence["_ThreatDetectionPolicyDefinition"]]
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
            Collation=json_data.get("Collation"),
            CreateMode=json_data.get("CreateMode"),
            CreationDate=json_data.get("CreationDate"),
            DefaultSecondaryLocation=json_data.get("DefaultSecondaryLocation"),
            Edition=json_data.get("Edition"),
            ElasticPoolName=json_data.get("ElasticPoolName"),
            Encryption=json_data.get("Encryption"),
            ExtendedAuditingPolicy=deserialize_list(json_data.get("ExtendedAuditingPolicy"), ExtendedAuditingPolicyDefinition),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            MaxSizeBytes=json_data.get("MaxSizeBytes"),
            MaxSizeGb=json_data.get("MaxSizeGb"),
            Name=json_data.get("Name"),
            ReadScale=json_data.get("ReadScale"),
            RequestedServiceObjectiveId=json_data.get("RequestedServiceObjectiveId"),
            RequestedServiceObjectiveName=json_data.get("RequestedServiceObjectiveName"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            RestorePointInTime=json_data.get("RestorePointInTime"),
            ServerName=json_data.get("ServerName"),
            SourceDatabaseDeletionDate=json_data.get("SourceDatabaseDeletionDate"),
            SourceDatabaseId=json_data.get("SourceDatabaseId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            ZoneRedundant=json_data.get("ZoneRedundant"),
            Import=deserialize_list(json_data.get("Import"), ImportDefinition),
            ThreatDetectionPolicy=deserialize_list(json_data.get("ThreatDetectionPolicy"), ThreatDetectionPolicyDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ExtendedAuditingPolicyDefinition(BaseModel):
    LogMonitoringEnabled: Optional[bool]
    RetentionInDays: Optional[float]
    StorageAccountAccessKey: Optional[str]
    StorageAccountAccessKeyIsSecondary: Optional[bool]
    StorageEndpoint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtendedAuditingPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtendedAuditingPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            LogMonitoringEnabled=json_data.get("LogMonitoringEnabled"),
            RetentionInDays=json_data.get("RetentionInDays"),
            StorageAccountAccessKey=json_data.get("StorageAccountAccessKey"),
            StorageAccountAccessKeyIsSecondary=json_data.get("StorageAccountAccessKeyIsSecondary"),
            StorageEndpoint=json_data.get("StorageEndpoint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtendedAuditingPolicyDefinition = ExtendedAuditingPolicyDefinition


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
class ImportDefinition(BaseModel):
    AdministratorLogin: Optional[str]
    AdministratorLoginPassword: Optional[str]
    AuthenticationType: Optional[str]
    OperationMode: Optional[str]
    StorageKey: Optional[str]
    StorageKeyType: Optional[str]
    StorageUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ImportDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImportDefinition"]:
        if not json_data:
            return None
        return cls(
            AdministratorLogin=json_data.get("AdministratorLogin"),
            AdministratorLoginPassword=json_data.get("AdministratorLoginPassword"),
            AuthenticationType=json_data.get("AuthenticationType"),
            OperationMode=json_data.get("OperationMode"),
            StorageKey=json_data.get("StorageKey"),
            StorageKeyType=json_data.get("StorageKeyType"),
            StorageUri=json_data.get("StorageUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImportDefinition = ImportDefinition


@dataclass
class ThreatDetectionPolicyDefinition(BaseModel):
    DisabledAlerts: Optional[Sequence[str]]
    EmailAccountAdmins: Optional[str]
    EmailAddresses: Optional[Sequence[str]]
    RetentionDays: Optional[float]
    State: Optional[str]
    StorageAccountAccessKey: Optional[str]
    StorageEndpoint: Optional[str]
    UseServerDefault: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ThreatDetectionPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThreatDetectionPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            DisabledAlerts=json_data.get("DisabledAlerts"),
            EmailAccountAdmins=json_data.get("EmailAccountAdmins"),
            EmailAddresses=json_data.get("EmailAddresses"),
            RetentionDays=json_data.get("RetentionDays"),
            State=json_data.get("State"),
            StorageAccountAccessKey=json_data.get("StorageAccountAccessKey"),
            StorageEndpoint=json_data.get("StorageEndpoint"),
            UseServerDefault=json_data.get("UseServerDefault"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThreatDetectionPolicyDefinition = ThreatDetectionPolicyDefinition


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


