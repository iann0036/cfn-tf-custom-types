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
    Address: Optional[str]
    AllocatedStorage: Optional[float]
    AllowMajorVersionUpgrade: Optional[bool]
    ApplyImmediately: Optional[bool]
    Arn: Optional[str]
    AutoMinorVersionUpgrade: Optional[bool]
    AvailabilityZone: Optional[str]
    BackupRetentionPeriod: Optional[float]
    BackupWindow: Optional[str]
    CaCertIdentifier: Optional[str]
    CharacterSetName: Optional[str]
    CopyTagsToSnapshot: Optional[bool]
    DbSubnetGroupName: Optional[str]
    DeleteAutomatedBackups: Optional[bool]
    DeletionProtection: Optional[bool]
    Domain: Optional[str]
    DomainIamRoleName: Optional[str]
    EnabledCloudwatchLogsExports: Optional[Sequence[str]]
    Endpoint: Optional[str]
    Engine: Optional[str]
    EngineVersion: Optional[str]
    FinalSnapshotIdentifier: Optional[str]
    HostedZoneId: Optional[str]
    IamDatabaseAuthenticationEnabled: Optional[bool]
    Id: Optional[str]
    Identifier: Optional[str]
    IdentifierPrefix: Optional[str]
    InstanceClass: Optional[str]
    Iops: Optional[float]
    KmsKeyId: Optional[str]
    LicenseModel: Optional[str]
    MaintenanceWindow: Optional[str]
    MaxAllocatedStorage: Optional[float]
    MonitoringInterval: Optional[float]
    MonitoringRoleArn: Optional[str]
    MultiAz: Optional[bool]
    Name: Optional[str]
    OptionGroupName: Optional[str]
    ParameterGroupName: Optional[str]
    Password: Optional[str]
    PerformanceInsightsEnabled: Optional[bool]
    PerformanceInsightsKmsKeyId: Optional[str]
    PerformanceInsightsRetentionPeriod: Optional[float]
    Port: Optional[float]
    PubliclyAccessible: Optional[bool]
    Replicas: Optional[Sequence[str]]
    ReplicateSourceDb: Optional[str]
    ResourceId: Optional[str]
    SecurityGroupNames: Optional[Sequence[str]]
    SkipFinalSnapshot: Optional[bool]
    SnapshotIdentifier: Optional[str]
    Status: Optional[str]
    StorageEncrypted: Optional[bool]
    StorageType: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Timezone: Optional[str]
    Username: Optional[str]
    VpcSecurityGroupIds: Optional[Sequence[str]]
    S3Import: Optional[Sequence["_S3Import"]]
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
            Address=json_data.get("Address"),
            AllocatedStorage=json_data.get("AllocatedStorage"),
            AllowMajorVersionUpgrade=json_data.get("AllowMajorVersionUpgrade"),
            ApplyImmediately=json_data.get("ApplyImmediately"),
            Arn=json_data.get("Arn"),
            AutoMinorVersionUpgrade=json_data.get("AutoMinorVersionUpgrade"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            BackupRetentionPeriod=json_data.get("BackupRetentionPeriod"),
            BackupWindow=json_data.get("BackupWindow"),
            CaCertIdentifier=json_data.get("CaCertIdentifier"),
            CharacterSetName=json_data.get("CharacterSetName"),
            CopyTagsToSnapshot=json_data.get("CopyTagsToSnapshot"),
            DbSubnetGroupName=json_data.get("DbSubnetGroupName"),
            DeleteAutomatedBackups=json_data.get("DeleteAutomatedBackups"),
            DeletionProtection=json_data.get("DeletionProtection"),
            Domain=json_data.get("Domain"),
            DomainIamRoleName=json_data.get("DomainIamRoleName"),
            EnabledCloudwatchLogsExports=json_data.get("EnabledCloudwatchLogsExports"),
            Endpoint=json_data.get("Endpoint"),
            Engine=json_data.get("Engine"),
            EngineVersion=json_data.get("EngineVersion"),
            FinalSnapshotIdentifier=json_data.get("FinalSnapshotIdentifier"),
            HostedZoneId=json_data.get("HostedZoneId"),
            IamDatabaseAuthenticationEnabled=json_data.get("IamDatabaseAuthenticationEnabled"),
            Id=json_data.get("Id"),
            Identifier=json_data.get("Identifier"),
            IdentifierPrefix=json_data.get("IdentifierPrefix"),
            InstanceClass=json_data.get("InstanceClass"),
            Iops=json_data.get("Iops"),
            KmsKeyId=json_data.get("KmsKeyId"),
            LicenseModel=json_data.get("LicenseModel"),
            MaintenanceWindow=json_data.get("MaintenanceWindow"),
            MaxAllocatedStorage=json_data.get("MaxAllocatedStorage"),
            MonitoringInterval=json_data.get("MonitoringInterval"),
            MonitoringRoleArn=json_data.get("MonitoringRoleArn"),
            MultiAz=json_data.get("MultiAz"),
            Name=json_data.get("Name"),
            OptionGroupName=json_data.get("OptionGroupName"),
            ParameterGroupName=json_data.get("ParameterGroupName"),
            Password=json_data.get("Password"),
            PerformanceInsightsEnabled=json_data.get("PerformanceInsightsEnabled"),
            PerformanceInsightsKmsKeyId=json_data.get("PerformanceInsightsKmsKeyId"),
            PerformanceInsightsRetentionPeriod=json_data.get("PerformanceInsightsRetentionPeriod"),
            Port=json_data.get("Port"),
            PubliclyAccessible=json_data.get("PubliclyAccessible"),
            Replicas=json_data.get("Replicas"),
            ReplicateSourceDb=json_data.get("ReplicateSourceDb"),
            ResourceId=json_data.get("ResourceId"),
            SecurityGroupNames=json_data.get("SecurityGroupNames"),
            SkipFinalSnapshot=json_data.get("SkipFinalSnapshot"),
            SnapshotIdentifier=json_data.get("SnapshotIdentifier"),
            Status=json_data.get("Status"),
            StorageEncrypted=json_data.get("StorageEncrypted"),
            StorageType=json_data.get("StorageType"),
            Tags=json_data.get("Tags"),
            Timezone=json_data.get("Timezone"),
            Username=json_data.get("Username"),
            VpcSecurityGroupIds=json_data.get("VpcSecurityGroupIds"),
            S3Import=json_data.get("S3Import"),
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
class S3Import:
    BucketName: Optional[str]
    BucketPrefix: Optional[str]
    IngestionRole: Optional[str]
    SourceEngine: Optional[str]
    SourceEngineVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Import"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Import"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
            BucketPrefix=json_data.get("BucketPrefix"),
            IngestionRole=json_data.get("IngestionRole"),
            SourceEngine=json_data.get("SourceEngine"),
            SourceEngineVersion=json_data.get("SourceEngineVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Import = S3Import


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


