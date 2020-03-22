# Terraform::AWS::IotTopicRule

CloudFormation equivalent of aws_iot_topic_rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::IotTopicRule",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#sql" title="Sql">Sql</a>" : <i>String</i>,
        "<a href="#sqlversion" title="SqlVersion">SqlVersion</a>" : <i>String</i>,
        "<a href="#cloudwatchalarm" title="CloudwatchAlarm">CloudwatchAlarm</a>" : <i>[ <a href="cloudwatchalarm.md">CloudwatchAlarm</a>, ... ]</i>,
        "<a href="#cloudwatchmetric" title="CloudwatchMetric">CloudwatchMetric</a>" : <i>[ <a href="cloudwatchmetric.md">CloudwatchMetric</a>, ... ]</i>,
        "<a href="#dynamodb" title="Dynamodb">Dynamodb</a>" : <i>[ <a href="dynamodb.md">Dynamodb</a>, ... ]</i>,
        "<a href="#elasticsearch" title="Elasticsearch">Elasticsearch</a>" : <i>[ <a href="elasticsearch.md">Elasticsearch</a>, ... ]</i>,
        "<a href="#firehose" title="Firehose">Firehose</a>" : <i>[ <a href="firehose.md">Firehose</a>, ... ]</i>,
        "<a href="#kinesis" title="Kinesis">Kinesis</a>" : <i>[ <a href="kinesis.md">Kinesis</a>, ... ]</i>,
        "<a href="#lambda" title="Lambda">Lambda</a>" : <i>[ <a href="lambda.md">Lambda</a>, ... ]</i>,
        "<a href="#republish" title="Republish">Republish</a>" : <i>[ <a href="republish.md">Republish</a>, ... ]</i>,
        "<a href="#s3" title="S3">S3</a>" : <i>[ <a href="s3.md">S3</a>, ... ]</i>,
        "<a href="#sns" title="Sns">Sns</a>" : <i>[ <a href="sns.md">Sns</a>, ... ]</i>,
        "<a href="#sqs" title="Sqs">Sqs</a>" : <i>[ <a href="sqs.md">Sqs</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::IotTopicRule
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#sql" title="Sql">Sql</a>: <i>String</i>
    <a href="#sqlversion" title="SqlVersion">SqlVersion</a>: <i>String</i>
    <a href="#cloudwatchalarm" title="CloudwatchAlarm">CloudwatchAlarm</a>: <i>
      - <a href="cloudwatchalarm.md">CloudwatchAlarm</a></i>
    <a href="#cloudwatchmetric" title="CloudwatchMetric">CloudwatchMetric</a>: <i>
      - <a href="cloudwatchmetric.md">CloudwatchMetric</a></i>
    <a href="#dynamodb" title="Dynamodb">Dynamodb</a>: <i>
      - <a href="dynamodb.md">Dynamodb</a></i>
    <a href="#elasticsearch" title="Elasticsearch">Elasticsearch</a>: <i>
      - <a href="elasticsearch.md">Elasticsearch</a></i>
    <a href="#firehose" title="Firehose">Firehose</a>: <i>
      - <a href="firehose.md">Firehose</a></i>
    <a href="#kinesis" title="Kinesis">Kinesis</a>: <i>
      - <a href="kinesis.md">Kinesis</a></i>
    <a href="#lambda" title="Lambda">Lambda</a>: <i>
      - <a href="lambda.md">Lambda</a></i>
    <a href="#republish" title="Republish">Republish</a>: <i>
      - <a href="republish.md">Republish</a></i>
    <a href="#s3" title="S3">S3</a>: <i>
      - <a href="s3.md">S3</a></i>
    <a href="#sns" title="Sns">Sns</a>: <i>
      - <a href="sns.md">Sns</a></i>
    <a href="#sqs" title="Sqs">Sqs</a>: <i>
      - <a href="sqs.md">Sqs</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sql

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SqlVersion

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudwatchAlarm

_Required_: No

_Type_: List of <a href="cloudwatchalarm.md">CloudwatchAlarm</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudwatchMetric

_Required_: No

_Type_: List of <a href="cloudwatchmetric.md">CloudwatchMetric</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dynamodb

_Required_: No

_Type_: List of <a href="dynamodb.md">Dynamodb</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Elasticsearch

_Required_: No

_Type_: List of <a href="elasticsearch.md">Elasticsearch</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Firehose

_Required_: No

_Type_: List of <a href="firehose.md">Firehose</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Kinesis

_Required_: No

_Type_: List of <a href="kinesis.md">Kinesis</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lambda

_Required_: No

_Type_: List of <a href="lambda.md">Lambda</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Republish

_Required_: No

_Type_: List of <a href="republish.md">Republish</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3

_Required_: No

_Type_: List of <a href="s3.md">S3</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sns

_Required_: No

_Type_: List of <a href="sns.md">Sns</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sqs

_Required_: No

_Type_: List of <a href="sqs.md">Sqs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

