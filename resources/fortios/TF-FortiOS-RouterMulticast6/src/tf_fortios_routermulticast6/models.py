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
    MulticastPmtu: Optional[str]
    MulticastRouting: Optional[str]
    Vdomparam: Optional[str]
    Interface: Optional[Sequence["_InterfaceDefinition"]]
    PimSmGlobal: Optional[Sequence["_PimSmGlobalDefinition"]]

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
            MulticastPmtu=json_data.get("MulticastPmtu"),
            MulticastRouting=json_data.get("MulticastRouting"),
            Vdomparam=json_data.get("Vdomparam"),
            Interface=deserialize_list(json_data.get("Interface"), InterfaceDefinition),
            PimSmGlobal=deserialize_list(json_data.get("PimSmGlobal"), PimSmGlobalDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InterfaceDefinition(BaseModel):
    HelloHoldtime: Optional[float]
    HelloInterval: Optional[float]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InterfaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InterfaceDefinition"]:
        if not json_data:
            return None
        return cls(
            HelloHoldtime=json_data.get("HelloHoldtime"),
            HelloInterval=json_data.get("HelloInterval"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InterfaceDefinition = InterfaceDefinition


@dataclass
class PimSmGlobalDefinition(BaseModel):
    RegisterRateLimit: Optional[float]
    RpAddress: Optional[Sequence["_RpAddressDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PimSmGlobalDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PimSmGlobalDefinition"]:
        if not json_data:
            return None
        return cls(
            RegisterRateLimit=json_data.get("RegisterRateLimit"),
            RpAddress=deserialize_list(json_data.get("RpAddress"), RpAddressDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PimSmGlobalDefinition = PimSmGlobalDefinition


@dataclass
class RpAddressDefinition(BaseModel):
    Id: Optional[float]
    Ip6Address: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RpAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RpAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Ip6Address=json_data.get("Ip6Address"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RpAddressDefinition = RpAddressDefinition


