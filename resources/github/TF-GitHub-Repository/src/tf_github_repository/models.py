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
    AllowMergeCommit: Optional[bool]
    AllowRebaseMerge: Optional[bool]
    AllowSquashMerge: Optional[bool]
    ArchiveOnDestroy: Optional[bool]
    Archived: Optional[bool]
    AutoInit: Optional[bool]
    DefaultBranch: Optional[str]
    DeleteBranchOnMerge: Optional[bool]
    Description: Optional[str]
    Etag: Optional[str]
    FullName: Optional[str]
    GitCloneUrl: Optional[str]
    GitignoreTemplate: Optional[str]
    HasDownloads: Optional[bool]
    HasIssues: Optional[bool]
    HasProjects: Optional[bool]
    HasWiki: Optional[bool]
    HomepageUrl: Optional[str]
    HtmlUrl: Optional[str]
    HttpCloneUrl: Optional[str]
    Id: Optional[str]
    IsTemplate: Optional[bool]
    LicenseTemplate: Optional[str]
    Name: Optional[str]
    NodeId: Optional[str]
    Private: Optional[bool]
    RepoId: Optional[float]
    SshCloneUrl: Optional[str]
    SvnUrl: Optional[str]
    Topics: Optional[Sequence[str]]
    Visibility: Optional[str]
    VulnerabilityAlerts: Optional[bool]
    Pages: Optional[Sequence["_PagesDefinition"]]
    Template: Optional[Sequence["_TemplateDefinition"]]

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
            AllowMergeCommit=json_data.get("AllowMergeCommit"),
            AllowRebaseMerge=json_data.get("AllowRebaseMerge"),
            AllowSquashMerge=json_data.get("AllowSquashMerge"),
            ArchiveOnDestroy=json_data.get("ArchiveOnDestroy"),
            Archived=json_data.get("Archived"),
            AutoInit=json_data.get("AutoInit"),
            DefaultBranch=json_data.get("DefaultBranch"),
            DeleteBranchOnMerge=json_data.get("DeleteBranchOnMerge"),
            Description=json_data.get("Description"),
            Etag=json_data.get("Etag"),
            FullName=json_data.get("FullName"),
            GitCloneUrl=json_data.get("GitCloneUrl"),
            GitignoreTemplate=json_data.get("GitignoreTemplate"),
            HasDownloads=json_data.get("HasDownloads"),
            HasIssues=json_data.get("HasIssues"),
            HasProjects=json_data.get("HasProjects"),
            HasWiki=json_data.get("HasWiki"),
            HomepageUrl=json_data.get("HomepageUrl"),
            HtmlUrl=json_data.get("HtmlUrl"),
            HttpCloneUrl=json_data.get("HttpCloneUrl"),
            Id=json_data.get("Id"),
            IsTemplate=json_data.get("IsTemplate"),
            LicenseTemplate=json_data.get("LicenseTemplate"),
            Name=json_data.get("Name"),
            NodeId=json_data.get("NodeId"),
            Private=json_data.get("Private"),
            RepoId=json_data.get("RepoId"),
            SshCloneUrl=json_data.get("SshCloneUrl"),
            SvnUrl=json_data.get("SvnUrl"),
            Topics=json_data.get("Topics"),
            Visibility=json_data.get("Visibility"),
            VulnerabilityAlerts=json_data.get("VulnerabilityAlerts"),
            Pages=deserialize_list(json_data.get("Pages"), PagesDefinition),
            Template=deserialize_list(json_data.get("Template"), TemplateDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PagesDefinition(BaseModel):
    Cname: Optional[str]
    Source: Optional[Sequence["_SourceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PagesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PagesDefinition"]:
        if not json_data:
            return None
        return cls(
            Cname=json_data.get("Cname"),
            Source=deserialize_list(json_data.get("Source"), SourceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PagesDefinition = PagesDefinition


@dataclass
class SourceDefinition(BaseModel):
    Branch: Optional[str]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceDefinition"]:
        if not json_data:
            return None
        return cls(
            Branch=json_data.get("Branch"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceDefinition = SourceDefinition


@dataclass
class TemplateDefinition(BaseModel):
    Owner: Optional[str]
    Repository: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TemplateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TemplateDefinition"]:
        if not json_data:
            return None
        return cls(
            Owner=json_data.get("Owner"),
            Repository=json_data.get("Repository"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TemplateDefinition = TemplateDefinition


