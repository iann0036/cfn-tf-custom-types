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
    Asn: Optional[Sequence[float]]
    FilterRulesLimit: Optional[float]
    GeoipContinents: Optional[Sequence[str]]
    GeoipCountries: Optional[Sequence[str]]
    GeoipRegions: Optional[Sequence[str]]
    Id: Optional[str]
    Ipv4: Optional[Sequence[str]]
    Ipv6: Optional[Sequence[str]]
    Name: Optional[str]

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
            Asn=json_data.get("Asn"),
            FilterRulesLimit=json_data.get("FilterRulesLimit"),
            GeoipContinents=json_data.get("GeoipContinents"),
            GeoipCountries=json_data.get("GeoipCountries"),
            GeoipRegions=json_data.get("GeoipRegions"),
            Id=json_data.get("Id"),
            Ipv4=json_data.get("Ipv4"),
            Ipv6=json_data.get("Ipv6"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


