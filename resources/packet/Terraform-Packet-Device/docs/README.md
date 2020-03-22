# Terraform::Packet::Device

Provides a Packet device resource. This can be used to create,
modify, and delete devices.

~> **Note:** All arguments including the `root_password` and `user_data` will be stored in
 the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Packet::Device",
    "Properties" : {
        "<a href="#alwayspxe" title="AlwaysPxe">AlwaysPxe</a>" : <i>Boolean</i>,
        "<a href="#billingcycle" title="BillingCycle">BillingCycle</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#facilities" title="Facilities">Facilities</a>" : <i>[ String, ... ]</i>,
        "<a href="#facility" title="Facility">Facility</a>" : <i>String</i>,
        "<a href="#forcedetachvolumes" title="ForceDetachVolumes">ForceDetachVolumes</a>" : <i>Boolean</i>,
        "<a href="#hardwarereservationid" title="HardwareReservationId">HardwareReservationId</a>" : <i>String</i>,
        "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
        "<a href="#ipaddresstypes" title="IpAddressTypes">IpAddressTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#ipxescripturl" title="IpxeScriptUrl">IpxeScriptUrl</a>" : <i>String</i>,
        "<a href="#networktype" title="NetworkType">NetworkType</a>" : <i>String</i>,
        "<a href="#operatingsystem" title="OperatingSystem">OperatingSystem</a>" : <i>String</i>,
        "<a href="#plan" title="Plan">Plan</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#projectsshkeyids" title="ProjectSshKeyIds">ProjectSshKeyIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#publicipv4subnetsize" title="PublicIpv4SubnetSize">PublicIpv4SubnetSize</a>" : <i>Double</i>,
        "<a href="#storage" title="Storage">Storage</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
        "<a href="#waitforreservationdeprovision" title="WaitForReservationDeprovision">WaitForReservationDeprovision</a>" : <i>Boolean</i>,
        "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>[ <a href="ipaddress.md">IpAddress</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Packet::Device
Properties:
    <a href="#alwayspxe" title="AlwaysPxe">AlwaysPxe</a>: <i>Boolean</i>
    <a href="#billingcycle" title="BillingCycle">BillingCycle</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#facilities" title="Facilities">Facilities</a>: <i>
      - String</i>
    <a href="#facility" title="Facility">Facility</a>: <i>String</i>
    <a href="#forcedetachvolumes" title="ForceDetachVolumes">ForceDetachVolumes</a>: <i>Boolean</i>
    <a href="#hardwarereservationid" title="HardwareReservationId">HardwareReservationId</a>: <i>String</i>
    <a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
    <a href="#ipaddresstypes" title="IpAddressTypes">IpAddressTypes</a>: <i>
      - String</i>
    <a href="#ipxescripturl" title="IpxeScriptUrl">IpxeScriptUrl</a>: <i>String</i>
    <a href="#networktype" title="NetworkType">NetworkType</a>: <i>String</i>
    <a href="#operatingsystem" title="OperatingSystem">OperatingSystem</a>: <i>String</i>
    <a href="#plan" title="Plan">Plan</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#projectsshkeyids" title="ProjectSshKeyIds">ProjectSshKeyIds</a>: <i>
      - String</i>
    <a href="#publicipv4subnetsize" title="PublicIpv4SubnetSize">PublicIpv4SubnetSize</a>: <i>Double</i>
    <a href="#storage" title="Storage">Storage</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
    <a href="#waitforreservationdeprovision" title="WaitForReservationDeprovision">WaitForReservationDeprovision</a>: <i>Boolean</i>
    <a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>
      - <a href="ipaddress.md">IpAddress</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AlwaysPxe

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BillingCycle

monthly or hourly.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description string for the device.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Facilities

List of facility codes with deployment preferences. Packet API will go through the list and will deploy your device to first facility with free capacity. List items must be facility codes or `any` (a wildcard). To find the facility code, visit [Facilities API docs](https://www.packet.com/developers/api/facilities), set your API auth token in the top of the page and see JSON from the API response.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Facility

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceDetachVolumes

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HardwareReservationId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

The device name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddressTypes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpxeScriptUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OperatingSystem

The operating system slug. To find the slug, or visit [Operating Systems API docs](https://www.packet.com/developers/api/operatingsystems), set your API auth token in the top of the page and see JSON from the API response.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Plan

The device plan slug. To find the plan slug, visit [Device plans API docs](https://www.packet.com/developers/api/plans), set your auth token in the top of the page and see JSON from the API response.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The ID of the project in which to create the device.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectSshKeyIds

Array of IDs of the project SSH keys which should be added to the device. If you omit this, SSH keys of all the members of the parent project will be added to the device. If you specify this array, only the listed project SSH keys will be added. Project SSH keys can be created with the [packet_project_ssh_key][https://www.terraform.io/docs/providers/packet/r/project_ssh_key.html] resource.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIpv4SubnetSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Storage

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Tags attached to the device.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForReservationDeprovision

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

_Required_: No

_Type_: List of <a href="ipaddress.md">IpAddress</a>

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

#### AccessPrivateIpv4

Returns the <code>AccessPrivateIpv4</code> value.

#### AccessPublicIpv4

Returns the <code>AccessPublicIpv4</code> value.

#### AccessPublicIpv6

Returns the <code>AccessPublicIpv6</code> value.

#### Created

Returns the <code>Created</code> value.

#### DeployedFacility

Returns the <code>DeployedFacility</code> value.

#### Id

Returns the <code>Id</code> value.

#### Locked

Returns the <code>Locked</code> value.

#### Network

Returns the <code>Network</code> value.

#### Ports

Returns the <code>Ports</code> value.

#### RootPassword

Returns the <code>RootPassword</code> value.

#### SshKeyIds

Returns the <code>SshKeyIds</code> value.

#### State

Returns the <code>State</code> value.

#### Updated

Returns the <code>Updated</code> value.

