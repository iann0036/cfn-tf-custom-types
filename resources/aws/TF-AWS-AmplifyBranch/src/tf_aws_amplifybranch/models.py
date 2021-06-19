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
    AppId: Optional[str]
    Arn: Optional[str]
    AssociatedResources: Optional[Sequence[str]]
    BackendEnvironmentArn: Optional[str]
    BasicAuthCredentials: Optional[str]
    BranchName: Optional[str]
    CustomDomains: Optional[Sequence[str]]
    Description: Optional[str]
    DestinationBranch: Optional[str]
    DisplayName: Optional[str]
    EnableAutoBuild: Optional[bool]
    EnableBasicAuth: Optional[bool]
    EnableNotification: Optional[bool]
    EnablePerformanceMode: Optional[bool]
    EnablePullRequestPreview: Optional[bool]
    EnvironmentVariables: Optional[Sequence["_EnvironmentVariablesDefinition"]]
    Framework: Optional[str]
    Id: Optional[str]
    PullRequestEnvironmentName: Optional[str]
    SourceBranch: Optional[str]
    Stage: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Ttl: Optional[str]

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
            AppId=json_data.get("AppId"),
            Arn=json_data.get("Arn"),
            AssociatedResources=json_data.get("AssociatedResources"),
            BackendEnvironmentArn=json_data.get("BackendEnvironmentArn"),
            BasicAuthCredentials=json_data.get("BasicAuthCredentials"),
            BranchName=json_data.get("BranchName"),
            CustomDomains=json_data.get("CustomDomains"),
            Description=json_data.get("Description"),
            DestinationBranch=json_data.get("DestinationBranch"),
            DisplayName=json_data.get("DisplayName"),
            EnableAutoBuild=json_data.get("EnableAutoBuild"),
            EnableBasicAuth=json_data.get("EnableBasicAuth"),
            EnableNotification=json_data.get("EnableNotification"),
            EnablePerformanceMode=json_data.get("EnablePerformanceMode"),
            EnablePullRequestPreview=json_data.get("EnablePullRequestPreview"),
            EnvironmentVariables=deserialize_list(json_data.get("EnvironmentVariables"), EnvironmentVariablesDefinition),
            Framework=json_data.get("Framework"),
            Id=json_data.get("Id"),
            PullRequestEnvironmentName=json_data.get("PullRequestEnvironmentName"),
            SourceBranch=json_data.get("SourceBranch"),
            Stage=json_data.get("Stage"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Ttl=json_data.get("Ttl"),
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


