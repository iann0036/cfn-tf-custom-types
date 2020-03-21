# Terraform::AzureRM::ApplicationGateway FrontendIpConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#privateipaddress" title="PrivateIpAddress">PrivateIpAddress</a>" : <i>String</i>,
    "<a href="#privateipaddressallocation" title="PrivateIpAddressAllocation">PrivateIpAddressAllocation</a>" : <i>String</i>,
    "<a href="#publicipaddressid" title="PublicIpAddressId">PublicIpAddressId</a>" : <i>String</i>,
    "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#privateipaddress" title="PrivateIpAddress">PrivateIpAddress</a>: <i>String</i>
<a href="#privateipaddressallocation" title="PrivateIpAddressAllocation">PrivateIpAddressAllocation</a>: <i>String</i>
<a href="#publicipaddressid" title="PublicIpAddressId">PublicIpAddressId</a>: <i>String</i>
<a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
</pre>

## Properties

#### Name

The name of the Frontend IP Configuration.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateIpAddress

The Private IP Address to use for the Application Gateway.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateIpAddressAllocation

The Allocation Method for the Private IP Address. Possible values are `Dynamic` and `Static`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIpAddressId

The ID of a Public IP Address which the Application Gateway should use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

The ID of the Subnet which the Application Gateway should be connected to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

