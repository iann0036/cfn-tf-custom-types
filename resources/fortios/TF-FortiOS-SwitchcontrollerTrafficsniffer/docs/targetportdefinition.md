# TF::FortiOS::SwitchcontrollerTrafficsniffer TargetPortDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#switchid" title="SwitchId">SwitchId</a>" : <i>String</i>,
    "<a href="#inports" title="InPorts">InPorts</a>" : <i>[ <a href="inportsdefinition.md">InPortsDefinition</a>, ... ]</i>,
    "<a href="#outports" title="OutPorts">OutPorts</a>" : <i>[ <a href="outportsdefinition.md">OutPortsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#switchid" title="SwitchId">SwitchId</a>: <i>String</i>
<a href="#inports" title="InPorts">InPorts</a>: <i>
      - <a href="inportsdefinition.md">InPortsDefinition</a></i>
<a href="#outports" title="OutPorts">OutPorts</a>: <i>
      - <a href="outportsdefinition.md">OutPortsDefinition</a></i>
</pre>

## Properties

#### Description

Description for the sniffer port entry.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchId

Managed-switch ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InPorts

_Required_: No

_Type_: List of <a href="inportsdefinition.md">InPortsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutPorts

_Required_: No

_Type_: List of <a href="outportsdefinition.md">OutPortsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

