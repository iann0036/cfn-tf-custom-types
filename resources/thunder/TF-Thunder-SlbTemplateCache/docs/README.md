# TF::Thunder::SlbTemplateCache

`thunder_slb_template_cache` Provides details about thunder slb template cache

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SlbTemplateCache",
    "Properties" : {
        "<a href="#acceptreloadreq" title="AcceptReloadReq">AcceptReloadReq</a>" : <i>Double</i>,
        "<a href="#age" title="Age">Age</a>" : <i>Double</i>,
        "<a href="#defaultpolicynocache" title="DefaultPolicyNocache">DefaultPolicyNocache</a>" : <i>Double</i>,
        "<a href="#disableinsertage" title="DisableInsertAge">DisableInsertAge</a>" : <i>Double</i>,
        "<a href="#disableinsertvia" title="DisableInsertVia">DisableInsertVia</a>" : <i>Double</i>,
        "<a href="#logging" title="Logging">Logging</a>" : <i>String</i>,
        "<a href="#maxcachesize" title="MaxCacheSize">MaxCacheSize</a>" : <i>Double</i>,
        "<a href="#maxcontentsize" title="MaxContentSize">MaxContentSize</a>" : <i>Double</i>,
        "<a href="#mincontentsize" title="MinContentSize">MinContentSize</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#removecookies" title="RemoveCookies">RemoveCookies</a>" : <i>Double</i>,
        "<a href="#replacementpolicy" title="ReplacementPolicy">ReplacementPolicy</a>" : <i>String</i>,
        "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#verifyhost" title="VerifyHost">VerifyHost</a>" : <i>Double</i>,
        "<a href="#localuripolicy" title="LocalUriPolicy">LocalUriPolicy</a>" : <i>[ <a href="localuripolicydefinition.md">LocalUriPolicyDefinition</a>, ... ]</i>,
        "<a href="#samplingenable" title="SamplingEnable">SamplingEnable</a>" : <i>[ <a href="samplingenabledefinition.md">SamplingEnableDefinition</a>, ... ]</i>,
        "<a href="#uripolicy" title="UriPolicy">UriPolicy</a>" : <i>[ <a href="uripolicydefinition.md">UriPolicyDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SlbTemplateCache
Properties:
    <a href="#acceptreloadreq" title="AcceptReloadReq">AcceptReloadReq</a>: <i>Double</i>
    <a href="#age" title="Age">Age</a>: <i>Double</i>
    <a href="#defaultpolicynocache" title="DefaultPolicyNocache">DefaultPolicyNocache</a>: <i>Double</i>
    <a href="#disableinsertage" title="DisableInsertAge">DisableInsertAge</a>: <i>Double</i>
    <a href="#disableinsertvia" title="DisableInsertVia">DisableInsertVia</a>: <i>Double</i>
    <a href="#logging" title="Logging">Logging</a>: <i>String</i>
    <a href="#maxcachesize" title="MaxCacheSize">MaxCacheSize</a>: <i>Double</i>
    <a href="#maxcontentsize" title="MaxContentSize">MaxContentSize</a>: <i>Double</i>
    <a href="#mincontentsize" title="MinContentSize">MinContentSize</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#removecookies" title="RemoveCookies">RemoveCookies</a>: <i>Double</i>
    <a href="#replacementpolicy" title="ReplacementPolicy">ReplacementPolicy</a>: <i>String</i>
    <a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#verifyhost" title="VerifyHost">VerifyHost</a>: <i>Double</i>
    <a href="#localuripolicy" title="LocalUriPolicy">LocalUriPolicy</a>: <i>
      - <a href="localuripolicydefinition.md">LocalUriPolicyDefinition</a></i>
    <a href="#samplingenable" title="SamplingEnable">SamplingEnable</a>: <i>
      - <a href="samplingenabledefinition.md">SamplingEnableDefinition</a></i>
    <a href="#uripolicy" title="UriPolicy">UriPolicy</a>: <i>
      - <a href="uripolicydefinition.md">UriPolicyDefinition</a></i>
</pre>

## Properties

#### AcceptReloadReq

Accept reload requests via cache-control directives in HTTP headers.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Age

Specify duration in seconds cached content valid, default is 3600 seconds (seconds that the cached content is valid (default 3600 seconds)).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultPolicyNocache

Specify default policy to be to not cache.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableInsertAge

Disable insertion of age header in response served from RAM cache.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableInsertVia

Disable insertion of via header in response served from RAM cache.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logging

Specify logging template (Logging Config name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxCacheSize

Specify maximum cache size in megabytes, default is 80MB (RAM cache size in megabytes (default 80MB)).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxContentSize

Maximum size (bytes) of response that can be cached - default 81920 (80KB).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinContentSize

Minimum size (bytes) of response that can be cached - default 512.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specify cache template name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoveCookies

Remove cookies in response and cache.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplacementPolicy

‘LFU’: LFU;.

_Required_: No

_Type_: String

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

#### VerifyHost

Verify request using host before sending response from RAM cache.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalUriPolicy

_Required_: No

_Type_: List of <a href="localuripolicydefinition.md">LocalUriPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SamplingEnable

_Required_: No

_Type_: List of <a href="samplingenabledefinition.md">SamplingEnableDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UriPolicy

_Required_: No

_Type_: List of <a href="uripolicydefinition.md">UriPolicyDefinition</a>

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

