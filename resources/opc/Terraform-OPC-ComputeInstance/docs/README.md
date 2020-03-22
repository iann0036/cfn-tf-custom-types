# Terraform::OPC::ComputeInstance

The ``opc_compute_instance`` resource creates and manages an instance in an Oracle Cloud Infrastructure Compute Classic identity domain.

~> **Caution:** The ``opc_compute_instance`` resource can completely delete your
instance just as easily as it can create it. To avoid costly accidents,
consider setting
[``prevent_destroy``](/docs/configuration/resources.html#prevent_destroy)
on your instance resources as an extra safety measure.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OPC::ComputeInstance",
    "Properties" : {
        "<a href="#bootorder" title="BootOrder">BootOrder</a>" : <i>[ Double, ... ]</i>,
        "<a href="#desiredstate" title="DesiredState">DesiredState</a>" : <i>String</i>,
        "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
        "<a href="#imagelist" title="ImageList">ImageList</a>" : <i>String</i>,
        "<a href="#instanceattributes" title="InstanceAttributes">InstanceAttributes</a>" : <i>String</i>,
        "<a href="#label" title="Label">Label</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#reversedns" title="ReverseDns">ReverseDns</a>" : <i>Boolean</i>,
        "<a href="#shape" title="Shape">Shape</a>" : <i>String</i>,
        "<a href="#sshkeys" title="SshKeys">SshKeys</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#networkinginfo" title="NetworkingInfo">NetworkingInfo</a>" : <i>[ <a href="networkinginfo.md">NetworkingInfo</a>, ... ]</i>,
        "<a href="#storage" title="Storage">Storage</a>" : <i>[ <a href="storage.md">Storage</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OPC::ComputeInstance
Properties:
    <a href="#bootorder" title="BootOrder">BootOrder</a>: <i>
      - Double</i>
    <a href="#desiredstate" title="DesiredState">DesiredState</a>: <i>String</i>
    <a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
    <a href="#imagelist" title="ImageList">ImageList</a>: <i>String</i>
    <a href="#instanceattributes" title="InstanceAttributes">InstanceAttributes</a>: <i>String</i>
    <a href="#label" title="Label">Label</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#reversedns" title="ReverseDns">ReverseDns</a>: <i>Boolean</i>
    <a href="#shape" title="Shape">Shape</a>: <i>String</i>
    <a href="#sshkeys" title="SshKeys">SshKeys</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#networkinginfo" title="NetworkingInfo">NetworkingInfo</a>: <i>
      - <a href="networkinginfo.md">NetworkingInfo</a></i>
    <a href="#storage" title="Storage">Storage</a>: <i>
      - <a href="storage.md">Storage</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### BootOrder

The index number of the bootable storage volume, presented as a list, that should be used to boot the instance. The only valid value is `[1]`. If you set this attribute, you must also specify a bootable storage volume with index number 1 in the volume sub-parameter of storage_attachments. When you specify boot_order, you don't need to specify the imagelist attribute, because the instance is booted using the image on the specified bootable storage volume. If you specify both boot_order and imagelist, the imagelist attribute is ignored.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredState

Set the desire state of the instance to `running` (default) or `shutdown`. You can use this request to shut down and restart individual instances which use a persistent bootable storage volume.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

The host name assigned to the instance. On an Oracle Linux instance, this host name is displayed in response to the hostname command. Only relative DNS is supported. The domain name is suffixed to the host name that you specify. The host name must not end with a period. If you don't specify a host name, then a name is generated automatically.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageList

The imageList of the instance, e.g. `/oracle/public/oel_6.4_2GB_v1`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceAttributes

A JSON string of custom attributes. See [Attributes](#attributes) below for more information.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

The label to apply to the instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReverseDns

If set to `true` (default), then reverse DNS records are created. If set to `false`, no reverse DNS records are created.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shape

The shape of the instance, e.g. `oc4`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKeys

A list of the names of the SSH Keys that can be used to log into the instance.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A list of strings that should be supplied to the instance as tags.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkingInfo

_Required_: No

_Type_: List of <a href="networkinginfo.md">NetworkingInfo</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Storage

_Required_: No

_Type_: List of <a href="storage.md">Storage</a>

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

#### Attributes

Returns the <code>Attributes</code> value.

#### AvailabilityDomain

Returns the <code>AvailabilityDomain</code> value.

#### Domain

Returns the <code>Domain</code> value.

#### Entry

Returns the <code>Entry</code> value.

#### Fingerprint

Returns the <code>Fingerprint</code> value.

#### Fqdn

Returns the <code>Fqdn</code> value.

#### Id

Returns the <code>Id</code> value.

#### ImageFormat

Returns the <code>ImageFormat</code> value.

#### IpAddress

Returns the <code>IpAddress</code> value.

#### PlacementRequirements

Returns the <code>PlacementRequirements</code> value.

#### Platform

Returns the <code>Platform</code> value.

#### Priority

Returns the <code>Priority</code> value.

#### QuotaReservation

Returns the <code>QuotaReservation</code> value.

#### Relationships

Returns the <code>Relationships</code> value.

#### Resolvers

Returns the <code>Resolvers</code> value.

#### Site

Returns the <code>Site</code> value.

#### StartTime

Returns the <code>StartTime</code> value.

#### State

Returns the <code>State</code> value.

#### Vcable

Returns the <code>Vcable</code> value.

#### Virtio

Returns the <code>Virtio</code> value.

#### VncAddress

Returns the <code>VncAddress</code> value.

