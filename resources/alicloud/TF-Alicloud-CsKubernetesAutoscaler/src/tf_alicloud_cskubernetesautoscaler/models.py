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
    ClusterId: Optional[str]
    CoolDownDuration: Optional[str]
    DeferScaleInDuration: Optional[str]
    Id: Optional[str]
    UseEcsRamRoleToken: Optional[bool]
    Utilization: Optional[str]
    Nodepools: Optional[Sequence["_NodepoolsDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            ClusterId=json_data.get("ClusterId"),
            CoolDownDuration=json_data.get("CoolDownDuration"),
            DeferScaleInDuration=json_data.get("DeferScaleInDuration"),
            Id=json_data.get("Id"),
            UseEcsRamRoleToken=json_data.get("UseEcsRamRoleToken"),
            Utilization=json_data.get("Utilization"),
            Nodepools=deserialize_list(json_data.get("Nodepools"), NodepoolsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class NodepoolsDefinition(BaseModel):
    Id: Optional[str]
    Labels: Optional[str]
    Taints: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodepoolsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodepoolsDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Labels=json_data.get("Labels"),
            Taints=json_data.get("Taints"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodepoolsDefinition = NodepoolsDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


