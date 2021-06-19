# TF::Nomad::ExternalVolume

Creates and registers an external volume in Nomad.

This can be used to create and register external volumes in a Nomad cluster.

~> **Warning:** this resource will store any sensitive values placed in
  `secrets` or `mount_options` in the Terraform's state file. Take care to
  [protect your state file](/docs/state/sensitive-data.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Nomad::ExternalVolume",
    "Properties" : {
        "<a href="#capacitymax" title="CapacityMax">CapacityMax</a>" : <i>String</i>,
        "<a href="#capacitymin" title="CapacityMin">CapacityMin</a>" : <i>String</i>,
        "<a href="#cloneid" title="CloneId">CloneId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
        "<a href="#parameters" title="Parameters">Parameters</a>" : <i>[ <a href="parametersdefinition.md">ParametersDefinition</a>, ... ]</i>,
        "<a href="#pluginid" title="PluginId">PluginId</a>" : <i>String</i>,
        "<a href="#secrets" title="Secrets">Secrets</a>" : <i>[ <a href="secretsdefinition.md">SecretsDefinition</a>, ... ]</i>,
        "<a href="#snapshotid" title="SnapshotId">SnapshotId</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#volumeid" title="VolumeId">VolumeId</a>" : <i>String</i>,
        "<a href="#capability" title="Capability">Capability</a>" : <i>[ <a href="capabilitydefinition.md">CapabilityDefinition</a>, ... ]</i>,
        "<a href="#mountoptions" title="MountOptions">MountOptions</a>" : <i>[ <a href="mountoptionsdefinition.md">MountOptionsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Nomad::ExternalVolume
Properties:
    <a href="#capacitymax" title="CapacityMax">CapacityMax</a>: <i>String</i>
    <a href="#capacitymin" title="CapacityMin">CapacityMin</a>: <i>String</i>
    <a href="#cloneid" title="CloneId">CloneId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
    <a href="#parameters" title="Parameters">Parameters</a>: <i>
      - <a href="parametersdefinition.md">ParametersDefinition</a></i>
    <a href="#pluginid" title="PluginId">PluginId</a>: <i>String</i>
    <a href="#secrets" title="Secrets">Secrets</a>: <i>
      - <a href="secretsdefinition.md">SecretsDefinition</a></i>
    <a href="#snapshotid" title="SnapshotId">SnapshotId</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#volumeid" title="VolumeId">VolumeId</a>: <i>String</i>
    <a href="#capability" title="Capability">Capability</a>: <i>
      - <a href="capabilitydefinition.md">CapabilityDefinition</a></i>
    <a href="#mountoptions" title="MountOptions">MountOptions</a>: <i>
      - <a href="mountoptionsdefinition.md">MountOptionsDefinition</a></i>
</pre>

## Properties

#### CapacityMax

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapacityMin

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloneId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameters

_Required_: No

_Type_: List of <a href="parametersdefinition.md">ParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PluginId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Secrets

_Required_: No

_Type_: List of <a href="secretsdefinition.md">SecretsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Capability

_Required_: No

_Type_: List of <a href="capabilitydefinition.md">CapabilityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MountOptions

_Required_: No

_Type_: List of <a href="mountoptionsdefinition.md">MountOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ControllerRequired

Returns the <code>ControllerRequired</code> value.

#### ControllersExpected

Returns the <code>ControllersExpected</code> value.

#### ControllersHealthy

Returns the <code>ControllersHealthy</code> value.

#### Id

Returns the <code>Id</code> value.

#### NodesExpected

Returns the <code>NodesExpected</code> value.

#### NodesHealthy

Returns the <code>NodesHealthy</code> value.

#### PluginProvider

Returns the <code>PluginProvider</code> value.

#### PluginProviderVersion

Returns the <code>PluginProviderVersion</code> value.

#### Schedulable

Returns the <code>Schedulable</code> value.

