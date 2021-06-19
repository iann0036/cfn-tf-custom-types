# TF::AWS::IotTopicRule ErrorActionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cloudwatchalarm" title="CloudwatchAlarm">CloudwatchAlarm</a>" : <i>[ <a href="cloudwatchalarmdefinition.md">CloudwatchAlarmDefinition</a>, ... ]</i>,
    "<a href="#cloudwatchmetric" title="CloudwatchMetric">CloudwatchMetric</a>" : <i>[ <a href="cloudwatchmetricdefinition.md">CloudwatchMetricDefinition</a>, ... ]</i>,
    "<a href="#dynamodb" title="Dynamodb">Dynamodb</a>" : <i>[ <a href="dynamodbdefinition.md">DynamodbDefinition</a>, ... ]</i>,
    "<a href="#dynamodbv2" title="Dynamodbv2">Dynamodbv2</a>" : <i>[ <a href="dynamodbv2definition.md">Dynamodbv2Definition</a>, ... ]</i>,
    "<a href="#elasticsearch" title="Elasticsearch">Elasticsearch</a>" : <i>[ <a href="elasticsearchdefinition.md">ElasticsearchDefinition</a>, ... ]</i>,
    "<a href="#firehose" title="Firehose">Firehose</a>" : <i>[ <a href="firehosedefinition.md">FirehoseDefinition</a>, ... ]</i>,
    "<a href="#iotanalytics" title="IotAnalytics">IotAnalytics</a>" : <i>[ <a href="iotanalyticsdefinition.md">IotAnalyticsDefinition</a>, ... ]</i>,
    "<a href="#iotevents" title="IotEvents">IotEvents</a>" : <i>[ <a href="ioteventsdefinition.md">IotEventsDefinition</a>, ... ]</i>,
    "<a href="#kinesis" title="Kinesis">Kinesis</a>" : <i>[ <a href="kinesisdefinition.md">KinesisDefinition</a>, ... ]</i>,
    "<a href="#lambda" title="Lambda">Lambda</a>" : <i>[ <a href="lambdadefinition.md">LambdaDefinition</a>, ... ]</i>,
    "<a href="#republish" title="Republish">Republish</a>" : <i>[ <a href="republishdefinition.md">RepublishDefinition</a>, ... ]</i>,
    "<a href="#s3" title="S3">S3</a>" : <i>[ <a href="s3definition.md">S3Definition</a>, ... ]</i>,
    "<a href="#sns" title="Sns">Sns</a>" : <i>[ <a href="snsdefinition.md">SnsDefinition</a>, ... ]</i>,
    "<a href="#sqs" title="Sqs">Sqs</a>" : <i>[ <a href="sqsdefinition.md">SqsDefinition</a>, ... ]</i>,
    "<a href="#stepfunctions" title="StepFunctions">StepFunctions</a>" : <i>[ <a href="stepfunctionsdefinition.md">StepFunctionsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cloudwatchalarm" title="CloudwatchAlarm">CloudwatchAlarm</a>: <i>
      - <a href="cloudwatchalarmdefinition.md">CloudwatchAlarmDefinition</a></i>
<a href="#cloudwatchmetric" title="CloudwatchMetric">CloudwatchMetric</a>: <i>
      - <a href="cloudwatchmetricdefinition.md">CloudwatchMetricDefinition</a></i>
<a href="#dynamodb" title="Dynamodb">Dynamodb</a>: <i>
      - <a href="dynamodbdefinition.md">DynamodbDefinition</a></i>
<a href="#dynamodbv2" title="Dynamodbv2">Dynamodbv2</a>: <i>
      - <a href="dynamodbv2definition.md">Dynamodbv2Definition</a></i>
<a href="#elasticsearch" title="Elasticsearch">Elasticsearch</a>: <i>
      - <a href="elasticsearchdefinition.md">ElasticsearchDefinition</a></i>
<a href="#firehose" title="Firehose">Firehose</a>: <i>
      - <a href="firehosedefinition.md">FirehoseDefinition</a></i>
<a href="#iotanalytics" title="IotAnalytics">IotAnalytics</a>: <i>
      - <a href="iotanalyticsdefinition.md">IotAnalyticsDefinition</a></i>
<a href="#iotevents" title="IotEvents">IotEvents</a>: <i>
      - <a href="ioteventsdefinition.md">IotEventsDefinition</a></i>
<a href="#kinesis" title="Kinesis">Kinesis</a>: <i>
      - <a href="kinesisdefinition.md">KinesisDefinition</a></i>
<a href="#lambda" title="Lambda">Lambda</a>: <i>
      - <a href="lambdadefinition.md">LambdaDefinition</a></i>
<a href="#republish" title="Republish">Republish</a>: <i>
      - <a href="republishdefinition.md">RepublishDefinition</a></i>
<a href="#s3" title="S3">S3</a>: <i>
      - <a href="s3definition.md">S3Definition</a></i>
<a href="#sns" title="Sns">Sns</a>: <i>
      - <a href="snsdefinition.md">SnsDefinition</a></i>
<a href="#sqs" title="Sqs">Sqs</a>: <i>
      - <a href="sqsdefinition.md">SqsDefinition</a></i>
<a href="#stepfunctions" title="StepFunctions">StepFunctions</a>: <i>
      - <a href="stepfunctionsdefinition.md">StepFunctionsDefinition</a></i>
</pre>

## Properties

#### CloudwatchAlarm

_Required_: No

_Type_: List of <a href="cloudwatchalarmdefinition.md">CloudwatchAlarmDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudwatchMetric

_Required_: No

_Type_: List of <a href="cloudwatchmetricdefinition.md">CloudwatchMetricDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dynamodb

_Required_: No

_Type_: List of <a href="dynamodbdefinition.md">DynamodbDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dynamodbv2

_Required_: No

_Type_: List of <a href="dynamodbv2definition.md">Dynamodbv2Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Elasticsearch

_Required_: No

_Type_: List of <a href="elasticsearchdefinition.md">ElasticsearchDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Firehose

_Required_: No

_Type_: List of <a href="firehosedefinition.md">FirehoseDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IotAnalytics

_Required_: No

_Type_: List of <a href="iotanalyticsdefinition.md">IotAnalyticsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IotEvents

_Required_: No

_Type_: List of <a href="ioteventsdefinition.md">IotEventsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Kinesis

_Required_: No

_Type_: List of <a href="kinesisdefinition.md">KinesisDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lambda

_Required_: No

_Type_: List of <a href="lambdadefinition.md">LambdaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Republish

_Required_: No

_Type_: List of <a href="republishdefinition.md">RepublishDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3

_Required_: No

_Type_: List of <a href="s3definition.md">S3Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sns

_Required_: No

_Type_: List of <a href="snsdefinition.md">SnsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sqs

_Required_: No

_Type_: List of <a href="sqsdefinition.md">SqsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StepFunctions

_Required_: No

_Type_: List of <a href="stepfunctionsdefinition.md">StepFunctionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

