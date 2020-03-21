# Terraform::AzureRM::MonitorAutoscaleSetting

CloudFormation equivalent of azurerm_monitor_autoscale_setting

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::MonitorAutoscaleSetting",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#targetresourceid" title="TargetResourceId">TargetResourceId</a>" : <i>String</i>,
        "<a href="#notification" title="Notification">Notification</a>" : <i>[ &lt;a href=&#34;notification.md&#34;&gt;Notification&lt;/a&gt;, ... ]</i>,
        "<a href="#profile" title="Profile">Profile</a>" : <i>[ &lt;a href=&#34;profile.md&#34;&gt;Profile&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#email" title="Email">Email</a>" : <i>[ &lt;a href=&#34;email.md&#34;&gt;Email&lt;/a&gt;, ... ]</i>,
        "<a href="#webhook" title="Webhook">Webhook</a>" : <i>[ &lt;a href=&#34;webhook.md&#34;&gt;Webhook&lt;/a&gt;, ... ]</i>,
        "<a href="#capacity" title="Capacity">Capacity</a>" : <i>[ &lt;a href=&#34;capacity.md&#34;&gt;Capacity&lt;/a&gt;, ... ]</i>,
        "<a href="#fixeddate" title="FixedDate">FixedDate</a>" : <i>[ &lt;a href=&#34;fixeddate.md&#34;&gt;FixedDate&lt;/a&gt;, ... ]</i>,
        "<a href="#recurrence" title="Recurrence">Recurrence</a>" : <i>[ &lt;a href=&#34;recurrence.md&#34;&gt;Recurrence&lt;/a&gt;, ... ]</i>,
        "<a href="#rule" title="Rule">Rule</a>" : <i>[ &lt;a href=&#34;rule.md&#34;&gt;Rule&lt;/a&gt;, ... ]</i>,
        "<a href="#metrictrigger" title="MetricTrigger">MetricTrigger</a>" : <i>[ &lt;a href=&#34;metrictrigger.md&#34;&gt;MetricTrigger&lt;/a&gt;, ... ]</i>,
        "<a href="#scaleaction" title="ScaleAction">ScaleAction</a>" : <i>[ &lt;a href=&#34;scaleaction.md&#34;&gt;ScaleAction&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::MonitorAutoscaleSetting
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#targetresourceid" title="TargetResourceId">TargetResourceId</a>: <i>String</i>
    <a href="#notification" title="Notification">Notification</a>: <i>
      - &lt;a href=&#34;notification.md&#34;&gt;Notification&lt;/a&gt;</i>
    <a href="#profile" title="Profile">Profile</a>: <i>
      - &lt;a href=&#34;profile.md&#34;&gt;Profile&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#email" title="Email">Email</a>: <i>
      - &lt;a href=&#34;email.md&#34;&gt;Email&lt;/a&gt;</i>
    <a href="#webhook" title="Webhook">Webhook</a>: <i>
      - &lt;a href=&#34;webhook.md&#34;&gt;Webhook&lt;/a&gt;</i>
    <a href="#capacity" title="Capacity">Capacity</a>: <i>
      - &lt;a href=&#34;capacity.md&#34;&gt;Capacity&lt;/a&gt;</i>
    <a href="#fixeddate" title="FixedDate">FixedDate</a>: <i>
      - &lt;a href=&#34;fixeddate.md&#34;&gt;FixedDate&lt;/a&gt;</i>
    <a href="#recurrence" title="Recurrence">Recurrence</a>: <i>
      - &lt;a href=&#34;recurrence.md&#34;&gt;Recurrence&lt;/a&gt;</i>
    <a href="#rule" title="Rule">Rule</a>: <i>
      - &lt;a href=&#34;rule.md&#34;&gt;Rule&lt;/a&gt;</i>
    <a href="#metrictrigger" title="MetricTrigger">MetricTrigger</a>: <i>
      - &lt;a href=&#34;metrictrigger.md&#34;&gt;MetricTrigger&lt;/a&gt;</i>
    <a href="#scaleaction" title="ScaleAction">ScaleAction</a>: <i>
      - &lt;a href=&#34;scaleaction.md&#34;&gt;ScaleAction&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetResourceId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notification

_Required_: No

_Type_: List of &lt;a href=&#34;notification.md&#34;&gt;Notification&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Profile

_Required_: No

_Type_: List of &lt;a href=&#34;profile.md&#34;&gt;Profile&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

_Required_: No

_Type_: List of &lt;a href=&#34;email.md&#34;&gt;Email&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Webhook

_Required_: No

_Type_: List of &lt;a href=&#34;webhook.md&#34;&gt;Webhook&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Capacity

_Required_: No

_Type_: List of &lt;a href=&#34;capacity.md&#34;&gt;Capacity&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FixedDate

_Required_: No

_Type_: List of &lt;a href=&#34;fixeddate.md&#34;&gt;FixedDate&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Recurrence

_Required_: No

_Type_: List of &lt;a href=&#34;recurrence.md&#34;&gt;Recurrence&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No

_Type_: List of &lt;a href=&#34;rule.md&#34;&gt;Rule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricTrigger

_Required_: No

_Type_: List of &lt;a href=&#34;metrictrigger.md&#34;&gt;MetricTrigger&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleAction

_Required_: No

_Type_: List of &lt;a href=&#34;scaleaction.md&#34;&gt;ScaleAction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

