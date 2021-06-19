# TF::AVI::Analyticsprofile

The AnalyticsProfile resource allows the creation and management of Avi AnalyticsProfile

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Analyticsprofile",
    "Properties" : {
        "<a href="#apdexresponsethreshold" title="ApdexResponseThreshold">ApdexResponseThreshold</a>" : <i>Double</i>,
        "<a href="#apdexresponsetoleratedfactor" title="ApdexResponseToleratedFactor">ApdexResponseToleratedFactor</a>" : <i>Double</i>,
        "<a href="#apdexrttthreshold" title="ApdexRttThreshold">ApdexRttThreshold</a>" : <i>Double</i>,
        "<a href="#apdexrtttoleratedfactor" title="ApdexRttToleratedFactor">ApdexRttToleratedFactor</a>" : <i>Double</i>,
        "<a href="#apdexrumthreshold" title="ApdexRumThreshold">ApdexRumThreshold</a>" : <i>Double</i>,
        "<a href="#apdexrumtoleratedfactor" title="ApdexRumToleratedFactor">ApdexRumToleratedFactor</a>" : <i>Double</i>,
        "<a href="#apdexserverresponsethreshold" title="ApdexServerResponseThreshold">ApdexServerResponseThreshold</a>" : <i>Double</i>,
        "<a href="#apdexserverresponsetoleratedfactor" title="ApdexServerResponseToleratedFactor">ApdexServerResponseToleratedFactor</a>" : <i>Double</i>,
        "<a href="#apdexserverrttthreshold" title="ApdexServerRttThreshold">ApdexServerRttThreshold</a>" : <i>Double</i>,
        "<a href="#apdexserverrtttoleratedfactor" title="ApdexServerRttToleratedFactor">ApdexServerRttToleratedFactor</a>" : <i>Double</i>,
        "<a href="#connlossyooothreshold" title="ConnLossyOooThreshold">ConnLossyOooThreshold</a>" : <i>Double</i>,
        "<a href="#connlossytimeorexmtthreshold" title="ConnLossyTimeoRexmtThreshold">ConnLossyTimeoRexmtThreshold</a>" : <i>Double</i>,
        "<a href="#connlossytotalrexmtthreshold" title="ConnLossyTotalRexmtThreshold">ConnLossyTotalRexmtThreshold</a>" : <i>Double</i>,
        "<a href="#connlossyzerowinsizeeventthreshold" title="ConnLossyZeroWinSizeEventThreshold">ConnLossyZeroWinSizeEventThreshold</a>" : <i>Double</i>,
        "<a href="#connserverlossyooothreshold" title="ConnServerLossyOooThreshold">ConnServerLossyOooThreshold</a>" : <i>Double</i>,
        "<a href="#connserverlossytimeorexmtthreshold" title="ConnServerLossyTimeoRexmtThreshold">ConnServerLossyTimeoRexmtThreshold</a>" : <i>Double</i>,
        "<a href="#connserverlossytotalrexmtthreshold" title="ConnServerLossyTotalRexmtThreshold">ConnServerLossyTotalRexmtThreshold</a>" : <i>Double</i>,
        "<a href="#connserverlossyzerowinsizeeventthreshold" title="ConnServerLossyZeroWinSizeEventThreshold">ConnServerLossyZeroWinSizeEventThreshold</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enableadaptiveconfig" title="EnableAdaptiveConfig">EnableAdaptiveConfig</a>" : <i>Boolean</i>,
        "<a href="#enableadvancedanalytics" title="EnableAdvancedAnalytics">EnableAdvancedAnalytics</a>" : <i>Boolean</i>,
        "<a href="#enableondemandmetrics" title="EnableOndemandMetrics">EnableOndemandMetrics</a>" : <i>Boolean</i>,
        "<a href="#enableseanalytics" title="EnableSeAnalytics">EnableSeAnalytics</a>" : <i>Boolean</i>,
        "<a href="#enableserveranalytics" title="EnableServerAnalytics">EnableServerAnalytics</a>" : <i>Boolean</i>,
        "<a href="#enablevsanalytics" title="EnableVsAnalytics">EnableVsAnalytics</a>" : <i>Boolean</i>,
        "<a href="#excludeclientclosebeforerequestaserror" title="ExcludeClientCloseBeforeRequestAsError">ExcludeClientCloseBeforeRequestAsError</a>" : <i>Boolean</i>,
        "<a href="#excludednspolicydropassignificant" title="ExcludeDnsPolicyDropAsSignificant">ExcludeDnsPolicyDropAsSignificant</a>" : <i>Boolean</i>,
        "<a href="#excludegsdownaserror" title="ExcludeGsDownAsError">ExcludeGsDownAsError</a>" : <i>Boolean</i>,
        "<a href="#excludehttperrorcodes" title="ExcludeHttpErrorCodes">ExcludeHttpErrorCodes</a>" : <i>[ Double, ... ]</i>,
        "<a href="#excludeinvaliddnsdomainaserror" title="ExcludeInvalidDnsDomainAsError">ExcludeInvalidDnsDomainAsError</a>" : <i>Boolean</i>,
        "<a href="#excludeinvaliddnsqueryaserror" title="ExcludeInvalidDnsQueryAsError">ExcludeInvalidDnsQueryAsError</a>" : <i>Boolean</i>,
        "<a href="#excludeissuerrevokedocspresponsesaserror" title="ExcludeIssuerRevokedOcspResponsesAsError">ExcludeIssuerRevokedOcspResponsesAsError</a>" : <i>Boolean</i>,
        "<a href="#excludenodnsrecordaserror" title="ExcludeNoDnsRecordAsError">ExcludeNoDnsRecordAsError</a>" : <i>Boolean</i>,
        "<a href="#excludenovalidgsmemberaserror" title="ExcludeNoValidGsMemberAsError">ExcludeNoValidGsMemberAsError</a>" : <i>Boolean</i>,
        "<a href="#excludepersistencechangeaserror" title="ExcludePersistenceChangeAsError">ExcludePersistenceChangeAsError</a>" : <i>Boolean</i>,
        "<a href="#excluderevokedocspresponsesaserror" title="ExcludeRevokedOcspResponsesAsError">ExcludeRevokedOcspResponsesAsError</a>" : <i>Boolean</i>,
        "<a href="#excludeserverdnserroraserror" title="ExcludeServerDnsErrorAsError">ExcludeServerDnsErrorAsError</a>" : <i>Boolean</i>,
        "<a href="#excludeservertcpresetaserror" title="ExcludeServerTcpResetAsError">ExcludeServerTcpResetAsError</a>" : <i>Boolean</i>,
        "<a href="#excludesiperrorcodes" title="ExcludeSipErrorCodes">ExcludeSipErrorCodes</a>" : <i>[ Double, ... ]</i>,
        "<a href="#excludestaleocspresponsesaserror" title="ExcludeStaleOcspResponsesAsError">ExcludeStaleOcspResponsesAsError</a>" : <i>Boolean</i>,
        "<a href="#excludesynretransmitaserror" title="ExcludeSynRetransmitAsError">ExcludeSynRetransmitAsError</a>" : <i>Boolean</i>,
        "<a href="#excludetcpresetaserror" title="ExcludeTcpResetAsError">ExcludeTcpResetAsError</a>" : <i>Boolean</i>,
        "<a href="#excludeunavailableocspresponsesaserror" title="ExcludeUnavailableOcspResponsesAsError">ExcludeUnavailableOcspResponsesAsError</a>" : <i>Boolean</i>,
        "<a href="#excludeunsupporteddnsqueryaserror" title="ExcludeUnsupportedDnsQueryAsError">ExcludeUnsupportedDnsQueryAsError</a>" : <i>Boolean</i>,
        "<a href="#healthscoremaxserverlimit" title="HealthscoreMaxServerLimit">HealthscoreMaxServerLimit</a>" : <i>Double</i>,
        "<a href="#hseventthrottlewindow" title="HsEventThrottleWindow">HsEventThrottleWindow</a>" : <i>Double</i>,
        "<a href="#hsmaxanomalypenalty" title="HsMaxAnomalyPenalty">HsMaxAnomalyPenalty</a>" : <i>Double</i>,
        "<a href="#hsmaxresourcespenalty" title="HsMaxResourcesPenalty">HsMaxResourcesPenalty</a>" : <i>Double</i>,
        "<a href="#hsmaxsecuritypenalty" title="HsMaxSecurityPenalty">HsMaxSecurityPenalty</a>" : <i>Double</i>,
        "<a href="#hsmindosrate" title="HsMinDosRate">HsMinDosRate</a>" : <i>Double</i>,
        "<a href="#hsperformanceboost" title="HsPerformanceBoost">HsPerformanceBoost</a>" : <i>Double</i>,
        "<a href="#hspscoretrafficthresholdl4client" title="HsPscoreTrafficThresholdL4Client">HsPscoreTrafficThresholdL4Client</a>" : <i>Double</i>,
        "<a href="#hspscoretrafficthresholdl4server" title="HsPscoreTrafficThresholdL4Server">HsPscoreTrafficThresholdL4Server</a>" : <i>Double</i>,
        "<a href="#hssecuritycertscoreexpired" title="HsSecurityCertscoreExpired">HsSecurityCertscoreExpired</a>" : <i>Double</i>,
        "<a href="#hssecuritycertscoregt30d" title="HsSecurityCertscoreGt30d">HsSecurityCertscoreGt30d</a>" : <i>Double</i>,
        "<a href="#hssecuritycertscorele07d" title="HsSecurityCertscoreLe07d">HsSecurityCertscoreLe07d</a>" : <i>Double</i>,
        "<a href="#hssecuritycertscorele30d" title="HsSecurityCertscoreLe30d">HsSecurityCertscoreLe30d</a>" : <i>Double</i>,
        "<a href="#hssecuritychaininvaliditypenalty" title="HsSecurityChainInvalidityPenalty">HsSecurityChainInvalidityPenalty</a>" : <i>Double</i>,
        "<a href="#hssecuritycipherscoreeq000b" title="HsSecurityCipherscoreEq000b">HsSecurityCipherscoreEq000b</a>" : <i>Double</i>,
        "<a href="#hssecuritycipherscorege128b" title="HsSecurityCipherscoreGe128b">HsSecurityCipherscoreGe128b</a>" : <i>Double</i>,
        "<a href="#hssecuritycipherscorelt128b" title="HsSecurityCipherscoreLt128b">HsSecurityCipherscoreLt128b</a>" : <i>Double</i>,
        "<a href="#hssecurityencalgoscorenone" title="HsSecurityEncalgoScoreNone">HsSecurityEncalgoScoreNone</a>" : <i>Double</i>,
        "<a href="#hssecurityencalgoscorerc4" title="HsSecurityEncalgoScoreRc4">HsSecurityEncalgoScoreRc4</a>" : <i>Double</i>,
        "<a href="#hssecurityhstspenalty" title="HsSecurityHstsPenalty">HsSecurityHstsPenalty</a>" : <i>Double</i>,
        "<a href="#hssecuritynonpfspenalty" title="HsSecurityNonpfsPenalty">HsSecurityNonpfsPenalty</a>" : <i>Double</i>,
        "<a href="#hssecurityocsprevokedscore" title="HsSecurityOcspRevokedScore">HsSecurityOcspRevokedScore</a>" : <i>Double</i>,
        "<a href="#hssecurityselfsignedcertpenalty" title="HsSecuritySelfsignedcertPenalty">HsSecuritySelfsignedcertPenalty</a>" : <i>Double</i>,
        "<a href="#hssecurityssl30score" title="HsSecuritySsl30Score">HsSecuritySsl30Score</a>" : <i>Double</i>,
        "<a href="#hssecuritytls10score" title="HsSecurityTls10Score">HsSecurityTls10Score</a>" : <i>Double</i>,
        "<a href="#hssecuritytls11score" title="HsSecurityTls11Score">HsSecurityTls11Score</a>" : <i>Double</i>,
        "<a href="#hssecuritytls12score" title="HsSecurityTls12Score">HsSecurityTls12Score</a>" : <i>Double</i>,
        "<a href="#hssecurityweaksignaturealgopenalty" title="HsSecurityWeakSignatureAlgoPenalty">HsSecurityWeakSignatureAlgoPenalty</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ondemandmetricsidletimeout" title="OndemandMetricsIdleTimeout">OndemandMetricsIdleTimeout</a>" : <i>Double</i>,
        "<a href="#respcodeblock" title="RespCodeBlock">RespCodeBlock</a>" : <i>[ String, ... ]</i>,
        "<a href="#siplogdepth" title="SipLogDepth">SipLogDepth</a>" : <i>Double</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#clientlogconfig" title="ClientLogConfig">ClientLogConfig</a>" : <i>[ <a href="clientlogconfigdefinition.md">ClientLogConfigDefinition</a>, ... ]</i>,
        "<a href="#clientlogstreamingconfig" title="ClientLogStreamingConfig">ClientLogStreamingConfig</a>" : <i>[ <a href="clientlogstreamingconfigdefinition.md">ClientLogStreamingConfigDefinition</a>, ... ]</i>,
        "<a href="#markers" title="Markers">Markers</a>" : <i>[ <a href="markersdefinition.md">MarkersDefinition</a>, ... ]</i>,
        "<a href="#ranges" title="Ranges">Ranges</a>" : <i>[ <a href="rangesdefinition.md">RangesDefinition</a>, ... ]</i>,
        "<a href="#sensitivelogprofile" title="SensitiveLogProfile">SensitiveLogProfile</a>" : <i>[ <a href="sensitivelogprofiledefinition.md">SensitiveLogProfileDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Analyticsprofile
Properties:
    <a href="#apdexresponsethreshold" title="ApdexResponseThreshold">ApdexResponseThreshold</a>: <i>Double</i>
    <a href="#apdexresponsetoleratedfactor" title="ApdexResponseToleratedFactor">ApdexResponseToleratedFactor</a>: <i>Double</i>
    <a href="#apdexrttthreshold" title="ApdexRttThreshold">ApdexRttThreshold</a>: <i>Double</i>
    <a href="#apdexrtttoleratedfactor" title="ApdexRttToleratedFactor">ApdexRttToleratedFactor</a>: <i>Double</i>
    <a href="#apdexrumthreshold" title="ApdexRumThreshold">ApdexRumThreshold</a>: <i>Double</i>
    <a href="#apdexrumtoleratedfactor" title="ApdexRumToleratedFactor">ApdexRumToleratedFactor</a>: <i>Double</i>
    <a href="#apdexserverresponsethreshold" title="ApdexServerResponseThreshold">ApdexServerResponseThreshold</a>: <i>Double</i>
    <a href="#apdexserverresponsetoleratedfactor" title="ApdexServerResponseToleratedFactor">ApdexServerResponseToleratedFactor</a>: <i>Double</i>
    <a href="#apdexserverrttthreshold" title="ApdexServerRttThreshold">ApdexServerRttThreshold</a>: <i>Double</i>
    <a href="#apdexserverrtttoleratedfactor" title="ApdexServerRttToleratedFactor">ApdexServerRttToleratedFactor</a>: <i>Double</i>
    <a href="#connlossyooothreshold" title="ConnLossyOooThreshold">ConnLossyOooThreshold</a>: <i>Double</i>
    <a href="#connlossytimeorexmtthreshold" title="ConnLossyTimeoRexmtThreshold">ConnLossyTimeoRexmtThreshold</a>: <i>Double</i>
    <a href="#connlossytotalrexmtthreshold" title="ConnLossyTotalRexmtThreshold">ConnLossyTotalRexmtThreshold</a>: <i>Double</i>
    <a href="#connlossyzerowinsizeeventthreshold" title="ConnLossyZeroWinSizeEventThreshold">ConnLossyZeroWinSizeEventThreshold</a>: <i>Double</i>
    <a href="#connserverlossyooothreshold" title="ConnServerLossyOooThreshold">ConnServerLossyOooThreshold</a>: <i>Double</i>
    <a href="#connserverlossytimeorexmtthreshold" title="ConnServerLossyTimeoRexmtThreshold">ConnServerLossyTimeoRexmtThreshold</a>: <i>Double</i>
    <a href="#connserverlossytotalrexmtthreshold" title="ConnServerLossyTotalRexmtThreshold">ConnServerLossyTotalRexmtThreshold</a>: <i>Double</i>
    <a href="#connserverlossyzerowinsizeeventthreshold" title="ConnServerLossyZeroWinSizeEventThreshold">ConnServerLossyZeroWinSizeEventThreshold</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enableadaptiveconfig" title="EnableAdaptiveConfig">EnableAdaptiveConfig</a>: <i>Boolean</i>
    <a href="#enableadvancedanalytics" title="EnableAdvancedAnalytics">EnableAdvancedAnalytics</a>: <i>Boolean</i>
    <a href="#enableondemandmetrics" title="EnableOndemandMetrics">EnableOndemandMetrics</a>: <i>Boolean</i>
    <a href="#enableseanalytics" title="EnableSeAnalytics">EnableSeAnalytics</a>: <i>Boolean</i>
    <a href="#enableserveranalytics" title="EnableServerAnalytics">EnableServerAnalytics</a>: <i>Boolean</i>
    <a href="#enablevsanalytics" title="EnableVsAnalytics">EnableVsAnalytics</a>: <i>Boolean</i>
    <a href="#excludeclientclosebeforerequestaserror" title="ExcludeClientCloseBeforeRequestAsError">ExcludeClientCloseBeforeRequestAsError</a>: <i>Boolean</i>
    <a href="#excludednspolicydropassignificant" title="ExcludeDnsPolicyDropAsSignificant">ExcludeDnsPolicyDropAsSignificant</a>: <i>Boolean</i>
    <a href="#excludegsdownaserror" title="ExcludeGsDownAsError">ExcludeGsDownAsError</a>: <i>Boolean</i>
    <a href="#excludehttperrorcodes" title="ExcludeHttpErrorCodes">ExcludeHttpErrorCodes</a>: <i>
      - Double</i>
    <a href="#excludeinvaliddnsdomainaserror" title="ExcludeInvalidDnsDomainAsError">ExcludeInvalidDnsDomainAsError</a>: <i>Boolean</i>
    <a href="#excludeinvaliddnsqueryaserror" title="ExcludeInvalidDnsQueryAsError">ExcludeInvalidDnsQueryAsError</a>: <i>Boolean</i>
    <a href="#excludeissuerrevokedocspresponsesaserror" title="ExcludeIssuerRevokedOcspResponsesAsError">ExcludeIssuerRevokedOcspResponsesAsError</a>: <i>Boolean</i>
    <a href="#excludenodnsrecordaserror" title="ExcludeNoDnsRecordAsError">ExcludeNoDnsRecordAsError</a>: <i>Boolean</i>
    <a href="#excludenovalidgsmemberaserror" title="ExcludeNoValidGsMemberAsError">ExcludeNoValidGsMemberAsError</a>: <i>Boolean</i>
    <a href="#excludepersistencechangeaserror" title="ExcludePersistenceChangeAsError">ExcludePersistenceChangeAsError</a>: <i>Boolean</i>
    <a href="#excluderevokedocspresponsesaserror" title="ExcludeRevokedOcspResponsesAsError">ExcludeRevokedOcspResponsesAsError</a>: <i>Boolean</i>
    <a href="#excludeserverdnserroraserror" title="ExcludeServerDnsErrorAsError">ExcludeServerDnsErrorAsError</a>: <i>Boolean</i>
    <a href="#excludeservertcpresetaserror" title="ExcludeServerTcpResetAsError">ExcludeServerTcpResetAsError</a>: <i>Boolean</i>
    <a href="#excludesiperrorcodes" title="ExcludeSipErrorCodes">ExcludeSipErrorCodes</a>: <i>
      - Double</i>
    <a href="#excludestaleocspresponsesaserror" title="ExcludeStaleOcspResponsesAsError">ExcludeStaleOcspResponsesAsError</a>: <i>Boolean</i>
    <a href="#excludesynretransmitaserror" title="ExcludeSynRetransmitAsError">ExcludeSynRetransmitAsError</a>: <i>Boolean</i>
    <a href="#excludetcpresetaserror" title="ExcludeTcpResetAsError">ExcludeTcpResetAsError</a>: <i>Boolean</i>
    <a href="#excludeunavailableocspresponsesaserror" title="ExcludeUnavailableOcspResponsesAsError">ExcludeUnavailableOcspResponsesAsError</a>: <i>Boolean</i>
    <a href="#excludeunsupporteddnsqueryaserror" title="ExcludeUnsupportedDnsQueryAsError">ExcludeUnsupportedDnsQueryAsError</a>: <i>Boolean</i>
    <a href="#healthscoremaxserverlimit" title="HealthscoreMaxServerLimit">HealthscoreMaxServerLimit</a>: <i>Double</i>
    <a href="#hseventthrottlewindow" title="HsEventThrottleWindow">HsEventThrottleWindow</a>: <i>Double</i>
    <a href="#hsmaxanomalypenalty" title="HsMaxAnomalyPenalty">HsMaxAnomalyPenalty</a>: <i>Double</i>
    <a href="#hsmaxresourcespenalty" title="HsMaxResourcesPenalty">HsMaxResourcesPenalty</a>: <i>Double</i>
    <a href="#hsmaxsecuritypenalty" title="HsMaxSecurityPenalty">HsMaxSecurityPenalty</a>: <i>Double</i>
    <a href="#hsmindosrate" title="HsMinDosRate">HsMinDosRate</a>: <i>Double</i>
    <a href="#hsperformanceboost" title="HsPerformanceBoost">HsPerformanceBoost</a>: <i>Double</i>
    <a href="#hspscoretrafficthresholdl4client" title="HsPscoreTrafficThresholdL4Client">HsPscoreTrafficThresholdL4Client</a>: <i>Double</i>
    <a href="#hspscoretrafficthresholdl4server" title="HsPscoreTrafficThresholdL4Server">HsPscoreTrafficThresholdL4Server</a>: <i>Double</i>
    <a href="#hssecuritycertscoreexpired" title="HsSecurityCertscoreExpired">HsSecurityCertscoreExpired</a>: <i>Double</i>
    <a href="#hssecuritycertscoregt30d" title="HsSecurityCertscoreGt30d">HsSecurityCertscoreGt30d</a>: <i>Double</i>
    <a href="#hssecuritycertscorele07d" title="HsSecurityCertscoreLe07d">HsSecurityCertscoreLe07d</a>: <i>Double</i>
    <a href="#hssecuritycertscorele30d" title="HsSecurityCertscoreLe30d">HsSecurityCertscoreLe30d</a>: <i>Double</i>
    <a href="#hssecuritychaininvaliditypenalty" title="HsSecurityChainInvalidityPenalty">HsSecurityChainInvalidityPenalty</a>: <i>Double</i>
    <a href="#hssecuritycipherscoreeq000b" title="HsSecurityCipherscoreEq000b">HsSecurityCipherscoreEq000b</a>: <i>Double</i>
    <a href="#hssecuritycipherscorege128b" title="HsSecurityCipherscoreGe128b">HsSecurityCipherscoreGe128b</a>: <i>Double</i>
    <a href="#hssecuritycipherscorelt128b" title="HsSecurityCipherscoreLt128b">HsSecurityCipherscoreLt128b</a>: <i>Double</i>
    <a href="#hssecurityencalgoscorenone" title="HsSecurityEncalgoScoreNone">HsSecurityEncalgoScoreNone</a>: <i>Double</i>
    <a href="#hssecurityencalgoscorerc4" title="HsSecurityEncalgoScoreRc4">HsSecurityEncalgoScoreRc4</a>: <i>Double</i>
    <a href="#hssecurityhstspenalty" title="HsSecurityHstsPenalty">HsSecurityHstsPenalty</a>: <i>Double</i>
    <a href="#hssecuritynonpfspenalty" title="HsSecurityNonpfsPenalty">HsSecurityNonpfsPenalty</a>: <i>Double</i>
    <a href="#hssecurityocsprevokedscore" title="HsSecurityOcspRevokedScore">HsSecurityOcspRevokedScore</a>: <i>Double</i>
    <a href="#hssecurityselfsignedcertpenalty" title="HsSecuritySelfsignedcertPenalty">HsSecuritySelfsignedcertPenalty</a>: <i>Double</i>
    <a href="#hssecurityssl30score" title="HsSecuritySsl30Score">HsSecuritySsl30Score</a>: <i>Double</i>
    <a href="#hssecuritytls10score" title="HsSecurityTls10Score">HsSecurityTls10Score</a>: <i>Double</i>
    <a href="#hssecuritytls11score" title="HsSecurityTls11Score">HsSecurityTls11Score</a>: <i>Double</i>
    <a href="#hssecuritytls12score" title="HsSecurityTls12Score">HsSecurityTls12Score</a>: <i>Double</i>
    <a href="#hssecurityweaksignaturealgopenalty" title="HsSecurityWeakSignatureAlgoPenalty">HsSecurityWeakSignatureAlgoPenalty</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ondemandmetricsidletimeout" title="OndemandMetricsIdleTimeout">OndemandMetricsIdleTimeout</a>: <i>Double</i>
    <a href="#respcodeblock" title="RespCodeBlock">RespCodeBlock</a>: <i>
      - String</i>
    <a href="#siplogdepth" title="SipLogDepth">SipLogDepth</a>: <i>Double</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#clientlogconfig" title="ClientLogConfig">ClientLogConfig</a>: <i>
      - <a href="clientlogconfigdefinition.md">ClientLogConfigDefinition</a></i>
    <a href="#clientlogstreamingconfig" title="ClientLogStreamingConfig">ClientLogStreamingConfig</a>: <i>
      - <a href="clientlogstreamingconfigdefinition.md">ClientLogStreamingConfigDefinition</a></i>
    <a href="#markers" title="Markers">Markers</a>: <i>
      - <a href="markersdefinition.md">MarkersDefinition</a></i>
    <a href="#ranges" title="Ranges">Ranges</a>: <i>
      - <a href="rangesdefinition.md">RangesDefinition</a></i>
    <a href="#sensitivelogprofile" title="SensitiveLogProfile">SensitiveLogProfile</a>: <i>
      - <a href="sensitivelogprofiledefinition.md">SensitiveLogProfileDefinition</a></i>
</pre>

## Properties

#### ApdexResponseThreshold

If a client receives an http response in less than the satisfactory latency threshold, the request is considered satisfied. It is considered tolerated if it is not satisfied and less than tolerated latency factor multiplied by the satisfactory latency threshold. Greater than this number and the client's request is considered frustrated. Allowed values are 1-30000. Unit is milliseconds. Allowed in basic(allowed values- 500) edition, essentials(allowed values- 500) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApdexResponseToleratedFactor

Client tolerated response latency factor. Client must receive a response within this factor times the satisfactory threshold (apdex_response_threshold) to be considered tolerated. Allowed values are 1-1000. Allowed in basic(allowed values- 4) edition, essentials(allowed values- 4) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApdexRttThreshold

Satisfactory client to avi round trip time(rtt). Allowed values are 1-2000. Unit is milliseconds. Allowed in basic(allowed values- 250) edition, essentials(allowed values- 250) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApdexRttToleratedFactor

Tolerated client to avi round trip time(rtt) factor. It is a multiple of apdex_rtt_tolerated_factor. Allowed values are 1-1000. Allowed in basic(allowed values- 4) edition, essentials(allowed values- 4) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApdexRumThreshold

If a client is able to load a page in less than the satisfactory latency threshold, the pageload is considered satisfied. It is considered tolerated if it is greater than satisfied but less than the tolerated latency multiplied by satisifed latency. Greater than this number and the client's request is considered frustrated. A pageload includes the time for dns lookup, download of all http objects, and page render time. Allowed values are 1-30000. Unit is milliseconds. Allowed in basic(allowed values- 5000) edition, essentials(allowed values- 5000) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApdexRumToleratedFactor

Virtual service threshold factor for tolerated page load time (plt) as multiple of apdex_rum_threshold. Allowed values are 1-1000. Allowed in basic(allowed values- 4) edition, essentials(allowed values- 4) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApdexServerResponseThreshold

A server http response is considered satisfied if latency is less than the satisfactory latency threshold. The response is considered tolerated when it is greater than satisfied but less than the tolerated latency factor * s_latency. Greater than this number and the server response is considered frustrated. Allowed values are 1-30000. Unit is milliseconds. Allowed in basic(allowed values- 400) edition, essentials(allowed values- 400) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApdexServerResponseToleratedFactor

Server tolerated response latency factor. Servermust response within this factor times the satisfactory threshold (apdex_server_response_threshold) to be considered tolerated. Allowed values are 1-1000. Allowed in basic(allowed values- 4) edition, essentials(allowed values- 4) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApdexServerRttThreshold

Satisfactory client to avi round trip time(rtt). Allowed values are 1-2000. Unit is milliseconds. Allowed in basic(allowed values- 125) edition, essentials(allowed values- 125) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApdexServerRttToleratedFactor

Tolerated client to avi round trip time(rtt) factor. It is a multiple of apdex_rtt_tolerated_factor. Allowed values are 1-1000. Allowed in basic(allowed values- 4) edition, essentials(allowed values- 4) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnLossyOooThreshold

A connection between client and avi is considered lossy when more than this percentage of out of order packets are received. Allowed values are 1-100. Unit is percent. Allowed in basic(allowed values- 50) edition, essentials(allowed values- 50) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnLossyTimeoRexmtThreshold

A connection between client and avi is considered lossy when more than this percentage of packets are retransmitted due to timeout. Allowed values are 1-100. Unit is percent. Allowed in basic(allowed values- 20) edition, essentials(allowed values- 20) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnLossyTotalRexmtThreshold

A connection between client and avi is considered lossy when more than this percentage of packets are retransmitted. Allowed values are 1-100. Unit is percent. Allowed in basic(allowed values- 50) edition, essentials(allowed values- 50) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnLossyZeroWinSizeEventThreshold

A client connection is considered lossy when percentage of times a packet could not be trasmitted due to tcp zero window is above this threshold. Allowed values are 0-100. Unit is percent. Allowed in basic(allowed values- 2) edition, essentials(allowed values- 2) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnServerLossyOooThreshold

A connection between avi and server is considered lossy when more than this percentage of out of order packets are received. Allowed values are 1-100. Unit is percent. Allowed in basic(allowed values- 50) edition, essentials(allowed values- 50) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnServerLossyTimeoRexmtThreshold

A connection between avi and server is considered lossy when more than this percentage of packets are retransmitted due to timeout. Allowed values are 1-100. Unit is percent. Allowed in basic(allowed values- 20) edition, essentials(allowed values- 20) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnServerLossyTotalRexmtThreshold

A connection between avi and server is considered lossy when more than this percentage of packets are retransmitted. Allowed values are 1-100. Unit is percent. Allowed in basic(allowed values- 50) edition, essentials(allowed values- 50) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnServerLossyZeroWinSizeEventThreshold

A server connection is considered lossy when percentage of times a packet could not be trasmitted due to tcp zero window is above this threshold. Allowed values are 0-100. Unit is percent. Allowed in basic(allowed values- 2) edition, essentials(allowed values- 2) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

User defined description for the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableAdaptiveConfig

Enable adaptive configuration for optimizing resource usage. Field introduced in 20.1.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableAdvancedAnalytics

Enables advanced analytics features like anomaly detection. If set to false, anomaly computation (and associated rules/events) for vs, pool and server metrics will be deactivated. However, setting it to false reduces cpu and memory requirements for analytics subsystem. Field introduced in 17.2.13, 18.1.5, 18.2.1. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition. Special default for basic edition is false, essentials edition is false, enterprise is true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableOndemandMetrics

Virtual service (vs) metrics are processed only when there is live data traffic on the vs. In case, vs is idle for a period of time as specified by ondemand_metrics_idle_timeout then metrics processing is suspended for that vs. Field introduced in 20.1.3.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableSeAnalytics

Enable node (service engine) level analytics forvs metrics. Field introduced in 20.1.3.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableServerAnalytics

Enables analytics on backend servers. This may be desired in container environment when there are large number of ephemeral servers. Additionally, no healthscore of servers is computed when server analytics is enabled. Field introduced in 20.1.3.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableVsAnalytics

Enable virtualservice (frontend) analytics. This flag enables metrics and healthscore for virtualservice. Field introduced in 20.1.3.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeClientCloseBeforeRequestAsError

Exclude client closed connection before an http request could be completed from being classified as an error. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeDnsPolicyDropAsSignificant

Exclude dns policy drops from the list of errors. Field introduced in 17.2.2. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeGsDownAsError

Exclude queries to gslb services that are operationally down from the list of errors. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeHttpErrorCodes

List of http status codes to be excluded from being classified as an error. Error connections or responses impacts health score, are included as significant logs, and may be classified as part of a dos attack.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeInvalidDnsDomainAsError

Exclude dns queries to domains outside the domains configured in the dns application profile from the list of errors. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeInvalidDnsQueryAsError

Exclude invalid dns queries from the list of errors. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeIssuerRevokedOcspResponsesAsError

Exclude the issuer-revoked ocsp responses from the list of errors. Field introduced in 20.1.1. Allowed in basic(allowed values- true) edition, essentials(allowed values- true) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeNoDnsRecordAsError

Exclude queries to domains that did not have configured services/records from the list of errors. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeNoValidGsMemberAsError

Exclude queries to gslb services that have no available members from the list of errors. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludePersistenceChangeAsError

Exclude persistence server changed while load balancing' from the list of errors. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeRevokedOcspResponsesAsError

Exclude the revoked ocsp certificate status responses from the list of errors. Field introduced in 20.1.1. Allowed in basic(allowed values- true) edition, essentials(allowed values- true) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeServerDnsErrorAsError

Exclude server dns error response from the list of errors. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeServerTcpResetAsError

Exclude server tcp reset from errors. It is common for applications like ms exchange. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeSipErrorCodes

List of sip status codes to be excluded from being classified as an error. Field introduced in 17.2.13, 18.1.5, 18.2.1. Allowed in basic edition, essentials edition, enterprise edition.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeStaleOcspResponsesAsError

Exclude the stale ocsp certificate status responses from the list of errors. Field introduced in 20.1.1. Allowed in basic(allowed values- true) edition, essentials(allowed values- true) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeSynRetransmitAsError

Exclude 'server unanswered syns' from the list of errors. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeTcpResetAsError

Exclude tcp resets by client from the list of potential errors. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeUnavailableOcspResponsesAsError

Exclude the unavailable ocsp responses from the list of errors. Field introduced in 20.1.1. Allowed in basic(allowed values- true) edition, essentials(allowed values- true) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeUnsupportedDnsQueryAsError

Exclude unsupported dns queries from the list of errors. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthscoreMaxServerLimit

Skips health score computation of pool servers when number of servers in a pool is more than this setting. Allowed values are 0-5000. Special values are 0- 'server health score is deactivated'. Field introduced in 17.2.13, 18.1.4. Allowed in basic(allowed values- 0) edition, essentials(allowed values- 0) edition, enterprise edition. Special default for basic edition is 0, essentials edition is 0, enterprise is 20.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HsEventThrottleWindow

Time window (in secs) within which only unique health change events should occur. Allowed in basic(allowed values- 1209600) edition, essentials(allowed values- 1209600) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HsMaxAnomalyPenalty

Maximum penalty that may be deducted from health score for anomalies. Allowed values are 0-100. Allowed in basic(allowed values- 10) edition, essentials(allowed values- 10) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HsMaxResourcesPenalty

Maximum penalty that may be deducted from health score for high resource utilization. Allowed values are 0-100. Allowed in basic(allowed values- 25) edition, essentials(allowed values- 25) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HsMaxSecurityPenalty

Maximum penalty that may be deducted from health score based on security assessment. Allowed values are 0-100. Allowed in basic(allowed values- 100) edition, essentials(allowed values- 100) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HsMinDosRate

Dos connection rate below which the dos security assessment will not kick in. Allowed in basic(allowed values- 1000) edition, essentials(allowed values- 1000) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HsPerformanceBoost

Adds free performance score credits to health score. It can be used for compensating health score for known slow applications. Allowed values are 0-100. Allowed in basic(allowed values- 0) edition, essentials(allowed values- 0) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HsPscoreTrafficThresholdL4Client

Threshold number of connections in 5min, below which apdexr, apdexc, rum_apdex, and other network quality metrics are not computed. Allowed in basic(allowed values- 10) edition, essentials(allowed values- 10) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HsPscoreTrafficThresholdL4Server

Threshold number of connections in 5min, below which apdexr, apdexc, rum_apdex, and other network quality metrics are not computed. Allowed in basic(allowed values- 10) edition, essentials(allowed values- 10) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HsSecurityCertscoreExpired

Score assigned when the certificate has expired. Allowed values are 0-5. Allowed in basic(allowed values- 0.0) edition, essentials(allowed values- 0.0) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HsSecurityCertscoreGt30d

Score assigned when the certificate expires in more than 30 days. Allowed values are 0-5. Allowed in basic(allowed values- 5.0) edition, essentials(allowed values- 5.0) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HsSecurityCertscoreLe07d

Score assigned when the certificate expires in less than or equal to 7 days. Allowed values are 0-5. Allowed in basic(allowed values- 2.0) edition, essentials(allowed values- 2.0) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HsSecurityCertscoreLe30d

Score assigned when the certificate expires in less than or equal to 30 days. Allowed values are 0-5. Allowed in basic(allowed values- 4.0) edition, essentials(allowed values- 4.0) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HsSecurityChainInvalidityPenalty

Penalty for allowing certificates with invalid chain. Allowed values are 0-5. Allowed in basic(allowed values- 1.0) edition, essentials(allowed values- 1.0) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HsSecurityCipherscoreEq000b

Score assigned when the minimum cipher strength is 0 bits. Allowed values are 0-5. Allowed in basic(allowed values- 0.0) edition, essentials(allowed values- 0.0) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HsSecurityCipherscoreGe128b

Score assigned when the minimum cipher strength is greater than equal to 128 bits. Allowed values are 0-5. Allowed in basic(allowed values- 5.0) edition, essentials(allowed values- 5.0) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HsSecurityCipherscoreLt128b

Score assigned when the minimum cipher strength is less than 128 bits. Allowed values are 0-5. Allowed in basic(allowed values- 3.5) edition, essentials(allowed values- 3.5) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HsSecurityEncalgoScoreNone

Score assigned when no algorithm is used for encryption. Allowed values are 0-5. Allowed in basic(allowed values- 0.0) edition, essentials(allowed values- 0.0) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HsSecurityEncalgoScoreRc4

Score assigned when rc4 algorithm is used for encryption. Allowed values are 0-5. Allowed in basic(allowed values- 2.5) edition, essentials(allowed values- 2.5) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HsSecurityHstsPenalty

Penalty for not enabling hsts. Allowed values are 0-5. Allowed in basic(allowed values- 1.0) edition, essentials(allowed values- 1.0) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HsSecurityNonpfsPenalty

Penalty for allowing non-pfs handshakes. Allowed values are 0-5. Allowed in basic(allowed values- 1.0) edition, essentials(allowed values- 1.0) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HsSecurityOcspRevokedScore

Score assigned when ocsp certificate status is set to revoked or issuer revoked. Allowed values are 0.0-5.0. Field introduced in 20.1.1. Allowed in basic(allowed values- 0.0) edition, essentials(allowed values- 0.0) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HsSecuritySelfsignedcertPenalty

Deprecated. Allowed values are 0-5. Allowed in basic(allowed values- 1.0) edition, essentials(allowed values- 1.0) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HsSecuritySsl30Score

Score assigned when supporting ssl3.0 encryption protocol. Allowed values are 0-5. Allowed in basic(allowed values- 3.5) edition, essentials(allowed values- 3.5) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HsSecurityTls10Score

Score assigned when supporting tls1.0 encryption protocol. Allowed values are 0-5. Allowed in basic(allowed values- 5.0) edition, essentials(allowed values- 5.0) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HsSecurityTls11Score

Score assigned when supporting tls1.1 encryption protocol. Allowed values are 0-5. Allowed in basic(allowed values- 5.0) edition, essentials(allowed values- 5.0) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HsSecurityTls12Score

Score assigned when supporting tls1.2 encryption protocol. Allowed values are 0-5. Allowed in basic(allowed values- 5.0) edition, essentials(allowed values- 5.0) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HsSecurityWeakSignatureAlgoPenalty

Penalty for allowing weak signature algorithm(s). Allowed values are 0-5. Allowed in basic(allowed values- 1.0) edition, essentials(allowed values- 1.0) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the analytics profile.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OndemandMetricsIdleTimeout

This flag sets the time duration of no live data traffic after which virtual service metrics processing is suspended. It is applicable only when enable_ondemand_metrics is set to false. Field introduced in 18.1.1. Unit is seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RespCodeBlock

Block of http response codes to be excluded from being classified as an error. Enum options - AP_HTTP_RSP_4XX, AP_HTTP_RSP_5XX.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SipLogDepth

Maximum number of sip messages added in logs for a sip transaction. By default, this value is 20. Allowed values are 1-1000. Field introduced in 17.2.13, 18.1.5, 18.2.1. Allowed in basic(allowed values- 20) edition, essentials(allowed values- 20) edition, enterprise edition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

It is a reference to an object of type tenant.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientLogConfig

_Required_: No

_Type_: List of <a href="clientlogconfigdefinition.md">ClientLogConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientLogStreamingConfig

_Required_: No

_Type_: List of <a href="clientlogstreamingconfigdefinition.md">ClientLogStreamingConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Markers

_Required_: No

_Type_: List of <a href="markersdefinition.md">MarkersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ranges

_Required_: No

_Type_: List of <a href="rangesdefinition.md">RangesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SensitiveLogProfile

_Required_: No

_Type_: List of <a href="sensitivelogprofiledefinition.md">SensitiveLogProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

