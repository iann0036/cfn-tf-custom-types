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
    ConnLimit: Optional[float]
    ConnLimitNoLogging: Optional[float]
    ConnLimitReset: Optional[float]
    ConnRateLimit: Optional[float]
    ConnRateLimitNoLogging: Optional[float]
    ConnRateLimitReset: Optional[float]
    IcmpLockup: Optional[float]
    IcmpLockupPeriod: Optional[float]
    IcmpRateLimit: Optional[float]
    Icmpv6Lockup: Optional[float]
    Icmpv6LockupPeriod: Optional[float]
    Icmpv6RateLimit: Optional[float]
    Id: Optional[str]
    Name: Optional[str]
    RateInterval: Optional[str]
    SubnetGratuitousArp: Optional[float]
    TcpStackTfoActiveConnLimit: Optional[float]
    TcpStackTfoBackoffTime: Optional[float]
    TcpStackTfoCookieTimeLimit: Optional[float]
    UserTag: Optional[str]
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
            ConnLimit=json_data.get("ConnLimit"),
            ConnLimitNoLogging=json_data.get("ConnLimitNoLogging"),
            ConnLimitReset=json_data.get("ConnLimitReset"),
            ConnRateLimit=json_data.get("ConnRateLimit"),
            ConnRateLimitNoLogging=json_data.get("ConnRateLimitNoLogging"),
            ConnRateLimitReset=json_data.get("ConnRateLimitReset"),
            IcmpLockup=json_data.get("IcmpLockup"),
            IcmpLockupPeriod=json_data.get("IcmpLockupPeriod"),
            IcmpRateLimit=json_data.get("IcmpRateLimit"),
            Icmpv6Lockup=json_data.get("Icmpv6Lockup"),
            Icmpv6LockupPeriod=json_data.get("Icmpv6LockupPeriod"),
            Icmpv6RateLimit=json_data.get("Icmpv6RateLimit"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            RateInterval=json_data.get("RateInterval"),
            SubnetGratuitousArp=json_data.get("SubnetGratuitousArp"),
            TcpStackTfoActiveConnLimit=json_data.get("TcpStackTfoActiveConnLimit"),
            TcpStackTfoBackoffTime=json_data.get("TcpStackTfoBackoffTime"),
            TcpStackTfoCookieTimeLimit=json_data.get("TcpStackTfoCookieTimeLimit"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


