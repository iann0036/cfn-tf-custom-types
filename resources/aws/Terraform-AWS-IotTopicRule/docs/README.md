# Terraform::AWS::IotTopicRule

CloudFormation equivalent of aws_iot_topic_rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::IotTopicRule",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#arn" title="Arn">Arn</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#sql" title="Sql">Sql</a>" : <i>String</i>,
        "<a href="#sqlversion" title="SqlVersion">SqlVersion</a>" : <i>String</i>,
        "<a href="#cloudwatchalarm" title="CloudwatchAlarm">CloudwatchAlarm</a>" : <i>[ &lt;a href=&#34;cloudwatchalarm.md&#34;&gt;CloudwatchAlarm&lt;/a&gt;, ... ]</i>,
        "<a href="#cloudwatchmetric" title="CloudwatchMetric">CloudwatchMetric</a>" : <i>[ &lt;a href=&#34;cloudwatchmetric.md&#34;&gt;CloudwatchMetric&lt;/a&gt;, ... ]</i>,
        "<a href="#dynamodb" title="Dynamodb">Dynamodb</a>" : <i>[ &lt;a href=&#34;dynamodb.md&#34;&gt;Dynamodb&lt;/a&gt;, ... ]</i>,
        "<a href="#elasticsearch" title="Elasticsearch">Elasticsearch</a>" : <i>[ &lt;a href=&#34;elasticsearch.md&#34;&gt;Elasticsearch&lt;/a&gt;, ... ]</i>,
        "<a href="#firehose" title="Firehose">Firehose</a>" : <i>[ &lt;a href=&#34;firehose.md&#34;&gt;Firehose&lt;/a&gt;, ... ]</i>,
        "<a href="#kinesis" title="Kinesis">Kinesis</a>" : <i>[ &lt;a href=&#34;kinesis.md&#34;&gt;Kinesis&lt;/a&gt;, ... ]</i>,
        "<a href="#lambda" title="Lambda">Lambda</a>" : <i>[ &lt;a href=&#34;lambda.md&#34;&gt;Lambda&lt;/a&gt;, ... ]</i>,
        "<a href="#republish" title="Republish">Republish</a>" : <i>[ &lt;a href=&#34;republish.md&#34;&gt;Republish&lt;/a&gt;, ... ]</i>,
        "<a href="#s3" title="S3">S3</a>" : <i>[ &lt;a href=&#34;s3.md&#34;&gt;S3&lt;/a&gt;, ... ]</i>,
        "<a href="#sns" title="Sns">Sns</a>" : <i>[ &lt;a href=&#34;sns.md&#34;&gt;Sns&lt;/a&gt;, ... ]</i>,
        "<a href="#sqs" title="Sqs">Sqs</a>" : <i>[ &lt;a href=&#34;sqs.md&#34;&gt;Sqs&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::IotTopicRule
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#arn" title="Arn">Arn</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#sql" title="Sql">Sql</a>: <i>String</i>
    <a href="#sqlversion" title="SqlVersion">SqlVersion</a>: <i>String</i>
    <a href="#cloudwatchalarm" title="CloudwatchAlarm">CloudwatchAlarm</a>: <i>
      - &lt;a href=&#34;cloudwatchalarm.md&#34;&gt;CloudwatchAlarm&lt;/a&gt;</i>
    <a href="#cloudwatchmetric" title="CloudwatchMetric">CloudwatchMetric</a>: <i>
      - &lt;a href=&#34;cloudwatchmetric.md&#34;&gt;CloudwatchMetric&lt;/a&gt;</i>
    <a href="#dynamodb" title="Dynamodb">Dynamodb</a>: <i>
      - &lt;a href=&#34;dynamodb.md&#34;&gt;Dynamodb&lt;/a&gt;</i>
    <a href="#elasticsearch" title="Elasticsearch">Elasticsearch</a>: <i>
      - &lt;a href=&#34;elasticsearch.md&#34;&gt;Elasticsearch&lt;/a&gt;</i>
    <a href="#firehose" title="Firehose">Firehose</a>: <i>
      - &lt;a href=&#34;firehose.md&#34;&gt;Firehose&lt;/a&gt;</i>
    <a href="#kinesis" title="Kinesis">Kinesis</a>: <i>
      - &lt;a href=&#34;kinesis.md&#34;&gt;Kinesis&lt;/a&gt;</i>
    <a href="#lambda" title="Lambda">Lambda</a>: <i>
      - &lt;a href=&#34;lambda.md&#34;&gt;Lambda&lt;/a&gt;</i>
    <a href="#republish" title="Republish">Republish</a>: <i>
      - &lt;a href=&#34;republish.md&#34;&gt;Republish&lt;/a&gt;</i>
    <a href="#s3" title="S3">S3</a>: <i>
      - &lt;a href=&#34;s3.md&#34;&gt;S3&lt;/a&gt;</i>
    <a href="#sns" title="Sns">Sns</a>: <i>
      - &lt;a href=&#34;sns.md&#34;&gt;Sns&lt;/a&gt;</i>
    <a href="#sqs" title="Sqs">Sqs</a>: <i>
      - &lt;a href=&#34;sqs.md&#34;&gt;Sqs&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Arn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

_Type_: List of &lt;a href=&#34;cloudwatchalarm.md&#34;&gt;CloudwatchAlarm&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudwatchMetric

_Required_: No

_Type_: List of &lt;a href=&#34;cloudwatchmetric.md&#34;&gt;CloudwatchMetric&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dynamodb

_Required_: No

_Type_: List of &lt;a href=&#34;dynamodb.md&#34;&gt;Dynamodb&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Elasticsearch

_Required_: No

_Type_: List of &lt;a href=&#34;elasticsearch.md&#34;&gt;Elasticsearch&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Firehose

_Required_: No

_Type_: List of &lt;a href=&#34;firehose.md&#34;&gt;Firehose&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Kinesis

_Required_: No

_Type_: List of &lt;a href=&#34;kinesis.md&#34;&gt;Kinesis&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lambda

_Required_: No

_Type_: List of &lt;a href=&#34;lambda.md&#34;&gt;Lambda&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Republish

_Required_: No

_Type_: List of &lt;a href=&#34;republish.md&#34;&gt;Republish&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3

_Required_: No

_Type_: List of &lt;a href=&#34;s3.md&#34;&gt;S3&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sns

_Required_: No

_Type_: List of &lt;a href=&#34;sns.md&#34;&gt;Sns&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sqs

_Required_: No

_Type_: List of &lt;a href=&#34;sqs.md&#34;&gt;Sqs&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the &lt;code&gt;Arn&lt;/code&gt; value.

