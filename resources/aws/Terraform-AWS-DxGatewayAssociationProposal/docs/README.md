# Terraform::AWS::DxGatewayAssociationProposal

Manages a Direct Connect Gateway Association Proposal, typically for enabling cross-account associations. For single account associations, see the [`aws_dx_gateway_association` resource](/docs/providers/aws/r/dx_gateway_association.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::DxGatewayAssociationProposal",
    "Properties" : {
        "<a href="#allowedprefixes" title="AllowedPrefixes">AllowedPrefixes</a>" : <i>[ String, ... ]</i>,
        "<a href="#associatedgatewayid" title="AssociatedGatewayId">AssociatedGatewayId</a>" : <i>String</i>,
        "<a href="#dxgatewayid" title="DxGatewayId">DxGatewayId</a>" : <i>String</i>,
        "<a href="#dxgatewayowneraccountid" title="DxGatewayOwnerAccountId">DxGatewayOwnerAccountId</a>" : <i>String</i>,
        "<a href="#vpngatewayid" title="VpnGatewayId">VpnGatewayId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::DxGatewayAssociationProposal
Properties:
    <a href="#allowedprefixes" title="AllowedPrefixes">AllowedPrefixes</a>: <i>
      - String</i>
    <a href="#associatedgatewayid" title="AssociatedGatewayId">AssociatedGatewayId</a>: <i>String</i>
    <a href="#dxgatewayid" title="DxGatewayId">DxGatewayId</a>: <i>String</i>
    <a href="#dxgatewayowneraccountid" title="DxGatewayOwnerAccountId">DxGatewayOwnerAccountId</a>: <i>String</i>
    <a href="#vpngatewayid" title="VpnGatewayId">VpnGatewayId</a>: <i>String</i>
</pre>

## Properties

#### AllowedPrefixes

VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssociatedGatewayId

The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DxGatewayId

Direct Connect Gateway identifier.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DxGatewayOwnerAccountId

AWS Account identifier of the Direct Connect Gateway's owner.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnGatewayId

*Deprecated:* Use `associated_gateway_id` instead. Virtual Gateway identifier to associate with the Direct Connect Gateway.

_Required_: No

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

#### AssociatedGatewayOwnerAccountId

Returns the <code>AssociatedGatewayOwnerAccountId</code> value.

#### AssociatedGatewayType

Returns the <code>AssociatedGatewayType</code> value.

#### Id

Returns the <code>Id</code> value.

