# TF::Nutanix::VirtualMachine DiskListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#datasourcereference" title="DataSourceReference">DataSourceReference</a>" : <i>[ <a href="datasourcereferencedefinition.md">DataSourceReferenceDefinition</a>, ... ]</i>,
    "<a href="#disksizebytes" title="DiskSizeBytes">DiskSizeBytes</a>" : <i>Double</i>,
    "<a href="#disksizemib" title="DiskSizeMib">DiskSizeMib</a>" : <i>Double</i>,
    "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
    "<a href="#volumegroupreference" title="VolumeGroupReference">VolumeGroupReference</a>" : <i>[ <a href="volumegroupreferencedefinition.md">VolumeGroupReferenceDefinition</a>, ... ]</i>,
    "<a href="#deviceproperties" title="DeviceProperties">DeviceProperties</a>" : <i>[ <a href="devicepropertiesdefinition.md">DevicePropertiesDefinition</a>, ... ]</i>,
    "<a href="#storageconfig" title="StorageConfig">StorageConfig</a>" : <i>[ <a href="storageconfigdefinition.md">StorageConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#datasourcereference" title="DataSourceReference">DataSourceReference</a>: <i>
      - <a href="datasourcereferencedefinition.md">DataSourceReferenceDefinition</a></i>
<a href="#disksizebytes" title="DiskSizeBytes">DiskSizeBytes</a>: <i>Double</i>
<a href="#disksizemib" title="DiskSizeMib">DiskSizeMib</a>: <i>Double</i>
<a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
<a href="#volumegroupreference" title="VolumeGroupReference">VolumeGroupReference</a>: <i>
      - <a href="volumegroupreferencedefinition.md">VolumeGroupReferenceDefinition</a></i>
<a href="#deviceproperties" title="DeviceProperties">DeviceProperties</a>: <i>
      - <a href="devicepropertiesdefinition.md">DevicePropertiesDefinition</a></i>
<a href="#storageconfig" title="StorageConfig">StorageConfig</a>: <i>
      - <a href="storageconfigdefinition.md">StorageConfigDefinition</a></i>
</pre>

## Properties

#### DataSourceReference

_Required_: No

_Type_: List of <a href="datasourcereferencedefinition.md">DataSourceReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSizeBytes

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSizeMib

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeGroupReference

_Required_: No

_Type_: List of <a href="volumegroupreferencedefinition.md">VolumeGroupReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceProperties

_Required_: No

_Type_: List of <a href="devicepropertiesdefinition.md">DevicePropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageConfig

_Required_: No

_Type_: List of <a href="storageconfigdefinition.md">StorageConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

