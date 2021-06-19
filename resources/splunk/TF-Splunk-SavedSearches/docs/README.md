# TF::Splunk::SavedSearches

Create and manage saved searches.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Splunk::SavedSearches",
    "Properties" : {
        "<a href="#actionemailauthpassword" title="ActionEmailAuthPassword">ActionEmailAuthPassword</a>" : <i>String</i>,
        "<a href="#actionemailauthusername" title="ActionEmailAuthUsername">ActionEmailAuthUsername</a>" : <i>String</i>,
        "<a href="#actionemailbcc" title="ActionEmailBcc">ActionEmailBcc</a>" : <i>String</i>,
        "<a href="#actionemailcc" title="ActionEmailCc">ActionEmailCc</a>" : <i>String</i>,
        "<a href="#actionemailcommand" title="ActionEmailCommand">ActionEmailCommand</a>" : <i>String</i>,
        "<a href="#actionemailformat" title="ActionEmailFormat">ActionEmailFormat</a>" : <i>String</i>,
        "<a href="#actionemailfrom" title="ActionEmailFrom">ActionEmailFrom</a>" : <i>String</i>,
        "<a href="#actionemailhostname" title="ActionEmailHostname">ActionEmailHostname</a>" : <i>String</i>,
        "<a href="#actionemailincluderesultslink" title="ActionEmailIncludeResultsLink">ActionEmailIncludeResultsLink</a>" : <i>Double</i>,
        "<a href="#actionemailincludesearch" title="ActionEmailIncludeSearch">ActionEmailIncludeSearch</a>" : <i>Double</i>,
        "<a href="#actionemailincludetrigger" title="ActionEmailIncludeTrigger">ActionEmailIncludeTrigger</a>" : <i>Double</i>,
        "<a href="#actionemailincludetriggertime" title="ActionEmailIncludeTriggerTime">ActionEmailIncludeTriggerTime</a>" : <i>Double</i>,
        "<a href="#actionemailincludeviewlink" title="ActionEmailIncludeViewLink">ActionEmailIncludeViewLink</a>" : <i>Double</i>,
        "<a href="#actionemailinline" title="ActionEmailInline">ActionEmailInline</a>" : <i>Boolean</i>,
        "<a href="#actionemailmailserver" title="ActionEmailMailserver">ActionEmailMailserver</a>" : <i>String</i>,
        "<a href="#actionemailmaxresults" title="ActionEmailMaxResults">ActionEmailMaxResults</a>" : <i>Double</i>,
        "<a href="#actionemailmaxtime" title="ActionEmailMaxTime">ActionEmailMaxTime</a>" : <i>String</i>,
        "<a href="#actionemailmessagealert" title="ActionEmailMessageAlert">ActionEmailMessageAlert</a>" : <i>String</i>,
        "<a href="#actionemailmessagereport" title="ActionEmailMessageReport">ActionEmailMessageReport</a>" : <i>String</i>,
        "<a href="#actionemailpdfview" title="ActionEmailPdfview">ActionEmailPdfview</a>" : <i>String</i>,
        "<a href="#actionemailpreprocessresults" title="ActionEmailPreprocessResults">ActionEmailPreprocessResults</a>" : <i>String</i>,
        "<a href="#actionemailreportcidfontlist" title="ActionEmailReportCidFontList">ActionEmailReportCidFontList</a>" : <i>String</i>,
        "<a href="#actionemailreportincludesplunklogo" title="ActionEmailReportIncludeSplunkLogo">ActionEmailReportIncludeSplunkLogo</a>" : <i>Boolean</i>,
        "<a href="#actionemailreportpaperorientation" title="ActionEmailReportPaperOrientation">ActionEmailReportPaperOrientation</a>" : <i>String</i>,
        "<a href="#actionemailreportpapersize" title="ActionEmailReportPaperSize">ActionEmailReportPaperSize</a>" : <i>String</i>,
        "<a href="#actionemailreportserverenabled" title="ActionEmailReportServerEnabled">ActionEmailReportServerEnabled</a>" : <i>Boolean</i>,
        "<a href="#actionemailreportserverurl" title="ActionEmailReportServerUrl">ActionEmailReportServerUrl</a>" : <i>String</i>,
        "<a href="#actionemailsendcsv" title="ActionEmailSendCsv">ActionEmailSendCsv</a>" : <i>Double</i>,
        "<a href="#actionemailsendpdf" title="ActionEmailSendPdf">ActionEmailSendPdf</a>" : <i>Boolean</i>,
        "<a href="#actionemailsendresults" title="ActionEmailSendResults">ActionEmailSendResults</a>" : <i>Boolean</i>,
        "<a href="#actionemailsubject" title="ActionEmailSubject">ActionEmailSubject</a>" : <i>String</i>,
        "<a href="#actionemailto" title="ActionEmailTo">ActionEmailTo</a>" : <i>String</i>,
        "<a href="#actionemailtrackalert" title="ActionEmailTrackAlert">ActionEmailTrackAlert</a>" : <i>Boolean</i>,
        "<a href="#actionemailttl" title="ActionEmailTtl">ActionEmailTtl</a>" : <i>String</i>,
        "<a href="#actionemailusessl" title="ActionEmailUseSsl">ActionEmailUseSsl</a>" : <i>Boolean</i>,
        "<a href="#actionemailusetls" title="ActionEmailUseTls">ActionEmailUseTls</a>" : <i>Boolean</i>,
        "<a href="#actionemailwidthsortcolumns" title="ActionEmailWidthSortColumns">ActionEmailWidthSortColumns</a>" : <i>Boolean</i>,
        "<a href="#actionpopulatelookupcommand" title="ActionPopulateLookupCommand">ActionPopulateLookupCommand</a>" : <i>String</i>,
        "<a href="#actionpopulatelookupdest" title="ActionPopulateLookupDest">ActionPopulateLookupDest</a>" : <i>String</i>,
        "<a href="#actionpopulatelookuphostname" title="ActionPopulateLookupHostname">ActionPopulateLookupHostname</a>" : <i>String</i>,
        "<a href="#actionpopulatelookupmaxresults" title="ActionPopulateLookupMaxResults">ActionPopulateLookupMaxResults</a>" : <i>Double</i>,
        "<a href="#actionpopulatelookupmaxtime" title="ActionPopulateLookupMaxTime">ActionPopulateLookupMaxTime</a>" : <i>Double</i>,
        "<a href="#actionpopulatelookuptrackalert" title="ActionPopulateLookupTrackAlert">ActionPopulateLookupTrackAlert</a>" : <i>Boolean</i>,
        "<a href="#actionpopulatelookupttl" title="ActionPopulateLookupTtl">ActionPopulateLookupTtl</a>" : <i>String</i>,
        "<a href="#actionrsscommand" title="ActionRssCommand">ActionRssCommand</a>" : <i>String</i>,
        "<a href="#actionrsshostname" title="ActionRssHostname">ActionRssHostname</a>" : <i>String</i>,
        "<a href="#actionrssmaxresults" title="ActionRssMaxResults">ActionRssMaxResults</a>" : <i>Double</i>,
        "<a href="#actionrssmaxtime" title="ActionRssMaxTime">ActionRssMaxTime</a>" : <i>Double</i>,
        "<a href="#actionrsstrackalert" title="ActionRssTrackAlert">ActionRssTrackAlert</a>" : <i>Boolean</i>,
        "<a href="#actionrssttl" title="ActionRssTtl">ActionRssTtl</a>" : <i>String</i>,
        "<a href="#actionscriptcommand" title="ActionScriptCommand">ActionScriptCommand</a>" : <i>String</i>,
        "<a href="#actionscriptfilename" title="ActionScriptFilename">ActionScriptFilename</a>" : <i>String</i>,
        "<a href="#actionscripthostname" title="ActionScriptHostname">ActionScriptHostname</a>" : <i>String</i>,
        "<a href="#actionscriptmaxresults" title="ActionScriptMaxResults">ActionScriptMaxResults</a>" : <i>Double</i>,
        "<a href="#actionscriptmaxtime" title="ActionScriptMaxTime">ActionScriptMaxTime</a>" : <i>Double</i>,
        "<a href="#actionscripttrackalert" title="ActionScriptTrackAlert">ActionScriptTrackAlert</a>" : <i>Boolean</i>,
        "<a href="#actionscriptttl" title="ActionScriptTtl">ActionScriptTtl</a>" : <i>String</i>,
        "<a href="#actionslackparamattachment" title="ActionSlackParamAttachment">ActionSlackParamAttachment</a>" : <i>String</i>,
        "<a href="#actionslackparamchannel" title="ActionSlackParamChannel">ActionSlackParamChannel</a>" : <i>String</i>,
        "<a href="#actionslackparamfields" title="ActionSlackParamFields">ActionSlackParamFields</a>" : <i>String</i>,
        "<a href="#actionslackparammessage" title="ActionSlackParamMessage">ActionSlackParamMessage</a>" : <i>String</i>,
        "<a href="#actionslackparamwebhookurloverride" title="ActionSlackParamWebhookUrlOverride">ActionSlackParamWebhookUrlOverride</a>" : <i>String</i>,
        "<a href="#actionsummaryindexcommand" title="ActionSummaryIndexCommand">ActionSummaryIndexCommand</a>" : <i>String</i>,
        "<a href="#actionsummaryindexhostname" title="ActionSummaryIndexHostname">ActionSummaryIndexHostname</a>" : <i>String</i>,
        "<a href="#actionsummaryindexinline" title="ActionSummaryIndexInline">ActionSummaryIndexInline</a>" : <i>Boolean</i>,
        "<a href="#actionsummaryindexmaxresults" title="ActionSummaryIndexMaxResults">ActionSummaryIndexMaxResults</a>" : <i>Double</i>,
        "<a href="#actionsummaryindexmaxtime" title="ActionSummaryIndexMaxTime">ActionSummaryIndexMaxTime</a>" : <i>Double</i>,
        "<a href="#actionsummaryindexname" title="ActionSummaryIndexName">ActionSummaryIndexName</a>" : <i>String</i>,
        "<a href="#actionsummaryindextrackalert" title="ActionSummaryIndexTrackAlert">ActionSummaryIndexTrackAlert</a>" : <i>Boolean</i>,
        "<a href="#actionsummaryindexttl" title="ActionSummaryIndexTtl">ActionSummaryIndexTtl</a>" : <i>String</i>,
        "<a href="#actions" title="Actions">Actions</a>" : <i>String</i>,
        "<a href="#alertcomparator" title="AlertComparator">AlertComparator</a>" : <i>String</i>,
        "<a href="#alertcondition" title="AlertCondition">AlertCondition</a>" : <i>String</i>,
        "<a href="#alertdigestmode" title="AlertDigestMode">AlertDigestMode</a>" : <i>Boolean</i>,
        "<a href="#alertexpires" title="AlertExpires">AlertExpires</a>" : <i>String</i>,
        "<a href="#alertseverity" title="AlertSeverity">AlertSeverity</a>" : <i>Double</i>,
        "<a href="#alertsuppress" title="AlertSuppress">AlertSuppress</a>" : <i>Boolean</i>,
        "<a href="#alertsuppressfields" title="AlertSuppressFields">AlertSuppressFields</a>" : <i>String</i>,
        "<a href="#alertsuppressperiod" title="AlertSuppressPeriod">AlertSuppressPeriod</a>" : <i>String</i>,
        "<a href="#alertthreshold" title="AlertThreshold">AlertThreshold</a>" : <i>String</i>,
        "<a href="#alerttrack" title="AlertTrack">AlertTrack</a>" : <i>Boolean</i>,
        "<a href="#alerttype" title="AlertType">AlertType</a>" : <i>String</i>,
        "<a href="#allowskew" title="AllowSkew">AllowSkew</a>" : <i>String</i>,
        "<a href="#autosummarize" title="AutoSummarize">AutoSummarize</a>" : <i>Boolean</i>,
        "<a href="#autosummarizecommand" title="AutoSummarizeCommand">AutoSummarizeCommand</a>" : <i>String</i>,
        "<a href="#autosummarizecronschedule" title="AutoSummarizeCronSchedule">AutoSummarizeCronSchedule</a>" : <i>String</i>,
        "<a href="#autosummarizedispatchearliesttime" title="AutoSummarizeDispatchEarliestTime">AutoSummarizeDispatchEarliestTime</a>" : <i>String</i>,
        "<a href="#autosummarizedispatchlatesttime" title="AutoSummarizeDispatchLatestTime">AutoSummarizeDispatchLatestTime</a>" : <i>String</i>,
        "<a href="#autosummarizedispatchtimeformat" title="AutoSummarizeDispatchTimeFormat">AutoSummarizeDispatchTimeFormat</a>" : <i>String</i>,
        "<a href="#autosummarizedispatchttl" title="AutoSummarizeDispatchTtl">AutoSummarizeDispatchTtl</a>" : <i>String</i>,
        "<a href="#autosummarizemaxdisabledbuckets" title="AutoSummarizeMaxDisabledBuckets">AutoSummarizeMaxDisabledBuckets</a>" : <i>Double</i>,
        "<a href="#autosummarizemaxsummaryratio" title="AutoSummarizeMaxSummaryRatio">AutoSummarizeMaxSummaryRatio</a>" : <i>Double</i>,
        "<a href="#autosummarizemaxsummarysize" title="AutoSummarizeMaxSummarySize">AutoSummarizeMaxSummarySize</a>" : <i>Double</i>,
        "<a href="#autosummarizemaxtime" title="AutoSummarizeMaxTime">AutoSummarizeMaxTime</a>" : <i>Double</i>,
        "<a href="#autosummarizesuspendperiod" title="AutoSummarizeSuspendPeriod">AutoSummarizeSuspendPeriod</a>" : <i>String</i>,
        "<a href="#autosummarizetimespan" title="AutoSummarizeTimespan">AutoSummarizeTimespan</a>" : <i>String</i>,
        "<a href="#cronschedule" title="CronSchedule">CronSchedule</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#disabled" title="Disabled">Disabled</a>" : <i>Boolean</i>,
        "<a href="#dispatchbuckets" title="DispatchBuckets">DispatchBuckets</a>" : <i>Double</i>,
        "<a href="#dispatchearliesttime" title="DispatchEarliestTime">DispatchEarliestTime</a>" : <i>String</i>,
        "<a href="#dispatchindexearliest" title="DispatchIndexEarliest">DispatchIndexEarliest</a>" : <i>String</i>,
        "<a href="#dispatchindexlatest" title="DispatchIndexLatest">DispatchIndexLatest</a>" : <i>String</i>,
        "<a href="#dispatchindexedrealtime" title="DispatchIndexedRealtime">DispatchIndexedRealtime</a>" : <i>Boolean</i>,
        "<a href="#dispatchindexedrealtimeminspan" title="DispatchIndexedRealtimeMinspan">DispatchIndexedRealtimeMinspan</a>" : <i>Double</i>,
        "<a href="#dispatchindexedrealtimeoffset" title="DispatchIndexedRealtimeOffset">DispatchIndexedRealtimeOffset</a>" : <i>Double</i>,
        "<a href="#dispatchlatesttime" title="DispatchLatestTime">DispatchLatestTime</a>" : <i>String</i>,
        "<a href="#dispatchlookups" title="DispatchLookups">DispatchLookups</a>" : <i>Boolean</i>,
        "<a href="#dispatchmaxcount" title="DispatchMaxCount">DispatchMaxCount</a>" : <i>Double</i>,
        "<a href="#dispatchmaxtime" title="DispatchMaxTime">DispatchMaxTime</a>" : <i>Double</i>,
        "<a href="#dispatchreducefreq" title="DispatchReduceFreq">DispatchReduceFreq</a>" : <i>Double</i>,
        "<a href="#dispatchrtbackfill" title="DispatchRtBackfill">DispatchRtBackfill</a>" : <i>Boolean</i>,
        "<a href="#dispatchrtmaximumspan" title="DispatchRtMaximumSpan">DispatchRtMaximumSpan</a>" : <i>Double</i>,
        "<a href="#dispatchspawnprocess" title="DispatchSpawnProcess">DispatchSpawnProcess</a>" : <i>Boolean</i>,
        "<a href="#dispatchtimeformat" title="DispatchTimeFormat">DispatchTimeFormat</a>" : <i>String</i>,
        "<a href="#dispatchttl" title="DispatchTtl">DispatchTtl</a>" : <i>String</i>,
        "<a href="#displayview" title="DisplayView">DisplayView</a>" : <i>String</i>,
        "<a href="#isscheduled" title="IsScheduled">IsScheduled</a>" : <i>Boolean</i>,
        "<a href="#isvisible" title="IsVisible">IsVisible</a>" : <i>Boolean</i>,
        "<a href="#maxconcurrent" title="MaxConcurrent">MaxConcurrent</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#realtimeschedule" title="RealtimeSchedule">RealtimeSchedule</a>" : <i>Boolean</i>,
        "<a href="#requestuidispatchapp" title="RequestUiDispatchApp">RequestUiDispatchApp</a>" : <i>String</i>,
        "<a href="#requestuidispatchview" title="RequestUiDispatchView">RequestUiDispatchView</a>" : <i>String</i>,
        "<a href="#restartonsearchpeeradd" title="RestartOnSearchpeerAdd">RestartOnSearchpeerAdd</a>" : <i>Boolean</i>,
        "<a href="#runonstartup" title="RunOnStartup">RunOnStartup</a>" : <i>Boolean</i>,
        "<a href="#schedulepriority" title="SchedulePriority">SchedulePriority</a>" : <i>String</i>,
        "<a href="#schedulewindow" title="ScheduleWindow">ScheduleWindow</a>" : <i>String</i>,
        "<a href="#search" title="Search">Search</a>" : <i>String</i>,
        "<a href="#vsid" title="Vsid">Vsid</a>" : <i>String</i>,
        "<a href="#workloadpool" title="WorkloadPool">WorkloadPool</a>" : <i>String</i>,
        "<a href="#acl" title="Acl">Acl</a>" : <i>[ <a href="acldefinition.md">AclDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Splunk::SavedSearches
Properties:
    <a href="#actionemailauthpassword" title="ActionEmailAuthPassword">ActionEmailAuthPassword</a>: <i>String</i>
    <a href="#actionemailauthusername" title="ActionEmailAuthUsername">ActionEmailAuthUsername</a>: <i>String</i>
    <a href="#actionemailbcc" title="ActionEmailBcc">ActionEmailBcc</a>: <i>String</i>
    <a href="#actionemailcc" title="ActionEmailCc">ActionEmailCc</a>: <i>String</i>
    <a href="#actionemailcommand" title="ActionEmailCommand">ActionEmailCommand</a>: <i>String</i>
    <a href="#actionemailformat" title="ActionEmailFormat">ActionEmailFormat</a>: <i>String</i>
    <a href="#actionemailfrom" title="ActionEmailFrom">ActionEmailFrom</a>: <i>String</i>
    <a href="#actionemailhostname" title="ActionEmailHostname">ActionEmailHostname</a>: <i>String</i>
    <a href="#actionemailincluderesultslink" title="ActionEmailIncludeResultsLink">ActionEmailIncludeResultsLink</a>: <i>Double</i>
    <a href="#actionemailincludesearch" title="ActionEmailIncludeSearch">ActionEmailIncludeSearch</a>: <i>Double</i>
    <a href="#actionemailincludetrigger" title="ActionEmailIncludeTrigger">ActionEmailIncludeTrigger</a>: <i>Double</i>
    <a href="#actionemailincludetriggertime" title="ActionEmailIncludeTriggerTime">ActionEmailIncludeTriggerTime</a>: <i>Double</i>
    <a href="#actionemailincludeviewlink" title="ActionEmailIncludeViewLink">ActionEmailIncludeViewLink</a>: <i>Double</i>
    <a href="#actionemailinline" title="ActionEmailInline">ActionEmailInline</a>: <i>Boolean</i>
    <a href="#actionemailmailserver" title="ActionEmailMailserver">ActionEmailMailserver</a>: <i>String</i>
    <a href="#actionemailmaxresults" title="ActionEmailMaxResults">ActionEmailMaxResults</a>: <i>Double</i>
    <a href="#actionemailmaxtime" title="ActionEmailMaxTime">ActionEmailMaxTime</a>: <i>String</i>
    <a href="#actionemailmessagealert" title="ActionEmailMessageAlert">ActionEmailMessageAlert</a>: <i>String</i>
    <a href="#actionemailmessagereport" title="ActionEmailMessageReport">ActionEmailMessageReport</a>: <i>String</i>
    <a href="#actionemailpdfview" title="ActionEmailPdfview">ActionEmailPdfview</a>: <i>String</i>
    <a href="#actionemailpreprocessresults" title="ActionEmailPreprocessResults">ActionEmailPreprocessResults</a>: <i>String</i>
    <a href="#actionemailreportcidfontlist" title="ActionEmailReportCidFontList">ActionEmailReportCidFontList</a>: <i>String</i>
    <a href="#actionemailreportincludesplunklogo" title="ActionEmailReportIncludeSplunkLogo">ActionEmailReportIncludeSplunkLogo</a>: <i>Boolean</i>
    <a href="#actionemailreportpaperorientation" title="ActionEmailReportPaperOrientation">ActionEmailReportPaperOrientation</a>: <i>String</i>
    <a href="#actionemailreportpapersize" title="ActionEmailReportPaperSize">ActionEmailReportPaperSize</a>: <i>String</i>
    <a href="#actionemailreportserverenabled" title="ActionEmailReportServerEnabled">ActionEmailReportServerEnabled</a>: <i>Boolean</i>
    <a href="#actionemailreportserverurl" title="ActionEmailReportServerUrl">ActionEmailReportServerUrl</a>: <i>String</i>
    <a href="#actionemailsendcsv" title="ActionEmailSendCsv">ActionEmailSendCsv</a>: <i>Double</i>
    <a href="#actionemailsendpdf" title="ActionEmailSendPdf">ActionEmailSendPdf</a>: <i>Boolean</i>
    <a href="#actionemailsendresults" title="ActionEmailSendResults">ActionEmailSendResults</a>: <i>Boolean</i>
    <a href="#actionemailsubject" title="ActionEmailSubject">ActionEmailSubject</a>: <i>String</i>
    <a href="#actionemailto" title="ActionEmailTo">ActionEmailTo</a>: <i>String</i>
    <a href="#actionemailtrackalert" title="ActionEmailTrackAlert">ActionEmailTrackAlert</a>: <i>Boolean</i>
    <a href="#actionemailttl" title="ActionEmailTtl">ActionEmailTtl</a>: <i>String</i>
    <a href="#actionemailusessl" title="ActionEmailUseSsl">ActionEmailUseSsl</a>: <i>Boolean</i>
    <a href="#actionemailusetls" title="ActionEmailUseTls">ActionEmailUseTls</a>: <i>Boolean</i>
    <a href="#actionemailwidthsortcolumns" title="ActionEmailWidthSortColumns">ActionEmailWidthSortColumns</a>: <i>Boolean</i>
    <a href="#actionpopulatelookupcommand" title="ActionPopulateLookupCommand">ActionPopulateLookupCommand</a>: <i>String</i>
    <a href="#actionpopulatelookupdest" title="ActionPopulateLookupDest">ActionPopulateLookupDest</a>: <i>String</i>
    <a href="#actionpopulatelookuphostname" title="ActionPopulateLookupHostname">ActionPopulateLookupHostname</a>: <i>String</i>
    <a href="#actionpopulatelookupmaxresults" title="ActionPopulateLookupMaxResults">ActionPopulateLookupMaxResults</a>: <i>Double</i>
    <a href="#actionpopulatelookupmaxtime" title="ActionPopulateLookupMaxTime">ActionPopulateLookupMaxTime</a>: <i>Double</i>
    <a href="#actionpopulatelookuptrackalert" title="ActionPopulateLookupTrackAlert">ActionPopulateLookupTrackAlert</a>: <i>Boolean</i>
    <a href="#actionpopulatelookupttl" title="ActionPopulateLookupTtl">ActionPopulateLookupTtl</a>: <i>String</i>
    <a href="#actionrsscommand" title="ActionRssCommand">ActionRssCommand</a>: <i>String</i>
    <a href="#actionrsshostname" title="ActionRssHostname">ActionRssHostname</a>: <i>String</i>
    <a href="#actionrssmaxresults" title="ActionRssMaxResults">ActionRssMaxResults</a>: <i>Double</i>
    <a href="#actionrssmaxtime" title="ActionRssMaxTime">ActionRssMaxTime</a>: <i>Double</i>
    <a href="#actionrsstrackalert" title="ActionRssTrackAlert">ActionRssTrackAlert</a>: <i>Boolean</i>
    <a href="#actionrssttl" title="ActionRssTtl">ActionRssTtl</a>: <i>String</i>
    <a href="#actionscriptcommand" title="ActionScriptCommand">ActionScriptCommand</a>: <i>String</i>
    <a href="#actionscriptfilename" title="ActionScriptFilename">ActionScriptFilename</a>: <i>String</i>
    <a href="#actionscripthostname" title="ActionScriptHostname">ActionScriptHostname</a>: <i>String</i>
    <a href="#actionscriptmaxresults" title="ActionScriptMaxResults">ActionScriptMaxResults</a>: <i>Double</i>
    <a href="#actionscriptmaxtime" title="ActionScriptMaxTime">ActionScriptMaxTime</a>: <i>Double</i>
    <a href="#actionscripttrackalert" title="ActionScriptTrackAlert">ActionScriptTrackAlert</a>: <i>Boolean</i>
    <a href="#actionscriptttl" title="ActionScriptTtl">ActionScriptTtl</a>: <i>String</i>
    <a href="#actionslackparamattachment" title="ActionSlackParamAttachment">ActionSlackParamAttachment</a>: <i>String</i>
    <a href="#actionslackparamchannel" title="ActionSlackParamChannel">ActionSlackParamChannel</a>: <i>String</i>
    <a href="#actionslackparamfields" title="ActionSlackParamFields">ActionSlackParamFields</a>: <i>String</i>
    <a href="#actionslackparammessage" title="ActionSlackParamMessage">ActionSlackParamMessage</a>: <i>String</i>
    <a href="#actionslackparamwebhookurloverride" title="ActionSlackParamWebhookUrlOverride">ActionSlackParamWebhookUrlOverride</a>: <i>String</i>
    <a href="#actionsummaryindexcommand" title="ActionSummaryIndexCommand">ActionSummaryIndexCommand</a>: <i>String</i>
    <a href="#actionsummaryindexhostname" title="ActionSummaryIndexHostname">ActionSummaryIndexHostname</a>: <i>String</i>
    <a href="#actionsummaryindexinline" title="ActionSummaryIndexInline">ActionSummaryIndexInline</a>: <i>Boolean</i>
    <a href="#actionsummaryindexmaxresults" title="ActionSummaryIndexMaxResults">ActionSummaryIndexMaxResults</a>: <i>Double</i>
    <a href="#actionsummaryindexmaxtime" title="ActionSummaryIndexMaxTime">ActionSummaryIndexMaxTime</a>: <i>Double</i>
    <a href="#actionsummaryindexname" title="ActionSummaryIndexName">ActionSummaryIndexName</a>: <i>String</i>
    <a href="#actionsummaryindextrackalert" title="ActionSummaryIndexTrackAlert">ActionSummaryIndexTrackAlert</a>: <i>Boolean</i>
    <a href="#actionsummaryindexttl" title="ActionSummaryIndexTtl">ActionSummaryIndexTtl</a>: <i>String</i>
    <a href="#actions" title="Actions">Actions</a>: <i>String</i>
    <a href="#alertcomparator" title="AlertComparator">AlertComparator</a>: <i>String</i>
    <a href="#alertcondition" title="AlertCondition">AlertCondition</a>: <i>String</i>
    <a href="#alertdigestmode" title="AlertDigestMode">AlertDigestMode</a>: <i>Boolean</i>
    <a href="#alertexpires" title="AlertExpires">AlertExpires</a>: <i>String</i>
    <a href="#alertseverity" title="AlertSeverity">AlertSeverity</a>: <i>Double</i>
    <a href="#alertsuppress" title="AlertSuppress">AlertSuppress</a>: <i>Boolean</i>
    <a href="#alertsuppressfields" title="AlertSuppressFields">AlertSuppressFields</a>: <i>String</i>
    <a href="#alertsuppressperiod" title="AlertSuppressPeriod">AlertSuppressPeriod</a>: <i>String</i>
    <a href="#alertthreshold" title="AlertThreshold">AlertThreshold</a>: <i>String</i>
    <a href="#alerttrack" title="AlertTrack">AlertTrack</a>: <i>Boolean</i>
    <a href="#alerttype" title="AlertType">AlertType</a>: <i>String</i>
    <a href="#allowskew" title="AllowSkew">AllowSkew</a>: <i>String</i>
    <a href="#autosummarize" title="AutoSummarize">AutoSummarize</a>: <i>Boolean</i>
    <a href="#autosummarizecommand" title="AutoSummarizeCommand">AutoSummarizeCommand</a>: <i>String</i>
    <a href="#autosummarizecronschedule" title="AutoSummarizeCronSchedule">AutoSummarizeCronSchedule</a>: <i>String</i>
    <a href="#autosummarizedispatchearliesttime" title="AutoSummarizeDispatchEarliestTime">AutoSummarizeDispatchEarliestTime</a>: <i>String</i>
    <a href="#autosummarizedispatchlatesttime" title="AutoSummarizeDispatchLatestTime">AutoSummarizeDispatchLatestTime</a>: <i>String</i>
    <a href="#autosummarizedispatchtimeformat" title="AutoSummarizeDispatchTimeFormat">AutoSummarizeDispatchTimeFormat</a>: <i>String</i>
    <a href="#autosummarizedispatchttl" title="AutoSummarizeDispatchTtl">AutoSummarizeDispatchTtl</a>: <i>String</i>
    <a href="#autosummarizemaxdisabledbuckets" title="AutoSummarizeMaxDisabledBuckets">AutoSummarizeMaxDisabledBuckets</a>: <i>Double</i>
    <a href="#autosummarizemaxsummaryratio" title="AutoSummarizeMaxSummaryRatio">AutoSummarizeMaxSummaryRatio</a>: <i>Double</i>
    <a href="#autosummarizemaxsummarysize" title="AutoSummarizeMaxSummarySize">AutoSummarizeMaxSummarySize</a>: <i>Double</i>
    <a href="#autosummarizemaxtime" title="AutoSummarizeMaxTime">AutoSummarizeMaxTime</a>: <i>Double</i>
    <a href="#autosummarizesuspendperiod" title="AutoSummarizeSuspendPeriod">AutoSummarizeSuspendPeriod</a>: <i>String</i>
    <a href="#autosummarizetimespan" title="AutoSummarizeTimespan">AutoSummarizeTimespan</a>: <i>String</i>
    <a href="#cronschedule" title="CronSchedule">CronSchedule</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#disabled" title="Disabled">Disabled</a>: <i>Boolean</i>
    <a href="#dispatchbuckets" title="DispatchBuckets">DispatchBuckets</a>: <i>Double</i>
    <a href="#dispatchearliesttime" title="DispatchEarliestTime">DispatchEarliestTime</a>: <i>String</i>
    <a href="#dispatchindexearliest" title="DispatchIndexEarliest">DispatchIndexEarliest</a>: <i>String</i>
    <a href="#dispatchindexlatest" title="DispatchIndexLatest">DispatchIndexLatest</a>: <i>String</i>
    <a href="#dispatchindexedrealtime" title="DispatchIndexedRealtime">DispatchIndexedRealtime</a>: <i>Boolean</i>
    <a href="#dispatchindexedrealtimeminspan" title="DispatchIndexedRealtimeMinspan">DispatchIndexedRealtimeMinspan</a>: <i>Double</i>
    <a href="#dispatchindexedrealtimeoffset" title="DispatchIndexedRealtimeOffset">DispatchIndexedRealtimeOffset</a>: <i>Double</i>
    <a href="#dispatchlatesttime" title="DispatchLatestTime">DispatchLatestTime</a>: <i>String</i>
    <a href="#dispatchlookups" title="DispatchLookups">DispatchLookups</a>: <i>Boolean</i>
    <a href="#dispatchmaxcount" title="DispatchMaxCount">DispatchMaxCount</a>: <i>Double</i>
    <a href="#dispatchmaxtime" title="DispatchMaxTime">DispatchMaxTime</a>: <i>Double</i>
    <a href="#dispatchreducefreq" title="DispatchReduceFreq">DispatchReduceFreq</a>: <i>Double</i>
    <a href="#dispatchrtbackfill" title="DispatchRtBackfill">DispatchRtBackfill</a>: <i>Boolean</i>
    <a href="#dispatchrtmaximumspan" title="DispatchRtMaximumSpan">DispatchRtMaximumSpan</a>: <i>Double</i>
    <a href="#dispatchspawnprocess" title="DispatchSpawnProcess">DispatchSpawnProcess</a>: <i>Boolean</i>
    <a href="#dispatchtimeformat" title="DispatchTimeFormat">DispatchTimeFormat</a>: <i>String</i>
    <a href="#dispatchttl" title="DispatchTtl">DispatchTtl</a>: <i>String</i>
    <a href="#displayview" title="DisplayView">DisplayView</a>: <i>String</i>
    <a href="#isscheduled" title="IsScheduled">IsScheduled</a>: <i>Boolean</i>
    <a href="#isvisible" title="IsVisible">IsVisible</a>: <i>Boolean</i>
    <a href="#maxconcurrent" title="MaxConcurrent">MaxConcurrent</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#realtimeschedule" title="RealtimeSchedule">RealtimeSchedule</a>: <i>Boolean</i>
    <a href="#requestuidispatchapp" title="RequestUiDispatchApp">RequestUiDispatchApp</a>: <i>String</i>
    <a href="#requestuidispatchview" title="RequestUiDispatchView">RequestUiDispatchView</a>: <i>String</i>
    <a href="#restartonsearchpeeradd" title="RestartOnSearchpeerAdd">RestartOnSearchpeerAdd</a>: <i>Boolean</i>
    <a href="#runonstartup" title="RunOnStartup">RunOnStartup</a>: <i>Boolean</i>
    <a href="#schedulepriority" title="SchedulePriority">SchedulePriority</a>: <i>String</i>
    <a href="#schedulewindow" title="ScheduleWindow">ScheduleWindow</a>: <i>String</i>
    <a href="#search" title="Search">Search</a>: <i>String</i>
    <a href="#vsid" title="Vsid">Vsid</a>: <i>String</i>
    <a href="#workloadpool" title="WorkloadPool">WorkloadPool</a>: <i>String</i>
    <a href="#acl" title="Acl">Acl</a>: <i>
      - <a href="acldefinition.md">AclDefinition</a></i>
</pre>

## Properties

#### ActionEmailAuthPassword

The password to use when authenticating with the SMTP server. Normally this value is set when editing the email settings, however you can set a clear text password here and it is encrypted on the next platform restart.Defaults to empty string.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailAuthUsername

The username to use when authenticating with the SMTP server. If this is empty string, no authentication is attempted. Defaults to empty stringNOTE: Your SMTP server might reject unauthenticated emails.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailBcc

BCC email address to use if action.email is enabled.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailCc

CC email address to use if action.email is enabled.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailCommand

The search command (or pipeline) which is responsible for executing the action.Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailFormat

Valid values: (table | plain | html | raw | csv)Specify the format of text in the email. This value also applies to any attachments.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailFrom

Email address from which the email action originates.Defaults to splunk@$LOCALHOST or whatever value is set in alert_actions.conf.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailHostname

Sets the hostname used in the web link (url) sent in email actions.This value accepts two forms:hostname (for example, splunkserver, splunkserver.example.com).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailIncludeResultsLink

Specify whether to include a link to the results. Defaults to 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailIncludeSearch

Specify whether to include the search that caused an email to be sent. Defaults to 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailIncludeTrigger

Specify whether to show the trigger condition that caused the alert to fire. Defaults to 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailIncludeTriggerTime

Specify whether to show the time that the alert was fired. Defaults to 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailIncludeViewLink

Specify whether to show the title and a link to enable the user to edit the saved search. Defaults to 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailInline

Indicates whether the search results are contained in the body of the email.Results can be either inline or attached to an email.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailMailserver

Set the address of the MTA server to be used to send the emails.Defaults to <LOCALHOST> or whatever is set in alert_actions.conf.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailMaxResults

Sets the global maximum number of search results to send when email.action is enabled. Defaults to 100.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailMaxTime

Valid values are Integer[m|s|h|d].Specifies the maximum amount of time the execution of an email action takes before the action is aborted. Defaults to 5m.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailMessageAlert

Customize the message sent in the emailed alert. Defaults to: The alert condition for '$name$' was triggered.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailMessageReport

Customize the message sent in the emailed report. Defaults to: The scheduled report '$name$' has run.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailPdfview

The name of the view to deliver if sendpdf is enabled.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailPreprocessResults

Search string to preprocess results before emailing them. Defaults to empty string (no preprocessing).Usually the preprocessing consists of filtering out unwanted internal fields.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailReportCidFontList

Space-separated list. Specifies the set (and load order) of CID fonts for handling Simplified Chinese(gb), Traditional Chinese(cns), Japanese(jp), and Korean(kor) in Integrated PDF Rendering.If multiple fonts provide a glyph for a given character code, the glyph from the first font specified in the list is used.To skip loading any CID fonts, specify the empty string.Defaults to 'gb cns jp kor'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailReportIncludeSplunkLogo

Indicates whether to include the Splunk logo with the report.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailReportPaperOrientation

Valid values: (portrait | landscape)Specifies the paper orientation: portrait or landscape. Defaults to portrait.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailReportPaperSize

Valid values: (letter | legal | ledger | a2 | a3 | a4 | a5)Specifies the paper size for PDFs. Defaults to letter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailReportServerEnabled

No Supported.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailReportServerUrl

Not supported.For a default locally installed report server, the URL is http://localhost:8091/.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailSendCsv

Specify whether to send results as a CSV file. Defaults to 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailSendPdf

Indicates whether to create and send the results as a PDF. Defaults to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailSendResults

Indicates whether to attach the search results in the email.Results can be either attached or inline. See action.email.inline.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailSubject

Specifies an alternate email subject.Defaults to SplunkAlert-<savedsearchname>.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailTo

A comma or semicolon separated list of recipient email addresses. Required if this search is scheduled and the email alert action is enabled.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailTrackAlert

Indicates whether the execution of this action signifies a trackable alert.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailTtl

Valid values are Integer[p].Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows <Integer>, int is the number of scheduled periods. Defaults to 86400 (24 hours).If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailUseSsl

Indicates whether to use SSL when communicating with the SMTP server. Defaults to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailUseTls

Indicates whether to use TLS (transport layer security) when communicating with the SMTP server (starttls).Defaults to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionEmailWidthSortColumns

Indicates whether columns should be sorted from least wide to most wide, left to right.Only valid if format=text.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionPopulateLookupCommand

The search command (or pipeline) which is responsible for executing the action.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionPopulateLookupDest

Lookup name of path of the lookup to populate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionPopulateLookupHostname

Sets the hostname used in the web link (url) sent in alert actions.This value accepts two forms: hostname (for example, splunkserver, splunkserver.example.com)\n\nprotocol://hostname:port (for example, http://splunkserver:8000, https://splunkserver.example.com:443).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionPopulateLookupMaxResults

Sets the maximum number of search results sent using alerts. Defaults to 100.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionPopulateLookupMaxTime

Valid values are: Integer[m|s|h|d]Sets the maximum amount of time the execution of an action takes before the action is aborted. Defaults to 5m.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionPopulateLookupTrackAlert

Indicates whether the execution of this action signifies a trackable alert.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionPopulateLookupTtl

Valid values are Integer[p]Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, then this specifies the number of scheduled periods. Defaults to 10p.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionRssCommand

The search command (or pipeline) which is responsible for executing the action.Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionRssHostname

Sets the hostname used in the web link (url) sent in alert actions.This value accepts two forms:hostname (for example, splunkserver, splunkserver.example.com)\n\nprotocol://hostname:port (for example, http://splunkserver:8000, https://splunkserver.example.com:443).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionRssMaxResults

Sets the maximum number of search results sent using alerts. Defaults to 100.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionRssMaxTime

Valid values are Integer[m|s|h|d].Sets the maximum amount of time the execution of an action takes before the action is aborted. Defaults to 1m.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionRssTrackAlert

Indicates whether the execution of this action signifies a trackable alert.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionRssTtl

Valid values are: Integer[p] Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, specifies the number of scheduled periods. Defaults to 86400 (24 hours).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionScriptCommand

The search command (or pipeline) which is responsible for executing the action.Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionScriptFilename

File name of the script to call. Required if script action is enabled.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionScriptHostname

Sets the hostname used in the web link (url) sent in alert actions.This value accepts two forms:hostname (for example, splunkserver, splunkserver.example.com)\n\nprotocol://hostname:port (for example, http://splunkserver:8000, https://splunkserver.example.com:443).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionScriptMaxResults

Sets the maximum number of search results sent using alerts. Defaults to 100.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionScriptMaxTime

Valid values are Integer[m|s|h|d].Sets the maximum amount of time the execution of an action takes before the action is aborted. Defaults to 1m.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionScriptTrackAlert

Indicates whether the execution of this action signifies a trackable alert.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionScriptTtl

Valid values are: Integer[p] Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, specifies the number of scheduled periods. Defaults to 86400 (24 hours).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionSlackParamAttachment

Include a message attachment. Valid values are message, none, or alert_link.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionSlackParamChannel

Slack channel to send the message to (Should start with # or @).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionSlackParamFields

Show one or more fields from the search results below your Slack message. Comma-separated list of field names. Allows wildcards. eg. index,source*.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionSlackParamMessage

Enter the chat message to send to the Slack channel. The message can include tokens that insert text based on the results of the search.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionSlackParamWebhookUrlOverride

You can override the Slack webhook URL here if you need to send the alert message to a different Slack team.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionSummaryIndexCommand

The search command (or pipeline) which is responsible for executing the action.Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionSummaryIndexHostname

Sets the hostname used in the web link (url) sent in summary-index alert actions.This value accepts two forms:hostname (for example, splunkserver, splunkserver.example.com)protocol://hostname:port (for example, http://splunkserver:8000, https://splunkserver.example.com:443).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionSummaryIndexInline

Determines whether to execute the summary indexing action as part of the scheduled search.NOTE: This option is considered only if the summary index action is enabled and is always executed (in other words, if counttype = always).Defaults to true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionSummaryIndexMaxResults

Sets the maximum number of search results sent using alerts. Defaults to 100.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionSummaryIndexMaxTime

Valid values are Integer[m|s|h|d].Sets the maximum amount of time the execution of an action takes before the action is aborted. Defaults to 1m.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionSummaryIndexName

Specifies the name of the summary index where the results of the scheduled search are saved.Defaults to summary.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionSummaryIndexTrackAlert

Indicates whether the execution of this action signifies a trackable alert.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionSummaryIndexTtl

Valid values are: Integer[p] Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, specifies the number of scheduled periods. Defaults to 86400 (24 hours).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Actions

A comma-separated list of actions to enable. For example: rss,email.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertComparator

One of the following strings: greater than, less than, equal to, rises by, drops by, rises by perc, drops by percUsed with alert_threshold to trigger alert actions.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertCondition

Contains a conditional search that is evaluated against the results of the saved search. Defaults to an empty string.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertDigestMode

Specifies whether alert actions are applied to the entire result set or on each individual result.Defaults to 1 (true).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertExpires

Valid values: [number][time-unit]Sets the period of time to show the alert in the dashboard. Defaults to 24h.Use [number][time-unit] to specify a time. For example: 60 = 60 seconds, 1m = 1 minute, 1h = 60 minutes = 1 hour.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertSeverity

Valid values: (1 | 2 | 3 | 4 | 5 | 6) Sets the alert severity level.Valid values are:1 DEBUG 2 INFO 3 WARN 4 ERROR 5 SEVERE 6 FATAL Defaults to 3.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertSuppress

Indicates whether alert suppression is enabled for this scheduled search.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertSuppressFields

Comma delimited list of fields to use for suppression when doing per result alerting. Required if suppression is turned on and per result alerting is enabled.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertSuppressPeriod

Valid values: [number][time-unit] Specifies the suppresion period. Only valid if alert.supress is enabled.Use [number][time-unit] to specify a time. For example: 60 = 60 seconds, 1m = 1 minute, 1h = 60 minutes = 1 hour.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertThreshold

Valid values are: Integer[%]Specifies the value to compare (see alert_comparator) before triggering the alert actions. If expressed as a percentage, indicates value to use when alert_comparator is set to rises by perc or drops by perc.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertTrack

Valid values: (true | false | auto) Specifies whether to track the actions triggered by this scheduled search.auto - determine whether to track or not based on the tracking setting of each action, do not track scheduled searches that always trigger actions. Default value true - force alert tracking.false - disable alert tracking for this search.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertType

What to base the alert on, overriden by alert_condition if it is specified. Valid values are: always, custom, number of events, number of hosts, number of sources.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowSkew

Allows the search scheduler to distribute scheduled searches randomly and more evenly over their specified search periods.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoSummarize

Indicates whether the scheduler should ensure that the data for this search is automatically summarized. Defaults to 0.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoSummarizeCommand

An auto summarization template for this search. See auto summarization options in savedsearches.conf for more details.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoSummarizeCronSchedule

Cron schedule that probes and generates the summaries for this saved search.The default value is */10 * * * * and corresponds to \`every ten hours\`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoSummarizeDispatchEarliestTime

A time string that specifies the earliest time for summarizing this search. Can be a relative or absolute time.If this value is an absolute time, use the dispatch.time_format to format the value.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoSummarizeDispatchLatestTime

A time string that specifies the latest time for summarizing this saved search. Can be a relative or absolute time.If this value is an absolute time, use the dispatch.time_format to format the value.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoSummarizeDispatchTimeFormat

Defines the time format that Splunk software uses to specify the earliest and latest time. Defaults to %FT%T.%Q%:z.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoSummarizeDispatchTtl

Valid values: Integer[p]. Defaults to 60.Indicates the time to live (in seconds) for the artifacts of the summarization of the scheduled search.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoSummarizeMaxDisabledBuckets

The maximum number of buckets with the suspended summarization before the summarization search is completely stopped, and the summarization of the search is suspended for auto_summarize.suspend_period. Defaults to 2.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoSummarizeMaxSummaryRatio

The maximum ratio of summary_size/bucket_size, which specifies when to stop summarization and deem it unhelpful for a bucket. Defaults to 0.1 Note: The test is only performed if the summary size is larger than auto_summarize.max_summary_size.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoSummarizeMaxSummarySize

The minimum summary size, in bytes, before testing whether the summarization is helpful.The default value is 52428800 and is equivalent to 5MB.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoSummarizeMaxTime

Maximum time (in seconds) that the summary search is allowed to run. Defaults to 3600.Note: This is an approximate time. The summary search stops at clean bucket boundaries.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoSummarizeSuspendPeriod

Time specfier indicating when to suspend summarization of this search if the summarization is deemed unhelpful.Defaults to 24h.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoSummarizeTimespan

The list of time ranges that each summarized chunk should span. This comprises the list of available granularity levels for which summaries would be available. Specify a comma delimited list of time specifiers.For example a timechart over the last month whose granuality is at the day level should set this to 1d. If you need the same data summarized at the hour level for weekly charts, use: 1h,1d.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CronSchedule

Valid values: cron stringThe cron schedule to execute this search. For example: */5 * * * * causes the search to execute every 5 minutes.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Human-readable description of this saved search. Defaults to empty string.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disabled

Indicates if the saved search is enabled. Defaults to 0.Disabled saved searches are not visible in Splunk Web.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DispatchBuckets

The maximum number of timeline buckets. Defaults to 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DispatchEarliestTime

A time string that specifies the earliest time for this search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DispatchIndexEarliest

A time string that specifies the earliest index time for this search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DispatchIndexLatest

A time string that specifies the latest index time for this search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DispatchIndexedRealtime

A time string that specifies the earliest time for this search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DispatchIndexedRealtimeMinspan

Allows for a per-job override of the [search] indexed_realtime_disk_sync_delay setting in limits.conf.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DispatchIndexedRealtimeOffset

Allows for a per-job override of the [search] indexed_realtime_disk_sync_delay setting in limits.conf.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DispatchLatestTime

A time string that specifies the latest time for this saved search. Can be a relative or absolute time.If this value is an absolute time, use the dispatch.time_format to format the value.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DispatchLookups

Enables or disables the lookups for this search. Defaults to 1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DispatchMaxCount

The maximum number of results before finalizing the search. Defaults to 500000.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DispatchMaxTime

Indicates the maximum amount of time (in seconds) before finalizing the search. Defaults to 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DispatchReduceFreq

Specifies, in seconds, how frequently the MapReduce reduce phase runs on accumulated map values. Defaults to 10.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DispatchRtBackfill

Whether to back fill the real time window for this search. Parameter valid only if this is a real time search. Defaults to 0.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DispatchRtMaximumSpan

Allows for a per-job override of the [search] indexed_realtime_maximum_span setting in limits.conf.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DispatchSpawnProcess

Specifies whether a new search process spawns when this saved search is executed. Defaults to 1. Searches against indexes must run in a separate process.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DispatchTimeFormat

A time format string that defines the time format for specifying the earliest and latest time. Defaults to %FT%T.%Q%:z.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DispatchTtl

Valid values: Integer[p]. Defaults to 2p.Indicates the time to live (in seconds) for the artifacts of the scheduled search, if no actions are triggered.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayView

Defines the default UI view name (not label) in which to load the results. Accessibility is subject to the user having sufficient permissions.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsScheduled

Whether this search is to be run on a schedule.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsVisible

Specifies whether this saved search should be listed in the visible saved search list. Defaults to 1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxConcurrent

The maximum number of concurrent instances of this search the scheduler is allowed to run. Defaults to 1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A name for the search.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RealtimeSchedule

Defaults to 1. Controls the way the scheduler computes the next execution time of a scheduled search. If this value is set to 1, the scheduler bases its determination of the next scheduled search execution time on the current time. If this value is set to 0, the scheduler bases its determination of the next scheduled search on the last search execution time. This is called continuous scheduling. If set to 0, the scheduler never skips scheduled execution periods. However, the execution of the saved search might fall behind depending on the scheduler load. Use continuous scheduling whenever you enable the summary index option.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestUiDispatchApp

Specifies a field used by Splunk Web to denote the app this search should be dispatched in.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestUiDispatchView

Specifies a field used by Splunk Web to denote the view this search should be displayed in.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestartOnSearchpeerAdd

Specifies whether to restart a real-time search managed by the scheduler when a search peer becomes available for this saved search. Defaults to 1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunOnStartup

Indicates whether this search runs at startup. If it does not run on startup, it runs at the next scheduled time. Defaults to 0. Set to 1 for scheduled searches that populate lookup tables.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchedulePriority

Raises the scheduling priority of the named search. Defaults to Default.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduleWindow

Time window (in minutes) during which the search has lower priority. Defaults to 0. The scheduler can give higher priority to more critical searches during this window. The window must be smaller than the search period.Set to auto to let the scheduler determine the optimal window value automatically. Requires the edit_search_schedule_window capability to override auto.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Search

Required when creating a new search.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vsid

Defines the viewstate id associated with the UI view listed in 'displayview'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkloadPool

Specifies the new workload pool where the existing running search will be placed.`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Acl

_Required_: No

_Type_: List of <a href="acldefinition.md">AclDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ActionEmail

The state of the email action. Read-only attribute. Value ignored on POST. Use actions to specify a list of enabled actions. Defaults to 0.

#### ActionPopulateLookup

The state of the populate lookup action. Read-only attribute. Value ignored on POST. Use actions to specify a list of enabled actions. Defaults to 0.

#### ActionRss

The state of the rss action. Read-only attribute. Value ignored on POST.Use actions to specify a list of enabled actions. Defaults to 0.

#### ActionScript

The state of the script action. Read-only attribute. Value ignored on POST. Use actions to specify a list of enabled actions. Defaults to 0.

#### ActionSummaryIndex

The state of the summary index action. Read-only attribute. Value ignored on POST. Use actions to specify a list of enabled actions. Defaults to 0.

#### Id

Returns the <code>Id</code> value.

