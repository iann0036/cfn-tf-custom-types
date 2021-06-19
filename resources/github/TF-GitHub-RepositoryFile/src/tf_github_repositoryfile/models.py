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
    Branch: Optional[str]
    CommitAuthor: Optional[str]
    CommitEmail: Optional[str]
    CommitMessage: Optional[str]
    CommitSha: Optional[str]
    Content: Optional[str]
    File: Optional[str]
    Id: Optional[str]
    OverwriteOnCreate: Optional[bool]
    Repository: Optional[str]
    Sha: Optional[str]

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
            Branch=json_data.get("Branch"),
            CommitAuthor=json_data.get("CommitAuthor"),
            CommitEmail=json_data.get("CommitEmail"),
            CommitMessage=json_data.get("CommitMessage"),
            CommitSha=json_data.get("CommitSha"),
            Content=json_data.get("Content"),
            File=json_data.get("File"),
            Id=json_data.get("Id"),
            OverwriteOnCreate=json_data.get("OverwriteOnCreate"),
            Repository=json_data.get("Repository"),
            Sha=json_data.get("Sha"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


