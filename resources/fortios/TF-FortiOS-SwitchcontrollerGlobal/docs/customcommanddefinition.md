# TF::FortiOS::SwitchcontrollerGlobal CustomCommandDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#commandentry" title="CommandEntry">CommandEntry</a>" : <i>String</i>,
    "<a href="#commandname" title="CommandName">CommandName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#commandentry" title="CommandEntry">CommandEntry</a>: <i>String</i>
<a href="#commandname" title="CommandName">CommandName</a>: <i>String</i>
</pre>

## Properties

#### CommandEntry

List of FortiSwitch commands.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommandName

Name of custom command to push to all FortiSwitches in VDOM.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

