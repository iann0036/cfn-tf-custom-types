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
    Nodes: Optional[Sequence["_Nodes"]]
    NotificationTopicArn: Optional[str]
    ParameterGroupName: Optional[str]
    Port: Optional[float]
    ReplicationFactor: Optional[float]
    SecurityGroupIds: Optional[Sequence[str]]
    SubnetGroupName: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    ServerSideEncryption: Optional[Sequence["_ServerSideEncryption"]]
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
            Nodes=json_data.get("Nodes"),
            NotificationTopicArn=json_data.get("NotificationTopicArn"),
            ParameterGroupName=json_data.get("ParameterGroupName"),
            Port=json_data.get("Port"),
            ReplicationFactor=json_data.get("ReplicationFactor"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SubnetGroupName=json_data.get("SubnetGroupName"),
            Tags=json_data.get("Tags"),
            ServerSideEncryption=json_data.get("ServerSideEncryption"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Nodes:
    Address: Optional[str]
    AvailabilityZone: Optional[str]
    Id: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Nodes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Nodes"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            Id=json_data.get("Id"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Nodes = Nodes


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
class ServerSideEncryption:
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ServerSideEncryption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerSideEncryption"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerSideEncryption = ServerSideEncryption


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


