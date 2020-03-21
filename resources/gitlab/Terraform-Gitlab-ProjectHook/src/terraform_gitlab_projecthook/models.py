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
    EnableSslVerification: Optional[bool]
    IssuesEvents: Optional[bool]
    JobEvents: Optional[bool]
    MergeRequestsEvents: Optional[bool]
    NoteEvents: Optional[bool]
    PipelineEvents: Optional[bool]
    Project: Optional[str]
    PushEvents: Optional[bool]
    TagPushEvents: Optional[bool]
    Token: Optional[str]
    Url: Optional[str]
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
            EnableSslVerification=json_data.get("EnableSslVerification"),
            IssuesEvents=json_data.get("IssuesEvents"),
            JobEvents=json_data.get("JobEvents"),
            MergeRequestsEvents=json_data.get("MergeRequestsEvents"),
            NoteEvents=json_data.get("NoteEvents"),
            PipelineEvents=json_data.get("PipelineEvents"),
            Project=json_data.get("Project"),
            PushEvents=json_data.get("PushEvents"),
            TagPushEvents=json_data.get("TagPushEvents"),
            Token=json_data.get("Token"),
            Url=json_data.get("Url"),
            WikiPageEvents=json_data.get("WikiPageEvents"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


