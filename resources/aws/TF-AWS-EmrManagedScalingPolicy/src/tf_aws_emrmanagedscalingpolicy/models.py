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
    ClusterId: Optional[str]
    Id: Optional[str]
    ComputeLimits: Optional[Sequence["_ComputeLimitsDefinition"]]

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
            ClusterId=json_data.get("ClusterId"),
            Id=json_data.get("Id"),
            ComputeLimits=deserialize_list(json_data.get("ComputeLimits"), ComputeLimitsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ComputeLimitsDefinition(BaseModel):
    MaximumCapacityUnits: Optional[float]
    MaximumCoreCapacityUnits: Optional[float]
    MaximumOndemandCapacityUnits: Optional[float]
    MinimumCapacityUnits: Optional[float]
    UnitType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ComputeLimitsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComputeLimitsDefinition"]:
        if not json_data:
            return None
        return cls(
            MaximumCapacityUnits=json_data.get("MaximumCapacityUnits"),
            MaximumCoreCapacityUnits=json_data.get("MaximumCoreCapacityUnits"),
            MaximumOndemandCapacityUnits=json_data.get("MaximumOndemandCapacityUnits"),
            MinimumCapacityUnits=json_data.get("MinimumCapacityUnits"),
            UnitType=json_data.get("UnitType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComputeLimitsDefinition = ComputeLimitsDefinition


