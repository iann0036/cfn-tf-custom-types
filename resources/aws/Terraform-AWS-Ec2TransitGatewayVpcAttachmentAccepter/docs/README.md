# Terraform::AWS::Ec2TransitGatewayVpcAttachmentAccepter

CloudFormation equivalent of aws_ec2_transit_gateway_vpc_attachment_accepter

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::Ec2TransitGatewayVpcAttachmentAccepter",
    "Properties" : {
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#transitgatewayattachmentid" title="TransitGatewayAttachmentId">TransitGatewayAttachmentId</a>" : <i>String</i>,
        "<a href="#transitgatewaydefaultroutetableassociation" title="TransitGatewayDefaultRouteTableAssociation">TransitGatewayDefaultRouteTableAssociation</a>" : <i>Boolean</i>,
        "<a href="#transitgatewaydefaultroutetablepropagation" title="TransitGatewayDefaultRouteTablePropagation">TransitGatewayDefaultRouteTablePropagation</a>" : <i>Boolean</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::Ec2TransitGatewayVpcAttachmentAccepter
Properties:
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#transitgatewayattachmentid" title="TransitGatewayAttachmentId">TransitGatewayAttachmentId</a>: <i>String</i>
    <a href="#transitgatewaydefaultroutetableassociation" title="TransitGatewayDefaultRouteTableAssociation">TransitGatewayDefaultRouteTableAssociation</a>: <i>Boolean</i>
    <a href="#transitgatewaydefaultroutetablepropagation" title="TransitGatewayDefaultRouteTablePropagation">TransitGatewayDefaultRouteTablePropagation</a>: <i>Boolean</i>
</pre>

## Properties

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransitGatewayAttachmentId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransitGatewayDefaultRouteTableAssociation

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransitGatewayDefaultRouteTablePropagation

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### DnsSupport

Returns the <code>DnsSupport</code> value.

#### Ipv6Support

Returns the <code>Ipv6Support</code> value.

#### SubnetIds

Returns the <code>SubnetIds</code> value.

#### TransitGatewayId

Returns the <code>TransitGatewayId</code> value.

#### VpcId

Returns the <code>VpcId</code> value.

#### VpcOwnerId

Returns the <code>VpcOwnerId</code> value.

