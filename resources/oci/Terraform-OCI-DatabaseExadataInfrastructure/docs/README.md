# Terraform::OCI::DatabaseExadataInfrastructure

This resource provides the Exadata Infrastructure resource in Oracle Cloud Infrastructure Database service.

Create Exadata infrastructure.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::DatabaseExadataInfrastructure",
    "Properties" : {
        "<a href="#activationfile" title="ActivationFile">ActivationFile</a>" : <i>String</i>,
        "<a href="#adminnetworkcidr" title="AdminNetworkCidr">AdminNetworkCidr</a>" : <i>String</i>,
        "<a href="#cloudcontrolplaneserver1" title="CloudControlPlaneServer1">CloudControlPlaneServer1</a>" : <i>String</i>,
        "<a href="#cloudcontrolplaneserver2" title="CloudControlPlaneServer2">CloudControlPlaneServer2</a>" : <i>String</i>,
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#corporateproxy" title="CorporateProxy">CorporateProxy</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtags.md">DefinedTags</a>, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#dnsserver" title="DnsServer">DnsServer</a>" : <i>[ String, ... ]</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtags.md">FreeformTags</a>, ... ]</i>,
        "<a href="#gateway" title="Gateway">Gateway</a>" : <i>String</i>,
        "<a href="#infinibandnetworkcidr" title="InfiniBandNetworkCidr">InfiniBandNetworkCidr</a>" : <i>String</i>,
        "<a href="#netmask" title="Netmask">Netmask</a>" : <i>String</i>,
        "<a href="#ntpserver" title="NtpServer">NtpServer</a>" : <i>[ String, ... ]</i>,
        "<a href="#shape" title="Shape">Shape</a>" : <i>String</i>,
        "<a href="#timezone" title="TimeZone">TimeZone</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::DatabaseExadataInfrastructure
Properties:
    <a href="#activationfile" title="ActivationFile">ActivationFile</a>: <i>String</i>
    <a href="#adminnetworkcidr" title="AdminNetworkCidr">AdminNetworkCidr</a>: <i>String</i>
    <a href="#cloudcontrolplaneserver1" title="CloudControlPlaneServer1">CloudControlPlaneServer1</a>: <i>String</i>
    <a href="#cloudcontrolplaneserver2" title="CloudControlPlaneServer2">CloudControlPlaneServer2</a>: <i>String</i>
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#corporateproxy" title="CorporateProxy">CorporateProxy</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtags.md">DefinedTags</a></i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#dnsserver" title="DnsServer">DnsServer</a>: <i>
      - String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtags.md">FreeformTags</a></i>
    <a href="#gateway" title="Gateway">Gateway</a>: <i>String</i>
    <a href="#infinibandnetworkcidr" title="InfiniBandNetworkCidr">InfiniBandNetworkCidr</a>: <i>String</i>
    <a href="#netmask" title="Netmask">Netmask</a>: <i>String</i>
    <a href="#ntpserver" title="NtpServer">NtpServer</a>: <i>
      - String</i>
    <a href="#shape" title="Shape">Shape</a>: <i>String</i>
    <a href="#timezone" title="TimeZone">TimeZone</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### ActivationFile

The activation zip file. If provided in config, exadata infrastructure will be activated after creation. Updates are not allowed on activated exadata infrastructure.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminNetworkCidr

(Updatable) The CIDR block for the Exadata administration network.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudControlPlaneServer1

(Updatable) The IP address for the first control plane server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudControlPlaneServer2

(Updatable) The IP address for the second control plane server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompartmentId

(Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CorporateProxy

(Updatable) The corporate network proxy for access to the control plane network. Oracle recommends using an HTTPS proxy when possible for enhanced security.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

(Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

_Required_: No

_Type_: List of <a href="definedtags.md">DefinedTags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

The user-friendly name for the Exadata infrastructure. The name does not need to be unique.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsServer

(Updatable) The list of DNS server IP addresses. Maximum of 3 allowed.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

(Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

_Required_: No

_Type_: List of <a href="freeformtags.md">FreeformTags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gateway

(Updatable) The gateway for the control plane network.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InfiniBandNetworkCidr

(Updatable) The CIDR block for the Exadata InfiniBand interconnect.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Netmask

(Updatable) The netmask for the control plane network.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NtpServer

(Updatable) The list of NTP server IP addresses. Maximum of 3 allowed.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shape

The shape of the Exadata infrastructure. The shape determines the amount of CPU, storage, and memory resources allocated to the instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeZone

(Updatable) The time zone of the Exadata infrastructure. For details, see [Exadata Infrastructure Time Zones](https://docs.cloud.oracle.com/iaas/Content/Database/References/timezones.htm).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CpusEnabled

Returns the <code>CpusEnabled</code> value.

#### DataStorageSizeInTbs

Returns the <code>DataStorageSizeInTbs</code> value.

#### Id

Returns the <code>Id</code> value.

#### LifecycleDetails

Returns the <code>LifecycleDetails</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

