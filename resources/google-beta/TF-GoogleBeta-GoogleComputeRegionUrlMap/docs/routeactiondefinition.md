# TF::GoogleBeta::GoogleComputeRegionUrlMap RouteActionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#corspolicy" title="CorsPolicy">CorsPolicy</a>" : <i>[ <a href="corspolicydefinition.md">CorsPolicyDefinition</a>, ... ]</i>,
    "<a href="#faultinjectionpolicy" title="FaultInjectionPolicy">FaultInjectionPolicy</a>" : <i>[ <a href="faultinjectionpolicydefinition.md">FaultInjectionPolicyDefinition</a>, ... ]</i>,
    "<a href="#requestmirrorpolicy" title="RequestMirrorPolicy">RequestMirrorPolicy</a>" : <i>[ <a href="requestmirrorpolicydefinition.md">RequestMirrorPolicyDefinition</a>, ... ]</i>,
    "<a href="#retrypolicy" title="RetryPolicy">RetryPolicy</a>" : <i>[ <a href="retrypolicydefinition.md">RetryPolicyDefinition</a>, ... ]</i>,
    "<a href="#timeout" title="Timeout">Timeout</a>" : <i>[ <a href="timeoutdefinition.md">TimeoutDefinition</a>, ... ]</i>,
    "<a href="#urlrewrite" title="UrlRewrite">UrlRewrite</a>" : <i>[ <a href="urlrewritedefinition.md">UrlRewriteDefinition</a>, ... ]</i>,
    "<a href="#weightedbackendservices" title="WeightedBackendServices">WeightedBackendServices</a>" : <i>[ <a href="weightedbackendservicesdefinition.md">WeightedBackendServicesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#corspolicy" title="CorsPolicy">CorsPolicy</a>: <i>
      - <a href="corspolicydefinition.md">CorsPolicyDefinition</a></i>
<a href="#faultinjectionpolicy" title="FaultInjectionPolicy">FaultInjectionPolicy</a>: <i>
      - <a href="faultinjectionpolicydefinition.md">FaultInjectionPolicyDefinition</a></i>
<a href="#requestmirrorpolicy" title="RequestMirrorPolicy">RequestMirrorPolicy</a>: <i>
      - <a href="requestmirrorpolicydefinition.md">RequestMirrorPolicyDefinition</a></i>
<a href="#retrypolicy" title="RetryPolicy">RetryPolicy</a>: <i>
      - <a href="retrypolicydefinition.md">RetryPolicyDefinition</a></i>
<a href="#timeout" title="Timeout">Timeout</a>: <i>
      - <a href="timeoutdefinition.md">TimeoutDefinition</a></i>
<a href="#urlrewrite" title="UrlRewrite">UrlRewrite</a>: <i>
      - <a href="urlrewritedefinition.md">UrlRewriteDefinition</a></i>
<a href="#weightedbackendservices" title="WeightedBackendServices">WeightedBackendServices</a>: <i>
      - <a href="weightedbackendservicesdefinition.md">WeightedBackendServicesDefinition</a></i>
</pre>

## Properties

#### CorsPolicy

_Required_: No

_Type_: List of <a href="corspolicydefinition.md">CorsPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FaultInjectionPolicy

_Required_: No

_Type_: List of <a href="faultinjectionpolicydefinition.md">FaultInjectionPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestMirrorPolicy

_Required_: No

_Type_: List of <a href="requestmirrorpolicydefinition.md">RequestMirrorPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryPolicy

_Required_: No

_Type_: List of <a href="retrypolicydefinition.md">RetryPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

_Required_: No

_Type_: List of <a href="timeoutdefinition.md">TimeoutDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlRewrite

_Required_: No

_Type_: List of <a href="urlrewritedefinition.md">UrlRewriteDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeightedBackendServices

_Required_: No

_Type_: List of <a href="weightedbackendservicesdefinition.md">WeightedBackendServicesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

