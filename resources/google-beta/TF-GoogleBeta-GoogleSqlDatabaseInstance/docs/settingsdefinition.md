# TF::GoogleBeta::GoogleSqlDatabaseInstance SettingsDefinition

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
    "<a href="#diskautoresizelimit" title="DiskAutoresizeLimit">DiskAutoresizeLimit</a>" : <i>Double</i>,
    "<a href="#disksize" title="DiskSize">DiskSize</a>" : <i>Double</i>,
    "<a href="#disktype" title="DiskType">DiskType</a>" : <i>String</i>,
    "<a href="#pricingplan" title="PricingPlan">PricingPlan</a>" : <i>String</i>,
    "<a href="#replicationtype" title="ReplicationType">ReplicationType</a>" : <i>String</i>,
    "<a href="#tier" title="Tier">Tier</a>" : <i>String</i>,
    "<a href="#userlabels" title="UserLabels">UserLabels</a>" : <i>[ <a href="userlabelsdefinition.md">UserLabelsDefinition</a>, ... ]</i>,
    "<a href="#backupconfiguration" title="BackupConfiguration">BackupConfiguration</a>" : <i>[ <a href="backupconfigurationdefinition.md">BackupConfigurationDefinition</a>, ... ]</i>,
    "<a href="#databaseflags" title="DatabaseFlags">DatabaseFlags</a>" : <i>[ <a href="databaseflagsdefinition.md">DatabaseFlagsDefinition</a>, ... ]</i>,
    "<a href="#insightsconfig" title="InsightsConfig">InsightsConfig</a>" : <i>[ <a href="insightsconfigdefinition.md">InsightsConfigDefinition</a>, ... ]</i>,
    "<a href="#ipconfiguration" title="IpConfiguration">IpConfiguration</a>" : <i>[ <a href="ipconfigurationdefinition.md">IpConfigurationDefinition</a>, ... ]</i>,
    "<a href="#locationpreference" title="LocationPreference">LocationPreference</a>" : <i>[ <a href="locationpreferencedefinition.md">LocationPreferenceDefinition</a>, ... ]</i>,
    "<a href="#maintenancewindow" title="MaintenanceWindow">MaintenanceWindow</a>" : <i>[ <a href="maintenancewindowdefinition.md">MaintenanceWindowDefinition</a>, ... ]</i>
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
<a href="#diskautoresizelimit" title="DiskAutoresizeLimit">DiskAutoresizeLimit</a>: <i>Double</i>
<a href="#disksize" title="DiskSize">DiskSize</a>: <i>Double</i>
<a href="#disktype" title="DiskType">DiskType</a>: <i>String</i>
<a href="#pricingplan" title="PricingPlan">PricingPlan</a>: <i>String</i>
<a href="#replicationtype" title="ReplicationType">ReplicationType</a>: <i>String</i>
<a href="#tier" title="Tier">Tier</a>: <i>String</i>
<a href="#userlabels" title="UserLabels">UserLabels</a>: <i>
      - <a href="userlabelsdefinition.md">UserLabelsDefinition</a></i>
<a href="#backupconfiguration" title="BackupConfiguration">BackupConfiguration</a>: <i>
      - <a href="backupconfigurationdefinition.md">BackupConfigurationDefinition</a></i>
<a href="#databaseflags" title="DatabaseFlags">DatabaseFlags</a>: <i>
      - <a href="databaseflagsdefinition.md">DatabaseFlagsDefinition</a></i>
<a href="#insightsconfig" title="InsightsConfig">InsightsConfig</a>: <i>
      - <a href="insightsconfigdefinition.md">InsightsConfigDefinition</a></i>
<a href="#ipconfiguration" title="IpConfiguration">IpConfiguration</a>: <i>
      - <a href="ipconfigurationdefinition.md">IpConfigurationDefinition</a></i>
<a href="#locationpreference" title="LocationPreference">LocationPreference</a>: <i>
      - <a href="locationpreferencedefinition.md">LocationPreferenceDefinition</a></i>
<a href="#maintenancewindow" title="MaintenanceWindow">MaintenanceWindow</a>: <i>
      - <a href="maintenancewindowdefinition.md">MaintenanceWindowDefinition</a></i>
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

#### DiskAutoresizeLimit

_Required_: No

_Type_: Double

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

_Type_: List of <a href="userlabelsdefinition.md">UserLabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupConfiguration

_Required_: No

_Type_: List of <a href="backupconfigurationdefinition.md">BackupConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseFlags

_Required_: No

_Type_: List of <a href="databaseflagsdefinition.md">DatabaseFlagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsightsConfig

_Required_: No

_Type_: List of <a href="insightsconfigdefinition.md">InsightsConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpConfiguration

_Required_: No

_Type_: List of <a href="ipconfigurationdefinition.md">IpConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocationPreference

_Required_: No

_Type_: List of <a href="locationpreferencedefinition.md">LocationPreferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintenanceWindow

_Required_: No

_Type_: List of <a href="maintenancewindowdefinition.md">MaintenanceWindowDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

