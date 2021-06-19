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
    AccessToken: Optional[str]
    Arn: Optional[str]
    AutoBranchCreationPatterns: Optional[Sequence[str]]
    BasicAuthCredentials: Optional[str]
    BuildSpec: Optional[str]
    DefaultDomain: Optional[str]
    Description: Optional[str]
    EnableAutoBranchCreation: Optional[bool]
    EnableBasicAuth: Optional[bool]
    EnableBranchAutoBuild: Optional[bool]
    EnableBranchAutoDeletion: Optional[bool]
    EnvironmentVariables: Optional[Sequence["_EnvironmentVariablesDefinition"]]
    IamServiceRoleArn: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    OauthToken: Optional[str]
    Platform: Optional[str]
    ProductionBranch: Optional[Sequence["_ProductionBranchDefinition"]]
    Repository: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    AutoBranchCreationConfig: Optional[Sequence["_AutoBranchCreationConfigDefinition"]]
    CustomRule: Optional[Sequence["_CustomRuleDefinition"]]

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
            AccessToken=json_data.get("AccessToken"),
            Arn=json_data.get("Arn"),
            AutoBranchCreationPatterns=json_data.get("AutoBranchCreationPatterns"),
            BasicAuthCredentials=json_data.get("BasicAuthCredentials"),
            BuildSpec=json_data.get("BuildSpec"),
            DefaultDomain=json_data.get("DefaultDomain"),
            Description=json_data.get("Description"),
            EnableAutoBranchCreation=json_data.get("EnableAutoBranchCreation"),
            EnableBasicAuth=json_data.get("EnableBasicAuth"),
            EnableBranchAutoBuild=json_data.get("EnableBranchAutoBuild"),
            EnableBranchAutoDeletion=json_data.get("EnableBranchAutoDeletion"),
            EnvironmentVariables=deserialize_list(json_data.get("EnvironmentVariables"), EnvironmentVariablesDefinition),
            IamServiceRoleArn=json_data.get("IamServiceRoleArn"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            OauthToken=json_data.get("OauthToken"),
            Platform=json_data.get("Platform"),
            ProductionBranch=deserialize_list(json_data.get("ProductionBranch"), ProductionBranchDefinition),
            Repository=json_data.get("Repository"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            AutoBranchCreationConfig=deserialize_list(json_data.get("AutoBranchCreationConfig"), AutoBranchCreationConfigDefinition),
            CustomRule=deserialize_list(json_data.get("CustomRule"), CustomRuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EnvironmentVariablesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvironmentVariablesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvironmentVariablesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvironmentVariablesDefinition = EnvironmentVariablesDefinition


@dataclass
class ProductionBranchDefinition(BaseModel):
    BranchName: Optional[str]
    LastDeployTime: Optional[str]
    Status: Optional[str]
    ThumbnailUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProductionBranchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProductionBranchDefinition"]:
        if not json_data:
            return None
        return cls(
            BranchName=json_data.get("BranchName"),
            LastDeployTime=json_data.get("LastDeployTime"),
            Status=json_data.get("Status"),
            ThumbnailUrl=json_data.get("ThumbnailUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProductionBranchDefinition = ProductionBranchDefinition


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
class AutoBranchCreationConfigDefinition(BaseModel):
    BasicAuthCredentials: Optional[str]
    BuildSpec: Optional[str]
    EnableAutoBuild: Optional[bool]
    EnableBasicAuth: Optional[bool]
    EnablePerformanceMode: Optional[bool]
    EnablePullRequestPreview: Optional[bool]
    EnvironmentVariables: Optional[Sequence["_EnvironmentVariablesDefinition2"]]
    Framework: Optional[str]
    PullRequestEnvironmentName: Optional[str]
    Stage: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AutoBranchCreationConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoBranchCreationConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            BasicAuthCredentials=json_data.get("BasicAuthCredentials"),
            BuildSpec=json_data.get("BuildSpec"),
            EnableAutoBuild=json_data.get("EnableAutoBuild"),
            EnableBasicAuth=json_data.get("EnableBasicAuth"),
            EnablePerformanceMode=json_data.get("EnablePerformanceMode"),
            EnablePullRequestPreview=json_data.get("EnablePullRequestPreview"),
            EnvironmentVariables=deserialize_list(json_data.get("EnvironmentVariables"), EnvironmentVariablesDefinition2),
            Framework=json_data.get("Framework"),
            PullRequestEnvironmentName=json_data.get("PullRequestEnvironmentName"),
            Stage=json_data.get("Stage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoBranchCreationConfigDefinition = AutoBranchCreationConfigDefinition


@dataclass
class EnvironmentVariablesDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvironmentVariablesDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvironmentVariablesDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvironmentVariablesDefinition2 = EnvironmentVariablesDefinition2


@dataclass
class CustomRuleDefinition(BaseModel):
    Condition: Optional[str]
    Source: Optional[str]
    Status: Optional[str]
    Target: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Condition=json_data.get("Condition"),
            Source=json_data.get("Source"),
            Status=json_data.get("Status"),
            Target=json_data.get("Target"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomRuleDefinition = CustomRuleDefinition


