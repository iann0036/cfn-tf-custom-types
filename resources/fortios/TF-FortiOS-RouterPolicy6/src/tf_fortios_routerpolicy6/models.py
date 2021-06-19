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
    Comments: Optional[str]
    Dst: Optional[str]
    EndPort: Optional[float]
    Gateway: Optional[str]
    Id: Optional[str]
    InputDevice: Optional[str]
    OutputDevice: Optional[str]
    Protocol: Optional[float]
    SeqNum: Optional[float]
    Src: Optional[str]
    StartPort: Optional[float]
    Status: Optional[str]
    Tos: Optional[str]
    TosMask: Optional[str]
    Vdomparam: Optional[str]

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
            Comments=json_data.get("Comments"),
            Dst=json_data.get("Dst"),
            EndPort=json_data.get("EndPort"),
            Gateway=json_data.get("Gateway"),
            Id=json_data.get("Id"),
            InputDevice=json_data.get("InputDevice"),
            OutputDevice=json_data.get("OutputDevice"),
            Protocol=json_data.get("Protocol"),
            SeqNum=json_data.get("SeqNum"),
            Src=json_data.get("Src"),
            StartPort=json_data.get("StartPort"),
            Status=json_data.get("Status"),
            Tos=json_data.get("Tos"),
            TosMask=json_data.get("TosMask"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


