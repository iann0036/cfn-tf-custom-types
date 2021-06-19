# TF::AWS::DxGatewayAssociation

Associates a Direct Connect Gateway with a VGW or transit gateway.

To create a cross-account association, create an [`aws_dx_gateway_association_proposal` resource](/docs/providers/aws/r/dx_gateway_association_proposal.html)
in the AWS account that owns the VGW or transit gateway and then accept the proposal in the AWS account that owns the Direct Connect Gateway
by creating an `aws_dx_gateway_association` resource with the `proposal_id` and `associated_gateway_owner_account_id` attributes set.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::DxGatewayAssociation",
    "Properties" : {
        "<a href="#allowedprefixes" title="AllowedPrefixes">AllowedPrefixes</a>" : <i>[ String, ... ]</i>,
        "<a href="#associatedgatewayid" title="AssociatedGatewayId">AssociatedGatewayId</a>" : <i>String</i>,
        "<a href="#associatedgatewayowneraccountid" title="AssociatedGatewayOwnerAccountId">AssociatedGatewayOwnerAccountId</a>" : <i>String</i>,
        "<a href="#dxgatewayid" title="DxGatewayId">DxGatewayId</a>" : <i>String</i>,
        "<a href="#proposalid" title="ProposalId">ProposalId</a>" : <i>String</i>,
        "<a href="#vpngatewayid" title="VpnGatewayId">VpnGatewayId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::DxGatewayAssociation
Properties:
    <a href="#allowedprefixes" title="AllowedPrefixes">AllowedPrefixes</a>: <i>
      - String</i>
    <a href="#associatedgatewayid" title="AssociatedGatewayId">AssociatedGatewayId</a>: <i>String</i>
    <a href="#associatedgatewayowneraccountid" title="AssociatedGatewayOwnerAccountId">AssociatedGatewayOwnerAccountId</a>: <i>String</i>
    <a href="#dxgatewayid" title="DxGatewayId">DxGatewayId</a>: <i>String</i>
    <a href="#proposalid" title="ProposalId">ProposalId</a>: <i>String</i>
    <a href="#vpngatewayid" title="VpnGatewayId">VpnGatewayId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AllowedPrefixes

VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssociatedGatewayId

The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for single account Direct Connect gateway associations.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssociatedGatewayOwnerAccountId

The ID of the AWS account that owns the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for cross-account Direct Connect gateway associations.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DxGatewayId

The ID of the Direct Connect gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProposalId

The ID of the Direct Connect gateway association proposal.
Used for cross-account Direct Connect gateway associations.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnGatewayId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AssociatedGatewayType

Returns the <code>AssociatedGatewayType</code> value.

#### DxGatewayAssociationId

Returns the <code>DxGatewayAssociationId</code> value.

#### DxGatewayOwnerAccountId

Returns the <code>DxGatewayOwnerAccountId</code> value.

#### Id

Returns the <code>Id</code> value.

