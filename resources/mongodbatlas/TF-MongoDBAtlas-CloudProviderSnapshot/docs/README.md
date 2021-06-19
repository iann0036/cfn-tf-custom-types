# TF::MongoDBAtlas::CloudProviderSnapshot

`mongodbatlas_cloud_provider_snapshot` provides a resource to take a cloud backup snapshot on demand.
On-demand snapshots happen immediately, unlike scheduled snapshots which occur at regular intervals. If there is already an on-demand snapshot with a status of queued or inProgress, you must wait until Atlas has completed the on-demand snapshot before taking another.

-> **NOTE:** Groups and projects are synonymous terms. You may find `groupId` in the official documentation.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::MongoDBAtlas::CloudProviderSnapshot",
    "Properties" : {
        "<a href="#clustername" title="ClusterName">ClusterName</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#retentionindays" title="RetentionInDays">RetentionInDays</a>" : <i>Double</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::MongoDBAtlas::CloudProviderSnapshot
Properties:
    <a href="#clustername" title="ClusterName">ClusterName</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#retentionindays" title="RetentionInDays">RetentionInDays</a>: <i>Double</i>
</pre>

## Properties

#### ClusterName

The name of the Atlas cluster that contains the snapshots you want to retrieve.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the on-demand snapshot.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The unique identifier of the project for the Atlas cluster.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionInDays

The number of days that Atlas should retain the on-demand snapshot. Must be at least 1.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### ExpiresAt

Returns the <code>ExpiresAt</code> value.

#### Id

Returns the <code>Id</code> value.

#### MasterKeyUuid

Returns the <code>MasterKeyUuid</code> value.

#### MongodVersion

Returns the <code>MongodVersion</code> value.

#### SnapshotId

Returns the <code>SnapshotId</code> value.

#### SnapshotType

Returns the <code>SnapshotType</code> value.

#### Status

Returns the <code>Status</code> value.

#### StorageSizeBytes

Returns the <code>StorageSizeBytes</code> value.

#### Type

Returns the <code>Type</code> value.

