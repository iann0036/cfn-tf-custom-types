# Terraform::AzureRM::MonitorAutoscaleSetting

Manages a AutoScale Setting which can be applied to Virtual Machine Scale Sets, App Services and other scalable resources.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::MonitorAutoscaleSetting",
    "Properties" : {
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#targetresourceid" title="TargetResourceId">TargetResourceId</a>" : <i>String</i>,
        "<a href="#notification" title="Notification">Notification</a>" : <i>[ <a href="notification.md">Notification</a>, ... ]</i>,
        "<a href="#profile" title="Profile">Profile</a>" : <i>[ <a href="profile.md">Profile</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#email" title="Email">Email</a>" : <i>[ <a href="email.md">Email</a>, ... ]</i>,
        "<a href="#webhook" title="Webhook">Webhook</a>" : <i>[ <a href="webhook.md">Webhook</a>, ... ]</i>,
        "<a href="#capacity" title="Capacity">Capacity</a>" : <i>[ <a href="capacity.md">Capacity</a>, ... ]</i>,
        "<a href="#fixeddate" title="FixedDate">FixedDate</a>" : <i>[ <a href="fixeddate.md">FixedDate</a>, ... ]</i>,
        "<a href="#recurrence" title="Recurrence">Recurrence</a>" : <i>[ <a href="recurrence.md">Recurrence</a>, ... ]</i>,
        "<a href="#rule" title="Rule">Rule</a>" : <i>[ <a href="rule.md">Rule</a>, ... ]</i>,
        "<a href="#metrictrigger" title="MetricTrigger">MetricTrigger</a>" : <i>[ <a href="metrictrigger.md">MetricTrigger</a>, ... ]</i>,
        "<a href="#scaleaction" title="ScaleAction">ScaleAction</a>" : <i>[ <a href="scaleaction.md">ScaleAction</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::MonitorAutoscaleSetting
Properties:
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#targetresourceid" title="TargetResourceId">TargetResourceId</a>: <i>String</i>
    <a href="#notification" title="Notification">Notification</a>: <i>
      - <a href="notification.md">Notification</a></i>
    <a href="#profile" title="Profile">Profile</a>: <i>
      - <a href="profile.md">Profile</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#email" title="Email">Email</a>: <i>
      - <a href="email.md">Email</a></i>
    <a href="#webhook" title="Webhook">Webhook</a>: <i>
      - <a href="webhook.md">Webhook</a></i>
    <a href="#capacity" title="Capacity">Capacity</a>: <i>
      - <a href="capacity.md">Capacity</a></i>
    <a href="#fixeddate" title="FixedDate">FixedDate</a>: <i>
      - <a href="fixeddate.md">FixedDate</a></i>
    <a href="#recurrence" title="Recurrence">Recurrence</a>: <i>
      - <a href="recurrence.md">Recurrence</a></i>
    <a href="#rule" title="Rule">Rule</a>: <i>
      - <a href="rule.md">Rule</a></i>
    <a href="#metrictrigger" title="MetricTrigger">MetricTrigger</a>: <i>
      - <a href="metrictrigger.md">MetricTrigger</a></i>
    <a href="#scaleaction" title="ScaleAction">ScaleAction</a>: <i>
      - <a href="scaleaction.md">ScaleAction</a></i>
</pre>

## Properties

#### Enabled

Specifies whether automatic scaling is enabled for the target resource. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

Specifies the supported Azure location where the AutoScale Setting should exist. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the AutoScale Setting. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the Resource Group in the AutoScale Setting should be created. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetResourceId

Specifies the resource ID of the resource that the autoscale setting should be added to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notification

_Required_: No

_Type_: List of <a href="notification.md">Notification</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Profile

_Required_: No

_Type_: List of <a href="profile.md">Profile</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

_Required_: No

_Type_: List of <a href="email.md">Email</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Webhook

_Required_: No

_Type_: List of <a href="webhook.md">Webhook</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Capacity

_Required_: No

_Type_: List of <a href="capacity.md">Capacity</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FixedDate

_Required_: No

_Type_: List of <a href="fixeddate.md">FixedDate</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Recurrence

_Required_: No

_Type_: List of <a href="recurrence.md">Recurrence</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No

_Type_: List of <a href="rule.md">Rule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricTrigger

_Required_: No

_Type_: List of <a href="metrictrigger.md">MetricTrigger</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleAction

_Required_: No

_Type_: List of <a href="scaleaction.md">ScaleAction</a>

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

