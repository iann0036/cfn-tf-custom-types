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
    DefaultPort: Optional[float]
    Description: Optional[str]
    HostSetIds: Optional[Sequence[str]]
    Id: Optional[str]
    Name: Optional[str]
    ScopeId: Optional[str]
    SessionConnectionLimit: Optional[float]
    SessionMaxSeconds: Optional[float]
    Type: Optional[str]
    WorkerFilter: Optional[str]

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
            DefaultPort=json_data.get("DefaultPort"),
            Description=json_data.get("Description"),
            HostSetIds=json_data.get("HostSetIds"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ScopeId=json_data.get("ScopeId"),
            SessionConnectionLimit=json_data.get("SessionConnectionLimit"),
            SessionMaxSeconds=json_data.get("SessionMaxSeconds"),
            Type=json_data.get("Type"),
            WorkerFilter=json_data.get("WorkerFilter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


