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
    BwRateLimitDuration: Optional[float]
    BwRateLimitNoLogging: Optional[float]
    BwRateLimitResume: Optional[float]
    ConnLimit: Optional[float]
    ConnLimitNoLogging: Optional[float]
    ConnRateLimit: Optional[float]
    ConnRateLimitNoLogging: Optional[float]
    DampeningFlaps: Optional[float]
    Decrement: Optional[float]
    DelSessionOnServerDown: Optional[float]
    DestNat: Optional[float]
    DownGracePeriod: Optional[float]
    DownTimer: Optional[float]
    Dscp: Optional[float]
    DynamicMemberPriority: Optional[float]
    Every: Optional[float]
    ExtendedStats: Optional[float]
    FlapPeriod: Optional[float]
    HealthCheck: Optional[str]
    HealthCheckDisable: Optional[float]
    Id: Optional[str]
    InbandHealthCheck: Optional[float]
    InitialSlowStart: Optional[float]
    Name: Optional[str]
    NoSsl: Optional[float]
    RateInterval: Optional[str]
    Reassign: Optional[float]
    RequestRateInterval: Optional[str]
    RequestRateLimit: Optional[float]
    RequestRateNoLogging: Optional[float]
    ReselOnReset: Optional[float]
    Reset: Optional[float]
    RestoreSvcTime: Optional[float]
    Resume: Optional[float]
    Retry: Optional[float]
    SharedPartitionPool: Optional[float]
    SlowStart: Optional[float]
    SourceNat: Optional[str]
    StatsDataAction: Optional[str]
    SubGroup: Optional[float]
    TemplatePortPoolShared: Optional[str]
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
            BwRateLimitDuration=json_data.get("BwRateLimitDuration"),
            BwRateLimitNoLogging=json_data.get("BwRateLimitNoLogging"),
            BwRateLimitResume=json_data.get("BwRateLimitResume"),
            ConnLimit=json_data.get("ConnLimit"),
            ConnLimitNoLogging=json_data.get("ConnLimitNoLogging"),
            ConnRateLimit=json_data.get("ConnRateLimit"),
            ConnRateLimitNoLogging=json_data.get("ConnRateLimitNoLogging"),
            DampeningFlaps=json_data.get("DampeningFlaps"),
            Decrement=json_data.get("Decrement"),
            DelSessionOnServerDown=json_data.get("DelSessionOnServerDown"),
            DestNat=json_data.get("DestNat"),
            DownGracePeriod=json_data.get("DownGracePeriod"),
            DownTimer=json_data.get("DownTimer"),
            Dscp=json_data.get("Dscp"),
            DynamicMemberPriority=json_data.get("DynamicMemberPriority"),
            Every=json_data.get("Every"),
            ExtendedStats=json_data.get("ExtendedStats"),
            FlapPeriod=json_data.get("FlapPeriod"),
            HealthCheck=json_data.get("HealthCheck"),
            HealthCheckDisable=json_data.get("HealthCheckDisable"),
            Id=json_data.get("Id"),
            InbandHealthCheck=json_data.get("InbandHealthCheck"),
            InitialSlowStart=json_data.get("InitialSlowStart"),
            Name=json_data.get("Name"),
            NoSsl=json_data.get("NoSsl"),
            RateInterval=json_data.get("RateInterval"),
            Reassign=json_data.get("Reassign"),
            RequestRateInterval=json_data.get("RequestRateInterval"),
            RequestRateLimit=json_data.get("RequestRateLimit"),
            RequestRateNoLogging=json_data.get("RequestRateNoLogging"),
            ReselOnReset=json_data.get("ReselOnReset"),
            Reset=json_data.get("Reset"),
            RestoreSvcTime=json_data.get("RestoreSvcTime"),
            Resume=json_data.get("Resume"),
            Retry=json_data.get("Retry"),
            SharedPartitionPool=json_data.get("SharedPartitionPool"),
            SlowStart=json_data.get("SlowStart"),
            SourceNat=json_data.get("SourceNat"),
            StatsDataAction=json_data.get("StatsDataAction"),
            SubGroup=json_data.get("SubGroup"),
            TemplatePortPoolShared=json_data.get("TemplatePortPoolShared"),
            Till=json_data.get("Till"),
            Times=json_data.get("Times"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


