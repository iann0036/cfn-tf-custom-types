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
    Uuid: Optional[str]
    SuppressProtocols: Optional[Sequence["_SuppressProtocolsDefinition"]]

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
            Uuid=json_data.get("Uuid"),
            SuppressProtocols=deserialize_list(json_data.get("SuppressProtocols"), SuppressProtocolsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SuppressProtocolsDefinition(BaseModel):
    Connected: Optional[float]
    Ebgp: Optional[float]
    Ibgp: Optional[float]
    Isis: Optional[float]
    Ospf: Optional[float]
    Rip: Optional[float]
    Static: Optional[float]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SuppressProtocolsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SuppressProtocolsDefinition"]:
        if not json_data:
            return None
        return cls(
            Connected=json_data.get("Connected"),
            Ebgp=json_data.get("Ebgp"),
            Ibgp=json_data.get("Ibgp"),
            Isis=json_data.get("Isis"),
            Ospf=json_data.get("Ospf"),
            Rip=json_data.get("Rip"),
            Static=json_data.get("Static"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SuppressProtocolsDefinition = SuppressProtocolsDefinition


