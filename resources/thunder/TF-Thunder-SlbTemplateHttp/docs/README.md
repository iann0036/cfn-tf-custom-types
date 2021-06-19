# TF::Thunder::SlbTemplateHttp

`thunder_slb_template_http` Provides details about thunder slb template http

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SlbTemplateHttp",
    "Properties" : {
        "<a href="#100contwaitforreqcomplete" title="100ContWaitForReqComplete">100ContWaitForReqComplete</a>" : <i>Double</i>,
        "<a href="#bypasssg" title="BypassSg">BypassSg</a>" : <i>String</i>,
        "<a href="#clientiphdrreplace" title="ClientIpHdrReplace">ClientIpHdrReplace</a>" : <i>Double</i>,
        "<a href="#clientporthdrreplace" title="ClientPortHdrReplace">ClientPortHdrReplace</a>" : <i>Double</i>,
        "<a href="#compressionautodisableonhighcpu" title="CompressionAutoDisableOnHighCpu">CompressionAutoDisableOnHighCpu</a>" : <i>Double</i>,
        "<a href="#compressionenable" title="CompressionEnable">CompressionEnable</a>" : <i>Double</i>,
        "<a href="#compressionkeepacceptencoding" title="CompressionKeepAcceptEncoding">CompressionKeepAcceptEncoding</a>" : <i>Double</i>,
        "<a href="#compressionkeepacceptencodingenable" title="CompressionKeepAcceptEncodingEnable">CompressionKeepAcceptEncodingEnable</a>" : <i>Double</i>,
        "<a href="#compressionlevel" title="CompressionLevel">CompressionLevel</a>" : <i>Double</i>,
        "<a href="#compressionminimumcontentlength" title="CompressionMinimumContentLength">CompressionMinimumContentLength</a>" : <i>Double</i>,
        "<a href="#cookieformat" title="CookieFormat">CookieFormat</a>" : <i>String</i>,
        "<a href="#failoverurl" title="FailoverUrl">FailoverUrl</a>" : <i>String</i>,
        "<a href="#insertclientip" title="InsertClientIp">InsertClientIp</a>" : <i>Double</i>,
        "<a href="#insertclientipheadername" title="InsertClientIpHeaderName">InsertClientIpHeaderName</a>" : <i>String</i>,
        "<a href="#insertclientport" title="InsertClientPort">InsertClientPort</a>" : <i>Double</i>,
        "<a href="#insertclientportheadername" title="InsertClientPortHeaderName">InsertClientPortHeaderName</a>" : <i>String</i>,
        "<a href="#keepclientalive" title="KeepClientAlive">KeepClientAlive</a>" : <i>Double</i>,
        "<a href="#logretry" title="LogRetry">LogRetry</a>" : <i>Double</i>,
        "<a href="#maxconcurrentstreams" title="MaxConcurrentStreams">MaxConcurrentStreams</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nonhttpbypass" title="NonHttpBypass">NonHttpBypass</a>" : <i>Double</i>,
        "<a href="#persiston401" title="PersistOn401">PersistOn401</a>" : <i>Double</i>,
        "<a href="#rdport" title="RdPort">RdPort</a>" : <i>Double</i>,
        "<a href="#rdrespcode" title="RdRespCode">RdRespCode</a>" : <i>String</i>,
        "<a href="#rdsecure" title="RdSecure">RdSecure</a>" : <i>Double</i>,
        "<a href="#rdsimpleloc" title="RdSimpleLoc">RdSimpleLoc</a>" : <i>String</i>,
        "<a href="#redirect" title="Redirect">Redirect</a>" : <i>Double</i>,
        "<a href="#reqhdrwaittime" title="ReqHdrWaitTime">ReqHdrWaitTime</a>" : <i>Double</i>,
        "<a href="#reqhdrwaittimeval" title="ReqHdrWaitTimeVal">ReqHdrWaitTimeVal</a>" : <i>Double</i>,
        "<a href="#requestlinecaseinsensitive" title="RequestLineCaseInsensitive">RequestLineCaseInsensitive</a>" : <i>Double</i>,
        "<a href="#requesttimeout" title="RequestTimeout">RequestTimeout</a>" : <i>Double</i>,
        "<a href="#retryon5xx" title="RetryOn5xx">RetryOn5xx</a>" : <i>Double</i>,
        "<a href="#retryon5xxperreq" title="RetryOn5xxPerReq">RetryOn5xxPerReq</a>" : <i>Double</i>,
        "<a href="#retryon5xxperreqval" title="RetryOn5xxPerReqVal">RetryOn5xxPerReqVal</a>" : <i>Double</i>,
        "<a href="#retryon5xxval" title="RetryOn5xxVal">RetryOn5xxVal</a>" : <i>Double</i>,
        "<a href="#stricttransactionswitch" title="StrictTransactionSwitch">StrictTransactionSwitch</a>" : <i>Double</i>,
        "<a href="#term11clienthdrconnclose" title="Term11clientHdrConnClose">Term11clientHdrConnClose</a>" : <i>Double</i>,
        "<a href="#urlhashfirst" title="UrlHashFirst">UrlHashFirst</a>" : <i>Double</i>,
        "<a href="#urlhashlast" title="UrlHashLast">UrlHashLast</a>" : <i>Double</i>,
        "<a href="#urlhashoffset" title="UrlHashOffset">UrlHashOffset</a>" : <i>Double</i>,
        "<a href="#urlhashpersist" title="UrlHashPersist">UrlHashPersist</a>" : <i>Double</i>,
        "<a href="#useserverstatus" title="UseServerStatus">UseServerStatus</a>" : <i>Double</i>,
        "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#compressioncontenttype" title="CompressionContentType">CompressionContentType</a>" : <i>[ <a href="compressioncontenttypedefinition.md">CompressionContentTypeDefinition</a>, ... ]</i>,
        "<a href="#compressionexcludecontenttype" title="CompressionExcludeContentType">CompressionExcludeContentType</a>" : <i>[ <a href="compressionexcludecontenttypedefinition.md">CompressionExcludeContentTypeDefinition</a>, ... ]</i>,
        "<a href="#compressionexcludeuri" title="CompressionExcludeUri">CompressionExcludeUri</a>" : <i>[ <a href="compressionexcludeuridefinition.md">CompressionExcludeUriDefinition</a>, ... ]</i>,
        "<a href="#hostswitching" title="HostSwitching">HostSwitching</a>" : <i>[ <a href="hostswitchingdefinition.md">HostSwitchingDefinition</a>, ... ]</i>,
        "<a href="#redirectrewrite" title="RedirectRewrite">RedirectRewrite</a>" : <i>[ <a href="redirectrewritedefinition.md">RedirectRewriteDefinition</a>, ... ]</i>,
        "<a href="#requestheadereraselist" title="RequestHeaderEraseList">RequestHeaderEraseList</a>" : <i>[ <a href="requestheadereraselistdefinition.md">RequestHeaderEraseListDefinition</a>, ... ]</i>,
        "<a href="#requestheaderinsertlist" title="RequestHeaderInsertList">RequestHeaderInsertList</a>" : <i>[ <a href="requestheaderinsertlistdefinition.md">RequestHeaderInsertListDefinition</a>, ... ]</i>,
        "<a href="#responsecontentreplacelist" title="ResponseContentReplaceList">ResponseContentReplaceList</a>" : <i>[ <a href="responsecontentreplacelistdefinition.md">ResponseContentReplaceListDefinition</a>, ... ]</i>,
        "<a href="#responseheadereraselist" title="ResponseHeaderEraseList">ResponseHeaderEraseList</a>" : <i>[ <a href="responseheadereraselistdefinition.md">ResponseHeaderEraseListDefinition</a>, ... ]</i>,
        "<a href="#responseheaderinsertlist" title="ResponseHeaderInsertList">ResponseHeaderInsertList</a>" : <i>[ <a href="responseheaderinsertlistdefinition.md">ResponseHeaderInsertListDefinition</a>, ... ]</i>,
        "<a href="#template" title="Template">Template</a>" : <i>[ <a href="templatedefinition.md">TemplateDefinition</a>, ... ]</i>,
        "<a href="#urlswitching" title="UrlSwitching">UrlSwitching</a>" : <i>[ <a href="urlswitchingdefinition.md">UrlSwitchingDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SlbTemplateHttp
Properties:
    <a href="#100contwaitforreqcomplete" title="100ContWaitForReqComplete">100ContWaitForReqComplete</a>: <i>Double</i>
    <a href="#bypasssg" title="BypassSg">BypassSg</a>: <i>String</i>
    <a href="#clientiphdrreplace" title="ClientIpHdrReplace">ClientIpHdrReplace</a>: <i>Double</i>
    <a href="#clientporthdrreplace" title="ClientPortHdrReplace">ClientPortHdrReplace</a>: <i>Double</i>
    <a href="#compressionautodisableonhighcpu" title="CompressionAutoDisableOnHighCpu">CompressionAutoDisableOnHighCpu</a>: <i>Double</i>
    <a href="#compressionenable" title="CompressionEnable">CompressionEnable</a>: <i>Double</i>
    <a href="#compressionkeepacceptencoding" title="CompressionKeepAcceptEncoding">CompressionKeepAcceptEncoding</a>: <i>Double</i>
    <a href="#compressionkeepacceptencodingenable" title="CompressionKeepAcceptEncodingEnable">CompressionKeepAcceptEncodingEnable</a>: <i>Double</i>
    <a href="#compressionlevel" title="CompressionLevel">CompressionLevel</a>: <i>Double</i>
    <a href="#compressionminimumcontentlength" title="CompressionMinimumContentLength">CompressionMinimumContentLength</a>: <i>Double</i>
    <a href="#cookieformat" title="CookieFormat">CookieFormat</a>: <i>String</i>
    <a href="#failoverurl" title="FailoverUrl">FailoverUrl</a>: <i>String</i>
    <a href="#insertclientip" title="InsertClientIp">InsertClientIp</a>: <i>Double</i>
    <a href="#insertclientipheadername" title="InsertClientIpHeaderName">InsertClientIpHeaderName</a>: <i>String</i>
    <a href="#insertclientport" title="InsertClientPort">InsertClientPort</a>: <i>Double</i>
    <a href="#insertclientportheadername" title="InsertClientPortHeaderName">InsertClientPortHeaderName</a>: <i>String</i>
    <a href="#keepclientalive" title="KeepClientAlive">KeepClientAlive</a>: <i>Double</i>
    <a href="#logretry" title="LogRetry">LogRetry</a>: <i>Double</i>
    <a href="#maxconcurrentstreams" title="MaxConcurrentStreams">MaxConcurrentStreams</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nonhttpbypass" title="NonHttpBypass">NonHttpBypass</a>: <i>Double</i>
    <a href="#persiston401" title="PersistOn401">PersistOn401</a>: <i>Double</i>
    <a href="#rdport" title="RdPort">RdPort</a>: <i>Double</i>
    <a href="#rdrespcode" title="RdRespCode">RdRespCode</a>: <i>String</i>
    <a href="#rdsecure" title="RdSecure">RdSecure</a>: <i>Double</i>
    <a href="#rdsimpleloc" title="RdSimpleLoc">RdSimpleLoc</a>: <i>String</i>
    <a href="#redirect" title="Redirect">Redirect</a>: <i>Double</i>
    <a href="#reqhdrwaittime" title="ReqHdrWaitTime">ReqHdrWaitTime</a>: <i>Double</i>
    <a href="#reqhdrwaittimeval" title="ReqHdrWaitTimeVal">ReqHdrWaitTimeVal</a>: <i>Double</i>
    <a href="#requestlinecaseinsensitive" title="RequestLineCaseInsensitive">RequestLineCaseInsensitive</a>: <i>Double</i>
    <a href="#requesttimeout" title="RequestTimeout">RequestTimeout</a>: <i>Double</i>
    <a href="#retryon5xx" title="RetryOn5xx">RetryOn5xx</a>: <i>Double</i>
    <a href="#retryon5xxperreq" title="RetryOn5xxPerReq">RetryOn5xxPerReq</a>: <i>Double</i>
    <a href="#retryon5xxperreqval" title="RetryOn5xxPerReqVal">RetryOn5xxPerReqVal</a>: <i>Double</i>
    <a href="#retryon5xxval" title="RetryOn5xxVal">RetryOn5xxVal</a>: <i>Double</i>
    <a href="#stricttransactionswitch" title="StrictTransactionSwitch">StrictTransactionSwitch</a>: <i>Double</i>
    <a href="#term11clienthdrconnclose" title="Term11clientHdrConnClose">Term11clientHdrConnClose</a>: <i>Double</i>
    <a href="#urlhashfirst" title="UrlHashFirst">UrlHashFirst</a>: <i>Double</i>
    <a href="#urlhashlast" title="UrlHashLast">UrlHashLast</a>: <i>Double</i>
    <a href="#urlhashoffset" title="UrlHashOffset">UrlHashOffset</a>: <i>Double</i>
    <a href="#urlhashpersist" title="UrlHashPersist">UrlHashPersist</a>: <i>Double</i>
    <a href="#useserverstatus" title="UseServerStatus">UseServerStatus</a>: <i>Double</i>
    <a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#compressioncontenttype" title="CompressionContentType">CompressionContentType</a>: <i>
      - <a href="compressioncontenttypedefinition.md">CompressionContentTypeDefinition</a></i>
    <a href="#compressionexcludecontenttype" title="CompressionExcludeContentType">CompressionExcludeContentType</a>: <i>
      - <a href="compressionexcludecontenttypedefinition.md">CompressionExcludeContentTypeDefinition</a></i>
    <a href="#compressionexcludeuri" title="CompressionExcludeUri">CompressionExcludeUri</a>: <i>
      - <a href="compressionexcludeuridefinition.md">CompressionExcludeUriDefinition</a></i>
    <a href="#hostswitching" title="HostSwitching">HostSwitching</a>: <i>
      - <a href="hostswitchingdefinition.md">HostSwitchingDefinition</a></i>
    <a href="#redirectrewrite" title="RedirectRewrite">RedirectRewrite</a>: <i>
      - <a href="redirectrewritedefinition.md">RedirectRewriteDefinition</a></i>
    <a href="#requestheadereraselist" title="RequestHeaderEraseList">RequestHeaderEraseList</a>: <i>
      - <a href="requestheadereraselistdefinition.md">RequestHeaderEraseListDefinition</a></i>
    <a href="#requestheaderinsertlist" title="RequestHeaderInsertList">RequestHeaderInsertList</a>: <i>
      - <a href="requestheaderinsertlistdefinition.md">RequestHeaderInsertListDefinition</a></i>
    <a href="#responsecontentreplacelist" title="ResponseContentReplaceList">ResponseContentReplaceList</a>: <i>
      - <a href="responsecontentreplacelistdefinition.md">ResponseContentReplaceListDefinition</a></i>
    <a href="#responseheadereraselist" title="ResponseHeaderEraseList">ResponseHeaderEraseList</a>: <i>
      - <a href="responseheadereraselistdefinition.md">ResponseHeaderEraseListDefinition</a></i>
    <a href="#responseheaderinsertlist" title="ResponseHeaderInsertList">ResponseHeaderInsertList</a>: <i>
      - <a href="responseheaderinsertlistdefinition.md">ResponseHeaderInsertListDefinition</a></i>
    <a href="#template" title="Template">Template</a>: <i>
      - <a href="templatedefinition.md">TemplateDefinition</a></i>
    <a href="#urlswitching" title="UrlSwitching">UrlSwitching</a>: <i>
      - <a href="urlswitchingdefinition.md">UrlSwitchingDefinition</a></i>
</pre>

## Properties

#### 100ContWaitForReqComplete

When REQ has Expect 100 and response is not 100, then wait for whole request to be sent.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BypassSg

Select service group for non-http traffic (Service Group Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientIpHdrReplace

Replace the existing header.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientPortHdrReplace

Replace the existing header.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompressionAutoDisableOnHighCpu

Auto-disable software compression on high cpu usage (Disable compression if cpu usage is above threshold. Default is off.).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompressionEnable

Enable Compression.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompressionKeepAcceptEncoding

Keep accept encoding.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompressionKeepAcceptEncodingEnable

Enable Server Accept Encoding.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompressionLevel

compression level, default 1 (compression level value, default is 1).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompressionMinimumContentLength

Minimum Content Length (Minimum content length for compression in bytes. Default is 120.).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CookieFormat

‘rfc6265’: Follow rfc6265;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailoverUrl

Failover to this URL (Failover URL Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsertClientIp

Insert Client IP address into HTTP header.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsertClientIpHeaderName

HTTP Header Name for inserting Client IP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsertClientPort

Insert Client Port address into HTTP header.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsertClientPortHeaderName

HTTP Header Name for inserting Client Port.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepClientAlive

Keep client alive.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogRetry

log when HTTP request retry.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxConcurrentStreams

Max concurrent streams, default 100.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

HTTP Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NonHttpBypass

Bypass non-http traffic instead of dropping.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PersistOn401

Persist to the same server if the response code is 401.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RdPort

Port (Port Number).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RdRespCode

‘301’: Moved Permanently; ‘302’: Found; ‘303’: See Other; ‘307’: Temporary Redirect;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RdSecure

Use HTTPS.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RdSimpleLoc

Redirect location tag absolute URI string.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Redirect

Automatically send a redirect response.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReqHdrWaitTime

HTTP request header wait time before abort connection.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReqHdrWaitTimeVal

Number of seconds wait for client request header (default is 7).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestLineCaseInsensitive

Parse http request line as case insensitive.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestTimeout

Request timeout if response not received (timeout in seconds).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryOn5xx

Retry http request on HTTP 5xx code.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryOn5xxPerReq

Retry http request on HTTP 5xx code for each request.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryOn5xxPerReqVal

Number of times to retry (default is 3).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryOn5xxVal

Number of times to retry (default is 3).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StrictTransactionSwitch

Force server selection on every HTTP request.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Term11clientHdrConnClose

Terminate HTTP 1.1 client when req has Connection: close.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlHashFirst

Use the begining part of URL to calculate hash value (URL string length to calculate hash value).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlHashLast

Use the end part of URL to calculate hash value (URL string length to calculate hash value).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlHashOffset

Skip part of URL to calculate hash value (Offset of the URL string).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlHashPersist

Use URL’s hash value to select server.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseServerStatus

Use Server-Status header to do URL hashing.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserTag

Customized tag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompressionContentType

_Required_: No

_Type_: List of <a href="compressioncontenttypedefinition.md">CompressionContentTypeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompressionExcludeContentType

_Required_: No

_Type_: List of <a href="compressionexcludecontenttypedefinition.md">CompressionExcludeContentTypeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompressionExcludeUri

_Required_: No

_Type_: List of <a href="compressionexcludeuridefinition.md">CompressionExcludeUriDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostSwitching

_Required_: No

_Type_: List of <a href="hostswitchingdefinition.md">HostSwitchingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectRewrite

_Required_: No

_Type_: List of <a href="redirectrewritedefinition.md">RedirectRewriteDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestHeaderEraseList

_Required_: No

_Type_: List of <a href="requestheadereraselistdefinition.md">RequestHeaderEraseListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestHeaderInsertList

_Required_: No

_Type_: List of <a href="requestheaderinsertlistdefinition.md">RequestHeaderInsertListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseContentReplaceList

_Required_: No

_Type_: List of <a href="responsecontentreplacelistdefinition.md">ResponseContentReplaceListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseHeaderEraseList

_Required_: No

_Type_: List of <a href="responseheadereraselistdefinition.md">ResponseHeaderEraseListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseHeaderInsertList

_Required_: No

_Type_: List of <a href="responseheaderinsertlistdefinition.md">ResponseHeaderInsertListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

_Required_: No

_Type_: List of <a href="templatedefinition.md">TemplateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlSwitching

_Required_: No

_Type_: List of <a href="urlswitchingdefinition.md">UrlSwitchingDefinition</a>

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

