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
    ConfidentialIssueChannel: Optional[str]
    ConfidentialIssuesEvents: Optional[bool]
    ConfidentialNoteEvents: Optional[bool]
    IssueChannel: Optional[str]
    IssuesEvents: Optional[bool]
    JobEvents: Optional[bool]
    MergeRequestChannel: Optional[str]
    MergeRequestsEvents: Optional[bool]
    NoteChannel: Optional[str]
    NoteEvents: Optional[bool]
    NotifyOnlyBrokenPipelines: Optional[bool]
    NotifyOnlyDefaultBranch: Optional[bool]
    PipelineChannel: Optional[str]
    PipelineEvents: Optional[bool]
    Project: Optional[str]
    PushChannel: Optional[str]
    PushEvents: Optional[bool]
    TagPushChannel: Optional[str]
    TagPushEvents: Optional[bool]
    Username: Optional[str]
    Webhook: Optional[str]
    WikiPageChannel: Optional[str]
    WikiPageEvents: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ConfidentialIssueChannel=json_data.get("ConfidentialIssueChannel"),
            ConfidentialIssuesEvents=json_data.get("ConfidentialIssuesEvents"),
            ConfidentialNoteEvents=json_data.get("ConfidentialNoteEvents"),
            IssueChannel=json_data.get("IssueChannel"),
            IssuesEvents=json_data.get("IssuesEvents"),
            JobEvents=json_data.get("JobEvents"),
            MergeRequestChannel=json_data.get("MergeRequestChannel"),
            MergeRequestsEvents=json_data.get("MergeRequestsEvents"),
            NoteChannel=json_data.get("NoteChannel"),
            NoteEvents=json_data.get("NoteEvents"),
            NotifyOnlyBrokenPipelines=json_data.get("NotifyOnlyBrokenPipelines"),
            NotifyOnlyDefaultBranch=json_data.get("NotifyOnlyDefaultBranch"),
            PipelineChannel=json_data.get("PipelineChannel"),
            PipelineEvents=json_data.get("PipelineEvents"),
            Project=json_data.get("Project"),
            PushChannel=json_data.get("PushChannel"),
            PushEvents=json_data.get("PushEvents"),
            TagPushChannel=json_data.get("TagPushChannel"),
            TagPushEvents=json_data.get("TagPushEvents"),
            Username=json_data.get("Username"),
            Webhook=json_data.get("Webhook"),
            WikiPageChannel=json_data.get("WikiPageChannel"),
            WikiPageEvents=json_data.get("WikiPageEvents"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


