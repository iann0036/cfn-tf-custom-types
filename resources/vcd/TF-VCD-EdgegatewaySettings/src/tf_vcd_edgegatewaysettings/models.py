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
    EdgeGatewayId: Optional[str]
    EdgeGatewayName: Optional[str]
    FwDefaultRuleAction: Optional[str]
    FwDefaultRuleLoggingEnabled: Optional[bool]
    FwEnabled: Optional[bool]
    Id: Optional[str]
    LbAccelerationEnabled: Optional[bool]
    LbEnabled: Optional[bool]
    LbLoggingEnabled: Optional[bool]
    LbLoglevel: Optional[str]
    Org: Optional[str]
    Vdc: Optional[str]

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
            EdgeGatewayId=json_data.get("EdgeGatewayId"),
            EdgeGatewayName=json_data.get("EdgeGatewayName"),
            FwDefaultRuleAction=json_data.get("FwDefaultRuleAction"),
            FwDefaultRuleLoggingEnabled=json_data.get("FwDefaultRuleLoggingEnabled"),
            FwEnabled=json_data.get("FwEnabled"),
            Id=json_data.get("Id"),
            LbAccelerationEnabled=json_data.get("LbAccelerationEnabled"),
            LbEnabled=json_data.get("LbEnabled"),
            LbLoggingEnabled=json_data.get("LbLoggingEnabled"),
            LbLoglevel=json_data.get("LbLoglevel"),
            Org=json_data.get("Org"),
            Vdc=json_data.get("Vdc"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


