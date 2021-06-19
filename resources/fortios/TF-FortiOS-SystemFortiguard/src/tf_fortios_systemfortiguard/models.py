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
    AntispamCache: Optional[str]
    AntispamCacheMpercent: Optional[float]
    AntispamCacheTtl: Optional[float]
    AntispamExpiration: Optional[float]
    AntispamForceOff: Optional[str]
    AntispamLicense: Optional[float]
    AntispamTimeout: Optional[float]
    AnycastSdnsServerIp: Optional[str]
    AnycastSdnsServerPort: Optional[float]
    AutoJoinForticloud: Optional[str]
    DdnsServerIp: Optional[str]
    DdnsServerPort: Optional[float]
    FortiguardAnycast: Optional[str]
    FortiguardAnycastSource: Optional[str]
    Id: Optional[str]
    Interface: Optional[str]
    InterfaceSelectMethod: Optional[str]
    LoadBalanceServers: Optional[float]
    OutbreakPreventionCache: Optional[str]
    OutbreakPreventionCacheMpercent: Optional[float]
    OutbreakPreventionCacheTtl: Optional[float]
    OutbreakPreventionExpiration: Optional[float]
    OutbreakPreventionForceOff: Optional[str]
    OutbreakPreventionLicense: Optional[float]
    OutbreakPreventionTimeout: Optional[float]
    Port: Optional[str]
    Protocol: Optional[str]
    ProxyPassword: Optional[str]
    ProxyServerIp: Optional[str]
    ProxyServerPort: Optional[float]
    ProxyUsername: Optional[str]
    SandboxRegion: Optional[str]
    SdnsOptions: Optional[str]
    SdnsServerIp: Optional[str]
    SdnsServerPort: Optional[float]
    ServiceAccountId: Optional[str]
    SourceIp: Optional[str]
    SourceIp6: Optional[str]
    UpdateServerLocation: Optional[str]
    Vdomparam: Optional[str]
    WebfilterCache: Optional[str]
    WebfilterCacheTtl: Optional[float]
    WebfilterExpiration: Optional[float]
    WebfilterForceOff: Optional[str]
    WebfilterLicense: Optional[float]
    WebfilterTimeout: Optional[float]

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
            AntispamCache=json_data.get("AntispamCache"),
            AntispamCacheMpercent=json_data.get("AntispamCacheMpercent"),
            AntispamCacheTtl=json_data.get("AntispamCacheTtl"),
            AntispamExpiration=json_data.get("AntispamExpiration"),
            AntispamForceOff=json_data.get("AntispamForceOff"),
            AntispamLicense=json_data.get("AntispamLicense"),
            AntispamTimeout=json_data.get("AntispamTimeout"),
            AnycastSdnsServerIp=json_data.get("AnycastSdnsServerIp"),
            AnycastSdnsServerPort=json_data.get("AnycastSdnsServerPort"),
            AutoJoinForticloud=json_data.get("AutoJoinForticloud"),
            DdnsServerIp=json_data.get("DdnsServerIp"),
            DdnsServerPort=json_data.get("DdnsServerPort"),
            FortiguardAnycast=json_data.get("FortiguardAnycast"),
            FortiguardAnycastSource=json_data.get("FortiguardAnycastSource"),
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
            InterfaceSelectMethod=json_data.get("InterfaceSelectMethod"),
            LoadBalanceServers=json_data.get("LoadBalanceServers"),
            OutbreakPreventionCache=json_data.get("OutbreakPreventionCache"),
            OutbreakPreventionCacheMpercent=json_data.get("OutbreakPreventionCacheMpercent"),
            OutbreakPreventionCacheTtl=json_data.get("OutbreakPreventionCacheTtl"),
            OutbreakPreventionExpiration=json_data.get("OutbreakPreventionExpiration"),
            OutbreakPreventionForceOff=json_data.get("OutbreakPreventionForceOff"),
            OutbreakPreventionLicense=json_data.get("OutbreakPreventionLicense"),
            OutbreakPreventionTimeout=json_data.get("OutbreakPreventionTimeout"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            ProxyPassword=json_data.get("ProxyPassword"),
            ProxyServerIp=json_data.get("ProxyServerIp"),
            ProxyServerPort=json_data.get("ProxyServerPort"),
            ProxyUsername=json_data.get("ProxyUsername"),
            SandboxRegion=json_data.get("SandboxRegion"),
            SdnsOptions=json_data.get("SdnsOptions"),
            SdnsServerIp=json_data.get("SdnsServerIp"),
            SdnsServerPort=json_data.get("SdnsServerPort"),
            ServiceAccountId=json_data.get("ServiceAccountId"),
            SourceIp=json_data.get("SourceIp"),
            SourceIp6=json_data.get("SourceIp6"),
            UpdateServerLocation=json_data.get("UpdateServerLocation"),
            Vdomparam=json_data.get("Vdomparam"),
            WebfilterCache=json_data.get("WebfilterCache"),
            WebfilterCacheTtl=json_data.get("WebfilterCacheTtl"),
            WebfilterExpiration=json_data.get("WebfilterExpiration"),
            WebfilterForceOff=json_data.get("WebfilterForceOff"),
            WebfilterLicense=json_data.get("WebfilterLicense"),
            WebfilterTimeout=json_data.get("WebfilterTimeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


