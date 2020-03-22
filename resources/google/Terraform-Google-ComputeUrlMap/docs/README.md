# Terraform::Google::ComputeUrlMap

UrlMaps are used to route requests to a backend service based on rules
that you define for the host and path of an incoming URL.


To get more information about UrlMap, see:

* [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/urlMaps)

<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=url_map_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div>

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::ComputeUrlMap",
    "Properties" : {
        "<a href="#defaultservice" title="DefaultService">DefaultService</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#headeraction" title="HeaderAction">HeaderAction</a>" : <i>[ <a href="headeraction.md">HeaderAction</a>, ... ]</i>,
        "<a href="#hostrule" title="HostRule">HostRule</a>" : <i>[ <a href="hostrule.md">HostRule</a>, ... ]</i>,
        "<a href="#pathmatcher" title="PathMatcher">PathMatcher</a>" : <i>[ <a href="pathmatcher.md">PathMatcher</a>, ... ]</i>,
        "<a href="#test" title="Test">Test</a>" : <i>[ <a href="test.md">Test</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#requestheaderstoadd" title="RequestHeadersToAdd">RequestHeadersToAdd</a>" : <i>[ <a href="requestheaderstoadd.md">RequestHeadersToAdd</a>, ... ]</i>,
        "<a href="#responseheaderstoadd" title="ResponseHeadersToAdd">ResponseHeadersToAdd</a>" : <i>[ <a href="responseheaderstoadd.md">ResponseHeadersToAdd</a>, ... ]</i>,
        "<a href="#pathrule" title="PathRule">PathRule</a>" : <i>[ <a href="pathrule.md">PathRule</a>, ... ]</i>,
        "<a href="#routerules" title="RouteRules">RouteRules</a>" : <i>[ <a href="routerules.md">RouteRules</a>, ... ]</i>,
        "<a href="#routeaction" title="RouteAction">RouteAction</a>" : <i>[ <a href="routeaction.md">RouteAction</a>, ... ]</i>,
        "<a href="#urlredirect" title="UrlRedirect">UrlRedirect</a>" : <i>[ <a href="urlredirect.md">UrlRedirect</a>, ... ]</i>,
        "<a href="#matchrules" title="MatchRules">MatchRules</a>" : <i>[ <a href="matchrules.md">MatchRules</a>, ... ]</i>,
        "<a href="#corspolicy" title="CorsPolicy">CorsPolicy</a>" : <i>[ <a href="corspolicy.md">CorsPolicy</a>, ... ]</i>,
        "<a href="#faultinjectionpolicy" title="FaultInjectionPolicy">FaultInjectionPolicy</a>" : <i>[ <a href="faultinjectionpolicy.md">FaultInjectionPolicy</a>, ... ]</i>,
        "<a href="#requestmirrorpolicy" title="RequestMirrorPolicy">RequestMirrorPolicy</a>" : <i>[ <a href="requestmirrorpolicy.md">RequestMirrorPolicy</a>, ... ]</i>,
        "<a href="#retrypolicy" title="RetryPolicy">RetryPolicy</a>" : <i>[ <a href="retrypolicy.md">RetryPolicy</a>, ... ]</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>[ <a href="timeout.md">Timeout</a>, ... ]</i>,
        "<a href="#urlrewrite" title="UrlRewrite">UrlRewrite</a>" : <i>[ <a href="urlrewrite.md">UrlRewrite</a>, ... ]</i>,
        "<a href="#weightedbackendservices" title="WeightedBackendServices">WeightedBackendServices</a>" : <i>[ <a href="weightedbackendservices.md">WeightedBackendServices</a>, ... ]</i>,
        "<a href="#headermatches" title="HeaderMatches">HeaderMatches</a>" : <i>[ <a href="headermatches.md">HeaderMatches</a>, ... ]</i>,
        "<a href="#metadatafilters" title="MetadataFilters">MetadataFilters</a>" : <i>[ <a href="metadatafilters.md">MetadataFilters</a>, ... ]</i>,
        "<a href="#queryparametermatches" title="QueryParameterMatches">QueryParameterMatches</a>" : <i>[ <a href="queryparametermatches.md">QueryParameterMatches</a>, ... ]</i>,
        "<a href="#abort" title="Abort">Abort</a>" : <i>[ <a href="abort.md">Abort</a>, ... ]</i>,
        "<a href="#delay" title="Delay">Delay</a>" : <i>[ <a href="delay.md">Delay</a>, ... ]</i>,
        "<a href="#pertrytimeout" title="PerTryTimeout">PerTryTimeout</a>" : <i>[ <a href="pertrytimeout.md">PerTryTimeout</a>, ... ]</i>,
        "<a href="#rangematch" title="RangeMatch">RangeMatch</a>" : <i>[ <a href="rangematch.md">RangeMatch</a>, ... ]</i>,
        "<a href="#filterlabels" title="FilterLabels">FilterLabels</a>" : <i>[ <a href="filterlabels.md">FilterLabels</a>, ... ]</i>,
        "<a href="#fixeddelay" title="FixedDelay">FixedDelay</a>" : <i>[ <a href="fixeddelay.md">FixedDelay</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::ComputeUrlMap
Properties:
    <a href="#defaultservice" title="DefaultService">DefaultService</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#headeraction" title="HeaderAction">HeaderAction</a>: <i>
      - <a href="headeraction.md">HeaderAction</a></i>
    <a href="#hostrule" title="HostRule">HostRule</a>: <i>
      - <a href="hostrule.md">HostRule</a></i>
    <a href="#pathmatcher" title="PathMatcher">PathMatcher</a>: <i>
      - <a href="pathmatcher.md">PathMatcher</a></i>
    <a href="#test" title="Test">Test</a>: <i>
      - <a href="test.md">Test</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#requestheaderstoadd" title="RequestHeadersToAdd">RequestHeadersToAdd</a>: <i>
      - <a href="requestheaderstoadd.md">RequestHeadersToAdd</a></i>
    <a href="#responseheaderstoadd" title="ResponseHeadersToAdd">ResponseHeadersToAdd</a>: <i>
      - <a href="responseheaderstoadd.md">ResponseHeadersToAdd</a></i>
    <a href="#pathrule" title="PathRule">PathRule</a>: <i>
      - <a href="pathrule.md">PathRule</a></i>
    <a href="#routerules" title="RouteRules">RouteRules</a>: <i>
      - <a href="routerules.md">RouteRules</a></i>
    <a href="#routeaction" title="RouteAction">RouteAction</a>: <i>
      - <a href="routeaction.md">RouteAction</a></i>
    <a href="#urlredirect" title="UrlRedirect">UrlRedirect</a>: <i>
      - <a href="urlredirect.md">UrlRedirect</a></i>
    <a href="#matchrules" title="MatchRules">MatchRules</a>: <i>
      - <a href="matchrules.md">MatchRules</a></i>
    <a href="#corspolicy" title="CorsPolicy">CorsPolicy</a>: <i>
      - <a href="corspolicy.md">CorsPolicy</a></i>
    <a href="#faultinjectionpolicy" title="FaultInjectionPolicy">FaultInjectionPolicy</a>: <i>
      - <a href="faultinjectionpolicy.md">FaultInjectionPolicy</a></i>
    <a href="#requestmirrorpolicy" title="RequestMirrorPolicy">RequestMirrorPolicy</a>: <i>
      - <a href="requestmirrorpolicy.md">RequestMirrorPolicy</a></i>
    <a href="#retrypolicy" title="RetryPolicy">RetryPolicy</a>: <i>
      - <a href="retrypolicy.md">RetryPolicy</a></i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>
      - <a href="timeout.md">Timeout</a></i>
    <a href="#urlrewrite" title="UrlRewrite">UrlRewrite</a>: <i>
      - <a href="urlrewrite.md">UrlRewrite</a></i>
    <a href="#weightedbackendservices" title="WeightedBackendServices">WeightedBackendServices</a>: <i>
      - <a href="weightedbackendservices.md">WeightedBackendServices</a></i>
    <a href="#headermatches" title="HeaderMatches">HeaderMatches</a>: <i>
      - <a href="headermatches.md">HeaderMatches</a></i>
    <a href="#metadatafilters" title="MetadataFilters">MetadataFilters</a>: <i>
      - <a href="metadatafilters.md">MetadataFilters</a></i>
    <a href="#queryparametermatches" title="QueryParameterMatches">QueryParameterMatches</a>: <i>
      - <a href="queryparametermatches.md">QueryParameterMatches</a></i>
    <a href="#abort" title="Abort">Abort</a>: <i>
      - <a href="abort.md">Abort</a></i>
    <a href="#delay" title="Delay">Delay</a>: <i>
      - <a href="delay.md">Delay</a></i>
    <a href="#pertrytimeout" title="PerTryTimeout">PerTryTimeout</a>: <i>
      - <a href="pertrytimeout.md">PerTryTimeout</a></i>
    <a href="#rangematch" title="RangeMatch">RangeMatch</a>: <i>
      - <a href="rangematch.md">RangeMatch</a></i>
    <a href="#filterlabels" title="FilterLabels">FilterLabels</a>: <i>
      - <a href="filterlabels.md">FilterLabels</a></i>
    <a href="#fixeddelay" title="FixedDelay">FixedDelay</a>: <i>
      - <a href="fixeddelay.md">FixedDelay</a></i>
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

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderAction

_Required_: No

_Type_: List of <a href="headeraction.md">HeaderAction</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostRule

_Required_: No

_Type_: List of <a href="hostrule.md">HostRule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathMatcher

_Required_: No

_Type_: List of <a href="pathmatcher.md">PathMatcher</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Test

_Required_: No

_Type_: List of <a href="test.md">Test</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestHeadersToAdd

_Required_: No

_Type_: List of <a href="requestheaderstoadd.md">RequestHeadersToAdd</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseHeadersToAdd

_Required_: No

_Type_: List of <a href="responseheaderstoadd.md">ResponseHeadersToAdd</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathRule

_Required_: No

_Type_: List of <a href="pathrule.md">PathRule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteRules

_Required_: No

_Type_: List of <a href="routerules.md">RouteRules</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteAction

_Required_: No

_Type_: List of <a href="routeaction.md">RouteAction</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlRedirect

_Required_: No

_Type_: List of <a href="urlredirect.md">UrlRedirect</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchRules

_Required_: No

_Type_: List of <a href="matchrules.md">MatchRules</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CorsPolicy

_Required_: No

_Type_: List of <a href="corspolicy.md">CorsPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FaultInjectionPolicy

_Required_: No

_Type_: List of <a href="faultinjectionpolicy.md">FaultInjectionPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestMirrorPolicy

_Required_: No

_Type_: List of <a href="requestmirrorpolicy.md">RequestMirrorPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryPolicy

_Required_: No

_Type_: List of <a href="retrypolicy.md">RetryPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

_Required_: No

_Type_: List of <a href="timeout.md">Timeout</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlRewrite

_Required_: No

_Type_: List of <a href="urlrewrite.md">UrlRewrite</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeightedBackendServices

_Required_: No

_Type_: List of <a href="weightedbackendservices.md">WeightedBackendServices</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderMatches

_Required_: No

_Type_: List of <a href="headermatches.md">HeaderMatches</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetadataFilters

_Required_: No

_Type_: List of <a href="metadatafilters.md">MetadataFilters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryParameterMatches

_Required_: No

_Type_: List of <a href="queryparametermatches.md">QueryParameterMatches</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Abort

_Required_: No

_Type_: List of <a href="abort.md">Abort</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Delay

_Required_: No

_Type_: List of <a href="delay.md">Delay</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PerTryTimeout

_Required_: No

_Type_: List of <a href="pertrytimeout.md">PerTryTimeout</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RangeMatch

_Required_: No

_Type_: List of <a href="rangematch.md">RangeMatch</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterLabels

_Required_: No

_Type_: List of <a href="filterlabels.md">FilterLabels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FixedDelay

_Required_: No

_Type_: List of <a href="fixeddelay.md">FixedDelay</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreationTimestamp

Returns the <code>CreationTimestamp</code> value.

#### Fingerprint

Returns the <code>Fingerprint</code> value.

#### Id

Returns the <code>Id</code> value.

#### MapId

Returns the <code>MapId</code> value.

#### SelfLink

Returns the <code>SelfLink</code> value.

