# TF::PrismaCloud::AlertRule

Manage an alert rule.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::PrismaCloud::AlertRule",
    "Properties" : {
        "<a href="#allowautoremediate" title="AllowAutoRemediate">AllowAutoRemediate</a>" : <i>Boolean</i>,
        "<a href="#delaynotificationms" title="DelayNotificationMs">DelayNotificationMs</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#excludedpolicies" title="ExcludedPolicies">ExcludedPolicies</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notifyondismissed" title="NotifyOnDismissed">NotifyOnDismissed</a>" : <i>Boolean</i>,
        "<a href="#notifyonopen" title="NotifyOnOpen">NotifyOnOpen</a>" : <i>Boolean</i>,
        "<a href="#notifyonresolved" title="NotifyOnResolved">NotifyOnResolved</a>" : <i>Boolean</i>,
        "<a href="#notifyonsnoozed" title="NotifyOnSnoozed">NotifyOnSnoozed</a>" : <i>Boolean</i>,
        "<a href="#policies" title="Policies">Policies</a>" : <i>[ String, ... ]</i>,
        "<a href="#policylabels" title="PolicyLabels">PolicyLabels</a>" : <i>[ String, ... ]</i>,
        "<a href="#scanall" title="ScanAll">ScanAll</a>" : <i>Boolean</i>,
        "<a href="#notificationconfig" title="NotificationConfig">NotificationConfig</a>" : <i>[ <a href="notificationconfigdefinition.md">NotificationConfigDefinition</a>, ... ]</i>,
        "<a href="#target" title="Target">Target</a>" : <i>[ <a href="targetdefinition.md">TargetDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::PrismaCloud::AlertRule
Properties:
    <a href="#allowautoremediate" title="AllowAutoRemediate">AllowAutoRemediate</a>: <i>Boolean</i>
    <a href="#delaynotificationms" title="DelayNotificationMs">DelayNotificationMs</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#excludedpolicies" title="ExcludedPolicies">ExcludedPolicies</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notifyondismissed" title="NotifyOnDismissed">NotifyOnDismissed</a>: <i>Boolean</i>
    <a href="#notifyonopen" title="NotifyOnOpen">NotifyOnOpen</a>: <i>Boolean</i>
    <a href="#notifyonresolved" title="NotifyOnResolved">NotifyOnResolved</a>: <i>Boolean</i>
    <a href="#notifyonsnoozed" title="NotifyOnSnoozed">NotifyOnSnoozed</a>: <i>Boolean</i>
    <a href="#policies" title="Policies">Policies</a>: <i>
      - String</i>
    <a href="#policylabels" title="PolicyLabels">PolicyLabels</a>: <i>
      - String</i>
    <a href="#scanall" title="ScanAll">ScanAll</a>: <i>Boolean</i>
    <a href="#notificationconfig" title="NotificationConfig">NotificationConfig</a>: <i>
      - <a href="notificationconfigdefinition.md">NotificationConfigDefinition</a></i>
    <a href="#target" title="Target">Target</a>: <i>
      - <a href="targetdefinition.md">TargetDefinition</a></i>
</pre>

## Properties

#### AllowAutoRemediate

Allow auto-remediation.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DelayNotificationMs

Delay notifications by the specified miliseconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Enabled (default: `true`).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludedPolicies

List of policies to exclude from scan.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Rule/Scan name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyOnDismissed

Include dismissed alerts in notification.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyOnOpen

Include open alerts in notification (default: `true`).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyOnResolved

Include resolved alerts in notification.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyOnSnoozed

Include snoozed alerts in notification.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policies

List of specific policies to scan.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyLabels

List of policy labels.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScanAll

Scan all policies.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationConfig

_Required_: No

_Type_: List of <a href="notificationconfigdefinition.md">NotificationConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Target

_Required_: No

_Type_: List of <a href="targetdefinition.md">TargetDefinition</a>

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

#### LastModifiedBy

Returns the <code>LastModifiedBy</code> value.

#### LastModifiedOn

Returns the <code>LastModifiedOn</code> value.

#### NotificationChannels

Returns the <code>NotificationChannels</code> value.

#### OpenAlertsCount

Returns the <code>OpenAlertsCount</code> value.

#### Owner

Returns the <code>Owner</code> value.

#### PolicyScanConfigId

Returns the <code>PolicyScanConfigId</code> value.

#### ReadOnly

Returns the <code>ReadOnly</code> value.

