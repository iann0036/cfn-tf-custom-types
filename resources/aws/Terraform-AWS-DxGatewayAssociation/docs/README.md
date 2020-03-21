# Terraform::AWS::DxGatewayAssociation

CloudFormation equivalent of aws_dx_gateway_association

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::DxGatewayAssociation",
    "Properties" : {
        "<a href="#allowedprefixes" title="AllowedPrefixes">AllowedPrefixes</a>" : <i>[ String, ... ]</i>,
        "<a href="#associatedgatewayid" title="AssociatedGatewayId">AssociatedGatewayId</a>" : <i>String</i>,
        "<a href="#associatedgatewayowneraccountid" title="AssociatedGatewayOwnerAccountId">AssociatedGatewayOwnerAccountId</a>" : <i>String</i>,
        "<a href="#dxgatewayid" title="DxGatewayId">DxGatewayId</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#proposalid" title="ProposalId">ProposalId</a>" : <i>String</i>,
        "<a href="#vpngatewayid" title="VpnGatewayId">VpnGatewayId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::DxGatewayAssociation
Properties:
    <a href="#allowedprefixes" title="AllowedPrefixes">AllowedPrefixes</a>: <i>
      - String</i>
    <a href="#associatedgatewayid" title="AssociatedGatewayId">AssociatedGatewayId</a>: <i>String</i>
    <a href="#associatedgatewayowneraccountid" title="AssociatedGatewayOwnerAccountId">AssociatedGatewayOwnerAccountId</a>: <i>String</i>
    <a href="#dxgatewayid" title="DxGatewayId">DxGatewayId</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#proposalid" title="ProposalId">ProposalId</a>: <i>String</i>
    <a href="#vpngatewayid" title="VpnGatewayId">VpnGatewayId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### AllowedPrefixes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssociatedGatewayId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssociatedGatewayOwnerAccountId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DxGatewayId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProposalId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnGatewayId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

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

Returns the &lt;code&gt;AssociatedGatewayType&lt;/code&gt; value.

#### DxGatewayAssociationId

Returns the &lt;code&gt;DxGatewayAssociationId&lt;/code&gt; value.

#### DxGatewayOwnerAccountId

Returns the &lt;code&gt;DxGatewayOwnerAccountId&lt;/code&gt; value.

