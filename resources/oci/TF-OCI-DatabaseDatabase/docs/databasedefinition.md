# TF::OCI::DatabaseDatabase DatabaseDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#adminpassword" title="AdminPassword">AdminPassword</a>" : <i>String</i>,
    "<a href="#backupid" title="BackupId">BackupId</a>" : <i>String</i>,
    "<a href="#backuptdepassword" title="BackupTdePassword">BackupTdePassword</a>" : <i>String</i>,
    "<a href="#characterset" title="CharacterSet">CharacterSet</a>" : <i>String</i>,
    "<a href="#databasesoftwareimageid" title="DatabaseSoftwareImageId">DatabaseSoftwareImageId</a>" : <i>String</i>,
    "<a href="#dbname" title="DbName">DbName</a>" : <i>String</i>,
    "<a href="#dbuniquename" title="DbUniqueName">DbUniqueName</a>" : <i>String</i>,
    "<a href="#dbworkload" title="DbWorkload">DbWorkload</a>" : <i>String</i>,
    "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>, ... ]</i>,
    "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>, ... ]</i>,
    "<a href="#ncharacterset" title="NcharacterSet">NcharacterSet</a>" : <i>String</i>,
    "<a href="#pdbname" title="PdbName">PdbName</a>" : <i>String</i>,
    "<a href="#tdewalletpassword" title="TdeWalletPassword">TdeWalletPassword</a>" : <i>String</i>,
    "<a href="#dbbackupconfig" title="DbBackupConfig">DbBackupConfig</a>" : <i>[ <a href="dbbackupconfigdefinition2.md">DbBackupConfigDefinition2</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#adminpassword" title="AdminPassword">AdminPassword</a>: <i>String</i>
<a href="#backupid" title="BackupId">BackupId</a>: <i>String</i>
<a href="#backuptdepassword" title="BackupTdePassword">BackupTdePassword</a>: <i>String</i>
<a href="#characterset" title="CharacterSet">CharacterSet</a>: <i>String</i>
<a href="#databasesoftwareimageid" title="DatabaseSoftwareImageId">DatabaseSoftwareImageId</a>: <i>String</i>
<a href="#dbname" title="DbName">DbName</a>: <i>String</i>
<a href="#dbuniquename" title="DbUniqueName">DbUniqueName</a>: <i>String</i>
<a href="#dbworkload" title="DbWorkload">DbWorkload</a>: <i>String</i>
<a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtagsdefinition.md">DefinedTagsDefinition</a></i>
<a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a></i>
<a href="#ncharacterset" title="NcharacterSet">NcharacterSet</a>: <i>String</i>
<a href="#pdbname" title="PdbName">PdbName</a>: <i>String</i>
<a href="#tdewalletpassword" title="TdeWalletPassword">TdeWalletPassword</a>: <i>String</i>
<a href="#dbbackupconfig" title="DbBackupConfig">DbBackupConfig</a>: <i>
      - <a href="dbbackupconfigdefinition2.md">DbBackupConfigDefinition2</a></i>
</pre>

## Properties

#### AdminPassword

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupTdePassword

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CharacterSet

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseSoftwareImageId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbUniqueName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbWorkload

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

_Required_: No

_Type_: List of <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

_Required_: No

_Type_: List of <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NcharacterSet

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PdbName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TdeWalletPassword

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbBackupConfig

_Required_: No

_Type_: List of <a href="dbbackupconfigdefinition2.md">DbBackupConfigDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

