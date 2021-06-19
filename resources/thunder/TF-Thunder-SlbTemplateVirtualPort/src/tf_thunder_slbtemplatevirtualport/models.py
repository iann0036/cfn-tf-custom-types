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
    Aflow: Optional[float]
    AllowSynOtherflags: Optional[float]
    AllowVipToRportMapping: Optional[float]
    ConnLimit: Optional[float]
    ConnLimitNoLogging: Optional[float]
    ConnLimitReset: Optional[float]
    ConnRateLimit: Optional[float]
    ConnRateLimitNoLogging: Optional[float]
    ConnRateLimitReset: Optional[float]
    DropUnknownConn: Optional[float]
    Dscp: Optional[float]
    Id: Optional[str]
    IgnoreTcpMsl: Optional[float]
    LogOptions: Optional[str]
    Name: Optional[str]
    NonSynInitiation: Optional[float]
    PktRateInterval: Optional[str]
    PktRateLimitReset: Optional[float]
    PktRateType: Optional[str]
    Rate: Optional[float]
    RateInterval: Optional[str]
    ResetL7OnFailover: Optional[float]
    ResetUnknownConn: Optional[float]
    SnatMsl: Optional[float]
    SnatPortPreserve: Optional[float]
    UserTag: Optional[str]
    Uuid: Optional[str]
    WhenRrEnable: Optional[float]

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
            Aflow=json_data.get("Aflow"),
            AllowSynOtherflags=json_data.get("AllowSynOtherflags"),
            AllowVipToRportMapping=json_data.get("AllowVipToRportMapping"),
            ConnLimit=json_data.get("ConnLimit"),
            ConnLimitNoLogging=json_data.get("ConnLimitNoLogging"),
            ConnLimitReset=json_data.get("ConnLimitReset"),
            ConnRateLimit=json_data.get("ConnRateLimit"),
            ConnRateLimitNoLogging=json_data.get("ConnRateLimitNoLogging"),
            ConnRateLimitReset=json_data.get("ConnRateLimitReset"),
            DropUnknownConn=json_data.get("DropUnknownConn"),
            Dscp=json_data.get("Dscp"),
            Id=json_data.get("Id"),
            IgnoreTcpMsl=json_data.get("IgnoreTcpMsl"),
            LogOptions=json_data.get("LogOptions"),
            Name=json_data.get("Name"),
            NonSynInitiation=json_data.get("NonSynInitiation"),
            PktRateInterval=json_data.get("PktRateInterval"),
            PktRateLimitReset=json_data.get("PktRateLimitReset"),
            PktRateType=json_data.get("PktRateType"),
            Rate=json_data.get("Rate"),
            RateInterval=json_data.get("RateInterval"),
            ResetL7OnFailover=json_data.get("ResetL7OnFailover"),
            ResetUnknownConn=json_data.get("ResetUnknownConn"),
            SnatMsl=json_data.get("SnatMsl"),
            SnatPortPreserve=json_data.get("SnatPortPreserve"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            WhenRrEnable=json_data.get("WhenRrEnable"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


