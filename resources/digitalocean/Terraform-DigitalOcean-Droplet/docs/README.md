# Terraform::DigitalOcean::Droplet

Provides a DigitalOcean Droplet resource. This can be used to create,
modify, and delete Droplets. Droplets also support
[provisioning](/docs/provisioners/index.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::DigitalOcean::Droplet",
    "Properties" : {
        "<a href="#backups" title="Backups">Backups</a>" : <i>Boolean</i>,
        "<a href="#image" title="Image">Image</a>" : <i>String</i>,
        "<a href="#ipv6" title="Ipv6">Ipv6</a>" : <i>Boolean</i>,
        "<a href="#monitoring" title="Monitoring">Monitoring</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#privatenetworking" title="PrivateNetworking">PrivateNetworking</a>" : <i>Boolean</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#resizedisk" title="ResizeDisk">ResizeDisk</a>" : <i>Boolean</i>,
        "<a href="#size" title="Size">Size</a>" : <i>String</i>,
        "<a href="#sshkeys" title="SshKeys">SshKeys</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
        "<a href="#volumeids" title="VolumeIds">VolumeIds</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::DigitalOcean::Droplet
Properties:
    <a href="#backups" title="Backups">Backups</a>: <i>Boolean</i>
    <a href="#image" title="Image">Image</a>: <i>String</i>
    <a href="#ipv6" title="Ipv6">Ipv6</a>: <i>Boolean</i>
    <a href="#monitoring" title="Monitoring">Monitoring</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#privatenetworking" title="PrivateNetworking">PrivateNetworking</a>: <i>Boolean</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#resizedisk" title="ResizeDisk">ResizeDisk</a>: <i>Boolean</i>
    <a href="#size" title="Size">Size</a>: <i>String</i>
    <a href="#sshkeys" title="SshKeys">SshKeys</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
    <a href="#volumeids" title="VolumeIds">VolumeIds</a>: <i>
      - String</i>
</pre>

## Properties

#### Backups

Boolean controlling if backups are made. Defaults to
false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

The Droplet image ID or slug.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6

Boolean controlling if IPv6 is enabled. Defaults to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Monitoring

Boolean controlling whether monitoring agent is installed.
Defaults to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The Droplet name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateNetworking

Boolean controlling if private networks are
enabled. Defaults to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region to start in.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResizeDisk

Boolean controlling whether to increase the disk
size when resizing a Droplet. It defaults to `true`. When set to `false`,
only the Droplet's RAM and CPU will be resized. **Increasing a Droplet's disk
size is a permanent change**. Increasing only RAM and CPU is reversible.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

The unique slug that indentifies the type of Droplet. You can find a list of available slugs on [DigitalOcean API documentation](https://developers.digitalocean.com/documentation/v2/#list-all-sizes).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKeys

A list of SSH IDs or fingerprints to enable in
the format `[12345, 123456]`. To retrieve this info, use a tool such
as `curl` with the [DigitalOcean API](https://developers.digitalocean.com/documentation/v2/#ssh-keys),
to retrieve them.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A list of the tags to be applied to this Droplet.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### Disk

Returns the <code>Disk</code> value.

#### Ipv4Address

Returns the <code>Ipv4Address</code> value.

#### Ipv4AddressPrivate

Returns the <code>Ipv4AddressPrivate</code> value.

#### Ipv6Address

Returns the <code>Ipv6Address</code> value.

#### Ipv6AddressPrivate

Returns the <code>Ipv6AddressPrivate</code> value.

#### Locked

Returns the <code>Locked</code> value.

#### Memory

Returns the <code>Memory</code> value.

#### PriceHourly

Returns the <code>PriceHourly</code> value.

#### PriceMonthly

Returns the <code>PriceMonthly</code> value.

#### Status

Returns the <code>Status</code> value.

#### Urn

Returns the <code>Urn</code> value.

#### Vcpus

Returns the <code>Vcpus</code> value.

