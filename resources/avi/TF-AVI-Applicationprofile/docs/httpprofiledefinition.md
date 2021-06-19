# TF::AVI::Applicationprofile HttpProfileDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowdotsinheadername" title="AllowDotsInHeaderName">AllowDotsInHeaderName</a>" : <i>Boolean</i>,
    "<a href="#clientbodytimeout" title="ClientBodyTimeout">ClientBodyTimeout</a>" : <i>Double</i>,
    "<a href="#clientheadertimeout" title="ClientHeaderTimeout">ClientHeaderTimeout</a>" : <i>Double</i>,
    "<a href="#clientmaxbodysize" title="ClientMaxBodySize">ClientMaxBodySize</a>" : <i>Double</i>,
    "<a href="#clientmaxheadersize" title="ClientMaxHeaderSize">ClientMaxHeaderSize</a>" : <i>Double</i>,
    "<a href="#clientmaxrequestsize" title="ClientMaxRequestSize">ClientMaxRequestSize</a>" : <i>Double</i>,
    "<a href="#connectionmultiplexingenabled" title="ConnectionMultiplexingEnabled">ConnectionMultiplexingEnabled</a>" : <i>Boolean</i>,
    "<a href="#detectntlmapp" title="DetectNtlmApp">DetectNtlmApp</a>" : <i>Boolean</i>,
    "<a href="#disablekeepalivepostsmsie6" title="DisableKeepalivePostsMsie6">DisableKeepalivePostsMsie6</a>" : <i>Boolean</i>,
    "<a href="#disablesnihostnamecheck" title="DisableSniHostnameCheck">DisableSniHostnameCheck</a>" : <i>Boolean</i>,
    "<a href="#enablechunkmerge" title="EnableChunkMerge">EnableChunkMerge</a>" : <i>Boolean</i>,
    "<a href="#enablefireandforget" title="EnableFireAndForget">EnableFireAndForget</a>" : <i>Boolean</i>,
    "<a href="#enablerequestbodybuffering" title="EnableRequestBodyBuffering">EnableRequestBodyBuffering</a>" : <i>Boolean</i>,
    "<a href="#enablerequestbodymetrics" title="EnableRequestBodyMetrics">EnableRequestBodyMetrics</a>" : <i>Boolean</i>,
    "<a href="#fwdclosehdrforboundconnections" title="FwdCloseHdrForBoundConnections">FwdCloseHdrForBoundConnections</a>" : <i>Boolean</i>,
    "<a href="#hstsenabled" title="HstsEnabled">HstsEnabled</a>" : <i>Boolean</i>,
    "<a href="#hstsmaxage" title="HstsMaxAge">HstsMaxAge</a>" : <i>Double</i>,
    "<a href="#hstssubdomainsenabled" title="HstsSubdomainsEnabled">HstsSubdomainsEnabled</a>" : <i>Boolean</i>,
    "<a href="#httptohttps" title="HttpToHttps">HttpToHttps</a>" : <i>Boolean</i>,
    "<a href="#httpupstreambuffersize" title="HttpUpstreamBufferSize">HttpUpstreamBufferSize</a>" : <i>Double</i>,
    "<a href="#httponlyenabled" title="HttponlyEnabled">HttponlyEnabled</a>" : <i>Boolean</i>,
    "<a href="#keepaliveheader" title="KeepaliveHeader">KeepaliveHeader</a>" : <i>Boolean</i>,
    "<a href="#keepalivetimeout" title="KeepaliveTimeout">KeepaliveTimeout</a>" : <i>Double</i>,
    "<a href="#maxbadrpscip" title="MaxBadRpsCip">MaxBadRpsCip</a>" : <i>Double</i>,
    "<a href="#maxbadrpscipuri" title="MaxBadRpsCipUri">MaxBadRpsCipUri</a>" : <i>Double</i>,
    "<a href="#maxbadrpsuri" title="MaxBadRpsUri">MaxBadRpsUri</a>" : <i>Double</i>,
    "<a href="#maxkeepaliverequests" title="MaxKeepaliveRequests">MaxKeepaliveRequests</a>" : <i>Double</i>,
    "<a href="#maxresponseheaderssize" title="MaxResponseHeadersSize">MaxResponseHeadersSize</a>" : <i>Double</i>,
    "<a href="#maxrpscip" title="MaxRpsCip">MaxRpsCip</a>" : <i>Double</i>,
    "<a href="#maxrpscipuri" title="MaxRpsCipUri">MaxRpsCipUri</a>" : <i>Double</i>,
    "<a href="#maxrpsunknowncip" title="MaxRpsUnknownCip">MaxRpsUnknownCip</a>" : <i>Double</i>,
    "<a href="#maxrpsunknownuri" title="MaxRpsUnknownUri">MaxRpsUnknownUri</a>" : <i>Double</i>,
    "<a href="#maxrpsuri" title="MaxRpsUri">MaxRpsUri</a>" : <i>Double</i>,
    "<a href="#pkiprofileref" title="PkiProfileRef">PkiProfileRef</a>" : <i>String</i>,
    "<a href="#postaccepttimeout" title="PostAcceptTimeout">PostAcceptTimeout</a>" : <i>Double</i>,
    "<a href="#resetconnhttponsslport" title="ResetConnHttpOnSslPort">ResetConnHttpOnSslPort</a>" : <i>Boolean</i>,
    "<a href="#respondwith100continue" title="RespondWith100Continue">RespondWith100Continue</a>" : <i>Boolean</i>,
    "<a href="#securecookieenabled" title="SecureCookieEnabled">SecureCookieEnabled</a>" : <i>Boolean</i>,
    "<a href="#serversideredirecttohttps" title="ServerSideRedirectToHttps">ServerSideRedirectToHttps</a>" : <i>Boolean</i>,
    "<a href="#sslclientcertificatemode" title="SslClientCertificateMode">SslClientCertificateMode</a>" : <i>String</i>,
    "<a href="#useappkeepalivetimeout" title="UseAppKeepaliveTimeout">UseAppKeepaliveTimeout</a>" : <i>Boolean</i>,
    "<a href="#websocketsenabled" title="WebsocketsEnabled">WebsocketsEnabled</a>" : <i>Boolean</i>,
    "<a href="#xforwardedprotoenabled" title="XForwardedProtoEnabled">XForwardedProtoEnabled</a>" : <i>Boolean</i>,
    "<a href="#xffalternatename" title="XffAlternateName">XffAlternateName</a>" : <i>String</i>,
    "<a href="#xffenabled" title="XffEnabled">XffEnabled</a>" : <i>Boolean</i>,
    "<a href="#cacheconfig" title="CacheConfig">CacheConfig</a>" : <i>[ <a href="cacheconfigdefinition.md">CacheConfigDefinition</a>, ... ]</i>,
    "<a href="#compressionprofile" title="CompressionProfile">CompressionProfile</a>" : <i>[ <a href="compressionprofiledefinition.md">CompressionProfileDefinition</a>, ... ]</i>,
    "<a href="#http2profile" title="Http2Profile">Http2Profile</a>" : <i>[ <a href="http2profiledefinition.md">Http2ProfileDefinition</a>, ... ]</i>,
    "<a href="#sslclientcertificateaction" title="SslClientCertificateAction">SslClientCertificateAction</a>" : <i>[ <a href="sslclientcertificateactiondefinition.md">SslClientCertificateActionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#allowdotsinheadername" title="AllowDotsInHeaderName">AllowDotsInHeaderName</a>: <i>Boolean</i>
<a href="#clientbodytimeout" title="ClientBodyTimeout">ClientBodyTimeout</a>: <i>Double</i>
<a href="#clientheadertimeout" title="ClientHeaderTimeout">ClientHeaderTimeout</a>: <i>Double</i>
<a href="#clientmaxbodysize" title="ClientMaxBodySize">ClientMaxBodySize</a>: <i>Double</i>
<a href="#clientmaxheadersize" title="ClientMaxHeaderSize">ClientMaxHeaderSize</a>: <i>Double</i>
<a href="#clientmaxrequestsize" title="ClientMaxRequestSize">ClientMaxRequestSize</a>: <i>Double</i>
<a href="#connectionmultiplexingenabled" title="ConnectionMultiplexingEnabled">ConnectionMultiplexingEnabled</a>: <i>Boolean</i>
<a href="#detectntlmapp" title="DetectNtlmApp">DetectNtlmApp</a>: <i>Boolean</i>
<a href="#disablekeepalivepostsmsie6" title="DisableKeepalivePostsMsie6">DisableKeepalivePostsMsie6</a>: <i>Boolean</i>
<a href="#disablesnihostnamecheck" title="DisableSniHostnameCheck">DisableSniHostnameCheck</a>: <i>Boolean</i>
<a href="#enablechunkmerge" title="EnableChunkMerge">EnableChunkMerge</a>: <i>Boolean</i>
<a href="#enablefireandforget" title="EnableFireAndForget">EnableFireAndForget</a>: <i>Boolean</i>
<a href="#enablerequestbodybuffering" title="EnableRequestBodyBuffering">EnableRequestBodyBuffering</a>: <i>Boolean</i>
<a href="#enablerequestbodymetrics" title="EnableRequestBodyMetrics">EnableRequestBodyMetrics</a>: <i>Boolean</i>
<a href="#fwdclosehdrforboundconnections" title="FwdCloseHdrForBoundConnections">FwdCloseHdrForBoundConnections</a>: <i>Boolean</i>
<a href="#hstsenabled" title="HstsEnabled">HstsEnabled</a>: <i>Boolean</i>
<a href="#hstsmaxage" title="HstsMaxAge">HstsMaxAge</a>: <i>Double</i>
<a href="#hstssubdomainsenabled" title="HstsSubdomainsEnabled">HstsSubdomainsEnabled</a>: <i>Boolean</i>
<a href="#httptohttps" title="HttpToHttps">HttpToHttps</a>: <i>Boolean</i>
<a href="#httpupstreambuffersize" title="HttpUpstreamBufferSize">HttpUpstreamBufferSize</a>: <i>Double</i>
<a href="#httponlyenabled" title="HttponlyEnabled">HttponlyEnabled</a>: <i>Boolean</i>
<a href="#keepaliveheader" title="KeepaliveHeader">KeepaliveHeader</a>: <i>Boolean</i>
<a href="#keepalivetimeout" title="KeepaliveTimeout">KeepaliveTimeout</a>: <i>Double</i>
<a href="#maxbadrpscip" title="MaxBadRpsCip">MaxBadRpsCip</a>: <i>Double</i>
<a href="#maxbadrpscipuri" title="MaxBadRpsCipUri">MaxBadRpsCipUri</a>: <i>Double</i>
<a href="#maxbadrpsuri" title="MaxBadRpsUri">MaxBadRpsUri</a>: <i>Double</i>
<a href="#maxkeepaliverequests" title="MaxKeepaliveRequests">MaxKeepaliveRequests</a>: <i>Double</i>
<a href="#maxresponseheaderssize" title="MaxResponseHeadersSize">MaxResponseHeadersSize</a>: <i>Double</i>
<a href="#maxrpscip" title="MaxRpsCip">MaxRpsCip</a>: <i>Double</i>
<a href="#maxrpscipuri" title="MaxRpsCipUri">MaxRpsCipUri</a>: <i>Double</i>
<a href="#maxrpsunknowncip" title="MaxRpsUnknownCip">MaxRpsUnknownCip</a>: <i>Double</i>
<a href="#maxrpsunknownuri" title="MaxRpsUnknownUri">MaxRpsUnknownUri</a>: <i>Double</i>
<a href="#maxrpsuri" title="MaxRpsUri">MaxRpsUri</a>: <i>Double</i>
<a href="#pkiprofileref" title="PkiProfileRef">PkiProfileRef</a>: <i>String</i>
<a href="#postaccepttimeout" title="PostAcceptTimeout">PostAcceptTimeout</a>: <i>Double</i>
<a href="#resetconnhttponsslport" title="ResetConnHttpOnSslPort">ResetConnHttpOnSslPort</a>: <i>Boolean</i>
<a href="#respondwith100continue" title="RespondWith100Continue">RespondWith100Continue</a>: <i>Boolean</i>
<a href="#securecookieenabled" title="SecureCookieEnabled">SecureCookieEnabled</a>: <i>Boolean</i>
<a href="#serversideredirecttohttps" title="ServerSideRedirectToHttps">ServerSideRedirectToHttps</a>: <i>Boolean</i>
<a href="#sslclientcertificatemode" title="SslClientCertificateMode">SslClientCertificateMode</a>: <i>String</i>
<a href="#useappkeepalivetimeout" title="UseAppKeepaliveTimeout">UseAppKeepaliveTimeout</a>: <i>Boolean</i>
<a href="#websocketsenabled" title="WebsocketsEnabled">WebsocketsEnabled</a>: <i>Boolean</i>
<a href="#xforwardedprotoenabled" title="XForwardedProtoEnabled">XForwardedProtoEnabled</a>: <i>Boolean</i>
<a href="#xffalternatename" title="XffAlternateName">XffAlternateName</a>: <i>String</i>
<a href="#xffenabled" title="XffEnabled">XffEnabled</a>: <i>Boolean</i>
<a href="#cacheconfig" title="CacheConfig">CacheConfig</a>: <i>
      - <a href="cacheconfigdefinition.md">CacheConfigDefinition</a></i>
<a href="#compressionprofile" title="CompressionProfile">CompressionProfile</a>: <i>
      - <a href="compressionprofiledefinition.md">CompressionProfileDefinition</a></i>
<a href="#http2profile" title="Http2Profile">Http2Profile</a>: <i>
      - <a href="http2profiledefinition.md">Http2ProfileDefinition</a></i>
<a href="#sslclientcertificateaction" title="SslClientCertificateAction">SslClientCertificateAction</a>: <i>
      - <a href="sslclientcertificateactiondefinition.md">SslClientCertificateActionDefinition</a></i>
</pre>

## Properties

#### AllowDotsInHeaderName

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientBodyTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientHeaderTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientMaxBodySize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientMaxHeaderSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientMaxRequestSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionMultiplexingEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DetectNtlmApp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableKeepalivePostsMsie6

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableSniHostnameCheck

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableChunkMerge

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableFireAndForget

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableRequestBodyBuffering

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableRequestBodyMetrics

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FwdCloseHdrForBoundConnections

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HstsEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HstsMaxAge

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HstsSubdomainsEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpToHttps

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpUpstreamBufferSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttponlyEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepaliveHeader

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepaliveTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxBadRpsCip

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxBadRpsCipUri

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxBadRpsUri

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxKeepaliveRequests

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxResponseHeadersSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRpsCip

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRpsCipUri

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRpsUnknownCip

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRpsUnknownUri

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRpsUri

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PkiProfileRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PostAcceptTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResetConnHttpOnSslPort

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RespondWith100Continue

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecureCookieEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerSideRedirectToHttps

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslClientCertificateMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseAppKeepaliveTimeout

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebsocketsEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### XForwardedProtoEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### XffAlternateName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### XffEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheConfig

_Required_: No

_Type_: List of <a href="cacheconfigdefinition.md">CacheConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompressionProfile

_Required_: No

_Type_: List of <a href="compressionprofiledefinition.md">CompressionProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Http2Profile

_Required_: No

_Type_: List of <a href="http2profiledefinition.md">Http2ProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslClientCertificateAction

_Required_: No

_Type_: List of <a href="sslclientcertificateactiondefinition.md">SslClientCertificateActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

