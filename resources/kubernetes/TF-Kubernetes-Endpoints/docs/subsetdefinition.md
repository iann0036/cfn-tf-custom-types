# TF::Kubernetes::Endpoints SubsetDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#address" title="Address">Address</a>" : <i>[ <a href="addressdefinition.md">AddressDefinition</a>, ... ]</i>,
    "<a href="#notreadyaddress" title="NotReadyAddress">NotReadyAddress</a>" : <i>[ <a href="notreadyaddressdefinition.md">NotReadyAddressDefinition</a>, ... ]</i>,
    "<a href="#port" title="Port">Port</a>" : <i>[ <a href="portdefinition.md">PortDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#address" title="Address">Address</a>: <i>
      - <a href="addressdefinition.md">AddressDefinition</a></i>
<a href="#notreadyaddress" title="NotReadyAddress">NotReadyAddress</a>: <i>
      - <a href="notreadyaddressdefinition.md">NotReadyAddressDefinition</a></i>
<a href="#port" title="Port">Port</a>: <i>
      - <a href="portdefinition.md">PortDefinition</a></i>
</pre>

## Properties

#### Address

_Required_: No

_Type_: List of <a href="addressdefinition.md">AddressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotReadyAddress

_Required_: No

_Type_: List of <a href="notreadyaddressdefinition.md">NotReadyAddressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: List of <a href="portdefinition.md">PortDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

