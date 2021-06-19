# TF::AzureRM::MssqlVirtualMachine

Manages a Microsoft SQL Virtual Machine

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::MssqlVirtualMachine",
    "Properties" : {
        "<a href="#rservicesenabled" title="RServicesEnabled">RServicesEnabled</a>" : <i>Boolean</i>,
        "<a href="#sqlconnectivityport" title="SqlConnectivityPort">SqlConnectivityPort</a>" : <i>Double</i>,
        "<a href="#sqlconnectivitytype" title="SqlConnectivityType">SqlConnectivityType</a>" : <i>String</i>,
        "<a href="#sqlconnectivityupdatepassword" title="SqlConnectivityUpdatePassword">SqlConnectivityUpdatePassword</a>" : <i>String</i>,
        "<a href="#sqlconnectivityupdateusername" title="SqlConnectivityUpdateUsername">SqlConnectivityUpdateUsername</a>" : <i>String</i>,
        "<a href="#sqllicensetype" title="SqlLicenseType">SqlLicenseType</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#virtualmachineid" title="VirtualMachineId">VirtualMachineId</a>" : <i>String</i>,
        "<a href="#autobackup" title="AutoBackup">AutoBackup</a>" : <i>[ <a href="autobackupdefinition.md">AutoBackupDefinition</a>, ... ]</i>,
        "<a href="#autopatching" title="AutoPatching">AutoPatching</a>" : <i>[ <a href="autopatchingdefinition.md">AutoPatchingDefinition</a>, ... ]</i>,
        "<a href="#keyvaultcredential" title="KeyVaultCredential">KeyVaultCredential</a>" : <i>[ <a href="keyvaultcredentialdefinition.md">KeyVaultCredentialDefinition</a>, ... ]</i>,
        "<a href="#storageconfiguration" title="StorageConfiguration">StorageConfiguration</a>" : <i>[ <a href="storageconfigurationdefinition.md">StorageConfigurationDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::MssqlVirtualMachine
Properties:
    <a href="#rservicesenabled" title="RServicesEnabled">RServicesEnabled</a>: <i>Boolean</i>
    <a href="#sqlconnectivityport" title="SqlConnectivityPort">SqlConnectivityPort</a>: <i>Double</i>
    <a href="#sqlconnectivitytype" title="SqlConnectivityType">SqlConnectivityType</a>: <i>String</i>
    <a href="#sqlconnectivityupdatepassword" title="SqlConnectivityUpdatePassword">SqlConnectivityUpdatePassword</a>: <i>String</i>
    <a href="#sqlconnectivityupdateusername" title="SqlConnectivityUpdateUsername">SqlConnectivityUpdateUsername</a>: <i>String</i>
    <a href="#sqllicensetype" title="SqlLicenseType">SqlLicenseType</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#virtualmachineid" title="VirtualMachineId">VirtualMachineId</a>: <i>String</i>
    <a href="#autobackup" title="AutoBackup">AutoBackup</a>: <i>
      - <a href="autobackupdefinition.md">AutoBackupDefinition</a></i>
    <a href="#autopatching" title="AutoPatching">AutoPatching</a>: <i>
      - <a href="autopatchingdefinition.md">AutoPatchingDefinition</a></i>
    <a href="#keyvaultcredential" title="KeyVaultCredential">KeyVaultCredential</a>: <i>
      - <a href="keyvaultcredentialdefinition.md">KeyVaultCredentialDefinition</a></i>
    <a href="#storageconfiguration" title="StorageConfiguration">StorageConfiguration</a>: <i>
      - <a href="storageconfigurationdefinition.md">StorageConfigurationDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### RServicesEnabled

Should R Services be enabled?.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SqlConnectivityPort

The SQL Server port. Defaults to `1433`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SqlConnectivityType

The connectivity type used for this SQL Server. Defaults to `PRIVATE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SqlConnectivityUpdatePassword

The SQL Server sysadmin login password.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SqlConnectivityUpdateUsername

The SQL Server sysadmin login to create.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SqlLicenseType

The SQL Server license type. Possible values are `AHUB` (Azure Hybrid Benefit) and `PAYG` (Pay-As-You-Go). Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualMachineId

The ID of the Virtual Machine. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoBackup

_Required_: No

_Type_: List of <a href="autobackupdefinition.md">AutoBackupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoPatching

_Required_: No

_Type_: List of <a href="autopatchingdefinition.md">AutoPatchingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyVaultCredential

_Required_: No

_Type_: List of <a href="keyvaultcredentialdefinition.md">KeyVaultCredentialDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageConfiguration

_Required_: No

_Type_: List of <a href="storageconfigurationdefinition.md">StorageConfigurationDefinition</a>

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

