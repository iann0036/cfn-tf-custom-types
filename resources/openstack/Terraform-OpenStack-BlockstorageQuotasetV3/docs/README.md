# Terraform::OpenStack::BlockstorageQuotasetV3

Manages a V3 block storage quotaset resource within OpenStack.

~> **Note:** This usually requires admin privileges.

~> **Note:** This resource has a no-op deletion so no actual actions will be done against the OpenStack API 
    in case of delete call.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenStack::BlockstorageQuotasetV3",
    "Properties" : {
        "<a href="#backupgigabytes" title="BackupGigabytes">BackupGigabytes</a>" : <i>Double</i>,
        "<a href="#backups" title="Backups">Backups</a>" : <i>Double</i>,
        "<a href="#gigabytes" title="Gigabytes">Gigabytes</a>" : <i>Double</i>,
        "<a href="#groups" title="Groups">Groups</a>" : <i>Double</i>,
        "<a href="#pervolumegigabytes" title="PerVolumeGigabytes">PerVolumeGigabytes</a>" : <i>Double</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#snapshots" title="Snapshots">Snapshots</a>" : <i>Double</i>,
        "<a href="#volumes" title="Volumes">Volumes</a>" : <i>Double</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenStack::BlockstorageQuotasetV3
Properties:
    <a href="#backupgigabytes" title="BackupGigabytes">BackupGigabytes</a>: <i>Double</i>
    <a href="#backups" title="Backups">Backups</a>: <i>Double</i>
    <a href="#gigabytes" title="Gigabytes">Gigabytes</a>: <i>Double</i>
    <a href="#groups" title="Groups">Groups</a>: <i>Double</i>
    <a href="#pervolumegigabytes" title="PerVolumeGigabytes">PerVolumeGigabytes</a>: <i>Double</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#snapshots" title="Snapshots">Snapshots</a>: <i>Double</i>
    <a href="#volumes" title="Volumes">Volumes</a>: <i>Double</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### BackupGigabytes

Quota value for backup gigabytes. Changing
this updates the existing quotaset.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backups

Quota value for backups. Changing this updates the
existing quotaset.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gigabytes

Quota value for gigabytes. Changing this updates the
existing quotaset.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Groups

Quota value for groups. Changing this updates the
existing quotaset.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PerVolumeGigabytes

Quota value for gigabytes per volume .
Changing this updates the existing quotaset.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

ID of the project to manage quotas. Changing this
creates a new quotaset.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to create the volume. If
omitted, the `region` argument of the provider is used. Changing this
creates a new quotaset.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Snapshots

Quota value for snapshots. Changing this updates the
existing quotaset.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Volumes

Quota value for volumes. Changing this updates the
existing quotaset.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

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

