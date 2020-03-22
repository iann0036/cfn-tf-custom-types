# Terraform::VSphere::VmfsDatastore

The `vsphere_vmfs_datastore` resource can be used to create and manage VMFS
datastores on an ESXi host or a set of hosts. The resource supports using any
SCSI device that can generally be used in a datastore, such as local disks, or
disks presented to a host or multiple hosts over Fibre Channel or iSCSI.
Devices can be specified manually, or discovered using the
[`vsphere_vmfs_disks`][data-source-vmfs-disks] data source.

[data-source-vmfs-disks]: /docs/providers/vsphere/d/vmfs_disks.html

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VSphere::VmfsDatastore",
    "Properties" : {
        "<a href="#customattributes" title="CustomAttributes">CustomAttributes</a>" : <i>[ <a href="customattributes.md">CustomAttributes</a>, ... ]</i>,
        "<a href="#datastoreclusterid" title="DatastoreClusterId">DatastoreClusterId</a>" : <i>String</i>,
        "<a href="#disks" title="Disks">Disks</a>" : <i>[ String, ... ]</i>,
        "<a href="#folder" title="Folder">Folder</a>" : <i>String</i>,
        "<a href="#hostsystemid" title="HostSystemId">HostSystemId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VSphere::VmfsDatastore
Properties:
    <a href="#customattributes" title="CustomAttributes">CustomAttributes</a>: <i>
      - <a href="customattributes.md">CustomAttributes</a></i>
    <a href="#datastoreclusterid" title="DatastoreClusterId">DatastoreClusterId</a>: <i>String</i>
    <a href="#disks" title="Disks">Disks</a>: <i>
      - String</i>
    <a href="#folder" title="Folder">Folder</a>: <i>String</i>
    <a href="#hostsystemid" title="HostSystemId">HostSystemId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
</pre>

## Properties

#### CustomAttributes

_Required_: No

_Type_: List of <a href="customattributes.md">CustomAttributes</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatastoreClusterId

The [managed object
ID][docs-about-morefs] of a datastore cluster to put this datastore in.
Conflicts with `folder`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disks

The disks to use with the datastore.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Folder

The relative path to a folder to put this datastore in.
This is a path relative to the datacenter you are deploying the datastore to.
Example: for the `dc1` datacenter, and a provided `folder` of `foo/bar`,
Terraform will place a datastore named `terraform-test` in a datastore folder
located at `/dc1/datastore/foo/bar`, with the final inventory path being
`/dc1/datastore/foo/bar/terraform-test`. Conflicts with
`datastore_cluster_id`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostSystemId

The [managed object ID][docs-about-morefs] of
the host to set the datastore up on. Note that this is not necessarily the
only host that the datastore will be set up on - see
[here](#auto-mounting-of-datastores-within-vcenter) for more info. Forces a
new resource if changed.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the datastore. Forces a new resource if
changed.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Accessible

Returns the <code>Accessible</code> value.

#### Capacity

Returns the <code>Capacity</code> value.

#### FreeSpace

Returns the <code>FreeSpace</code> value.

#### Id

Returns the <code>Id</code> value.

#### MaintenanceMode

Returns the <code>MaintenanceMode</code> value.

#### MultipleHostAccess

Returns the <code>MultipleHostAccess</code> value.

#### UncommittedSpace

Returns the <code>UncommittedSpace</code> value.

#### Url

Returns the <code>Url</code> value.

