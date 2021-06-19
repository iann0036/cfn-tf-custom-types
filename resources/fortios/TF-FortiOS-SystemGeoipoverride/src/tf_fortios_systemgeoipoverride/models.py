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
    CountryId: Optional[str]
    Description: Optional[str]
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Vdomparam: Optional[str]
    Ip6Range: Optional[Sequence["_Ip6RangeDefinition"]]
    IpRange: Optional[Sequence["_IpRangeDefinition"]]

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
            CountryId=json_data.get("CountryId"),
            Description=json_data.get("Description"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Vdomparam=json_data.get("Vdomparam"),
            Ip6Range=deserialize_list(json_data.get("Ip6Range"), Ip6RangeDefinition),
            IpRange=deserialize_list(json_data.get("IpRange"), IpRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Ip6RangeDefinition(BaseModel):
    EndIp: Optional[str]
    Id: Optional[float]
    StartIp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ip6RangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ip6RangeDefinition"]:
        if not json_data:
            return None
        return cls(
            EndIp=json_data.get("EndIp"),
            Id=json_data.get("Id"),
            StartIp=json_data.get("StartIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ip6RangeDefinition = Ip6RangeDefinition


@dataclass
class IpRangeDefinition(BaseModel):
    EndIp: Optional[str]
    Id: Optional[float]
    StartIp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            EndIp=json_data.get("EndIp"),
            Id=json_data.get("Id"),
            StartIp=json_data.get("StartIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpRangeDefinition = IpRangeDefinition


