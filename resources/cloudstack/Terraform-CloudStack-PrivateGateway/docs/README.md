# Terraform::CloudStack::PrivateGateway

Creates a private gateway for the given VPC.

*NOTE: private gateway can only be created using a ROOT account!*

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::CloudStack::PrivateGateway",
    "Properties" : {
        "<a href="#aclid" title="AclId">AclId</a>" : <i>String</i>,
        "<a href="#gateway" title="Gateway">Gateway</a>" : <i>String</i>,
        "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>String</i>,
        "<a href="#netmask" title="Netmask">Netmask</a>" : <i>String</i>,
        "<a href="#networkoffering" title="NetworkOffering">NetworkOffering</a>" : <i>String</i>,
        "<a href="#physicalnetworkid" title="PhysicalNetworkId">PhysicalNetworkId</a>" : <i>String</i>,
        "<a href="#vlan" title="Vlan">Vlan</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::CloudStack::PrivateGateway
Properties:
    <a href="#aclid" title="AclId">AclId</a>: <i>String</i>
    <a href="#gateway" title="Gateway">Gateway</a>: <i>String</i>
    <a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>String</i>
    <a href="#netmask" title="Netmask">Netmask</a>: <i>String</i>
    <a href="#networkoffering" title="NetworkOffering">NetworkOffering</a>: <i>String</i>
    <a href="#physicalnetworkid" title="PhysicalNetworkId">PhysicalNetworkId</a>: <i>String</i>
    <a href="#vlan" title="Vlan">Vlan</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
</pre>

## Properties

#### AclId

The ACL ID that should be attached to the network.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gateway

the gateway of the Private gateway. Changing this
forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

the IP address of the Private gateway. Changing this forces
a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Netmask

The netmask of the Private gateway. Changing
this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkOffering

The name or ID of the network offering to use for
the private gateways network connection.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PhysicalNetworkId

The ID of the physical network this private
gateway belongs to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vlan

The VLAN number (1-4095) the network will use.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

The VPC ID in which to create this Private gateway. Changing
this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

