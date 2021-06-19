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
    ApprovalsBeforeMerge: Optional[float]
    Archived: Optional[bool]
    ContainerRegistryEnabled: Optional[bool]
    DefaultBranch: Optional[str]
    Description: Optional[str]
    GroupWithProjectTemplatesId: Optional[float]
    HttpUrlToRepo: Optional[str]
    Id: Optional[str]
    ImportUrl: Optional[str]
    InitializeWithReadme: Optional[bool]
    IssuesEnabled: Optional[bool]
    LfsEnabled: Optional[bool]
    MergeMethod: Optional[str]
    MergeRequestsEnabled: Optional[bool]
    Mirror: Optional[bool]
    MirrorOverwritesDivergedBranches: Optional[bool]
    MirrorTriggerBuilds: Optional[bool]
    Name: Optional[str]
    NamespaceId: Optional[float]
    OnlyAllowMergeIfAllDiscussionsAreResolved: Optional[bool]
    OnlyAllowMergeIfPipelineSucceeds: Optional[bool]
    OnlyMirrorProtectedBranches: Optional[bool]
    PackagesEnabled: Optional[bool]
    PagesAccessLevel: Optional[str]
    Path: Optional[str]
    PathWithNamespace: Optional[str]
    PipelinesEnabled: Optional[bool]
    RemoveSourceBranchAfterMerge: Optional[bool]
    RequestAccessEnabled: Optional[bool]
    RunnersToken: Optional[str]
    SharedRunnersEnabled: Optional[bool]
    SnippetsEnabled: Optional[bool]
    SshUrlToRepo: Optional[str]
    Tags: Optional[Sequence[str]]
    TemplateName: Optional[str]
    TemplateProjectId: Optional[float]
    UseCustomTemplate: Optional[bool]
    VisibilityLevel: Optional[str]
    WebUrl: Optional[str]
    WikiEnabled: Optional[bool]
    PushRules: Optional[Sequence["_PushRulesDefinition"]]

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
            ApprovalsBeforeMerge=json_data.get("ApprovalsBeforeMerge"),
            Archived=json_data.get("Archived"),
            ContainerRegistryEnabled=json_data.get("ContainerRegistryEnabled"),
            DefaultBranch=json_data.get("DefaultBranch"),
            Description=json_data.get("Description"),
            GroupWithProjectTemplatesId=json_data.get("GroupWithProjectTemplatesId"),
            HttpUrlToRepo=json_data.get("HttpUrlToRepo"),
            Id=json_data.get("Id"),
            ImportUrl=json_data.get("ImportUrl"),
            InitializeWithReadme=json_data.get("InitializeWithReadme"),
            IssuesEnabled=json_data.get("IssuesEnabled"),
            LfsEnabled=json_data.get("LfsEnabled"),
            MergeMethod=json_data.get("MergeMethod"),
            MergeRequestsEnabled=json_data.get("MergeRequestsEnabled"),
            Mirror=json_data.get("Mirror"),
            MirrorOverwritesDivergedBranches=json_data.get("MirrorOverwritesDivergedBranches"),
            MirrorTriggerBuilds=json_data.get("MirrorTriggerBuilds"),
            Name=json_data.get("Name"),
            NamespaceId=json_data.get("NamespaceId"),
            OnlyAllowMergeIfAllDiscussionsAreResolved=json_data.get("OnlyAllowMergeIfAllDiscussionsAreResolved"),
            OnlyAllowMergeIfPipelineSucceeds=json_data.get("OnlyAllowMergeIfPipelineSucceeds"),
            OnlyMirrorProtectedBranches=json_data.get("OnlyMirrorProtectedBranches"),
            PackagesEnabled=json_data.get("PackagesEnabled"),
            PagesAccessLevel=json_data.get("PagesAccessLevel"),
            Path=json_data.get("Path"),
            PathWithNamespace=json_data.get("PathWithNamespace"),
            PipelinesEnabled=json_data.get("PipelinesEnabled"),
            RemoveSourceBranchAfterMerge=json_data.get("RemoveSourceBranchAfterMerge"),
            RequestAccessEnabled=json_data.get("RequestAccessEnabled"),
            RunnersToken=json_data.get("RunnersToken"),
            SharedRunnersEnabled=json_data.get("SharedRunnersEnabled"),
            SnippetsEnabled=json_data.get("SnippetsEnabled"),
            SshUrlToRepo=json_data.get("SshUrlToRepo"),
            Tags=json_data.get("Tags"),
            TemplateName=json_data.get("TemplateName"),
            TemplateProjectId=json_data.get("TemplateProjectId"),
            UseCustomTemplate=json_data.get("UseCustomTemplate"),
            VisibilityLevel=json_data.get("VisibilityLevel"),
            WebUrl=json_data.get("WebUrl"),
            WikiEnabled=json_data.get("WikiEnabled"),
            PushRules=deserialize_list(json_data.get("PushRules"), PushRulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PushRulesDefinition(BaseModel):
    AuthorEmailRegex: Optional[str]
    BranchNameRegex: Optional[str]
    CommitCommitterCheck: Optional[bool]
    CommitMessageNegativeRegex: Optional[str]
    CommitMessageRegex: Optional[str]
    DenyDeleteTag: Optional[bool]
    FileNameRegex: Optional[str]
    MaxFileSize: Optional[float]
    MemberCheck: Optional[bool]
    PreventSecrets: Optional[bool]
    RejectUnsignedCommits: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PushRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PushRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthorEmailRegex=json_data.get("AuthorEmailRegex"),
            BranchNameRegex=json_data.get("BranchNameRegex"),
            CommitCommitterCheck=json_data.get("CommitCommitterCheck"),
            CommitMessageNegativeRegex=json_data.get("CommitMessageNegativeRegex"),
            CommitMessageRegex=json_data.get("CommitMessageRegex"),
            DenyDeleteTag=json_data.get("DenyDeleteTag"),
            FileNameRegex=json_data.get("FileNameRegex"),
            MaxFileSize=json_data.get("MaxFileSize"),
            MemberCheck=json_data.get("MemberCheck"),
            PreventSecrets=json_data.get("PreventSecrets"),
            RejectUnsignedCommits=json_data.get("RejectUnsignedCommits"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PushRulesDefinition = PushRulesDefinition


