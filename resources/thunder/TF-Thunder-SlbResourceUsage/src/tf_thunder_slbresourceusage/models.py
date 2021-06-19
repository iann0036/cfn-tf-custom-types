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
    CacheTemplateCount: Optional[float]
    ClientSslTemplateCount: Optional[float]
    ConnReuseTemplateCount: Optional[float]
    FastTcpTemplateCount: Optional[float]
    FastUdpTemplateCount: Optional[float]
    HealthMonitorCount: Optional[float]
    HttpTemplateCount: Optional[float]
    Id: Optional[str]
    NatPoolAddrCount: Optional[float]
    PbslbSubnetCount: Optional[float]
    PersistCookieTemplateCount: Optional[float]
    PersistSrcipTemplateCount: Optional[float]
    ProxyTemplateCount: Optional[float]
    RealPortCount: Optional[float]
    RealServerCount: Optional[float]
    ServerSslTemplateCount: Optional[float]
    ServiceGroupCount: Optional[float]
    SlbThresholdResUsagePercent: Optional[float]
    StreamTemplateCount: Optional[float]
    VirtualPortCount: Optional[float]
    VirtualServerCount: Optional[float]

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
            CacheTemplateCount=json_data.get("CacheTemplateCount"),
            ClientSslTemplateCount=json_data.get("ClientSslTemplateCount"),
            ConnReuseTemplateCount=json_data.get("ConnReuseTemplateCount"),
            FastTcpTemplateCount=json_data.get("FastTcpTemplateCount"),
            FastUdpTemplateCount=json_data.get("FastUdpTemplateCount"),
            HealthMonitorCount=json_data.get("HealthMonitorCount"),
            HttpTemplateCount=json_data.get("HttpTemplateCount"),
            Id=json_data.get("Id"),
            NatPoolAddrCount=json_data.get("NatPoolAddrCount"),
            PbslbSubnetCount=json_data.get("PbslbSubnetCount"),
            PersistCookieTemplateCount=json_data.get("PersistCookieTemplateCount"),
            PersistSrcipTemplateCount=json_data.get("PersistSrcipTemplateCount"),
            ProxyTemplateCount=json_data.get("ProxyTemplateCount"),
            RealPortCount=json_data.get("RealPortCount"),
            RealServerCount=json_data.get("RealServerCount"),
            ServerSslTemplateCount=json_data.get("ServerSslTemplateCount"),
            ServiceGroupCount=json_data.get("ServiceGroupCount"),
            SlbThresholdResUsagePercent=json_data.get("SlbThresholdResUsagePercent"),
            StreamTemplateCount=json_data.get("StreamTemplateCount"),
            VirtualPortCount=json_data.get("VirtualPortCount"),
            VirtualServerCount=json_data.get("VirtualServerCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


