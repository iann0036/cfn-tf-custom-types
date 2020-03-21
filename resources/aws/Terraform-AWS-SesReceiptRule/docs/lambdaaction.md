# Terraform::AWS::SesReceiptRule LambdaAction

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#functionarn" title="FunctionArn">FunctionArn</a>" : <i>String</i>,
    "<a href="#invocationtype" title="InvocationType">InvocationType</a>" : <i>String</i>,
    "<a href="#position" title="Position">Position</a>" : <i>Double</i>,
    "<a href="#topicarn" title="TopicArn">TopicArn</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#functionarn" title="FunctionArn">FunctionArn</a>: <i>String</i>
<a href="#invocationtype" title="InvocationType">InvocationType</a>: <i>String</i>
<a href="#position" title="Position">Position</a>: <i>Double</i>
<a href="#topicarn" title="TopicArn">TopicArn</a>: <i>String</i>
</pre>

## Properties

#### FunctionArn

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InvocationType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Position

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopicArn

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

