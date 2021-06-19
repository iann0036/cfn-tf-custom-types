# TF::AWS::DmsReplicationTask

Provides a DMS (Data Migration Service) replication task resource. DMS replication tasks can be created, updated, deleted, and imported.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::DmsReplicationTask",
    "Properties" : {
        "<a href="#cdcstarttime" title="CdcStartTime">CdcStartTime</a>" : <i>String</i>,
        "<a href="#migrationtype" title="MigrationType">MigrationType</a>" : <i>String</i>,
        "<a href="#replicationinstancearn" title="ReplicationInstanceArn">ReplicationInstanceArn</a>" : <i>String</i>,
        "<a href="#replicationtaskid" title="ReplicationTaskId">ReplicationTaskId</a>" : <i>String</i>,
        "<a href="#replicationtasksettings" title="ReplicationTaskSettings">ReplicationTaskSettings</a>" : <i>String</i>,
        "<a href="#sourceendpointarn" title="SourceEndpointArn">SourceEndpointArn</a>" : <i>String</i>,
        "<a href="#tablemappings" title="TableMappings">TableMappings</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#targetendpointarn" title="TargetEndpointArn">TargetEndpointArn</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::DmsReplicationTask
Properties:
    <a href="#cdcstarttime" title="CdcStartTime">CdcStartTime</a>: <i>String</i>
    <a href="#migrationtype" title="MigrationType">MigrationType</a>: <i>String</i>
    <a href="#replicationinstancearn" title="ReplicationInstanceArn">ReplicationInstanceArn</a>: <i>String</i>
    <a href="#replicationtaskid" title="ReplicationTaskId">ReplicationTaskId</a>: <i>String</i>
    <a href="#replicationtasksettings" title="ReplicationTaskSettings">ReplicationTaskSettings</a>: <i>String</i>
    <a href="#sourceendpointarn" title="SourceEndpointArn">SourceEndpointArn</a>: <i>String</i>
    <a href="#tablemappings" title="TableMappings">TableMappings</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#targetendpointarn" title="TargetEndpointArn">TargetEndpointArn</a>: <i>String</i>
</pre>

## Properties

#### CdcStartTime

The Unix timestamp integer for the start of the Change Data Capture (CDC) operation.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MigrationType

The migration type. Can be one of `full-load | cdc | full-load-and-cdc`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplicationInstanceArn

The Amazon Resource Name (ARN) of the replication instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplicationTaskId

The replication task identifier.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplicationTaskSettings

An escaped JSON string that contains the task settings. For a complete list of task settings, see [Task Settings for AWS Database Migration Service Tasks](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.html).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceEndpointArn

The Amazon Resource Name (ARN) string that uniquely identifies the source endpoint.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TableMappings

An escaped JSON string that contains the table mappings. For information on table mapping see [Using Table Mapping with an AWS Database Migration Service Task to Select and Filter Data](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.html).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetEndpointArn

The Amazon Resource Name (ARN) string that uniquely identifies the target endpoint.

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

#### ReplicationTaskArn

Returns the <code>ReplicationTaskArn</code> value.

