# Terraform::AWS::SesReceiptRule BounceAction

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#message" title="Message">Message</a>" : <i>String</i>,
    "<a href="#position" title="Position">Position</a>" : <i>Double</i>,
    "<a href="#sender" title="Sender">Sender</a>" : <i>String</i>,
    "<a href="#smtpreplycode" title="SmtpReplyCode">SmtpReplyCode</a>" : <i>String</i>,
    "<a href="#statuscode" title="StatusCode">StatusCode</a>" : <i>String</i>,
    "<a href="#topicarn" title="TopicArn">TopicArn</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#message" title="Message">Message</a>: <i>String</i>
<a href="#position" title="Position">Position</a>: <i>Double</i>
<a href="#sender" title="Sender">Sender</a>: <i>String</i>
<a href="#smtpreplycode" title="SmtpReplyCode">SmtpReplyCode</a>: <i>String</i>
<a href="#statuscode" title="StatusCode">StatusCode</a>: <i>String</i>
<a href="#topicarn" title="TopicArn">TopicArn</a>: <i>String</i>
</pre>

## Properties

#### Message

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Position

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sender

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmtpReplyCode

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatusCode

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopicArn

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

