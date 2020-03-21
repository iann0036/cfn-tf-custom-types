# Terraform::Heroku::SpacePeeringConnectionAccepter

Provides a resource for accepting VPC peering requests to Heroku Private Spaces.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Heroku::SpacePeeringConnectionAccepter",
    "Properties" : {
        "<a href="#space" title="Space">Space</a>" : <i>String</i>,
        "<a href="#vpcpeeringconnectionid" title="VpcPeeringConnectionId">VpcPeeringConnectionId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Heroku::SpacePeeringConnectionAccepter
Properties:
    <a href="#space" title="Space">Space</a>: <i>String</i>
    <a href="#vpcpeeringconnectionid" title="VpcPeeringConnectionId">VpcPeeringConnectionId</a>: <i>String</i>
</pre>

## Properties

#### Space

The name of the space.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcPeeringConnectionId

The peering connection request ID.

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

#### Status

Returns the <code>Status</code> value.

#### Type

Returns the <code>Type</code> value.

