# TF::AVI::Upgradestatusinfo StateDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#reason" title="Reason">Reason</a>" : <i>String</i>,
    "<a href="#rebooted" title="Rebooted">Rebooted</a>" : <i>Boolean</i>,
    "<a href="#state" title="State">State</a>" : <i>[ <a href="statedefinition.md">StateDefinition</a>, ... ]</i>,
    "<a href="#lastchangedtime" title="LastChangedTime">LastChangedTime</a>" : <i>[ <a href="lastchangedtimedefinition.md">LastChangedTimeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#reason" title="Reason">Reason</a>: <i>String</i>
<a href="#rebooted" title="Rebooted">Rebooted</a>: <i>Boolean</i>
<a href="#state" title="State">State</a>: <i>
      - <a href="statedefinition.md">StateDefinition</a></i>
<a href="#lastchangedtime" title="LastChangedTime">LastChangedTime</a>: <i>
      - <a href="lastchangedtimedefinition.md">LastChangedTimeDefinition</a></i>
</pre>

## Properties

#### Reason

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rebooted

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

_Required_: No

_Type_: List of <a href="statedefinition.md">StateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LastChangedTime

_Required_: No

_Type_: List of <a href="lastchangedtimedefinition.md">LastChangedTimeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

