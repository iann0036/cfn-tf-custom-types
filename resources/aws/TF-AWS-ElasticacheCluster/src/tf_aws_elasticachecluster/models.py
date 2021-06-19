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
    AvailabilityZone: Optional[str]
    AzMode: Optional[str]
    CacheNodes: Optional[Sequence["_CacheNodesDefinition"]]
    ClusterAddress: Optional[str]
    ClusterId: Optional[str]
    ConfigurationEndpoint: Optional[str]
    Engine: Optional[str]
    EngineVersion: Optional[str]
    EngineVersionActual: Optional[str]
    FinalSnapshotIdentifier: Optional[str]
    Id: Optional[str]
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
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]

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
            AvailabilityZone=json_data.get("AvailabilityZone"),
            AzMode=json_data.get("AzMode"),
            CacheNodes=deserialize_list(json_data.get("CacheNodes"), CacheNodesDefinition),
            ClusterAddress=json_data.get("ClusterAddress"),
            ClusterId=json_data.get("ClusterId"),
            ConfigurationEndpoint=json_data.get("ConfigurationEndpoint"),
            Engine=json_data.get("Engine"),
            EngineVersion=json_data.get("EngineVersion"),
            EngineVersionActual=json_data.get("EngineVersionActual"),
            FinalSnapshotIdentifier=json_data.get("FinalSnapshotIdentifier"),
            Id=json_data.get("Id"),
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
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CacheNodesDefinition(BaseModel):
    Address: Optional[str]
    AvailabilityZone: Optional[str]
    Id: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CacheNodesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CacheNodesDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            Id=json_data.get("Id"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CacheNodesDefinition = CacheNodesDefinition


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


