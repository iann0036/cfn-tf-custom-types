# TF::AzureRM::NetworkInterface IpConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#primary" title="Primary">Primary</a>" : <i>Boolean</i>,
    "<a href="#privateipaddress" title="PrivateIpAddress">PrivateIpAddress</a>" : <i>String</i>,
    "<a href="#privateipaddressallocation" title="PrivateIpAddressAllocation">PrivateIpAddressAllocation</a>" : <i>String</i>,
    "<a href="#privateipaddressversion" title="PrivateIpAddressVersion">PrivateIpAddressVersion</a>" : <i>String</i>,
    "<a href="#publicipaddressid" title="PublicIpAddressId">PublicIpAddressId</a>" : <i>String</i>,
    "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#primary" title="Primary">Primary</a>: <i>Boolean</i>
<a href="#privateipaddress" title="PrivateIpAddress">PrivateIpAddress</a>: <i>String</i>
<a href="#privateipaddressallocation" title="PrivateIpAddressAllocation">PrivateIpAddressAllocation</a>: <i>String</i>
<a href="#privateipaddressversion" title="PrivateIpAddressVersion">PrivateIpAddressVersion</a>: <i>String</i>
<a href="#publicipaddressid" title="PublicIpAddressId">PublicIpAddressId</a>: <i>String</i>
<a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
</pre>

## Properties

#### Name

A name used for this IP Configuration.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Primary

Is this the Primary IP Configuration? Must be `true` for the first `ip_configuration` when multiple are specified. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateIpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateIpAddressAllocation

The allocation method used for the Private IP Address. Possible values are `Dynamic` and `Static`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateIpAddressVersion

The IP Version to use. Possible values are `IPv4` or `IPv6`. Defaults to `IPv4`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIpAddressId

Reference to a Public IP Address to associate with this NIC.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

The ID of the Subnet where this Network Interface should be located in.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

