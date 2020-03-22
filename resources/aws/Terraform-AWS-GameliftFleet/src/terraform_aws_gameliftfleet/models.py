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
    Tags: Optional[Sequence["_Tags"]]
    Ec2InboundPermission: Optional[Sequence["_Ec2InboundPermission"]]
    ResourceCreationLimitPolicy: Optional[Sequence["_ResourceCreationLimitPolicy"]]
    RuntimeConfiguration: Optional[Sequence["_RuntimeConfiguration"]]
    Timeouts: Optional["_Timeouts"]
    ServerProcess: Optional[Sequence["_ServerProcess"]]

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
            Tags=json_data.get("Tags"),
            Ec2InboundPermission=json_data.get("Ec2InboundPermission"),
            ResourceCreationLimitPolicy=json_data.get("ResourceCreationLimitPolicy"),
            RuntimeConfiguration=json_data.get("RuntimeConfiguration"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            ServerProcess=json_data.get("ServerProcess"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class Ec2InboundPermission:
    FromPort: Optional[float]
    IpRange: Optional[str]
    Protocol: Optional[str]
    ToPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Ec2InboundPermission"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ec2InboundPermission"]:
        if not json_data:
            return None
        return cls(
            FromPort=json_data.get("FromPort"),
            IpRange=json_data.get("IpRange"),
            Protocol=json_data.get("Protocol"),
            ToPort=json_data.get("ToPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ec2InboundPermission = Ec2InboundPermission


@dataclass
class ResourceCreationLimitPolicy:
    NewGameSessionsPerCreator: Optional[float]
    PolicyPeriodInMinutes: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceCreationLimitPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceCreationLimitPolicy"]:
        if not json_data:
            return None
        return cls(
            NewGameSessionsPerCreator=json_data.get("NewGameSessionsPerCreator"),
            PolicyPeriodInMinutes=json_data.get("PolicyPeriodInMinutes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceCreationLimitPolicy = ResourceCreationLimitPolicy


@dataclass
class RuntimeConfiguration:
    GameSessionActivationTimeoutSeconds: Optional[float]
    MaxConcurrentGameSessionActivations: Optional[float]
    ServerProcess: Optional[Sequence["_ServerProcess"]]

    @classmethod
    def _deserialize(
        cls: Type["_RuntimeConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuntimeConfiguration"]:
        if not json_data:
            return None
        return cls(
            GameSessionActivationTimeoutSeconds=json_data.get("GameSessionActivationTimeoutSeconds"),
            MaxConcurrentGameSessionActivations=json_data.get("MaxConcurrentGameSessionActivations"),
            ServerProcess=json_data.get("ServerProcess"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuntimeConfiguration = RuntimeConfiguration


@dataclass
class ServerProcess:
    ConcurrentExecutions: Optional[float]
    LaunchPath: Optional[str]
    Parameters: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerProcess"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerProcess"]:
        if not json_data:
            return None
        return cls(
            ConcurrentExecutions=json_data.get("ConcurrentExecutions"),
            LaunchPath=json_data.get("LaunchPath"),
            Parameters=json_data.get("Parameters"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerProcess = ServerProcess


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


