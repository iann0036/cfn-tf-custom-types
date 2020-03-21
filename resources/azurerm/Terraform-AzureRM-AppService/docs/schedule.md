# Terraform::AzureRM::AppService Schedule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#frequencyinterval" title="FrequencyInterval">FrequencyInterval</a>" : <i>Double</i>,
    "<a href="#frequencyunit" title="FrequencyUnit">FrequencyUnit</a>" : <i>String</i>,
    "<a href="#keepatleastonebackup" title="KeepAtLeastOneBackup">KeepAtLeastOneBackup</a>" : <i>Boolean</i>,
    "<a href="#retentionperiodindays" title="RetentionPeriodInDays">RetentionPeriodInDays</a>" : <i>Double</i>,
    "<a href="#starttime" title="StartTime">StartTime</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#frequencyinterval" title="FrequencyInterval">FrequencyInterval</a>: <i>Double</i>
<a href="#frequencyunit" title="FrequencyUnit">FrequencyUnit</a>: <i>String</i>
<a href="#keepatleastonebackup" title="KeepAtLeastOneBackup">KeepAtLeastOneBackup</a>: <i>Boolean</i>
<a href="#retentionperiodindays" title="RetentionPeriodInDays">RetentionPeriodInDays</a>: <i>Double</i>
<a href="#starttime" title="StartTime">StartTime</a>: <i>String</i>
</pre>

## Properties

#### FrequencyInterval

Sets how often the backup should be executed.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrequencyUnit

Sets the unit of time for how often the backup should be executed. Possible values are `Day` or `Hour`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepAtLeastOneBackup

Should at least one backup always be kept in the Storage Account by the Retention Policy, regardless of how old it is?.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionPeriodInDays

Specifies the number of days after which Backups should be deleted.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTime

Sets when the schedule should start working.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

