# Terraform::AWS::S3BucketNotification

CloudFormation equivalent of aws_s3_bucket_notification

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::S3BucketNotification",
    "Properties" : {
        "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
        "<a href="#lambdafunction" title="LambdaFunction">LambdaFunction</a>" : <i>[ <a href="lambdafunction.md">LambdaFunction</a>, ... ]</i>,
        "<a href="#queue" title="Queue">Queue</a>" : <i>[ <a href="queue.md">Queue</a>, ... ]</i>,
        "<a href="#topic" title="Topic">Topic</a>" : <i>[ <a href="topic.md">Topic</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::S3BucketNotification
Properties:
    <a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
    <a href="#lambdafunction" title="LambdaFunction">LambdaFunction</a>: <i>
      - <a href="lambdafunction.md">LambdaFunction</a></i>
    <a href="#queue" title="Queue">Queue</a>: <i>
      - <a href="queue.md">Queue</a></i>
    <a href="#topic" title="Topic">Topic</a>: <i>
      - <a href="topic.md">Topic</a></i>
</pre>

## Properties

#### Bucket

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LambdaFunction

_Required_: No

_Type_: List of <a href="lambdafunction.md">LambdaFunction</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Queue

_Required_: No

_Type_: List of <a href="queue.md">Queue</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Topic

_Required_: No

_Type_: List of <a href="topic.md">Topic</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

