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
    ConfidentialIssuesEvents: Optional[bool]
    ConfidentialNoteEvents: Optional[bool]
    DeploymentEvents: Optional[bool]
    EnableSslVerification: Optional[bool]
    Id: Optional[str]
    IssuesEvents: Optional[bool]
    JobEvents: Optional[bool]
    MergeRequestsEvents: Optional[bool]
    NoteEvents: Optional[bool]
    PipelineEvents: Optional[bool]
    Project: Optional[str]
    PushEvents: Optional[bool]
    PushEventsBranchFilter: Optional[str]
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
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ConfidentialIssuesEvents=json_data.get("ConfidentialIssuesEvents"),
            ConfidentialNoteEvents=json_data.get("ConfidentialNoteEvents"),
            DeploymentEvents=json_data.get("DeploymentEvents"),
            EnableSslVerification=json_data.get("EnableSslVerification"),
            Id=json_data.get("Id"),
            IssuesEvents=json_data.get("IssuesEvents"),
            JobEvents=json_data.get("JobEvents"),
            MergeRequestsEvents=json_data.get("MergeRequestsEvents"),
            NoteEvents=json_data.get("NoteEvents"),
            PipelineEvents=json_data.get("PipelineEvents"),
            Project=json_data.get("Project"),
            PushEvents=json_data.get("PushEvents"),
            PushEventsBranchFilter=json_data.get("PushEventsBranchFilter"),
            TagPushEvents=json_data.get("TagPushEvents"),
            Token=json_data.get("Token"),
            Url=json_data.get("Url"),
            WikiPageEvents=json_data.get("WikiPageEvents"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


