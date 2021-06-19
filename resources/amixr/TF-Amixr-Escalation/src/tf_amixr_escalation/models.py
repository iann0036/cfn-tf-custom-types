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
    ActionToTrigger: Optional[str]
    Duration: Optional[float]
    GroupToNotify: Optional[str]
    Id: Optional[str]
    Important: Optional[bool]
    NotifyIfTimeFrom: Optional[str]
    NotifyIfTimeTo: Optional[str]
    NotifyOnCallFromSchedule: Optional[str]
    PersonsToNotify: Optional[Sequence[str]]
    PersonsToNotifyNextEachTime: Optional[Sequence[str]]
    Position: Optional[float]
    RouteId: Optional[str]
    Type: Optional[str]

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
            ActionToTrigger=json_data.get("ActionToTrigger"),
            Duration=json_data.get("Duration"),
            GroupToNotify=json_data.get("GroupToNotify"),
            Id=json_data.get("Id"),
            Important=json_data.get("Important"),
            NotifyIfTimeFrom=json_data.get("NotifyIfTimeFrom"),
            NotifyIfTimeTo=json_data.get("NotifyIfTimeTo"),
            NotifyOnCallFromSchedule=json_data.get("NotifyOnCallFromSchedule"),
            PersonsToNotify=json_data.get("PersonsToNotify"),
            PersonsToNotifyNextEachTime=json_data.get("PersonsToNotifyNextEachTime"),
            Position=json_data.get("Position"),
            RouteId=json_data.get("RouteId"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


