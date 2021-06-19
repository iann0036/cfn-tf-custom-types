# TF::AzureRM::CosmosdbAccount BackupDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#intervalinminutes" title="IntervalInMinutes">IntervalInMinutes</a>" : <i>Double</i>,
    "<a href="#retentioninhours" title="RetentionInHours">RetentionInHours</a>" : <i>Double</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#intervalinminutes" title="IntervalInMinutes">IntervalInMinutes</a>: <i>Double</i>
<a href="#retentioninhours" title="RetentionInHours">RetentionInHours</a>: <i>Double</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### IntervalInMinutes

The interval in minutes between two backups. This is configurable only when `type` is `Periodic`. Possible values are between 60 and 1440.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionInHours

The time in hours that each backup is retained. This is configurable only when `type` is `Periodic`. Possible values are between 8 and 720.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of the `backup`. Possible values are `Continuous` and `Periodic`. Defaults to `Periodic`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

