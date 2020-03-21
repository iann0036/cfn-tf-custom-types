# Terraform::OpenTelekomCloud::CtsTrackerV1

Allows you to collect, store, and query cloud resource operation records.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenTelekomCloud::CtsTrackerV1",
    "Properties" : {
        "<a href="#bucketname" title="BucketName">BucketName</a>" : <i>String</i>,
        "<a href="#fileprefixname" title="FilePrefixName">FilePrefixName</a>" : <i>String</i>,
        "<a href="#issendallkeyoperation" title="IsSendAllKeyOperation">IsSendAllKeyOperation</a>" : <i>Boolean</i>,
        "<a href="#issupportsmn" title="IsSupportSmn">IsSupportSmn</a>" : <i>Boolean</i>,
        "<a href="#neednotifyuserlist" title="NeedNotifyUserList">NeedNotifyUserList</a>" : <i>[ String, ... ]</i>,
        "<a href="#operations" title="Operations">Operations</a>" : <i>[ String, ... ]</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#topicid" title="TopicId">TopicId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenTelekomCloud::CtsTrackerV1
Properties:
    <a href="#bucketname" title="BucketName">BucketName</a>: <i>String</i>
    <a href="#fileprefixname" title="FilePrefixName">FilePrefixName</a>: <i>String</i>
    <a href="#issendallkeyoperation" title="IsSendAllKeyOperation">IsSendAllKeyOperation</a>: <i>Boolean</i>
    <a href="#issupportsmn" title="IsSupportSmn">IsSupportSmn</a>: <i>Boolean</i>
    <a href="#neednotifyuserlist" title="NeedNotifyUserList">NeedNotifyUserList</a>: <i>
      - String</i>
    <a href="#operations" title="Operations">Operations</a>: <i>
      - String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#topicid" title="TopicId">TopicId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### BucketName

The OBS bucket name for a tracker.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilePrefixName

The prefix of a log that needs to be stored in an OBS bucket.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsSendAllKeyOperation

When the value is **false**, operations cannot be left empty.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsSupportSmn

Specifies whether SMN is supported. When the value is false, topic_id and operations can be left empty.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NeedNotifyUserList

The users using the login function. When these users log in, notifications will be sent.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Operations

Trigger conditions for sending a notification.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

The status of a tracker. The value should be **enabled** when creating a tracker, and when updating the value can be enabled or disabled.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopicId

The theme of the SMN service, Is obtained from SMN and in the format of **urn:smn:([a-z]|[A-Z]|[0-9]|\-){1,32}:([a-z]|[A-Z]|[0-9]){32}:([a-z]|[A-Z]|[0-9]|\-|\_){1,256}**.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### TrackerName

Returns the <code>TrackerName</code> value.

