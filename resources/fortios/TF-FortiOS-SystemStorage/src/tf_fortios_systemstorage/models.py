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
    Device: Optional[str]
    Id: Optional[str]
    MediaStatus: Optional[str]
    Name: Optional[str]
    Order: Optional[float]
    Partition: Optional[str]
    Size: Optional[float]
    Status: Optional[str]
    Usage: Optional[str]
    Vdomparam: Optional[str]
    WanoptMode: Optional[str]

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
            Device=json_data.get("Device"),
            Id=json_data.get("Id"),
            MediaStatus=json_data.get("MediaStatus"),
            Name=json_data.get("Name"),
            Order=json_data.get("Order"),
            Partition=json_data.get("Partition"),
            Size=json_data.get("Size"),
            Status=json_data.get("Status"),
            Usage=json_data.get("Usage"),
            Vdomparam=json_data.get("Vdomparam"),
            WanoptMode=json_data.get("WanoptMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel

