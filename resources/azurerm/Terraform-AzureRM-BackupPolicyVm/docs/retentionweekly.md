# Terraform::AzureRM::BackupPolicyVm RetentionWeekly

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#count" title="Count">Count</a>" : <i>Double</i>,
    "<a href="#weekdays" title="Weekdays">Weekdays</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#count" title="Count">Count</a>: <i>Double</i>
<a href="#weekdays" title="Weekdays">Weekdays</a>: <i>
      - String</i>
</pre>

## Properties

#### Count

The number of weekly backups to keep. Must be between `1` and `9999`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weekdays

The weekday backups to retain. Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

