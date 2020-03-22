# Terraform::Alicloud::DatahubSubscription

The subscription is the basic unit of resource usage in Datahub Service under Publish/Subscribe model. You can manage the relationships between user and topics by using subscriptions. [Refer to details](https://help.aliyun.com/document_detail/47440.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::DatahubSubscription",
    "Properties" : {
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#projectname" title="ProjectName">ProjectName</a>" : <i>String</i>,
        "<a href="#topicname" title="TopicName">TopicName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::DatahubSubscription
Properties:
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#projectname" title="ProjectName">ProjectName</a>: <i>String</i>
    <a href="#topicname" title="TopicName">TopicName</a>: <i>String</i>
</pre>

## Properties

#### Comment

Comment of the datahub subscription. It cannot be longer than 255 characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectName

The name of the datahub project that the subscription belongs to. Its length is limited to 3-32 and only characters such as letters, digits and '_' are allowed. It is case-insensitive.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopicName

The name of the datahub topic that the subscription belongs to. Its length is limited to 1-128 and only characters such as letters, digits and '_' are allowed. It is case-insensitive.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### LastModifyTime

Returns the <code>LastModifyTime</code> value.

#### SubId

Returns the <code>SubId</code> value.

