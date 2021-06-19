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
    AddrgrpLog: Optional[str]
    BleLog: Optional[str]
    ClbLog: Optional[str]
    DhcpStarvLog: Optional[str]
    Id: Optional[str]
    LedSchedLog: Optional[str]
    RadioEventLog: Optional[str]
    RogueEventLog: Optional[str]
    StaEventLog: Optional[str]
    StaLocateLog: Optional[str]
    Status: Optional[str]
    Vdomparam: Optional[str]
    WidsLog: Optional[str]
    WtpEventLog: Optional[str]

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
            AddrgrpLog=json_data.get("AddrgrpLog"),
            BleLog=json_data.get("BleLog"),
            ClbLog=json_data.get("ClbLog"),
            DhcpStarvLog=json_data.get("DhcpStarvLog"),
            Id=json_data.get("Id"),
            LedSchedLog=json_data.get("LedSchedLog"),
            RadioEventLog=json_data.get("RadioEventLog"),
            RogueEventLog=json_data.get("RogueEventLog"),
            StaEventLog=json_data.get("StaEventLog"),
            StaLocateLog=json_data.get("StaLocateLog"),
            Status=json_data.get("Status"),
            Vdomparam=json_data.get("Vdomparam"),
            WidsLog=json_data.get("WidsLog"),
            WtpEventLog=json_data.get("WtpEventLog"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


