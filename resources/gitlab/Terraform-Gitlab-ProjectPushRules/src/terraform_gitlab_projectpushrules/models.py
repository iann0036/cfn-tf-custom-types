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
    AuthorEmailRegex: Optional[str]
    BranchNameRegex: Optional[str]
    CommitMessageRegex: Optional[str]
    DenyDeleteTag: Optional[bool]
    FileNameRegex: Optional[str]
    Id: Optional[str]
    MaxFileSize: Optional[float]
    MemberCheck: Optional[bool]
    PreventSecrets: Optional[bool]
    Project: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AuthorEmailRegex=json_data.get("AuthorEmailRegex"),
            BranchNameRegex=json_data.get("BranchNameRegex"),
            CommitMessageRegex=json_data.get("CommitMessageRegex"),
            DenyDeleteTag=json_data.get("DenyDeleteTag"),
            FileNameRegex=json_data.get("FileNameRegex"),
            Id=json_data.get("Id"),
            MaxFileSize=json_data.get("MaxFileSize"),
            MemberCheck=json_data.get("MemberCheck"),
            PreventSecrets=json_data.get("PreventSecrets"),
            Project=json_data.get("Project"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


