# Terraform::AzureStack::VirtualNetwork Subnet

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#addressprefix" title="AddressPrefix">AddressPrefix</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#securitygroup" title="SecurityGroup">SecurityGroup</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#addressprefix" title="AddressPrefix">AddressPrefix</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#securitygroup" title="SecurityGroup">SecurityGroup</a>: <i>String</i>
</pre>

## Properties

#### AddressPrefix

The address prefix to use for the subnet.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the subnet.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroup

The Network Security Group to associate with
the subnet. (Referenced by `id`, ie. `azurestack_network_security_group.test.id`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

