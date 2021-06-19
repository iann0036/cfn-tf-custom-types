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
    DeleteProtectionValidation: Optional[bool]
    Id: Optional[str]
    LoadBalancerId: Optional[str]
    Name: Optional[str]
    Servers: Optional[Sequence["_ServersDefinition"]]

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
            DeleteProtectionValidation=json_data.get("DeleteProtectionValidation"),
            Id=json_data.get("Id"),
            LoadBalancerId=json_data.get("LoadBalancerId"),
            Name=json_data.get("Name"),
            Servers=deserialize_list(json_data.get("Servers"), ServersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ServersDefinition(BaseModel):
    Port: Optional[float]
    ServerIds: Optional[Sequence[str]]
    Type: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ServersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServersDefinition"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            ServerIds=json_data.get("ServerIds"),
            Type=json_data.get("Type"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServersDefinition = ServersDefinition


