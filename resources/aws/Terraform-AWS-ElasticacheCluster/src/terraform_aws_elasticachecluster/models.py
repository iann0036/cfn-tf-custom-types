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
    AvailabilityZone: Optional[str]
    AvailabilityZones: Optional[Sequence[str]]
    AzMode: Optional[str]
    CacheNodes: Optional[Sequence["_CacheNodes"]]
    ClusterAddress: Optional[str]
    ClusterId: Optional[str]
    ConfigurationEndpoint: Optional[str]
    Engine: Optional[str]
    EngineVersion: Optional[str]
    MaintenanceWindow: Optional[str]
    NodeType: Optional[str]
    NotificationTopicArn: Optional[str]
    NumCacheNodes: Optional[float]
    ParameterGroupName: Optional[str]
    Port: Optional[float]
    PreferredAvailabilityZones: Optional[Sequence[str]]
    ReplicationGroupId: Optional[str]
    SecurityGroupIds: Optional[Sequence[str]]
    SecurityGroupNames: Optional[Sequence[str]]
    SnapshotArns: Optional[Sequence[str]]
    SnapshotName: Optional[str]
    SnapshotRetentionLimit: Optional[float]
    SnapshotWindow: Optional[str]
    SubnetGroupName: Optional[str]
    Tags: Optional[Sequence["_Tags"]]

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
            AvailabilityZone=json_data.get("AvailabilityZone"),
            AvailabilityZones=json_data.get("AvailabilityZones"),
            AzMode=json_data.get("AzMode"),
            CacheNodes=json_data.get("CacheNodes"),
            ClusterAddress=json_data.get("ClusterAddress"),
            ClusterId=json_data.get("ClusterId"),
            ConfigurationEndpoint=json_data.get("ConfigurationEndpoint"),
            Engine=json_data.get("Engine"),
            EngineVersion=json_data.get("EngineVersion"),
            MaintenanceWindow=json_data.get("MaintenanceWindow"),
            NodeType=json_data.get("NodeType"),
            NotificationTopicArn=json_data.get("NotificationTopicArn"),
            NumCacheNodes=json_data.get("NumCacheNodes"),
            ParameterGroupName=json_data.get("ParameterGroupName"),
            Port=json_data.get("Port"),
            PreferredAvailabilityZones=json_data.get("PreferredAvailabilityZones"),
            ReplicationGroupId=json_data.get("ReplicationGroupId"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SecurityGroupNames=json_data.get("SecurityGroupNames"),
            SnapshotArns=json_data.get("SnapshotArns"),
            SnapshotName=json_data.get("SnapshotName"),
            SnapshotRetentionLimit=json_data.get("SnapshotRetentionLimit"),
            SnapshotWindow=json_data.get("SnapshotWindow"),
            SubnetGroupName=json_data.get("SubnetGroupName"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CacheNodes:
    Address: Optional[str]
    AvailabilityZone: Optional[str]
    Id: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CacheNodes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CacheNodes"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            Id=json_data.get("Id"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CacheNodes = CacheNodes


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


