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
    Id: Optional[str]
    ListenerId: Optional[str]
    LoadbalancerId: Optional[str]
    LocationId: Optional[str]
    ProtocolType: Optional[str]
    Backends: Optional[Sequence["_BackendsDefinition"]]

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
            Id=json_data.get("Id"),
            ListenerId=json_data.get("ListenerId"),
            LoadbalancerId=json_data.get("LoadbalancerId"),
            LocationId=json_data.get("LocationId"),
            ProtocolType=json_data.get("ProtocolType"),
            Backends=deserialize_list(json_data.get("Backends"), BackendsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BackendsDefinition(BaseModel):
    InstanceId: Optional[str]
    Port: Optional[float]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_BackendsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackendsDefinition"]:
        if not json_data:
            return None
        return cls(
            InstanceId=json_data.get("InstanceId"),
            Port=json_data.get("Port"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackendsDefinition = BackendsDefinition


