# Terraform::Alicloud::LogStore

The log store is a unit in Log Service to collect, store, and query the log data. Each log store belongs to a project,
and each project can create multiple Logstores. [Refer to details](https://www.alibabacloud.com/help/doc-detail/48874.htm)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::LogStore",
    "Properties" : {
        "<a href="#appendmeta" title="AppendMeta">AppendMeta</a>" : <i>Boolean</i>,
        "<a href="#autosplit" title="AutoSplit">AutoSplit</a>" : <i>Boolean</i>,
        "<a href="#enablewebtracking" title="EnableWebTracking">EnableWebTracking</a>" : <i>Boolean</i>,
        "<a href="#maxsplitshardcount" title="MaxSplitShardCount">MaxSplitShardCount</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#retentionperiod" title="RetentionPeriod">RetentionPeriod</a>" : <i>Double</i>,
        "<a href="#shardcount" title="ShardCount">ShardCount</a>" : <i>Double</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::LogStore
Properties:
    <a href="#appendmeta" title="AppendMeta">AppendMeta</a>: <i>Boolean</i>
    <a href="#autosplit" title="AutoSplit">AutoSplit</a>: <i>Boolean</i>
    <a href="#enablewebtracking" title="EnableWebTracking">EnableWebTracking</a>: <i>Boolean</i>
    <a href="#maxsplitshardcount" title="MaxSplitShardCount">MaxSplitShardCount</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#retentionperiod" title="RetentionPeriod">RetentionPeriod</a>: <i>Double</i>
    <a href="#shardcount" title="ShardCount">ShardCount</a>: <i>Double</i>
</pre>

## Properties

#### AppendMeta

Determines whether to append log meta automatically. The meta includes log receive time and client IP address. Default to true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoSplit

Determines whether to automatically split a shard. Default to true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableWebTracking

Determines whether to enable Web Tracking. Default false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSplitShardCount

The maximum number of shards for automatic split, which is in the range of 1 to 64. You must specify this parameter when autoSplit is true.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The log store, which is unique in the same project.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The project name to the log store belongs.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionPeriod

The data retention time (in days). Valid values: [1-3650]. Default to 30. Log store data will be stored permanently when the value is "3650".

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShardCount

The number of shards in this log store. Default to 2. You can modify it by "Split" or "Merge" operations. [Refer to details](https://www.alibabacloud.com/help/doc-detail/28976.htm).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### Shards

Returns the <code>Shards</code> value.

