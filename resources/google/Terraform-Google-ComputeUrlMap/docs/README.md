# Terraform::Google::ComputeUrlMap

CloudFormation equivalent of google_compute_url_map

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::ComputeUrlMap",
    "Properties" : {
        "<a href="#defaultservice" title="DefaultService">DefaultService</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#headeraction" title="HeaderAction">HeaderAction</a>" : <i>[ &lt;a href=&#34;headeraction.md&#34;&gt;HeaderAction&lt;/a&gt;, ... ]</i>,
        "<a href="#hostrule" title="HostRule">HostRule</a>" : <i>[ &lt;a href=&#34;hostrule.md&#34;&gt;HostRule&lt;/a&gt;, ... ]</i>,
        "<a href="#pathmatcher" title="PathMatcher">PathMatcher</a>" : <i>[ &lt;a href=&#34;pathmatcher.md&#34;&gt;PathMatcher&lt;/a&gt;, ... ]</i>,
        "<a href="#test" title="Test">Test</a>" : <i>[ &lt;a href=&#34;test.md&#34;&gt;Test&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#requestheaderstoadd" title="RequestHeadersToAdd">RequestHeadersToAdd</a>" : <i>[ &lt;a href=&#34;requestheaderstoadd.md&#34;&gt;RequestHeadersToAdd&lt;/a&gt;, ... ]</i>,
        "<a href="#responseheaderstoadd" title="ResponseHeadersToAdd">ResponseHeadersToAdd</a>" : <i>[ &lt;a href=&#34;responseheaderstoadd.md&#34;&gt;ResponseHeadersToAdd&lt;/a&gt;, ... ]</i>,
        "<a href="#pathrule" title="PathRule">PathRule</a>" : <i>[ &lt;a href=&#34;pathrule.md&#34;&gt;PathRule&lt;/a&gt;, ... ]</i>,
        "<a href="#routerules" title="RouteRules">RouteRules</a>" : <i>[ &lt;a href=&#34;routerules.md&#34;&gt;RouteRules&lt;/a&gt;, ... ]</i>,
        "<a href="#routeaction" title="RouteAction">RouteAction</a>" : <i>[ &lt;a href=&#34;routeaction.md&#34;&gt;RouteAction&lt;/a&gt;, ... ]</i>,
        "<a href="#urlredirect" title="UrlRedirect">UrlRedirect</a>" : <i>[ &lt;a href=&#34;urlredirect.md&#34;&gt;UrlRedirect&lt;/a&gt;, ... ]</i>,
        "<a href="#matchrules" title="MatchRules">MatchRules</a>" : <i>[ &lt;a href=&#34;matchrules.md&#34;&gt;MatchRules&lt;/a&gt;, ... ]</i>,
        "<a href="#corspolicy" title="CorsPolicy">CorsPolicy</a>" : <i>[ &lt;a href=&#34;corspolicy.md&#34;&gt;CorsPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#faultinjectionpolicy" title="FaultInjectionPolicy">FaultInjectionPolicy</a>" : <i>[ &lt;a href=&#34;faultinjectionpolicy.md&#34;&gt;FaultInjectionPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#requestmirrorpolicy" title="RequestMirrorPolicy">RequestMirrorPolicy</a>" : <i>[ &lt;a href=&#34;requestmirrorpolicy.md&#34;&gt;RequestMirrorPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#retrypolicy" title="RetryPolicy">RetryPolicy</a>" : <i>[ &lt;a href=&#34;retrypolicy.md&#34;&gt;RetryPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>[ &lt;a href=&#34;timeout.md&#34;&gt;Timeout&lt;/a&gt;, ... ]</i>,
        "<a href="#urlrewrite" title="UrlRewrite">UrlRewrite</a>" : <i>[ &lt;a href=&#34;urlrewrite.md&#34;&gt;UrlRewrite&lt;/a&gt;, ... ]</i>,
        "<a href="#weightedbackendservices" title="WeightedBackendServices">WeightedBackendServices</a>" : <i>[ &lt;a href=&#34;weightedbackendservices.md&#34;&gt;WeightedBackendServices&lt;/a&gt;, ... ]</i>,
        "<a href="#headermatches" title="HeaderMatches">HeaderMatches</a>" : <i>[ &lt;a href=&#34;headermatches.md&#34;&gt;HeaderMatches&lt;/a&gt;, ... ]</i>,
        "<a href="#metadatafilters" title="MetadataFilters">MetadataFilters</a>" : <i>[ &lt;a href=&#34;metadatafilters.md&#34;&gt;MetadataFilters&lt;/a&gt;, ... ]</i>,
        "<a href="#queryparametermatches" title="QueryParameterMatches">QueryParameterMatches</a>" : <i>[ &lt;a href=&#34;queryparametermatches.md&#34;&gt;QueryParameterMatches&lt;/a&gt;, ... ]</i>,
        "<a href="#abort" title="Abort">Abort</a>" : <i>[ &lt;a href=&#34;abort.md&#34;&gt;Abort&lt;/a&gt;, ... ]</i>,
        "<a href="#delay" title="Delay">Delay</a>" : <i>[ &lt;a href=&#34;delay.md&#34;&gt;Delay&lt;/a&gt;, ... ]</i>,
        "<a href="#pertrytimeout" title="PerTryTimeout">PerTryTimeout</a>" : <i>[ &lt;a href=&#34;pertrytimeout.md&#34;&gt;PerTryTimeout&lt;/a&gt;, ... ]</i>,
        "<a href="#rangematch" title="RangeMatch">RangeMatch</a>" : <i>[ &lt;a href=&#34;rangematch.md&#34;&gt;RangeMatch&lt;/a&gt;, ... ]</i>,
        "<a href="#filterlabels" title="FilterLabels">FilterLabels</a>" : <i>[ &lt;a href=&#34;filterlabels.md&#34;&gt;FilterLabels&lt;/a&gt;, ... ]</i>,
        "<a href="#fixeddelay" title="FixedDelay">FixedDelay</a>" : <i>[ &lt;a href=&#34;fixeddelay.md&#34;&gt;FixedDelay&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::ComputeUrlMap
Properties:
    <a href="#defaultservice" title="DefaultService">DefaultService</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#headeraction" title="HeaderAction">HeaderAction</a>: <i>
      - &lt;a href=&#34;headeraction.md&#34;&gt;HeaderAction&lt;/a&gt;</i>
    <a href="#hostrule" title="HostRule">HostRule</a>: <i>
      - &lt;a href=&#34;hostrule.md&#34;&gt;HostRule&lt;/a&gt;</i>
    <a href="#pathmatcher" title="PathMatcher">PathMatcher</a>: <i>
      - &lt;a href=&#34;pathmatcher.md&#34;&gt;PathMatcher&lt;/a&gt;</i>
    <a href="#test" title="Test">Test</a>: <i>
      - &lt;a href=&#34;test.md&#34;&gt;Test&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#requestheaderstoadd" title="RequestHeadersToAdd">RequestHeadersToAdd</a>: <i>
      - &lt;a href=&#34;requestheaderstoadd.md&#34;&gt;RequestHeadersToAdd&lt;/a&gt;</i>
    <a href="#responseheaderstoadd" title="ResponseHeadersToAdd">ResponseHeadersToAdd</a>: <i>
      - &lt;a href=&#34;responseheaderstoadd.md&#34;&gt;ResponseHeadersToAdd&lt;/a&gt;</i>
    <a href="#pathrule" title="PathRule">PathRule</a>: <i>
      - &lt;a href=&#34;pathrule.md&#34;&gt;PathRule&lt;/a&gt;</i>
    <a href="#routerules" title="RouteRules">RouteRules</a>: <i>
      - &lt;a href=&#34;routerules.md&#34;&gt;RouteRules&lt;/a&gt;</i>
    <a href="#routeaction" title="RouteAction">RouteAction</a>: <i>
      - &lt;a href=&#34;routeaction.md&#34;&gt;RouteAction&lt;/a&gt;</i>
    <a href="#urlredirect" title="UrlRedirect">UrlRedirect</a>: <i>
      - &lt;a href=&#34;urlredirect.md&#34;&gt;UrlRedirect&lt;/a&gt;</i>
    <a href="#matchrules" title="MatchRules">MatchRules</a>: <i>
      - &lt;a href=&#34;matchrules.md&#34;&gt;MatchRules&lt;/a&gt;</i>
    <a href="#corspolicy" title="CorsPolicy">CorsPolicy</a>: <i>
      - &lt;a href=&#34;corspolicy.md&#34;&gt;CorsPolicy&lt;/a&gt;</i>
    <a href="#faultinjectionpolicy" title="FaultInjectionPolicy">FaultInjectionPolicy</a>: <i>
      - &lt;a href=&#34;faultinjectionpolicy.md&#34;&gt;FaultInjectionPolicy&lt;/a&gt;</i>
    <a href="#requestmirrorpolicy" title="RequestMirrorPolicy">RequestMirrorPolicy</a>: <i>
      - &lt;a href=&#34;requestmirrorpolicy.md&#34;&gt;RequestMirrorPolicy&lt;/a&gt;</i>
    <a href="#retrypolicy" title="RetryPolicy">RetryPolicy</a>: <i>
      - &lt;a href=&#34;retrypolicy.md&#34;&gt;RetryPolicy&lt;/a&gt;</i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>
      - &lt;a href=&#34;timeout.md&#34;&gt;Timeout&lt;/a&gt;</i>
    <a href="#urlrewrite" title="UrlRewrite">UrlRewrite</a>: <i>
      - &lt;a href=&#34;urlrewrite.md&#34;&gt;UrlRewrite&lt;/a&gt;</i>
    <a href="#weightedbackendservices" title="WeightedBackendServices">WeightedBackendServices</a>: <i>
      - &lt;a href=&#34;weightedbackendservices.md&#34;&gt;WeightedBackendServices&lt;/a&gt;</i>
    <a href="#headermatches" title="HeaderMatches">HeaderMatches</a>: <i>
      - &lt;a href=&#34;headermatches.md&#34;&gt;HeaderMatches&lt;/a&gt;</i>
    <a href="#metadatafilters" title="MetadataFilters">MetadataFilters</a>: <i>
      - &lt;a href=&#34;metadatafilters.md&#34;&gt;MetadataFilters&lt;/a&gt;</i>
    <a href="#queryparametermatches" title="QueryParameterMatches">QueryParameterMatches</a>: <i>
      - &lt;a href=&#34;queryparametermatches.md&#34;&gt;QueryParameterMatches&lt;/a&gt;</i>
    <a href="#abort" title="Abort">Abort</a>: <i>
      - &lt;a href=&#34;abort.md&#34;&gt;Abort&lt;/a&gt;</i>
    <a href="#delay" title="Delay">Delay</a>: <i>
      - &lt;a href=&#34;delay.md&#34;&gt;Delay&lt;/a&gt;</i>
    <a href="#pertrytimeout" title="PerTryTimeout">PerTryTimeout</a>: <i>
      - &lt;a href=&#34;pertrytimeout.md&#34;&gt;PerTryTimeout&lt;/a&gt;</i>
    <a href="#rangematch" title="RangeMatch">RangeMatch</a>: <i>
      - &lt;a href=&#34;rangematch.md&#34;&gt;RangeMatch&lt;/a&gt;</i>
    <a href="#filterlabels" title="FilterLabels">FilterLabels</a>: <i>
      - &lt;a href=&#34;filterlabels.md&#34;&gt;FilterLabels&lt;/a&gt;</i>
    <a href="#fixeddelay" title="FixedDelay">FixedDelay</a>: <i>
      - &lt;a href=&#34;fixeddelay.md&#34;&gt;FixedDelay&lt;/a&gt;</i>
</pre>

## Properties

#### DefaultService

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderAction

_Required_: No

_Type_: List of &lt;a href=&#34;headeraction.md&#34;&gt;HeaderAction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostRule

_Required_: No

_Type_: List of &lt;a href=&#34;hostrule.md&#34;&gt;HostRule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathMatcher

_Required_: No

_Type_: List of &lt;a href=&#34;pathmatcher.md&#34;&gt;PathMatcher&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Test

_Required_: No

_Type_: List of &lt;a href=&#34;test.md&#34;&gt;Test&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestHeadersToAdd

_Required_: No

_Type_: List of &lt;a href=&#34;requestheaderstoadd.md&#34;&gt;RequestHeadersToAdd&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseHeadersToAdd

_Required_: No

_Type_: List of &lt;a href=&#34;responseheaderstoadd.md&#34;&gt;ResponseHeadersToAdd&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathRule

_Required_: No

_Type_: List of &lt;a href=&#34;pathrule.md&#34;&gt;PathRule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteRules

_Required_: No

_Type_: List of &lt;a href=&#34;routerules.md&#34;&gt;RouteRules&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteAction

_Required_: No

_Type_: List of &lt;a href=&#34;routeaction.md&#34;&gt;RouteAction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlRedirect

_Required_: No

_Type_: List of &lt;a href=&#34;urlredirect.md&#34;&gt;UrlRedirect&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchRules

_Required_: No

_Type_: List of &lt;a href=&#34;matchrules.md&#34;&gt;MatchRules&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CorsPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;corspolicy.md&#34;&gt;CorsPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FaultInjectionPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;faultinjectionpolicy.md&#34;&gt;FaultInjectionPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestMirrorPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;requestmirrorpolicy.md&#34;&gt;RequestMirrorPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;retrypolicy.md&#34;&gt;RetryPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

_Required_: No

_Type_: List of &lt;a href=&#34;timeout.md&#34;&gt;Timeout&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlRewrite

_Required_: No

_Type_: List of &lt;a href=&#34;urlrewrite.md&#34;&gt;UrlRewrite&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeightedBackendServices

_Required_: No

_Type_: List of &lt;a href=&#34;weightedbackendservices.md&#34;&gt;WeightedBackendServices&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderMatches

_Required_: No

_Type_: List of &lt;a href=&#34;headermatches.md&#34;&gt;HeaderMatches&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetadataFilters

_Required_: No

_Type_: List of &lt;a href=&#34;metadatafilters.md&#34;&gt;MetadataFilters&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryParameterMatches

_Required_: No

_Type_: List of &lt;a href=&#34;queryparametermatches.md&#34;&gt;QueryParameterMatches&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Abort

_Required_: No

_Type_: List of &lt;a href=&#34;abort.md&#34;&gt;Abort&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Delay

_Required_: No

_Type_: List of &lt;a href=&#34;delay.md&#34;&gt;Delay&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PerTryTimeout

_Required_: No

_Type_: List of &lt;a href=&#34;pertrytimeout.md&#34;&gt;PerTryTimeout&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RangeMatch

_Required_: No

_Type_: List of &lt;a href=&#34;rangematch.md&#34;&gt;RangeMatch&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterLabels

_Required_: No

_Type_: List of &lt;a href=&#34;filterlabels.md&#34;&gt;FilterLabels&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FixedDelay

_Required_: No

_Type_: List of &lt;a href=&#34;fixeddelay.md&#34;&gt;FixedDelay&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreationTimestamp

Returns the &lt;code&gt;CreationTimestamp&lt;/code&gt; value.

#### Fingerprint

Returns the &lt;code&gt;Fingerprint&lt;/code&gt; value.

#### MapId

Returns the &lt;code&gt;MapId&lt;/code&gt; value.

#### SelfLink

Returns the &lt;code&gt;SelfLink&lt;/code&gt; value.

