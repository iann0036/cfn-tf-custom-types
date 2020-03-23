# Terraform::AWS::SnsTopic

Provides an SNS topic resource

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
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>
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
      - <a href="tags.md">Tags</a></i>
</pre>

## Properties

#### ApplicationFailureFeedbackRoleArn

IAM role for failure feedback.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationSuccessFeedbackRoleArn

The IAM role permitted to receive success feedback for this topic.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationSuccessFeedbackSampleRate

Percentage of success to sample.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeliveryPolicy

The SNS delivery policy. More on [AWS documentation](https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

The display name for the SNS topic.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpFailureFeedbackRoleArn

IAM role for failure feedback.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpSuccessFeedbackRoleArn

The IAM role permitted to receive success feedback for this topic.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpSuccessFeedbackSampleRate

Percentage of success to sample.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsMasterKeyId

The ID of an AWS-managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see [Key Terms](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LambdaFailureFeedbackRoleArn

IAM role for failure feedback.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LambdaSuccessFeedbackRoleArn

The IAM role permitted to receive success feedback for this topic.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LambdaSuccessFeedbackSampleRate

Percentage of success to sample.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The friendly name for the SNS topic. By default generated by Terraform.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamePrefix

The friendly name for the SNS topic. Conflicts with `name`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policy

The fully-formed AWS policy as JSON. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://learn.hashicorp.com/terraform/aws/iam-policy).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SqsFailureFeedbackRoleArn

IAM role for failure feedback.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SqsSuccessFeedbackRoleArn

The IAM role permitted to receive success feedback for this topic.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SqsSuccessFeedbackSampleRate

Percentage of success to sample.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Key-value mapping of resource tags.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

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

