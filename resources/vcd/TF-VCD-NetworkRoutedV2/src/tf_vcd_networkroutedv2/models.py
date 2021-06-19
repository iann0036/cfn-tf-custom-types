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
    Description: Optional[str]
    Dns1: Optional[str]
    Dns2: Optional[str]
    DnsSuffix: Optional[str]
    EdgeGatewayId: Optional[str]
    Gateway: Optional[str]
    Id: Optional[str]
    InterfaceType: Optional[str]
    Name: Optional[str]
    Org: Optional[str]
    PrefixLength: Optional[float]
    Vdc: Optional[str]
    StaticIpPool: Optional[Sequence["_StaticIpPoolDefinition"]]

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
            Description=json_data.get("Description"),
            Dns1=json_data.get("Dns1"),
            Dns2=json_data.get("Dns2"),
            DnsSuffix=json_data.get("DnsSuffix"),
            EdgeGatewayId=json_data.get("EdgeGatewayId"),
            Gateway=json_data.get("Gateway"),
            Id=json_data.get("Id"),
            InterfaceType=json_data.get("InterfaceType"),
            Name=json_data.get("Name"),
            Org=json_data.get("Org"),
            PrefixLength=json_data.get("PrefixLength"),
            Vdc=json_data.get("Vdc"),
            StaticIpPool=deserialize_list(json_data.get("StaticIpPool"), StaticIpPoolDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class StaticIpPoolDefinition(BaseModel):
    EndAddress: Optional[str]
    StartAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StaticIpPoolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StaticIpPoolDefinition"]:
        if not json_data:
            return None
        return cls(
            EndAddress=json_data.get("EndAddress"),
            StartAddress=json_data.get("StartAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StaticIpPoolDefinition = StaticIpPoolDefinition


