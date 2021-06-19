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
    Id: Optional[str]
    Name: Optional[str]
    Limits: Optional[Sequence["_LimitsDefinition"]]

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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Limits=deserialize_list(json_data.get("Limits"), LimitsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LimitsDefinition(BaseModel):
    Region: Optional[str]
    RegionLimit: Optional[Sequence["_RegionLimitDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LimitsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LimitsDefinition"]:
        if not json_data:
            return None
        return cls(
            Region=json_data.get("Region"),
            RegionLimit=deserialize_list(json_data.get("RegionLimit"), RegionLimitDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LimitsDefinition = LimitsDefinition


@dataclass
class RegionLimitDefinition(BaseModel):
    Cpu: Optional[float]
    MemoryMb: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RegionLimitDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RegionLimitDefinition"]:
        if not json_data:
            return None
        return cls(
            Cpu=json_data.get("Cpu"),
            MemoryMb=json_data.get("MemoryMb"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RegionLimitDefinition = RegionLimitDefinition


