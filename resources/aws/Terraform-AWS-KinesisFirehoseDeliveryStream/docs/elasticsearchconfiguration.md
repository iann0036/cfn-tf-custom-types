# Terraform::AWS::KinesisFirehoseDeliveryStream ElasticsearchConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bufferinginterval" title="BufferingInterval">BufferingInterval</a>" : <i>Double</i>,
    "<a href="#bufferingsize" title="BufferingSize">BufferingSize</a>" : <i>Double</i>,
    "<a href="#domainarn" title="DomainArn">DomainArn</a>" : <i>String</i>,
    "<a href="#indexname" title="IndexName">IndexName</a>" : <i>String</i>,
    "<a href="#indexrotationperiod" title="IndexRotationPeriod">IndexRotationPeriod</a>" : <i>String</i>,
    "<a href="#retryduration" title="RetryDuration">RetryDuration</a>" : <i>Double</i>,
    "<a href="#rolearn" title="RoleArn">RoleArn</a>" : <i>String</i>,
    "<a href="#s3backupmode" title="S3BackupMode">S3BackupMode</a>" : <i>String</i>,
    "<a href="#typename" title="TypeName">TypeName</a>" : <i>String</i>,
    "<a href="#cloudwatchloggingoptions" title="CloudwatchLoggingOptions">CloudwatchLoggingOptions</a>" : <i>[ <a href="elasticsearchconfiguration-cloudwatchloggingoptions.md">CloudwatchLoggingOptions</a>, ... ]</i>,
    "<a href="#processingconfiguration" title="ProcessingConfiguration">ProcessingConfiguration</a>" : <i>[ <a href="elasticsearchconfiguration-processingconfiguration.md">ProcessingConfiguration</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#bufferinginterval" title="BufferingInterval">BufferingInterval</a>: <i>Double</i>
<a href="#bufferingsize" title="BufferingSize">BufferingSize</a>: <i>Double</i>
<a href="#domainarn" title="DomainArn">DomainArn</a>: <i>String</i>
<a href="#indexname" title="IndexName">IndexName</a>: <i>String</i>
<a href="#indexrotationperiod" title="IndexRotationPeriod">IndexRotationPeriod</a>: <i>String</i>
<a href="#retryduration" title="RetryDuration">RetryDuration</a>: <i>Double</i>
<a href="#rolearn" title="RoleArn">RoleArn</a>: <i>String</i>
<a href="#s3backupmode" title="S3BackupMode">S3BackupMode</a>: <i>String</i>
<a href="#typename" title="TypeName">TypeName</a>: <i>String</i>
<a href="#cloudwatchloggingoptions" title="CloudwatchLoggingOptions">CloudwatchLoggingOptions</a>: <i>
      - <a href="elasticsearchconfiguration-cloudwatchloggingoptions.md">CloudwatchLoggingOptions</a></i>
<a href="#processingconfiguration" title="ProcessingConfiguration">ProcessingConfiguration</a>: <i>
      - <a href="elasticsearchconfiguration-processingconfiguration.md">ProcessingConfiguration</a></i>
</pre>

## Properties

#### BufferingInterval

Buffer incoming data for the specified period of time, in seconds between 60 to 900, before delivering it to the destination.  The default value is 300s.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BufferingSize

Buffer incoming data to the specified size, in MBs between 1 to 100, before delivering it to the destination.  The default value is 5MB.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainArn

The ARN of the Amazon ES domain.  The IAM role must have permission for `DescribeElasticsearchDomain`, `DescribeElasticsearchDomains`, and `DescribeElasticsearchDomainConfig` after assuming `RoleARN`.  The pattern needs to be `arn:.*`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IndexName

The Elasticsearch index name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IndexRotationPeriod

The Elasticsearch index rotation period.  Index rotation appends a timestamp to the IndexName to facilitate expiration of old data.  Valid values are `NoRotation`, `OneHour`, `OneDay`, `OneWeek`, and `OneMonth`.  The default value is `OneDay`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryDuration

After an initial failure to deliver to Splunk, the total amount of time, in seconds between 0 to 7200, during which Firehose re-attempts delivery (including the first attempt).  After this time has elapsed, the failed documents are written to Amazon S3.  The default value is 300s.  There will be no retry if the value is 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleArn

The ARN of the IAM role to be assumed by Firehose for calling the Amazon ES Configuration API and for indexing documents.  The pattern needs to be `arn:.*`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3BackupMode

Defines how documents should be delivered to Amazon S3.  Valid values are `FailedEventsOnly` and `AllEvents`.  Default value is `FailedEventsOnly`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TypeName

The Elasticsearch type name with maximum length of 100 characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudwatchLoggingOptions

_Required_: No

_Type_: List of <a href="elasticsearchconfiguration-cloudwatchloggingoptions.md">CloudwatchLoggingOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessingConfiguration

_Required_: No

_Type_: List of <a href="elasticsearchconfiguration-processingconfiguration.md">ProcessingConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

