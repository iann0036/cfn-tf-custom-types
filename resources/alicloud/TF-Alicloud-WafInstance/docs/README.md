# TF::Alicloud::WafInstance

Provides a WAF Instance resource to create instance in the Web Application Firewall.

For information about WAF and how to use it, see [What is Alibaba Cloud WAF](https://www.alibabacloud.com/help/doc-detail/28517.htm).

-> **NOTE:** Available in 1.83.0+ .

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::WafInstance",
    "Properties" : {
        "<a href="#bigscreen" title="BigScreen">BigScreen</a>" : <i>String</i>,
        "<a href="#exclusiveippackage" title="ExclusiveIpPackage">ExclusiveIpPackage</a>" : <i>String</i>,
        "<a href="#extbandwidth" title="ExtBandwidth">ExtBandwidth</a>" : <i>String</i>,
        "<a href="#extdomainpackage" title="ExtDomainPackage">ExtDomainPackage</a>" : <i>String</i>,
        "<a href="#logstorage" title="LogStorage">LogStorage</a>" : <i>String</i>,
        "<a href="#logtime" title="LogTime">LogTime</a>" : <i>String</i>,
        "<a href="#modifytype" title="ModifyType">ModifyType</a>" : <i>String</i>,
        "<a href="#packagecode" title="PackageCode">PackageCode</a>" : <i>String</i>,
        "<a href="#period" title="Period">Period</a>" : <i>Double</i>,
        "<a href="#prefessionalservice" title="PrefessionalService">PrefessionalService</a>" : <i>String</i>,
        "<a href="#renewperiod" title="RenewPeriod">RenewPeriod</a>" : <i>Double</i>,
        "<a href="#renewalstatus" title="RenewalStatus">RenewalStatus</a>" : <i>String</i>,
        "<a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>" : <i>String</i>,
        "<a href="#subscriptiontype" title="SubscriptionType">SubscriptionType</a>" : <i>String</i>,
        "<a href="#waflog" title="WafLog">WafLog</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::WafInstance
Properties:
    <a href="#bigscreen" title="BigScreen">BigScreen</a>: <i>String</i>
    <a href="#exclusiveippackage" title="ExclusiveIpPackage">ExclusiveIpPackage</a>: <i>String</i>
    <a href="#extbandwidth" title="ExtBandwidth">ExtBandwidth</a>: <i>String</i>
    <a href="#extdomainpackage" title="ExtDomainPackage">ExtDomainPackage</a>: <i>String</i>
    <a href="#logstorage" title="LogStorage">LogStorage</a>: <i>String</i>
    <a href="#logtime" title="LogTime">LogTime</a>: <i>String</i>
    <a href="#modifytype" title="ModifyType">ModifyType</a>: <i>String</i>
    <a href="#packagecode" title="PackageCode">PackageCode</a>: <i>String</i>
    <a href="#period" title="Period">Period</a>: <i>Double</i>
    <a href="#prefessionalservice" title="PrefessionalService">PrefessionalService</a>: <i>String</i>
    <a href="#renewperiod" title="RenewPeriod">RenewPeriod</a>: <i>Double</i>
    <a href="#renewalstatus" title="RenewalStatus">RenewalStatus</a>: <i>String</i>
    <a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>: <i>String</i>
    <a href="#subscriptiontype" title="SubscriptionType">SubscriptionType</a>: <i>String</i>
    <a href="#waflog" title="WafLog">WafLog</a>: <i>String</i>
</pre>

## Properties

#### BigScreen

Specify whether big screen is supported. Valid values: ["0", "1"]. "0" for false and "1" for true.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExclusiveIpPackage

Specify the number of exclusive WAF IP addresses.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtBandwidth

The extra bandwidth. Unit: Mbit/s.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtDomainPackage

The number of extra domains.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogStorage

Log storage size. Unit: T. Valid values: [3, 5, 10, 20, 50].

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogTime

Log storage period. Unit: day. Valid values: [180, 360].

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ModifyType

Type of configuration change. Valid value: Upgrade.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PackageCode

Subscription plan:
* China site customers can purchase the following versions of China Mainland region, valid values: ["version_3", "version_4", "version_5"].
* China site customers can purchase the following versions of International region, valid values: ["version_pro_asia", "version_business_asia", "version_enterprise_asia"]
* International site customers can purchase the following versions of China Mainland region: ["version_pro_china", "version_business_china", "version_enterprise_china"]
* International site customers can purchase the following versions of International region: ["version_pro", "version_business", "version_enterprise"].

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

Service time of Web Application Firewall.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefessionalService

Specify whether professional service is supported. Valid values: ["true", "false"].

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RenewPeriod

Renewal period of WAF service. Unit: month.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RenewalStatus

Renewal status of WAF service. Valid values:
* AutoRenewal: The service time of WAF is renewed automatically.
* ManualRenewal (default): The service time of WAF is renewed manually.Specifies whether to configure a Layer-7 proxy, such as Anti-DDoS Pro or CDN, to filter the inbound traffic before it is forwarded to WAF. Valid values: "On" and "Off". Default to "Off".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupId

The resource group ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubscriptionType

Subscription of WAF service. Valid values: ["Subscription", "PayAsYouGo"].

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WafLog

Specify whether Log service is supported. Valid values: ["true", "false"].

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

#### Status

Returns the <code>Status</code> value.

