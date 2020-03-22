# Terraform::Alicloud::MarketOrder

Provides a market order resource.

-> **NOTE:** Terraform will auto build a market order  while it uses `alicloud_market_order` to build a market order resource.

-> **NOTE:** Available in 1.69.0+

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::MarketOrder",
    "Properties" : {
        "<a href="#components" title="Components">Components</a>" : <i>[ <a href="components.md">Components</a>, ... ]</i>,
        "<a href="#couponid" title="CouponId">CouponId</a>" : <i>String</i>,
        "<a href="#duration" title="Duration">Duration</a>" : <i>Double</i>,
        "<a href="#packageversion" title="PackageVersion">PackageVersion</a>" : <i>String</i>,
        "<a href="#paytype" title="PayType">PayType</a>" : <i>String</i>,
        "<a href="#pricingcycle" title="PricingCycle">PricingCycle</a>" : <i>String</i>,
        "<a href="#productcode" title="ProductCode">ProductCode</a>" : <i>String</i>,
        "<a href="#quantity" title="Quantity">Quantity</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::MarketOrder
Properties:
    <a href="#components" title="Components">Components</a>: <i>
      - <a href="components.md">Components</a></i>
    <a href="#couponid" title="CouponId">CouponId</a>: <i>String</i>
    <a href="#duration" title="Duration">Duration</a>: <i>Double</i>
    <a href="#packageversion" title="PackageVersion">PackageVersion</a>: <i>String</i>
    <a href="#paytype" title="PayType">PayType</a>: <i>String</i>
    <a href="#pricingcycle" title="PricingCycle">PricingCycle</a>: <i>String</i>
    <a href="#productcode" title="ProductCode">ProductCode</a>: <i>String</i>
    <a href="#quantity" title="Quantity">Quantity</a>: <i>Double</i>
</pre>

## Properties

#### Components

Service providers customize additional components.

_Required_: No

_Type_: List of <a href="components.md">Components</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CouponId

The coupon id of the market product.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Duration

The number of purchase cycles.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PackageVersion

The package version of the market product.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PayType

Valid values are `PrePaid`, `PostPaid`,System default to `PostPaid`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PricingCycle

The purchase cycle of the product, valid values are `Day`, `Month` and `Year`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProductCode

The product_code of market place product.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Quantity

The quantity of the market product will be purchased.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

