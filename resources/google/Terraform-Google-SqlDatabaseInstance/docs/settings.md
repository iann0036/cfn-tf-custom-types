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
    "<a href="#userlabels" title="UserLabels">UserLabels</a>" : <i>[ <a href="settings-userlabels.md">UserLabels</a>, ... ]</i>,
    "<a href="#backupconfiguration" title="BackupConfiguration">BackupConfiguration</a>" : <i>[ <a href="settings-backupconfiguration.md">BackupConfiguration</a>, ... ]</i>,
    "<a href="#databaseflags" title="DatabaseFlags">DatabaseFlags</a>" : <i>[ <a href="settings-databaseflags.md">DatabaseFlags</a>, ... ]</i>,
    "<a href="#ipconfiguration" title="IpConfiguration">IpConfiguration</a>" : <i>[ <a href="settings-ipconfiguration.md">IpConfiguration</a>, ... ]</i>,
    "<a href="#locationpreference" title="LocationPreference">LocationPreference</a>" : <i>[ <a href="settings-locationpreference.md">LocationPreference</a>, ... ]</i>,
    "<a href="#maintenancewindow" title="MaintenanceWindow">MaintenanceWindow</a>" : <i>[ <a href="settings-maintenancewindow.md">MaintenanceWindow</a>, ... ]</i>
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
      - <a href="settings-userlabels.md">UserLabels</a></i>
<a href="#backupconfiguration" title="BackupConfiguration">BackupConfiguration</a>: <i>
      - <a href="settings-backupconfiguration.md">BackupConfiguration</a></i>
<a href="#databaseflags" title="DatabaseFlags">DatabaseFlags</a>: <i>
      - <a href="settings-databaseflags.md">DatabaseFlags</a></i>
<a href="#ipconfiguration" title="IpConfiguration">IpConfiguration</a>: <i>
      - <a href="settings-ipconfiguration.md">IpConfiguration</a></i>
<a href="#locationpreference" title="LocationPreference">LocationPreference</a>: <i>
      - <a href="settings-locationpreference.md">LocationPreference</a></i>
<a href="#maintenancewindow" title="MaintenanceWindow">MaintenanceWindow</a>: <i>
      - <a href="settings-maintenancewindow.md">MaintenanceWindow</a></i>
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

_Type_: List of <a href="settings-userlabels.md">UserLabels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupConfiguration

_Required_: No

_Type_: List of <a href="settings-backupconfiguration.md">BackupConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseFlags

_Required_: No

_Type_: List of <a href="settings-databaseflags.md">DatabaseFlags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpConfiguration

_Required_: No

_Type_: List of <a href="settings-ipconfiguration.md">IpConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocationPreference

_Required_: No

_Type_: List of <a href="settings-locationpreference.md">LocationPreference</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintenanceWindow

_Required_: No

_Type_: List of <a href="settings-maintenancewindow.md">MaintenanceWindow</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

