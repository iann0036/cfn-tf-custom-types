# TF::MongoDBAtlas::CloudProviderSnapshotRestoreJob

`mongodbatlas_cloud_provider_snapshot_restore_job` provides a resource to create a new restore job from a cloud backup snapshot of a specified cluster. The restore job can be one of three types: 
* **automated:** Atlas automatically restores the snapshot with snapshotId to the Atlas cluster with name targetClusterName in the Atlas project with targetGroupId.

* **download:** Atlas provides a URL to download a .tar.gz of the snapshot with snapshotId. The contents of the archive contain the data files for your Atlas cluster.

* **pointInTime:**  Atlas performs a Continuous Cloud Backup restore.

-> **Important:** If you specify `deliveryType` : `automated` or `deliveryType` : `pointInTime` in your request body to create an automated restore job, Atlas removes all existing data on the target cluster prior to the restore.

-> **NOTE:** Groups and projects are synonymous terms. You may find `groupId` in the official documentation.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::MongoDBAtlas::CloudProviderSnapshotRestoreJob",
    "Properties" : {
        "<a href="#clustername" title="ClusterName">ClusterName</a>" : <i>String</i>,
        "<a href="#deliverytype" title="DeliveryType">DeliveryType</a>" : <i>[ <a href="deliverytypedefinition.md">DeliveryTypeDefinition</a>, ... ]</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#snapshotid" title="SnapshotId">SnapshotId</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::MongoDBAtlas::CloudProviderSnapshotRestoreJob
Properties:
    <a href="#clustername" title="ClusterName">ClusterName</a>: <i>String</i>
    <a href="#deliverytype" title="DeliveryType">DeliveryType</a>: <i>
      - <a href="deliverytypedefinition.md">DeliveryTypeDefinition</a></i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#snapshotid" title="SnapshotId">SnapshotId</a>: <i>String</i>
</pre>

## Properties

#### ClusterName

The name of the Atlas cluster whose snapshot you want to restore.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeliveryType

Type of restore job to create. Possible values are: **download** or **automated**, only one must be set it in ``true``.

_Required_: Yes

_Type_: List of <a href="deliverytypedefinition.md">DeliveryTypeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The unique identifier of the project for the Atlas cluster whose snapshot you want to restore.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotId

Unique identifier of the snapshot to restore.

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

#### Cancelled

Returns the <code>Cancelled</code> value.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### DeliveryUrl

Returns the <code>DeliveryUrl</code> value.

#### Expired

Returns the <code>Expired</code> value.

#### ExpiresAt

Returns the <code>ExpiresAt</code> value.

#### FinishedAt

Returns the <code>FinishedAt</code> value.

#### Id

Returns the <code>Id</code> value.

#### SnapshotRestoreJobId

Returns the <code>SnapshotRestoreJobId</code> value.

#### Timestamp

Returns the <code>Timestamp</code> value.

