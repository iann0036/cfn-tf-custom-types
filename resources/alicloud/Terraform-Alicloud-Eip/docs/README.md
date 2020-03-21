# Terraform::Alicloud::Eip

Provides an elastic IP resource.

-> **NOTE:** The resource only supports to create `PostPaid PayByTraffic`  or `PrePaid PayByBandwidth` elastic IP for international account. Otherwise, you will happened error `COMMODITY.INVALID_COMPONENT`.
Your account is international if you can use it to login in [International Web Console](https://account.alibabacloud.com/login/login.htm).

-> **NOTE:** From version 1.10.1, this resource supports creating "PrePaid" EIP. In addition, it supports setting EIP name and description.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::Eip",
    "Properties" : {
        "<a href="#bandwidth" title="Bandwidth">Bandwidth</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#instancechargetype" title="InstanceChargeType">InstanceChargeType</a>" : <i>String</i>,
        "<a href="#internetchargetype" title="InternetChargeType">InternetChargeType</a>" : <i>String</i>,
        "<a href="#isp" title="Isp">Isp</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#period" title="Period">Period</a>" : <i>Double</i>,
        "<a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::Eip
Properties:
    <a href="#bandwidth" title="Bandwidth">Bandwidth</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#instancechargetype" title="InstanceChargeType">InstanceChargeType</a>: <i>String</i>
    <a href="#internetchargetype" title="InternetChargeType">InternetChargeType</a>: <i>String</i>
    <a href="#isp" title="Isp">Isp</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#period" title="Period">Period</a>: <i>Double</i>
    <a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
</pre>

## Properties

#### Bandwidth

Maximum bandwidth to the elastic public network, measured in Mbps (Mega bit per second). If this value is not specified, then automatically sets it to 5 Mbps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the EIP instance, This description can have a string of 2 to 256 characters, It cannot begin with http:// or https://. Default value is null.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceChargeType

Elastic IP instance charge type. Valid values are "PrePaid" and "PostPaid". Default to "PostPaid".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetChargeType

Internet charge type of the EIP, Valid values are `PayByBandwidth`, `PayByTraffic`. Default to `PayByBandwidth`. From version `1.7.1`, default to `PayByTraffic`. It is only PayByBandwidth when `instance_charge_type` is PrePaid.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Isp

The line type of the Elastic IP instance. Default to `BGP`. Other type of the isp need to open a whitelist.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the EIP instance. This name can have a string of 2 to 128 characters, must contain only alphanumeric characters or hyphens, such as "-",".","_", and must not begin or end with a hyphen, and must not begin with http:// or https://.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

The duration that you will buy the resource, in month. It is valid when `instance_charge_type` is `PrePaid`.
Default to 1. Valid values: [1-9, 12, 24, 36]. At present, the provider does not support modify "period" and you can do that via web console.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupId

The Id of resource group which the eip belongs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### IpAddress

Returns the <code>IpAddress</code> value.

#### Status

Returns the <code>Status</code> value.

