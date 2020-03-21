# Terraform::OCI::DatabaseDbHome

CloudFormation equivalent of oci_database_db_home

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::DatabaseDbHome",
    "Properties" : {
        "<a href="#dbsystemid" title="DbSystemId">DbSystemId</a>" : <i>String</i>,
        "<a href="#dbversion" title="DbVersion">DbVersion</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#source" title="Source">Source</a>" : <i>String</i>,
        "<a href="#vmclusterid" title="VmClusterId">VmClusterId</a>" : <i>String</i>,
        "<a href="#database" title="Database">Database</a>" : <i>[ &lt;a href=&#34;database.md&#34;&gt;Database&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#dbbackupconfig" title="DbBackupConfig">DbBackupConfig</a>" : <i>[ &lt;a href=&#34;dbbackupconfig.md&#34;&gt;DbBackupConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#backupdestinationdetails" title="BackupDestinationDetails">BackupDestinationDetails</a>" : <i>[ &lt;a href=&#34;backupdestinationdetails.md&#34;&gt;BackupDestinationDetails&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::DatabaseDbHome
Properties:
    <a href="#dbsystemid" title="DbSystemId">DbSystemId</a>: <i>String</i>
    <a href="#dbversion" title="DbVersion">DbVersion</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#source" title="Source">Source</a>: <i>String</i>
    <a href="#vmclusterid" title="VmClusterId">VmClusterId</a>: <i>String</i>
    <a href="#database" title="Database">Database</a>: <i>
      - &lt;a href=&#34;database.md&#34;&gt;Database&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#dbbackupconfig" title="DbBackupConfig">DbBackupConfig</a>: <i>
      - &lt;a href=&#34;dbbackupconfig.md&#34;&gt;DbBackupConfig&lt;/a&gt;</i>
    <a href="#backupdestinationdetails" title="BackupDestinationDetails">BackupDestinationDetails</a>: <i>
      - &lt;a href=&#34;backupdestinationdetails.md&#34;&gt;BackupDestinationDetails&lt;/a&gt;</i>
</pre>

## Properties

#### DbSystemId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmClusterId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Database

_Required_: No

_Type_: List of &lt;a href=&#34;database.md&#34;&gt;Database&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbBackupConfig

_Required_: No

_Type_: List of &lt;a href=&#34;dbbackupconfig.md&#34;&gt;DbBackupConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupDestinationDetails

_Required_: No

_Type_: List of &lt;a href=&#34;backupdestinationdetails.md&#34;&gt;BackupDestinationDetails&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CompartmentId

Returns the &lt;code&gt;CompartmentId&lt;/code&gt; value.

#### DbHomeLocation

Returns the &lt;code&gt;DbHomeLocation&lt;/code&gt; value.

#### LastPatchHistoryEntryId

Returns the &lt;code&gt;LastPatchHistoryEntryId&lt;/code&gt; value.

#### LifecycleDetails

Returns the &lt;code&gt;LifecycleDetails&lt;/code&gt; value.

#### State

Returns the &lt;code&gt;State&lt;/code&gt; value.

#### TimeCreated

Returns the &lt;code&gt;TimeCreated&lt;/code&gt; value.

