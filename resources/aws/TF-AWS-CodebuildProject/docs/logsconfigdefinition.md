# TF::AWS::CodebuildProject LogsConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cloudwatchlogs" title="CloudwatchLogs">CloudwatchLogs</a>" : <i>[ <a href="cloudwatchlogsdefinition.md">CloudwatchLogsDefinition</a>, ... ]</i>,
    "<a href="#s3logs" title="S3Logs">S3Logs</a>" : <i>[ <a href="s3logsdefinition.md">S3LogsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cloudwatchlogs" title="CloudwatchLogs">CloudwatchLogs</a>: <i>
      - <a href="cloudwatchlogsdefinition.md">CloudwatchLogsDefinition</a></i>
<a href="#s3logs" title="S3Logs">S3Logs</a>: <i>
      - <a href="s3logsdefinition.md">S3LogsDefinition</a></i>
</pre>

## Properties

#### CloudwatchLogs

_Required_: No

_Type_: List of <a href="cloudwatchlogsdefinition.md">CloudwatchLogsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3Logs

_Required_: No

_Type_: List of <a href="s3logsdefinition.md">S3LogsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

