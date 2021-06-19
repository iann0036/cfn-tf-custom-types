# TF::Equinix::NetworkDevice

Resource `equinix_network_device` allows creation and management of Equinix Network
Edge virtual network devices.

Network Edge virtual network devices can be created in two modes:

* **managed** (default) where Equinix manages connectivity and services in the
device and customer gets limited access to the device
* **self-configured** where customer provisions and manages own services in the device
with less restricted access. Some device types are offered only in this mode

In addition to management modes, there are two software license modes available:

* **subscription**  where Equinix provides software license, including end-to-end
support, and bills for the service respectively.
* **BYOL** [bring your own license] where customer brings his own, already procured
device software license. There are no charges associated with such license.
It is the only licensing mode for *self-configured* devices

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Equinix::NetworkDevice",
    "Properties" : {
        "<a href="#accountnumber" title="AccountNumber">AccountNumber</a>" : <i>String</i>,
        "<a href="#acltemplateid" title="AclTemplateId">AclTemplateId</a>" : <i>String</i>,
        "<a href="#additionalbandwidth" title="AdditionalBandwidth">AdditionalBandwidth</a>" : <i>Double</i>,
        "<a href="#byol" title="Byol">Byol</a>" : <i>Boolean</i>,
        "<a href="#corecount" title="CoreCount">CoreCount</a>" : <i>Double</i>,
        "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
        "<a href="#interfacecount" title="InterfaceCount">InterfaceCount</a>" : <i>Double</i>,
        "<a href="#licensefile" title="LicenseFile">LicenseFile</a>" : <i>String</i>,
        "<a href="#licensetoken" title="LicenseToken">LicenseToken</a>" : <i>String</i>,
        "<a href="#metrocode" title="MetroCode">MetroCode</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notifications" title="Notifications">Notifications</a>" : <i>[ String, ... ]</i>,
        "<a href="#orderreference" title="OrderReference">OrderReference</a>" : <i>String</i>,
        "<a href="#packagecode" title="PackageCode">PackageCode</a>" : <i>String</i>,
        "<a href="#purchaseordernumber" title="PurchaseOrderNumber">PurchaseOrderNumber</a>" : <i>String</i>,
        "<a href="#selfmanaged" title="SelfManaged">SelfManaged</a>" : <i>Boolean</i>,
        "<a href="#termlength" title="TermLength">TermLength</a>" : <i>Double</i>,
        "<a href="#throughput" title="Throughput">Throughput</a>" : <i>Double</i>,
        "<a href="#throughputunit" title="ThroughputUnit">ThroughputUnit</a>" : <i>String</i>,
        "<a href="#typecode" title="TypeCode">TypeCode</a>" : <i>String</i>,
        "<a href="#vendorconfiguration" title="VendorConfiguration">VendorConfiguration</a>" : <i>[ <a href="vendorconfigurationdefinition.md">VendorConfigurationDefinition</a>, ... ]</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>,
        "<a href="#secondarydevice" title="SecondaryDevice">SecondaryDevice</a>" : <i>[ <a href="secondarydevicedefinition.md">SecondaryDeviceDefinition</a>, ... ]</i>,
        "<a href="#sshkey" title="SshKey">SshKey</a>" : <i>[ <a href="sshkeydefinition.md">SshKeyDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Equinix::NetworkDevice
Properties:
    <a href="#accountnumber" title="AccountNumber">AccountNumber</a>: <i>String</i>
    <a href="#acltemplateid" title="AclTemplateId">AclTemplateId</a>: <i>String</i>
    <a href="#additionalbandwidth" title="AdditionalBandwidth">AdditionalBandwidth</a>: <i>Double</i>
    <a href="#byol" title="Byol">Byol</a>: <i>Boolean</i>
    <a href="#corecount" title="CoreCount">CoreCount</a>: <i>Double</i>
    <a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
    <a href="#interfacecount" title="InterfaceCount">InterfaceCount</a>: <i>Double</i>
    <a href="#licensefile" title="LicenseFile">LicenseFile</a>: <i>String</i>
    <a href="#licensetoken" title="LicenseToken">LicenseToken</a>: <i>String</i>
    <a href="#metrocode" title="MetroCode">MetroCode</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notifications" title="Notifications">Notifications</a>: <i>
      - String</i>
    <a href="#orderreference" title="OrderReference">OrderReference</a>: <i>String</i>
    <a href="#packagecode" title="PackageCode">PackageCode</a>: <i>String</i>
    <a href="#purchaseordernumber" title="PurchaseOrderNumber">PurchaseOrderNumber</a>: <i>String</i>
    <a href="#selfmanaged" title="SelfManaged">SelfManaged</a>: <i>Boolean</i>
    <a href="#termlength" title="TermLength">TermLength</a>: <i>Double</i>
    <a href="#throughput" title="Throughput">Throughput</a>: <i>Double</i>
    <a href="#throughputunit" title="ThroughputUnit">ThroughputUnit</a>: <i>String</i>
    <a href="#typecode" title="TypeCode">TypeCode</a>: <i>String</i>
    <a href="#vendorconfiguration" title="VendorConfiguration">VendorConfiguration</a>: <i>
      - <a href="vendorconfigurationdefinition.md">VendorConfigurationDefinition</a></i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
    <a href="#secondarydevice" title="SecondaryDevice">SecondaryDevice</a>: <i>
      - <a href="secondarydevicedefinition.md">SecondaryDeviceDefinition</a></i>
    <a href="#sshkey" title="SshKey">SshKey</a>: <i>
      - <a href="sshkeydefinition.md">SshKeyDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AccountNumber

Billing account number for a device.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AclTemplateId

Identifier of an ACL template that
will be applied on the device.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalBandwidth

Additional Internet bandwidth, in Mbps,
that will be allocated to the device (in addition to default 15Mbps).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Byol

Boolean value that determines device licensing mode:
*bring your own license* or *subscription* (default).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoreCount

Number of CPU cores used by device,.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

Device hostname prefix.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterfaceCount

Number of network interfaces on a device. If not
specified, default number for a given device type will be used.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseFile

Path to the license file that will be uploaded and
applied on a device. Applicable for some devices types in BYOL licensing mode.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseToken

License Token applicable for some device types
in BYOL licensing mode.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetroCode

Device location metro code.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Device name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notifications

List of email addresses that will receive device
status notifications.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrderReference

Name/number used to identify device order on
the invoice.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PackageCode

Device software package code.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PurchaseOrderNumber

Purchase order number associated
with a device order.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SelfManaged

Boolean value that determines device management mode:
*self-managed* or *Equinix managed* (default).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TermLength

Device term length.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Throughput

Device license throughput.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThroughputUnit

License throughput unit (Mbps or Gbps).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TypeCode

Device type code.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VendorConfiguration

map of vendor specific configuration parameters
for a device.

_Required_: No

_Type_: List of <a href="vendorconfigurationdefinition.md">VendorConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

Device software software version.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryDevice

_Required_: No

_Type_: List of <a href="secondarydevicedefinition.md">SecondaryDeviceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKey

_Required_: No

_Type_: List of <a href="sshkeydefinition.md">SshKeyDefinition</a>

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

#### Asn

Returns the <code>Asn</code> value.

#### Ibx

Returns the <code>Ibx</code> value.

#### Id

Returns the <code>Id</code> value.

#### Interface

Returns the <code>Interface</code> value.

#### LicenseFileId

Returns the <code>LicenseFileId</code> value.

#### LicenseStatus

Returns the <code>LicenseStatus</code> value.

#### RedundancyType

Returns the <code>RedundancyType</code> value.

#### RedundantId

Returns the <code>RedundantId</code> value.

#### Region

Returns the <code>Region</code> value.

#### SshIpAddress

Returns the <code>SshIpAddress</code> value.

#### SshIpFqdn

Returns the <code>SshIpFqdn</code> value.

#### Status

Returns the <code>Status</code> value.

#### Uuid

Returns the <code>Uuid</code> value.

#### ZoneCode

Returns the <code>ZoneCode</code> value.

