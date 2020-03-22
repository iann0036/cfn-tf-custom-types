# Terraform::CloudScale::Server

Provides a cloudscale.ch Server resource. This can be used to create, modify, and delete servers.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::CloudScale::Server",
    "Properties" : {
        "<a href="#allowstoppingforupdate" title="AllowStoppingForUpdate">AllowStoppingForUpdate</a>" : <i>Boolean</i>,
        "<a href="#bulkvolumesizegb" title="BulkVolumeSizeGb">BulkVolumeSizeGb</a>" : <i>Double</i>,
        "<a href="#flavorslug" title="FlavorSlug">FlavorSlug</a>" : <i>String</i>,
        "<a href="#imageslug" title="ImageSlug">ImageSlug</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#servergroupids" title="ServerGroupIds">ServerGroupIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#sshkeys" title="SshKeys">SshKeys</a>" : <i>[ String, ... ]</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#useipv6" title="UseIpv6">UseIpv6</a>" : <i>Boolean</i>,
        "<a href="#useprivatenetwork" title="UsePrivateNetwork">UsePrivateNetwork</a>" : <i>Boolean</i>,
        "<a href="#usepublicnetwork" title="UsePublicNetwork">UsePublicNetwork</a>" : <i>Boolean</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
        "<a href="#volumesizegb" title="VolumeSizeGb">VolumeSizeGb</a>" : <i>Double</i>,
        "<a href="#zoneslug" title="ZoneSlug">ZoneSlug</a>" : <i>String</i>,
        "<a href="#interfaces" title="Interfaces">Interfaces</a>" : <i>[ <a href="interfaces.md">Interfaces</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::CloudScale::Server
Properties:
    <a href="#allowstoppingforupdate" title="AllowStoppingForUpdate">AllowStoppingForUpdate</a>: <i>Boolean</i>
    <a href="#bulkvolumesizegb" title="BulkVolumeSizeGb">BulkVolumeSizeGb</a>: <i>Double</i>
    <a href="#flavorslug" title="FlavorSlug">FlavorSlug</a>: <i>String</i>
    <a href="#imageslug" title="ImageSlug">ImageSlug</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#servergroupids" title="ServerGroupIds">ServerGroupIds</a>: <i>
      - String</i>
    <a href="#sshkeys" title="SshKeys">SshKeys</a>: <i>
      - String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#useipv6" title="UseIpv6">UseIpv6</a>: <i>Boolean</i>
    <a href="#useprivatenetwork" title="UsePrivateNetwork">UsePrivateNetwork</a>: <i>Boolean</i>
    <a href="#usepublicnetwork" title="UsePublicNetwork">UsePublicNetwork</a>: <i>Boolean</i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
    <a href="#volumesizegb" title="VolumeSizeGb">VolumeSizeGb</a>: <i>Double</i>
    <a href="#zoneslug" title="ZoneSlug">ZoneSlug</a>: <i>String</i>
    <a href="#interfaces" title="Interfaces">Interfaces</a>: <i>
      - <a href="interfaces.md">Interfaces</a></i>
</pre>

## Properties

#### AllowStoppingForUpdate

If true, allows Terraform to stop the instance to update its properties. If you try to update a property that requires stopping the instance without setting this field, the update will fail.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BulkVolumeSizeGb

The size in GB of the bulk storage volume of the new server. If this parameter is not specified, no bulk storage volume will be attached to the server. Valid values are multiples of 100.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlavorSlug

The slug (name) of the flavor to use for the new server. Possible values can be found in our [API documentation](https://www.cloudscale.ch/en/api/v1#flavors).
**Note:** If you want to update this value after initial creation, you must set [`allow_stopping_for_update`](#allow_stopping_for_update) to `true`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageSlug

The slug (name) of the image to use for the new server. Possible values can be found in our [API documentation](https://www.cloudscale.ch/en/api/v1#images).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the new server. The name has to be a valid host name or a fully qualified domain name (FQDN).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

The password of the default user of the new server. When omitted, no password will be set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerGroupIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKeys

A list of SSH public keys. Use the full content of your \*.pub file here.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

The desired state of a server. Can be `running` (default) or `stopped`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseIpv6

Enable/disable IPv6 on the public network interface of the new server. Can be `true` (default) or `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsePrivateNetwork

Attach the `default` private network interface to the new server. Can be `true` or `false` (default). Use [`interfaces`](#interfaces) option for advanced setups.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsePublicNetwork

Attach the public network interface to the new server. Can be `true` (default) or `false`. Use [`interfaces`](#interfaces) option for advanced setups.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

User data (custom cloud-config settings) to use for the new server. Needs to be valid YAML. A default configuration will be used if this parameter is not specified or set to null. Use only if you are an advanced user with knowledge of cloud-config and cloud-init.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeSizeGb

The size in GB of the SSD root volume of the new server.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneSlug

You can specify a zone slug. Options include `lpg1` and `rma1`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interfaces

_Required_: No

_Type_: List of <a href="interfaces.md">Interfaces</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Href

Returns the <code>Href</code> value.

#### Id

Returns the <code>Id</code> value.

#### PrivateIpv4Address

Returns the <code>PrivateIpv4Address</code> value.

#### PublicIpv4Address

Returns the <code>PublicIpv4Address</code> value.

#### PublicIpv6Address

Returns the <code>PublicIpv6Address</code> value.

#### ServerGroups

Returns the <code>ServerGroups</code> value.

#### SshFingerprints

Returns the <code>SshFingerprints</code> value.

#### SshHostKeys

Returns the <code>SshHostKeys</code> value.

#### Volumes

Returns the <code>Volumes</code> value.

