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
    AllowVersionUpgrade: Optional[bool]
    Arn: Optional[str]
    AutomatedSnapshotRetentionPeriod: Optional[float]
    AvailabilityZone: Optional[str]
    BucketName: Optional[str]
    ClusterIdentifier: Optional[str]
    ClusterParameterGroupName: Optional[str]
    ClusterPublicKey: Optional[str]
    ClusterRevisionNumber: Optional[str]
    ClusterSecurityGroups: Optional[Sequence[str]]
    ClusterSubnetGroupName: Optional[str]
    ClusterType: Optional[str]
    ClusterVersion: Optional[str]
    DatabaseName: Optional[str]
    DnsName: Optional[str]
    ElasticIp: Optional[str]
    EnableLogging: Optional[bool]
    Encrypted: Optional[bool]
    Endpoint: Optional[str]
    EnhancedVpcRouting: Optional[bool]
    FinalSnapshotIdentifier: Optional[str]
    IamRoles: Optional[Sequence[str]]
    KmsKeyId: Optional[str]
    MasterPassword: Optional[str]
    MasterUsername: Optional[str]
    NodeType: Optional[str]
    NumberOfNodes: Optional[float]
    OwnerAccount: Optional[str]
    Port: Optional[float]
    PreferredMaintenanceWindow: Optional[str]
    PubliclyAccessible: Optional[bool]
    S3KeyPrefix: Optional[str]
    SkipFinalSnapshot: Optional[bool]
    SnapshotClusterIdentifier: Optional[str]
    SnapshotIdentifier: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    VpcSecurityGroupIds: Optional[Sequence[str]]
    Logging: Optional[Sequence["_Logging"]]
    SnapshotCopy: Optional[Sequence["_SnapshotCopy"]]
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
            AllowVersionUpgrade=json_data.get("AllowVersionUpgrade"),
            Arn=json_data.get("Arn"),
            AutomatedSnapshotRetentionPeriod=json_data.get("AutomatedSnapshotRetentionPeriod"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            BucketName=json_data.get("BucketName"),
            ClusterIdentifier=json_data.get("ClusterIdentifier"),
            ClusterParameterGroupName=json_data.get("ClusterParameterGroupName"),
            ClusterPublicKey=json_data.get("ClusterPublicKey"),
            ClusterRevisionNumber=json_data.get("ClusterRevisionNumber"),
            ClusterSecurityGroups=json_data.get("ClusterSecurityGroups"),
            ClusterSubnetGroupName=json_data.get("ClusterSubnetGroupName"),
            ClusterType=json_data.get("ClusterType"),
            ClusterVersion=json_data.get("ClusterVersion"),
            DatabaseName=json_data.get("DatabaseName"),
            DnsName=json_data.get("DnsName"),
            ElasticIp=json_data.get("ElasticIp"),
            EnableLogging=json_data.get("EnableLogging"),
            Encrypted=json_data.get("Encrypted"),
            Endpoint=json_data.get("Endpoint"),
            EnhancedVpcRouting=json_data.get("EnhancedVpcRouting"),
            FinalSnapshotIdentifier=json_data.get("FinalSnapshotIdentifier"),
            IamRoles=json_data.get("IamRoles"),
            KmsKeyId=json_data.get("KmsKeyId"),
            MasterPassword=json_data.get("MasterPassword"),
            MasterUsername=json_data.get("MasterUsername"),
            NodeType=json_data.get("NodeType"),
            NumberOfNodes=json_data.get("NumberOfNodes"),
            OwnerAccount=json_data.get("OwnerAccount"),
            Port=json_data.get("Port"),
            PreferredMaintenanceWindow=json_data.get("PreferredMaintenanceWindow"),
            PubliclyAccessible=json_data.get("PubliclyAccessible"),
            S3KeyPrefix=json_data.get("S3KeyPrefix"),
            SkipFinalSnapshot=json_data.get("SkipFinalSnapshot"),
            SnapshotClusterIdentifier=json_data.get("SnapshotClusterIdentifier"),
            SnapshotIdentifier=json_data.get("SnapshotIdentifier"),
            Tags=json_data.get("Tags"),
            VpcSecurityGroupIds=json_data.get("VpcSecurityGroupIds"),
            Logging=json_data.get("Logging"),
            SnapshotCopy=json_data.get("SnapshotCopy"),
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
class Logging:
    BucketName: Optional[str]
    Enable: Optional[bool]
    S3KeyPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Logging"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Logging"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
            Enable=json_data.get("Enable"),
            S3KeyPrefix=json_data.get("S3KeyPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Logging = Logging


@dataclass
class SnapshotCopy:
    DestinationRegion: Optional[str]
    GrantName: Optional[str]
    RetentionPeriod: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SnapshotCopy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnapshotCopy"]:
        if not json_data:
            return None
        return cls(
            DestinationRegion=json_data.get("DestinationRegion"),
            GrantName=json_data.get("GrantName"),
            RetentionPeriod=json_data.get("RetentionPeriod"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnapshotCopy = SnapshotCopy


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


