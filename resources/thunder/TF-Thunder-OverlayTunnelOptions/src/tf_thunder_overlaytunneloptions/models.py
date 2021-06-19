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
    GatewayMac: Optional[str]
    Id: Optional[str]
    IpDscpPreserve: Optional[float]
    NvgreDisableFlowId: Optional[float]
    NvgreKeyModeLower24: Optional[float]
    TcpMssAdjustDisable: Optional[float]
    Uuid: Optional[str]
    VxlanDestPort: Optional[float]

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
            GatewayMac=json_data.get("GatewayMac"),
            Id=json_data.get("Id"),
            IpDscpPreserve=json_data.get("IpDscpPreserve"),
            NvgreDisableFlowId=json_data.get("NvgreDisableFlowId"),
            NvgreKeyModeLower24=json_data.get("NvgreKeyModeLower24"),
            TcpMssAdjustDisable=json_data.get("TcpMssAdjustDisable"),
            Uuid=json_data.get("Uuid"),
            VxlanDestPort=json_data.get("VxlanDestPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


