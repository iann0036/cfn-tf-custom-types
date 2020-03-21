# Terraform::OpenTelekomCloud::LogtankTopicV2

Manage a log topic resource within OpenTelekomCloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenTelekomCloud::LogtankTopicV2",
    "Properties" : {
        "<a href="#groupid" title="GroupId">GroupId</a>" : <i>String</i>,
        "<a href="#topicname" title="TopicName">TopicName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenTelekomCloud::LogtankTopicV2
Properties:
    <a href="#groupid" title="GroupId">GroupId</a>: <i>String</i>
    <a href="#topicname" title="TopicName">TopicName</a>: <i>String</i>
</pre>

## Properties

#### GroupId

Specifies the ID of a created log group.
Changing this parameter will create a new resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopicName

Specifies the log topic name.
Changing this parameter will create a new resource.

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

#### IndexEnabled

Returns the <code>IndexEnabled</code> value.

