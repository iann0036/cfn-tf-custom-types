# TF::AzureRM::LogAnalyticsSolution PlanDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#product" title="Product">Product</a>" : <i>String</i>,
    "<a href="#promotioncode" title="PromotionCode">PromotionCode</a>" : <i>String</i>,
    "<a href="#publisher" title="Publisher">Publisher</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#product" title="Product">Product</a>: <i>String</i>
<a href="#promotioncode" title="PromotionCode">PromotionCode</a>: <i>String</i>
<a href="#publisher" title="Publisher">Publisher</a>: <i>String</i>
</pre>

## Properties

#### Product

The product name of the solution. For example `OMSGallery/Containers`. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PromotionCode

A promotion code to be used with the solution.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Publisher

The publisher of the solution. For example `Microsoft`. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

