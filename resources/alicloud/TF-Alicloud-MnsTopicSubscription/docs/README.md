# TF::Alicloud::MnsTopicSubscription

Provides a MNS topic subscription resource.

-> **NOTE:** Terraform will auto build a mns topic subscription  while it uses `alicloud_mns_topic_subscription` to build a mns topic subscription resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::MnsTopicSubscription",
    "Properties" : {
        "<a href="#endpoint" title="Endpoint">Endpoint</a>" : <i>String</i>,
        "<a href="#filtertag" title="FilterTag">FilterTag</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notifycontentformat" title="NotifyContentFormat">NotifyContentFormat</a>" : <i>String</i>,
        "<a href="#notifystrategy" title="NotifyStrategy">NotifyStrategy</a>" : <i>String</i>,
        "<a href="#topicname" title="TopicName">TopicName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::MnsTopicSubscription
Properties:
    <a href="#endpoint" title="Endpoint">Endpoint</a>: <i>String</i>
    <a href="#filtertag" title="FilterTag">FilterTag</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notifycontentformat" title="NotifyContentFormat">NotifyContentFormat</a>: <i>String</i>
    <a href="#notifystrategy" title="NotifyStrategy">NotifyStrategy</a>: <i>String</i>
    <a href="#topicname" title="TopicName">TopicName</a>: <i>String</i>
</pre>

## Properties

#### Endpoint

The endpoint has three format. Available values format:
- HTTP Format: http://xxx.com/xxx
- Queue Format: acs:mns:{REGION}:{AccountID}:queues/{QueueName}
- Email Format: mail:directmail:{MailAddress}.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterTag

The length should be shorter than 16.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Two topics subscription on a single account in the same topic cannot have the same name. A topic subscription name must start with an English letter or a digit, and can contain English letters, digits, and hyphens, with the length not exceeding 256 characters.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyContentFormat

The NotifyContentFormat attribute of Subscription. This attribute specifies the content format of the messages pushed to users. The valid values: 'SIMPLIFIED', 'XML' and 'JSON'. Default to 'SIMPLIFIED'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyStrategy

The NotifyStrategy attribute of Subscription. This attribute specifies the retry strategy when message sending fails. the attribute has two value EXPONENTIAL_DECAY_RETR or BACKOFF_RETRY. Default value to BACKOFF_RETRY .

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopicName

The topic which The subscription belongs to was named with the name.A topic name must start with an English letter or a digit, and can contain English letters, digits, and hyphens, with the length not exceeding 256 characters.

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

