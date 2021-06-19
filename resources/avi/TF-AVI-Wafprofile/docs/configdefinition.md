# TF::AVI::Wafprofile ConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowedhttpversions" title="AllowedHttpVersions">AllowedHttpVersions</a>" : <i>[ String, ... ]</i>,
    "<a href="#allowedmethods" title="AllowedMethods">AllowedMethods</a>" : <i>[ String, ... ]</i>,
    "<a href="#allowedrequestcontenttypes" title="AllowedRequestContentTypes">AllowedRequestContentTypes</a>" : <i>[ String, ... ]</i>,
    "<a href="#argumentseparator" title="ArgumentSeparator">ArgumentSeparator</a>" : <i>String</i>,
    "<a href="#clientrequestmaxbodysize" title="ClientRequestMaxBodySize">ClientRequestMaxBodySize</a>" : <i>Double</i>,
    "<a href="#cookieformatversion" title="CookieFormatVersion">CookieFormatVersion</a>" : <i>Double</i>,
    "<a href="#ignoreincompleterequestbodyerror" title="IgnoreIncompleteRequestBodyError">IgnoreIncompleteRequestBodyError</a>" : <i>Boolean</i>,
    "<a href="#maxexecutiontime" title="MaxExecutionTime">MaxExecutionTime</a>" : <i>Double</i>,
    "<a href="#regexmatchlimit" title="RegexMatchLimit">RegexMatchLimit</a>" : <i>Double</i>,
    "<a href="#regexrecursionlimit" title="RegexRecursionLimit">RegexRecursionLimit</a>" : <i>Double</i>,
    "<a href="#requestbodydefaultaction" title="RequestBodyDefaultAction">RequestBodyDefaultAction</a>" : <i>String</i>,
    "<a href="#requesthdrdefaultaction" title="RequestHdrDefaultAction">RequestHdrDefaultAction</a>" : <i>String</i>,
    "<a href="#responsebodydefaultaction" title="ResponseBodyDefaultAction">ResponseBodyDefaultAction</a>" : <i>String</i>,
    "<a href="#responsehdrdefaultaction" title="ResponseHdrDefaultAction">ResponseHdrDefaultAction</a>" : <i>String</i>,
    "<a href="#restrictedextensions" title="RestrictedExtensions">RestrictedExtensions</a>" : <i>[ String, ... ]</i>,
    "<a href="#restrictedheaders" title="RestrictedHeaders">RestrictedHeaders</a>" : <i>[ String, ... ]</i>,
    "<a href="#sendstatusheader" title="SendStatusHeader">SendStatusHeader</a>" : <i>Boolean</i>,
    "<a href="#serverresponsemaxbodysize" title="ServerResponseMaxBodySize">ServerResponseMaxBodySize</a>" : <i>Double</i>,
    "<a href="#staticextensions" title="StaticExtensions">StaticExtensions</a>" : <i>[ String, ... ]</i>,
    "<a href="#statuscodeforrejectedrequests" title="StatusCodeForRejectedRequests">StatusCodeForRejectedRequests</a>" : <i>String</i>,
    "<a href="#statusheadername" title="StatusHeaderName">StatusHeaderName</a>" : <i>String</i>,
    "<a href="#xmlxxeprotection" title="XmlXxeProtection">XmlXxeProtection</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#allowedhttpversions" title="AllowedHttpVersions">AllowedHttpVersions</a>: <i>
      - String</i>
<a href="#allowedmethods" title="AllowedMethods">AllowedMethods</a>: <i>
      - String</i>
<a href="#allowedrequestcontenttypes" title="AllowedRequestContentTypes">AllowedRequestContentTypes</a>: <i>
      - String</i>
<a href="#argumentseparator" title="ArgumentSeparator">ArgumentSeparator</a>: <i>String</i>
<a href="#clientrequestmaxbodysize" title="ClientRequestMaxBodySize">ClientRequestMaxBodySize</a>: <i>Double</i>
<a href="#cookieformatversion" title="CookieFormatVersion">CookieFormatVersion</a>: <i>Double</i>
<a href="#ignoreincompleterequestbodyerror" title="IgnoreIncompleteRequestBodyError">IgnoreIncompleteRequestBodyError</a>: <i>Boolean</i>
<a href="#maxexecutiontime" title="MaxExecutionTime">MaxExecutionTime</a>: <i>Double</i>
<a href="#regexmatchlimit" title="RegexMatchLimit">RegexMatchLimit</a>: <i>Double</i>
<a href="#regexrecursionlimit" title="RegexRecursionLimit">RegexRecursionLimit</a>: <i>Double</i>
<a href="#requestbodydefaultaction" title="RequestBodyDefaultAction">RequestBodyDefaultAction</a>: <i>String</i>
<a href="#requesthdrdefaultaction" title="RequestHdrDefaultAction">RequestHdrDefaultAction</a>: <i>String</i>
<a href="#responsebodydefaultaction" title="ResponseBodyDefaultAction">ResponseBodyDefaultAction</a>: <i>String</i>
<a href="#responsehdrdefaultaction" title="ResponseHdrDefaultAction">ResponseHdrDefaultAction</a>: <i>String</i>
<a href="#restrictedextensions" title="RestrictedExtensions">RestrictedExtensions</a>: <i>
      - String</i>
<a href="#restrictedheaders" title="RestrictedHeaders">RestrictedHeaders</a>: <i>
      - String</i>
<a href="#sendstatusheader" title="SendStatusHeader">SendStatusHeader</a>: <i>Boolean</i>
<a href="#serverresponsemaxbodysize" title="ServerResponseMaxBodySize">ServerResponseMaxBodySize</a>: <i>Double</i>
<a href="#staticextensions" title="StaticExtensions">StaticExtensions</a>: <i>
      - String</i>
<a href="#statuscodeforrejectedrequests" title="StatusCodeForRejectedRequests">StatusCodeForRejectedRequests</a>: <i>String</i>
<a href="#statusheadername" title="StatusHeaderName">StatusHeaderName</a>: <i>String</i>
<a href="#xmlxxeprotection" title="XmlXxeProtection">XmlXxeProtection</a>: <i>Boolean</i>
</pre>

## Properties

#### AllowedHttpVersions

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedMethods

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedRequestContentTypes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ArgumentSeparator

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientRequestMaxBodySize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CookieFormatVersion

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreIncompleteRequestBodyError

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxExecutionTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegexMatchLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegexRecursionLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestBodyDefaultAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestHdrDefaultAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseBodyDefaultAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseHdrDefaultAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestrictedExtensions

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestrictedHeaders

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendStatusHeader

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerResponseMaxBodySize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticExtensions

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatusCodeForRejectedRequests

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatusHeaderName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### XmlXxeProtection

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

