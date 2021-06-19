# TF::AWS::Elb AccessLogsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
    "<a href="#bucketprefix" title="BucketPrefix">BucketPrefix</a>" : <i>String</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#interval" title="Interval">Interval</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
<a href="#bucketprefix" title="BucketPrefix">BucketPrefix</a>: <i>String</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#interval" title="Interval">Interval</a>: <i>Double</i>
</pre>

## Properties

#### Bucket

The S3 bucket name to store the logs in.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BucketPrefix

The S3 bucket prefix. Logs are stored in the root if not configured.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Boolean to enable / disable `access_logs`. Default is `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interval

The publishing interval in minutes. Default: 60 minutes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

