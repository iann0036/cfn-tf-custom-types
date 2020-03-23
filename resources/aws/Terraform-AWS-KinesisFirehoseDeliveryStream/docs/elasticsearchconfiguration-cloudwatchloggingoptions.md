# Terraform::AWS::KinesisFirehoseDeliveryStream ElasticsearchConfiguration CloudwatchLoggingOptions

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#loggroupname" title="LogGroupName">LogGroupName</a>" : <i>String</i>,
    "<a href="#logstreamname" title="LogStreamName">LogStreamName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#loggroupname" title="LogGroupName">LogGroupName</a>: <i>String</i>
<a href="#logstreamname" title="LogStreamName">LogStreamName</a>: <i>String</i>
</pre>

## Properties

#### Enabled

Enables or disables the logging. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogGroupName

The CloudWatch group name for logging. This value is required if `enabled` is true.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogStreamName

The CloudWatch log stream name for logging. This value is required if `enabled` is true.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

