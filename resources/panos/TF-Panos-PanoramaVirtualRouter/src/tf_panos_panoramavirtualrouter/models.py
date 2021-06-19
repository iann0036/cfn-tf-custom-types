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
    EbgpDist: Optional[float]
    EcmpHashSeed: Optional[float]
    EcmpHashSourceOnly: Optional[bool]
    EcmpHashUsePort: Optional[bool]
    EcmpLoadBalanceMethod: Optional[str]
    EcmpMaxPath: Optional[float]
    EcmpStrictSourcePath: Optional[bool]
    EcmpSymmetricReturn: Optional[bool]
    EcmpWeightedRoundRobinInterfaces: Optional[Sequence["_EcmpWeightedRoundRobinInterfacesDefinition"]]
    EnableEcmp: Optional[bool]
    IbgpDist: Optional[float]
    Id: Optional[str]
    Interfaces: Optional[Sequence[str]]
    Name: Optional[str]
    OspfExtDist: Optional[float]
    OspfIntDist: Optional[float]
    Ospfv3ExtDist: Optional[float]
    Ospfv3IntDist: Optional[float]
    RipDist: Optional[float]
    StaticDist: Optional[float]
    StaticIpv6Dist: Optional[float]
    Template: Optional[str]
    Vsys: Optional[str]

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
            EbgpDist=json_data.get("EbgpDist"),
            EcmpHashSeed=json_data.get("EcmpHashSeed"),
            EcmpHashSourceOnly=json_data.get("EcmpHashSourceOnly"),
            EcmpHashUsePort=json_data.get("EcmpHashUsePort"),
            EcmpLoadBalanceMethod=json_data.get("EcmpLoadBalanceMethod"),
            EcmpMaxPath=json_data.get("EcmpMaxPath"),
            EcmpStrictSourcePath=json_data.get("EcmpStrictSourcePath"),
            EcmpSymmetricReturn=json_data.get("EcmpSymmetricReturn"),
            EcmpWeightedRoundRobinInterfaces=deserialize_list(json_data.get("EcmpWeightedRoundRobinInterfaces"), EcmpWeightedRoundRobinInterfacesDefinition),
            EnableEcmp=json_data.get("EnableEcmp"),
            IbgpDist=json_data.get("IbgpDist"),
            Id=json_data.get("Id"),
            Interfaces=json_data.get("Interfaces"),
            Name=json_data.get("Name"),
            OspfExtDist=json_data.get("OspfExtDist"),
            OspfIntDist=json_data.get("OspfIntDist"),
            Ospfv3ExtDist=json_data.get("Ospfv3ExtDist"),
            Ospfv3IntDist=json_data.get("Ospfv3IntDist"),
            RipDist=json_data.get("RipDist"),
            StaticDist=json_data.get("StaticDist"),
            StaticIpv6Dist=json_data.get("StaticIpv6Dist"),
            Template=json_data.get("Template"),
            Vsys=json_data.get("Vsys"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EcmpWeightedRoundRobinInterfacesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_EcmpWeightedRoundRobinInterfacesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EcmpWeightedRoundRobinInterfacesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EcmpWeightedRoundRobinInterfacesDefinition = EcmpWeightedRoundRobinInterfacesDefinition


