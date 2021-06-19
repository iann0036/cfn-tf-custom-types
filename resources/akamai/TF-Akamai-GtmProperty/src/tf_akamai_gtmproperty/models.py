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
    BackupCname: Optional[str]
    BackupIp: Optional[str]
    BalanceByDownloadScore: Optional[bool]
    Cname: Optional[str]
    Comments: Optional[str]
    Domain: Optional[str]
    DynamicTtl: Optional[float]
    FailbackDelay: Optional[float]
    FailoverDelay: Optional[float]
    GhostDemandReporting: Optional[bool]
    HandoutLimit: Optional[float]
    HandoutMode: Optional[str]
    HealthMax: Optional[float]
    HealthMultiplier: Optional[float]
    HealthThreshold: Optional[float]
    Id: Optional[str]
    Ipv6: Optional[bool]
    LoadImbalancePercentage: Optional[float]
    MapName: Optional[str]
    MaxUnreachablePenalty: Optional[float]
    MinLiveFraction: Optional[float]
    Name: Optional[str]
    ScoreAggregationType: Optional[str]
    StaticTtl: Optional[float]
    StickinessBonusConstant: Optional[float]
    StickinessBonusPercentage: Optional[float]
    Type: Optional[str]
    UnreachableThreshold: Optional[float]
    UseComputedTargets: Optional[bool]
    WaitOnComplete: Optional[bool]
    WeightedHashBitsForIpv4: Optional[float]
    WeightedHashBitsForIpv6: Optional[float]
    LivenessTest: Optional[Sequence["_LivenessTestDefinition"]]
    StaticRrSet: Optional[Sequence["_StaticRrSetDefinition"]]
    TrafficTarget: Optional[Sequence["_TrafficTargetDefinition"]]

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
            BackupCname=json_data.get("BackupCname"),
            BackupIp=json_data.get("BackupIp"),
            BalanceByDownloadScore=json_data.get("BalanceByDownloadScore"),
            Cname=json_data.get("Cname"),
            Comments=json_data.get("Comments"),
            Domain=json_data.get("Domain"),
            DynamicTtl=json_data.get("DynamicTtl"),
            FailbackDelay=json_data.get("FailbackDelay"),
            FailoverDelay=json_data.get("FailoverDelay"),
            GhostDemandReporting=json_data.get("GhostDemandReporting"),
            HandoutLimit=json_data.get("HandoutLimit"),
            HandoutMode=json_data.get("HandoutMode"),
            HealthMax=json_data.get("HealthMax"),
            HealthMultiplier=json_data.get("HealthMultiplier"),
            HealthThreshold=json_data.get("HealthThreshold"),
            Id=json_data.get("Id"),
            Ipv6=json_data.get("Ipv6"),
            LoadImbalancePercentage=json_data.get("LoadImbalancePercentage"),
            MapName=json_data.get("MapName"),
            MaxUnreachablePenalty=json_data.get("MaxUnreachablePenalty"),
            MinLiveFraction=json_data.get("MinLiveFraction"),
            Name=json_data.get("Name"),
            ScoreAggregationType=json_data.get("ScoreAggregationType"),
            StaticTtl=json_data.get("StaticTtl"),
            StickinessBonusConstant=json_data.get("StickinessBonusConstant"),
            StickinessBonusPercentage=json_data.get("StickinessBonusPercentage"),
            Type=json_data.get("Type"),
            UnreachableThreshold=json_data.get("UnreachableThreshold"),
            UseComputedTargets=json_data.get("UseComputedTargets"),
            WaitOnComplete=json_data.get("WaitOnComplete"),
            WeightedHashBitsForIpv4=json_data.get("WeightedHashBitsForIpv4"),
            WeightedHashBitsForIpv6=json_data.get("WeightedHashBitsForIpv6"),
            LivenessTest=deserialize_list(json_data.get("LivenessTest"), LivenessTestDefinition),
            StaticRrSet=deserialize_list(json_data.get("StaticRrSet"), StaticRrSetDefinition),
            TrafficTarget=deserialize_list(json_data.get("TrafficTarget"), TrafficTargetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LivenessTestDefinition(BaseModel):
    AnswersRequired: Optional[bool]
    DisableNonstandardPortWarning: Optional[bool]
    Disabled: Optional[bool]
    ErrorPenalty: Optional[float]
    HttpError3xx: Optional[bool]
    HttpError4xx: Optional[bool]
    HttpError5xx: Optional[bool]
    Name: Optional[str]
    PeerCertificateVerification: Optional[bool]
    RecursionRequested: Optional[bool]
    RequestString: Optional[str]
    ResourceType: Optional[str]
    ResponseString: Optional[str]
    SslClientCertificate: Optional[str]
    SslClientPrivateKey: Optional[str]
    TestInterval: Optional[float]
    TestObject: Optional[str]
    TestObjectPassword: Optional[str]
    TestObjectPort: Optional[float]
    TestObjectProtocol: Optional[str]
    TestObjectUsername: Optional[str]
    TestTimeout: Optional[float]
    TimeoutPenalty: Optional[float]
    HttpHeader: Optional[Sequence["_HttpHeaderDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LivenessTestDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LivenessTestDefinition"]:
        if not json_data:
            return None
        return cls(
            AnswersRequired=json_data.get("AnswersRequired"),
            DisableNonstandardPortWarning=json_data.get("DisableNonstandardPortWarning"),
            Disabled=json_data.get("Disabled"),
            ErrorPenalty=json_data.get("ErrorPenalty"),
            HttpError3xx=json_data.get("HttpError3xx"),
            HttpError4xx=json_data.get("HttpError4xx"),
            HttpError5xx=json_data.get("HttpError5xx"),
            Name=json_data.get("Name"),
            PeerCertificateVerification=json_data.get("PeerCertificateVerification"),
            RecursionRequested=json_data.get("RecursionRequested"),
            RequestString=json_data.get("RequestString"),
            ResourceType=json_data.get("ResourceType"),
            ResponseString=json_data.get("ResponseString"),
            SslClientCertificate=json_data.get("SslClientCertificate"),
            SslClientPrivateKey=json_data.get("SslClientPrivateKey"),
            TestInterval=json_data.get("TestInterval"),
            TestObject=json_data.get("TestObject"),
            TestObjectPassword=json_data.get("TestObjectPassword"),
            TestObjectPort=json_data.get("TestObjectPort"),
            TestObjectProtocol=json_data.get("TestObjectProtocol"),
            TestObjectUsername=json_data.get("TestObjectUsername"),
            TestTimeout=json_data.get("TestTimeout"),
            TimeoutPenalty=json_data.get("TimeoutPenalty"),
            HttpHeader=deserialize_list(json_data.get("HttpHeader"), HttpHeaderDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LivenessTestDefinition = LivenessTestDefinition


@dataclass
class HttpHeaderDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpHeaderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpHeaderDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpHeaderDefinition = HttpHeaderDefinition


@dataclass
class StaticRrSetDefinition(BaseModel):
    Rdata: Optional[Sequence[str]]
    Ttl: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StaticRrSetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StaticRrSetDefinition"]:
        if not json_data:
            return None
        return cls(
            Rdata=json_data.get("Rdata"),
            Ttl=json_data.get("Ttl"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StaticRrSetDefinition = StaticRrSetDefinition


@dataclass
class TrafficTargetDefinition(BaseModel):
    DatacenterId: Optional[float]
    Enabled: Optional[bool]
    HandoutCname: Optional[str]
    Name: Optional[str]
    Servers: Optional[Sequence[str]]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TrafficTargetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrafficTargetDefinition"]:
        if not json_data:
            return None
        return cls(
            DatacenterId=json_data.get("DatacenterId"),
            Enabled=json_data.get("Enabled"),
            HandoutCname=json_data.get("HandoutCname"),
            Name=json_data.get("Name"),
            Servers=json_data.get("Servers"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrafficTargetDefinition = TrafficTargetDefinition


