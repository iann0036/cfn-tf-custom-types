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
    ActionEmail: Optional[bool]
    ActionEmailAuthPassword: Optional[str]
    ActionEmailAuthUsername: Optional[str]
    ActionEmailBcc: Optional[str]
    ActionEmailCc: Optional[str]
    ActionEmailCommand: Optional[str]
    ActionEmailFormat: Optional[str]
    ActionEmailFrom: Optional[str]
    ActionEmailHostname: Optional[str]
    ActionEmailIncludeResultsLink: Optional[float]
    ActionEmailIncludeSearch: Optional[float]
    ActionEmailIncludeTrigger: Optional[float]
    ActionEmailIncludeTriggerTime: Optional[float]
    ActionEmailIncludeViewLink: Optional[float]
    ActionEmailInline: Optional[bool]
    ActionEmailMailserver: Optional[str]
    ActionEmailMaxResults: Optional[float]
    ActionEmailMaxTime: Optional[str]
    ActionEmailMessageAlert: Optional[str]
    ActionEmailMessageReport: Optional[str]
    ActionEmailPdfview: Optional[str]
    ActionEmailPreprocessResults: Optional[str]
    ActionEmailReportCidFontList: Optional[str]
    ActionEmailReportIncludeSplunkLogo: Optional[bool]
    ActionEmailReportPaperOrientation: Optional[str]
    ActionEmailReportPaperSize: Optional[str]
    ActionEmailReportServerEnabled: Optional[bool]
    ActionEmailReportServerUrl: Optional[str]
    ActionEmailSendCsv: Optional[float]
    ActionEmailSendPdf: Optional[bool]
    ActionEmailSendResults: Optional[bool]
    ActionEmailSubject: Optional[str]
    ActionEmailTo: Optional[str]
    ActionEmailTrackAlert: Optional[bool]
    ActionEmailTtl: Optional[str]
    ActionEmailUseSsl: Optional[bool]
    ActionEmailUseTls: Optional[bool]
    ActionEmailWidthSortColumns: Optional[bool]
    ActionPopulateLookup: Optional[bool]
    ActionPopulateLookupCommand: Optional[str]
    ActionPopulateLookupDest: Optional[str]
    ActionPopulateLookupHostname: Optional[str]
    ActionPopulateLookupMaxResults: Optional[float]
    ActionPopulateLookupMaxTime: Optional[float]
    ActionPopulateLookupTrackAlert: Optional[bool]
    ActionPopulateLookupTtl: Optional[str]
    ActionRss: Optional[bool]
    ActionRssCommand: Optional[str]
    ActionRssHostname: Optional[str]
    ActionRssMaxResults: Optional[float]
    ActionRssMaxTime: Optional[float]
    ActionRssTrackAlert: Optional[bool]
    ActionRssTtl: Optional[str]
    ActionScript: Optional[bool]
    ActionScriptCommand: Optional[str]
    ActionScriptFilename: Optional[str]
    ActionScriptHostname: Optional[str]
    ActionScriptMaxResults: Optional[float]
    ActionScriptMaxTime: Optional[float]
    ActionScriptTrackAlert: Optional[bool]
    ActionScriptTtl: Optional[str]
    ActionSlackParamAttachment: Optional[str]
    ActionSlackParamChannel: Optional[str]
    ActionSlackParamFields: Optional[str]
    ActionSlackParamMessage: Optional[str]
    ActionSlackParamWebhookUrlOverride: Optional[str]
    ActionSummaryIndex: Optional[bool]
    ActionSummaryIndexCommand: Optional[str]
    ActionSummaryIndexHostname: Optional[str]
    ActionSummaryIndexInline: Optional[bool]
    ActionSummaryIndexMaxResults: Optional[float]
    ActionSummaryIndexMaxTime: Optional[float]
    ActionSummaryIndexName: Optional[str]
    ActionSummaryIndexTrackAlert: Optional[bool]
    ActionSummaryIndexTtl: Optional[str]
    Actions: Optional[str]
    AlertComparator: Optional[str]
    AlertCondition: Optional[str]
    AlertDigestMode: Optional[bool]
    AlertExpires: Optional[str]
    AlertSeverity: Optional[float]
    AlertSuppress: Optional[bool]
    AlertSuppressFields: Optional[str]
    AlertSuppressPeriod: Optional[str]
    AlertThreshold: Optional[str]
    AlertTrack: Optional[bool]
    AlertType: Optional[str]
    AllowSkew: Optional[str]
    AutoSummarize: Optional[bool]
    AutoSummarizeCommand: Optional[str]
    AutoSummarizeCronSchedule: Optional[str]
    AutoSummarizeDispatchEarliestTime: Optional[str]
    AutoSummarizeDispatchLatestTime: Optional[str]
    AutoSummarizeDispatchTimeFormat: Optional[str]
    AutoSummarizeDispatchTtl: Optional[str]
    AutoSummarizeMaxDisabledBuckets: Optional[float]
    AutoSummarizeMaxSummaryRatio: Optional[float]
    AutoSummarizeMaxSummarySize: Optional[float]
    AutoSummarizeMaxTime: Optional[float]
    AutoSummarizeSuspendPeriod: Optional[str]
    AutoSummarizeTimespan: Optional[str]
    CronSchedule: Optional[str]
    Description: Optional[str]
    Disabled: Optional[bool]
    DispatchBuckets: Optional[float]
    DispatchEarliestTime: Optional[str]
    DispatchIndexEarliest: Optional[str]
    DispatchIndexLatest: Optional[str]
    DispatchIndexedRealtime: Optional[bool]
    DispatchIndexedRealtimeMinspan: Optional[float]
    DispatchIndexedRealtimeOffset: Optional[float]
    DispatchLatestTime: Optional[str]
    DispatchLookups: Optional[bool]
    DispatchMaxCount: Optional[float]
    DispatchMaxTime: Optional[float]
    DispatchReduceFreq: Optional[float]
    DispatchRtBackfill: Optional[bool]
    DispatchRtMaximumSpan: Optional[float]
    DispatchSpawnProcess: Optional[bool]
    DispatchTimeFormat: Optional[str]
    DispatchTtl: Optional[str]
    DisplayView: Optional[str]
    Id: Optional[str]
    IsScheduled: Optional[bool]
    IsVisible: Optional[bool]
    MaxConcurrent: Optional[float]
    Name: Optional[str]
    RealtimeSchedule: Optional[bool]
    RequestUiDispatchApp: Optional[str]
    RequestUiDispatchView: Optional[str]
    RestartOnSearchpeerAdd: Optional[bool]
    RunOnStartup: Optional[bool]
    SchedulePriority: Optional[str]
    ScheduleWindow: Optional[str]
    Search: Optional[str]
    Vsid: Optional[str]
    WorkloadPool: Optional[str]
    Acl: Optional[Sequence["_AclDefinition"]]

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
            ActionEmail=json_data.get("ActionEmail"),
            ActionEmailAuthPassword=json_data.get("ActionEmailAuthPassword"),
            ActionEmailAuthUsername=json_data.get("ActionEmailAuthUsername"),
            ActionEmailBcc=json_data.get("ActionEmailBcc"),
            ActionEmailCc=json_data.get("ActionEmailCc"),
            ActionEmailCommand=json_data.get("ActionEmailCommand"),
            ActionEmailFormat=json_data.get("ActionEmailFormat"),
            ActionEmailFrom=json_data.get("ActionEmailFrom"),
            ActionEmailHostname=json_data.get("ActionEmailHostname"),
            ActionEmailIncludeResultsLink=json_data.get("ActionEmailIncludeResultsLink"),
            ActionEmailIncludeSearch=json_data.get("ActionEmailIncludeSearch"),
            ActionEmailIncludeTrigger=json_data.get("ActionEmailIncludeTrigger"),
            ActionEmailIncludeTriggerTime=json_data.get("ActionEmailIncludeTriggerTime"),
            ActionEmailIncludeViewLink=json_data.get("ActionEmailIncludeViewLink"),
            ActionEmailInline=json_data.get("ActionEmailInline"),
            ActionEmailMailserver=json_data.get("ActionEmailMailserver"),
            ActionEmailMaxResults=json_data.get("ActionEmailMaxResults"),
            ActionEmailMaxTime=json_data.get("ActionEmailMaxTime"),
            ActionEmailMessageAlert=json_data.get("ActionEmailMessageAlert"),
            ActionEmailMessageReport=json_data.get("ActionEmailMessageReport"),
            ActionEmailPdfview=json_data.get("ActionEmailPdfview"),
            ActionEmailPreprocessResults=json_data.get("ActionEmailPreprocessResults"),
            ActionEmailReportCidFontList=json_data.get("ActionEmailReportCidFontList"),
            ActionEmailReportIncludeSplunkLogo=json_data.get("ActionEmailReportIncludeSplunkLogo"),
            ActionEmailReportPaperOrientation=json_data.get("ActionEmailReportPaperOrientation"),
            ActionEmailReportPaperSize=json_data.get("ActionEmailReportPaperSize"),
            ActionEmailReportServerEnabled=json_data.get("ActionEmailReportServerEnabled"),
            ActionEmailReportServerUrl=json_data.get("ActionEmailReportServerUrl"),
            ActionEmailSendCsv=json_data.get("ActionEmailSendCsv"),
            ActionEmailSendPdf=json_data.get("ActionEmailSendPdf"),
            ActionEmailSendResults=json_data.get("ActionEmailSendResults"),
            ActionEmailSubject=json_data.get("ActionEmailSubject"),
            ActionEmailTo=json_data.get("ActionEmailTo"),
            ActionEmailTrackAlert=json_data.get("ActionEmailTrackAlert"),
            ActionEmailTtl=json_data.get("ActionEmailTtl"),
            ActionEmailUseSsl=json_data.get("ActionEmailUseSsl"),
            ActionEmailUseTls=json_data.get("ActionEmailUseTls"),
            ActionEmailWidthSortColumns=json_data.get("ActionEmailWidthSortColumns"),
            ActionPopulateLookup=json_data.get("ActionPopulateLookup"),
            ActionPopulateLookupCommand=json_data.get("ActionPopulateLookupCommand"),
            ActionPopulateLookupDest=json_data.get("ActionPopulateLookupDest"),
            ActionPopulateLookupHostname=json_data.get("ActionPopulateLookupHostname"),
            ActionPopulateLookupMaxResults=json_data.get("ActionPopulateLookupMaxResults"),
            ActionPopulateLookupMaxTime=json_data.get("ActionPopulateLookupMaxTime"),
            ActionPopulateLookupTrackAlert=json_data.get("ActionPopulateLookupTrackAlert"),
            ActionPopulateLookupTtl=json_data.get("ActionPopulateLookupTtl"),
            ActionRss=json_data.get("ActionRss"),
            ActionRssCommand=json_data.get("ActionRssCommand"),
            ActionRssHostname=json_data.get("ActionRssHostname"),
            ActionRssMaxResults=json_data.get("ActionRssMaxResults"),
            ActionRssMaxTime=json_data.get("ActionRssMaxTime"),
            ActionRssTrackAlert=json_data.get("ActionRssTrackAlert"),
            ActionRssTtl=json_data.get("ActionRssTtl"),
            ActionScript=json_data.get("ActionScript"),
            ActionScriptCommand=json_data.get("ActionScriptCommand"),
            ActionScriptFilename=json_data.get("ActionScriptFilename"),
            ActionScriptHostname=json_data.get("ActionScriptHostname"),
            ActionScriptMaxResults=json_data.get("ActionScriptMaxResults"),
            ActionScriptMaxTime=json_data.get("ActionScriptMaxTime"),
            ActionScriptTrackAlert=json_data.get("ActionScriptTrackAlert"),
            ActionScriptTtl=json_data.get("ActionScriptTtl"),
            ActionSlackParamAttachment=json_data.get("ActionSlackParamAttachment"),
            ActionSlackParamChannel=json_data.get("ActionSlackParamChannel"),
            ActionSlackParamFields=json_data.get("ActionSlackParamFields"),
            ActionSlackParamMessage=json_data.get("ActionSlackParamMessage"),
            ActionSlackParamWebhookUrlOverride=json_data.get("ActionSlackParamWebhookUrlOverride"),
            ActionSummaryIndex=json_data.get("ActionSummaryIndex"),
            ActionSummaryIndexCommand=json_data.get("ActionSummaryIndexCommand"),
            ActionSummaryIndexHostname=json_data.get("ActionSummaryIndexHostname"),
            ActionSummaryIndexInline=json_data.get("ActionSummaryIndexInline"),
            ActionSummaryIndexMaxResults=json_data.get("ActionSummaryIndexMaxResults"),
            ActionSummaryIndexMaxTime=json_data.get("ActionSummaryIndexMaxTime"),
            ActionSummaryIndexName=json_data.get("ActionSummaryIndexName"),
            ActionSummaryIndexTrackAlert=json_data.get("ActionSummaryIndexTrackAlert"),
            ActionSummaryIndexTtl=json_data.get("ActionSummaryIndexTtl"),
            Actions=json_data.get("Actions"),
            AlertComparator=json_data.get("AlertComparator"),
            AlertCondition=json_data.get("AlertCondition"),
            AlertDigestMode=json_data.get("AlertDigestMode"),
            AlertExpires=json_data.get("AlertExpires"),
            AlertSeverity=json_data.get("AlertSeverity"),
            AlertSuppress=json_data.get("AlertSuppress"),
            AlertSuppressFields=json_data.get("AlertSuppressFields"),
            AlertSuppressPeriod=json_data.get("AlertSuppressPeriod"),
            AlertThreshold=json_data.get("AlertThreshold"),
            AlertTrack=json_data.get("AlertTrack"),
            AlertType=json_data.get("AlertType"),
            AllowSkew=json_data.get("AllowSkew"),
            AutoSummarize=json_data.get("AutoSummarize"),
            AutoSummarizeCommand=json_data.get("AutoSummarizeCommand"),
            AutoSummarizeCronSchedule=json_data.get("AutoSummarizeCronSchedule"),
            AutoSummarizeDispatchEarliestTime=json_data.get("AutoSummarizeDispatchEarliestTime"),
            AutoSummarizeDispatchLatestTime=json_data.get("AutoSummarizeDispatchLatestTime"),
            AutoSummarizeDispatchTimeFormat=json_data.get("AutoSummarizeDispatchTimeFormat"),
            AutoSummarizeDispatchTtl=json_data.get("AutoSummarizeDispatchTtl"),
            AutoSummarizeMaxDisabledBuckets=json_data.get("AutoSummarizeMaxDisabledBuckets"),
            AutoSummarizeMaxSummaryRatio=json_data.get("AutoSummarizeMaxSummaryRatio"),
            AutoSummarizeMaxSummarySize=json_data.get("AutoSummarizeMaxSummarySize"),
            AutoSummarizeMaxTime=json_data.get("AutoSummarizeMaxTime"),
            AutoSummarizeSuspendPeriod=json_data.get("AutoSummarizeSuspendPeriod"),
            AutoSummarizeTimespan=json_data.get("AutoSummarizeTimespan"),
            CronSchedule=json_data.get("CronSchedule"),
            Description=json_data.get("Description"),
            Disabled=json_data.get("Disabled"),
            DispatchBuckets=json_data.get("DispatchBuckets"),
            DispatchEarliestTime=json_data.get("DispatchEarliestTime"),
            DispatchIndexEarliest=json_data.get("DispatchIndexEarliest"),
            DispatchIndexLatest=json_data.get("DispatchIndexLatest"),
            DispatchIndexedRealtime=json_data.get("DispatchIndexedRealtime"),
            DispatchIndexedRealtimeMinspan=json_data.get("DispatchIndexedRealtimeMinspan"),
            DispatchIndexedRealtimeOffset=json_data.get("DispatchIndexedRealtimeOffset"),
            DispatchLatestTime=json_data.get("DispatchLatestTime"),
            DispatchLookups=json_data.get("DispatchLookups"),
            DispatchMaxCount=json_data.get("DispatchMaxCount"),
            DispatchMaxTime=json_data.get("DispatchMaxTime"),
            DispatchReduceFreq=json_data.get("DispatchReduceFreq"),
            DispatchRtBackfill=json_data.get("DispatchRtBackfill"),
            DispatchRtMaximumSpan=json_data.get("DispatchRtMaximumSpan"),
            DispatchSpawnProcess=json_data.get("DispatchSpawnProcess"),
            DispatchTimeFormat=json_data.get("DispatchTimeFormat"),
            DispatchTtl=json_data.get("DispatchTtl"),
            DisplayView=json_data.get("DisplayView"),
            Id=json_data.get("Id"),
            IsScheduled=json_data.get("IsScheduled"),
            IsVisible=json_data.get("IsVisible"),
            MaxConcurrent=json_data.get("MaxConcurrent"),
            Name=json_data.get("Name"),
            RealtimeSchedule=json_data.get("RealtimeSchedule"),
            RequestUiDispatchApp=json_data.get("RequestUiDispatchApp"),
            RequestUiDispatchView=json_data.get("RequestUiDispatchView"),
            RestartOnSearchpeerAdd=json_data.get("RestartOnSearchpeerAdd"),
            RunOnStartup=json_data.get("RunOnStartup"),
            SchedulePriority=json_data.get("SchedulePriority"),
            ScheduleWindow=json_data.get("ScheduleWindow"),
            Search=json_data.get("Search"),
            Vsid=json_data.get("Vsid"),
            WorkloadPool=json_data.get("WorkloadPool"),
            Acl=deserialize_list(json_data.get("Acl"), AclDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AclDefinition(BaseModel):
    App: Optional[str]
    CanChangePerms: Optional[bool]
    CanShareApp: Optional[bool]
    CanShareGlobal: Optional[bool]
    CanShareUser: Optional[bool]
    CanWrite: Optional[bool]
    Owner: Optional[str]
    Read: Optional[Sequence[str]]
    Removable: Optional[bool]
    Sharing: Optional[str]
    Write: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AclDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AclDefinition"]:
        if not json_data:
            return None
        return cls(
            App=json_data.get("App"),
            CanChangePerms=json_data.get("CanChangePerms"),
            CanShareApp=json_data.get("CanShareApp"),
            CanShareGlobal=json_data.get("CanShareGlobal"),
            CanShareUser=json_data.get("CanShareUser"),
            CanWrite=json_data.get("CanWrite"),
            Owner=json_data.get("Owner"),
            Read=json_data.get("Read"),
            Removable=json_data.get("Removable"),
            Sharing=json_data.get("Sharing"),
            Write=json_data.get("Write"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AclDefinition = AclDefinition


