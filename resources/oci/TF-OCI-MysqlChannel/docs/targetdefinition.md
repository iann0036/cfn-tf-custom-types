# TF::OCI::MysqlChannel TargetDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#applierusername" title="ApplierUsername">ApplierUsername</a>" : <i>String</i>,
    "<a href="#channelname" title="ChannelName">ChannelName</a>" : <i>String</i>,
    "<a href="#dbsystemid" title="DbSystemId">DbSystemId</a>" : <i>String</i>,
    "<a href="#targettype" title="TargetType">TargetType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#applierusername" title="ApplierUsername">ApplierUsername</a>: <i>String</i>
<a href="#channelname" title="ChannelName">ChannelName</a>: <i>String</i>
<a href="#dbsystemid" title="DbSystemId">DbSystemId</a>: <i>String</i>
<a href="#targettype" title="TargetType">TargetType</a>: <i>String</i>
</pre>

## Properties

#### ApplierUsername

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChannelName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbSystemId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

