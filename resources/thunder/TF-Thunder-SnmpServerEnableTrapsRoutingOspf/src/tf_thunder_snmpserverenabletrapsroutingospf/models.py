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
    OspfIfAuthFailure: Optional[float]
    OspfIfConfigError: Optional[float]
    OspfIfRxBadPacket: Optional[float]
    OspfIfStateChange: Optional[float]
    OspfLsdbApproachingOverflow: Optional[float]
    OspfLsdbOverflow: Optional[float]
    OspfMaxAgeLsa: Optional[float]
    OspfNbrStateChange: Optional[float]
    OspfOriginateLsa: Optional[float]
    OspfTxRetransmit: Optional[float]
    OspfVirtIfAuthFailure: Optional[float]
    OspfVirtIfConfigError: Optional[float]
    OspfVirtIfRxBadPacket: Optional[float]
    OspfVirtIfStateChange: Optional[float]
    OspfVirtIfTxRetransmit: Optional[float]
    OspfVirtNbrStateChange: Optional[float]
    Uuid: Optional[str]

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
            OspfIfAuthFailure=json_data.get("OspfIfAuthFailure"),
            OspfIfConfigError=json_data.get("OspfIfConfigError"),
            OspfIfRxBadPacket=json_data.get("OspfIfRxBadPacket"),
            OspfIfStateChange=json_data.get("OspfIfStateChange"),
            OspfLsdbApproachingOverflow=json_data.get("OspfLsdbApproachingOverflow"),
            OspfLsdbOverflow=json_data.get("OspfLsdbOverflow"),
            OspfMaxAgeLsa=json_data.get("OspfMaxAgeLsa"),
            OspfNbrStateChange=json_data.get("OspfNbrStateChange"),
            OspfOriginateLsa=json_data.get("OspfOriginateLsa"),
            OspfTxRetransmit=json_data.get("OspfTxRetransmit"),
            OspfVirtIfAuthFailure=json_data.get("OspfVirtIfAuthFailure"),
            OspfVirtIfConfigError=json_data.get("OspfVirtIfConfigError"),
            OspfVirtIfRxBadPacket=json_data.get("OspfVirtIfRxBadPacket"),
            OspfVirtIfStateChange=json_data.get("OspfVirtIfStateChange"),
            OspfVirtIfTxRetransmit=json_data.get("OspfVirtIfTxRetransmit"),
            OspfVirtNbrStateChange=json_data.get("OspfVirtNbrStateChange"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


