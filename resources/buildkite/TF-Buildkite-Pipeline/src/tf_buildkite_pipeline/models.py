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
    BranchConfiguration: Optional[str]
    CancelIntermediateBuilds: Optional[bool]
    CancelIntermediateBuildsBranchFilter: Optional[str]
    DefaultBranch: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Repository: Optional[str]
    SkipIntermediateBuilds: Optional[bool]
    SkipIntermediateBuildsBranchFilter: Optional[str]
    Slug: Optional[str]
    Steps: Optional[str]
    Team: Optional[Sequence["_TeamDefinition"]]
    WebhookUrl: Optional[str]
    ProviderSettings: Optional[Sequence["_ProviderSettingsDefinition"]]

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
            BranchConfiguration=json_data.get("BranchConfiguration"),
            CancelIntermediateBuilds=json_data.get("CancelIntermediateBuilds"),
            CancelIntermediateBuildsBranchFilter=json_data.get("CancelIntermediateBuildsBranchFilter"),
            DefaultBranch=json_data.get("DefaultBranch"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Repository=json_data.get("Repository"),
            SkipIntermediateBuilds=json_data.get("SkipIntermediateBuilds"),
            SkipIntermediateBuildsBranchFilter=json_data.get("SkipIntermediateBuildsBranchFilter"),
            Slug=json_data.get("Slug"),
            Steps=json_data.get("Steps"),
            Team=deserialize_list(json_data.get("Team"), TeamDefinition),
            WebhookUrl=json_data.get("WebhookUrl"),
            ProviderSettings=deserialize_list(json_data.get("ProviderSettings"), ProviderSettingsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TeamDefinition(BaseModel):
    AccessLevel: Optional[str]
    Slug: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TeamDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TeamDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessLevel=json_data.get("AccessLevel"),
            Slug=json_data.get("Slug"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TeamDefinition = TeamDefinition


@dataclass
class ProviderSettingsDefinition(BaseModel):
    BuildBranches: Optional[bool]
    BuildPullRequestForks: Optional[bool]
    BuildPullRequestReadyForReview: Optional[bool]
    BuildPullRequests: Optional[bool]
    BuildTags: Optional[bool]
    CancelDeletedBranchBuilds: Optional[bool]
    PrefixPullRequestForkBranchNames: Optional[bool]
    PublishBlockedAsPending: Optional[bool]
    PublishCommitStatus: Optional[bool]
    PublishCommitStatusPerStep: Optional[bool]
    PullRequestBranchFilterConfiguration: Optional[str]
    PullRequestBranchFilterEnabled: Optional[bool]
    SeparatePullRequestStatuses: Optional[bool]
    SkipPullRequestBuildsForExistingCommits: Optional[bool]
    TriggerMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProviderSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProviderSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            BuildBranches=json_data.get("BuildBranches"),
            BuildPullRequestForks=json_data.get("BuildPullRequestForks"),
            BuildPullRequestReadyForReview=json_data.get("BuildPullRequestReadyForReview"),
            BuildPullRequests=json_data.get("BuildPullRequests"),
            BuildTags=json_data.get("BuildTags"),
            CancelDeletedBranchBuilds=json_data.get("CancelDeletedBranchBuilds"),
            PrefixPullRequestForkBranchNames=json_data.get("PrefixPullRequestForkBranchNames"),
            PublishBlockedAsPending=json_data.get("PublishBlockedAsPending"),
            PublishCommitStatus=json_data.get("PublishCommitStatus"),
            PublishCommitStatusPerStep=json_data.get("PublishCommitStatusPerStep"),
            PullRequestBranchFilterConfiguration=json_data.get("PullRequestBranchFilterConfiguration"),
            PullRequestBranchFilterEnabled=json_data.get("PullRequestBranchFilterEnabled"),
            SeparatePullRequestStatuses=json_data.get("SeparatePullRequestStatuses"),
            SkipPullRequestBuildsForExistingCommits=json_data.get("SkipPullRequestBuildsForExistingCommits"),
            TriggerMode=json_data.get("TriggerMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProviderSettingsDefinition = ProviderSettingsDefinition


