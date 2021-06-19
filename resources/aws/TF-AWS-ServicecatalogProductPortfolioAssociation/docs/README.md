# TF::AWS::ServicecatalogProductPortfolioAssociation

Manages a Service Catalog Product Portfolio Association.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::ServicecatalogProductPortfolioAssociation",
    "Properties" : {
        "<a href="#acceptlanguage" title="AcceptLanguage">AcceptLanguage</a>" : <i>String</i>,
        "<a href="#portfolioid" title="PortfolioId">PortfolioId</a>" : <i>String</i>,
        "<a href="#productid" title="ProductId">ProductId</a>" : <i>String</i>,
        "<a href="#sourceportfolioid" title="SourcePortfolioId">SourcePortfolioId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::ServicecatalogProductPortfolioAssociation
Properties:
    <a href="#acceptlanguage" title="AcceptLanguage">AcceptLanguage</a>: <i>String</i>
    <a href="#portfolioid" title="PortfolioId">PortfolioId</a>: <i>String</i>
    <a href="#productid" title="ProductId">ProductId</a>: <i>String</i>
    <a href="#sourceportfolioid" title="SourcePortfolioId">SourcePortfolioId</a>: <i>String</i>
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

#### ProductId

Product identifier.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourcePortfolioId

Identifier of the source portfolio.

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

#### Id

Returns the <code>Id</code> value.

