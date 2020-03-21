# Terraform::AWS::SnsTopic

CloudFormation equivalent of aws_sns_topic

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::SnsTopic",
    "Properties" : {
        "<a href="#applicationfailurefeedbackrolearn" title="ApplicationFailureFeedbackRoleArn">ApplicationFailureFeedbackRoleArn</a>" : <i>String</i>,
        "<a href="#applicationsuccessfeedbackrolearn" title="ApplicationSuccessFeedbackRoleArn">ApplicationSuccessFeedbackRoleArn</a>" : <i>String</i>,
        "<a href="#applicationsuccessfeedbacksamplerate" title="ApplicationSuccessFeedbackSampleRate">ApplicationSuccessFeedbackSampleRate</a>" : <i>Double</i>,
        "<a href="#deliverypolicy" title="DeliveryPolicy">DeliveryPolicy</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#httpfailurefeedbackrolearn" title="HttpFailureFeedbackRoleArn">HttpFailureFeedbackRoleArn</a>" : <i>String</i>,
        "<a href="#httpsuccessfeedbackrolearn" title="HttpSuccessFeedbackRoleArn">HttpSuccessFeedbackRoleArn</a>" : <i>String</i>,
        "<a href="#httpsuccessfeedbacksamplerate" title="HttpSuccessFeedbackSampleRate">HttpSuccessFeedbackSampleRate</a>" : <i>Double</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#kmsmasterkeyid" title="KmsMasterKeyId">KmsMasterKeyId</a>" : <i>String</i>,
        "<a href="#lambdafailurefeedbackrolearn" title="LambdaFailureFeedbackRoleArn">LambdaFailureFeedbackRoleArn</a>" : <i>String</i>,
        "<a href="#lambdasuccessfeedbackrolearn" title="LambdaSuccessFeedbackRoleArn">LambdaSuccessFeedbackRoleArn</a>" : <i>String</i>,
        "<a href="#lambdasuccessfeedbacksamplerate" title="LambdaSuccessFeedbackSampleRate">LambdaSuccessFeedbackSampleRate</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nameprefix" title="NamePrefix">NamePrefix</a>" : <i>String</i>,
        "<a href="#policy" title="Policy">Policy</a>" : <i>String</i>,
        "<a href="#sqsfailurefeedbackrolearn" title="SqsFailureFeedbackRoleArn">SqsFailureFeedbackRoleArn</a>" : <i>String</i>,
        "<a href="#sqssuccessfeedbackrolearn" title="SqsSuccessFeedbackRoleArn">SqsSuccessFeedbackRoleArn</a>" : <i>String</i>,
        "<a href="#sqssuccessfeedbacksamplerate" title="SqsSuccessFeedbackSampleRate">SqsSuccessFeedbackSampleRate</a>" : <i>Double</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::SnsTopic
Properties:
    <a href="#applicationfailurefeedbackrolearn" title="ApplicationFailureFeedbackRoleArn">ApplicationFailureFeedbackRoleArn</a>: <i>String</i>
    <a href="#applicationsuccessfeedbackrolearn" title="ApplicationSuccessFeedbackRoleArn">ApplicationSuccessFeedbackRoleArn</a>: <i>String</i>
    <a href="#applicationsuccessfeedbacksamplerate" title="ApplicationSuccessFeedbackSampleRate">ApplicationSuccessFeedbackSampleRate</a>: <i>Double</i>
    <a href="#deliverypolicy" title="DeliveryPolicy">DeliveryPolicy</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#httpfailurefeedbackrolearn" title="HttpFailureFeedbackRoleArn">HttpFailureFeedbackRoleArn</a>: <i>String</i>
    <a href="#httpsuccessfeedbackrolearn" title="HttpSuccessFeedbackRoleArn">HttpSuccessFeedbackRoleArn</a>: <i>String</i>
    <a href="#httpsuccessfeedbacksamplerate" title="HttpSuccessFeedbackSampleRate">HttpSuccessFeedbackSampleRate</a>: <i>Double</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#kmsmasterkeyid" title="KmsMasterKeyId">KmsMasterKeyId</a>: <i>String</i>
    <a href="#lambdafailurefeedbackrolearn" title="LambdaFailureFeedbackRoleArn">LambdaFailureFeedbackRoleArn</a>: <i>String</i>
    <a href="#lambdasuccessfeedbackrolearn" title="LambdaSuccessFeedbackRoleArn">LambdaSuccessFeedbackRoleArn</a>: <i>String</i>
    <a href="#lambdasuccessfeedbacksamplerate" title="LambdaSuccessFeedbackSampleRate">LambdaSuccessFeedbackSampleRate</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nameprefix" title="NamePrefix">NamePrefix</a>: <i>String</i>
    <a href="#policy" title="Policy">Policy</a>: <i>String</i>
    <a href="#sqsfailurefeedbackrolearn" title="SqsFailureFeedbackRoleArn">SqsFailureFeedbackRoleArn</a>: <i>String</i>
    <a href="#sqssuccessfeedbackrolearn" title="SqsSuccessFeedbackRoleArn">SqsSuccessFeedbackRoleArn</a>: <i>String</i>
    <a href="#sqssuccessfeedbacksamplerate" title="SqsSuccessFeedbackSampleRate">SqsSuccessFeedbackSampleRate</a>: <i>Double</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
</pre>

## Properties

#### ApplicationFailureFeedbackRoleArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationSuccessFeedbackRoleArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationSuccessFeedbackSampleRate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeliveryPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpFailureFeedbackRoleArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpSuccessFeedbackRoleArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpSuccessFeedbackSampleRate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsMasterKeyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LambdaFailureFeedbackRoleArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LambdaSuccessFeedbackRoleArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LambdaSuccessFeedbackSampleRate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamePrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SqsFailureFeedbackRoleArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SqsSuccessFeedbackRoleArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SqsSuccessFeedbackSampleRate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

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

