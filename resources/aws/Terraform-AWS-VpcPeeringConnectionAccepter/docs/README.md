# Terraform::AWS::VpcPeeringConnectionAccepter

CloudFormation equivalent of aws_vpc_peering_connection_accepter

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::VpcPeeringConnectionAccepter",
    "Properties" : {
        "<a href="#autoaccept" title="AutoAccept">AutoAccept</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#vpcpeeringconnectionid" title="VpcPeeringConnectionId">VpcPeeringConnectionId</a>" : <i>String</i>,
        "<a href="#accepter" title="Accepter">Accepter</a>" : <i>[ <a href="accepter.md">Accepter</a>, ... ]</i>,
        "<a href="#requester" title="Requester">Requester</a>" : <i>[ <a href="requester.md">Requester</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::VpcPeeringConnectionAccepter
Properties:
    <a href="#autoaccept" title="AutoAccept">AutoAccept</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#vpcpeeringconnectionid" title="VpcPeeringConnectionId">VpcPeeringConnectionId</a>: <i>String</i>
    <a href="#accepter" title="Accepter">Accepter</a>: <i>
      - <a href="accepter.md">Accepter</a></i>
    <a href="#requester" title="Requester">Requester</a>: <i>
      - <a href="requester.md">Requester</a></i>
</pre>

## Properties

#### AutoAccept

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcPeeringConnectionId

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

#### PeerOwnerId

Returns the <code>PeerOwnerId</code> value.

#### PeerRegion

Returns the <code>PeerRegion</code> value.

#### PeerVpcId

Returns the <code>PeerVpcId</code> value.

#### VpcId

Returns the <code>VpcId</code> value.

