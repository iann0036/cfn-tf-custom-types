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
    AtRestEncryptionEnabled: Optional[bool]
    AuthToken: Optional[str]
    AutoMinorVersionUpgrade: Optional[bool]
    AutomaticFailoverEnabled: Optional[bool]
    AvailabilityZones: Optional[Sequence[str]]
    ConfigurationEndpointAddress: Optional[str]
    Engine: Optional[str]
    EngineVersion: Optional[str]
    Id: Optional[str]
    KmsKeyId: Optional[str]
    MaintenanceWindow: Optional[str]
    MemberClusters: Optional[Sequence[str]]
    NodeType: Optional[str]
    NotificationTopicArn: Optional[str]
    NumberCacheClusters: Optional[float]
    ParameterGroupName: Optional[str]
    Port: Optional[float]
    PrimaryEndpointAddress: Optional[str]
    ReplicationGroupDescription: Optional[str]
    ReplicationGroupId: Optional[str]
    SecurityGroupIds: Optional[Sequence[str]]
    SecurityGroupNames: Optional[Sequence[str]]
    SnapshotArns: Optional[Sequence[str]]
    SnapshotName: Optional[str]
    SnapshotRetentionLimit: Optional[float]
    SnapshotWindow: Optional[str]
    SubnetGroupName: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    TransitEncryptionEnabled: Optional[bool]
    ClusterMode: Optional[Sequence["_ClusterMode"]]
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
            AtRestEncryptionEnabled=json_data.get("AtRestEncryptionEnabled"),
            AuthToken=json_data.get("AuthToken"),
            AutoMinorVersionUpgrade=json_data.get("AutoMinorVersionUpgrade"),
            AutomaticFailoverEnabled=json_data.get("AutomaticFailoverEnabled"),
            AvailabilityZones=json_data.get("AvailabilityZones"),
            ConfigurationEndpointAddress=json_data.get("ConfigurationEndpointAddress"),
            Engine=json_data.get("Engine"),
            EngineVersion=json_data.get("EngineVersion"),
            Id=json_data.get("Id"),
            KmsKeyId=json_data.get("KmsKeyId"),
            MaintenanceWindow=json_data.get("MaintenanceWindow"),
            MemberClusters=json_data.get("MemberClusters"),
            NodeType=json_data.get("NodeType"),
            NotificationTopicArn=json_data.get("NotificationTopicArn"),
            NumberCacheClusters=json_data.get("NumberCacheClusters"),
            ParameterGroupName=json_data.get("ParameterGroupName"),
            Port=json_data.get("Port"),
            PrimaryEndpointAddress=json_data.get("PrimaryEndpointAddress"),
            ReplicationGroupDescription=json_data.get("ReplicationGroupDescription"),
            ReplicationGroupId=json_data.get("ReplicationGroupId"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SecurityGroupNames=json_data.get("SecurityGroupNames"),
            SnapshotArns=json_data.get("SnapshotArns"),
            SnapshotName=json_data.get("SnapshotName"),
            SnapshotRetentionLimit=json_data.get("SnapshotRetentionLimit"),
            SnapshotWindow=json_data.get("SnapshotWindow"),
            SubnetGroupName=json_data.get("SubnetGroupName"),
            Tags=json_data.get("Tags"),
            TransitEncryptionEnabled=json_data.get("TransitEncryptionEnabled"),
            ClusterMode=json_data.get("ClusterMode"),
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
class ClusterMode:
    NumNodeGroups: Optional[float]
    ReplicasPerNodeGroup: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterMode"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterMode"]:
        if not json_data:
            return None
        return cls(
            NumNodeGroups=json_data.get("NumNodeGroups"),
            ReplicasPerNodeGroup=json_data.get("ReplicasPerNodeGroup"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterMode = ClusterMode


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


