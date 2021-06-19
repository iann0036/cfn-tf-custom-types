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
    AmiType: Optional[str]
    Arn: Optional[str]
    CapacityType: Optional[str]
    ClusterName: Optional[str]
    DiskSize: Optional[float]
    ForceUpdateVersion: Optional[bool]
    Id: Optional[str]
    InstanceTypes: Optional[Sequence[str]]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    NodeGroupName: Optional[str]
    NodeGroupNamePrefix: Optional[str]
    NodeRoleArn: Optional[str]
    ReleaseVersion: Optional[str]
    Resources: Optional[Sequence["_ResourcesDefinition2"]]
    Status: Optional[str]
    SubnetIds: Optional[Sequence[str]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Version: Optional[str]
    LaunchTemplate: Optional[Sequence["_LaunchTemplateDefinition"]]
    RemoteAccess: Optional[Sequence["_RemoteAccessDefinition"]]
    ScalingConfig: Optional[Sequence["_ScalingConfigDefinition"]]
    Taint: Optional[Sequence["_TaintDefinition"]]
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
            AmiType=json_data.get("AmiType"),
            Arn=json_data.get("Arn"),
            CapacityType=json_data.get("CapacityType"),
            ClusterName=json_data.get("ClusterName"),
            DiskSize=json_data.get("DiskSize"),
            ForceUpdateVersion=json_data.get("ForceUpdateVersion"),
            Id=json_data.get("Id"),
            InstanceTypes=json_data.get("InstanceTypes"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            NodeGroupName=json_data.get("NodeGroupName"),
            NodeGroupNamePrefix=json_data.get("NodeGroupNamePrefix"),
            NodeRoleArn=json_data.get("NodeRoleArn"),
            ReleaseVersion=json_data.get("ReleaseVersion"),
            Resources=deserialize_list(json_data.get("Resources"), ResourcesDefinition2),
            Status=json_data.get("Status"),
            SubnetIds=json_data.get("SubnetIds"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Version=json_data.get("Version"),
            LaunchTemplate=deserialize_list(json_data.get("LaunchTemplate"), LaunchTemplateDefinition),
            RemoteAccess=deserialize_list(json_data.get("RemoteAccess"), RemoteAccessDefinition),
            ScalingConfig=deserialize_list(json_data.get("ScalingConfig"), ScalingConfigDefinition),
            Taint=deserialize_list(json_data.get("Taint"), TaintDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class ResourcesDefinition2(BaseModel):
    AutoscalingGroups: Optional[Sequence["_ResourcesDefinition"]]
    RemoteAccessSecurityGroupId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourcesDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourcesDefinition2"]:
        if not json_data:
            return None
        return cls(
            AutoscalingGroups=deserialize_list(json_data.get("AutoscalingGroups"), ResourcesDefinition),
            RemoteAccessSecurityGroupId=json_data.get("RemoteAccessSecurityGroupId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourcesDefinition2 = ResourcesDefinition2


@dataclass
class ResourcesDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourcesDefinition = ResourcesDefinition


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
class LaunchTemplateDefinition(BaseModel):
    Id: Optional[str]
    Name: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchTemplateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchTemplateDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchTemplateDefinition = LaunchTemplateDefinition


@dataclass
class RemoteAccessDefinition(BaseModel):
    Ec2SshKey: Optional[str]
    SourceSecurityGroupIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RemoteAccessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RemoteAccessDefinition"]:
        if not json_data:
            return None
        return cls(
            Ec2SshKey=json_data.get("Ec2SshKey"),
            SourceSecurityGroupIds=json_data.get("SourceSecurityGroupIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RemoteAccessDefinition = RemoteAccessDefinition


@dataclass
class ScalingConfigDefinition(BaseModel):
    DesiredSize: Optional[float]
    MaxSize: Optional[float]
    MinSize: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ScalingConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScalingConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            DesiredSize=json_data.get("DesiredSize"),
            MaxSize=json_data.get("MaxSize"),
            MinSize=json_data.get("MinSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalingConfigDefinition = ScalingConfigDefinition


@dataclass
class TaintDefinition(BaseModel):
    Effect: Optional[str]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TaintDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaintDefinition"]:
        if not json_data:
            return None
        return cls(
            Effect=json_data.get("Effect"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaintDefinition = TaintDefinition


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


