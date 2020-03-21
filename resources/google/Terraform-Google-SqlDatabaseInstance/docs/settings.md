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

This specifies when the instance should be
active. Can be either `ALWAYS`, `NEVER` or `ON_DEMAND`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorizedGaeApplications

This property is only applicable to First Generation instances.
First Generation instances are now deprecated, see [here](https://cloud.google.com/sql/docs/mysql/upgrade-2nd-gen)
for information on how to upgrade to Second Generation instances.
A list of Google App Engine (GAE) project names that are allowed to access this instance.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityType

This specifies whether a PostgreSQL instance
should be set up for high availability (`REGIONAL`) or single zone (`ZONAL`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrashSafeReplication

This property is only applicable to First Generation instances.
First Generation instances are now deprecated, see [here](https://cloud.google.com/sql/docs/mysql/upgrade-2nd-gen)
for information on how to upgrade to Second Generation instances.
Specific to read instances, indicates
when crash-safe replication flags are enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskAutoresize

Configuration to increase storage size automatically.  Note that future `terraform apply` calls will attempt to resize the disk to the value specified in `disk_size` - if this is set, do not set `disk_size`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSize

The size of data disk, in GB. Size of a running instance cannot be reduced but can be increased.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskType

The type of data disk: PD_SSD or PD_HDD.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PricingPlan

Pricing plan for this instance, can only be `PER_USE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplicationType

This property is only applicable to First Generation instances.
First Generation instances are now deprecated, see [here](https://cloud.google.com/sql/docs/mysql/upgrade-2nd-gen)
for information on how to upgrade to Second Generation instances.
Replication type for this instance, can be one of `ASYNCHRONOUS` or `SYNCHRONOUS`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tier

The machine type to use. See [tiers](https://cloud.google.com/sql/docs/admin-api/v1beta4/tiers)
for more details and supported versions. Postgres supports only shared-core machine types such as `db-f1-micro`,
and custom machine types such as `db-custom-2-13312`. See the [Custom Machine Type Documentation](https://cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#create) to learn about specifying custom machine types.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserLabels

A set of key/value user label pairs to assign to the instance.

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

