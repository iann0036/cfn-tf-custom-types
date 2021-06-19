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
    AllSettings: Optional[Sequence["_AllSettingsDefinition"]]
    Application: Optional[str]
    Arn: Optional[str]
    AutoscalingGroups: Optional[Sequence[str]]
    Cname: Optional[str]
    CnamePrefix: Optional[str]
    Description: Optional[str]
    EndpointUrl: Optional[str]
    Id: Optional[str]
    Instances: Optional[Sequence[str]]
    LaunchConfigurations: Optional[Sequence[str]]
    LoadBalancers: Optional[Sequence[str]]
    Name: Optional[str]
    PlatformArn: Optional[str]
    PollInterval: Optional[str]
    Queues: Optional[Sequence[str]]
    SolutionStackName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    TemplateName: Optional[str]
    Tier: Optional[str]
    Triggers: Optional[Sequence[str]]
    VersionLabel: Optional[str]
    WaitForReadyTimeout: Optional[str]
    Setting: Optional[Sequence["_SettingDefinition"]]

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
            AllSettings=deserialize_list(json_data.get("AllSettings"), AllSettingsDefinition),
            Application=json_data.get("Application"),
            Arn=json_data.get("Arn"),
            AutoscalingGroups=json_data.get("AutoscalingGroups"),
            Cname=json_data.get("Cname"),
            CnamePrefix=json_data.get("CnamePrefix"),
            Description=json_data.get("Description"),
            EndpointUrl=json_data.get("EndpointUrl"),
            Id=json_data.get("Id"),
            Instances=json_data.get("Instances"),
            LaunchConfigurations=json_data.get("LaunchConfigurations"),
            LoadBalancers=json_data.get("LoadBalancers"),
            Name=json_data.get("Name"),
            PlatformArn=json_data.get("PlatformArn"),
            PollInterval=json_data.get("PollInterval"),
            Queues=json_data.get("Queues"),
            SolutionStackName=json_data.get("SolutionStackName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            TemplateName=json_data.get("TemplateName"),
            Tier=json_data.get("Tier"),
            Triggers=json_data.get("Triggers"),
            VersionLabel=json_data.get("VersionLabel"),
            WaitForReadyTimeout=json_data.get("WaitForReadyTimeout"),
            Setting=deserialize_list(json_data.get("Setting"), SettingDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AllSettingsDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Resource: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AllSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Resource=json_data.get("Resource"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllSettingsDefinition = AllSettingsDefinition


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
class SettingDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    Resource: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SettingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SettingDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            Resource=json_data.get("Resource"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SettingDefinition = SettingDefinition


