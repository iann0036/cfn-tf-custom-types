# Terraform::CloudStack::Network

Creates a network.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::CloudStack::Network",
    "Properties" : {
        "<a href="#aclid" title="AclId">AclId</a>" : <i>String</i>,
        "<a href="#cidr" title="Cidr">Cidr</a>" : <i>String</i>,
        "<a href="#displaytext" title="DisplayText">DisplayText</a>" : <i>String</i>,
        "<a href="#endip" title="Endip">Endip</a>" : <i>String</i>,
        "<a href="#gateway" title="Gateway">Gateway</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkdomain" title="NetworkDomain">NetworkDomain</a>" : <i>String</i>,
        "<a href="#networkoffering" title="NetworkOffering">NetworkOffering</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#sourcenatip" title="SourceNatIp">SourceNatIp</a>" : <i>Boolean</i>,
        "<a href="#startip" title="Startip">Startip</a>" : <i>String</i>,
        "<a href="#vlan" title="Vlan">Vlan</a>" : <i>Double</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::CloudStack::Network
Properties:
    <a href="#aclid" title="AclId">AclId</a>: <i>String</i>
    <a href="#cidr" title="Cidr">Cidr</a>: <i>String</i>
    <a href="#displaytext" title="DisplayText">DisplayText</a>: <i>String</i>
    <a href="#endip" title="Endip">Endip</a>: <i>String</i>
    <a href="#gateway" title="Gateway">Gateway</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkdomain" title="NetworkDomain">NetworkDomain</a>: <i>String</i>
    <a href="#networkoffering" title="NetworkOffering">NetworkOffering</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#sourcenatip" title="SourceNatIp">SourceNatIp</a>: <i>Boolean</i>
    <a href="#startip" title="Startip">Startip</a>: <i>String</i>
    <a href="#vlan" title="Vlan">Vlan</a>: <i>Double</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
</pre>

## Properties

#### AclId

The ACL ID that should be attached to the network or
`none` if you do not want to attach an ACL. You can dynamically attach and
swap ACL's, but if you want to detach an attached ACL and revert to using
`none`, this will force a new resource to be created. (defaults `none`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cidr

The CIDR block for the network. Changing this forces a new
resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayText

The display text of the network.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Endip

End of the IP block that will be available on the
network. Defaults to the last available IP in the range.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gateway

Gateway that will be provided to the instances in this
network. Defaults to the first usable IP in the range.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the network.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkDomain

DNS domain for the network.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkOffering

The name or ID of the network offering to use
for this network.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The name or ID of the project to deploy this
instance to. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceNatIp

If set to `true` a public IP will be associated
with the network. This is mainly used when the network supports the source
NAT service which claims the first associated IP address. This prevents the
ability to manage the IP address as an independent entity.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Startip

Start of the IP block that will be available on the
network. Defaults to the second available IP in the range.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vlan

The VLAN number (1-4095) the network will use. This might be
required by the Network Offering if specifyVlan=true is set. Only the ROOT
admin can set this value.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

The VPC ID in which to create this network. Changing
this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

The name or ID of the zone where this network will be
available. Changing this forces a new resource to be created.

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

#### Id

Returns the <code>Id</code> value.

#### SourceNatIpId

Returns the <code>SourceNatIpId</code> value.

