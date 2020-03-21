# Terraform::FlexibleEngine::CsbsBackupPolicyV1 ScheduledOperation

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#maxbackups" title="MaxBackups">MaxBackups</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#operationtype" title="OperationType">OperationType</a>" : <i>String</i>,
    "<a href="#permanent" title="Permanent">Permanent</a>" : <i>Boolean</i>,
    "<a href="#retentiondurationdays" title="RetentionDurationDays">RetentionDurationDays</a>" : <i>Double</i>,
    "<a href="#triggerpattern" title="TriggerPattern">TriggerPattern</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#maxbackups" title="MaxBackups">MaxBackups</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#operationtype" title="OperationType">OperationType</a>: <i>String</i>
<a href="#permanent" title="Permanent">Permanent</a>: <i>Boolean</i>
<a href="#retentiondurationdays" title="RetentionDurationDays">RetentionDurationDays</a>: <i>Double</i>
<a href="#triggerpattern" title="TriggerPattern">TriggerPattern</a>: <i>String</i>
</pre>

## Properties

#### Description

Specifies Scheduling period description.The value consists of 0 to 255 characters and must not contain a greater-than sign (>) or less-than sign (<).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Specifies whether the scheduling period is enabled. Default value is **true**.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxBackups

Specifies maximum number of backups that can be automatically created for a backup object.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies Scheduling period name.The value consists of 1 to 255 characters and can contain only letters, digits, underscores (_), and hyphens (-).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OperationType

Specifies Operation type, which can be backup.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Permanent

Specifies whether backups are permanently retained.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionDurationDays

Specifies duration of retaining a backup, in days.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TriggerPattern

Specifies Scheduling policy of the scheduler.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

