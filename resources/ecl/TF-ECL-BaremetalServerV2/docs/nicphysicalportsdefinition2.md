# TF::ECL::BaremetalServerV2 NicPhysicalPortsDefinition2

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#fixedips" title="FixedIps">FixedIps</a>" : <i>[ <a href="nicphysicalportsdefinition.md">NicPhysicalPortsDefinition</a>, ... ]</i>,
    "<a href="#networkid" title="NetworkId">NetworkId</a>" : <i>String</i>,
    "<a href="#portid" title="PortId">PortId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#fixedips" title="FixedIps">FixedIps</a>: <i>
      - <a href="nicphysicalportsdefinition.md">NicPhysicalPortsDefinition</a></i>
<a href="#networkid" title="NetworkId">NetworkId</a>: <i>String</i>
<a href="#portid" title="PortId">PortId</a>: <i>String</i>
</pre>

## Properties

#### FixedIps

_Required_: No

_Type_: List of <a href="nicphysicalportsdefinition.md">NicPhysicalPortsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

