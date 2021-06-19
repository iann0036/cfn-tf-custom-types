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
    Action: Optional[str]
    ConnLimit: Optional[float]
    ConnResume: Optional[float]
    ExtendedStats: Optional[float]
    ExternalIp: Optional[str]
    FqdnName: Optional[str]
    HealthCheck: Optional[str]
    HealthCheckDisable: Optional[float]
    HealthCheckShared: Optional[str]
    Host: Optional[str]
    Id: Optional[str]
    Ipv6: Optional[str]
    Name: Optional[str]
    NoLogging: Optional[float]
    ResolveAs: Optional[str]
    ServerIpv6Addr: Optional[str]
    SharedPartitionHealthCheck: Optional[float]
    SlowStart: Optional[float]
    SpoofingCache: Optional[float]
    StatsDataAction: Optional[str]
    TemplateServer: Optional[str]
    UserTag: Optional[str]
    Uuid: Optional[str]
    Weight: Optional[float]
    AlternateServer: Optional[Sequence["_AlternateServerDefinition"]]
    PortList: Optional[Sequence["_PortListDefinition"]]
    SamplingEnable: Optional[Sequence["_SamplingEnableDefinition"]]

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
            Action=json_data.get("Action"),
            ConnLimit=json_data.get("ConnLimit"),
            ConnResume=json_data.get("ConnResume"),
            ExtendedStats=json_data.get("ExtendedStats"),
            ExternalIp=json_data.get("ExternalIp"),
            FqdnName=json_data.get("FqdnName"),
            HealthCheck=json_data.get("HealthCheck"),
            HealthCheckDisable=json_data.get("HealthCheckDisable"),
            HealthCheckShared=json_data.get("HealthCheckShared"),
            Host=json_data.get("Host"),
            Id=json_data.get("Id"),
            Ipv6=json_data.get("Ipv6"),
            Name=json_data.get("Name"),
            NoLogging=json_data.get("NoLogging"),
            ResolveAs=json_data.get("ResolveAs"),
            ServerIpv6Addr=json_data.get("ServerIpv6Addr"),
            SharedPartitionHealthCheck=json_data.get("SharedPartitionHealthCheck"),
            SlowStart=json_data.get("SlowStart"),
            SpoofingCache=json_data.get("SpoofingCache"),
            StatsDataAction=json_data.get("StatsDataAction"),
            TemplateServer=json_data.get("TemplateServer"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            Weight=json_data.get("Weight"),
            AlternateServer=deserialize_list(json_data.get("AlternateServer"), AlternateServerDefinition),
            PortList=deserialize_list(json_data.get("PortList"), PortListDefinition),
            SamplingEnable=deserialize_list(json_data.get("SamplingEnable"), SamplingEnableDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AlternateServerDefinition(BaseModel):
    Alternate: Optional[float]
    AlternateName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AlternateServerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlternateServerDefinition"]:
        if not json_data:
            return None
        return cls(
            Alternate=json_data.get("Alternate"),
            AlternateName=json_data.get("AlternateName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlternateServerDefinition = AlternateServerDefinition


@dataclass
class PortListDefinition(BaseModel):
    Action: Optional[str]
    ConnLimit: Optional[float]
    ConnResume: Optional[float]
    ExtendedStats: Optional[float]
    FollowPortProtocol: Optional[str]
    HealthCheck: Optional[str]
    HealthCheckDisable: Optional[float]
    HealthCheckFollowPort: Optional[float]
    NoLogging: Optional[float]
    NoSsl: Optional[float]
    PortNumber: Optional[float]
    Protocol: Optional[str]
    Range: Optional[float]
    RportHealthCheckShared: Optional[str]
    SharedRportHealthCheck: Optional[float]
    StatsDataAction: Optional[str]
    SupportHttp2: Optional[float]
    TemplatePort: Optional[str]
    TemplateServerSsl: Optional[str]
    UserTag: Optional[str]
    Uuid: Optional[str]
    Weight: Optional[float]
    AlternatePort: Optional[Sequence["_AlternatePortDefinition"]]
    SamplingEnable: Optional[Sequence["_SamplingEnableDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PortListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortListDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            ConnLimit=json_data.get("ConnLimit"),
            ConnResume=json_data.get("ConnResume"),
            ExtendedStats=json_data.get("ExtendedStats"),
            FollowPortProtocol=json_data.get("FollowPortProtocol"),
            HealthCheck=json_data.get("HealthCheck"),
            HealthCheckDisable=json_data.get("HealthCheckDisable"),
            HealthCheckFollowPort=json_data.get("HealthCheckFollowPort"),
            NoLogging=json_data.get("NoLogging"),
            NoSsl=json_data.get("NoSsl"),
            PortNumber=json_data.get("PortNumber"),
            Protocol=json_data.get("Protocol"),
            Range=json_data.get("Range"),
            RportHealthCheckShared=json_data.get("RportHealthCheckShared"),
            SharedRportHealthCheck=json_data.get("SharedRportHealthCheck"),
            StatsDataAction=json_data.get("StatsDataAction"),
            SupportHttp2=json_data.get("SupportHttp2"),
            TemplatePort=json_data.get("TemplatePort"),
            TemplateServerSsl=json_data.get("TemplateServerSsl"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            Weight=json_data.get("Weight"),
            AlternatePort=deserialize_list(json_data.get("AlternatePort"), AlternatePortDefinition),
            SamplingEnable=deserialize_list(json_data.get("SamplingEnable"), SamplingEnableDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortListDefinition = PortListDefinition


@dataclass
class AlternatePortDefinition(BaseModel):
    Alternate: Optional[float]
    AlternateName: Optional[str]
    AlternateServerPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AlternatePortDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlternatePortDefinition"]:
        if not json_data:
            return None
        return cls(
            Alternate=json_data.get("Alternate"),
            AlternateName=json_data.get("AlternateName"),
            AlternateServerPort=json_data.get("AlternateServerPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlternatePortDefinition = AlternatePortDefinition


@dataclass
class SamplingEnableDefinition(BaseModel):
    Counters1: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SamplingEnableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SamplingEnableDefinition"]:
        if not json_data:
            return None
        return cls(
            Counters1=json_data.get("Counters1"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SamplingEnableDefinition = SamplingEnableDefinition


