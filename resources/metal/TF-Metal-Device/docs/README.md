# TF::Metal::Device

Provides an Equinix Metal device resource. This can be used to create,
modify, and delete devices.

~> **Note:** All arguments including the `root_password` and `user_data` will be stored in
 the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Metal::Device",
    "Properties" : {
        "<a href="#alwayspxe" title="AlwaysPxe">AlwaysPxe</a>" : <i>Boolean</i>,
        "<a href="#billingcycle" title="BillingCycle">BillingCycle</a>" : <i>String</i>,
        "<a href="#customdata" title="CustomData">CustomData</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#facilities" title="Facilities">Facilities</a>" : <i>[ String, ... ]</i>,
        "<a href="#forcedetachvolumes" title="ForceDetachVolumes">ForceDetachVolumes</a>" : <i>Boolean</i>,
        "<a href="#hardwarereservationid" title="HardwareReservationId">HardwareReservationId</a>" : <i>String</i>,
        "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
        "<a href="#ipxescripturl" title="IpxeScriptUrl">IpxeScriptUrl</a>" : <i>String</i>,
        "<a href="#metro" title="Metro">Metro</a>" : <i>String</i>,
        "<a href="#operatingsystem" title="OperatingSystem">OperatingSystem</a>" : <i>String</i>,
        "<a href="#plan" title="Plan">Plan</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#projectsshkeyids" title="ProjectSshKeyIds">ProjectSshKeyIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#storage" title="Storage">Storage</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
        "<a href="#waitforreservationdeprovision" title="WaitForReservationDeprovision">WaitForReservationDeprovision</a>" : <i>Boolean</i>,
        "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>[ <a href="ipaddressdefinition.md">IpAddressDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Metal::Device
Properties:
    <a href="#alwayspxe" title="AlwaysPxe">AlwaysPxe</a>: <i>Boolean</i>
    <a href="#billingcycle" title="BillingCycle">BillingCycle</a>: <i>String</i>
    <a href="#customdata" title="CustomData">CustomData</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#facilities" title="Facilities">Facilities</a>: <i>
      - String</i>
    <a href="#forcedetachvolumes" title="ForceDetachVolumes">ForceDetachVolumes</a>: <i>Boolean</i>
    <a href="#hardwarereservationid" title="HardwareReservationId">HardwareReservationId</a>: <i>String</i>
    <a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
    <a href="#ipxescripturl" title="IpxeScriptUrl">IpxeScriptUrl</a>: <i>String</i>
    <a href="#metro" title="Metro">Metro</a>: <i>String</i>
    <a href="#operatingsystem" title="OperatingSystem">OperatingSystem</a>: <i>String</i>
    <a href="#plan" title="Plan">Plan</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#projectsshkeyids" title="ProjectSshKeyIds">ProjectSshKeyIds</a>: <i>
      - String</i>
    <a href="#storage" title="Storage">Storage</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
    <a href="#waitforreservationdeprovision" title="WaitForReservationDeprovision">WaitForReservationDeprovision</a>: <i>Boolean</i>
    <a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>
      - <a href="ipaddressdefinition.md">IpAddressDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AlwaysPxe

If true, a device with OS `custom_ipxe` will
continue to boot via iPXE on reboots.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BillingCycle

monthly or hourly.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomData

A string of the desired Custom Data for the device.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description string for the device.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Facilities

List of facility codes with deployment preferences. Equinix Metal API will go through the list and will deploy your device to first facility with free capacity. List items must be facility codes or `any` (a wildcard). To find the facility code, visit [Facilities API docs](https://metal.equinix.com/developers/api/facilities/), set your API auth token in the top of the page and see JSON from the API response. Conflicts with `metro`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceDetachVolumes

Delete device even if it has volumes attached. Only applies for destroy action.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HardwareReservationId

The UUID of the hardware reservation where you want this device deployed, or `next-available` if you want to pick your next available reservation automatically.
Changing this from a reservation UUID to `next-available` will re-create the device in another reservation.
Please be careful when using hardware reservation UUID and `next-available` together for the same pool of reservations. It might happen that the reservation which Equinix Metal API will pick as `next-available` is the reservation which you refer with UUID in another metal_device resource. If that happens, and the metal_device with the UUID is created later, resource creation will fail because the reservation is already in use (by the resource created with `next-available`). To workaround this, have the `next-available` resource  [explicitly depend_on](https://learn.hashicorp.com/terraform/getting-started/dependencies.html#implicit-and-explicit-dependencies) the resource with hardware reservation UUID, so that the latter is created first. For more details, see [issue #176](https://github.com/packethost/terraform-provider-packet/issues/176).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

The device name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpxeScriptUrl

URL pointing to a hosted iPXE script. More
information is in the
[Custom iPXE](https://metal.equinix.com/developers/docs/servers/custom-ipxe/)
doc.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metro

Metro area for the new device. Conflicts with `facilities`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OperatingSystem

The operating system slug. To find the slug, or visit [Operating Systems API docs](https://metal.equinix.com/developers/api/operatingsystems), set your API auth token in the top of the page and see JSON from the API response.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Plan

The device plan slug. To find the plan slug, visit [Device plans API docs](https://metal.equinix.com/developers/api/plans), set your auth token in the top of the page and see JSON from the API response.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The ID of the project in which to create the device.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectSshKeyIds

Array of IDs of the project SSH keys which should be added to the device. If you omit this, SSH keys of all the members of the parent project will be added to the device. If you specify this array, only the listed project SSH keys will be added. Project SSH keys can be created with the [metal_project_ssh_key](project_ssh_key.md) resource.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Storage

JSON for custom partitioning. Only usable on reserved hardware. More information in in the [Custom Partitioning and RAID](https://metal.equinix.com/developers/docs/servers/custom-partitioning-raid/) doc.
* Please note that the disks.partitions.size attribute must be a string, not an integer. It can be a number string, or size notation string, e.g. "4G" or "8M" (for gigabytes and megabytes).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Tags attached to the device.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

A string of the desired User Data for the device.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForReservationDeprovision

Only used for devices in reserved hardware. If set, the deletion of this device will block until the hardware reservation is marked provisionable (about 4 minutes in August 2019).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

_Required_: No

_Type_: List of <a href="ipaddressdefinition.md">IpAddressDefinition</a>

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

#### DeployedHardwareReservationId

Returns the <code>DeployedHardwareReservationId</code> value.

#### Id

Returns the <code>Id</code> value.

#### Locked

Returns the <code>Locked</code> value.

#### Network

Returns the <code>Network</code> value.

#### NetworkType

Returns the <code>NetworkType</code> value.

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

