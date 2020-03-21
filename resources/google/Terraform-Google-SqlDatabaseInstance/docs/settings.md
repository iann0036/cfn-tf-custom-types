# Terraform::Google::SqlDatabaseInstance Settings

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#activationpolicy" title="ActivationPolicy">ActivationPolicy</a>" : <i>String</i>,
    "<a href="#authorizedgaeapplications" title="AuthorizedGaeApplications">AuthorizedGaeApplications</a>" : <i>[ String, ... ]</i>,
    "<a href="#availabilitytype" title="AvailabilityType">AvailabilityType</a>" : <i>String</i>,
    "<a href="#crashsafereplication" title="CrashSafeReplication">CrashSafeReplication</a>" : <i>Boolean</i>,
    "<a href="#diskautoresize" title="DiskAutoresize">DiskAutoresize</a>" : <i>Boolean</i>,
    "<a href="#disksize" title="DiskSize">DiskSize</a>" : <i>Double</i>,
    "<a href="#disktype" title="DiskType">DiskType</a>" : <i>String</i>,
    "<a href="#pricingplan" title="PricingPlan">PricingPlan</a>" : <i>String</i>,
    "<a href="#replicationtype" title="ReplicationType">ReplicationType</a>" : <i>String</i>,
    "<a href="#tier" title="Tier">Tier</a>" : <i>String</i>,
    "<a href="#userlabels" title="UserLabels">UserLabels</a>" : <i>[ &lt;a href=&#34;settings-userlabels.md&#34;&gt;UserLabels&lt;/a&gt;, ... ]</i>,
    "<a href="#backupconfiguration" title="BackupConfiguration">BackupConfiguration</a>" : <i>[ &lt;a href=&#34;settings-backupconfiguration.md&#34;&gt;BackupConfiguration&lt;/a&gt;, ... ]</i>,
    "<a href="#databaseflags" title="DatabaseFlags">DatabaseFlags</a>" : <i>[ &lt;a href=&#34;settings-databaseflags.md&#34;&gt;DatabaseFlags&lt;/a&gt;, ... ]</i>,
    "<a href="#ipconfiguration" title="IpConfiguration">IpConfiguration</a>" : <i>[ &lt;a href=&#34;settings-ipconfiguration.md&#34;&gt;IpConfiguration&lt;/a&gt;, ... ]</i>,
    "<a href="#locationpreference" title="LocationPreference">LocationPreference</a>" : <i>[ &lt;a href=&#34;settings-locationpreference.md&#34;&gt;LocationPreference&lt;/a&gt;, ... ]</i>,
    "<a href="#maintenancewindow" title="MaintenanceWindow">MaintenanceWindow</a>" : <i>[ &lt;a href=&#34;settings-maintenancewindow.md&#34;&gt;MaintenanceWindow&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#activationpolicy" title="ActivationPolicy">ActivationPolicy</a>: <i>String</i>
<a href="#authorizedgaeapplications" title="AuthorizedGaeApplications">AuthorizedGaeApplications</a>: <i>
      - String</i>
<a href="#availabilitytype" title="AvailabilityType">AvailabilityType</a>: <i>String</i>
<a href="#crashsafereplication" title="CrashSafeReplication">CrashSafeReplication</a>: <i>Boolean</i>
<a href="#diskautoresize" title="DiskAutoresize">DiskAutoresize</a>: <i>Boolean</i>
<a href="#disksize" title="DiskSize">DiskSize</a>: <i>Double</i>
<a href="#disktype" title="DiskType">DiskType</a>: <i>String</i>
<a href="#pricingplan" title="PricingPlan">PricingPlan</a>: <i>String</i>
<a href="#replicationtype" title="ReplicationType">ReplicationType</a>: <i>String</i>
<a href="#tier" title="Tier">Tier</a>: <i>String</i>
<a href="#userlabels" title="UserLabels">UserLabels</a>: <i>
      - &lt;a href=&#34;settings-userlabels.md&#34;&gt;UserLabels&lt;/a&gt;</i>
<a href="#backupconfiguration" title="BackupConfiguration">BackupConfiguration</a>: <i>
      - &lt;a href=&#34;settings-backupconfiguration.md&#34;&gt;BackupConfiguration&lt;/a&gt;</i>
<a href="#databaseflags" title="DatabaseFlags">DatabaseFlags</a>: <i>
      - &lt;a href=&#34;settings-databaseflags.md&#34;&gt;DatabaseFlags&lt;/a&gt;</i>
<a href="#ipconfiguration" title="IpConfiguration">IpConfiguration</a>: <i>
      - &lt;a href=&#34;settings-ipconfiguration.md&#34;&gt;IpConfiguration&lt;/a&gt;</i>
<a href="#locationpreference" title="LocationPreference">LocationPreference</a>: <i>
      - &lt;a href=&#34;settings-locationpreference.md&#34;&gt;LocationPreference&lt;/a&gt;</i>
<a href="#maintenancewindow" title="MaintenanceWindow">MaintenanceWindow</a>: <i>
      - &lt;a href=&#34;settings-maintenancewindow.md&#34;&gt;MaintenanceWindow&lt;/a&gt;</i>
</pre>

## Properties

#### ActivationPolicy

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorizedGaeApplications

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrashSafeReplication

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskAutoresize

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSize

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PricingPlan

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplicationType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tier

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserLabels

_Required_: No
_Type_: List of &lt;a href=&#34;settings-userlabels.md&#34;&gt;UserLabels&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupConfiguration

_Required_: No
_Type_: List of &lt;a href=&#34;settings-backupconfiguration.md&#34;&gt;BackupConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseFlags

_Required_: No
_Type_: List of &lt;a href=&#34;settings-databaseflags.md&#34;&gt;DatabaseFlags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpConfiguration

_Required_: No
_Type_: List of &lt;a href=&#34;settings-ipconfiguration.md&#34;&gt;IpConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocationPreference

_Required_: No
_Type_: List of &lt;a href=&#34;settings-locationpreference.md&#34;&gt;LocationPreference&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintenanceWindow

_Required_: No
_Type_: List of &lt;a href=&#34;settings-maintenancewindow.md&#34;&gt;MaintenanceWindow&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

