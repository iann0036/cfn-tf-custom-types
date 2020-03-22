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
    AmiType: Optional[str]
    Arn: Optional[str]
    ClusterName: Optional[str]
    DiskSize: Optional[float]
    Id: Optional[str]
    InstanceTypes: Optional[Sequence[str]]
    Labels: Optional[Sequence["_Labels"]]
    NodeGroupName: Optional[str]
    NodeRoleArn: Optional[str]
    ReleaseVersion: Optional[str]
    Resources: Optional[Sequence["_Resources"]]
    Status: Optional[str]
    SubnetIds: Optional[Sequence[str]]
    Tags: Optional[Sequence["_Tags"]]
    Version: Optional[str]
    RemoteAccess: Optional[Sequence["_RemoteAccess"]]
    ScalingConfig: Optional[Sequence["_ScalingConfig"]]
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
            AmiType=json_data.get("AmiType"),
            Arn=json_data.get("Arn"),
            ClusterName=json_data.get("ClusterName"),
            DiskSize=json_data.get("DiskSize"),
            Id=json_data.get("Id"),
            InstanceTypes=json_data.get("InstanceTypes"),
            Labels=json_data.get("Labels"),
            NodeGroupName=json_data.get("NodeGroupName"),
            NodeRoleArn=json_data.get("NodeRoleArn"),
            ReleaseVersion=json_data.get("ReleaseVersion"),
            Resources=json_data.get("Resources"),
            Status=json_data.get("Status"),
            SubnetIds=json_data.get("SubnetIds"),
            Tags=json_data.get("Tags"),
            Version=json_data.get("Version"),
            RemoteAccess=json_data.get("RemoteAccess"),
            ScalingConfig=json_data.get("ScalingConfig"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Labels:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels = Labels


@dataclass
class Resources:
    AutoscalingGroups: Optional[Sequence["_AutoscalingGroups"]]
    RemoteAccessSecurityGroupId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Resources"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Resources"]:
        if not json_data:
            return None
        return cls(
            AutoscalingGroups=json_data.get("AutoscalingGroups"),
            RemoteAccessSecurityGroupId=json_data.get("RemoteAccessSecurityGroupId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Resources = Resources


@dataclass
class AutoscalingGroups:
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscalingGroups"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscalingGroups"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscalingGroups = AutoscalingGroups


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
class RemoteAccess:
    Ec2SshKey: Optional[str]
    SourceSecurityGroupIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RemoteAccess"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RemoteAccess"]:
        if not json_data:
            return None
        return cls(
            Ec2SshKey=json_data.get("Ec2SshKey"),
            SourceSecurityGroupIds=json_data.get("SourceSecurityGroupIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RemoteAccess = RemoteAccess


@dataclass
class ScalingConfig:
    DesiredSize: Optional[float]
    MaxSize: Optional[float]
    MinSize: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ScalingConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScalingConfig"]:
        if not json_data:
            return None
        return cls(
            DesiredSize=json_data.get("DesiredSize"),
            MaxSize=json_data.get("MaxSize"),
            MinSize=json_data.get("MinSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalingConfig = ScalingConfig


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


