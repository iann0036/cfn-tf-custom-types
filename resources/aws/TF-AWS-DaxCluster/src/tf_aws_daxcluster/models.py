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
    Arn: Optional[str]
    AvailabilityZones: Optional[Sequence[str]]
    ClusterAddress: Optional[str]
    ClusterName: Optional[str]
    ConfigurationEndpoint: Optional[str]
    Description: Optional[str]
    IamRoleArn: Optional[str]
    Id: Optional[str]
    MaintenanceWindow: Optional[str]
    NodeType: Optional[str]
    Nodes: Optional[Sequence["_NodesDefinition"]]
    NotificationTopicArn: Optional[str]
    ParameterGroupName: Optional[str]
    Port: Optional[float]
    ReplicationFactor: Optional[float]
    SecurityGroupIds: Optional[Sequence[str]]
    SubnetGroupName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    ServerSideEncryption: Optional[Sequence["_ServerSideEncryptionDefinition"]]
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
            Arn=json_data.get("Arn"),
            AvailabilityZones=json_data.get("AvailabilityZones"),
            ClusterAddress=json_data.get("ClusterAddress"),
            ClusterName=json_data.get("ClusterName"),
            ConfigurationEndpoint=json_data.get("ConfigurationEndpoint"),
            Description=json_data.get("Description"),
            IamRoleArn=json_data.get("IamRoleArn"),
            Id=json_data.get("Id"),
            MaintenanceWindow=json_data.get("MaintenanceWindow"),
            NodeType=json_data.get("NodeType"),
            Nodes=deserialize_list(json_data.get("Nodes"), NodesDefinition),
            NotificationTopicArn=json_data.get("NotificationTopicArn"),
            ParameterGroupName=json_data.get("ParameterGroupName"),
            Port=json_data.get("Port"),
            ReplicationFactor=json_data.get("ReplicationFactor"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SubnetGroupName=json_data.get("SubnetGroupName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            ServerSideEncryption=deserialize_list(json_data.get("ServerSideEncryption"), ServerSideEncryptionDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class NodesDefinition(BaseModel):
    Address: Optional[str]
    AvailabilityZone: Optional[str]
    Id: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NodesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodesDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            Id=json_data.get("Id"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodesDefinition = NodesDefinition


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
class ServerSideEncryptionDefinition(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ServerSideEncryptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerSideEncryptionDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerSideEncryptionDefinition = ServerSideEncryptionDefinition


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


