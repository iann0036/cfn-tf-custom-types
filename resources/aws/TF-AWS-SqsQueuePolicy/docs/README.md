# TF::AWS::SqsQueuePolicy

Allows you to set a policy of an SQS Queue
while referencing ARN of the queue within the policy.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::SqsQueuePolicy",
    "Properties" : {
        "<a href="#policy" title="Policy">Policy</a>" : <i>String</i>,
        "<a href="#queueurl" title="QueueUrl">QueueUrl</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::SqsQueuePolicy
Properties:
    <a href="#policy" title="Policy">Policy</a>: <i>String</i>
    <a href="#queueurl" title="QueueUrl">QueueUrl</a>: <i>String</i>
</pre>

## Properties

#### Policy

The JSON policy for the SQS queue. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://learn.hashicorp.com/terraform/aws/iam-policy).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueueUrl

The URL of the SQS Queue to which to attach the policy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

