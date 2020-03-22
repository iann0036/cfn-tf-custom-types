# Terraform::TencentCloud::VpnGateway

Provides a resource to create a VPN gateway.

-> **NOTE:** The prepaid VPN gateway do not support renew operation or delete operation with terraform.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::VpnGateway",
    "Properties" : {
        "<a href="#bandwidth" title="Bandwidth">Bandwidth</a>" : <i>Double</i>,
        "<a href="#chargetype" title="ChargeType">ChargeType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#prepaidperiod" title="PrepaidPeriod">PrepaidPeriod</a>" : <i>Double</i>,
        "<a href="#prepaidrenewflag" title="PrepaidRenewFlag">PrepaidRenewFlag</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::VpnGateway
Properties:
    <a href="#bandwidth" title="Bandwidth">Bandwidth</a>: <i>Double</i>
    <a href="#chargetype" title="ChargeType">ChargeType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#prepaidperiod" title="PrepaidPeriod">PrepaidPeriod</a>: <i>Double</i>
    <a href="#prepaidrenewflag" title="PrepaidRenewFlag">PrepaidRenewFlag</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
</pre>

## Properties

#### Bandwidth

The maximum public network output bandwidth of VPN gateway (unit: Mbps), the available values include: 5,10,20,50,100. Default is 5. When charge type is `PREPAID`, bandwidth degradation operation is unsupported.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChargeType

Charge Type of the VPN gateway, valid values are `PREPAID`, `POSTPAID_BY_HOUR` and default is `POSTPAID_BY_HOUR`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the VPN gateway. The length of character is limited to 1-60.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrepaidPeriod

Period of instance to be prepaid. Valid values are 1, 2, 3, 4, 6, 7, 8, 9, 12, 24, 36 and unit is month. Caution: when this para and renew_flag para are valid, the request means to renew several months more pre-paid period. This para can only be set to take effect in create operation.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrepaidRenewFlag

Flag indicates whether to renew or not, valid values are `NOTIFY_AND_RENEW`, `NOTIFY_AND_AUTO_RENEW`, `NOT_NOTIFY_AND_NOT_RENEW`. This para can only be set to take effect in create operation.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A list of tags used to associate different resources.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

ID of the VPC.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

Zone of the VPN gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### ExpiredTime

Returns the <code>ExpiredTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### IsAddressBlocked

Returns the <code>IsAddressBlocked</code> value.

#### NewPurchasePlan

Returns the <code>NewPurchasePlan</code> value.

#### PublicIpAddress

Returns the <code>PublicIpAddress</code> value.

#### RestrictState

Returns the <code>RestrictState</code> value.

#### State

Returns the <code>State</code> value.

#### Type

Returns the <code>Type</code> value.

