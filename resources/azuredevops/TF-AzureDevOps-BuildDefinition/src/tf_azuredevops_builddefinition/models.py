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
    AgentPoolName: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Path: Optional[str]
    ProjectId: Optional[str]
    Revision: Optional[float]
    VariableGroups: Optional[Sequence[float]]
    CiTrigger: Optional[Sequence["_CiTriggerDefinition"]]
    PullRequestTrigger: Optional[Sequence["_PullRequestTriggerDefinition"]]
    Repository: Optional[Sequence["_RepositoryDefinition"]]
    Variable: Optional[Sequence["_VariableDefinition"]]

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
            AgentPoolName=json_data.get("AgentPoolName"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            ProjectId=json_data.get("ProjectId"),
            Revision=json_data.get("Revision"),
            VariableGroups=json_data.get("VariableGroups"),
            CiTrigger=deserialize_list(json_data.get("CiTrigger"), CiTriggerDefinition),
            PullRequestTrigger=deserialize_list(json_data.get("PullRequestTrigger"), PullRequestTriggerDefinition),
            Repository=deserialize_list(json_data.get("Repository"), RepositoryDefinition),
            Variable=deserialize_list(json_data.get("Variable"), VariableDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CiTriggerDefinition(BaseModel):
    UseYaml: Optional[bool]
    Override: Optional[Sequence["_OverrideDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CiTriggerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CiTriggerDefinition"]:
        if not json_data:
            return None
        return cls(
            UseYaml=json_data.get("UseYaml"),
            Override=deserialize_list(json_data.get("Override"), OverrideDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CiTriggerDefinition = CiTriggerDefinition


@dataclass
class OverrideDefinition(BaseModel):
    AutoCancel: Optional[bool]
    BranchFilter: Optional[Sequence["_BranchFilterDefinition"]]
    PathFilter: Optional[Sequence["_PathFilterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OverrideDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OverrideDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoCancel=json_data.get("AutoCancel"),
            BranchFilter=deserialize_list(json_data.get("BranchFilter"), BranchFilterDefinition),
            PathFilter=deserialize_list(json_data.get("PathFilter"), PathFilterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OverrideDefinition = OverrideDefinition


@dataclass
class BranchFilterDefinition(BaseModel):
    Exclude: Optional[Sequence[str]]
    Include: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_BranchFilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BranchFilterDefinition"]:
        if not json_data:
            return None
        return cls(
            Exclude=json_data.get("Exclude"),
            Include=json_data.get("Include"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BranchFilterDefinition = BranchFilterDefinition


@dataclass
class PathFilterDefinition(BaseModel):
    Exclude: Optional[Sequence[str]]
    Include: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PathFilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PathFilterDefinition"]:
        if not json_data:
            return None
        return cls(
            Exclude=json_data.get("Exclude"),
            Include=json_data.get("Include"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PathFilterDefinition = PathFilterDefinition


@dataclass
class PullRequestTriggerDefinition(BaseModel):
    CommentRequired: Optional[str]
    InitialBranch: Optional[str]
    UseYaml: Optional[bool]
    Forks: Optional[Sequence["_ForksDefinition"]]
    Override: Optional[Sequence["_OverrideDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PullRequestTriggerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PullRequestTriggerDefinition"]:
        if not json_data:
            return None
        return cls(
            CommentRequired=json_data.get("CommentRequired"),
            InitialBranch=json_data.get("InitialBranch"),
            UseYaml=json_data.get("UseYaml"),
            Forks=deserialize_list(json_data.get("Forks"), ForksDefinition),
            Override=deserialize_list(json_data.get("Override"), OverrideDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PullRequestTriggerDefinition = PullRequestTriggerDefinition


@dataclass
class ForksDefinition(BaseModel):
    Enabled: Optional[bool]
    ShareSecrets: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ForksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForksDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            ShareSecrets=json_data.get("ShareSecrets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForksDefinition = ForksDefinition


@dataclass
class RepositoryDefinition(BaseModel):
    BranchName: Optional[str]
    GithubEnterpriseUrl: Optional[str]
    RepoId: Optional[str]
    RepoType: Optional[str]
    ReportBuildStatus: Optional[bool]
    ServiceConnectionId: Optional[str]
    YmlPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RepositoryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RepositoryDefinition"]:
        if not json_data:
            return None
        return cls(
            BranchName=json_data.get("BranchName"),
            GithubEnterpriseUrl=json_data.get("GithubEnterpriseUrl"),
            RepoId=json_data.get("RepoId"),
            RepoType=json_data.get("RepoType"),
            ReportBuildStatus=json_data.get("ReportBuildStatus"),
            ServiceConnectionId=json_data.get("ServiceConnectionId"),
            YmlPath=json_data.get("YmlPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RepositoryDefinition = RepositoryDefinition


@dataclass
class VariableDefinition(BaseModel):
    AllowOverride: Optional[bool]
    IsSecret: Optional[bool]
    Name: Optional[str]
    SecretValue: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VariableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VariableDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowOverride=json_data.get("AllowOverride"),
            IsSecret=json_data.get("IsSecret"),
            Name=json_data.get("Name"),
            SecretValue=json_data.get("SecretValue"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VariableDefinition = VariableDefinition


