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
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    Status: Optional[str]
    Vdomparam: Optional[str]
    NodeList: Optional[Sequence["_NodeListDefinition"]]

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
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            Status=json_data.get("Status"),
            Vdomparam=json_data.get("Vdomparam"),
            NodeList=deserialize_list(json_data.get("NodeList"), NodeListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class NodeListDefinition(BaseModel):
    Serial: Optional[str]
    SetupTime: Optional[str]
    Time: Optional[str]
    Timing: Optional[str]
    UpgradePath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodeListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeListDefinition"]:
        if not json_data:
            return None
        return cls(
            Serial=json_data.get("Serial"),
            SetupTime=json_data.get("SetupTime"),
            Time=json_data.get("Time"),
            Timing=json_data.get("Timing"),
            UpgradePath=json_data.get("UpgradePath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeListDefinition = NodeListDefinition


