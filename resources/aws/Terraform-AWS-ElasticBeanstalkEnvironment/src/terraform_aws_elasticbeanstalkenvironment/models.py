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
    AllSettings: Optional[Sequence["_AllSettings"]]
    Application: Optional[str]
    Arn: Optional[str]
    AutoscalingGroups: Optional[Sequence[str]]
    Cname: Optional[str]
    CnamePrefix: Optional[str]
    Description: Optional[str]
    EndpointUrl: Optional[str]
    Instances: Optional[Sequence[str]]
    LaunchConfigurations: Optional[Sequence[str]]
    LoadBalancers: Optional[Sequence[str]]
    Name: Optional[str]
    PlatformArn: Optional[str]
    PollInterval: Optional[str]
    Queues: Optional[Sequence[str]]
    SolutionStackName: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    TemplateName: Optional[str]
    Tier: Optional[str]
    Triggers: Optional[Sequence[str]]
    VersionLabel: Optional[str]
    WaitForReadyTimeout: Optional[str]
    Setting: Optional[Sequence["_Setting"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AllSettings=json_data.get("AllSettings"),
            Application=json_data.get("Application"),
            Arn=json_data.get("Arn"),
            AutoscalingGroups=json_data.get("AutoscalingGroups"),
            Cname=json_data.get("Cname"),
            CnamePrefix=json_data.get("CnamePrefix"),
            Description=json_data.get("Description"),
            EndpointUrl=json_data.get("EndpointUrl"),
            Instances=json_data.get("Instances"),
            LaunchConfigurations=json_data.get("LaunchConfigurations"),
            LoadBalancers=json_data.get("LoadBalancers"),
            Name=json_data.get("Name"),
            PlatformArn=json_data.get("PlatformArn"),
            PollInterval=json_data.get("PollInterval"),
            Queues=json_data.get("Queues"),
            SolutionStackName=json_data.get("SolutionStackName"),
            Tags=json_data.get("Tags"),
            TemplateName=json_data.get("TemplateName"),
            Tier=json_data.get("Tier"),
            Triggers=json_data.get("Triggers"),
            VersionLabel=json_data.get("VersionLabel"),
            WaitForReadyTimeout=json_data.get("WaitForReadyTimeout"),
            Setting=json_data.get("Setting"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AllSettings:
    Name: Optional[str]
    Namespace: Optional[str]
    Resource: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AllSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllSettings"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Resource=json_data.get("Resource"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllSettings = AllSettings


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
class Setting:
    Name: Optional[str]
    Namespace: Optional[str]
    Resource: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Setting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Setting"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Resource=json_data.get("Resource"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Setting = Setting


