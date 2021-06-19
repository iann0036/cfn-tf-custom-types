# TF::CloudScale::Server InterfacesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#networkuuid" title="NetworkUuid">NetworkUuid</a>" : <i>String</i>,
    "<a href="#noaddress" title="NoAddress">NoAddress</a>" : <i>Boolean</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#addresses" title="Addresses">Addresses</a>" : <i>[ <a href="addressesdefinition.md">AddressesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#networkuuid" title="NetworkUuid">NetworkUuid</a>: <i>String</i>
<a href="#noaddress" title="NoAddress">NoAddress</a>: <i>Boolean</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#addresses" title="Addresses">Addresses</a>: <i>
      - <a href="addressesdefinition.md">AddressesDefinition</a></i>
</pre>

## Properties

#### NetworkUuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoAddress

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Addresses

_Required_: No

_Type_: List of <a href="addressesdefinition.md">AddressesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

