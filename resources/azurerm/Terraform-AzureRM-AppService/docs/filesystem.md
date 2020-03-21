# Terraform::AzureRM::AppService FileSystem

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#retentionindays" title="RetentionInDays">RetentionInDays</a>" : <i>Double</i>,
    "<a href="#retentioninmb" title="RetentionInMb">RetentionInMb</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#retentionindays" title="RetentionInDays">RetentionInDays</a>: <i>Double</i>
<a href="#retentioninmb" title="RetentionInMb">RetentionInMb</a>: <i>Double</i>
</pre>

## Properties

#### RetentionInDays

The number of days to retain logs for.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionInMb

The maximum size in megabytes that http log files can use before being removed.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

