# Terraform::AzureRM::MonitorAutoscaleSetting Profile Rule ScaleAction

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cooldown" title="Cooldown">Cooldown</a>" : <i>String</i>,
    "<a href="#direction" title="Direction">Direction</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#value" title="Value">Value</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#cooldown" title="Cooldown">Cooldown</a>: <i>String</i>
<a href="#direction" title="Direction">Direction</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#value" title="Value">Value</a>: <i>Double</i>
</pre>

## Properties

#### Cooldown

The amount of time to wait since the last scaling action before this action occurs. Must be between 1 minute and 1 week and formatted as a ISO 8601 string.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Direction

The scale direction. Possible values are `Increase` and `Decrease`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of action that should occur. Possible values are `ChangeCount`, `ExactCount` and `PercentChangeCount`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

The number of instances involved in the scaling action. Defaults to `1`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

