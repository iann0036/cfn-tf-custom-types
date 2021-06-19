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
    HashAlgorithm: Optional[str]
    HomeAddress: Optional[str]
    HomeAgent: Optional[str]
    Id: Optional[str]
    Lifetime: Optional[float]
    NMhaeKey: Optional[str]
    NMhaeKeyType: Optional[str]
    NMhaeSpi: Optional[float]
    Name: Optional[str]
    RegInterval: Optional[float]
    RegRetry: Optional[float]
    RenewInterval: Optional[float]
    RoamingInterface: Optional[str]
    Status: Optional[str]
    TunnelMode: Optional[str]
    Vdomparam: Optional[str]
    Network: Optional[Sequence["_NetworkDefinition"]]

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
            HashAlgorithm=json_data.get("HashAlgorithm"),
            HomeAddress=json_data.get("HomeAddress"),
            HomeAgent=json_data.get("HomeAgent"),
            Id=json_data.get("Id"),
            Lifetime=json_data.get("Lifetime"),
            NMhaeKey=json_data.get("NMhaeKey"),
            NMhaeKeyType=json_data.get("NMhaeKeyType"),
            NMhaeSpi=json_data.get("NMhaeSpi"),
            Name=json_data.get("Name"),
            RegInterval=json_data.get("RegInterval"),
            RegRetry=json_data.get("RegRetry"),
            RenewInterval=json_data.get("RenewInterval"),
            RoamingInterface=json_data.get("RoamingInterface"),
            Status=json_data.get("Status"),
            TunnelMode=json_data.get("TunnelMode"),
            Vdomparam=json_data.get("Vdomparam"),
            Network=deserialize_list(json_data.get("Network"), NetworkDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class NetworkDefinition(BaseModel):
    Id: Optional[float]
    Interface: Optional[str]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkDefinition = NetworkDefinition


