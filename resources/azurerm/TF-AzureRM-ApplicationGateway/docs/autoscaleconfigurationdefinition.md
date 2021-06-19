# TF::AzureRM::ApplicationGateway AutoscaleConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#maxcapacity" title="MaxCapacity">MaxCapacity</a>" : <i>Double</i>,
    "<a href="#mincapacity" title="MinCapacity">MinCapacity</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#maxcapacity" title="MaxCapacity">MaxCapacity</a>: <i>Double</i>
<a href="#mincapacity" title="MinCapacity">MinCapacity</a>: <i>Double</i>
</pre>

## Properties

#### MaxCapacity

Maximum capacity for autoscaling. Accepted values are in the range `2` to `125`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinCapacity

Minimum capacity for autoscaling. Accepted values are in the range `0` to `100`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

