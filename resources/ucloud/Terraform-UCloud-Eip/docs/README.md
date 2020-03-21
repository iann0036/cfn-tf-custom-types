# Terraform::UCloud::Eip

Provides an Elastic IP resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::UCloud::Eip",
    "Properties" : {
        "<a href="#bandwidth" title="Bandwidth">Bandwidth</a>" : <i>Double</i>,
        "<a href="#chargemode" title="ChargeMode">ChargeMode</a>" : <i>String</i>,
        "<a href="#chargetype" title="ChargeType">ChargeType</a>" : <i>String</i>,
        "<a href="#duration" title="Duration">Duration</a>" : <i>Double</i>,
        "<a href="#internettype" title="InternetType">InternetType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#remark" title="Remark">Remark</a>" : <i>String</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::UCloud::Eip
Properties:
    <a href="#bandwidth" title="Bandwidth">Bandwidth</a>: <i>Double</i>
    <a href="#chargemode" title="ChargeMode">ChargeMode</a>: <i>String</i>
    <a href="#chargetype" title="ChargeType">ChargeType</a>: <i>String</i>
    <a href="#duration" title="Duration">Duration</a>: <i>Double</i>
    <a href="#internettype" title="InternetType">InternetType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#remark" title="Remark">Remark</a>: <i>String</i>
    <a href="#tag" title="Tag">Tag</a>: <i>String</i>
</pre>

## Properties

#### Bandwidth

Maximum bandwidth to the elastic public network, measured in Mbps (Mega bit per second). The ranges for bandwidth are: 1-200 for pay by traffic, 1-800 for pay by bandwidth. (Default: `1`).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChargeMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChargeType

Elastic IP charge type. Possible values are: `year` as pay by year, `month` as pay by month, `dynamic` as pay by hour (specific permission required). (Default: `month`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Duration

The duration that you will buy the resource. (Default: `1`). It is not required when `dynamic` (pay by hour), the value is `0` when `month`(pay by month) and the instance will be valid till the last day of that month.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetType

Type of Elastic IP routes. Possible values are: `international` as international BGP IP and `bgp` as china mainland BGP IP.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the EIP, which contains 1-63 characters and only support Chinese, English, numbers, '-', '_', '.'. If not specified, terraform will auto-generate a name beginning with `tf-eip`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Remark

The remarks of the EIP. (Default: `""`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

A tag assigned to Elastic IP, which contains at most 63 characters and only support Chinese, English, numbers, '-', '_', and '.'. If it is not filled in or a empty string is filled in, then default tag will be assigned. (Default: `Default`).

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

#### CreateTime

Returns the <code>CreateTime</code> value.

#### ExpireTime

Returns the <code>ExpireTime</code> value.

#### IpSet

Returns the <code>IpSet</code> value.

#### PublicIp

Returns the <code>PublicIp</code> value.

#### Resource

Returns the <code>Resource</code> value.

#### Status

Returns the <code>Status</code> value.

