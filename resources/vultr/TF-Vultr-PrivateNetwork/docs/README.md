# TF::Vultr::PrivateNetwork

Provides a Vultr private network resource. This can be used to create, read, and delete private networks on your Vultr account.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Vultr::PrivateNetwork",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#v4subnet" title="V4Subnet">V4Subnet</a>" : <i>String</i>,
        "<a href="#v4subnetmask" title="V4SubnetMask">V4SubnetMask</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Vultr::PrivateNetwork
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#v4subnet" title="V4Subnet">V4Subnet</a>: <i>String</i>
    <a href="#v4subnetmask" title="V4SubnetMask">V4SubnetMask</a>: <i>Double</i>
</pre>

## Properties

#### Description

The description you want to give your network.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region ID that you want the network to be created in.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### V4Subnet

The IPv4 subnet to be used when attaching instances to this network.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### V4SubnetMask

The number of bits for the netmask in CIDR notation. Example: 32.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### DateCreated

Returns the <code>DateCreated</code> value.

#### Id

Returns the <code>Id</code> value.

