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
    Collation: Optional[str]
    CreateMode: Optional[str]
    CreationDate: Optional[str]
    DefaultSecondaryLocation: Optional[str]
    Edition: Optional[str]
    ElasticPoolName: Optional[str]
    Encryption: Optional[str]
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
    Tags: Optional[Sequence["_Tags"]]
    ZoneRedundant: Optional[bool]
    ExtendedAuditingPolicy: Optional[Sequence["_ExtendedAuditingPolicy"]]
    Import: Optional[Sequence["_Import"]]
    ThreatDetectionPolicy: Optional[Sequence["_ThreatDetectionPolicy"]]
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
            Collation=json_data.get("Collation"),
            CreateMode=json_data.get("CreateMode"),
            CreationDate=json_data.get("CreationDate"),
            DefaultSecondaryLocation=json_data.get("DefaultSecondaryLocation"),
            Edition=json_data.get("Edition"),
            ElasticPoolName=json_data.get("ElasticPoolName"),
            Encryption=json_data.get("Encryption"),
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
            Tags=json_data.get("Tags"),
            ZoneRedundant=json_data.get("ZoneRedundant"),
            ExtendedAuditingPolicy=json_data.get("ExtendedAuditingPolicy"),
            Import=json_data.get("Import"),
            ThreatDetectionPolicy=json_data.get("ThreatDetectionPolicy"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class ExtendedAuditingPolicy:
    RetentionInDays: Optional[float]
    StorageAccountAccessKey: Optional[str]
    StorageAccountAccessKeyIsSecondary: Optional[bool]
    StorageEndpoint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtendedAuditingPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtendedAuditingPolicy"]:
        if not json_data:
            return None
        return cls(
            RetentionInDays=json_data.get("RetentionInDays"),
            StorageAccountAccessKey=json_data.get("StorageAccountAccessKey"),
            StorageAccountAccessKeyIsSecondary=json_data.get("StorageAccountAccessKeyIsSecondary"),
            StorageEndpoint=json_data.get("StorageEndpoint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtendedAuditingPolicy = ExtendedAuditingPolicy


@dataclass
class Import:
    AdministratorLogin: Optional[str]
    AdministratorLoginPassword: Optional[str]
    AuthenticationType: Optional[str]
    OperationMode: Optional[str]
    StorageKey: Optional[str]
    StorageKeyType: Optional[str]
    StorageUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Import"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Import"]:
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
_Import = Import


@dataclass
class ThreatDetectionPolicy:
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
        cls: Type["_ThreatDetectionPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThreatDetectionPolicy"]:
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
_ThreatDetectionPolicy = ThreatDetectionPolicy


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


