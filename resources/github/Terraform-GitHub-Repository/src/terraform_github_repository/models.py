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
    AllowMergeCommit: Optional[bool]
    AllowRebaseMerge: Optional[bool]
    AllowSquashMerge: Optional[bool]
    Archived: Optional[bool]
    AutoInit: Optional[bool]
    DefaultBranch: Optional[str]
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
    LicenseTemplate: Optional[str]
    Name: Optional[str]
    Private: Optional[bool]
    SshCloneUrl: Optional[str]
    SvnUrl: Optional[str]
    Topics: Optional[Sequence[str]]
    Template: Optional[Sequence["_Template"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AllowMergeCommit=json_data.get("AllowMergeCommit"),
            AllowRebaseMerge=json_data.get("AllowRebaseMerge"),
            AllowSquashMerge=json_data.get("AllowSquashMerge"),
            Archived=json_data.get("Archived"),
            AutoInit=json_data.get("AutoInit"),
            DefaultBranch=json_data.get("DefaultBranch"),
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
            LicenseTemplate=json_data.get("LicenseTemplate"),
            Name=json_data.get("Name"),
            Private=json_data.get("Private"),
            SshCloneUrl=json_data.get("SshCloneUrl"),
            SvnUrl=json_data.get("SvnUrl"),
            Topics=json_data.get("Topics"),
            Template=json_data.get("Template"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Template:
    Owner: Optional[str]
    Repository: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Template"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Template"]:
        if not json_data:
            return None
        return cls(
            Owner=json_data.get("Owner"),
            Repository=json_data.get("Repository"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Template = Template


