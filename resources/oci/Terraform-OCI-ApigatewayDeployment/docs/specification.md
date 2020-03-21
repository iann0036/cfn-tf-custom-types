# Terraform::OCI::ApigatewayDeployment Specification

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#loggingpolicies" title="LoggingPolicies">LoggingPolicies</a>" : <i>[ <a href="specification-loggingpolicies.md">LoggingPolicies</a>, ... ]</i>,
    "<a href="#requestpolicies" title="RequestPolicies">RequestPolicies</a>" : <i>[ <a href="specification-requestpolicies.md">RequestPolicies</a>, ... ]</i>,
    "<a href="#routes" title="Routes">Routes</a>" : <i>[ <a href="specification-routes.md">Routes</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#loggingpolicies" title="LoggingPolicies">LoggingPolicies</a>: <i>
      - <a href="specification-loggingpolicies.md">LoggingPolicies</a></i>
<a href="#requestpolicies" title="RequestPolicies">RequestPolicies</a>: <i>
      - <a href="specification-requestpolicies.md">RequestPolicies</a></i>
<a href="#routes" title="Routes">Routes</a>: <i>
      - <a href="specification-routes.md">Routes</a></i>
</pre>

## Properties

#### LoggingPolicies

_Required_: No

_Type_: List of <a href="specification-loggingpolicies.md">LoggingPolicies</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestPolicies

_Required_: No

_Type_: List of <a href="specification-requestpolicies.md">RequestPolicies</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Routes

_Required_: No

_Type_: List of <a href="specification-routes.md">Routes</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

