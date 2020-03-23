# Terraform::AWS::VpcPeeringConnection

Provides a resource to manage a VPC peering connection.

~> **NOTE on VPC Peering Connections and VPC Peering Connection Options:** Terraform provides
both a standalone [VPC Peering Connection Options](vpc_peering_connection_options.html) and a VPC Peering Connection
resource with `accepter` and `requester` attributes. Do not manage options for the same VPC peering
connection in both a VPC Peering Connection resource and a VPC Peering Connection Options resource.
Doing so will cause a conflict of options and will overwrite the options.
Using a VPC Peering Connection Options resource decouples management of the connection options from
management of the VPC Peering Connection and allows options to be set correctly in cross-account scenarios.

-> **Note:** For cross-account (requester's AWS account differs from the accepter's AWS account) or inter-region
VPC Peering Connections use the `aws_vpc_peering_connection` resource to manage the requester's side of the
connection and use the `aws_vpc_peering_connection_accepter` resource to manage the accepter's side of the connection.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::VpcPeeringConnection",
    "Properties" : {
        "<a href="#autoaccept" title="AutoAccept">AutoAccept</a>" : <i>Boolean</i>,
        "<a href="#peerownerid" title="PeerOwnerId">PeerOwnerId</a>" : <i>String</i>,
        "<a href="#peerregion" title="PeerRegion">PeerRegion</a>" : <i>String</i>,
        "<a href="#peervpcid" title="PeerVpcId">PeerVpcId</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#accepter" title="Accepter">Accepter</a>" : <i>[ <a href="accepter.md">Accepter</a>, ... ]</i>,
        "<a href="#requester" title="Requester">Requester</a>" : <i>[ <a href="requester.md">Requester</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::VpcPeeringConnection
Properties:
    <a href="#autoaccept" title="AutoAccept">AutoAccept</a>: <i>Boolean</i>
    <a href="#peerownerid" title="PeerOwnerId">PeerOwnerId</a>: <i>String</i>
    <a href="#peerregion" title="PeerRegion">PeerRegion</a>: <i>String</i>
    <a href="#peervpcid" title="PeerVpcId">PeerVpcId</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#accepter" title="Accepter">Accepter</a>: <i>
      - <a href="accepter.md">Accepter</a></i>
    <a href="#requester" title="Requester">Requester</a>: <i>
      - <a href="requester.md">Requester</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AutoAccept

Accept the peering (both VPCs need to be in the same AWS account).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerOwnerId

The AWS account ID of the owner of the peer VPC.
Defaults to the account ID the [AWS provider][1] is currently connected to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerRegion

The region of the accepter VPC of the [VPC Peering Connection]. `auto_accept` must be `false`,
and use the `aws_vpc_peering_connection_accepter` to manage the accepter side.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerVpcId

The ID of the VPC with which you are creating the VPC Peering Connection.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

The ID of the requester VPC.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Accepter

_Required_: No

_Type_: List of <a href="accepter.md">Accepter</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Requester

_Required_: No

_Type_: List of <a href="requester.md">Requester</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AcceptStatus

Returns the <code>AcceptStatus</code> value.

#### Id

Returns the <code>Id</code> value.

