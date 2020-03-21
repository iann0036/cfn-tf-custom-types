# Terraform::OCI::DatabaseDbHome Database

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#adminpassword" title="AdminPassword">AdminPassword</a>" : <i>String</i>,
    "<a href="#backupid" title="BackupId">BackupId</a>" : <i>String</i>,
    "<a href="#backuptdepassword" title="BackupTdePassword">BackupTdePassword</a>" : <i>String</i>,
    "<a href="#characterset" title="CharacterSet">CharacterSet</a>" : <i>String</i>,
    "<a href="#dbname" title="DbName">DbName</a>" : <i>String</i>,
    "<a href="#dbworkload" title="DbWorkload">DbWorkload</a>" : <i>String</i>,
    "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ &lt;a href=&#34;database-definedtags.md&#34;&gt;DefinedTags&lt;/a&gt;, ... ]</i>,
    "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ &lt;a href=&#34;database-freeformtags.md&#34;&gt;FreeformTags&lt;/a&gt;, ... ]</i>,
    "<a href="#ncharacterset" title="NcharacterSet">NcharacterSet</a>" : <i>String</i>,
    "<a href="#pdbname" title="PdbName">PdbName</a>" : <i>String</i>,
    "<a href="#dbbackupconfig" title="DbBackupConfig">DbBackupConfig</a>" : <i>[ &lt;a href=&#34;database-dbbackupconfig.md&#34;&gt;DbBackupConfig&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#adminpassword" title="AdminPassword">AdminPassword</a>: <i>String</i>
<a href="#backupid" title="BackupId">BackupId</a>: <i>String</i>
<a href="#backuptdepassword" title="BackupTdePassword">BackupTdePassword</a>: <i>String</i>
<a href="#characterset" title="CharacterSet">CharacterSet</a>: <i>String</i>
<a href="#dbname" title="DbName">DbName</a>: <i>String</i>
<a href="#dbworkload" title="DbWorkload">DbWorkload</a>: <i>String</i>
<a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - &lt;a href=&#34;database-definedtags.md&#34;&gt;DefinedTags&lt;/a&gt;</i>
<a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - &lt;a href=&#34;database-freeformtags.md&#34;&gt;FreeformTags&lt;/a&gt;</i>
<a href="#ncharacterset" title="NcharacterSet">NcharacterSet</a>: <i>String</i>
<a href="#pdbname" title="PdbName">PdbName</a>: <i>String</i>
<a href="#dbbackupconfig" title="DbBackupConfig">DbBackupConfig</a>: <i>
      - &lt;a href=&#34;database-dbbackupconfig.md&#34;&gt;DbBackupConfig&lt;/a&gt;</i>
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

#### DbName

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbWorkload

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

_Required_: No
_Type_: List of &lt;a href=&#34;database-definedtags.md&#34;&gt;DefinedTags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

_Required_: No
_Type_: List of &lt;a href=&#34;database-freeformtags.md&#34;&gt;FreeformTags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NcharacterSet

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PdbName

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbBackupConfig

_Required_: No
_Type_: List of &lt;a href=&#34;database-dbbackupconfig.md&#34;&gt;DbBackupConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

