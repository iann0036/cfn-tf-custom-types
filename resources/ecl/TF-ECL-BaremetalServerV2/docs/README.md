# TF::ECL::BaremetalServerV2

Manages a baremetal v2 Server resource within Enterprise Cloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ECL::BaremetalServerV2",
    "Properties" : {
        "<a href="#adminpass" title="AdminPass">AdminPass</a>" : <i>String</i>,
        "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
        "<a href="#flavorid" title="FlavorId">FlavorId</a>" : <i>String</i>,
        "<a href="#flavorname" title="FlavorName">FlavorName</a>" : <i>String</i>,
        "<a href="#imageid" title="ImageId">ImageId</a>" : <i>String</i>,
        "<a href="#imagename" title="ImageName">ImageName</a>" : <i>String</i>,
        "<a href="#keypair" title="KeyPair">KeyPair</a>" : <i>String</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadatadefinition.md">MetadataDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
        "<a href="#filesystems" title="Filesystems">Filesystems</a>" : <i>[ <a href="filesystemsdefinition.md">FilesystemsDefinition</a>, ... ]</i>,
        "<a href="#lvmvolumegroups" title="LvmVolumeGroups">LvmVolumeGroups</a>" : <i>[ <a href="lvmvolumegroupsdefinition.md">LvmVolumeGroupsDefinition</a>, ... ]</i>,
        "<a href="#networks" title="Networks">Networks</a>" : <i>[ <a href="networksdefinition.md">NetworksDefinition</a>, ... ]</i>,
        "<a href="#personality" title="Personality">Personality</a>" : <i>[ <a href="personalitydefinition.md">PersonalityDefinition</a>, ... ]</i>,
        "<a href="#raidarrays" title="RaidArrays">RaidArrays</a>" : <i>[ <a href="raidarraysdefinition.md">RaidArraysDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ECL::BaremetalServerV2
Properties:
    <a href="#adminpass" title="AdminPass">AdminPass</a>: <i>String</i>
    <a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
    <a href="#flavorid" title="FlavorId">FlavorId</a>: <i>String</i>
    <a href="#flavorname" title="FlavorName">FlavorName</a>: <i>String</i>
    <a href="#imageid" title="ImageId">ImageId</a>: <i>String</i>
    <a href="#imagename" title="ImageName">ImageName</a>: <i>String</i>
    <a href="#keypair" title="KeyPair">KeyPair</a>: <i>String</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadatadefinition.md">MetadataDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
    <a href="#filesystems" title="Filesystems">Filesystems</a>: <i>
      - <a href="filesystemsdefinition.md">FilesystemsDefinition</a></i>
    <a href="#lvmvolumegroups" title="LvmVolumeGroups">LvmVolumeGroups</a>: <i>
      - <a href="lvmvolumegroupsdefinition.md">LvmVolumeGroupsDefinition</a></i>
    <a href="#networks" title="Networks">Networks</a>: <i>
      - <a href="networksdefinition.md">NetworksDefinition</a></i>
    <a href="#personality" title="Personality">Personality</a>: <i>
      - <a href="personalitydefinition.md">PersonalityDefinition</a></i>
    <a href="#raidarrays" title="RaidArrays">RaidArrays</a>: <i>
      - <a href="raidarraysdefinition.md">RaidArraysDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AdminPass

The admin user password for the server.
Changing this creates a new server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityZone

The availability zone in which to create
the server. Changing this creates a new server.

_Required_: No

_Type_: String

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

#### ImageId

The image ID of the desired image for the server.
Changing this creates a new server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageName

The name of the desired image for the server.
If `image_id` is empty, this argument will be used to get the image's id.
Changing this creates a new server.

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
within the server. Changing this updates the existing server metadata.

_Required_: No

_Type_: List of <a href="metadatadefinition.md">MetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A unique name for the resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

The user data to provide when launching the server.
Changing this creates a new server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filesystems

_Required_: No

_Type_: List of <a href="filesystemsdefinition.md">FilesystemsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LvmVolumeGroups

_Required_: No

_Type_: List of <a href="lvmvolumegroupsdefinition.md">LvmVolumeGroupsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Networks

_Required_: No

_Type_: List of <a href="networksdefinition.md">NetworksDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Personality

_Required_: No

_Type_: List of <a href="personalitydefinition.md">PersonalityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RaidArrays

_Required_: No

_Type_: List of <a href="raidarraysdefinition.md">RaidArraysDefinition</a>

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

#### Id

Returns the <code>Id</code> value.

#### NicPhysicalPorts

Returns the <code>NicPhysicalPorts</code> value.

