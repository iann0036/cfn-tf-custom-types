# TF::MongoDBAtlas::CloudProviderSnapshotBackupPolicy

`mongodbatlas_cloud_provider_snapshot_backup_policy` provides a resource that enables you to view and modify the snapshot schedule and retention settings for an Atlas cluster with Cloud Backup enabled.  A default policy is created automatically when Cloud Backup is enabled for the cluster.

-> **NOTE:** Groups and projects are synonymous terms. You may find `groupId` in the official documentation.

# Examples - Modifying Polices
When Cloud Backup is enabled for a cluster MongoDB Atlas automatically creates a default Cloud Backup schedule for the cluster with four policy items; hourly, daily, weekly, and monthly. Because of this default creation this provider automatically saves the Cloud Backup Snapshot Policy into the Terraform state when a cluster is created/modified to use Cloud Backup. If the default works well for you then you do not need to do anything other than create a cluster with Cloud Backup enabled and your Terraform state will have this information if you need it. However, if you want the po...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::MongoDBAtlas::CloudProviderSnapshotBackupPolicy",
    "Properties" : {
        "<a href="#clustername" title="ClusterName">ClusterName</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#referencehourofday" title="ReferenceHourOfDay">ReferenceHourOfDay</a>" : <i>Double</i>,
        "<a href="#referenceminuteofhour" title="ReferenceMinuteOfHour">ReferenceMinuteOfHour</a>" : <i>Double</i>,
        "<a href="#restorewindowdays" title="RestoreWindowDays">RestoreWindowDays</a>" : <i>Double</i>,
        "<a href="#updatesnapshots" title="UpdateSnapshots">UpdateSnapshots</a>" : <i>Boolean</i>,
        "<a href="#policies" title="Policies">Policies</a>" : <i>[ <a href="policiesdefinition.md">PoliciesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::MongoDBAtlas::CloudProviderSnapshotBackupPolicy
Properties:
    <a href="#clustername" title="ClusterName">ClusterName</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#referencehourofday" title="ReferenceHourOfDay">ReferenceHourOfDay</a>: <i>Double</i>
    <a href="#referenceminuteofhour" title="ReferenceMinuteOfHour">ReferenceMinuteOfHour</a>: <i>Double</i>
    <a href="#restorewindowdays" title="RestoreWindowDays">RestoreWindowDays</a>: <i>Double</i>
    <a href="#updatesnapshots" title="UpdateSnapshots">UpdateSnapshots</a>: <i>Boolean</i>
    <a href="#policies" title="Policies">Policies</a>: <i>
      - <a href="policiesdefinition.md">PoliciesDefinition</a></i>
</pre>

## Properties

#### ClusterName

The name of the Atlas cluster that contains the snapshot backup policy you want to retrieve.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The unique identifier of the project for the Atlas cluster.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReferenceHourOfDay

UTC Hour of day between 0 and 23, inclusive, representing which hour of the day that Atlas takes snapshots for backup policy items.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReferenceMinuteOfHour

UTC Minutes after referenceHourOfDay that Atlas takes snapshots for backup policy items. Must be between 0 and 59, inclusive.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestoreWindowDays

Number of days back in time you can restore to with point-in-time accuracy. Must be a positive, non-zero integer.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateSnapshots

Specify true to apply the retention changes in the updated backup policy to snapshots that Atlas took previously.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policies

_Required_: No

_Type_: List of <a href="policiesdefinition.md">PoliciesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ClusterId

Returns the <code>ClusterId</code> value.

#### Id

Returns the <code>Id</code> value.

#### NextSnapshot

Returns the <code>NextSnapshot</code> value.

