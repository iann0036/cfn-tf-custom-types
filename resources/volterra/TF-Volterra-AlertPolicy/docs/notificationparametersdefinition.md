# TF::Volterra::AlertPolicy NotificationParametersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#default" title="Default">Default</a>" : <i>Boolean</i>,
    "<a href="#groupinterval" title="GroupInterval">GroupInterval</a>" : <i>String</i>,
    "<a href="#groupwait" title="GroupWait">GroupWait</a>" : <i>String</i>,
    "<a href="#individual" title="Individual">Individual</a>" : <i>Boolean</i>,
    "<a href="#repeatinterval" title="RepeatInterval">RepeatInterval</a>" : <i>String</i>,
    "<a href="#vesiogroup" title="VesIoGroup">VesIoGroup</a>" : <i>Boolean</i>,
    "<a href="#custom" title="Custom">Custom</a>" : <i>[ <a href="customdefinition.md">CustomDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#default" title="Default">Default</a>: <i>Boolean</i>
<a href="#groupinterval" title="GroupInterval">GroupInterval</a>: <i>String</i>
<a href="#groupwait" title="GroupWait">GroupWait</a>: <i>String</i>
<a href="#individual" title="Individual">Individual</a>: <i>Boolean</i>
<a href="#repeatinterval" title="RepeatInterval">RepeatInterval</a>: <i>String</i>
<a href="#vesiogroup" title="VesIoGroup">VesIoGroup</a>: <i>Boolean</i>
<a href="#custom" title="Custom">Custom</a>: <i>
      - <a href="customdefinition.md">CustomDefinition</a></i>
</pre>

## Properties

#### Default

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupInterval

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupWait

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Individual

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RepeatInterval

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VesIoGroup

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Custom

_Required_: No

_Type_: List of <a href="customdefinition.md">CustomDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

