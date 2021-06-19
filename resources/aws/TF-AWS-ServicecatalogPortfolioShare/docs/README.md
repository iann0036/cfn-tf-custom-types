# TF::AWS::ServicecatalogPortfolioShare

Manages a Service Catalog Portfolio Share. Shares the specified portfolio with the specified account or organization node. You can share portfolios to an organization, an organizational unit, or a specific account.

If the portfolio share with the specified account or organization node already exists, using this resource to re-create the share will have no effect and will not return an error. You can then use this resource to update the share.

~> **NOTE:** Shares to an organization node can only be created by the management account of an organization or by a delegated administrator. If a delegated admin is de-registered, they can no longer create portfolio shares.

~> **NOTE:** AWSOrganizationsAccess must be enabled in order to create a portfolio share to an organization node.

~> **NOTE:** You can't share a shared resource, including portfolios that contain a shared product.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::ServicecatalogPortfolioShare",
    "Properties" : {
        "<a href="#acceptlanguage" title="AcceptLanguage">AcceptLanguage</a>" : <i>String</i>,
        "<a href="#portfolioid" title="PortfolioId">PortfolioId</a>" : <i>String</i>,
        "<a href="#principalid" title="PrincipalId">PrincipalId</a>" : <i>String</i>,
        "<a href="#sharetagoptions" title="ShareTagOptions">ShareTagOptions</a>" : <i>Boolean</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#waitforacceptance" title="WaitForAcceptance">WaitForAcceptance</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::ServicecatalogPortfolioShare
Properties:
    <a href="#acceptlanguage" title="AcceptLanguage">AcceptLanguage</a>: <i>String</i>
    <a href="#portfolioid" title="PortfolioId">PortfolioId</a>: <i>String</i>
    <a href="#principalid" title="PrincipalId">PrincipalId</a>: <i>String</i>
    <a href="#sharetagoptions" title="ShareTagOptions">ShareTagOptions</a>: <i>Boolean</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#waitforacceptance" title="WaitForAcceptance">WaitForAcceptance</a>: <i>Boolean</i>
</pre>

## Properties

#### AcceptLanguage

Language code. Valid values: `en` (English), `jp` (Japanese), `zh` (Chinese). Default value is `en`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortfolioId

Portfolio identifier.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrincipalId

Identifier of the principal with whom you will share the portfolio. Valid values AWS account IDs and ARNs of AWS Organizations and organizational units.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShareTagOptions

Whether to enable sharing of `aws_servicecatalog_tag_option` resources when creating the portfolio share.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Type of portfolio share. Valid values are `ACCOUNT` (an external account), `ORGANIZATION` (a share to every account in an organization), `ORGANIZATIONAL_UNIT`, `ORGANIZATION_MEMBER_ACCOUNT` (a share to an account in an organization).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForAcceptance

Whether to wait (up to the timeout) for the share to be accepted. Organizational shares are automatically accepted.

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

#### Accepted

Returns the <code>Accepted</code> value.

#### Id

Returns the <code>Id</code> value.

