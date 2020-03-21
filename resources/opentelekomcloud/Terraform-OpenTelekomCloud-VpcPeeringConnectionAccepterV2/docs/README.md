# Terraform::OpenTelekomCloud::VpcPeeringConnectionAccepterV2

Provides a resource to manage the accepter's side of a VPC Peering Connection.

When a cross-tenant (requester's tenant differs from the accepter's tenant) VPC Peering Connection is created, a VPC Peering Connection resource is automatically created in the
accepter's account.
The requester can use the `opentelekomcloud_vpc_peering_connection_v2` resource to manage its side of the connection
and the accepter can use the `opentelekomcloud_vpc_peering_connection_accepter_v2` resource to "adopt" its side of the
connection into management.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenTelekomCloud::VpcPeeringConnectionAccepterV2",
    "Properties" : {
        "<a href="#accept" title="Accept">Accept</a>" : <i>Boolean</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#vpcpeeringconnectionid" title="VpcPeeringConnectionId">VpcPeeringConnectionId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenTelekomCloud::VpcPeeringConnectionAccepterV2
Properties:
    <a href="#accept" title="Accept">Accept</a>: <i>Boolean</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#vpcpeeringconnectionid" title="VpcPeeringConnectionId">VpcPeeringConnectionId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Accept

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcPeeringConnectionId

_Required_: Yes

_Type_: String

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

#### Name

Returns the <code>Name</code> value.

#### PeerTenantId

Returns the <code>PeerTenantId</code> value.

#### PeerVpcId

Returns the <code>PeerVpcId</code> value.

#### Status

Returns the <code>Status</code> value.

#### VpcId

Returns the <code>VpcId</code> value.

