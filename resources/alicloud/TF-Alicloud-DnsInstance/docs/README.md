# TF::Alicloud::DnsInstance

Create an DNS Instance resource.

-> **NOTE:** Available in v1.80.0+.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::DnsInstance",
    "Properties" : {
        "<a href="#dnssecurity" title="DnsSecurity">DnsSecurity</a>" : <i>String</i>,
        "<a href="#domainnumbers" title="DomainNumbers">DomainNumbers</a>" : <i>String</i>,
        "<a href="#paymenttype" title="PaymentType">PaymentType</a>" : <i>String</i>,
        "<a href="#period" title="Period">Period</a>" : <i>Double</i>,
        "<a href="#renewperiod" title="RenewPeriod">RenewPeriod</a>" : <i>Double</i>,
        "<a href="#renewalstatus" title="RenewalStatus">RenewalStatus</a>" : <i>String</i>,
        "<a href="#versioncode" title="VersionCode">VersionCode</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::DnsInstance
Properties:
    <a href="#dnssecurity" title="DnsSecurity">DnsSecurity</a>: <i>String</i>
    <a href="#domainnumbers" title="DomainNumbers">DomainNumbers</a>: <i>String</i>
    <a href="#paymenttype" title="PaymentType">PaymentType</a>: <i>String</i>
    <a href="#period" title="Period">Period</a>: <i>Double</i>
    <a href="#renewperiod" title="RenewPeriod">RenewPeriod</a>: <i>Double</i>
    <a href="#renewalstatus" title="RenewalStatus">RenewalStatus</a>: <i>String</i>
    <a href="#versioncode" title="VersionCode">VersionCode</a>: <i>String</i>
</pre>

## Properties

#### DnsSecurity

DNS security level. Valid values: `no`, `basic`, `advanced`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainNumbers

Number of domain names bound.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PaymentType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

Creating a pre-paid instance, it must be set, the unit is month, please enter an integer multiple of 12 for annually paid products.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RenewPeriod

Automatic renewal period, the unit is month. When setting RenewalStatus to AutoRenewal, it must be set.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RenewalStatus

Automatic renewal status. Valid values: `AutoRenewal`, `ManualRenewal`, default to `ManualRenewal`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionCode

Paid package version. Valid values: `version_personal`, `version_enterprise_basic`, `version_enterprise_advanced`.

_Required_: Yes

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

#### VersionName

Returns the <code>VersionName</code> value.

