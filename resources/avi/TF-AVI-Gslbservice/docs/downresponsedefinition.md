# TF::AVI::Gslbservice DownResponseDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#fallbackip" title="FallbackIp">FallbackIp</a>" : <i>[ <a href="fallbackipdefinition.md">FallbackIpDefinition</a>, ... ]</i>,
    "<a href="#fallbackip6" title="FallbackIp6">FallbackIp6</a>" : <i>[ <a href="fallbackip6definition.md">FallbackIp6Definition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#fallbackip" title="FallbackIp">FallbackIp</a>: <i>
      - <a href="fallbackipdefinition.md">FallbackIpDefinition</a></i>
<a href="#fallbackip6" title="FallbackIp6">FallbackIp6</a>: <i>
      - <a href="fallbackip6definition.md">FallbackIp6Definition</a></i>
</pre>

## Properties

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FallbackIp

_Required_: No

_Type_: List of <a href="fallbackipdefinition.md">FallbackIpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FallbackIp6

_Required_: No

_Type_: List of <a href="fallbackip6definition.md">FallbackIp6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

