# TF::Google::ComputePacketMirroring MirroredResourcesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
    "<a href="#instances" title="Instances">Instances</a>" : <i>[ <a href="instancesdefinition.md">InstancesDefinition</a>, ... ]</i>,
    "<a href="#subnetworks" title="Subnetworks">Subnetworks</a>" : <i>[ <a href="subnetworksdefinition.md">SubnetworksDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
<a href="#instances" title="Instances">Instances</a>: <i>
      - <a href="instancesdefinition.md">InstancesDefinition</a></i>
<a href="#subnetworks" title="Subnetworks">Subnetworks</a>: <i>
      - <a href="subnetworksdefinition.md">SubnetworksDefinition</a></i>
</pre>

## Properties

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Instances

_Required_: No

_Type_: List of <a href="instancesdefinition.md">InstancesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnetworks

_Required_: No

_Type_: List of <a href="subnetworksdefinition.md">SubnetworksDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

