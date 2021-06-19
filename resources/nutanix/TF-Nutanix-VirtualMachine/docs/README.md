# TF::Nutanix::VirtualMachine

Provides a Nutanix Virtual Machine resource to Create a virtual machine.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Nutanix::VirtualMachine",
    "Properties" : {
        "<a href="#availabilityzonereference" title="AvailabilityZoneReference">AvailabilityZoneReference</a>" : <i>[ <a href="availabilityzonereferencedefinition.md">AvailabilityZoneReferenceDefinition</a>, ... ]</i>,
        "<a href="#bootdevicediskaddress" title="BootDeviceDiskAddress">BootDeviceDiskAddress</a>" : <i>[ <a href="bootdevicediskaddressdefinition.md">BootDeviceDiskAddressDefinition</a>, ... ]</i>,
        "<a href="#bootdevicemacaddress" title="BootDeviceMacAddress">BootDeviceMacAddress</a>" : <i>String</i>,
        "<a href="#bootdeviceorderlist" title="BootDeviceOrderList">BootDeviceOrderList</a>" : <i>[ String, ... ]</i>,
        "<a href="#boottype" title="BootType">BootType</a>" : <i>String</i>,
        "<a href="#cloudinitcdromuuid" title="CloudInitCdromUuid">CloudInitCdromUuid</a>" : <i>String</i>,
        "<a href="#clusteruuid" title="ClusterUuid">ClusterUuid</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enablescriptexec" title="EnableScriptExec">EnableScriptExec</a>" : <i>Boolean</i>,
        "<a href="#guestcustomizationcloudinitcustomkeyvalues" title="GuestCustomizationCloudInitCustomKeyValues">GuestCustomizationCloudInitCustomKeyValues</a>" : <i>[ <a href="guestcustomizationcloudinitcustomkeyvaluesdefinition.md">GuestCustomizationCloudInitCustomKeyValuesDefinition</a>, ... ]</i>,
        "<a href="#guestcustomizationcloudinitmetadata" title="GuestCustomizationCloudInitMetaData">GuestCustomizationCloudInitMetaData</a>" : <i>String</i>,
        "<a href="#guestcustomizationcloudinituserdata" title="GuestCustomizationCloudInitUserData">GuestCustomizationCloudInitUserData</a>" : <i>String</i>,
        "<a href="#guestcustomizationisoverridable" title="GuestCustomizationIsOverridable">GuestCustomizationIsOverridable</a>" : <i>Boolean</i>,
        "<a href="#guestcustomizationsysprep" title="GuestCustomizationSysprep">GuestCustomizationSysprep</a>" : <i>[ <a href="guestcustomizationsysprepdefinition.md">GuestCustomizationSysprepDefinition</a>, ... ]</i>,
        "<a href="#guestcustomizationsysprepcustomkeyvalues" title="GuestCustomizationSysprepCustomKeyValues">GuestCustomizationSysprepCustomKeyValues</a>" : <i>[ <a href="guestcustomizationsysprepcustomkeyvaluesdefinition.md">GuestCustomizationSysprepCustomKeyValuesDefinition</a>, ... ]</i>,
        "<a href="#guestosid" title="GuestOsId">GuestOsId</a>" : <i>String</i>,
        "<a href="#hardwareclocktimezone" title="HardwareClockTimezone">HardwareClockTimezone</a>" : <i>String</i>,
        "<a href="#machinetype" title="MachineType">MachineType</a>" : <i>String</i>,
        "<a href="#memorysizemib" title="MemorySizeMib">MemorySizeMib</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ngtcredentials" title="NgtCredentials">NgtCredentials</a>" : <i>[ <a href="ngtcredentialsdefinition.md">NgtCredentialsDefinition</a>, ... ]</i>,
        "<a href="#ngtenabledcapabilitylist" title="NgtEnabledCapabilityList">NgtEnabledCapabilityList</a>" : <i>[ String, ... ]</i>,
        "<a href="#numsockets" title="NumSockets">NumSockets</a>" : <i>Double</i>,
        "<a href="#numvcpuspersocket" title="NumVcpusPerSocket">NumVcpusPerSocket</a>" : <i>Double</i>,
        "<a href="#numvnumanodes" title="NumVnumaNodes">NumVnumaNodes</a>" : <i>Double</i>,
        "<a href="#nutanixguesttools" title="NutanixGuestTools">NutanixGuestTools</a>" : <i>[ <a href="nutanixguesttoolsdefinition.md">NutanixGuestToolsDefinition</a>, ... ]</i>,
        "<a href="#ownerreference" title="OwnerReference">OwnerReference</a>" : <i>[ <a href="ownerreferencedefinition.md">OwnerReferenceDefinition</a>, ... ]</i>,
        "<a href="#parentreference" title="ParentReference">ParentReference</a>" : <i>[ <a href="parentreferencedefinition.md">ParentReferenceDefinition</a>, ... ]</i>,
        "<a href="#powerstatemechanism" title="PowerStateMechanism">PowerStateMechanism</a>" : <i>String</i>,
        "<a href="#projectreference" title="ProjectReference">ProjectReference</a>" : <i>[ <a href="projectreferencedefinition.md">ProjectReferenceDefinition</a>, ... ]</i>,
        "<a href="#shouldfailonscriptfailure" title="ShouldFailOnScriptFailure">ShouldFailOnScriptFailure</a>" : <i>Boolean</i>,
        "<a href="#usehotadd" title="UseHotAdd">UseHotAdd</a>" : <i>Boolean</i>,
        "<a href="#vgaconsoleenabled" title="VgaConsoleEnabled">VgaConsoleEnabled</a>" : <i>Boolean</i>,
        "<a href="#categories" title="Categories">Categories</a>" : <i>[ <a href="categoriesdefinition.md">CategoriesDefinition</a>, ... ]</i>,
        "<a href="#disklist" title="DiskList">DiskList</a>" : <i>[ <a href="disklistdefinition.md">DiskListDefinition</a>, ... ]</i>,
        "<a href="#gpulist" title="GpuList">GpuList</a>" : <i>[ <a href="gpulistdefinition.md">GpuListDefinition</a>, ... ]</i>,
        "<a href="#niclist" title="NicList">NicList</a>" : <i>[ <a href="niclistdefinition.md">NicListDefinition</a>, ... ]</i>,
        "<a href="#serialportlist" title="SerialPortList">SerialPortList</a>" : <i>[ <a href="serialportlistdefinition.md">SerialPortListDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Nutanix::VirtualMachine
Properties:
    <a href="#availabilityzonereference" title="AvailabilityZoneReference">AvailabilityZoneReference</a>: <i>
      - <a href="availabilityzonereferencedefinition.md">AvailabilityZoneReferenceDefinition</a></i>
    <a href="#bootdevicediskaddress" title="BootDeviceDiskAddress">BootDeviceDiskAddress</a>: <i>
      - <a href="bootdevicediskaddressdefinition.md">BootDeviceDiskAddressDefinition</a></i>
    <a href="#bootdevicemacaddress" title="BootDeviceMacAddress">BootDeviceMacAddress</a>: <i>String</i>
    <a href="#bootdeviceorderlist" title="BootDeviceOrderList">BootDeviceOrderList</a>: <i>
      - String</i>
    <a href="#boottype" title="BootType">BootType</a>: <i>String</i>
    <a href="#cloudinitcdromuuid" title="CloudInitCdromUuid">CloudInitCdromUuid</a>: <i>String</i>
    <a href="#clusteruuid" title="ClusterUuid">ClusterUuid</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enablescriptexec" title="EnableScriptExec">EnableScriptExec</a>: <i>Boolean</i>
    <a href="#guestcustomizationcloudinitcustomkeyvalues" title="GuestCustomizationCloudInitCustomKeyValues">GuestCustomizationCloudInitCustomKeyValues</a>: <i>
      - <a href="guestcustomizationcloudinitcustomkeyvaluesdefinition.md">GuestCustomizationCloudInitCustomKeyValuesDefinition</a></i>
    <a href="#guestcustomizationcloudinitmetadata" title="GuestCustomizationCloudInitMetaData">GuestCustomizationCloudInitMetaData</a>: <i>String</i>
    <a href="#guestcustomizationcloudinituserdata" title="GuestCustomizationCloudInitUserData">GuestCustomizationCloudInitUserData</a>: <i>String</i>
    <a href="#guestcustomizationisoverridable" title="GuestCustomizationIsOverridable">GuestCustomizationIsOverridable</a>: <i>Boolean</i>
    <a href="#guestcustomizationsysprep" title="GuestCustomizationSysprep">GuestCustomizationSysprep</a>: <i>
      - <a href="guestcustomizationsysprepdefinition.md">GuestCustomizationSysprepDefinition</a></i>
    <a href="#guestcustomizationsysprepcustomkeyvalues" title="GuestCustomizationSysprepCustomKeyValues">GuestCustomizationSysprepCustomKeyValues</a>: <i>
      - <a href="guestcustomizationsysprepcustomkeyvaluesdefinition.md">GuestCustomizationSysprepCustomKeyValuesDefinition</a></i>
    <a href="#guestosid" title="GuestOsId">GuestOsId</a>: <i>String</i>
    <a href="#hardwareclocktimezone" title="HardwareClockTimezone">HardwareClockTimezone</a>: <i>String</i>
    <a href="#machinetype" title="MachineType">MachineType</a>: <i>String</i>
    <a href="#memorysizemib" title="MemorySizeMib">MemorySizeMib</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ngtcredentials" title="NgtCredentials">NgtCredentials</a>: <i>
      - <a href="ngtcredentialsdefinition.md">NgtCredentialsDefinition</a></i>
    <a href="#ngtenabledcapabilitylist" title="NgtEnabledCapabilityList">NgtEnabledCapabilityList</a>: <i>
      - String</i>
    <a href="#numsockets" title="NumSockets">NumSockets</a>: <i>Double</i>
    <a href="#numvcpuspersocket" title="NumVcpusPerSocket">NumVcpusPerSocket</a>: <i>Double</i>
    <a href="#numvnumanodes" title="NumVnumaNodes">NumVnumaNodes</a>: <i>Double</i>
    <a href="#nutanixguesttools" title="NutanixGuestTools">NutanixGuestTools</a>: <i>
      - <a href="nutanixguesttoolsdefinition.md">NutanixGuestToolsDefinition</a></i>
    <a href="#ownerreference" title="OwnerReference">OwnerReference</a>: <i>
      - <a href="ownerreferencedefinition.md">OwnerReferenceDefinition</a></i>
    <a href="#parentreference" title="ParentReference">ParentReference</a>: <i>
      - <a href="parentreferencedefinition.md">ParentReferenceDefinition</a></i>
    <a href="#powerstatemechanism" title="PowerStateMechanism">PowerStateMechanism</a>: <i>String</i>
    <a href="#projectreference" title="ProjectReference">ProjectReference</a>: <i>
      - <a href="projectreferencedefinition.md">ProjectReferenceDefinition</a></i>
    <a href="#shouldfailonscriptfailure" title="ShouldFailOnScriptFailure">ShouldFailOnScriptFailure</a>: <i>Boolean</i>
    <a href="#usehotadd" title="UseHotAdd">UseHotAdd</a>: <i>Boolean</i>
    <a href="#vgaconsoleenabled" title="VgaConsoleEnabled">VgaConsoleEnabled</a>: <i>Boolean</i>
    <a href="#categories" title="Categories">Categories</a>: <i>
      - <a href="categoriesdefinition.md">CategoriesDefinition</a></i>
    <a href="#disklist" title="DiskList">DiskList</a>: <i>
      - <a href="disklistdefinition.md">DiskListDefinition</a></i>
    <a href="#gpulist" title="GpuList">GpuList</a>: <i>
      - <a href="gpulistdefinition.md">GpuListDefinition</a></i>
    <a href="#niclist" title="NicList">NicList</a>: <i>
      - <a href="niclistdefinition.md">NicListDefinition</a></i>
    <a href="#serialportlist" title="SerialPortList">SerialPortList</a>: <i>
      - <a href="serialportlistdefinition.md">SerialPortListDefinition</a></i>
</pre>

## Properties

#### AvailabilityZoneReference

_Required_: No

_Type_: List of <a href="availabilityzonereferencedefinition.md">AvailabilityZoneReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootDeviceDiskAddress

_Required_: No

_Type_: List of <a href="bootdevicediskaddressdefinition.md">BootDeviceDiskAddressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootDeviceMacAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootDeviceOrderList

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudInitCdromUuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterUuid

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableScriptExec

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestCustomizationCloudInitCustomKeyValues

_Required_: No

_Type_: List of <a href="guestcustomizationcloudinitcustomkeyvaluesdefinition.md">GuestCustomizationCloudInitCustomKeyValuesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestCustomizationCloudInitMetaData

The contents of the meta_data configuration for cloud-init. This can be formatted as YAML or JSON. The value must be base64 encoded.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestCustomizationCloudInitUserData

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestCustomizationIsOverridable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestCustomizationSysprep

_Required_: No

_Type_: List of <a href="guestcustomizationsysprepdefinition.md">GuestCustomizationSysprepDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestCustomizationSysprepCustomKeyValues

_Required_: No

_Type_: List of <a href="guestcustomizationsysprepcustomkeyvaluesdefinition.md">GuestCustomizationSysprepCustomKeyValuesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestOsId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HardwareClockTimezone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MachineType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemorySizeMib

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NgtCredentials

_Required_: No

_Type_: List of <a href="ngtcredentialsdefinition.md">NgtCredentialsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NgtEnabledCapabilityList

Application names that are enabled.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumSockets

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumVcpusPerSocket

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumVnumaNodes

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NutanixGuestTools

_Required_: No

_Type_: List of <a href="nutanixguesttoolsdefinition.md">NutanixGuestToolsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OwnerReference

_Required_: No

_Type_: List of <a href="ownerreferencedefinition.md">OwnerReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParentReference

_Required_: No

_Type_: List of <a href="parentreferencedefinition.md">ParentReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PowerStateMechanism

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectReference

_Required_: No

_Type_: List of <a href="projectreferencedefinition.md">ProjectReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShouldFailOnScriptFailure

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseHotAdd

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VgaConsoleEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Categories

_Required_: No

_Type_: List of <a href="categoriesdefinition.md">CategoriesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskList

_Required_: No

_Type_: List of <a href="disklistdefinition.md">DiskListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GpuList

_Required_: No

_Type_: List of <a href="gpulistdefinition.md">GpuListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NicList

_Required_: No

_Type_: List of <a href="niclistdefinition.md">NicListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SerialPortList

_Required_: No

_Type_: List of <a href="serialportlistdefinition.md">SerialPortListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ApiVersion

Returns the <code>ApiVersion</code> value.

#### ClusterName

Returns the <code>ClusterName</code> value.

#### HostReference

Returns the <code>HostReference</code> value.

#### HypervisorType

Returns the <code>HypervisorType</code> value.

#### Id

Returns the <code>Id</code> value.

#### Metadata

Returns the <code>Metadata</code> value.

#### NicListStatus

Returns the <code>NicListStatus</code> value.

#### PowerState

Returns the <code>PowerState</code> value.

#### State

Returns the <code>State</code> value.

