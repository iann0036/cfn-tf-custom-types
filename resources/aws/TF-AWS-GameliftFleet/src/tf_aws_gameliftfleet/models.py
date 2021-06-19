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
    BuildId: Optional[str]
    Description: Optional[str]
    Ec2InstanceType: Optional[str]
    FleetType: Optional[str]
    Id: Optional[str]
    InstanceRoleArn: Optional[str]
    LogPaths: Optional[Sequence[str]]
    MetricGroups: Optional[Sequence[str]]
    Name: Optional[str]
    NewGameSessionProtectionPolicy: Optional[str]
    OperatingSystem: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Ec2InboundPermission: Optional[Sequence["_Ec2InboundPermissionDefinition"]]
    ResourceCreationLimitPolicy: Optional[Sequence["_ResourceCreationLimitPolicyDefinition"]]
    RuntimeConfiguration: Optional[Sequence["_RuntimeConfigurationDefinition"]]
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
            BuildId=json_data.get("BuildId"),
            Description=json_data.get("Description"),
            Ec2InstanceType=json_data.get("Ec2InstanceType"),
            FleetType=json_data.get("FleetType"),
            Id=json_data.get("Id"),
            InstanceRoleArn=json_data.get("InstanceRoleArn"),
            LogPaths=json_data.get("LogPaths"),
            MetricGroups=json_data.get("MetricGroups"),
            Name=json_data.get("Name"),
            NewGameSessionProtectionPolicy=json_data.get("NewGameSessionProtectionPolicy"),
            OperatingSystem=json_data.get("OperatingSystem"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Ec2InboundPermission=deserialize_list(json_data.get("Ec2InboundPermission"), Ec2InboundPermissionDefinition),
            ResourceCreationLimitPolicy=deserialize_list(json_data.get("ResourceCreationLimitPolicy"), ResourceCreationLimitPolicyDefinition),
            RuntimeConfiguration=deserialize_list(json_data.get("RuntimeConfiguration"), RuntimeConfigurationDefinition),
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
class Ec2InboundPermissionDefinition(BaseModel):
    FromPort: Optional[float]
    IpRange: Optional[str]
    Protocol: Optional[str]
    ToPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Ec2InboundPermissionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ec2InboundPermissionDefinition"]:
        if not json_data:
            return None
        return cls(
            FromPort=json_data.get("FromPort"),
            IpRange=json_data.get("IpRange"),
            Protocol=json_data.get("Protocol"),
            ToPort=json_data.get("ToPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ec2InboundPermissionDefinition = Ec2InboundPermissionDefinition


@dataclass
class ResourceCreationLimitPolicyDefinition(BaseModel):
    NewGameSessionsPerCreator: Optional[float]
    PolicyPeriodInMinutes: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceCreationLimitPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceCreationLimitPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            NewGameSessionsPerCreator=json_data.get("NewGameSessionsPerCreator"),
            PolicyPeriodInMinutes=json_data.get("PolicyPeriodInMinutes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceCreationLimitPolicyDefinition = ResourceCreationLimitPolicyDefinition


@dataclass
class RuntimeConfigurationDefinition(BaseModel):
    GameSessionActivationTimeoutSeconds: Optional[float]
    MaxConcurrentGameSessionActivations: Optional[float]
    ServerProcess: Optional[Sequence["_ServerProcessDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RuntimeConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuntimeConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            GameSessionActivationTimeoutSeconds=json_data.get("GameSessionActivationTimeoutSeconds"),
            MaxConcurrentGameSessionActivations=json_data.get("MaxConcurrentGameSessionActivations"),
            ServerProcess=deserialize_list(json_data.get("ServerProcess"), ServerProcessDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuntimeConfigurationDefinition = RuntimeConfigurationDefinition


@dataclass
class ServerProcessDefinition(BaseModel):
    ConcurrentExecutions: Optional[float]
    LaunchPath: Optional[str]
    Parameters: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerProcessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerProcessDefinition"]:
        if not json_data:
            return None
        return cls(
            ConcurrentExecutions=json_data.get("ConcurrentExecutions"),
            LaunchPath=json_data.get("LaunchPath"),
            Parameters=json_data.get("Parameters"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerProcessDefinition = ServerProcessDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


