# TF::AWS::S3Bucket LoggingDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#targetbucket" title="TargetBucket">TargetBucket</a>" : <i>String</i>,
    "<a href="#targetprefix" title="TargetPrefix">TargetPrefix</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#targetbucket" title="TargetBucket">TargetBucket</a>: <i>String</i>
<a href="#targetprefix" title="TargetPrefix">TargetPrefix</a>: <i>String</i>
</pre>

## Properties

#### TargetBucket

The name of the bucket that will receive the log objects.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetPrefix

To specify a key prefix for log objects.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

