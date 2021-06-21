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
    Active: Optional[bool]
    CreatedAt: Optional[str]
    Id: Optional[str]
    Project: Optional[str]
    RepositoryUrl: Optional[str]
    StaticContext: Optional[bool]
    Title: Optional[str]
    Token: Optional[str]
    UpdatedAt: Optional[str]

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
            Active=json_data.get("Active"),
            CreatedAt=json_data.get("CreatedAt"),
            Id=json_data.get("Id"),
            Project=json_data.get("Project"),
            RepositoryUrl=json_data.get("RepositoryUrl"),
            StaticContext=json_data.get("StaticContext"),
            Title=json_data.get("Title"),
            Token=json_data.get("Token"),
            UpdatedAt=json_data.get("UpdatedAt"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel

