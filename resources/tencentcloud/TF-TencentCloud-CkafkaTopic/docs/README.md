# TF::TencentCloud::CkafkaTopic

Use this resource to create ckafka topic.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::CkafkaTopic",
    "Properties" : {
        "<a href="#cleanuppolicy" title="CleanUpPolicy">CleanUpPolicy</a>" : <i>String</i>,
        "<a href="#enablewhitelist" title="EnableWhiteList">EnableWhiteList</a>" : <i>Boolean</i>,
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#ipwhitelist" title="IpWhiteList">IpWhiteList</a>" : <i>[ String, ... ]</i>,
        "<a href="#maxmessagebytes" title="MaxMessageBytes">MaxMessageBytes</a>" : <i>Double</i>,
        "<a href="#note" title="Note">Note</a>" : <i>String</i>,
        "<a href="#partitionnum" title="PartitionNum">PartitionNum</a>" : <i>Double</i>,
        "<a href="#replicanum" title="ReplicaNum">ReplicaNum</a>" : <i>Double</i>,
        "<a href="#retention" title="Retention">Retention</a>" : <i>Double</i>,
        "<a href="#segment" title="Segment">Segment</a>" : <i>Double</i>,
        "<a href="#syncreplicaminnum" title="SyncReplicaMinNum">SyncReplicaMinNum</a>" : <i>Double</i>,
        "<a href="#topicname" title="TopicName">TopicName</a>" : <i>String</i>,
        "<a href="#uncleanleaderelectionenable" title="UncleanLeaderElectionEnable">UncleanLeaderElectionEnable</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::CkafkaTopic
Properties:
    <a href="#cleanuppolicy" title="CleanUpPolicy">CleanUpPolicy</a>: <i>String</i>
    <a href="#enablewhitelist" title="EnableWhiteList">EnableWhiteList</a>: <i>Boolean</i>
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#ipwhitelist" title="IpWhiteList">IpWhiteList</a>: <i>
      - String</i>
    <a href="#maxmessagebytes" title="MaxMessageBytes">MaxMessageBytes</a>: <i>Double</i>
    <a href="#note" title="Note">Note</a>: <i>String</i>
    <a href="#partitionnum" title="PartitionNum">PartitionNum</a>: <i>Double</i>
    <a href="#replicanum" title="ReplicaNum">ReplicaNum</a>: <i>Double</i>
    <a href="#retention" title="Retention">Retention</a>: <i>Double</i>
    <a href="#segment" title="Segment">Segment</a>: <i>Double</i>
    <a href="#syncreplicaminnum" title="SyncReplicaMinNum">SyncReplicaMinNum</a>: <i>Double</i>
    <a href="#topicname" title="TopicName">TopicName</a>: <i>String</i>
    <a href="#uncleanleaderelectionenable" title="UncleanLeaderElectionEnable">UncleanLeaderElectionEnable</a>: <i>Boolean</i>
</pre>

## Properties

#### CleanUpPolicy

Clear log policy, log clear mode, default is `delete`. `delete`: logs are deleted according to the storage time. `compact`: logs are compressed according to the key. `compact, delete`: logs are compressed according to the key and will be deleted according to the storage time.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableWhiteList

Whether to open the ip whitelist, `true`: open, `false`: close.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

Ckafka instance ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpWhiteList

Ip whitelist, quota limit, required when enableWhileList=true.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxMessageBytes

Max message bytes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Note

The subject note is a string of no more than 64 characters. It must start with a letter, and the remaining part can contain letters, numbers and dashes (-).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PartitionNum

The number of partition.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplicaNum

The number of replica, the maximum is 3.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Retention

Message can be selected. Retention time, unit is ms, the current minimum value is 60000ms.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Segment

Segment scrolling time, in ms, the current minimum is 3600000ms.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SyncReplicaMinNum

Min number of sync replicas, Default is `1`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopicName

Name of the CKafka topic. It must start with a letter, the rest can contain letters, numbers and dashes(-). The length range is from 1 to 64.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UncleanLeaderElectionEnable

Whether to allow unsynchronized replicas to be selected as leader, default is `false`, `true: `allowed, `false`: not allowed.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### ForwardCosBucket

Returns the <code>ForwardCosBucket</code> value.

#### ForwardInterval

Returns the <code>ForwardInterval</code> value.

#### ForwardStatus

Returns the <code>ForwardStatus</code> value.

#### Id

Returns the <code>Id</code> value.

#### MessageStorageLocation

Returns the <code>MessageStorageLocation</code> value.

#### SegmentBytes

Returns the <code>SegmentBytes</code> value.

