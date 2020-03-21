# Terraform::Google::SqlDatabaseInstance

CloudFormation equivalent of google_sql_database_instance

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::SqlDatabaseInstance",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#connectionname" title="ConnectionName">ConnectionName</a>" : <i>String</i>,
        "<a href="#databaseversion" title="DatabaseVersion">DatabaseVersion</a>" : <i>String</i>,
        "<a href="#firstipaddress" title="FirstIpAddress">FirstIpAddress</a>" : <i>String</i>,
        "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>[ &lt;a href=&#34;ipaddress.md&#34;&gt;IpAddress&lt;/a&gt;, ... ]</i>,
        "<a href="#masterinstancename" title="MasterInstanceName">MasterInstanceName</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#privateipaddress" title="PrivateIpAddress">PrivateIpAddress</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#publicipaddress" title="PublicIpAddress">PublicIpAddress</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#selflink" title="SelfLink">SelfLink</a>" : <i>String</i>,
        "<a href="#servercacert" title="ServerCaCert">ServerCaCert</a>" : <i>[ &lt;a href=&#34;servercacert.md&#34;&gt;ServerCaCert&lt;/a&gt;, ... ]</i>,
        "<a href="#serviceaccountemailaddress" title="ServiceAccountEmailAddress">ServiceAccountEmailAddress</a>" : <i>String</i>,
        "<a href="#replicaconfiguration" title="ReplicaConfiguration">ReplicaConfiguration</a>" : <i>[ &lt;a href=&#34;replicaconfiguration.md&#34;&gt;ReplicaConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#settings" title="Settings">Settings</a>" : <i>[ &lt;a href=&#34;settings.md&#34;&gt;Settings&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#backupconfiguration" title="BackupConfiguration">BackupConfiguration</a>" : <i>[ &lt;a href=&#34;backupconfiguration.md&#34;&gt;BackupConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#databaseflags" title="DatabaseFlags">DatabaseFlags</a>" : <i>[ &lt;a href=&#34;databaseflags.md&#34;&gt;DatabaseFlags&lt;/a&gt;, ... ]</i>,
        "<a href="#ipconfiguration" title="IpConfiguration">IpConfiguration</a>" : <i>[ &lt;a href=&#34;ipconfiguration.md&#34;&gt;IpConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#locationpreference" title="LocationPreference">LocationPreference</a>" : <i>[ &lt;a href=&#34;locationpreference.md&#34;&gt;LocationPreference&lt;/a&gt;, ... ]</i>,
        "<a href="#maintenancewindow" title="MaintenanceWindow">MaintenanceWindow</a>" : <i>[ &lt;a href=&#34;maintenancewindow.md&#34;&gt;MaintenanceWindow&lt;/a&gt;, ... ]</i>,
        "<a href="#authorizednetworks" title="AuthorizedNetworks">AuthorizedNetworks</a>" : <i>[ &lt;a href=&#34;authorizednetworks.md&#34;&gt;AuthorizedNetworks&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::SqlDatabaseInstance
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#connectionname" title="ConnectionName">ConnectionName</a>: <i>String</i>
    <a href="#databaseversion" title="DatabaseVersion">DatabaseVersion</a>: <i>String</i>
    <a href="#firstipaddress" title="FirstIpAddress">FirstIpAddress</a>: <i>String</i>
    <a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>
      - &lt;a href=&#34;ipaddress.md&#34;&gt;IpAddress&lt;/a&gt;</i>
    <a href="#masterinstancename" title="MasterInstanceName">MasterInstanceName</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#privateipaddress" title="PrivateIpAddress">PrivateIpAddress</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#publicipaddress" title="PublicIpAddress">PublicIpAddress</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#selflink" title="SelfLink">SelfLink</a>: <i>String</i>
    <a href="#servercacert" title="ServerCaCert">ServerCaCert</a>: <i>
      - &lt;a href=&#34;servercacert.md&#34;&gt;ServerCaCert&lt;/a&gt;</i>
    <a href="#serviceaccountemailaddress" title="ServiceAccountEmailAddress">ServiceAccountEmailAddress</a>: <i>String</i>
    <a href="#replicaconfiguration" title="ReplicaConfiguration">ReplicaConfiguration</a>: <i>
      - &lt;a href=&#34;replicaconfiguration.md&#34;&gt;ReplicaConfiguration&lt;/a&gt;</i>
    <a href="#settings" title="Settings">Settings</a>: <i>
      - &lt;a href=&#34;settings.md&#34;&gt;Settings&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#backupconfiguration" title="BackupConfiguration">BackupConfiguration</a>: <i>
      - &lt;a href=&#34;backupconfiguration.md&#34;&gt;BackupConfiguration&lt;/a&gt;</i>
    <a href="#databaseflags" title="DatabaseFlags">DatabaseFlags</a>: <i>
      - &lt;a href=&#34;databaseflags.md&#34;&gt;DatabaseFlags&lt;/a&gt;</i>
    <a href="#ipconfiguration" title="IpConfiguration">IpConfiguration</a>: <i>
      - &lt;a href=&#34;ipconfiguration.md&#34;&gt;IpConfiguration&lt;/a&gt;</i>
    <a href="#locationpreference" title="LocationPreference">LocationPreference</a>: <i>
      - &lt;a href=&#34;locationpreference.md&#34;&gt;LocationPreference&lt;/a&gt;</i>
    <a href="#maintenancewindow" title="MaintenanceWindow">MaintenanceWindow</a>: <i>
      - &lt;a href=&#34;maintenancewindow.md&#34;&gt;MaintenanceWindow&lt;/a&gt;</i>
    <a href="#authorizednetworks" title="AuthorizedNetworks">AuthorizedNetworks</a>: <i>
      - &lt;a href=&#34;authorizednetworks.md&#34;&gt;AuthorizedNetworks&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirstIpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

_Required_: No

_Type_: List of &lt;a href=&#34;ipaddress.md&#34;&gt;IpAddress&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterInstanceName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateIpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SelfLink

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerCaCert

_Required_: No

_Type_: List of &lt;a href=&#34;servercacert.md&#34;&gt;ServerCaCert&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccountEmailAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplicaConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;replicaconfiguration.md&#34;&gt;ReplicaConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Settings

_Required_: No

_Type_: List of &lt;a href=&#34;settings.md&#34;&gt;Settings&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;backupconfiguration.md&#34;&gt;BackupConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseFlags

_Required_: No

_Type_: List of &lt;a href=&#34;databaseflags.md&#34;&gt;DatabaseFlags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;ipconfiguration.md&#34;&gt;IpConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocationPreference

_Required_: No

_Type_: List of &lt;a href=&#34;locationpreference.md&#34;&gt;LocationPreference&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintenanceWindow

_Required_: No

_Type_: List of &lt;a href=&#34;maintenancewindow.md&#34;&gt;MaintenanceWindow&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorizedNetworks

_Required_: No

_Type_: List of &lt;a href=&#34;authorizednetworks.md&#34;&gt;AuthorizedNetworks&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ConnectionName

Returns the &lt;code&gt;ConnectionName&lt;/code&gt; value.

#### FirstIpAddress

Returns the &lt;code&gt;FirstIpAddress&lt;/code&gt; value.

#### IpAddress

Returns the &lt;code&gt;IpAddress&lt;/code&gt; value.

#### PrivateIpAddress

Returns the &lt;code&gt;PrivateIpAddress&lt;/code&gt; value.

#### PublicIpAddress

Returns the &lt;code&gt;PublicIpAddress&lt;/code&gt; value.

#### SelfLink

Returns the &lt;code&gt;SelfLink&lt;/code&gt; value.

#### ServerCaCert

Returns the &lt;code&gt;ServerCaCert&lt;/code&gt; value.

#### ServiceAccountEmailAddress

Returns the &lt;code&gt;ServiceAccountEmailAddress&lt;/code&gt; value.

