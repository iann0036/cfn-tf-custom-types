# Terraform::AzureStack::Lb FrontendIpConfiguration

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

Specifies the name of the frontend ip configuration.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateIpAddress

Private IP Address to assign to the Load Balancer. The last one and first four IPs in any range are reserved and cannot be manually assigned.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateIpAddressAllocation

Defines how a private IP address is assigned. Options are Static or Dynamic.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIpAddressId

Reference to Public IP address to be associated with the Load Balancer.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

Reference to subnet associated with the IP Configuration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

