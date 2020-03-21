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
    ApprovalsBeforeMerge: Optional[float]
    Archived: Optional[bool]
    ContainerRegistryEnabled: Optional[bool]
    DefaultBranch: Optional[str]
    Description: Optional[str]
    HttpUrlToRepo: Optional[str]
    InitializeWithReadme: Optional[bool]
    IssuesEnabled: Optional[bool]
    LfsEnabled: Optional[bool]
    MergeMethod: Optional[str]
    MergeRequestsEnabled: Optional[bool]
    Name: Optional[str]
    NamespaceId: Optional[float]
    OnlyAllowMergeIfAllDiscussionsAreResolved: Optional[bool]
    OnlyAllowMergeIfPipelineSucceeds: Optional[bool]
    Path: Optional[str]
    PipelinesEnabled: Optional[bool]
    RequestAccessEnabled: Optional[bool]
    RunnersToken: Optional[str]
    SharedRunnersEnabled: Optional[bool]
    SnippetsEnabled: Optional[bool]
    SshUrlToRepo: Optional[str]
    Tags: Optional[Sequence[str]]
    VisibilityLevel: Optional[str]
    WebUrl: Optional[str]
    WikiEnabled: Optional[bool]
    SharedWithGroups: Optional[Sequence["_SharedWithGroups"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ApprovalsBeforeMerge=json_data.get("ApprovalsBeforeMerge"),
            Archived=json_data.get("Archived"),
            ContainerRegistryEnabled=json_data.get("ContainerRegistryEnabled"),
            DefaultBranch=json_data.get("DefaultBranch"),
            Description=json_data.get("Description"),
            HttpUrlToRepo=json_data.get("HttpUrlToRepo"),
            InitializeWithReadme=json_data.get("InitializeWithReadme"),
            IssuesEnabled=json_data.get("IssuesEnabled"),
            LfsEnabled=json_data.get("LfsEnabled"),
            MergeMethod=json_data.get("MergeMethod"),
            MergeRequestsEnabled=json_data.get("MergeRequestsEnabled"),
            Name=json_data.get("Name"),
            NamespaceId=json_data.get("NamespaceId"),
            OnlyAllowMergeIfAllDiscussionsAreResolved=json_data.get("OnlyAllowMergeIfAllDiscussionsAreResolved"),
            OnlyAllowMergeIfPipelineSucceeds=json_data.get("OnlyAllowMergeIfPipelineSucceeds"),
            Path=json_data.get("Path"),
            PipelinesEnabled=json_data.get("PipelinesEnabled"),
            RequestAccessEnabled=json_data.get("RequestAccessEnabled"),
            RunnersToken=json_data.get("RunnersToken"),
            SharedRunnersEnabled=json_data.get("SharedRunnersEnabled"),
            SnippetsEnabled=json_data.get("SnippetsEnabled"),
            SshUrlToRepo=json_data.get("SshUrlToRepo"),
            Tags=json_data.get("Tags"),
            VisibilityLevel=json_data.get("VisibilityLevel"),
            WebUrl=json_data.get("WebUrl"),
            WikiEnabled=json_data.get("WikiEnabled"),
            SharedWithGroups=json_data.get("SharedWithGroups"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SharedWithGroups:
    GroupAccessLevel: Optional[str]
    GroupId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SharedWithGroups"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SharedWithGroups"]:
        if not json_data:
            return None
        return cls(
            GroupAccessLevel=json_data.get("GroupAccessLevel"),
            GroupId=json_data.get("GroupId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SharedWithGroups = SharedWithGroups


