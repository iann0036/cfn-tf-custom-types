# TF::AVI::Image PatchDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#patchtype" title="PatchType">PatchType</a>" : <i>String</i>,
    "<a href="#reboot" title="Reboot">Reboot</a>" : <i>Boolean</i>,
    "<a href="#rebootlist" title="RebootList">RebootList</a>" : <i>[ <a href="rebootlistdefinition.md">RebootListDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#patchtype" title="PatchType">PatchType</a>: <i>String</i>
<a href="#reboot" title="Reboot">Reboot</a>: <i>Boolean</i>
<a href="#rebootlist" title="RebootList">RebootList</a>: <i>
      - <a href="rebootlistdefinition.md">RebootListDefinition</a></i>
</pre>

## Properties

#### PatchType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Reboot

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RebootList

_Required_: No

_Type_: List of <a href="rebootlistdefinition.md">RebootListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

