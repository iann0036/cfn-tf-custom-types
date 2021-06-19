# TF::AWS::MskCluster BrokerLogsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cloudwatchlogs" title="CloudwatchLogs">CloudwatchLogs</a>" : <i>[ <a href="cloudwatchlogsdefinition.md">CloudwatchLogsDefinition</a>, ... ]</i>,
    "<a href="#firehose" title="Firehose">Firehose</a>" : <i>[ <a href="firehosedefinition.md">FirehoseDefinition</a>, ... ]</i>,
    "<a href="#s3" title="S3">S3</a>" : <i>[ <a href="s3definition.md">S3Definition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cloudwatchlogs" title="CloudwatchLogs">CloudwatchLogs</a>: <i>
      - <a href="cloudwatchlogsdefinition.md">CloudwatchLogsDefinition</a></i>
<a href="#firehose" title="Firehose">Firehose</a>: <i>
      - <a href="firehosedefinition.md">FirehoseDefinition</a></i>
<a href="#s3" title="S3">S3</a>: <i>
      - <a href="s3definition.md">S3Definition</a></i>
</pre>

## Properties

#### CloudwatchLogs

_Required_: No

_Type_: List of <a href="cloudwatchlogsdefinition.md">CloudwatchLogsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Firehose

_Required_: No

_Type_: List of <a href="firehosedefinition.md">FirehoseDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3

_Required_: No

_Type_: List of <a href="s3definition.md">S3Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

