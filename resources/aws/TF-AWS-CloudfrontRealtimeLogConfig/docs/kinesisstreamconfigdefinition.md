# TF::AWS::CloudfrontRealtimeLogConfig KinesisStreamConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#rolearn" title="RoleArn">RoleArn</a>" : <i>String</i>,
    "<a href="#streamarn" title="StreamArn">StreamArn</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#rolearn" title="RoleArn">RoleArn</a>: <i>String</i>
<a href="#streamarn" title="StreamArn">StreamArn</a>: <i>String</i>
</pre>

## Properties

#### RoleArn

The ARN of an [IAM role](iam_role.html) that CloudFront can use to send real-time log data to the Kinesis data stream.
See the [AWS documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html#understand-real-time-log-config-iam-role) for more information.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StreamArn

The ARN of the [Kinesis data stream](kinesis_stream.html).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

