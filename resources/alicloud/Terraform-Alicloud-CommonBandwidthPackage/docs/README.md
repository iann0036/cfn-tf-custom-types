# Terraform::Alicloud::CommonBandwidthPackage

Provides a common bandwidth package resource.

-> **NOTE:** Terraform will auto build common bandwidth package instance while it uses `alicloud_common_bandwidth_package` to build a common bandwidth package resource.

For information about common bandwidth package and how to use it, see [What is Common Bandwidth Package](https://www.alibabacloud.com/help/product/55092.htm).

For information about common bandwidth package billing methods, see [Common Bandwidth Package Billing Methods](https://www.alibabacloud.com/help/doc-detail/67459.html?spm=a2c5t.11065259.1996646101.searchclickresult.7ec93235Vfkwhy).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::CommonBandwidthPackage",
    "Properties" : {
        "<a href="#bandwidth" title="Bandwidth">Bandwidth</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#internetchargetype" title="InternetChargeType">InternetChargeType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ratio" title="Ratio">Ratio</a>" : <i>Double</i>,
        "<a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::CommonBandwidthPackage
Properties:
    <a href="#bandwidth" title="Bandwidth">Bandwidth</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#internetchargetype" title="InternetChargeType">InternetChargeType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ratio" title="Ratio">Ratio</a>: <i>Double</i>
    <a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>: <i>String</i>
</pre>

## Properties

#### Bandwidth

The bandwidth of the common bandwidth package, in Mbps.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description of the common bandwidth package instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetChargeType

The billing method of the common bandwidth package. Valid values are "PayByBandwidth" and "PayBy95" and "PayByTraffic". "PayBy95" is pay by classic 95th percentile pricing. International Account doesn't supports "PayByBandwidth" and "PayBy95". Default to "PayByTraffic".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the common bandwidth package.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ratio

Ratio of the common bandwidth package. It is valid when `internet_charge_type` is `PayBy95`. Default to 100. Valid values: [10-100].

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupId

The Id of resource group which the common bandwidth package belongs.

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

