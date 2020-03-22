# Terraform::VSphere::NasDatastore

The `vsphere_nas_datastore` resource can be used to create and manage NAS
datastores on an ESXi host or a set of hosts. The resource supports mounting
NFS v3 and v4.1 shares to be used as datastores.

~> **NOTE:** Unlike [`vsphere_vmfs_datastore`][resource-vmfs-datastore], a NAS
datastore is only mounted on the hosts you choose to mount it on. To mount on
multiple hosts, you must specify each host that you want to add in the
`host_system_ids` argument.

[resource-vmfs-datastore]: /docs/providers/vsphere/r/vmfs_datastore.html

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VSphere::NasDatastore",
    "Properties" : {
        "<a href="#accessmode" title="AccessMode">AccessMode</a>" : <i>String</i>,
        "<a href="#customattributes" title="CustomAttributes">CustomAttributes</a>" : <i>[ <a href="customattributes.md">CustomAttributes</a>, ... ]</i>,
        "<a href="#datastoreclusterid" title="DatastoreClusterId">DatastoreClusterId</a>" : <i>String</i>,
        "<a href="#folder" title="Folder">Folder</a>" : <i>String</i>,
        "<a href="#hostsystemids" title="HostSystemIds">HostSystemIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#remotehosts" title="RemoteHosts">RemoteHosts</a>" : <i>[ String, ... ]</i>,
        "<a href="#remotepath" title="RemotePath">RemotePath</a>" : <i>String</i>,
        "<a href="#securitytype" title="SecurityType">SecurityType</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VSphere::NasDatastore
Properties:
    <a href="#accessmode" title="AccessMode">AccessMode</a>: <i>String</i>
    <a href="#customattributes" title="CustomAttributes">CustomAttributes</a>: <i>
      - <a href="customattributes.md">CustomAttributes</a></i>
    <a href="#datastoreclusterid" title="DatastoreClusterId">DatastoreClusterId</a>: <i>String</i>
    <a href="#folder" title="Folder">Folder</a>: <i>String</i>
    <a href="#hostsystemids" title="HostSystemIds">HostSystemIds</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#remotehosts" title="RemoteHosts">RemoteHosts</a>: <i>
      - String</i>
    <a href="#remotepath" title="RemotePath">RemotePath</a>: <i>String</i>
    <a href="#securitytype" title="SecurityType">SecurityType</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### AccessMode

Access mode for the mount point. Can be one of
`readOnly` or `readWrite`. Note that `readWrite` does not necessarily mean
that the datastore will be read-write depending on the permissions of the
actual share. Default: `readWrite`. Forces a new resource if changed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomAttributes

Map of custom attribute ids to attribute
value strings to set on datasource resource. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.

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

#### HostSystemIds

The [managed object IDs][docs-about-morefs] of
the hosts to mount the datastore on.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the datastore. Forces a new resource if
changed.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteHosts

The hostnames or IP addresses of the remote
server or servers. Only one element should be present for NFS v3 but multiple
can be present for NFS v4.1. Forces a new resource if changed.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemotePath

The remote path of the mount point. Forces a new
resource if changed.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityType

The security type to use when using NFS v4.1.
Can be one of `AUTH_SYS`, `SEC_KRB5`, or `SEC_KRB5I`. Forces a new resource
if changed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of NAS volume. Can be one of `NFS` (to denote
v3) or `NFS41` (to denote NFS v4.1). Default: `NFS`. Forces a new resource if
changed.

_Required_: No

_Type_: String

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

#### ProtocolEndpoint

Returns the <code>ProtocolEndpoint</code> value.

#### UncommittedSpace

Returns the <code>UncommittedSpace</code> value.

#### Url

Returns the <code>Url</code> value.

