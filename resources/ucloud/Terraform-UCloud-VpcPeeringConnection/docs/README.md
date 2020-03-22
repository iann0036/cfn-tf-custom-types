# Terraform::UCloud::VpcPeeringConnection

Provides an VPC Peering Connection for establishing a connection between multiple VPC.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::UCloud::VpcPeeringConnection",
    "Properties" : {
        "<a href="#peerprojectid" title="PeerProjectId">PeerProjectId</a>" : <i>String</i>,
        "<a href="#peervpcid" title="PeerVpcId">PeerVpcId</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::UCloud::VpcPeeringConnection
Properties:
    <a href="#peerprojectid" title="PeerProjectId">PeerProjectId</a>: <i>String</i>
    <a href="#peervpcid" title="PeerVpcId">PeerVpcId</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
</pre>

## Properties

#### PeerProjectId

The ID of accepter project of the specific VPC Peering Connection to retrieve.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerVpcId

The short ID of accepter VPC of the specific VPC Peering Connection to retrieve.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

The short of ID of the requester VPC of the specific VPC Peering Connection to retrieve.

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

