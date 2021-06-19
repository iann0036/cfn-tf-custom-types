# TF::AzureRM::MssqlVirtualMachine StorageConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#disktype" title="DiskType">DiskType</a>" : <i>String</i>,
    "<a href="#storageworkloadtype" title="StorageWorkloadType">StorageWorkloadType</a>" : <i>String</i>,
    "<a href="#datasettings" title="DataSettings">DataSettings</a>" : <i>[ <a href="datasettingsdefinition.md">DataSettingsDefinition</a>, ... ]</i>,
    "<a href="#logsettings" title="LogSettings">LogSettings</a>" : <i>[ <a href="logsettingsdefinition.md">LogSettingsDefinition</a>, ... ]</i>,
    "<a href="#tempdbsettings" title="TempDbSettings">TempDbSettings</a>" : <i>[ <a href="tempdbsettingsdefinition.md">TempDbSettingsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#disktype" title="DiskType">DiskType</a>: <i>String</i>
<a href="#storageworkloadtype" title="StorageWorkloadType">StorageWorkloadType</a>: <i>String</i>
<a href="#datasettings" title="DataSettings">DataSettings</a>: <i>
      - <a href="datasettingsdefinition.md">DataSettingsDefinition</a></i>
<a href="#logsettings" title="LogSettings">LogSettings</a>: <i>
      - <a href="logsettingsdefinition.md">LogSettingsDefinition</a></i>
<a href="#tempdbsettings" title="TempDbSettings">TempDbSettings</a>: <i>
      - <a href="tempdbsettingsdefinition.md">TempDbSettingsDefinition</a></i>
</pre>

## Properties

#### DiskType

The type of disk configuration to apply to the SQL Server. Valid values include `NEW`, `EXTEND`, or `ADD`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageWorkloadType

The type of storage workload. Valid values include `GENERAL`, `OLTP`, or `DW`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataSettings

_Required_: No

_Type_: List of <a href="datasettingsdefinition.md">DataSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogSettings

_Required_: No

_Type_: List of <a href="logsettingsdefinition.md">LogSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TempDbSettings

_Required_: No

_Type_: List of <a href="tempdbsettingsdefinition.md">TempDbSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

