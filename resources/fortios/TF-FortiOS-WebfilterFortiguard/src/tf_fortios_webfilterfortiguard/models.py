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
    CacheMemPercent: Optional[float]
    CacheMode: Optional[str]
    CachePrefixMatch: Optional[str]
    ClosePorts: Optional[str]
    Id: Optional[str]
    OvrdAuthHttps: Optional[str]
    OvrdAuthPort: Optional[float]
    OvrdAuthPortHttp: Optional[float]
    OvrdAuthPortHttps: Optional[float]
    OvrdAuthPortHttpsFlow: Optional[float]
    OvrdAuthPortWarning: Optional[float]
    RequestPacketSizeLimit: Optional[float]
    Vdomparam: Optional[str]
    WarnAuthHttps: Optional[str]

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
            CacheMemPercent=json_data.get("CacheMemPercent"),
            CacheMode=json_data.get("CacheMode"),
            CachePrefixMatch=json_data.get("CachePrefixMatch"),
            ClosePorts=json_data.get("ClosePorts"),
            Id=json_data.get("Id"),
            OvrdAuthHttps=json_data.get("OvrdAuthHttps"),
            OvrdAuthPort=json_data.get("OvrdAuthPort"),
            OvrdAuthPortHttp=json_data.get("OvrdAuthPortHttp"),
            OvrdAuthPortHttps=json_data.get("OvrdAuthPortHttps"),
            OvrdAuthPortHttpsFlow=json_data.get("OvrdAuthPortHttpsFlow"),
            OvrdAuthPortWarning=json_data.get("OvrdAuthPortWarning"),
            RequestPacketSizeLimit=json_data.get("RequestPacketSizeLimit"),
            Vdomparam=json_data.get("Vdomparam"),
            WarnAuthHttps=json_data.get("WarnAuthHttps"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


