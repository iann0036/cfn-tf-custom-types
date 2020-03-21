# Terraform::AzureRM::ServicebusSubscriptionRule CorrelationFilter

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#contenttype" title="ContentType">ContentType</a>" : <i>String</i>,
    "<a href="#correlationid" title="CorrelationId">CorrelationId</a>" : <i>String</i>,
    "<a href="#label" title="Label">Label</a>" : <i>String</i>,
    "<a href="#messageid" title="MessageId">MessageId</a>" : <i>String</i>,
    "<a href="#replyto" title="ReplyTo">ReplyTo</a>" : <i>String</i>,
    "<a href="#replytosessionid" title="ReplyToSessionId">ReplyToSessionId</a>" : <i>String</i>,
    "<a href="#sessionid" title="SessionId">SessionId</a>" : <i>String</i>,
    "<a href="#to" title="To">To</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#contenttype" title="ContentType">ContentType</a>: <i>String</i>
<a href="#correlationid" title="CorrelationId">CorrelationId</a>: <i>String</i>
<a href="#label" title="Label">Label</a>: <i>String</i>
<a href="#messageid" title="MessageId">MessageId</a>: <i>String</i>
<a href="#replyto" title="ReplyTo">ReplyTo</a>: <i>String</i>
<a href="#replytosessionid" title="ReplyToSessionId">ReplyToSessionId</a>: <i>String</i>
<a href="#sessionid" title="SessionId">SessionId</a>: <i>String</i>
<a href="#to" title="To">To</a>: <i>String</i>
</pre>

## Properties

#### ContentType

Content type of the message.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CorrelationId

Identifier of the correlation.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

Application specific label.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MessageId

Identifier of the message.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplyTo

Address of the queue to reply to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplyToSessionId

Session identifier to reply to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionId

Session identifier.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### To

Address to send to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

