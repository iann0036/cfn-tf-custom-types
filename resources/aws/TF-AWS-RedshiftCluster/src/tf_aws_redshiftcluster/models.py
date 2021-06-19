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
    AllowVersionUpgrade: Optional[bool]
    Arn: Optional[str]
    AutomatedSnapshotRetentionPeriod: Optional[float]
    AvailabilityZone: Optional[str]
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
    Encrypted: Optional[bool]
    Endpoint: Optional[str]
    EnhancedVpcRouting: Optional[bool]
    FinalSnapshotIdentifier: Optional[str]
    IamRoles: Optional[Sequence[str]]
    Id: Optional[str]
    KmsKeyId: Optional[str]
    MasterPassword: Optional[str]
    MasterUsername: Optional[str]
    NodeType: Optional[str]
    NumberOfNodes: Optional[float]
    OwnerAccount: Optional[str]
    Port: Optional[float]
    PreferredMaintenanceWindow: Optional[str]
    PubliclyAccessible: Optional[bool]
    SkipFinalSnapshot: Optional[bool]
    SnapshotClusterIdentifier: Optional[str]
    SnapshotIdentifier: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    VpcSecurityGroupIds: Optional[Sequence[str]]
    Logging: Optional[Sequence["_LoggingDefinition"]]
    SnapshotCopy: Optional[Sequence["_SnapshotCopyDefinition"]]
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
            AllowVersionUpgrade=json_data.get("AllowVersionUpgrade"),
            Arn=json_data.get("Arn"),
            AutomatedSnapshotRetentionPeriod=json_data.get("AutomatedSnapshotRetentionPeriod"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
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
            Encrypted=json_data.get("Encrypted"),
            Endpoint=json_data.get("Endpoint"),
            EnhancedVpcRouting=json_data.get("EnhancedVpcRouting"),
            FinalSnapshotIdentifier=json_data.get("FinalSnapshotIdentifier"),
            IamRoles=json_data.get("IamRoles"),
            Id=json_data.get("Id"),
            KmsKeyId=json_data.get("KmsKeyId"),
            MasterPassword=json_data.get("MasterPassword"),
            MasterUsername=json_data.get("MasterUsername"),
            NodeType=json_data.get("NodeType"),
            NumberOfNodes=json_data.get("NumberOfNodes"),
            OwnerAccount=json_data.get("OwnerAccount"),
            Port=json_data.get("Port"),
            PreferredMaintenanceWindow=json_data.get("PreferredMaintenanceWindow"),
            PubliclyAccessible=json_data.get("PubliclyAccessible"),
            SkipFinalSnapshot=json_data.get("SkipFinalSnapshot"),
            SnapshotClusterIdentifier=json_data.get("SnapshotClusterIdentifier"),
            SnapshotIdentifier=json_data.get("SnapshotIdentifier"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            VpcSecurityGroupIds=json_data.get("VpcSecurityGroupIds"),
            Logging=deserialize_list(json_data.get("Logging"), LoggingDefinition),
            SnapshotCopy=deserialize_list(json_data.get("SnapshotCopy"), SnapshotCopyDefinition),
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
class LoggingDefinition(BaseModel):
    BucketName: Optional[str]
    Enable: Optional[bool]
    S3KeyPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingDefinition"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
            Enable=json_data.get("Enable"),
            S3KeyPrefix=json_data.get("S3KeyPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingDefinition = LoggingDefinition


@dataclass
class SnapshotCopyDefinition(BaseModel):
    DestinationRegion: Optional[str]
    GrantName: Optional[str]
    RetentionPeriod: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SnapshotCopyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnapshotCopyDefinition"]:
        if not json_data:
            return None
        return cls(
            DestinationRegion=json_data.get("DestinationRegion"),
            GrantName=json_data.get("GrantName"),
            RetentionPeriod=json_data.get("RetentionPeriod"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnapshotCopyDefinition = SnapshotCopyDefinition


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


