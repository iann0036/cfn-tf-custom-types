# TF::Equinix::NetworkDevice SecondaryDeviceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accountnumber" title="AccountNumber">AccountNumber</a>" : <i>String</i>,
    "<a href="#acltemplateid" title="AclTemplateId">AclTemplateId</a>" : <i>String</i>,
    "<a href="#additionalbandwidth" title="AdditionalBandwidth">AdditionalBandwidth</a>" : <i>Double</i>,
    "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
    "<a href="#licensefile" title="LicenseFile">LicenseFile</a>" : <i>String</i>,
    "<a href="#licensetoken" title="LicenseToken">LicenseToken</a>" : <i>String</i>,
    "<a href="#metrocode" title="MetroCode">MetroCode</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#notifications" title="Notifications">Notifications</a>" : <i>[ String, ... ]</i>,
    "<a href="#vendorconfiguration" title="VendorConfiguration">VendorConfiguration</a>" : <i>[ <a href="vendorconfigurationdefinition.md">VendorConfigurationDefinition</a>, ... ]</i>,
    "<a href="#sshkey" title="SshKey">SshKey</a>" : <i>[ <a href="sshkeydefinition.md">SshKeyDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#accountnumber" title="AccountNumber">AccountNumber</a>: <i>String</i>
<a href="#acltemplateid" title="AclTemplateId">AclTemplateId</a>: <i>String</i>
<a href="#additionalbandwidth" title="AdditionalBandwidth">AdditionalBandwidth</a>: <i>Double</i>
<a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
<a href="#licensefile" title="LicenseFile">LicenseFile</a>: <i>String</i>
<a href="#licensetoken" title="LicenseToken">LicenseToken</a>: <i>String</i>
<a href="#metrocode" title="MetroCode">MetroCode</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#notifications" title="Notifications">Notifications</a>: <i>
      - String</i>
<a href="#vendorconfiguration" title="VendorConfiguration">VendorConfiguration</a>: <i>
      - <a href="vendorconfigurationdefinition.md">VendorConfigurationDefinition</a></i>
<a href="#sshkey" title="SshKey">SshKey</a>: <i>
      - <a href="sshkeydefinition.md">SshKeyDefinition</a></i>
</pre>

## Properties

#### AccountNumber

Billing account number for
secondary device.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AclTemplateId

Identifier of an ACL template that will
be applied on a secondary device.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalBandwidth

Additional Internet
bandwidth, in Mbps, for a secondary device.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

Secondary device hostname.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseFile

Path to the license file that
will be uploaded and applied on a secondary device. Applicable for some devices
types in BYOL licensing mode.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseToken

License Token can be provided
for some device types o the device.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetroCode

Metro location of a secondary device.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

reference by name to previously provisioned public SSH key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notifications

List of email addresses that
will receive notifications about secondary device.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VendorConfiguration

_Required_: No

_Type_: List of <a href="vendorconfigurationdefinition.md">VendorConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKey

_Required_: No

_Type_: List of <a href="sshkeydefinition.md">SshKeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

