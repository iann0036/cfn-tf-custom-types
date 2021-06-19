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
    AlwaysRevalidate: Optional[str]
    CacheByDefault: Optional[str]
    CacheCookie: Optional[str]
    CacheExpired: Optional[str]
    DefaultTtl: Optional[float]
    External: Optional[str]
    FreshFactor: Optional[float]
    HostValidate: Optional[str]
    Id: Optional[str]
    IgnoreConditional: Optional[str]
    IgnoreIeReload: Optional[str]
    IgnoreIms: Optional[str]
    IgnorePnc: Optional[str]
    MaxObjectSize: Optional[float]
    MaxTtl: Optional[float]
    MinTtl: Optional[float]
    NegRespTime: Optional[float]
    RevalPnc: Optional[str]
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
            AlwaysRevalidate=json_data.get("AlwaysRevalidate"),
            CacheByDefault=json_data.get("CacheByDefault"),
            CacheCookie=json_data.get("CacheCookie"),
            CacheExpired=json_data.get("CacheExpired"),
            DefaultTtl=json_data.get("DefaultTtl"),
            External=json_data.get("External"),
            FreshFactor=json_data.get("FreshFactor"),
            HostValidate=json_data.get("HostValidate"),
            Id=json_data.get("Id"),
            IgnoreConditional=json_data.get("IgnoreConditional"),
            IgnoreIeReload=json_data.get("IgnoreIeReload"),
            IgnoreIms=json_data.get("IgnoreIms"),
            IgnorePnc=json_data.get("IgnorePnc"),
            MaxObjectSize=json_data.get("MaxObjectSize"),
            MaxTtl=json_data.get("MaxTtl"),
            MinTtl=json_data.get("MinTtl"),
            NegRespTime=json_data.get("NegRespTime"),
            RevalPnc=json_data.get("RevalPnc"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


