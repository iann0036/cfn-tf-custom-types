# TF::OCI::WaasWaasPolicy WhitelistsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#addresslists" title="AddressLists">AddressLists</a>" : <i>[ String, ... ]</i>,
    "<a href="#addresses" title="Addresses">Addresses</a>" : <i>[ String, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#addresslists" title="AddressLists">AddressLists</a>: <i>
      - String</i>
<a href="#addresses" title="Addresses">Addresses</a>: <i>
      - String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### AddressLists

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Addresses

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

