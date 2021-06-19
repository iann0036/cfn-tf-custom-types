# TF::OCI::DatabaseExadataInfrastructureStorage

CloudFormation equivalent of oci_database_exadata_infrastructure_storage

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::DatabaseExadataInfrastructureStorage",
    "Properties" : {
        "<a href="#activationfile" title="ActivationFile">ActivationFile</a>" : <i>String</i>,
        "<a href="#adminnetworkcidr" title="AdminNetworkCidr">AdminNetworkCidr</a>" : <i>String</i>,
        "<a href="#cloudcontrolplaneserver1" title="CloudControlPlaneServer1">CloudControlPlaneServer1</a>" : <i>String</i>,
        "<a href="#cloudcontrolplaneserver2" title="CloudControlPlaneServer2">CloudControlPlaneServer2</a>" : <i>String</i>,
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#computecount" title="ComputeCount">ComputeCount</a>" : <i>Double</i>,
        "<a href="#corporateproxy" title="CorporateProxy">CorporateProxy</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#dnsserver" title="DnsServer">DnsServer</a>" : <i>[ String, ... ]</i>,
        "<a href="#exadatainfrastructureid" title="ExadataInfrastructureId">ExadataInfrastructureId</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>, ... ]</i>,
        "<a href="#gateway" title="Gateway">Gateway</a>" : <i>String</i>,
        "<a href="#infinibandnetworkcidr" title="InfiniBandNetworkCidr">InfiniBandNetworkCidr</a>" : <i>String</i>,
        "<a href="#netmask" title="Netmask">Netmask</a>" : <i>String</i>,
        "<a href="#ntpserver" title="NtpServer">NtpServer</a>" : <i>[ String, ... ]</i>,
        "<a href="#shape" title="Shape">Shape</a>" : <i>String</i>,
        "<a href="#storagecount" title="StorageCount">StorageCount</a>" : <i>Double</i>,
        "<a href="#timezone" title="TimeZone">TimeZone</a>" : <i>String</i>,
        "<a href="#contacts" title="Contacts">Contacts</a>" : <i>[ <a href="contactsdefinition.md">ContactsDefinition</a>, ... ]</i>,
        "<a href="#maintenancewindow" title="MaintenanceWindow">MaintenanceWindow</a>" : <i>[ <a href="maintenancewindowdefinition.md">MaintenanceWindowDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::DatabaseExadataInfrastructureStorage
Properties:
    <a href="#activationfile" title="ActivationFile">ActivationFile</a>: <i>String</i>
    <a href="#adminnetworkcidr" title="AdminNetworkCidr">AdminNetworkCidr</a>: <i>String</i>
    <a href="#cloudcontrolplaneserver1" title="CloudControlPlaneServer1">CloudControlPlaneServer1</a>: <i>String</i>
    <a href="#cloudcontrolplaneserver2" title="CloudControlPlaneServer2">CloudControlPlaneServer2</a>: <i>String</i>
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#computecount" title="ComputeCount">ComputeCount</a>: <i>Double</i>
    <a href="#corporateproxy" title="CorporateProxy">CorporateProxy</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtagsdefinition.md">DefinedTagsDefinition</a></i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#dnsserver" title="DnsServer">DnsServer</a>: <i>
      - String</i>
    <a href="#exadatainfrastructureid" title="ExadataInfrastructureId">ExadataInfrastructureId</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a></i>
    <a href="#gateway" title="Gateway">Gateway</a>: <i>String</i>
    <a href="#infinibandnetworkcidr" title="InfiniBandNetworkCidr">InfiniBandNetworkCidr</a>: <i>String</i>
    <a href="#netmask" title="Netmask">Netmask</a>: <i>String</i>
    <a href="#ntpserver" title="NtpServer">NtpServer</a>: <i>
      - String</i>
    <a href="#shape" title="Shape">Shape</a>: <i>String</i>
    <a href="#storagecount" title="StorageCount">StorageCount</a>: <i>Double</i>
    <a href="#timezone" title="TimeZone">TimeZone</a>: <i>String</i>
    <a href="#contacts" title="Contacts">Contacts</a>: <i>
      - <a href="contactsdefinition.md">ContactsDefinition</a></i>
    <a href="#maintenancewindow" title="MaintenanceWindow">MaintenanceWindow</a>: <i>
      - <a href="maintenancewindowdefinition.md">MaintenanceWindowDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### ActivationFile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminNetworkCidr

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudControlPlaneServer1

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudControlPlaneServer2

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompartmentId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComputeCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CorporateProxy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

_Required_: No

_Type_: List of <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsServer

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExadataInfrastructureId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

_Required_: No

_Type_: List of <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gateway

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InfiniBandNetworkCidr

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Netmask

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NtpServer

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shape

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeZone

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Contacts

_Required_: No

_Type_: List of <a href="contactsdefinition.md">ContactsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintenanceWindow

_Required_: No

_Type_: List of <a href="maintenancewindowdefinition.md">MaintenanceWindowDefinition</a>

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

#### ActivatedStorageCount

Returns the <code>ActivatedStorageCount</code> value.

#### AdditionalStorageCount

Returns the <code>AdditionalStorageCount</code> value.

#### CpusEnabled

Returns the <code>CpusEnabled</code> value.

#### CsiNumber

Returns the <code>CsiNumber</code> value.

#### DataStorageSizeInTbs

Returns the <code>DataStorageSizeInTbs</code> value.

#### DbNodeStorageSizeInGbs

Returns the <code>DbNodeStorageSizeInGbs</code> value.

#### Id

Returns the <code>Id</code> value.

#### LifecycleDetails

Returns the <code>LifecycleDetails</code> value.

#### MaintenanceSloStatus

Returns the <code>MaintenanceSloStatus</code> value.

#### MaxCpuCount

Returns the <code>MaxCpuCount</code> value.

#### MaxDataStorageInTbs

Returns the <code>MaxDataStorageInTbs</code> value.

#### MaxDbNodeStorageInGbs

Returns the <code>MaxDbNodeStorageInGbs</code> value.

#### MaxMemoryInGbs

Returns the <code>MaxMemoryInGbs</code> value.

#### MemorySizeInGbs

Returns the <code>MemorySizeInGbs</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

