# Terraform::AWS::DmsReplicationTask

CloudFormation equivalent of aws_dms_replication_task

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::DmsReplicationTask",
    "Properties" : {
        "<a href="#cdcstarttime" title="CdcStartTime">CdcStartTime</a>" : <i>String</i>,
        "<a href="#migrationtype" title="MigrationType">MigrationType</a>" : <i>String</i>,
        "<a href="#replicationinstancearn" title="ReplicationInstanceArn">ReplicationInstanceArn</a>" : <i>String</i>,
        "<a href="#replicationtaskid" title="ReplicationTaskId">ReplicationTaskId</a>" : <i>String</i>,
        "<a href="#replicationtasksettings" title="ReplicationTaskSettings">ReplicationTaskSettings</a>" : <i>String</i>,
        "<a href="#sourceendpointarn" title="SourceEndpointArn">SourceEndpointArn</a>" : <i>String</i>,
        "<a href="#tablemappings" title="TableMappings">TableMappings</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#targetendpointarn" title="TargetEndpointArn">TargetEndpointArn</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::DmsReplicationTask
Properties:
    <a href="#cdcstarttime" title="CdcStartTime">CdcStartTime</a>: <i>String</i>
    <a href="#migrationtype" title="MigrationType">MigrationType</a>: <i>String</i>
    <a href="#replicationinstancearn" title="ReplicationInstanceArn">ReplicationInstanceArn</a>: <i>String</i>
    <a href="#replicationtaskid" title="ReplicationTaskId">ReplicationTaskId</a>: <i>String</i>
    <a href="#replicationtasksettings" title="ReplicationTaskSettings">ReplicationTaskSettings</a>: <i>String</i>
    <a href="#sourceendpointarn" title="SourceEndpointArn">SourceEndpointArn</a>: <i>String</i>
    <a href="#tablemappings" title="TableMappings">TableMappings</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#targetendpointarn" title="TargetEndpointArn">TargetEndpointArn</a>: <i>String</i>
</pre>

## Properties

#### CdcStartTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MigrationType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplicationInstanceArn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplicationTaskId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplicationTaskSettings

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceEndpointArn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TableMappings

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetEndpointArn

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

