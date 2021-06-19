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
    BackupServerEventLog: Optional[float]
    ConnRate: Optional[float]
    ConnRateDuration: Optional[float]
    ConnRateGracePeriod: Optional[float]
    ConnRateLog: Optional[float]
    ConnRateRevertDuration: Optional[float]
    ConnRevertRate: Optional[float]
    ExtendedStats: Optional[float]
    HealthCheck: Optional[str]
    HealthCheckDisable: Optional[float]
    Id: Optional[str]
    L4SessionRevertDuration: Optional[float]
    L4SessionUsage: Optional[float]
    L4SessionUsageDuration: Optional[float]
    L4SessionUsageGracePeriod: Optional[float]
    L4SessionUsageLog: Optional[float]
    L4SessionUsageRevertRate: Optional[float]
    LbMethod: Optional[str]
    LcMethod: Optional[str]
    MinActiveMember: Optional[float]
    MinActiveMemberAction: Optional[str]
    Name: Optional[str]
    PriorityAffinity: Optional[float]
    Protocol: Optional[str]
    PseudoRoundRobin: Optional[float]
    ReportDelay: Optional[float]
    ResetOnServerSelectionFail: Optional[float]
    ResetPriorityAffinity: Optional[float]
    RptExtServer: Optional[float]
    SampleRspTime: Optional[float]
    SharedPartitionPolicyTemplate: Optional[float]
    SharedPartitionSvcgrpHealthCheck: Optional[float]
    StatelessAutoSwitch: Optional[float]
    StatelessLbMethod: Optional[str]
    StatelessLbMethod2: Optional[str]
    StatsDataAction: Optional[str]
    StrictSelect: Optional[float]
    SvcgrpHealthCheckShared: Optional[str]
    TemplatePolicy: Optional[str]
    TemplatePolicyShared: Optional[str]
    TemplatePort: Optional[str]
    TemplateServer: Optional[str]
    TopFastest: Optional[float]
    TopSlowest: Optional[float]
    TrafficReplicationMirror: Optional[float]
    TrafficReplicationMirrorDaRepl: Optional[float]
    TrafficReplicationMirrorIpRepl: Optional[float]
    TrafficReplicationMirrorSaDaRepl: Optional[float]
    TrafficReplicationMirrorSaRepl: Optional[float]
    UserTag: Optional[str]
    Uuid: Optional[str]
    MemberList: Optional[Sequence["_MemberListDefinition"]]
    Priorities: Optional[Sequence["_PrioritiesDefinition"]]
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
            BackupServerEventLog=json_data.get("BackupServerEventLog"),
            ConnRate=json_data.get("ConnRate"),
            ConnRateDuration=json_data.get("ConnRateDuration"),
            ConnRateGracePeriod=json_data.get("ConnRateGracePeriod"),
            ConnRateLog=json_data.get("ConnRateLog"),
            ConnRateRevertDuration=json_data.get("ConnRateRevertDuration"),
            ConnRevertRate=json_data.get("ConnRevertRate"),
            ExtendedStats=json_data.get("ExtendedStats"),
            HealthCheck=json_data.get("HealthCheck"),
            HealthCheckDisable=json_data.get("HealthCheckDisable"),
            Id=json_data.get("Id"),
            L4SessionRevertDuration=json_data.get("L4SessionRevertDuration"),
            L4SessionUsage=json_data.get("L4SessionUsage"),
            L4SessionUsageDuration=json_data.get("L4SessionUsageDuration"),
            L4SessionUsageGracePeriod=json_data.get("L4SessionUsageGracePeriod"),
            L4SessionUsageLog=json_data.get("L4SessionUsageLog"),
            L4SessionUsageRevertRate=json_data.get("L4SessionUsageRevertRate"),
            LbMethod=json_data.get("LbMethod"),
            LcMethod=json_data.get("LcMethod"),
            MinActiveMember=json_data.get("MinActiveMember"),
            MinActiveMemberAction=json_data.get("MinActiveMemberAction"),
            Name=json_data.get("Name"),
            PriorityAffinity=json_data.get("PriorityAffinity"),
            Protocol=json_data.get("Protocol"),
            PseudoRoundRobin=json_data.get("PseudoRoundRobin"),
            ReportDelay=json_data.get("ReportDelay"),
            ResetOnServerSelectionFail=json_data.get("ResetOnServerSelectionFail"),
            ResetPriorityAffinity=json_data.get("ResetPriorityAffinity"),
            RptExtServer=json_data.get("RptExtServer"),
            SampleRspTime=json_data.get("SampleRspTime"),
            SharedPartitionPolicyTemplate=json_data.get("SharedPartitionPolicyTemplate"),
            SharedPartitionSvcgrpHealthCheck=json_data.get("SharedPartitionSvcgrpHealthCheck"),
            StatelessAutoSwitch=json_data.get("StatelessAutoSwitch"),
            StatelessLbMethod=json_data.get("StatelessLbMethod"),
            StatelessLbMethod2=json_data.get("StatelessLbMethod2"),
            StatsDataAction=json_data.get("StatsDataAction"),
            StrictSelect=json_data.get("StrictSelect"),
            SvcgrpHealthCheckShared=json_data.get("SvcgrpHealthCheckShared"),
            TemplatePolicy=json_data.get("TemplatePolicy"),
            TemplatePolicyShared=json_data.get("TemplatePolicyShared"),
            TemplatePort=json_data.get("TemplatePort"),
            TemplateServer=json_data.get("TemplateServer"),
            TopFastest=json_data.get("TopFastest"),
            TopSlowest=json_data.get("TopSlowest"),
            TrafficReplicationMirror=json_data.get("TrafficReplicationMirror"),
            TrafficReplicationMirrorDaRepl=json_data.get("TrafficReplicationMirrorDaRepl"),
            TrafficReplicationMirrorIpRepl=json_data.get("TrafficReplicationMirrorIpRepl"),
            TrafficReplicationMirrorSaDaRepl=json_data.get("TrafficReplicationMirrorSaDaRepl"),
            TrafficReplicationMirrorSaRepl=json_data.get("TrafficReplicationMirrorSaRepl"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            MemberList=deserialize_list(json_data.get("MemberList"), MemberListDefinition),
            Priorities=deserialize_list(json_data.get("Priorities"), PrioritiesDefinition),
            SamplingEnable=deserialize_list(json_data.get("SamplingEnable"), SamplingEnableDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MemberListDefinition(BaseModel):
    FqdnName: Optional[str]
    Host: Optional[str]
    MemberPriority: Optional[float]
    MemberState: Optional[str]
    MemberStatsDataDisable: Optional[float]
    MemberTemplate: Optional[str]
    Name: Optional[str]
    Port: Optional[float]
    ResolveAs: Optional[str]
    ServerIpv6Addr: Optional[str]
    UserTag: Optional[str]
    Uuid: Optional[str]
    SamplingEnable: Optional[Sequence["_SamplingEnableDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MemberListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MemberListDefinition"]:
        if not json_data:
            return None
        return cls(
            FqdnName=json_data.get("FqdnName"),
            Host=json_data.get("Host"),
            MemberPriority=json_data.get("MemberPriority"),
            MemberState=json_data.get("MemberState"),
            MemberStatsDataDisable=json_data.get("MemberStatsDataDisable"),
            MemberTemplate=json_data.get("MemberTemplate"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            ResolveAs=json_data.get("ResolveAs"),
            ServerIpv6Addr=json_data.get("ServerIpv6Addr"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            SamplingEnable=deserialize_list(json_data.get("SamplingEnable"), SamplingEnableDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MemberListDefinition = MemberListDefinition


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


@dataclass
class PrioritiesDefinition(BaseModel):
    Priority: Optional[float]
    PriorityAction: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrioritiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrioritiesDefinition"]:
        if not json_data:
            return None
        return cls(
            Priority=json_data.get("Priority"),
            PriorityAction=json_data.get("PriorityAction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrioritiesDefinition = PrioritiesDefinition


