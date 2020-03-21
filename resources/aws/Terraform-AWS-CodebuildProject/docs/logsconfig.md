# Terraform::AWS::CodebuildProject LogsConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cloudwatchlogs" title="CloudwatchLogs">CloudwatchLogs</a>" : <i>[ <a href="logsconfig-cloudwatchlogs.md">CloudwatchLogs</a>, ... ]</i>,
    "<a href="#s3logs" title="S3Logs">S3Logs</a>" : <i>[ <a href="logsconfig-s3logs.md">S3Logs</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cloudwatchlogs" title="CloudwatchLogs">CloudwatchLogs</a>: <i>
      - <a href="logsconfig-cloudwatchlogs.md">CloudwatchLogs</a></i>
<a href="#s3logs" title="S3Logs">S3Logs</a>: <i>
      - <a href="logsconfig-s3logs.md">S3Logs</a></i>
</pre>

## Properties

#### CloudwatchLogs

_Required_: No

_Type_: List of <a href="logsconfig-cloudwatchlogs.md">CloudwatchLogs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3Logs

_Required_: No

_Type_: List of <a href="logsconfig-s3logs.md">S3Logs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

