# TF::AzureRM::BackupPolicyFileShare BackupDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#frequency" title="Frequency">Frequency</a>" : <i>String</i>,
    "<a href="#time" title="Time">Time</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#frequency" title="Frequency">Frequency</a>: <i>String</i>
<a href="#time" title="Time">Time</a>: <i>String</i>
</pre>

## Properties

#### Frequency

Sets the backup frequency. Currently, only `Daily` is supported.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Time

The time of day to perform the backup in 24-hour format. Times must be either on the hour or half hour (e.g. 12:00, 12:30, 13:00, etc.).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

