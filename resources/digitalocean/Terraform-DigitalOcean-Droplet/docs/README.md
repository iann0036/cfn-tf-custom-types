# Terraform::DigitalOcean::Droplet

CloudFormation equivalent of digitalocean_droplet

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::DigitalOcean::Droplet",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#backups" title="Backups">Backups</a>" : <i>Boolean</i>,
        "<a href="#createdat" title="CreatedAt">CreatedAt</a>" : <i>String</i>,
        "<a href="#disk" title="Disk">Disk</a>" : <i>Double</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#image" title="Image">Image</a>" : <i>String</i>,
        "<a href="#ipv4address" title="Ipv4Address">Ipv4Address</a>" : <i>String</i>,
        "<a href="#ipv4addressprivate" title="Ipv4AddressPrivate">Ipv4AddressPrivate</a>" : <i>String</i>,
        "<a href="#ipv6" title="Ipv6">Ipv6</a>" : <i>Boolean</i>,
        "<a href="#ipv6address" title="Ipv6Address">Ipv6Address</a>" : <i>String</i>,
        "<a href="#ipv6addressprivate" title="Ipv6AddressPrivate">Ipv6AddressPrivate</a>" : <i>String</i>,
        "<a href="#locked" title="Locked">Locked</a>" : <i>Boolean</i>,
        "<a href="#memory" title="Memory">Memory</a>" : <i>Double</i>,
        "<a href="#monitoring" title="Monitoring">Monitoring</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#pricehourly" title="PriceHourly">PriceHourly</a>" : <i>Double</i>,
        "<a href="#pricemonthly" title="PriceMonthly">PriceMonthly</a>" : <i>Double</i>,
        "<a href="#privatenetworking" title="PrivateNetworking">PrivateNetworking</a>" : <i>Boolean</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#resizedisk" title="ResizeDisk">ResizeDisk</a>" : <i>Boolean</i>,
        "<a href="#size" title="Size">Size</a>" : <i>String</i>,
        "<a href="#sshkeys" title="SshKeys">SshKeys</a>" : <i>[ String, ... ]</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#urn" title="Urn">Urn</a>" : <i>String</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
        "<a href="#vcpus" title="Vcpus">Vcpus</a>" : <i>Double</i>,
        "<a href="#volumeids" title="VolumeIds">VolumeIds</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::DigitalOcean::Droplet
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#backups" title="Backups">Backups</a>: <i>Boolean</i>
    <a href="#createdat" title="CreatedAt">CreatedAt</a>: <i>String</i>
    <a href="#disk" title="Disk">Disk</a>: <i>Double</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#image" title="Image">Image</a>: <i>String</i>
    <a href="#ipv4address" title="Ipv4Address">Ipv4Address</a>: <i>String</i>
    <a href="#ipv4addressprivate" title="Ipv4AddressPrivate">Ipv4AddressPrivate</a>: <i>String</i>
    <a href="#ipv6" title="Ipv6">Ipv6</a>: <i>Boolean</i>
    <a href="#ipv6address" title="Ipv6Address">Ipv6Address</a>: <i>String</i>
    <a href="#ipv6addressprivate" title="Ipv6AddressPrivate">Ipv6AddressPrivate</a>: <i>String</i>
    <a href="#locked" title="Locked">Locked</a>: <i>Boolean</i>
    <a href="#memory" title="Memory">Memory</a>: <i>Double</i>
    <a href="#monitoring" title="Monitoring">Monitoring</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#pricehourly" title="PriceHourly">PriceHourly</a>: <i>Double</i>
    <a href="#pricemonthly" title="PriceMonthly">PriceMonthly</a>: <i>Double</i>
    <a href="#privatenetworking" title="PrivateNetworking">PrivateNetworking</a>: <i>Boolean</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#resizedisk" title="ResizeDisk">ResizeDisk</a>: <i>Boolean</i>
    <a href="#size" title="Size">Size</a>: <i>String</i>
    <a href="#sshkeys" title="SshKeys">SshKeys</a>: <i>
      - String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#urn" title="Urn">Urn</a>: <i>String</i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
    <a href="#vcpus" title="Vcpus">Vcpus</a>: <i>Double</i>
    <a href="#volumeids" title="VolumeIds">VolumeIds</a>: <i>
      - String</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backups

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreatedAt

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disk

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4Address

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4AddressPrivate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6Address

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6AddressPrivate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Locked

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Memory

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Monitoring

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PriceHourly

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PriceMonthly

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateNetworking

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResizeDisk

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKeys

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Urn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vcpus

_Required_: No

_Type_: Double

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

Returns the &lt;code&gt;CreatedAt&lt;/code&gt; value.

#### Disk

Returns the &lt;code&gt;Disk&lt;/code&gt; value.

#### Ipv4Address

Returns the &lt;code&gt;Ipv4Address&lt;/code&gt; value.

#### Ipv4AddressPrivate

Returns the &lt;code&gt;Ipv4AddressPrivate&lt;/code&gt; value.

#### Ipv6Address

Returns the &lt;code&gt;Ipv6Address&lt;/code&gt; value.

#### Ipv6AddressPrivate

Returns the &lt;code&gt;Ipv6AddressPrivate&lt;/code&gt; value.

#### Locked

Returns the &lt;code&gt;Locked&lt;/code&gt; value.

#### Memory

Returns the &lt;code&gt;Memory&lt;/code&gt; value.

#### PriceHourly

Returns the &lt;code&gt;PriceHourly&lt;/code&gt; value.

#### PriceMonthly

Returns the &lt;code&gt;PriceMonthly&lt;/code&gt; value.

#### Status

Returns the &lt;code&gt;Status&lt;/code&gt; value.

#### Urn

Returns the &lt;code&gt;Urn&lt;/code&gt; value.

#### Vcpus

Returns the &lt;code&gt;Vcpus&lt;/code&gt; value.

