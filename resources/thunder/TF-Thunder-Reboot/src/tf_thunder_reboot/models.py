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
    All: Optional[float]
    At: Optional[float]
    Cancel: Optional[float]
    DayOfMonth: Optional[float]
    DayOfMonth2: Optional[float]
    Device: Optional[float]
    Id: Optional[str]
    In: Optional[str]
    Month: Optional[str]
    Month2: Optional[str]
    Reason: Optional[str]
    Reason2: Optional[str]
    Reason3: Optional[str]
    Time: Optional[str]

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
            All=json_data.get("All"),
            At=json_data.get("At"),
            Cancel=json_data.get("Cancel"),
            DayOfMonth=json_data.get("DayOfMonth"),
            DayOfMonth2=json_data.get("DayOfMonth2"),
            Device=json_data.get("Device"),
            Id=json_data.get("Id"),
            In=json_data.get("In"),
            Month=json_data.get("Month"),
            Month2=json_data.get("Month2"),
            Reason=json_data.get("Reason"),
            Reason2=json_data.get("Reason2"),
            Reason3=json_data.get("Reason3"),
            Time=json_data.get("Time"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


