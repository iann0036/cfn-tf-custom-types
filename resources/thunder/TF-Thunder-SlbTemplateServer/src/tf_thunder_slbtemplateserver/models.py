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
    Add: Optional[float]
    BwRateLimit: Optional[float]
    BwRateLimitAcct: Optional[str]
    BwRateLimitDuration: Optional[float]
    BwRateLimitNoLogging: Optional[float]
    BwRateLimitResume: Optional[float]
    ConnLimit: Optional[float]
    ConnLimitNoLogging: Optional[float]
    ConnRateLimit: Optional[float]
    ConnRateLimitNoLogging: Optional[float]
    DnsQueryInterval: Optional[float]
    DynamicServerPrefix: Optional[str]
    Every: Optional[float]
    ExtendedStats: Optional[float]
    HealthCheck: Optional[str]
    HealthCheckDisable: Optional[float]
    Id: Optional[str]
    InitialSlowStart: Optional[float]
    LogSelectionFailure: Optional[float]
    MaxDynamicServer: Optional[float]
    MinTtlRatio: Optional[float]
    Name: Optional[str]
    RateInterval: Optional[str]
    Resume: Optional[float]
    SlowStart: Optional[float]
    SpoofingCache: Optional[float]
    StatsDataAction: Optional[str]
    Till: Optional[float]
    Times: Optional[float]
    UserTag: Optional[str]
    Uuid: Optional[str]
    Weight: Optional[float]

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
            Add=json_data.get("Add"),
            BwRateLimit=json_data.get("BwRateLimit"),
            BwRateLimitAcct=json_data.get("BwRateLimitAcct"),
            BwRateLimitDuration=json_data.get("BwRateLimitDuration"),
            BwRateLimitNoLogging=json_data.get("BwRateLimitNoLogging"),
            BwRateLimitResume=json_data.get("BwRateLimitResume"),
            ConnLimit=json_data.get("ConnLimit"),
            ConnLimitNoLogging=json_data.get("ConnLimitNoLogging"),
            ConnRateLimit=json_data.get("ConnRateLimit"),
            ConnRateLimitNoLogging=json_data.get("ConnRateLimitNoLogging"),
            DnsQueryInterval=json_data.get("DnsQueryInterval"),
            DynamicServerPrefix=json_data.get("DynamicServerPrefix"),
            Every=json_data.get("Every"),
            ExtendedStats=json_data.get("ExtendedStats"),
            HealthCheck=json_data.get("HealthCheck"),
            HealthCheckDisable=json_data.get("HealthCheckDisable"),
            Id=json_data.get("Id"),
            InitialSlowStart=json_data.get("InitialSlowStart"),
            LogSelectionFailure=json_data.get("LogSelectionFailure"),
            MaxDynamicServer=json_data.get("MaxDynamicServer"),
            MinTtlRatio=json_data.get("MinTtlRatio"),
            Name=json_data.get("Name"),
            RateInterval=json_data.get("RateInterval"),
            Resume=json_data.get("Resume"),
            SlowStart=json_data.get("SlowStart"),
            SpoofingCache=json_data.get("SpoofingCache"),
            StatsDataAction=json_data.get("StatsDataAction"),
            Till=json_data.get("Till"),
            Times=json_data.get("Times"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


