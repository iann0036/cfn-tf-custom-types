# Terraform::Google::ComputeUrlMap RouteAction

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#corspolicy" title="CorsPolicy">CorsPolicy</a>" : <i>[ <a href="routeaction-corspolicy.md">CorsPolicy</a>, ... ]</i>,
    "<a href="#faultinjectionpolicy" title="FaultInjectionPolicy">FaultInjectionPolicy</a>" : <i>[ <a href="routeaction-faultinjectionpolicy.md">FaultInjectionPolicy</a>, ... ]</i>,
    "<a href="#requestmirrorpolicy" title="RequestMirrorPolicy">RequestMirrorPolicy</a>" : <i>[ <a href="routeaction-requestmirrorpolicy.md">RequestMirrorPolicy</a>, ... ]</i>,
    "<a href="#retrypolicy" title="RetryPolicy">RetryPolicy</a>" : <i>[ <a href="routeaction-retrypolicy.md">RetryPolicy</a>, ... ]</i>,
    "<a href="#timeout" title="Timeout">Timeout</a>" : <i>[ <a href="routeaction-timeout.md">Timeout</a>, ... ]</i>,
    "<a href="#urlrewrite" title="UrlRewrite">UrlRewrite</a>" : <i>[ <a href="routeaction-urlrewrite.md">UrlRewrite</a>, ... ]</i>,
    "<a href="#weightedbackendservices" title="WeightedBackendServices">WeightedBackendServices</a>" : <i>[ <a href="routeaction-weightedbackendservices.md">WeightedBackendServices</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#corspolicy" title="CorsPolicy">CorsPolicy</a>: <i>
      - <a href="routeaction-corspolicy.md">CorsPolicy</a></i>
<a href="#faultinjectionpolicy" title="FaultInjectionPolicy">FaultInjectionPolicy</a>: <i>
      - <a href="routeaction-faultinjectionpolicy.md">FaultInjectionPolicy</a></i>
<a href="#requestmirrorpolicy" title="RequestMirrorPolicy">RequestMirrorPolicy</a>: <i>
      - <a href="routeaction-requestmirrorpolicy.md">RequestMirrorPolicy</a></i>
<a href="#retrypolicy" title="RetryPolicy">RetryPolicy</a>: <i>
      - <a href="routeaction-retrypolicy.md">RetryPolicy</a></i>
<a href="#timeout" title="Timeout">Timeout</a>: <i>
      - <a href="routeaction-timeout.md">Timeout</a></i>
<a href="#urlrewrite" title="UrlRewrite">UrlRewrite</a>: <i>
      - <a href="routeaction-urlrewrite.md">UrlRewrite</a></i>
<a href="#weightedbackendservices" title="WeightedBackendServices">WeightedBackendServices</a>: <i>
      - <a href="routeaction-weightedbackendservices.md">WeightedBackendServices</a></i>
</pre>

## Properties

#### CorsPolicy

_Required_: No

_Type_: List of <a href="routeaction-corspolicy.md">CorsPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FaultInjectionPolicy

_Required_: No

_Type_: List of <a href="routeaction-faultinjectionpolicy.md">FaultInjectionPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestMirrorPolicy

_Required_: No

_Type_: List of <a href="routeaction-requestmirrorpolicy.md">RequestMirrorPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryPolicy

_Required_: No

_Type_: List of <a href="routeaction-retrypolicy.md">RetryPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

_Required_: No

_Type_: List of <a href="routeaction-timeout.md">Timeout</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlRewrite

_Required_: No

_Type_: List of <a href="routeaction-urlrewrite.md">UrlRewrite</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeightedBackendServices

_Required_: No

_Type_: List of <a href="routeaction-weightedbackendservices.md">WeightedBackendServices</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

