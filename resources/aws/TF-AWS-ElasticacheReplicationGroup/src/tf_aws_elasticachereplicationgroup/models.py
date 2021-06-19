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
    ApplyImmediately: Optional[bool]
    Arn: Optional[str]
    AtRestEncryptionEnabled: Optional[bool]
    AuthToken: Optional[str]
    AutoMinorVersionUpgrade: Optional[bool]
    AutomaticFailoverEnabled: Optional[bool]
    AvailabilityZones: Optional[Sequence[str]]
    ClusterEnabled: Optional[bool]
    ConfigurationEndpointAddress: Optional[str]
    Engine: Optional[str]
    EngineVersion: Optional[str]
    EngineVersionActual: Optional[str]
    FinalSnapshotIdentifier: Optional[str]
    GlobalReplicationGroupId: Optional[str]
    Id: Optional[str]
    KmsKeyId: Optional[str]
    MaintenanceWindow: Optional[str]
    MemberClusters: Optional[Sequence[str]]
    MultiAzEnabled: Optional[bool]
    NodeType: Optional[str]
    NotificationTopicArn: Optional[str]
    NumberCacheClusters: Optional[float]
    ParameterGroupName: Optional[str]
    Port: Optional[float]
    PrimaryEndpointAddress: Optional[str]
    ReaderEndpointAddress: Optional[str]
    ReplicationGroupDescription: Optional[str]
    ReplicationGroupId: Optional[str]
    SecurityGroupIds: Optional[Sequence[str]]
    SecurityGroupNames: Optional[Sequence[str]]
    SnapshotArns: Optional[Sequence[str]]
    SnapshotName: Optional[str]
    SnapshotRetentionLimit: Optional[float]
    SnapshotWindow: Optional[str]
    SubnetGroupName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    TransitEncryptionEnabled: Optional[bool]
    ClusterMode: Optional[Sequence["_ClusterModeDefinition"]]
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
            ApplyImmediately=json_data.get("ApplyImmediately"),
            Arn=json_data.get("Arn"),
            AtRestEncryptionEnabled=json_data.get("AtRestEncryptionEnabled"),
            AuthToken=json_data.get("AuthToken"),
            AutoMinorVersionUpgrade=json_data.get("AutoMinorVersionUpgrade"),
            AutomaticFailoverEnabled=json_data.get("AutomaticFailoverEnabled"),
            AvailabilityZones=json_data.get("AvailabilityZones"),
            ClusterEnabled=json_data.get("ClusterEnabled"),
            ConfigurationEndpointAddress=json_data.get("ConfigurationEndpointAddress"),
            Engine=json_data.get("Engine"),
            EngineVersion=json_data.get("EngineVersion"),
            EngineVersionActual=json_data.get("EngineVersionActual"),
            FinalSnapshotIdentifier=json_data.get("FinalSnapshotIdentifier"),
            GlobalReplicationGroupId=json_data.get("GlobalReplicationGroupId"),
            Id=json_data.get("Id"),
            KmsKeyId=json_data.get("KmsKeyId"),
            MaintenanceWindow=json_data.get("MaintenanceWindow"),
            MemberClusters=json_data.get("MemberClusters"),
            MultiAzEnabled=json_data.get("MultiAzEnabled"),
            NodeType=json_data.get("NodeType"),
            NotificationTopicArn=json_data.get("NotificationTopicArn"),
            NumberCacheClusters=json_data.get("NumberCacheClusters"),
            ParameterGroupName=json_data.get("ParameterGroupName"),
            Port=json_data.get("Port"),
            PrimaryEndpointAddress=json_data.get("PrimaryEndpointAddress"),
            ReaderEndpointAddress=json_data.get("ReaderEndpointAddress"),
            ReplicationGroupDescription=json_data.get("ReplicationGroupDescription"),
            ReplicationGroupId=json_data.get("ReplicationGroupId"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SecurityGroupNames=json_data.get("SecurityGroupNames"),
            SnapshotArns=json_data.get("SnapshotArns"),
            SnapshotName=json_data.get("SnapshotName"),
            SnapshotRetentionLimit=json_data.get("SnapshotRetentionLimit"),
            SnapshotWindow=json_data.get("SnapshotWindow"),
            SubnetGroupName=json_data.get("SubnetGroupName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            TransitEncryptionEnabled=json_data.get("TransitEncryptionEnabled"),
            ClusterMode=deserialize_list(json_data.get("ClusterMode"), ClusterModeDefinition),
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
class ClusterModeDefinition(BaseModel):
    NumNodeGroups: Optional[float]
    ReplicasPerNodeGroup: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterModeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterModeDefinition"]:
        if not json_data:
            return None
        return cls(
            NumNodeGroups=json_data.get("NumNodeGroups"),
            ReplicasPerNodeGroup=json_data.get("ReplicasPerNodeGroup"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterModeDefinition = ClusterModeDefinition


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


