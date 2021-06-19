# TF::Google::CloudRunService ResourcesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#limits" title="Limits">Limits</a>" : <i>[ <a href="limitsdefinition.md">LimitsDefinition</a>, ... ]</i>,
    "<a href="#requests" title="Requests">Requests</a>" : <i>[ <a href="requestsdefinition.md">RequestsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#limits" title="Limits">Limits</a>: <i>
      - <a href="limitsdefinition.md">LimitsDefinition</a></i>
<a href="#requests" title="Requests">Requests</a>: <i>
      - <a href="requestsdefinition.md">RequestsDefinition</a></i>
</pre>

## Properties

#### Limits

_Required_: No

_Type_: List of <a href="limitsdefinition.md">LimitsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Requests

_Required_: No

_Type_: List of <a href="requestsdefinition.md">RequestsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

