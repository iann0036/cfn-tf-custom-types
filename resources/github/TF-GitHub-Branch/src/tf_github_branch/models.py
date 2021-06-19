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
    Etag: Optional[str]
    Id: Optional[str]
    Ref: Optional[str]
    Repository: Optional[str]
    Sha: Optional[str]
    SourceBranch: Optional[str]
    SourceSha: Optional[str]

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
            Etag=json_data.get("Etag"),
            Id=json_data.get("Id"),
            Ref=json_data.get("Ref"),
            Repository=json_data.get("Repository"),
            Sha=json_data.get("Sha"),
            SourceBranch=json_data.get("SourceBranch"),
            SourceSha=json_data.get("SourceSha"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


