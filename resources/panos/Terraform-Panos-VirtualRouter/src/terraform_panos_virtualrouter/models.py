# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    EbgpDist: Optional[float]
    IbgpDist: Optional[float]
    Interfaces: Optional[Sequence[str]]
    Name: Optional[str]
    OspfExtDist: Optional[float]
    OspfIntDist: Optional[float]
    Ospfv3ExtDist: Optional[float]
    Ospfv3IntDist: Optional[float]
    RipDist: Optional[float]
    StaticDist: Optional[float]
    StaticIpv6Dist: Optional[float]
    Vsys: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            EbgpDist=json_data.get("EbgpDist"),
            IbgpDist=json_data.get("IbgpDist"),
            Interfaces=json_data.get("Interfaces"),
            Name=json_data.get("Name"),
            OspfExtDist=json_data.get("OspfExtDist"),
            OspfIntDist=json_data.get("OspfIntDist"),
            Ospfv3ExtDist=json_data.get("Ospfv3ExtDist"),
            Ospfv3IntDist=json_data.get("Ospfv3IntDist"),
            RipDist=json_data.get("RipDist"),
            StaticDist=json_data.get("StaticDist"),
            StaticIpv6Dist=json_data.get("StaticIpv6Dist"),
            Vsys=json_data.get("Vsys"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


