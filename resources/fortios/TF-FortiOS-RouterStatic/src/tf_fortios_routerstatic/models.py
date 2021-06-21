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
    Bfd: Optional[str]
    Blackhole: Optional[str]
    Comment: Optional[str]
    Device: Optional[str]
    Distance: Optional[float]
    Dst: Optional[str]
    Dstaddr: Optional[str]
    DynamicGateway: Optional[str]
    Gateway: Optional[str]
    Id: Optional[str]
    InternetService: Optional[float]
    InternetServiceCustom: Optional[str]
    LinkMonitorExempt: Optional[str]
    Priority: Optional[float]
    Sdwan: Optional[str]
    SeqNum: Optional[float]
    Src: Optional[str]
    Status: Optional[str]
    Vdomparam: Optional[str]
    VirtualWanLink: Optional[str]
    Vrf: Optional[float]
    Weight: Optional[float]

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
            Bfd=json_data.get("Bfd"),
            Blackhole=json_data.get("Blackhole"),
            Comment=json_data.get("Comment"),
            Device=json_data.get("Device"),
            Distance=json_data.get("Distance"),
            Dst=json_data.get("Dst"),
            Dstaddr=json_data.get("Dstaddr"),
            DynamicGateway=json_data.get("DynamicGateway"),
            Gateway=json_data.get("Gateway"),
            Id=json_data.get("Id"),
            InternetService=json_data.get("InternetService"),
            InternetServiceCustom=json_data.get("InternetServiceCustom"),
            LinkMonitorExempt=json_data.get("LinkMonitorExempt"),
            Priority=json_data.get("Priority"),
            Sdwan=json_data.get("Sdwan"),
            SeqNum=json_data.get("SeqNum"),
            Src=json_data.get("Src"),
            Status=json_data.get("Status"),
            Vdomparam=json_data.get("Vdomparam"),
            VirtualWanLink=json_data.get("VirtualWanLink"),
            Vrf=json_data.get("Vrf"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel

