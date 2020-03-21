# Terraform::Google::ComputeInstanceTemplate

Manages a VM instance template resource within GCE. For more information see
[the official documentation](https://cloud.google.com/compute/docs/instance-templates)
and
[API](https://cloud.google.com/compute/docs/reference/latest/instanceTemplates).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::ComputeInstanceTemplate",
    "Properties" : {
        "<a href="#canipforward" title="CanIpForward">CanIpForward</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enabledisplay" title="EnableDisplay">EnableDisplay</a>" : <i>Boolean</i>,
        "<a href="#instancedescription" title="InstanceDescription">InstanceDescription</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labels.md">Labels</a>, ... ]</i>,
        "<a href="#machinetype" title="MachineType">MachineType</a>" : <i>String</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadata.md">Metadata</a>, ... ]</i>,
        "<a href="#metadatastartupscript" title="MetadataStartupScript">MetadataStartupScript</a>" : <i>String</i>,
        "<a href="#mincpuplatform" title="MinCpuPlatform">MinCpuPlatform</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nameprefix" title="NamePrefix">NamePrefix</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#disk" title="Disk">Disk</a>" : <i>[ <a href="disk.md">Disk</a>, ... ]</i>,
        "<a href="#guestaccelerator" title="GuestAccelerator">GuestAccelerator</a>" : <i>[ <a href="guestaccelerator.md">GuestAccelerator</a>, ... ]</i>,
        "<a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>" : <i>[ <a href="networkinterface.md">NetworkInterface</a>, ... ]</i>,
        "<a href="#scheduling" title="Scheduling">Scheduling</a>" : <i>[ <a href="scheduling.md">Scheduling</a>, ... ]</i>,
        "<a href="#serviceaccount" title="ServiceAccount">ServiceAccount</a>" : <i>[ <a href="serviceaccount.md">ServiceAccount</a>, ... ]</i>,
        "<a href="#shieldedinstanceconfig" title="ShieldedInstanceConfig">ShieldedInstanceConfig</a>" : <i>[ <a href="shieldedinstanceconfig.md">ShieldedInstanceConfig</a>, ... ]</i>,
        "<a href="#diskencryptionkey" title="DiskEncryptionKey">DiskEncryptionKey</a>" : <i>[ <a href="diskencryptionkey.md">DiskEncryptionKey</a>, ... ]</i>,
        "<a href="#accessconfig" title="AccessConfig">AccessConfig</a>" : <i>[ <a href="accessconfig.md">AccessConfig</a>, ... ]</i>,
        "<a href="#aliasiprange" title="AliasIpRange">AliasIpRange</a>" : <i>[ <a href="aliasiprange.md">AliasIpRange</a>, ... ]</i>,
        "<a href="#nodeaffinities" title="NodeAffinities">NodeAffinities</a>" : <i>[ <a href="nodeaffinities.md">NodeAffinities</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::ComputeInstanceTemplate
Properties:
    <a href="#canipforward" title="CanIpForward">CanIpForward</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enabledisplay" title="EnableDisplay">EnableDisplay</a>: <i>Boolean</i>
    <a href="#instancedescription" title="InstanceDescription">InstanceDescription</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labels.md">Labels</a></i>
    <a href="#machinetype" title="MachineType">MachineType</a>: <i>String</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadata.md">Metadata</a></i>
    <a href="#metadatastartupscript" title="MetadataStartupScript">MetadataStartupScript</a>: <i>String</i>
    <a href="#mincpuplatform" title="MinCpuPlatform">MinCpuPlatform</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nameprefix" title="NamePrefix">NamePrefix</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#disk" title="Disk">Disk</a>: <i>
      - <a href="disk.md">Disk</a></i>
    <a href="#guestaccelerator" title="GuestAccelerator">GuestAccelerator</a>: <i>
      - <a href="guestaccelerator.md">GuestAccelerator</a></i>
    <a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>: <i>
      - <a href="networkinterface.md">NetworkInterface</a></i>
    <a href="#scheduling" title="Scheduling">Scheduling</a>: <i>
      - <a href="scheduling.md">Scheduling</a></i>
    <a href="#serviceaccount" title="ServiceAccount">ServiceAccount</a>: <i>
      - <a href="serviceaccount.md">ServiceAccount</a></i>
    <a href="#shieldedinstanceconfig" title="ShieldedInstanceConfig">ShieldedInstanceConfig</a>: <i>
      - <a href="shieldedinstanceconfig.md">ShieldedInstanceConfig</a></i>
    <a href="#diskencryptionkey" title="DiskEncryptionKey">DiskEncryptionKey</a>: <i>
      - <a href="diskencryptionkey.md">DiskEncryptionKey</a></i>
    <a href="#accessconfig" title="AccessConfig">AccessConfig</a>: <i>
      - <a href="accessconfig.md">AccessConfig</a></i>
    <a href="#aliasiprange" title="AliasIpRange">AliasIpRange</a>: <i>
      - <a href="aliasiprange.md">AliasIpRange</a></i>
    <a href="#nodeaffinities" title="NodeAffinities">NodeAffinities</a>: <i>
      - <a href="nodeaffinities.md">NodeAffinities</a></i>
</pre>

## Properties

#### CanIpForward

Whether to allow sending and receiving of
packets with non-matching source or destination IPs. This defaults to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A brief description of this resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableDisplay

Enable [Virtual Displays](https://cloud.google.com/compute/docs/instances/enable-instance-virtual-display#verify_display_driver) on this instance.
**Note**: [`allow_stopping_for_update`](#allow_stopping_for_update) must be set to true in order to update this field.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceDescription

A brief description to use for instances
created from this template.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

A set of key/value label pairs to assign to instances
created from this template,.

_Required_: No

_Type_: List of <a href="labels.md">Labels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MachineType

The machine type to create.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

Metadata key/value pairs to make available from
within instances created from this template.

_Required_: No

_Type_: List of <a href="metadata.md">Metadata</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetadataStartupScript

An alternative to using the
startup-script metadata key, mostly to match the compute_instance resource.
This replaces the startup-script metadata key on the created instance and
thus the two mechanisms are not allowed to be used simultaneously.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinCpuPlatform

Specifies a minimum CPU platform. Applicable values are the friendly names of CPU platforms, such as
`Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the instance template. If you leave
this blank, Terraform will auto-generate a unique name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamePrefix

Creates a unique name beginning with the specified
prefix. Conflicts with `name`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

An instance template is a global resource that is not
bound to a zone or a region. However, you can still specify some regional
resources in an instance template, which restricts the template to the
region where that resource resides. For example, a custom `subnetwork`
resource is tied to a specific region. Defaults to the region of the
Provider if no value is given.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Tags to attach to the instance.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disk

_Required_: No

_Type_: List of <a href="disk.md">Disk</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestAccelerator

_Required_: No

_Type_: List of <a href="guestaccelerator.md">GuestAccelerator</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInterface

_Required_: No

_Type_: List of <a href="networkinterface.md">NetworkInterface</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scheduling

_Required_: No

_Type_: List of <a href="scheduling.md">Scheduling</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccount

_Required_: No

_Type_: List of <a href="serviceaccount.md">ServiceAccount</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShieldedInstanceConfig

_Required_: No

_Type_: List of <a href="shieldedinstanceconfig.md">ShieldedInstanceConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskEncryptionKey

_Required_: No

_Type_: List of <a href="diskencryptionkey.md">DiskEncryptionKey</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessConfig

_Required_: No

_Type_: List of <a href="accessconfig.md">AccessConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AliasIpRange

_Required_: No

_Type_: List of <a href="aliasiprange.md">AliasIpRange</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeAffinities

_Required_: No

_Type_: List of <a href="nodeaffinities.md">NodeAffinities</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### MetadataFingerprint

Returns the <code>MetadataFingerprint</code> value.

#### SelfLink

Returns the <code>SelfLink</code> value.

#### TagsFingerprint

Returns the <code>TagsFingerprint</code> value.

