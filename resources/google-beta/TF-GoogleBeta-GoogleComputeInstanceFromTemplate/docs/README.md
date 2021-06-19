# TF::GoogleBeta::GoogleComputeInstanceFromTemplate

CloudFormation equivalent of google_compute_instance_from_template

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleComputeInstanceFromTemplate",
    "Properties" : {
        "<a href="#allowstoppingforupdate" title="AllowStoppingForUpdate">AllowStoppingForUpdate</a>" : <i>Boolean</i>,
        "<a href="#attacheddisk" title="AttachedDisk">AttachedDisk</a>" : <i>[ <a href="attacheddiskdefinition.md">AttachedDiskDefinition</a>, ... ]</i>,
        "<a href="#canipforward" title="CanIpForward">CanIpForward</a>" : <i>Boolean</i>,
        "<a href="#deletionprotection" title="DeletionProtection">DeletionProtection</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#desiredstatus" title="DesiredStatus">DesiredStatus</a>" : <i>String</i>,
        "<a href="#enabledisplay" title="EnableDisplay">EnableDisplay</a>" : <i>Boolean</i>,
        "<a href="#guestaccelerator" title="GuestAccelerator">GuestAccelerator</a>" : <i>[ <a href="guestacceleratordefinition.md">GuestAcceleratorDefinition</a>, ... ]</i>,
        "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#machinetype" title="MachineType">MachineType</a>" : <i>String</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadatadefinition.md">MetadataDefinition</a>, ... ]</i>,
        "<a href="#metadatastartupscript" title="MetadataStartupScript">MetadataStartupScript</a>" : <i>String</i>,
        "<a href="#mincpuplatform" title="MinCpuPlatform">MinCpuPlatform</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#resourcepolicies" title="ResourcePolicies">ResourcePolicies</a>" : <i>[ String, ... ]</i>,
        "<a href="#scratchdisk" title="ScratchDisk">ScratchDisk</a>" : <i>[ <a href="scratchdiskdefinition.md">ScratchDiskDefinition</a>, ... ]</i>,
        "<a href="#serviceaccount" title="ServiceAccount">ServiceAccount</a>" : <i>[ <a href="serviceaccountdefinition.md">ServiceAccountDefinition</a>, ... ]</i>,
        "<a href="#sourceinstancetemplate" title="SourceInstanceTemplate">SourceInstanceTemplate</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>,
        "<a href="#bootdisk" title="BootDisk">BootDisk</a>" : <i>[ <a href="bootdiskdefinition.md">BootDiskDefinition</a>, ... ]</i>,
        "<a href="#confidentialinstanceconfig" title="ConfidentialInstanceConfig">ConfidentialInstanceConfig</a>" : <i>[ <a href="confidentialinstanceconfigdefinition.md">ConfidentialInstanceConfigDefinition</a>, ... ]</i>,
        "<a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>" : <i>[ <a href="networkinterfacedefinition.md">NetworkInterfaceDefinition</a>, ... ]</i>,
        "<a href="#reservationaffinity" title="ReservationAffinity">ReservationAffinity</a>" : <i>[ <a href="reservationaffinitydefinition.md">ReservationAffinityDefinition</a>, ... ]</i>,
        "<a href="#scheduling" title="Scheduling">Scheduling</a>" : <i>[ <a href="schedulingdefinition.md">SchedulingDefinition</a>, ... ]</i>,
        "<a href="#shieldedinstanceconfig" title="ShieldedInstanceConfig">ShieldedInstanceConfig</a>" : <i>[ <a href="shieldedinstanceconfigdefinition.md">ShieldedInstanceConfigDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GoogleBeta::GoogleComputeInstanceFromTemplate
Properties:
    <a href="#allowstoppingforupdate" title="AllowStoppingForUpdate">AllowStoppingForUpdate</a>: <i>Boolean</i>
    <a href="#attacheddisk" title="AttachedDisk">AttachedDisk</a>: <i>
      - <a href="attacheddiskdefinition.md">AttachedDiskDefinition</a></i>
    <a href="#canipforward" title="CanIpForward">CanIpForward</a>: <i>Boolean</i>
    <a href="#deletionprotection" title="DeletionProtection">DeletionProtection</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#desiredstatus" title="DesiredStatus">DesiredStatus</a>: <i>String</i>
    <a href="#enabledisplay" title="EnableDisplay">EnableDisplay</a>: <i>Boolean</i>
    <a href="#guestaccelerator" title="GuestAccelerator">GuestAccelerator</a>: <i>
      - <a href="guestacceleratordefinition.md">GuestAcceleratorDefinition</a></i>
    <a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#machinetype" title="MachineType">MachineType</a>: <i>String</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadatadefinition.md">MetadataDefinition</a></i>
    <a href="#metadatastartupscript" title="MetadataStartupScript">MetadataStartupScript</a>: <i>String</i>
    <a href="#mincpuplatform" title="MinCpuPlatform">MinCpuPlatform</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#resourcepolicies" title="ResourcePolicies">ResourcePolicies</a>: <i>
      - String</i>
    <a href="#scratchdisk" title="ScratchDisk">ScratchDisk</a>: <i>
      - <a href="scratchdiskdefinition.md">ScratchDiskDefinition</a></i>
    <a href="#serviceaccount" title="ServiceAccount">ServiceAccount</a>: <i>
      - <a href="serviceaccountdefinition.md">ServiceAccountDefinition</a></i>
    <a href="#sourceinstancetemplate" title="SourceInstanceTemplate">SourceInstanceTemplate</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
    <a href="#bootdisk" title="BootDisk">BootDisk</a>: <i>
      - <a href="bootdiskdefinition.md">BootDiskDefinition</a></i>
    <a href="#confidentialinstanceconfig" title="ConfidentialInstanceConfig">ConfidentialInstanceConfig</a>: <i>
      - <a href="confidentialinstanceconfigdefinition.md">ConfidentialInstanceConfigDefinition</a></i>
    <a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>: <i>
      - <a href="networkinterfacedefinition.md">NetworkInterfaceDefinition</a></i>
    <a href="#reservationaffinity" title="ReservationAffinity">ReservationAffinity</a>: <i>
      - <a href="reservationaffinitydefinition.md">ReservationAffinityDefinition</a></i>
    <a href="#scheduling" title="Scheduling">Scheduling</a>: <i>
      - <a href="schedulingdefinition.md">SchedulingDefinition</a></i>
    <a href="#shieldedinstanceconfig" title="ShieldedInstanceConfig">ShieldedInstanceConfig</a>: <i>
      - <a href="shieldedinstanceconfigdefinition.md">ShieldedInstanceConfigDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AllowStoppingForUpdate

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AttachedDisk

_Required_: No

_Type_: List of <a href="attacheddiskdefinition.md">AttachedDiskDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CanIpForward

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeletionProtection

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredStatus

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableDisplay

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestAccelerator

_Required_: No

_Type_: List of <a href="guestacceleratordefinition.md">GuestAcceleratorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MachineType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of <a href="metadatadefinition.md">MetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetadataStartupScript

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinCpuPlatform

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourcePolicies

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScratchDisk

_Required_: No

_Type_: List of <a href="scratchdiskdefinition.md">ScratchDiskDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccount

_Required_: No

_Type_: List of <a href="serviceaccountdefinition.md">ServiceAccountDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceInstanceTemplate

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootDisk

_Required_: No

_Type_: List of <a href="bootdiskdefinition.md">BootDiskDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfidentialInstanceConfig

_Required_: No

_Type_: List of <a href="confidentialinstanceconfigdefinition.md">ConfidentialInstanceConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInterface

_Required_: No

_Type_: List of <a href="networkinterfacedefinition.md">NetworkInterfaceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReservationAffinity

_Required_: No

_Type_: List of <a href="reservationaffinitydefinition.md">ReservationAffinityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scheduling

_Required_: No

_Type_: List of <a href="schedulingdefinition.md">SchedulingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShieldedInstanceConfig

_Required_: No

_Type_: List of <a href="shieldedinstanceconfigdefinition.md">ShieldedInstanceConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CpuPlatform

Returns the <code>CpuPlatform</code> value.

#### CurrentStatus

Returns the <code>CurrentStatus</code> value.

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

