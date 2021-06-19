# TF::Volterra::FastAcl DestinationIpAddressDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#address" title="Address">Address</a>" : <i>[ <a href="addressdefinition.md">AddressDefinition</a>, ... ]</i>,
    "<a href="#ports" title="Ports">Ports</a>" : <i>[ <a href="portsdefinition.md">PortsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#address" title="Address">Address</a>: <i>
      - <a href="addressdefinition.md">AddressDefinition</a></i>
<a href="#ports" title="Ports">Ports</a>: <i>
      - <a href="portsdefinition.md">PortsDefinition</a></i>
</pre>

## Properties

#### Protocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Address

_Required_: No

_Type_: List of <a href="addressdefinition.md">AddressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ports

_Required_: No

_Type_: List of <a href="portsdefinition.md">PortsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

