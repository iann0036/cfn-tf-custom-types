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
    DefaultBranch: Optional[str]
    Id: Optional[str]
    IsFork: Optional[bool]
    Name: Optional[str]
    ParentRepositoryId: Optional[str]
    ProjectId: Optional[str]
    RemoteUrl: Optional[str]
    Size: Optional[float]
    SshUrl: Optional[str]
    Url: Optional[str]
    WebUrl: Optional[str]
    Initialization: Optional[Sequence["_InitializationDefinition"]]

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
            DefaultBranch=json_data.get("DefaultBranch"),
            Id=json_data.get("Id"),
            IsFork=json_data.get("IsFork"),
            Name=json_data.get("Name"),
            ParentRepositoryId=json_data.get("ParentRepositoryId"),
            ProjectId=json_data.get("ProjectId"),
            RemoteUrl=json_data.get("RemoteUrl"),
            Size=json_data.get("Size"),
            SshUrl=json_data.get("SshUrl"),
            Url=json_data.get("Url"),
            WebUrl=json_data.get("WebUrl"),
            Initialization=deserialize_list(json_data.get("Initialization"), InitializationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InitializationDefinition(BaseModel):
    InitType: Optional[str]
    SourceType: Optional[str]
    SourceUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InitializationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InitializationDefinition"]:
        if not json_data:
            return None
        return cls(
            InitType=json_data.get("InitType"),
            SourceType=json_data.get("SourceType"),
            SourceUrl=json_data.get("SourceUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InitializationDefinition = InitializationDefinition


