# Terraform::OpenStack::ComputeInstanceV2

Manages a V2 VM instance resource within OpenStack.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenStack::ComputeInstanceV2",
    "Properties" : {
        "<a href="#accessipv4" title="AccessIpV4">AccessIpV4</a>" : <i>String</i>,
        "<a href="#accessipv6" title="AccessIpV6">AccessIpV6</a>" : <i>String</i>,
        "<a href="#adminpass" title="AdminPass">AdminPass</a>" : <i>String</i>,
        "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
        "<a href="#configdrive" title="ConfigDrive">ConfigDrive</a>" : <i>Boolean</i>,
        "<a href="#flavorid" title="FlavorId">FlavorId</a>" : <i>String</i>,
        "<a href="#flavorname" title="FlavorName">FlavorName</a>" : <i>String</i>,
        "<a href="#floatingip" title="FloatingIp">FloatingIp</a>" : <i>String</i>,
        "<a href="#forcedelete" title="ForceDelete">ForceDelete</a>" : <i>Boolean</i>,
        "<a href="#imageid" title="ImageId">ImageId</a>" : <i>String</i>,
        "<a href="#imagename" title="ImageName">ImageName</a>" : <i>String</i>,
        "<a href="#keypair" title="KeyPair">KeyPair</a>" : <i>String</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadata.md">Metadata</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#powerstate" title="PowerState">PowerState</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>" : <i>[ String, ... ]</i>,
        "<a href="#stopbeforedestroy" title="StopBeforeDestroy">StopBeforeDestroy</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
        "<a href="#blockdevice" title="BlockDevice">BlockDevice</a>" : <i>[ <a href="blockdevice.md">BlockDevice</a>, ... ]</i>,
        "<a href="#network" title="Network">Network</a>" : <i>[ <a href="network.md">Network</a>, ... ]</i>,
        "<a href="#personality" title="Personality">Personality</a>" : <i>[ <a href="personality.md">Personality</a>, ... ]</i>,
        "<a href="#schedulerhints" title="SchedulerHints">SchedulerHints</a>" : <i>[ <a href="schedulerhints.md">SchedulerHints</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#vendoroptions" title="VendorOptions">VendorOptions</a>" : <i>[ <a href="vendoroptions.md">VendorOptions</a>, ... ]</i>,
        "<a href="#volume" title="Volume">Volume</a>" : <i>[ <a href="volume.md">Volume</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenStack::ComputeInstanceV2
Properties:
    <a href="#accessipv4" title="AccessIpV4">AccessIpV4</a>: <i>String</i>
    <a href="#accessipv6" title="AccessIpV6">AccessIpV6</a>: <i>String</i>
    <a href="#adminpass" title="AdminPass">AdminPass</a>: <i>String</i>
    <a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
    <a href="#configdrive" title="ConfigDrive">ConfigDrive</a>: <i>Boolean</i>
    <a href="#flavorid" title="FlavorId">FlavorId</a>: <i>String</i>
    <a href="#flavorname" title="FlavorName">FlavorName</a>: <i>String</i>
    <a href="#floatingip" title="FloatingIp">FloatingIp</a>: <i>String</i>
    <a href="#forcedelete" title="ForceDelete">ForceDelete</a>: <i>Boolean</i>
    <a href="#imageid" title="ImageId">ImageId</a>: <i>String</i>
    <a href="#imagename" title="ImageName">ImageName</a>: <i>String</i>
    <a href="#keypair" title="KeyPair">KeyPair</a>: <i>String</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadata.md">Metadata</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#powerstate" title="PowerState">PowerState</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>: <i>
      - String</i>
    <a href="#stopbeforedestroy" title="StopBeforeDestroy">StopBeforeDestroy</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
    <a href="#blockdevice" title="BlockDevice">BlockDevice</a>: <i>
      - <a href="blockdevice.md">BlockDevice</a></i>
    <a href="#network" title="Network">Network</a>: <i>
      - <a href="network.md">Network</a></i>
    <a href="#personality" title="Personality">Personality</a>: <i>
      - <a href="personality.md">Personality</a></i>
    <a href="#schedulerhints" title="SchedulerHints">SchedulerHints</a>: <i>
      - <a href="schedulerhints.md">SchedulerHints</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#vendoroptions" title="VendorOptions">VendorOptions</a>: <i>
      - <a href="vendoroptions.md">VendorOptions</a></i>
    <a href="#volume" title="Volume">Volume</a>: <i>
      - <a href="volume.md">Volume</a></i>
</pre>

## Properties

#### AccessIpV4

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessIpV6

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminPass

The administrative password to assign to the server.
Changing this changes the root password on the existing server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityZone

The availability zone in which to create
the server. Changing this creates a new server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigDrive

Whether to use the config_drive feature to
configure the instance. Changing this creates a new server.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlavorId

The flavor ID of
the desired flavor for the server. Changing this resizes the existing server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlavorName

The name of the
desired flavor for the server. Changing this resizes the existing server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FloatingIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceDelete

Whether to force the OpenStack instance to be
forcefully deleted. This is useful for environments that have reclaim / soft
deletion enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageId

The image ID of
the desired image for the server. Changing this creates a new server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageName

The name of the
desired image for the server. Changing this creates a new server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyPair

The name of a key pair to put on the server. The key
pair must already be created and associated with the tenant's account.
Changing this creates a new server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

Metadata key/value pairs to make available from
within the instance. Changing this updates the existing server metadata.

_Required_: No

_Type_: List of <a href="metadata.md">Metadata</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A unique name for the resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PowerState

Provide the VM state. Only 'active' and 'shutoff'
are supported values. *Note*: If the initial power_state is the shutoff
the VM will be stopped immediately after build and the provisioners like
remote-exec or files are not supported.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to create the server instance. If
omitted, the `region` argument of the provider is used. Changing this
creates a new server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroups

An array of one or more security group names
or ids to associate with the server. Changing this results in adding/removing
security groups from the existing server. *Note*: When attaching the
instance to networks using Ports, place the security groups on the Port
and not the instance.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StopBeforeDestroy

Whether to try stop instance gracefully
before destroying it, thus giving chance for guest OS daemons to stop correctly.
If instance doesn't stop within timeout, it will be destroyed anyway.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A set of string tags for the instance. Changing this
updates the existing instance tags.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

The user data to provide when launching the instance.
Changing this creates a new server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockDevice

_Required_: No

_Type_: List of <a href="blockdevice.md">BlockDevice</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

_Required_: No

_Type_: List of <a href="network.md">Network</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Personality

_Required_: No

_Type_: List of <a href="personality.md">Personality</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchedulerHints

_Required_: No

_Type_: List of <a href="schedulerhints.md">SchedulerHints</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VendorOptions

_Required_: No

_Type_: List of <a href="vendoroptions.md">VendorOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Volume

_Required_: No

_Type_: List of <a href="volume.md">Volume</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AllMetadata

Returns the <code>AllMetadata</code> value.

#### AllTags

Returns the <code>AllTags</code> value.

#### Id

Returns the <code>Id</code> value.

