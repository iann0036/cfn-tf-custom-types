# Terraform::OraclePaaS::DatabaseServiceInstance

CloudFormation equivalent of oraclepaas_database_service_instance

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OraclePaaS::DatabaseServiceInstance",
    "Properties" : {
        "<a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>" : <i>String</i>,
        "<a href="#bringyourownlicense" title="BringYourOwnLicense">BringYourOwnLicense</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#desiredstate" title="DesiredState">DesiredState</a>" : <i>String</i>,
        "<a href="#edition" title="Edition">Edition</a>" : <i>String</i>,
        "<a href="#highperformancestorage" title="HighPerformanceStorage">HighPerformanceStorage</a>" : <i>Boolean</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#ipnetwork" title="IpNetwork">IpNetwork</a>" : <i>String</i>,
        "<a href="#ipreservations" title="IpReservations">IpReservations</a>" : <i>[ String, ... ]</i>,
        "<a href="#level" title="Level">Level</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notificationemail" title="NotificationEmail">NotificationEmail</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#shape" title="Shape">Shape</a>" : <i>String</i>,
        "<a href="#sshpublickey" title="SshPublicKey">SshPublicKey</a>" : <i>String</i>,
        "<a href="#subnet" title="Subnet">Subnet</a>" : <i>String</i>,
        "<a href="#subscriptiontype" title="SubscriptionType">SubscriptionType</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>,
        "<a href="#backups" title="Backups">Backups</a>" : <i>[ &lt;a href=&#34;backups.md&#34;&gt;Backups&lt;/a&gt;, ... ]</i>,
        "<a href="#databaseconfiguration" title="DatabaseConfiguration">DatabaseConfiguration</a>" : <i>[ &lt;a href=&#34;databaseconfiguration.md&#34;&gt;DatabaseConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#defaultaccessrules" title="DefaultAccessRules">DefaultAccessRules</a>" : <i>[ &lt;a href=&#34;defaultaccessrules.md&#34;&gt;DefaultAccessRules&lt;/a&gt;, ... ]</i>,
        "<a href="#hybriddisasterrecovery" title="HybridDisasterRecovery">HybridDisasterRecovery</a>" : <i>[ &lt;a href=&#34;hybriddisasterrecovery.md&#34;&gt;HybridDisasterRecovery&lt;/a&gt;, ... ]</i>,
        "<a href="#instantiatefrombackup" title="InstantiateFromBackup">InstantiateFromBackup</a>" : <i>[ &lt;a href=&#34;instantiatefrombackup.md&#34;&gt;InstantiateFromBackup&lt;/a&gt;, ... ]</i>,
        "<a href="#standby" title="Standby">Standby</a>" : <i>[ &lt;a href=&#34;standby.md&#34;&gt;Standby&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OraclePaaS::DatabaseServiceInstance
Properties:
    <a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>: <i>String</i>
    <a href="#bringyourownlicense" title="BringYourOwnLicense">BringYourOwnLicense</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#desiredstate" title="DesiredState">DesiredState</a>: <i>String</i>
    <a href="#edition" title="Edition">Edition</a>: <i>String</i>
    <a href="#highperformancestorage" title="HighPerformanceStorage">HighPerformanceStorage</a>: <i>Boolean</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#ipnetwork" title="IpNetwork">IpNetwork</a>: <i>String</i>
    <a href="#ipreservations" title="IpReservations">IpReservations</a>: <i>
      - String</i>
    <a href="#level" title="Level">Level</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notificationemail" title="NotificationEmail">NotificationEmail</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#shape" title="Shape">Shape</a>: <i>String</i>
    <a href="#sshpublickey" title="SshPublicKey">SshPublicKey</a>: <i>String</i>
    <a href="#subnet" title="Subnet">Subnet</a>: <i>String</i>
    <a href="#subscriptiontype" title="SubscriptionType">SubscriptionType</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
    <a href="#backups" title="Backups">Backups</a>: <i>
      - &lt;a href=&#34;backups.md&#34;&gt;Backups&lt;/a&gt;</i>
    <a href="#databaseconfiguration" title="DatabaseConfiguration">DatabaseConfiguration</a>: <i>
      - &lt;a href=&#34;databaseconfiguration.md&#34;&gt;DatabaseConfiguration&lt;/a&gt;</i>
    <a href="#defaultaccessrules" title="DefaultAccessRules">DefaultAccessRules</a>: <i>
      - &lt;a href=&#34;defaultaccessrules.md&#34;&gt;DefaultAccessRules&lt;/a&gt;</i>
    <a href="#hybriddisasterrecovery" title="HybridDisasterRecovery">HybridDisasterRecovery</a>: <i>
      - &lt;a href=&#34;hybriddisasterrecovery.md&#34;&gt;HybridDisasterRecovery&lt;/a&gt;</i>
    <a href="#instantiatefrombackup" title="InstantiateFromBackup">InstantiateFromBackup</a>: <i>
      - &lt;a href=&#34;instantiatefrombackup.md&#34;&gt;InstantiateFromBackup&lt;/a&gt;</i>
    <a href="#standby" title="Standby">Standby</a>: <i>
      - &lt;a href=&#34;standby.md&#34;&gt;Standby&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### AvailabilityDomain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BringYourOwnLicense

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredState

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Edition

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HighPerformanceStorage

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpNetwork

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpReservations

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Level

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationEmail

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shape

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshPublicKey

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubscriptionType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backups

_Required_: No

_Type_: List of &lt;a href=&#34;backups.md&#34;&gt;Backups&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;databaseconfiguration.md&#34;&gt;DatabaseConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultAccessRules

_Required_: No

_Type_: List of &lt;a href=&#34;defaultaccessrules.md&#34;&gt;DefaultAccessRules&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HybridDisasterRecovery

_Required_: No

_Type_: List of &lt;a href=&#34;hybriddisasterrecovery.md&#34;&gt;HybridDisasterRecovery&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstantiateFromBackup

_Required_: No

_Type_: List of &lt;a href=&#34;instantiatefrombackup.md&#34;&gt;InstantiateFromBackup&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Standby

_Required_: No

_Type_: List of &lt;a href=&#34;standby.md&#34;&gt;Standby&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CloudStorageContainer

Returns the &lt;code&gt;CloudStorageContainer&lt;/code&gt; value.

#### ComputeSiteName

Returns the &lt;code&gt;ComputeSiteName&lt;/code&gt; value.

#### DbaasMonitorUrl

Returns the &lt;code&gt;DbaasMonitorUrl&lt;/code&gt; value.

#### EmUrl

Returns the &lt;code&gt;EmUrl&lt;/code&gt; value.

#### GlassfishUrl

Returns the &lt;code&gt;GlassfishUrl&lt;/code&gt; value.

#### IdentityDomain

Returns the &lt;code&gt;IdentityDomain&lt;/code&gt; value.

#### Status

Returns the &lt;code&gt;Status&lt;/code&gt; value.

#### Uri

Returns the &lt;code&gt;Uri&lt;/code&gt; value.

