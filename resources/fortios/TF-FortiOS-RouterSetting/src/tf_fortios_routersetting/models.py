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
    BgpDebugFlags: Optional[str]
    Hostname: Optional[str]
    Id: Optional[str]
    IgmpDebugFlags: Optional[str]
    ImiDebugFlags: Optional[str]
    IsisDebugFlags: Optional[str]
    Ospf6DebugEventsFlags: Optional[str]
    Ospf6DebugIfsmFlags: Optional[str]
    Ospf6DebugLsaFlags: Optional[str]
    Ospf6DebugNfsmFlags: Optional[str]
    Ospf6DebugNsmFlags: Optional[str]
    Ospf6DebugPacketFlags: Optional[str]
    Ospf6DebugRouteFlags: Optional[str]
    OspfDebugEventsFlags: Optional[str]
    OspfDebugIfsmFlags: Optional[str]
    OspfDebugLsaFlags: Optional[str]
    OspfDebugNfsmFlags: Optional[str]
    OspfDebugNsmFlags: Optional[str]
    OspfDebugPacketFlags: Optional[str]
    OspfDebugRouteFlags: Optional[str]
    PimdmDebugFlags: Optional[str]
    PimsmDebugJoinpruneFlags: Optional[str]
    PimsmDebugSimpleFlags: Optional[str]
    PimsmDebugTimerFlags: Optional[str]
    RipDebugFlags: Optional[str]
    RipngDebugFlags: Optional[str]
    ShowFilter: Optional[str]
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
            BgpDebugFlags=json_data.get("BgpDebugFlags"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            IgmpDebugFlags=json_data.get("IgmpDebugFlags"),
            ImiDebugFlags=json_data.get("ImiDebugFlags"),
            IsisDebugFlags=json_data.get("IsisDebugFlags"),
            Ospf6DebugEventsFlags=json_data.get("Ospf6DebugEventsFlags"),
            Ospf6DebugIfsmFlags=json_data.get("Ospf6DebugIfsmFlags"),
            Ospf6DebugLsaFlags=json_data.get("Ospf6DebugLsaFlags"),
            Ospf6DebugNfsmFlags=json_data.get("Ospf6DebugNfsmFlags"),
            Ospf6DebugNsmFlags=json_data.get("Ospf6DebugNsmFlags"),
            Ospf6DebugPacketFlags=json_data.get("Ospf6DebugPacketFlags"),
            Ospf6DebugRouteFlags=json_data.get("Ospf6DebugRouteFlags"),
            OspfDebugEventsFlags=json_data.get("OspfDebugEventsFlags"),
            OspfDebugIfsmFlags=json_data.get("OspfDebugIfsmFlags"),
            OspfDebugLsaFlags=json_data.get("OspfDebugLsaFlags"),
            OspfDebugNfsmFlags=json_data.get("OspfDebugNfsmFlags"),
            OspfDebugNsmFlags=json_data.get("OspfDebugNsmFlags"),
            OspfDebugPacketFlags=json_data.get("OspfDebugPacketFlags"),
            OspfDebugRouteFlags=json_data.get("OspfDebugRouteFlags"),
            PimdmDebugFlags=json_data.get("PimdmDebugFlags"),
            PimsmDebugJoinpruneFlags=json_data.get("PimsmDebugJoinpruneFlags"),
            PimsmDebugSimpleFlags=json_data.get("PimsmDebugSimpleFlags"),
            PimsmDebugTimerFlags=json_data.get("PimsmDebugTimerFlags"),
            RipDebugFlags=json_data.get("RipDebugFlags"),
            RipngDebugFlags=json_data.get("RipngDebugFlags"),
            ShowFilter=json_data.get("ShowFilter"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


