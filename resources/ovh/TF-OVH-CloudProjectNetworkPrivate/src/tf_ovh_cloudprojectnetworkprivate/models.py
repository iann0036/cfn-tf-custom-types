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
    Name: Optional[str]
    Regions: Optional[Sequence[str]]
    RegionsStatus: Optional[Sequence["_RegionsStatusDefinition"]]
    ServiceName: Optional[str]
    Status: Optional[str]
    Type: Optional[str]
    VlanId: Optional[float]

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
            Name=json_data.get("Name"),
            Regions=json_data.get("Regions"),
            RegionsStatus=deserialize_list(json_data.get("RegionsStatus"), RegionsStatusDefinition),
            ServiceName=json_data.get("ServiceName"),
            Status=json_data.get("Status"),
            Type=json_data.get("Type"),
            VlanId=json_data.get("VlanId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RegionsStatusDefinition(BaseModel):
    Region: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RegionsStatusDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RegionsStatusDefinition"]:
        if not json_data:
            return None
        return cls(
            Region=json_data.get("Region"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RegionsStatusDefinition = RegionsStatusDefinition


