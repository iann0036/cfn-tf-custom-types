# Terraform::AzureRM::LinuxVirtualMachine

Manages a Linux Virtual Machine.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::LinuxVirtualMachine",
    "Properties" : {
        "<a href="#adminpassword" title="AdminPassword">AdminPassword</a>" : <i>String</i>,
        "<a href="#adminusername" title="AdminUsername">AdminUsername</a>" : <i>String</i>,
        "<a href="#allowextensionoperations" title="AllowExtensionOperations">AllowExtensionOperations</a>" : <i>Boolean</i>,
        "<a href="#availabilitysetid" title="AvailabilitySetId">AvailabilitySetId</a>" : <i>String</i>,
        "<a href="#computername" title="ComputerName">ComputerName</a>" : <i>String</i>,
        "<a href="#customdata" title="CustomData">CustomData</a>" : <i>String</i>,
        "<a href="#dedicatedhostid" title="DedicatedHostId">DedicatedHostId</a>" : <i>String</i>,
        "<a href="#disablepasswordauthentication" title="DisablePasswordAuthentication">DisablePasswordAuthentication</a>" : <i>Boolean</i>,
        "<a href="#evictionpolicy" title="EvictionPolicy">EvictionPolicy</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#maxbidprice" title="MaxBidPrice">MaxBidPrice</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkinterfaceids" title="NetworkInterfaceIds">NetworkInterfaceIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>String</i>,
        "<a href="#provisionvmagent" title="ProvisionVmAgent">ProvisionVmAgent</a>" : <i>Boolean</i>,
        "<a href="#proximityplacementgroupid" title="ProximityPlacementGroupId">ProximityPlacementGroupId</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#size" title="Size">Size</a>" : <i>String</i>,
        "<a href="#sourceimageid" title="SourceImageId">SourceImageId</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>,
        "<a href="#additionalcapabilities" title="AdditionalCapabilities">AdditionalCapabilities</a>" : <i>[ <a href="additionalcapabilities.md">AdditionalCapabilities</a>, ... ]</i>,
        "<a href="#adminsshkey" title="AdminSshKey">AdminSshKey</a>" : <i>[ <a href="adminsshkey.md">AdminSshKey</a>, ... ]</i>,
        "<a href="#bootdiagnostics" title="BootDiagnostics">BootDiagnostics</a>" : <i>[ <a href="bootdiagnostics.md">BootDiagnostics</a>, ... ]</i>,
        "<a href="#identity" title="Identity">Identity</a>" : <i>[ <a href="identity.md">Identity</a>, ... ]</i>,
        "<a href="#osdisk" title="OsDisk">OsDisk</a>" : <i>[ <a href="osdisk.md">OsDisk</a>, ... ]</i>,
        "<a href="#plan" title="Plan">Plan</a>" : <i>[ <a href="plan.md">Plan</a>, ... ]</i>,
        "<a href="#secret" title="Secret">Secret</a>" : <i>[ <a href="secret.md">Secret</a>, ... ]</i>,
        "<a href="#sourceimagereference" title="SourceImageReference">SourceImageReference</a>" : <i>[ <a href="sourceimagereference.md">SourceImageReference</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#diffdisksettings" title="DiffDiskSettings">DiffDiskSettings</a>" : <i>[ <a href="diffdisksettings.md">DiffDiskSettings</a>, ... ]</i>,
        "<a href="#certificate" title="Certificate">Certificate</a>" : <i>[ <a href="certificate.md">Certificate</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::LinuxVirtualMachine
Properties:
    <a href="#adminpassword" title="AdminPassword">AdminPassword</a>: <i>String</i>
    <a href="#adminusername" title="AdminUsername">AdminUsername</a>: <i>String</i>
    <a href="#allowextensionoperations" title="AllowExtensionOperations">AllowExtensionOperations</a>: <i>Boolean</i>
    <a href="#availabilitysetid" title="AvailabilitySetId">AvailabilitySetId</a>: <i>String</i>
    <a href="#computername" title="ComputerName">ComputerName</a>: <i>String</i>
    <a href="#customdata" title="CustomData">CustomData</a>: <i>String</i>
    <a href="#dedicatedhostid" title="DedicatedHostId">DedicatedHostId</a>: <i>String</i>
    <a href="#disablepasswordauthentication" title="DisablePasswordAuthentication">DisablePasswordAuthentication</a>: <i>Boolean</i>
    <a href="#evictionpolicy" title="EvictionPolicy">EvictionPolicy</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#maxbidprice" title="MaxBidPrice">MaxBidPrice</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkinterfaceids" title="NetworkInterfaceIds">NetworkInterfaceIds</a>: <i>
      - String</i>
    <a href="#priority" title="Priority">Priority</a>: <i>String</i>
    <a href="#provisionvmagent" title="ProvisionVmAgent">ProvisionVmAgent</a>: <i>Boolean</i>
    <a href="#proximityplacementgroupid" title="ProximityPlacementGroupId">ProximityPlacementGroupId</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#size" title="Size">Size</a>: <i>String</i>
    <a href="#sourceimageid" title="SourceImageId">SourceImageId</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
    <a href="#additionalcapabilities" title="AdditionalCapabilities">AdditionalCapabilities</a>: <i>
      - <a href="additionalcapabilities.md">AdditionalCapabilities</a></i>
    <a href="#adminsshkey" title="AdminSshKey">AdminSshKey</a>: <i>
      - <a href="adminsshkey.md">AdminSshKey</a></i>
    <a href="#bootdiagnostics" title="BootDiagnostics">BootDiagnostics</a>: <i>
      - <a href="bootdiagnostics.md">BootDiagnostics</a></i>
    <a href="#identity" title="Identity">Identity</a>: <i>
      - <a href="identity.md">Identity</a></i>
    <a href="#osdisk" title="OsDisk">OsDisk</a>: <i>
      - <a href="osdisk.md">OsDisk</a></i>
    <a href="#plan" title="Plan">Plan</a>: <i>
      - <a href="plan.md">Plan</a></i>
    <a href="#secret" title="Secret">Secret</a>: <i>
      - <a href="secret.md">Secret</a></i>
    <a href="#sourceimagereference" title="SourceImageReference">SourceImageReference</a>: <i>
      - <a href="sourceimagereference.md">SourceImageReference</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#diffdisksettings" title="DiffDiskSettings">DiffDiskSettings</a>: <i>
      - <a href="diffdisksettings.md">DiffDiskSettings</a></i>
    <a href="#certificate" title="Certificate">Certificate</a>: <i>
      - <a href="certificate.md">Certificate</a></i>
</pre>

## Properties

#### AdminPassword

The Password which should be used for the local-administrator on this Virtual Machine. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminUsername

The username of the local administrator used for the Virtual Machine. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowExtensionOperations

Should Extension Operations be allowed on this Virtual Machine? Changing this forces a new resource to be created.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilitySetId

Specifies the ID of the Availability Set in which the Virtual Machine should exist. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComputerName

Specifies the Hostname which should be used for this Virtual Machine. If unspecified this defaults to the value for the `name` field. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomData

The Base64-Encoded Custom Data which should be used for this Virtual Machine. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DedicatedHostId

The ID of a Dedicated Host where this machine should be run on. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisablePasswordAuthentication

Should Password Authentication be disabled on this Virtual Machine? Defaults to `true`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EvictionPolicy

Specifies what should happen when the Virtual Machine is evicted for price reasons when using a Spot instance. At this time the only supported value is `Deallocate`. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

The Azure location where the Linux Virtual Machine should exist. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxBidPrice

The maximum price you're willing to pay for this Virtual Machine, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machine will be evicted using the `eviction_policy`. Defaults to `-1`, which means that the Virtual Machine should not be evicted for price reasons.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Linux Virtual Machine. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInterfaceIds

. A list of Network Interface ID's which should be attached to this Virtual Machine. The first Network Interface ID in this list will be the Primary Network Interface on the Virtual Machine.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

Specifies the priority of this Virtual Machine. Possible values are `Regular` and `Spot`. Defaults to `Regular`. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProvisionVmAgent

Should the Azure VM Agent be provisioned on this Virtual Machine? Defaults to `true`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProximityPlacementGroupId

The ID of the Proximity Placement Group which the Virtual Machine should be assigned to. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the Resource Group in which the Linux Virtual Machine should be exist. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

The SKU which should be used for this Virtual Machine, such as `Standard_F2`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceImageId

The ID of the Image which this Virtual Machine should be created from. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags which should be assigned to this Virtual Machine.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

The Zone in which this Virtual Machine should be created. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalCapabilities

_Required_: No

_Type_: List of <a href="additionalcapabilities.md">AdditionalCapabilities</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminSshKey

_Required_: No

_Type_: List of <a href="adminsshkey.md">AdminSshKey</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootDiagnostics

_Required_: No

_Type_: List of <a href="bootdiagnostics.md">BootDiagnostics</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identity

_Required_: No

_Type_: List of <a href="identity.md">Identity</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsDisk

_Required_: No

_Type_: List of <a href="osdisk.md">OsDisk</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Plan

_Required_: No

_Type_: List of <a href="plan.md">Plan</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Secret

_Required_: No

_Type_: List of <a href="secret.md">Secret</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceImageReference

_Required_: No

_Type_: List of <a href="sourceimagereference.md">SourceImageReference</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiffDiskSettings

_Required_: No

_Type_: List of <a href="diffdisksettings.md">DiffDiskSettings</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Certificate

_Required_: No

_Type_: List of <a href="certificate.md">Certificate</a>

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

#### PrivateIpAddress

Returns the <code>PrivateIpAddress</code> value.

#### PrivateIpAddresses

Returns the <code>PrivateIpAddresses</code> value.

#### PublicIpAddress

Returns the <code>PublicIpAddress</code> value.

#### PublicIpAddresses

Returns the <code>PublicIpAddresses</code> value.

#### VirtualMachineId

Returns the <code>VirtualMachineId</code> value.

