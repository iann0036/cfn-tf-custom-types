# Terraform::Nutanix::VirtualMachine

Provides a Nutanix Virtual Machine resource to Create a virtual machine.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Nutanix::VirtualMachine",
    "Properties" : {
        "<a href="#availabilityzonereference" title="AvailabilityZoneReference">AvailabilityZoneReference</a>" : <i>[ <a href="availabilityzonereference.md">AvailabilityZoneReference</a>, ... ]</i>,
        "<a href="#bootdevicediskaddress" title="BootDeviceDiskAddress">BootDeviceDiskAddress</a>" : <i>[ <a href="bootdevicediskaddress.md">BootDeviceDiskAddress</a>, ... ]</i>,
        "<a href="#bootdevicemacaddress" title="BootDeviceMacAddress">BootDeviceMacAddress</a>" : <i>String</i>,
        "<a href="#bootdeviceorderlist" title="BootDeviceOrderList">BootDeviceOrderList</a>" : <i>[ String, ... ]</i>,
        "<a href="#clusteruuid" title="ClusterUuid">ClusterUuid</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enablescriptexec" title="EnableScriptExec">EnableScriptExec</a>" : <i>Boolean</i>,
        "<a href="#guestcustomizationcloudinitcustomkeyvalues" title="GuestCustomizationCloudInitCustomKeyValues">GuestCustomizationCloudInitCustomKeyValues</a>" : <i>[ <a href="guestcustomizationcloudinitcustomkeyvalues.md">GuestCustomizationCloudInitCustomKeyValues</a>, ... ]</i>,
        "<a href="#guestcustomizationcloudinitmetadata" title="GuestCustomizationCloudInitMetaData">GuestCustomizationCloudInitMetaData</a>" : <i>String</i>,
        "<a href="#guestcustomizationcloudinituserdata" title="GuestCustomizationCloudInitUserData">GuestCustomizationCloudInitUserData</a>" : <i>String</i>,
        "<a href="#guestcustomizationisoverridable" title="GuestCustomizationIsOverridable">GuestCustomizationIsOverridable</a>" : <i>Boolean</i>,
        "<a href="#guestcustomizationsysprep" title="GuestCustomizationSysprep">GuestCustomizationSysprep</a>" : <i>[ <a href="guestcustomizationsysprep.md">GuestCustomizationSysprep</a>, ... ]</i>,
        "<a href="#guestcustomizationsysprepcustomkeyvalues" title="GuestCustomizationSysprepCustomKeyValues">GuestCustomizationSysprepCustomKeyValues</a>" : <i>[ <a href="guestcustomizationsysprepcustomkeyvalues.md">GuestCustomizationSysprepCustomKeyValues</a>, ... ]</i>,
        "<a href="#guestosid" title="GuestOsId">GuestOsId</a>" : <i>String</i>,
        "<a href="#hardwareclocktimezone" title="HardwareClockTimezone">HardwareClockTimezone</a>" : <i>String</i>,
        "<a href="#memorysizemib" title="MemorySizeMib">MemorySizeMib</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ngtcredentials" title="NgtCredentials">NgtCredentials</a>" : <i>[ <a href="ngtcredentials.md">NgtCredentials</a>, ... ]</i>,
        "<a href="#ngtenabledcapabilitylist" title="NgtEnabledCapabilityList">NgtEnabledCapabilityList</a>" : <i>[ String, ... ]</i>,
        "<a href="#numsockets" title="NumSockets">NumSockets</a>" : <i>Double</i>,
        "<a href="#numvcpuspersocket" title="NumVcpusPerSocket">NumVcpusPerSocket</a>" : <i>Double</i>,
        "<a href="#numvnumanodes" title="NumVnumaNodes">NumVnumaNodes</a>" : <i>Double</i>,
        "<a href="#nutanixguesttools" title="NutanixGuestTools">NutanixGuestTools</a>" : <i>[ <a href="nutanixguesttools.md">NutanixGuestTools</a>, ... ]</i>,
        "<a href="#ownerreference" title="OwnerReference">OwnerReference</a>" : <i>[ <a href="ownerreference.md">OwnerReference</a>, ... ]</i>,
        "<a href="#parentreference" title="ParentReference">ParentReference</a>" : <i>[ <a href="parentreference.md">ParentReference</a>, ... ]</i>,
        "<a href="#powerstatemechanism" title="PowerStateMechanism">PowerStateMechanism</a>" : <i>String</i>,
        "<a href="#projectreference" title="ProjectReference">ProjectReference</a>" : <i>[ <a href="projectreference.md">ProjectReference</a>, ... ]</i>,
        "<a href="#shouldfailonscriptfailure" title="ShouldFailOnScriptFailure">ShouldFailOnScriptFailure</a>" : <i>Boolean</i>,
        "<a href="#vgaconsoleenabled" title="VgaConsoleEnabled">VgaConsoleEnabled</a>" : <i>Boolean</i>,
        "<a href="#categories" title="Categories">Categories</a>" : <i>[ <a href="categories.md">Categories</a>, ... ]</i>,
        "<a href="#disklist" title="DiskList">DiskList</a>" : <i>[ <a href="disklist.md">DiskList</a>, ... ]</i>,
        "<a href="#gpulist" title="GpuList">GpuList</a>" : <i>[ <a href="gpulist.md">GpuList</a>, ... ]</i>,
        "<a href="#niclist" title="NicList">NicList</a>" : <i>[ <a href="niclist.md">NicList</a>, ... ]</i>,
        "<a href="#serialportlist" title="SerialPortList">SerialPortList</a>" : <i>[ <a href="serialportlist.md">SerialPortList</a>, ... ]</i>,
        "<a href="#deviceproperties" title="DeviceProperties">DeviceProperties</a>" : <i>[ <a href="deviceproperties.md">DeviceProperties</a>, ... ]</i>,
        "<a href="#ipendpointlist" title="IpEndpointList">IpEndpointList</a>" : <i>[ <a href="ipendpointlist.md">IpEndpointList</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Nutanix::VirtualMachine
Properties:
    <a href="#availabilityzonereference" title="AvailabilityZoneReference">AvailabilityZoneReference</a>: <i>
      - <a href="availabilityzonereference.md">AvailabilityZoneReference</a></i>
    <a href="#bootdevicediskaddress" title="BootDeviceDiskAddress">BootDeviceDiskAddress</a>: <i>
      - <a href="bootdevicediskaddress.md">BootDeviceDiskAddress</a></i>
    <a href="#bootdevicemacaddress" title="BootDeviceMacAddress">BootDeviceMacAddress</a>: <i>String</i>
    <a href="#bootdeviceorderlist" title="BootDeviceOrderList">BootDeviceOrderList</a>: <i>
      - String</i>
    <a href="#clusteruuid" title="ClusterUuid">ClusterUuid</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enablescriptexec" title="EnableScriptExec">EnableScriptExec</a>: <i>Boolean</i>
    <a href="#guestcustomizationcloudinitcustomkeyvalues" title="GuestCustomizationCloudInitCustomKeyValues">GuestCustomizationCloudInitCustomKeyValues</a>: <i>
      - <a href="guestcustomizationcloudinitcustomkeyvalues.md">GuestCustomizationCloudInitCustomKeyValues</a></i>
    <a href="#guestcustomizationcloudinitmetadata" title="GuestCustomizationCloudInitMetaData">GuestCustomizationCloudInitMetaData</a>: <i>String</i>
    <a href="#guestcustomizationcloudinituserdata" title="GuestCustomizationCloudInitUserData">GuestCustomizationCloudInitUserData</a>: <i>String</i>
    <a href="#guestcustomizationisoverridable" title="GuestCustomizationIsOverridable">GuestCustomizationIsOverridable</a>: <i>Boolean</i>
    <a href="#guestcustomizationsysprep" title="GuestCustomizationSysprep">GuestCustomizationSysprep</a>: <i>
      - <a href="guestcustomizationsysprep.md">GuestCustomizationSysprep</a></i>
    <a href="#guestcustomizationsysprepcustomkeyvalues" title="GuestCustomizationSysprepCustomKeyValues">GuestCustomizationSysprepCustomKeyValues</a>: <i>
      - <a href="guestcustomizationsysprepcustomkeyvalues.md">GuestCustomizationSysprepCustomKeyValues</a></i>
    <a href="#guestosid" title="GuestOsId">GuestOsId</a>: <i>String</i>
    <a href="#hardwareclocktimezone" title="HardwareClockTimezone">HardwareClockTimezone</a>: <i>String</i>
    <a href="#memorysizemib" title="MemorySizeMib">MemorySizeMib</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ngtcredentials" title="NgtCredentials">NgtCredentials</a>: <i>
      - <a href="ngtcredentials.md">NgtCredentials</a></i>
    <a href="#ngtenabledcapabilitylist" title="NgtEnabledCapabilityList">NgtEnabledCapabilityList</a>: <i>
      - String</i>
    <a href="#numsockets" title="NumSockets">NumSockets</a>: <i>Double</i>
    <a href="#numvcpuspersocket" title="NumVcpusPerSocket">NumVcpusPerSocket</a>: <i>Double</i>
    <a href="#numvnumanodes" title="NumVnumaNodes">NumVnumaNodes</a>: <i>Double</i>
    <a href="#nutanixguesttools" title="NutanixGuestTools">NutanixGuestTools</a>: <i>
      - <a href="nutanixguesttools.md">NutanixGuestTools</a></i>
    <a href="#ownerreference" title="OwnerReference">OwnerReference</a>: <i>
      - <a href="ownerreference.md">OwnerReference</a></i>
    <a href="#parentreference" title="ParentReference">ParentReference</a>: <i>
      - <a href="parentreference.md">ParentReference</a></i>
    <a href="#powerstatemechanism" title="PowerStateMechanism">PowerStateMechanism</a>: <i>String</i>
    <a href="#projectreference" title="ProjectReference">ProjectReference</a>: <i>
      - <a href="projectreference.md">ProjectReference</a></i>
    <a href="#shouldfailonscriptfailure" title="ShouldFailOnScriptFailure">ShouldFailOnScriptFailure</a>: <i>Boolean</i>
    <a href="#vgaconsoleenabled" title="VgaConsoleEnabled">VgaConsoleEnabled</a>: <i>Boolean</i>
    <a href="#categories" title="Categories">Categories</a>: <i>
      - <a href="categories.md">Categories</a></i>
    <a href="#disklist" title="DiskList">DiskList</a>: <i>
      - <a href="disklist.md">DiskList</a></i>
    <a href="#gpulist" title="GpuList">GpuList</a>: <i>
      - <a href="gpulist.md">GpuList</a></i>
    <a href="#niclist" title="NicList">NicList</a>: <i>
      - <a href="niclist.md">NicList</a></i>
    <a href="#serialportlist" title="SerialPortList">SerialPortList</a>: <i>
      - <a href="serialportlist.md">SerialPortList</a></i>
    <a href="#deviceproperties" title="DeviceProperties">DeviceProperties</a>: <i>
      - <a href="deviceproperties.md">DeviceProperties</a></i>
    <a href="#ipendpointlist" title="IpEndpointList">IpEndpointList</a>: <i>
      - <a href="ipendpointlist.md">IpEndpointList</a></i>
</pre>

## Properties

#### AvailabilityZoneReference

_Required_: No

_Type_: List of <a href="availabilityzonereference.md">AvailabilityZoneReference</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootDeviceDiskAddress

_Required_: No

_Type_: List of <a href="bootdevicediskaddress.md">BootDeviceDiskAddress</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootDeviceMacAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootDeviceOrderList

_Required_: No

_Type_: List of String

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

_Type_: List of <a href="guestcustomizationcloudinitcustomkeyvalues.md">GuestCustomizationCloudInitCustomKeyValues</a>

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

_Type_: List of <a href="guestcustomizationsysprep.md">GuestCustomizationSysprep</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestCustomizationSysprepCustomKeyValues

_Required_: No

_Type_: List of <a href="guestcustomizationsysprepcustomkeyvalues.md">GuestCustomizationSysprepCustomKeyValues</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestOsId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HardwareClockTimezone

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

_Type_: List of <a href="ngtcredentials.md">NgtCredentials</a>

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

_Type_: List of <a href="nutanixguesttools.md">NutanixGuestTools</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OwnerReference

_Required_: No

_Type_: List of <a href="ownerreference.md">OwnerReference</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParentReference

_Required_: No

_Type_: List of <a href="parentreference.md">ParentReference</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PowerStateMechanism

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectReference

_Required_: No

_Type_: List of <a href="projectreference.md">ProjectReference</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShouldFailOnScriptFailure

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VgaConsoleEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Categories

_Required_: No

_Type_: List of <a href="categories.md">Categories</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskList

_Required_: No

_Type_: List of <a href="disklist.md">DiskList</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GpuList

_Required_: No

_Type_: List of <a href="gpulist.md">GpuList</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NicList

_Required_: No

_Type_: List of <a href="niclist.md">NicList</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SerialPortList

_Required_: No

_Type_: List of <a href="serialportlist.md">SerialPortList</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceProperties

_Required_: No

_Type_: List of <a href="deviceproperties.md">DeviceProperties</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpEndpointList

_Required_: No

_Type_: List of <a href="ipendpointlist.md">IpEndpointList</a>

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

#### Metadata

Returns the <code>Metadata</code> value.

#### NicListStatus

Returns the <code>NicListStatus</code> value.

#### PowerState

Returns the <code>PowerState</code> value.

#### State

Returns the <code>State</code> value.

