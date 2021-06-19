# TF::OpsGenie::NotificationRule StepsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#sendafter" title="SendAfter">SendAfter</a>" : <i>Double</i>,
    "<a href="#contact" title="Contact">Contact</a>" : <i>[ <a href="contactdefinition.md">ContactDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#sendafter" title="SendAfter">SendAfter</a>: <i>Double</i>
<a href="#contact" title="Contact">Contact</a>: <i>
      - <a href="contactdefinition.md">ContactDefinition</a></i>
</pre>

## Properties

#### Enabled

Defined if this step is enabled. Default: `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendAfter

Time period, in minutes, notification will be sent after.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Contact

_Required_: No

_Type_: List of <a href="contactdefinition.md">ContactDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

