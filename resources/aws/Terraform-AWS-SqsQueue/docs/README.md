# Terraform::AWS::SqsQueue

CloudFormation equivalent of aws_sqs_queue

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::SqsQueue",
    "Properties" : {
        "<a href="#contentbaseddeduplication" title="ContentBasedDeduplication">ContentBasedDeduplication</a>" : <i>Boolean</i>,
        "<a href="#delayseconds" title="DelaySeconds">DelaySeconds</a>" : <i>Double</i>,
        "<a href="#fifoqueue" title="FifoQueue">FifoQueue</a>" : <i>Boolean</i>,
        "<a href="#kmsdatakeyreuseperiodseconds" title="KmsDataKeyReusePeriodSeconds">KmsDataKeyReusePeriodSeconds</a>" : <i>Double</i>,
        "<a href="#kmsmasterkeyid" title="KmsMasterKeyId">KmsMasterKeyId</a>" : <i>String</i>,
        "<a href="#maxmessagesize" title="MaxMessageSize">MaxMessageSize</a>" : <i>Double</i>,
        "<a href="#messageretentionseconds" title="MessageRetentionSeconds">MessageRetentionSeconds</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nameprefix" title="NamePrefix">NamePrefix</a>" : <i>String</i>,
        "<a href="#policy" title="Policy">Policy</a>" : <i>String</i>,
        "<a href="#receivewaittimeseconds" title="ReceiveWaitTimeSeconds">ReceiveWaitTimeSeconds</a>" : <i>Double</i>,
        "<a href="#redrivepolicy" title="RedrivePolicy">RedrivePolicy</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#visibilitytimeoutseconds" title="VisibilityTimeoutSeconds">VisibilityTimeoutSeconds</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::SqsQueue
Properties:
    <a href="#contentbaseddeduplication" title="ContentBasedDeduplication">ContentBasedDeduplication</a>: <i>Boolean</i>
    <a href="#delayseconds" title="DelaySeconds">DelaySeconds</a>: <i>Double</i>
    <a href="#fifoqueue" title="FifoQueue">FifoQueue</a>: <i>Boolean</i>
    <a href="#kmsdatakeyreuseperiodseconds" title="KmsDataKeyReusePeriodSeconds">KmsDataKeyReusePeriodSeconds</a>: <i>Double</i>
    <a href="#kmsmasterkeyid" title="KmsMasterKeyId">KmsMasterKeyId</a>: <i>String</i>
    <a href="#maxmessagesize" title="MaxMessageSize">MaxMessageSize</a>: <i>Double</i>
    <a href="#messageretentionseconds" title="MessageRetentionSeconds">MessageRetentionSeconds</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nameprefix" title="NamePrefix">NamePrefix</a>: <i>String</i>
    <a href="#policy" title="Policy">Policy</a>: <i>String</i>
    <a href="#receivewaittimeseconds" title="ReceiveWaitTimeSeconds">ReceiveWaitTimeSeconds</a>: <i>Double</i>
    <a href="#redrivepolicy" title="RedrivePolicy">RedrivePolicy</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#visibilitytimeoutseconds" title="VisibilityTimeoutSeconds">VisibilityTimeoutSeconds</a>: <i>Double</i>
</pre>

## Properties

#### ContentBasedDeduplication

Enables content-based deduplication for FIFO queues. For more information, see the [related documentation](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html#FIFO-queues-exactly-once-processing).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DelaySeconds

The time in seconds that the delivery of all messages in the queue will be delayed. An integer from 0 to 900 (15 minutes). The default for this attribute is 0 seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FifoQueue

Boolean designating a FIFO queue. If not set, it defaults to `false` making it standard.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsDataKeyReusePeriodSeconds

The length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. An integer representing seconds, between 60 seconds (1 minute) and 86,400 seconds (24 hours). The default is 300 (5 minutes).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsMasterKeyId

The ID of an AWS-managed customer master key (CMK) for Amazon SQS or a custom CMK. For more information, see [Key Terms](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-sse-key-terms).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxMessageSize

The limit of how many bytes a message can contain before Amazon SQS rejects it. An integer from 1024 bytes (1 KiB) up to 262144 bytes (256 KiB). The default for this attribute is 262144 (256 KiB).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MessageRetentionSeconds

The number of seconds Amazon SQS retains a message. Integer representing seconds, from 60 (1 minute) to 1209600 (14 days). The default for this attribute is 345600 (4 days).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

This is the human-readable name of the queue. If omitted, Terraform will assign a random name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamePrefix

Creates a unique name beginning with the specified prefix. Conflicts with `name`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policy

The JSON policy for the SQS queue. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://learn.hashicorp.com/terraform/aws/iam-policy).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReceiveWaitTimeSeconds

The time for which a ReceiveMessage call will wait for a message to arrive (long polling) before returning. An integer from 0 to 20 (seconds). The default for this attribute is 0, meaning that the call will return immediately.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedrivePolicy

The JSON policy to set up the Dead Letter Queue, see [AWS docs](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/SQSDeadLetterQueue.html). **Note:** when specifying `maxReceiveCount`, you must specify it as an integer (`5`), and not a string (`"5"`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the queue.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VisibilityTimeoutSeconds

The visibility timeout for the queue. An integer from 0 to 43200 (12 hours). The default for this attribute is 30. For more information about visibility timeout, see [AWS docs](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/AboutVT.html).

_Required_: No

_Type_: Double

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

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

