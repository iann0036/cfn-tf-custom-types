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
    ApdexResponseThreshold: Optional[float]
    ApdexResponseToleratedFactor: Optional[float]
    ApdexRttThreshold: Optional[float]
    ApdexRttToleratedFactor: Optional[float]
    ApdexRumThreshold: Optional[float]
    ApdexRumToleratedFactor: Optional[float]
    ApdexServerResponseThreshold: Optional[float]
    ApdexServerResponseToleratedFactor: Optional[float]
    ApdexServerRttThreshold: Optional[float]
    ApdexServerRttToleratedFactor: Optional[float]
    ConnLossyOooThreshold: Optional[float]
    ConnLossyTimeoRexmtThreshold: Optional[float]
    ConnLossyTotalRexmtThreshold: Optional[float]
    ConnLossyZeroWinSizeEventThreshold: Optional[float]
    ConnServerLossyOooThreshold: Optional[float]
    ConnServerLossyTimeoRexmtThreshold: Optional[float]
    ConnServerLossyTotalRexmtThreshold: Optional[float]
    ConnServerLossyZeroWinSizeEventThreshold: Optional[float]
    Description: Optional[str]
    EnableAdaptiveConfig: Optional[bool]
    EnableAdvancedAnalytics: Optional[bool]
    EnableOndemandMetrics: Optional[bool]
    EnableSeAnalytics: Optional[bool]
    EnableServerAnalytics: Optional[bool]
    EnableVsAnalytics: Optional[bool]
    ExcludeClientCloseBeforeRequestAsError: Optional[bool]
    ExcludeDnsPolicyDropAsSignificant: Optional[bool]
    ExcludeGsDownAsError: Optional[bool]
    ExcludeHttpErrorCodes: Optional[Sequence[float]]
    ExcludeInvalidDnsDomainAsError: Optional[bool]
    ExcludeInvalidDnsQueryAsError: Optional[bool]
    ExcludeIssuerRevokedOcspResponsesAsError: Optional[bool]
    ExcludeNoDnsRecordAsError: Optional[bool]
    ExcludeNoValidGsMemberAsError: Optional[bool]
    ExcludePersistenceChangeAsError: Optional[bool]
    ExcludeRevokedOcspResponsesAsError: Optional[bool]
    ExcludeServerDnsErrorAsError: Optional[bool]
    ExcludeServerTcpResetAsError: Optional[bool]
    ExcludeSipErrorCodes: Optional[Sequence[float]]
    ExcludeStaleOcspResponsesAsError: Optional[bool]
    ExcludeSynRetransmitAsError: Optional[bool]
    ExcludeTcpResetAsError: Optional[bool]
    ExcludeUnavailableOcspResponsesAsError: Optional[bool]
    ExcludeUnsupportedDnsQueryAsError: Optional[bool]
    HealthscoreMaxServerLimit: Optional[float]
    HsEventThrottleWindow: Optional[float]
    HsMaxAnomalyPenalty: Optional[float]
    HsMaxResourcesPenalty: Optional[float]
    HsMaxSecurityPenalty: Optional[float]
    HsMinDosRate: Optional[float]
    HsPerformanceBoost: Optional[float]
    HsPscoreTrafficThresholdL4Client: Optional[float]
    HsPscoreTrafficThresholdL4Server: Optional[float]
    HsSecurityCertscoreExpired: Optional[float]
    HsSecurityCertscoreGt30d: Optional[float]
    HsSecurityCertscoreLe07d: Optional[float]
    HsSecurityCertscoreLe30d: Optional[float]
    HsSecurityChainInvalidityPenalty: Optional[float]
    HsSecurityCipherscoreEq000b: Optional[float]
    HsSecurityCipherscoreGe128b: Optional[float]
    HsSecurityCipherscoreLt128b: Optional[float]
    HsSecurityEncalgoScoreNone: Optional[float]
    HsSecurityEncalgoScoreRc4: Optional[float]
    HsSecurityHstsPenalty: Optional[float]
    HsSecurityNonpfsPenalty: Optional[float]
    HsSecurityOcspRevokedScore: Optional[float]
    HsSecuritySelfsignedcertPenalty: Optional[float]
    HsSecuritySsl30Score: Optional[float]
    HsSecurityTls10Score: Optional[float]
    HsSecurityTls11Score: Optional[float]
    HsSecurityTls12Score: Optional[float]
    HsSecurityWeakSignatureAlgoPenalty: Optional[float]
    Id: Optional[str]
    Name: Optional[str]
    OndemandMetricsIdleTimeout: Optional[float]
    RespCodeBlock: Optional[Sequence[str]]
    SipLogDepth: Optional[float]
    TenantRef: Optional[str]
    Uuid: Optional[str]
    ClientLogConfig: Optional[Sequence["_ClientLogConfigDefinition"]]
    ClientLogStreamingConfig: Optional[Sequence["_ClientLogStreamingConfigDefinition"]]
    Markers: Optional[Sequence["_MarkersDefinition"]]
    Ranges: Optional[Sequence["_RangesDefinition"]]
    SensitiveLogProfile: Optional[Sequence["_SensitiveLogProfileDefinition"]]

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
            ApdexResponseThreshold=json_data.get("ApdexResponseThreshold"),
            ApdexResponseToleratedFactor=json_data.get("ApdexResponseToleratedFactor"),
            ApdexRttThreshold=json_data.get("ApdexRttThreshold"),
            ApdexRttToleratedFactor=json_data.get("ApdexRttToleratedFactor"),
            ApdexRumThreshold=json_data.get("ApdexRumThreshold"),
            ApdexRumToleratedFactor=json_data.get("ApdexRumToleratedFactor"),
            ApdexServerResponseThreshold=json_data.get("ApdexServerResponseThreshold"),
            ApdexServerResponseToleratedFactor=json_data.get("ApdexServerResponseToleratedFactor"),
            ApdexServerRttThreshold=json_data.get("ApdexServerRttThreshold"),
            ApdexServerRttToleratedFactor=json_data.get("ApdexServerRttToleratedFactor"),
            ConnLossyOooThreshold=json_data.get("ConnLossyOooThreshold"),
            ConnLossyTimeoRexmtThreshold=json_data.get("ConnLossyTimeoRexmtThreshold"),
            ConnLossyTotalRexmtThreshold=json_data.get("ConnLossyTotalRexmtThreshold"),
            ConnLossyZeroWinSizeEventThreshold=json_data.get("ConnLossyZeroWinSizeEventThreshold"),
            ConnServerLossyOooThreshold=json_data.get("ConnServerLossyOooThreshold"),
            ConnServerLossyTimeoRexmtThreshold=json_data.get("ConnServerLossyTimeoRexmtThreshold"),
            ConnServerLossyTotalRexmtThreshold=json_data.get("ConnServerLossyTotalRexmtThreshold"),
            ConnServerLossyZeroWinSizeEventThreshold=json_data.get("ConnServerLossyZeroWinSizeEventThreshold"),
            Description=json_data.get("Description"),
            EnableAdaptiveConfig=json_data.get("EnableAdaptiveConfig"),
            EnableAdvancedAnalytics=json_data.get("EnableAdvancedAnalytics"),
            EnableOndemandMetrics=json_data.get("EnableOndemandMetrics"),
            EnableSeAnalytics=json_data.get("EnableSeAnalytics"),
            EnableServerAnalytics=json_data.get("EnableServerAnalytics"),
            EnableVsAnalytics=json_data.get("EnableVsAnalytics"),
            ExcludeClientCloseBeforeRequestAsError=json_data.get("ExcludeClientCloseBeforeRequestAsError"),
            ExcludeDnsPolicyDropAsSignificant=json_data.get("ExcludeDnsPolicyDropAsSignificant"),
            ExcludeGsDownAsError=json_data.get("ExcludeGsDownAsError"),
            ExcludeHttpErrorCodes=json_data.get("ExcludeHttpErrorCodes"),
            ExcludeInvalidDnsDomainAsError=json_data.get("ExcludeInvalidDnsDomainAsError"),
            ExcludeInvalidDnsQueryAsError=json_data.get("ExcludeInvalidDnsQueryAsError"),
            ExcludeIssuerRevokedOcspResponsesAsError=json_data.get("ExcludeIssuerRevokedOcspResponsesAsError"),
            ExcludeNoDnsRecordAsError=json_data.get("ExcludeNoDnsRecordAsError"),
            ExcludeNoValidGsMemberAsError=json_data.get("ExcludeNoValidGsMemberAsError"),
            ExcludePersistenceChangeAsError=json_data.get("ExcludePersistenceChangeAsError"),
            ExcludeRevokedOcspResponsesAsError=json_data.get("ExcludeRevokedOcspResponsesAsError"),
            ExcludeServerDnsErrorAsError=json_data.get("ExcludeServerDnsErrorAsError"),
            ExcludeServerTcpResetAsError=json_data.get("ExcludeServerTcpResetAsError"),
            ExcludeSipErrorCodes=json_data.get("ExcludeSipErrorCodes"),
            ExcludeStaleOcspResponsesAsError=json_data.get("ExcludeStaleOcspResponsesAsError"),
            ExcludeSynRetransmitAsError=json_data.get("ExcludeSynRetransmitAsError"),
            ExcludeTcpResetAsError=json_data.get("ExcludeTcpResetAsError"),
            ExcludeUnavailableOcspResponsesAsError=json_data.get("ExcludeUnavailableOcspResponsesAsError"),
            ExcludeUnsupportedDnsQueryAsError=json_data.get("ExcludeUnsupportedDnsQueryAsError"),
            HealthscoreMaxServerLimit=json_data.get("HealthscoreMaxServerLimit"),
            HsEventThrottleWindow=json_data.get("HsEventThrottleWindow"),
            HsMaxAnomalyPenalty=json_data.get("HsMaxAnomalyPenalty"),
            HsMaxResourcesPenalty=json_data.get("HsMaxResourcesPenalty"),
            HsMaxSecurityPenalty=json_data.get("HsMaxSecurityPenalty"),
            HsMinDosRate=json_data.get("HsMinDosRate"),
            HsPerformanceBoost=json_data.get("HsPerformanceBoost"),
            HsPscoreTrafficThresholdL4Client=json_data.get("HsPscoreTrafficThresholdL4Client"),
            HsPscoreTrafficThresholdL4Server=json_data.get("HsPscoreTrafficThresholdL4Server"),
            HsSecurityCertscoreExpired=json_data.get("HsSecurityCertscoreExpired"),
            HsSecurityCertscoreGt30d=json_data.get("HsSecurityCertscoreGt30d"),
            HsSecurityCertscoreLe07d=json_data.get("HsSecurityCertscoreLe07d"),
            HsSecurityCertscoreLe30d=json_data.get("HsSecurityCertscoreLe30d"),
            HsSecurityChainInvalidityPenalty=json_data.get("HsSecurityChainInvalidityPenalty"),
            HsSecurityCipherscoreEq000b=json_data.get("HsSecurityCipherscoreEq000b"),
            HsSecurityCipherscoreGe128b=json_data.get("HsSecurityCipherscoreGe128b"),
            HsSecurityCipherscoreLt128b=json_data.get("HsSecurityCipherscoreLt128b"),
            HsSecurityEncalgoScoreNone=json_data.get("HsSecurityEncalgoScoreNone"),
            HsSecurityEncalgoScoreRc4=json_data.get("HsSecurityEncalgoScoreRc4"),
            HsSecurityHstsPenalty=json_data.get("HsSecurityHstsPenalty"),
            HsSecurityNonpfsPenalty=json_data.get("HsSecurityNonpfsPenalty"),
            HsSecurityOcspRevokedScore=json_data.get("HsSecurityOcspRevokedScore"),
            HsSecuritySelfsignedcertPenalty=json_data.get("HsSecuritySelfsignedcertPenalty"),
            HsSecuritySsl30Score=json_data.get("HsSecuritySsl30Score"),
            HsSecurityTls10Score=json_data.get("HsSecurityTls10Score"),
            HsSecurityTls11Score=json_data.get("HsSecurityTls11Score"),
            HsSecurityTls12Score=json_data.get("HsSecurityTls12Score"),
            HsSecurityWeakSignatureAlgoPenalty=json_data.get("HsSecurityWeakSignatureAlgoPenalty"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            OndemandMetricsIdleTimeout=json_data.get("OndemandMetricsIdleTimeout"),
            RespCodeBlock=json_data.get("RespCodeBlock"),
            SipLogDepth=json_data.get("SipLogDepth"),
            TenantRef=json_data.get("TenantRef"),
            Uuid=json_data.get("Uuid"),
            ClientLogConfig=deserialize_list(json_data.get("ClientLogConfig"), ClientLogConfigDefinition),
            ClientLogStreamingConfig=deserialize_list(json_data.get("ClientLogStreamingConfig"), ClientLogStreamingConfigDefinition),
            Markers=deserialize_list(json_data.get("Markers"), MarkersDefinition),
            Ranges=deserialize_list(json_data.get("Ranges"), RangesDefinition),
            SensitiveLogProfile=deserialize_list(json_data.get("SensitiveLogProfile"), SensitiveLogProfileDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ClientLogConfigDefinition(BaseModel):
    EnableSignificantLogCollection: Optional[bool]
    FilteredLogProcessing: Optional[str]
    NonSignificantLogProcessing: Optional[str]
    SignificantLogProcessing: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClientLogConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientLogConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            EnableSignificantLogCollection=json_data.get("EnableSignificantLogCollection"),
            FilteredLogProcessing=json_data.get("FilteredLogProcessing"),
            NonSignificantLogProcessing=json_data.get("NonSignificantLogProcessing"),
            SignificantLogProcessing=json_data.get("SignificantLogProcessing"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientLogConfigDefinition = ClientLogConfigDefinition


@dataclass
class ClientLogStreamingConfigDefinition(BaseModel):
    ExternalServer: Optional[str]
    ExternalServerPort: Optional[float]
    LogTypesToSend: Optional[str]
    MaxLogsPerSecond: Optional[float]
    Protocol: Optional[str]
    FormatConfig: Optional[Sequence["_FormatConfigDefinition"]]
    SyslogConfig: Optional[Sequence["_SyslogConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClientLogStreamingConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientLogStreamingConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ExternalServer=json_data.get("ExternalServer"),
            ExternalServerPort=json_data.get("ExternalServerPort"),
            LogTypesToSend=json_data.get("LogTypesToSend"),
            MaxLogsPerSecond=json_data.get("MaxLogsPerSecond"),
            Protocol=json_data.get("Protocol"),
            FormatConfig=deserialize_list(json_data.get("FormatConfig"), FormatConfigDefinition),
            SyslogConfig=deserialize_list(json_data.get("SyslogConfig"), SyslogConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientLogStreamingConfigDefinition = ClientLogStreamingConfigDefinition


@dataclass
class FormatConfigDefinition(BaseModel):
    Format: Optional[str]
    IncludedFields: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_FormatConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FormatConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Format=json_data.get("Format"),
            IncludedFields=json_data.get("IncludedFields"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FormatConfigDefinition = FormatConfigDefinition


@dataclass
class SyslogConfigDefinition(BaseModel):
    Facility: Optional[float]
    FilteredLogSeverity: Optional[float]
    Hostname: Optional[str]
    NonSignificantLogSeverity: Optional[float]
    SignificantLogSeverity: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SyslogConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SyslogConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Facility=json_data.get("Facility"),
            FilteredLogSeverity=json_data.get("FilteredLogSeverity"),
            Hostname=json_data.get("Hostname"),
            NonSignificantLogSeverity=json_data.get("NonSignificantLogSeverity"),
            SignificantLogSeverity=json_data.get("SignificantLogSeverity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SyslogConfigDefinition = SyslogConfigDefinition


@dataclass
class MarkersDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MarkersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MarkersDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MarkersDefinition = MarkersDefinition


@dataclass
class RangesDefinition(BaseModel):
    Begin: Optional[float]
    End: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RangesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RangesDefinition"]:
        if not json_data:
            return None
        return cls(
            Begin=json_data.get("Begin"),
            End=json_data.get("End"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RangesDefinition = RangesDefinition


@dataclass
class SensitiveLogProfileDefinition(BaseModel):
    HeaderFieldRules: Optional[Sequence["_HeaderFieldRulesDefinition"]]
    WafFieldRules: Optional[Sequence["_WafFieldRulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SensitiveLogProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SensitiveLogProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            HeaderFieldRules=deserialize_list(json_data.get("HeaderFieldRules"), HeaderFieldRulesDefinition),
            WafFieldRules=deserialize_list(json_data.get("WafFieldRules"), WafFieldRulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SensitiveLogProfileDefinition = SensitiveLogProfileDefinition


@dataclass
class HeaderFieldRulesDefinition(BaseModel):
    Action: Optional[str]
    Enabled: Optional[bool]
    Index: Optional[float]
    Name: Optional[str]
    Match: Optional[Sequence["_MatchDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderFieldRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderFieldRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Enabled=json_data.get("Enabled"),
            Index=json_data.get("Index"),
            Name=json_data.get("Name"),
            Match=deserialize_list(json_data.get("Match"), MatchDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeaderFieldRulesDefinition = HeaderFieldRulesDefinition


@dataclass
class MatchDefinition(BaseModel):
    MatchCriteria: Optional[str]
    MatchStr: Optional[Sequence[str]]
    StringGroupRefs: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchCriteria=json_data.get("MatchCriteria"),
            MatchStr=json_data.get("MatchStr"),
            StringGroupRefs=json_data.get("StringGroupRefs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchDefinition = MatchDefinition


@dataclass
class WafFieldRulesDefinition(BaseModel):
    Action: Optional[str]
    Enabled: Optional[bool]
    Index: Optional[float]
    Name: Optional[str]
    Match: Optional[Sequence["_MatchDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WafFieldRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WafFieldRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Enabled=json_data.get("Enabled"),
            Index=json_data.get("Index"),
            Name=json_data.get("Name"),
            Match=deserialize_list(json_data.get("Match"), MatchDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WafFieldRulesDefinition = WafFieldRulesDefinition


