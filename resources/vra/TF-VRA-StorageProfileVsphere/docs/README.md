# TF::VRA::StorageProfileVsphere

CloudFormation equivalent of vra_storage_profile_vsphere

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VRA::StorageProfileVsphere",
    "Properties" : {
        "<a href="#datastoreid" title="DatastoreId">DatastoreId</a>" : <i>String</i>,
        "<a href="#defaultitem" title="DefaultItem">DefaultItem</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#diskmode" title="DiskMode">DiskMode</a>" : <i>String</i>,
        "<a href="#disktype" title="DiskType">DiskType</a>" : <i>String</i>,
        "<a href="#limitiops" title="LimitIops">LimitIops</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#provisioningtype" title="ProvisioningType">ProvisioningType</a>" : <i>String</i>,
        "<a href="#regionid" title="RegionId">RegionId</a>" : <i>String</i>,
        "<a href="#shares" title="Shares">Shares</a>" : <i>String</i>,
        "<a href="#shareslevel" title="SharesLevel">SharesLevel</a>" : <i>String</i>,
        "<a href="#storagepolicyid" title="StoragePolicyId">StoragePolicyId</a>" : <i>String</i>,
        "<a href="#supportsencryption" title="SupportsEncryption">SupportsEncryption</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::VRA::StorageProfileVsphere
Properties:
    <a href="#datastoreid" title="DatastoreId">DatastoreId</a>: <i>String</i>
    <a href="#defaultitem" title="DefaultItem">DefaultItem</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#diskmode" title="DiskMode">DiskMode</a>: <i>String</i>
    <a href="#disktype" title="DiskType">DiskType</a>: <i>String</i>
    <a href="#limitiops" title="LimitIops">LimitIops</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#provisioningtype" title="ProvisioningType">ProvisioningType</a>: <i>String</i>
    <a href="#regionid" title="RegionId">RegionId</a>: <i>String</i>
    <a href="#shares" title="Shares">Shares</a>: <i>String</i>
    <a href="#shareslevel" title="SharesLevel">SharesLevel</a>: <i>String</i>
    <a href="#storagepolicyid" title="StoragePolicyId">StoragePolicyId</a>: <i>String</i>
    <a href="#supportsencryption" title="SupportsEncryption">SupportsEncryption</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
</pre>

## Properties

#### DatastoreId

Id of the vSphere Datastore for placing disk and VM.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultItem

Indicates if this storage profile is a default profile.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A human-friendly description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskMode

Type of mode for the disk.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskType

Indicates the performance tier for the storage type. Premium disks are SSD backed and Standard disks are HDD backed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LimitIops

The upper bound for the I/O operations per second allocated for each virtual disk.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A human-friendly name used as an identifier in APIs that support this option.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProvisioningType

Type of provisioning policy for the disk.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegionId

The Id of the region that is associated with the storage profile.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shares

A specific number of shares assigned to each virtual machine.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharesLevel

Indicates whether this storage profile supports encryption or not.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StoragePolicyId

Id of the vSphere Storage Policy to be applied.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SupportsEncryption

Indicates whether this storage policy should support encryption or not.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CloudAccountId

Returns the <code>CloudAccountId</code> value.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### ExternalRegionId

Returns the <code>ExternalRegionId</code> value.

#### Id

Returns the <code>Id</code> value.

#### Links

Returns the <code>Links</code> value.

#### OrgId

Returns the <code>OrgId</code> value.

#### Owner

Returns the <code>Owner</code> value.

#### UpdatedAt

Returns the <code>UpdatedAt</code> value.

