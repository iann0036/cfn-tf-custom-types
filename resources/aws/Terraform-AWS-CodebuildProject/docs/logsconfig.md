# Terraform::AWS::CodebuildProject LogsConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cloudwatchlogs" title="CloudwatchLogs">CloudwatchLogs</a>" : <i>[ &lt;a href=&#34;logsconfig-cloudwatchlogs.md&#34;&gt;CloudwatchLogs&lt;/a&gt;, ... ]</i>,
    "<a href="#s3logs" title="S3Logs">S3Logs</a>" : <i>[ &lt;a href=&#34;logsconfig-s3logs.md&#34;&gt;S3Logs&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cloudwatchlogs" title="CloudwatchLogs">CloudwatchLogs</a>: <i>
      - &lt;a href=&#34;logsconfig-cloudwatchlogs.md&#34;&gt;CloudwatchLogs&lt;/a&gt;</i>
<a href="#s3logs" title="S3Logs">S3Logs</a>: <i>
      - &lt;a href=&#34;logsconfig-s3logs.md&#34;&gt;S3Logs&lt;/a&gt;</i>
</pre>

## Properties

#### CloudwatchLogs

_Required_: No
_Type_: List of &lt;a href=&#34;logsconfig-cloudwatchlogs.md&#34;&gt;CloudwatchLogs&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3Logs

_Required_: No
_Type_: List of &lt;a href=&#34;logsconfig-s3logs.md&#34;&gt;S3Logs&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

