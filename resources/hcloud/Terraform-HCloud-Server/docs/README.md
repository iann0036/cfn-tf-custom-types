# Terraform::HCloud::Server

Provides an Hetzner Cloud server resource. This can be used to create, modify, and delete servers. Servers also support [provisioning](https://www.terraform.io/docs/provisioners/index.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HCloud::Server",
    "Properties" : {
        "<a href="#backups" title="Backups">Backups</a>" : <i>Boolean</i>,
        "<a href="#datacenter" title="Datacenter">Datacenter</a>" : <i>String</i>,
        "<a href="#image" title="Image">Image</a>" : <i>String</i>,
        "<a href="#iso" title="Iso">Iso</a>" : <i>String</i>,
        "<a href="#keepdisk" title="KeepDisk">KeepDisk</a>" : <i>Boolean</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labels.md">Labels</a>, ... ]</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#rescue" title="Rescue">Rescue</a>" : <i>String</i>,
        "<a href="#servertype" title="ServerType">ServerType</a>" : <i>String</i>,
        "<a href="#sshkeys" title="SshKeys">SshKeys</a>" : <i>[ String, ... ]</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HCloud::Server
Properties:
    <a href="#backups" title="Backups">Backups</a>: <i>Boolean</i>
    <a href="#datacenter" title="Datacenter">Datacenter</a>: <i>String</i>
    <a href="#image" title="Image">Image</a>: <i>String</i>
    <a href="#iso" title="Iso">Iso</a>: <i>String</i>
    <a href="#keepdisk" title="KeepDisk">KeepDisk</a>: <i>Boolean</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labels.md">Labels</a></i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#rescue" title="Rescue">Rescue</a>: <i>String</i>
    <a href="#servertype" title="ServerType">ServerType</a>: <i>String</i>
    <a href="#sshkeys" title="SshKeys">SshKeys</a>: <i>
      - String</i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
</pre>

## Properties

#### Backups

Enable or disable backups.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Datacenter

The datacenter name to create the server in.
- `user_data` - (Optional, string) Cloud-Init user data to use during server creation
- `ssh_keys` - (Optional, list) SSH key IDs or names which should be injected into the server at creation time
- `keep_disk` - (Optional, bool) If true, do not upgrade the disk. This allows downgrading the server type later.
- `iso` - (Optional, string) ID or Name of an ISO image to mount.
- `rescue` - (Optional, string) Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
- `labels` - (Optional, map) User-defined labels (key-value pairs) should be created with.
- `backups` - (Optional, boolean) Enable or disable backups.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

Name or ID of the image the server is created from.
- `location` - (Optional, string) The location name to create the server in. `nbg1`, `fsn1` or `hel1`
- `datacenter` - (Optional, string) The datacenter name to create the server in.
- `user_data` - (Optional, string) Cloud-Init user data to use during server creation
- `ssh_keys` - (Optional, list) SSH key IDs or names which should be injected into the server at creation time
- `keep_disk` - (Optional, bool) If true, do not upgrade the disk. This allows downgrading the server type later.
- `iso` - (Optional, string) ID or Name of an ISO image to mount.
- `rescue` - (Optional, string) Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
- `labels` - (Optional, map) User-defined labels (key-value pairs) should be created with.
- `backups` - (Optional, boolean) Enable or disable backups.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Iso

ID or Name of an ISO image to mount.
- `rescue` - (Optional, string) Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
- `labels` - (Optional, map) User-defined labels (key-value pairs) should be created with.
- `backups` - (Optional, boolean) Enable or disable backups.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepDisk

If true, do not upgrade the disk. This allows downgrading the server type later.
- `iso` - (Optional, string) ID or Name of an ISO image to mount.
- `rescue` - (Optional, string) Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
- `labels` - (Optional, map) User-defined labels (key-value pairs) should be created with.
- `backups` - (Optional, boolean) Enable or disable backups.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

User-defined labels (key-value pairs) should be created with.
- `backups` - (Optional, boolean) Enable or disable backups.

_Required_: No

_Type_: List of <a href="labels.md">Labels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

The location name to create the server in. `nbg1`, `fsn1` or `hel1`
- `datacenter` - (Optional, string) The datacenter name to create the server in.
- `user_data` - (Optional, string) Cloud-Init user data to use during server creation
- `ssh_keys` - (Optional, list) SSH key IDs or names which should be injected into the server at creation time
- `keep_disk` - (Optional, bool) If true, do not upgrade the disk. This allows downgrading the server type later.
- `iso` - (Optional, string) ID or Name of an ISO image to mount.
- `rescue` - (Optional, string) Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
- `labels` - (Optional, map) User-defined labels (key-value pairs) should be created with.
- `backups` - (Optional, boolean) Enable or disable backups.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the server to create (must be unique per project and a valid hostname as per RFC 1123).
- `server_type` - (Required, string) Name of the server type this server should be created with.
- `image` - (Required, string) Name or ID of the image the server is created from.
- `location` - (Optional, string) The location name to create the server in. `nbg1`, `fsn1` or `hel1`
- `datacenter` - (Optional, string) The datacenter name to create the server in.
- `user_data` - (Optional, string) Cloud-Init user data to use during server creation
- `ssh_keys` - (Optional, list) SSH key IDs or names which should be injected into the server at creation time
- `keep_disk` - (Optional, bool) If true, do not upgrade the disk. This allows downgrading the server type later.
- `iso` - (Optional, string) ID or Name of an ISO image to mount.
- `rescue` - (Optional, string) Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
- `labels` - (Optional, map) User-defined labels (key-value pairs) should be created with.
- `backups` - (Optional, boolean) Enable or disable backups.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rescue

Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
- `labels` - (Optional, map) User-defined labels (key-value pairs) should be created with.
- `backups` - (Optional, boolean) Enable or disable backups.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerType

Name of the server type this server should be created with.
- `image` - (Required, string) Name or ID of the image the server is created from.
- `location` - (Optional, string) The location name to create the server in. `nbg1`, `fsn1` or `hel1`
- `datacenter` - (Optional, string) The datacenter name to create the server in.
- `user_data` - (Optional, string) Cloud-Init user data to use during server creation
- `ssh_keys` - (Optional, list) SSH key IDs or names which should be injected into the server at creation time
- `keep_disk` - (Optional, bool) If true, do not upgrade the disk. This allows downgrading the server type later.
- `iso` - (Optional, string) ID or Name of an ISO image to mount.
- `rescue` - (Optional, string) Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
- `labels` - (Optional, map) User-defined labels (key-value pairs) should be created with.
- `backups` - (Optional, boolean) Enable or disable backups.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKeys

SSH key IDs or names which should be injected into the server at creation time
- `keep_disk` - (Optional, bool) If true, do not upgrade the disk. This allows downgrading the server type later.
- `iso` - (Optional, string) ID or Name of an ISO image to mount.
- `rescue` - (Optional, string) Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
- `labels` - (Optional, map) User-defined labels (key-value pairs) should be created with.
- `backups` - (Optional, boolean) Enable or disable backups.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

Cloud-Init user data to use during server creation
- `ssh_keys` - (Optional, list) SSH key IDs or names which should be injected into the server at creation time
- `keep_disk` - (Optional, bool) If true, do not upgrade the disk. This allows downgrading the server type later.
- `iso` - (Optional, string) ID or Name of an ISO image to mount.
- `rescue` - (Optional, string) Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
- `labels` - (Optional, map) User-defined labels (key-value pairs) should be created with.
- `backups` - (Optional, boolean) Enable or disable backups.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### BackupWindow

Returns the <code>BackupWindow</code> value.

#### Id

Returns the <code>Id</code> value.

#### Ipv4Address

Returns the <code>Ipv4Address</code> value.

#### Ipv6Address

Returns the <code>Ipv6Address</code> value.

#### Ipv6Network

Returns the <code>Ipv6Network</code> value.

#### Status

Returns the <code>Status</code> value.

