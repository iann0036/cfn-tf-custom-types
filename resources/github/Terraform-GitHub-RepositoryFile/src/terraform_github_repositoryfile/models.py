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
    Branch: Optional[str]
    CommitAuthor: Optional[str]
    CommitEmail: Optional[str]
    CommitMessage: Optional[str]
    Content: Optional[str]
    File: Optional[str]
    Repository: Optional[str]
    Sha: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Branch=json_data.get("Branch"),
            CommitAuthor=json_data.get("CommitAuthor"),
            CommitEmail=json_data.get("CommitEmail"),
            CommitMessage=json_data.get("CommitMessage"),
            Content=json_data.get("Content"),
            File=json_data.get("File"),
            Repository=json_data.get("Repository"),
            Sha=json_data.get("Sha"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


