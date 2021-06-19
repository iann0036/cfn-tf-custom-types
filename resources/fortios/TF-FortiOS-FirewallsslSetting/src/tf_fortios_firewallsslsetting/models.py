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
    AbbreviateHandshake: Optional[str]
    CertCacheCapacity: Optional[float]
    CertCacheTimeout: Optional[float]
    Id: Optional[str]
    KxpQueueThreshold: Optional[float]
    NoMatchingCipherAction: Optional[str]
    ProxyConnectTimeout: Optional[float]
    SessionCacheCapacity: Optional[float]
    SessionCacheTimeout: Optional[float]
    SslDhBits: Optional[str]
    SslQueueThreshold: Optional[float]
    SslSendEmptyFrags: Optional[str]
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
            AbbreviateHandshake=json_data.get("AbbreviateHandshake"),
            CertCacheCapacity=json_data.get("CertCacheCapacity"),
            CertCacheTimeout=json_data.get("CertCacheTimeout"),
            Id=json_data.get("Id"),
            KxpQueueThreshold=json_data.get("KxpQueueThreshold"),
            NoMatchingCipherAction=json_data.get("NoMatchingCipherAction"),
            ProxyConnectTimeout=json_data.get("ProxyConnectTimeout"),
            SessionCacheCapacity=json_data.get("SessionCacheCapacity"),
            SessionCacheTimeout=json_data.get("SessionCacheTimeout"),
            SslDhBits=json_data.get("SslDhBits"),
            SslQueueThreshold=json_data.get("SslQueueThreshold"),
            SslSendEmptyFrags=json_data.get("SslSendEmptyFrags"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


