# TF::Alicloud::EcsDedicatedHost

This resouce used to create a dedicated host and store its initial version. For information about Aliecs Dedicated Host and how to use it, see [What is Resource Aliecs Dedicated Host](https://www.alibabacloud.com/help/doc-detail/134238.htm).

-> **NOTE:** Available in 1.91.0+.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::EcsDedicatedHost",
    "Properties" : {
        "<a href="#actiononmaintenance" title="ActionOnMaintenance">ActionOnMaintenance</a>" : <i>String</i>,
        "<a href="#autoplacement" title="AutoPlacement">AutoPlacement</a>" : <i>String</i>,
        "<a href="#autoreleasetime" title="AutoReleaseTime">AutoReleaseTime</a>" : <i>String</i>,
        "<a href="#autorenew" title="AutoRenew">AutoRenew</a>" : <i>Boolean</i>,
        "<a href="#autorenewperiod" title="AutoRenewPeriod">AutoRenewPeriod</a>" : <i>Double</i>,
        "<a href="#cpuovercommitratio" title="CpuOverCommitRatio">CpuOverCommitRatio</a>" : <i>Double</i>,
        "<a href="#dedicatedhostclusterid" title="DedicatedHostClusterId">DedicatedHostClusterId</a>" : <i>String</i>,
        "<a href="#dedicatedhostname" title="DedicatedHostName">DedicatedHostName</a>" : <i>String</i>,
        "<a href="#dedicatedhosttype" title="DedicatedHostType">DedicatedHostType</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#detailfee" title="DetailFee">DetailFee</a>" : <i>Boolean</i>,
        "<a href="#dryrun" title="DryRun">DryRun</a>" : <i>Boolean</i>,
        "<a href="#expiredtime" title="ExpiredTime">ExpiredTime</a>" : <i>String</i>,
        "<a href="#minquantity" title="MinQuantity">MinQuantity</a>" : <i>Double</i>,
        "<a href="#paymenttype" title="PaymentType">PaymentType</a>" : <i>String</i>,
        "<a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>" : <i>String</i>,
        "<a href="#salecycle" title="SaleCycle">SaleCycle</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>,
        "<a href="#networkattributes" title="NetworkAttributes">NetworkAttributes</a>" : <i>[ <a href="networkattributesdefinition.md">NetworkAttributesDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::EcsDedicatedHost
Properties:
    <a href="#actiononmaintenance" title="ActionOnMaintenance">ActionOnMaintenance</a>: <i>String</i>
    <a href="#autoplacement" title="AutoPlacement">AutoPlacement</a>: <i>String</i>
    <a href="#autoreleasetime" title="AutoReleaseTime">AutoReleaseTime</a>: <i>String</i>
    <a href="#autorenew" title="AutoRenew">AutoRenew</a>: <i>Boolean</i>
    <a href="#autorenewperiod" title="AutoRenewPeriod">AutoRenewPeriod</a>: <i>Double</i>
    <a href="#cpuovercommitratio" title="CpuOverCommitRatio">CpuOverCommitRatio</a>: <i>Double</i>
    <a href="#dedicatedhostclusterid" title="DedicatedHostClusterId">DedicatedHostClusterId</a>: <i>String</i>
    <a href="#dedicatedhostname" title="DedicatedHostName">DedicatedHostName</a>: <i>String</i>
    <a href="#dedicatedhosttype" title="DedicatedHostType">DedicatedHostType</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#detailfee" title="DetailFee">DetailFee</a>: <i>Boolean</i>
    <a href="#dryrun" title="DryRun">DryRun</a>: <i>Boolean</i>
    <a href="#expiredtime" title="ExpiredTime">ExpiredTime</a>: <i>String</i>
    <a href="#minquantity" title="MinQuantity">MinQuantity</a>: <i>Double</i>
    <a href="#paymenttype" title="PaymentType">PaymentType</a>: <i>String</i>
    <a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>: <i>String</i>
    <a href="#salecycle" title="SaleCycle">SaleCycle</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
    <a href="#networkattributes" title="NetworkAttributes">NetworkAttributes</a>: <i>
      - <a href="networkattributesdefinition.md">NetworkAttributesDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### ActionOnMaintenance

The policy used to migrate the instances from the dedicated host when the dedicated host fails or needs to be repaired online. Valid values: `Migrate`, `Stop`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoPlacement

Specifies whether to add the dedicated host to the resource pool for automatic deployment. If you do not specify the DedicatedHostId parameter when you create an instance on a dedicated host, Alibaba Cloud automatically selects a dedicated host from the resource pool to host the instance. Valid values: `on`, `off`. Default: `on`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoReleaseTime

The automatic release time of the dedicated host. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC+0.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoRenew

Specifies whether to automatically renew the subscription dedicated host.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoRenewPeriod

The auto-renewal period of the dedicated host. Unit: months. Valid values: `1`, `2`, `3`, `6`, and `12`. takes effect and is required only when the AutoRenew parameter is set to true.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuOverCommitRatio

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DedicatedHostClusterId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DedicatedHostName

The name of the dedicated host. The name must be 2 to 128 characters in length. It must start with a letter but cannot start with http:// or https://. It can contain letters, digits, colons (:), underscores (_), and hyphens (-).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DedicatedHostType

The type of the dedicated host. You can call the [DescribeDedicatedHostTypes](https://www.alibabacloud.com/help/doc-detail/134240.htm) operation to obtain the most recent list of dedicated host types.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description of the dedicated host. The description must be 2 to 256 characters in length and cannot start with http:// or https://.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DetailFee

Specifies whether to return the billing details of the order when the billing method is changed from subscription to pay-as-you-go. Default: `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DryRun

Specifies whether to only validate the request. Default: `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpiredTime

The subscription period of the dedicated host. The Period parameter takes effect and is required only when the ChargeType parameter is set to PrePaid.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinQuantity

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PaymentType

The billing method of the dedicated host. Valid values: `PrePaid`, `PostPaid`. Default: `PostPaid`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupId

The ID of the resource group to which the dedicated host belongs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SaleCycle

The unit of the subscription period of the dedicated host.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneId

The zone ID of the dedicated host. This parameter is empty by default. If you do not specify this parameter, the system automatically selects a zone.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkAttributes

_Required_: No

_Type_: List of <a href="networkattributesdefinition.md">NetworkAttributesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

