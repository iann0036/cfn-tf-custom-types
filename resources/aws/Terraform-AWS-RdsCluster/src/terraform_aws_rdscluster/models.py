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
    ApplyImmediately: Optional[bool]
    Arn: Optional[str]
    AvailabilityZones: Optional[Sequence[str]]
    BacktrackWindow: Optional[float]
    BackupRetentionPeriod: Optional[float]
    ClusterIdentifier: Optional[str]
    ClusterIdentifierPrefix: Optional[str]
    ClusterMembers: Optional[Sequence[str]]
    ClusterResourceId: Optional[str]
    CopyTagsToSnapshot: Optional[bool]
    DatabaseName: Optional[str]
    DbClusterParameterGroupName: Optional[str]
    DbSubnetGroupName: Optional[str]
    DeletionProtection: Optional[bool]
    EnableHttpEndpoint: Optional[bool]
    EnabledCloudwatchLogsExports: Optional[Sequence[str]]
    Endpoint: Optional[str]
    Engine: Optional[str]
    EngineMode: Optional[str]
    EngineVersion: Optional[str]
    FinalSnapshotIdentifier: Optional[str]
    GlobalClusterIdentifier: Optional[str]
    HostedZoneId: Optional[str]
    IamDatabaseAuthenticationEnabled: Optional[bool]
    IamRoles: Optional[Sequence[str]]
    Id: Optional[str]
    KmsKeyId: Optional[str]
    MasterPassword: Optional[str]
    MasterUsername: Optional[str]
    Port: Optional[float]
    PreferredBackupWindow: Optional[str]
    PreferredMaintenanceWindow: Optional[str]
    ReaderEndpoint: Optional[str]
    ReplicationSourceIdentifier: Optional[str]
    SkipFinalSnapshot: Optional[bool]
    SnapshotIdentifier: Optional[str]
    SourceRegion: Optional[str]
    StorageEncrypted: Optional[bool]
    Tags: Optional[Sequence["_Tags"]]
    VpcSecurityGroupIds: Optional[Sequence[str]]
    S3Import: Optional[Sequence["_S3Import"]]
    ScalingConfiguration: Optional[Sequence["_ScalingConfiguration"]]
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
            ApplyImmediately=json_data.get("ApplyImmediately"),
            Arn=json_data.get("Arn"),
            AvailabilityZones=json_data.get("AvailabilityZones"),
            BacktrackWindow=json_data.get("BacktrackWindow"),
            BackupRetentionPeriod=json_data.get("BackupRetentionPeriod"),
            ClusterIdentifier=json_data.get("ClusterIdentifier"),
            ClusterIdentifierPrefix=json_data.get("ClusterIdentifierPrefix"),
            ClusterMembers=json_data.get("ClusterMembers"),
            ClusterResourceId=json_data.get("ClusterResourceId"),
            CopyTagsToSnapshot=json_data.get("CopyTagsToSnapshot"),
            DatabaseName=json_data.get("DatabaseName"),
            DbClusterParameterGroupName=json_data.get("DbClusterParameterGroupName"),
            DbSubnetGroupName=json_data.get("DbSubnetGroupName"),
            DeletionProtection=json_data.get("DeletionProtection"),
            EnableHttpEndpoint=json_data.get("EnableHttpEndpoint"),
            EnabledCloudwatchLogsExports=json_data.get("EnabledCloudwatchLogsExports"),
            Endpoint=json_data.get("Endpoint"),
            Engine=json_data.get("Engine"),
            EngineMode=json_data.get("EngineMode"),
            EngineVersion=json_data.get("EngineVersion"),
            FinalSnapshotIdentifier=json_data.get("FinalSnapshotIdentifier"),
            GlobalClusterIdentifier=json_data.get("GlobalClusterIdentifier"),
            HostedZoneId=json_data.get("HostedZoneId"),
            IamDatabaseAuthenticationEnabled=json_data.get("IamDatabaseAuthenticationEnabled"),
            IamRoles=json_data.get("IamRoles"),
            Id=json_data.get("Id"),
            KmsKeyId=json_data.get("KmsKeyId"),
            MasterPassword=json_data.get("MasterPassword"),
            MasterUsername=json_data.get("MasterUsername"),
            Port=json_data.get("Port"),
            PreferredBackupWindow=json_data.get("PreferredBackupWindow"),
            PreferredMaintenanceWindow=json_data.get("PreferredMaintenanceWindow"),
            ReaderEndpoint=json_data.get("ReaderEndpoint"),
            ReplicationSourceIdentifier=json_data.get("ReplicationSourceIdentifier"),
            SkipFinalSnapshot=json_data.get("SkipFinalSnapshot"),
            SnapshotIdentifier=json_data.get("SnapshotIdentifier"),
            SourceRegion=json_data.get("SourceRegion"),
            StorageEncrypted=json_data.get("StorageEncrypted"),
            Tags=json_data.get("Tags"),
            VpcSecurityGroupIds=json_data.get("VpcSecurityGroupIds"),
            S3Import=json_data.get("S3Import"),
            ScalingConfiguration=json_data.get("ScalingConfiguration"),
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
class ScalingConfiguration:
    AutoPause: Optional[bool]
    MaxCapacity: Optional[float]
    MinCapacity: Optional[float]
    SecondsUntilAutoPause: Optional[float]
    TimeoutAction: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScalingConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScalingConfiguration"]:
        if not json_data:
            return None
        return cls(
            AutoPause=json_data.get("AutoPause"),
            MaxCapacity=json_data.get("MaxCapacity"),
            MinCapacity=json_data.get("MinCapacity"),
            SecondsUntilAutoPause=json_data.get("SecondsUntilAutoPause"),
            TimeoutAction=json_data.get("TimeoutAction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalingConfiguration = ScalingConfiguration


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


