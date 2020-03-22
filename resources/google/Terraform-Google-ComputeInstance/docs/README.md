# Terraform::Google::ComputeInstance

Manages a VM instance resource within GCE. For more information see
[the official documentation](https://cloud.google.com/compute/docs/instances)
and
[API](https://cloud.google.com/compute/docs/reference/latest/instances).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::ComputeInstance",
    "Properties" : {
        "<a href="#allowstoppingforupdate" title="AllowStoppingForUpdate">AllowStoppingForUpdate</a>" : <i>Boolean</i>,
        "<a href="#canipforward" title="CanIpForward">CanIpForward</a>" : <i>Boolean</i>,
        "<a href="#deletionprotection" title="DeletionProtection">DeletionProtection</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#desiredstatus" title="DesiredStatus">DesiredStatus</a>" : <i>String</i>,
        "<a href="#enabledisplay" title="EnableDisplay">EnableDisplay</a>" : <i>Boolean</i>,
        "<a href="#guestaccelerator" title="GuestAccelerator">GuestAccelerator</a>" : <i>[ <a href="guestaccelerator.md">GuestAccelerator</a>, ... ]</i>,
        "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labels.md">Labels</a>, ... ]</i>,
        "<a href="#machinetype" title="MachineType">MachineType</a>" : <i>String</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadata.md">Metadata</a>, ... ]</i>,
        "<a href="#metadatastartupscript" title="MetadataStartupScript">MetadataStartupScript</a>" : <i>String</i>,
        "<a href="#mincpuplatform" title="MinCpuPlatform">MinCpuPlatform</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>,
        "<a href="#attacheddisk" title="AttachedDisk">AttachedDisk</a>" : <i>[ <a href="attacheddisk.md">AttachedDisk</a>, ... ]</i>,
        "<a href="#bootdisk" title="BootDisk">BootDisk</a>" : <i>[ <a href="bootdisk.md">BootDisk</a>, ... ]</i>,
        "<a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>" : <i>[ <a href="networkinterface.md">NetworkInterface</a>, ... ]</i>,
        "<a href="#scheduling" title="Scheduling">Scheduling</a>" : <i>[ <a href="scheduling.md">Scheduling</a>, ... ]</i>,
        "<a href="#scratchdisk" title="ScratchDisk">ScratchDisk</a>" : <i>[ <a href="scratchdisk.md">ScratchDisk</a>, ... ]</i>,
        "<a href="#serviceaccount" title="ServiceAccount">ServiceAccount</a>" : <i>[ <a href="serviceaccount.md">ServiceAccount</a>, ... ]</i>,
        "<a href="#shieldedinstanceconfig" title="ShieldedInstanceConfig">ShieldedInstanceConfig</a>" : <i>[ <a href="shieldedinstanceconfig.md">ShieldedInstanceConfig</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#initializeparams" title="InitializeParams">InitializeParams</a>" : <i>[ <a href="initializeparams.md">InitializeParams</a>, ... ]</i>,
        "<a href="#accessconfig" title="AccessConfig">AccessConfig</a>" : <i>[ <a href="accessconfig.md">AccessConfig</a>, ... ]</i>,
        "<a href="#aliasiprange" title="AliasIpRange">AliasIpRange</a>" : <i>[ <a href="aliasiprange.md">AliasIpRange</a>, ... ]</i>,
        "<a href="#nodeaffinities" title="NodeAffinities">NodeAffinities</a>" : <i>[ <a href="nodeaffinities.md">NodeAffinities</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::ComputeInstance
Properties:
    <a href="#allowstoppingforupdate" title="AllowStoppingForUpdate">AllowStoppingForUpdate</a>: <i>Boolean</i>
    <a href="#canipforward" title="CanIpForward">CanIpForward</a>: <i>Boolean</i>
    <a href="#deletionprotection" title="DeletionProtection">DeletionProtection</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#desiredstatus" title="DesiredStatus">DesiredStatus</a>: <i>String</i>
    <a href="#enabledisplay" title="EnableDisplay">EnableDisplay</a>: <i>Boolean</i>
    <a href="#guestaccelerator" title="GuestAccelerator">GuestAccelerator</a>: <i>
      - <a href="guestaccelerator.md">GuestAccelerator</a></i>
    <a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labels.md">Labels</a></i>
    <a href="#machinetype" title="MachineType">MachineType</a>: <i>String</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadata.md">Metadata</a></i>
    <a href="#metadatastartupscript" title="MetadataStartupScript">MetadataStartupScript</a>: <i>String</i>
    <a href="#mincpuplatform" title="MinCpuPlatform">MinCpuPlatform</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
    <a href="#attacheddisk" title="AttachedDisk">AttachedDisk</a>: <i>
      - <a href="attacheddisk.md">AttachedDisk</a></i>
    <a href="#bootdisk" title="BootDisk">BootDisk</a>: <i>
      - <a href="bootdisk.md">BootDisk</a></i>
    <a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>: <i>
      - <a href="networkinterface.md">NetworkInterface</a></i>
    <a href="#scheduling" title="Scheduling">Scheduling</a>: <i>
      - <a href="scheduling.md">Scheduling</a></i>
    <a href="#scratchdisk" title="ScratchDisk">ScratchDisk</a>: <i>
      - <a href="scratchdisk.md">ScratchDisk</a></i>
    <a href="#serviceaccount" title="ServiceAccount">ServiceAccount</a>: <i>
      - <a href="serviceaccount.md">ServiceAccount</a></i>
    <a href="#shieldedinstanceconfig" title="ShieldedInstanceConfig">ShieldedInstanceConfig</a>: <i>
      - <a href="shieldedinstanceconfig.md">ShieldedInstanceConfig</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#initializeparams" title="InitializeParams">InitializeParams</a>: <i>
      - <a href="initializeparams.md">InitializeParams</a></i>
    <a href="#accessconfig" title="AccessConfig">AccessConfig</a>: <i>
      - <a href="accessconfig.md">AccessConfig</a></i>
    <a href="#aliasiprange" title="AliasIpRange">AliasIpRange</a>: <i>
      - <a href="aliasiprange.md">AliasIpRange</a></i>
    <a href="#nodeaffinities" title="NodeAffinities">NodeAffinities</a>: <i>
      - <a href="nodeaffinities.md">NodeAffinities</a></i>
</pre>

## Properties

#### AllowStoppingForUpdate

If true, allows Terraform to stop the instance to update its properties.
If you try to update a property that requires stopping the instance without setting this field, the update will fail.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CanIpForward

Whether to allow sending and receiving of
packets with non-matching source or destination IPs.
This defaults to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeletionProtection

Enable deletion protection on this instance. Defaults to false.
**Note:** you must disable deletion protection before removing the resource (e.g., via `terraform destroy`), or the instance cannot be deleted and the Terraform run will not complete successfully.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A brief description of this resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredStatus

Desired status of the instance. Either
`"RUNNING"` or `"TERMINATED"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableDisplay

Enable [Virtual Displays](https://cloud.google.com/compute/docs/instances/enable-instance-virtual-display#verify_display_driver) on this instance.
**Note**: [`allow_stopping_for_update`](#allow_stopping_for_update) must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestAccelerator

List of the type and count of accelerator cards attached to the instance. Structure documented below.
**Note:** GPU accelerators can only be used with [`on_host_maintenance`](#on_host_maintenance) option set to TERMINATE.
**Note**: This field uses [attr-as-block mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html) to avoid
breaking users during the 0.12 upgrade. To explicitly send a list
of zero objects you must use the following syntax:
`example=[]`
For more details about this behavior, see [this section](https://www.terraform.io/docs/configuration/attr-as-blocks.html#defining-a-fixed-object-collection-value).

_Required_: No

_Type_: List of <a href="guestaccelerator.md">GuestAccelerator</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

A custom hostname for the instance. Must be a fully qualified DNS name and RFC-1035-valid.
Valid format is a series of labels 1-63 characters long matching the regular expression `[a-z]([-a-z0-9]*[a-z0-9])`, concatenated with periods.
The entire hostname must not exceed 253 characters. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

A map of key/value label pairs to assign to the instance.

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
within the instance. Ssh keys attached in the Cloud Console will be removed.
Add them to your config in order to keep them attached to your instance.

_Required_: No

_Type_: List of <a href="metadata.md">Metadata</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetadataStartupScript

An alternative to using the
startup-script metadata key, except this one forces the instance to be
recreated (thus re-running the script) if it is changed. This replaces the
startup-script metadata key on the created instance and thus the two
mechanisms are not allowed to be used simultaneously.  Users are free to use
either mechanism - the only distinction is that this separate attribute
willl cause a recreate on modification.  On import, `metadata_startup_script`
will be set, but `metadata.startup-script` will not - if you choose to use the
other mechanism, you will see a diff immediately after import, which will cause a
destroy/recreate operation.  You may want to modify your state file manually
using `terraform state` commands, depending on your use case.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinCpuPlatform

Specifies a minimum CPU platform for the VM instance. Applicable values are the friendly names of CPU platforms, such as
`Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).
**Note**: [`allow_stopping_for_update`](#allow_stopping_for_update) must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A list of tags to attach to the instance.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

The zone that the machine should be created in.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AttachedDisk

_Required_: No

_Type_: List of <a href="attacheddisk.md">AttachedDisk</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootDisk

_Required_: No

_Type_: List of <a href="bootdisk.md">BootDisk</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInterface

_Required_: No

_Type_: List of <a href="networkinterface.md">NetworkInterface</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scheduling

_Required_: No

_Type_: List of <a href="scheduling.md">Scheduling</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScratchDisk

_Required_: No

_Type_: List of <a href="scratchdisk.md">ScratchDisk</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccount

_Required_: No

_Type_: List of <a href="serviceaccount.md">ServiceAccount</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShieldedInstanceConfig

_Required_: No

_Type_: List of <a href="shieldedinstanceconfig.md">ShieldedInstanceConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitializeParams

_Required_: No

_Type_: List of <a href="initializeparams.md">InitializeParams</a>

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

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CpuPlatform

Returns the <code>CpuPlatform</code> value.

#### Id

Returns the <code>Id</code> value.

#### InstanceId

Returns the <code>InstanceId</code> value.

#### LabelFingerprint

Returns the <code>LabelFingerprint</code> value.

#### MetadataFingerprint

Returns the <code>MetadataFingerprint</code> value.

#### SelfLink

Returns the <code>SelfLink</code> value.

#### TagsFingerprint

Returns the <code>TagsFingerprint</code> value.

