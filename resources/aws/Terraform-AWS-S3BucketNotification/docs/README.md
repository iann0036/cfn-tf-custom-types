# Terraform::AWS::S3BucketNotification

CloudFormation equivalent of aws_s3_bucket_notification

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::S3BucketNotification",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
        "<a href="#lambdafunction" title="LambdaFunction">LambdaFunction</a>" : <i>[ &lt;a href=&#34;lambdafunction.md&#34;&gt;LambdaFunction&lt;/a&gt;, ... ]</i>,
        "<a href="#queue" title="Queue">Queue</a>" : <i>[ &lt;a href=&#34;queue.md&#34;&gt;Queue&lt;/a&gt;, ... ]</i>,
        "<a href="#topic" title="Topic">Topic</a>" : <i>[ &lt;a href=&#34;topic.md&#34;&gt;Topic&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::S3BucketNotification
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
    <a href="#lambdafunction" title="LambdaFunction">LambdaFunction</a>: <i>
      - &lt;a href=&#34;lambdafunction.md&#34;&gt;LambdaFunction&lt;/a&gt;</i>
    <a href="#queue" title="Queue">Queue</a>: <i>
      - &lt;a href=&#34;queue.md&#34;&gt;Queue&lt;/a&gt;</i>
    <a href="#topic" title="Topic">Topic</a>: <i>
      - &lt;a href=&#34;topic.md&#34;&gt;Topic&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bucket

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LambdaFunction

_Required_: No

_Type_: List of &lt;a href=&#34;lambdafunction.md&#34;&gt;LambdaFunction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Queue

_Required_: No

_Type_: List of &lt;a href=&#34;queue.md&#34;&gt;Queue&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Topic

_Required_: No

_Type_: List of &lt;a href=&#34;topic.md&#34;&gt;Topic&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

