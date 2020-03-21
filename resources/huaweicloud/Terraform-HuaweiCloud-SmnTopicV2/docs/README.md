# Terraform::HuaweiCloud::SmnTopicV2

Manages a V2 topic resource within HuaweiCloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HuaweiCloud::SmnTopicV2",
    "Properties" : {
        "<a href="#createtime" title="CreateTime">CreateTime</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#pushpolicy" title="PushPolicy">PushPolicy</a>" : <i>Double</i>,
        "<a href="#topicurn" title="TopicUrn">TopicUrn</a>" : <i>String</i>,
        "<a href="#updatetime" title="UpdateTime">UpdateTime</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HuaweiCloud::SmnTopicV2
Properties:
    <a href="#createtime" title="CreateTime">CreateTime</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#pushpolicy" title="PushPolicy">PushPolicy</a>: <i>Double</i>
    <a href="#topicurn" title="TopicUrn">TopicUrn</a>: <i>String</i>
    <a href="#updatetime" title="UpdateTime">UpdateTime</a>: <i>String</i>
</pre>

## Properties

#### CreateTime

Time when the topic was created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

Topic display name, which is presented as the
name of the email sender in an email message.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the topic to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PushPolicy

Message pushing policy. 0 indicates that the message
sending fails and the message is cached in the queue. 1 indicates that the
failed message is discarded.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopicUrn

Resource identifier of a topic, which is unique.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateTime

Time when the topic was updated.

_Required_: No

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

