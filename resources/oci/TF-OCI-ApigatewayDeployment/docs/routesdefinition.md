# TF::OCI::ApigatewayDeployment RoutesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#methods" title="Methods">Methods</a>" : <i>[ String, ... ]</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    "<a href="#backend" title="Backend">Backend</a>" : <i>[ <a href="backenddefinition.md">BackendDefinition</a>, ... ]</i>,
    "<a href="#loggingpolicies" title="LoggingPolicies">LoggingPolicies</a>" : <i>[ <a href="loggingpoliciesdefinition.md">LoggingPoliciesDefinition</a>, ... ]</i>,
    "<a href="#requestpolicies" title="RequestPolicies">RequestPolicies</a>" : <i>[ <a href="requestpoliciesdefinition.md">RequestPoliciesDefinition</a>, ... ]</i>,
    "<a href="#responsepolicies" title="ResponsePolicies">ResponsePolicies</a>" : <i>[ <a href="responsepoliciesdefinition.md">ResponsePoliciesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#methods" title="Methods">Methods</a>: <i>
      - String</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
<a href="#backend" title="Backend">Backend</a>: <i>
      - <a href="backenddefinition.md">BackendDefinition</a></i>
<a href="#loggingpolicies" title="LoggingPolicies">LoggingPolicies</a>: <i>
      - <a href="loggingpoliciesdefinition.md">LoggingPoliciesDefinition</a></i>
<a href="#requestpolicies" title="RequestPolicies">RequestPolicies</a>: <i>
      - <a href="requestpoliciesdefinition.md">RequestPoliciesDefinition</a></i>
<a href="#responsepolicies" title="ResponsePolicies">ResponsePolicies</a>: <i>
      - <a href="responsepoliciesdefinition.md">ResponsePoliciesDefinition</a></i>
</pre>

## Properties

#### Methods

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backend

_Required_: No

_Type_: List of <a href="backenddefinition.md">BackendDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingPolicies

_Required_: No

_Type_: List of <a href="loggingpoliciesdefinition.md">LoggingPoliciesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestPolicies

_Required_: No

_Type_: List of <a href="requestpoliciesdefinition.md">RequestPoliciesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponsePolicies

_Required_: No

_Type_: List of <a href="responsepoliciesdefinition.md">ResponsePoliciesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

