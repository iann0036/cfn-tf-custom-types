# Terraform::OraclePaaS::DatabaseServiceInstance

The `oraclepaas_database_service_instance` resource creates and manages a an Oracle Database Cloud Service instance on the Oracle Cloud Platform.

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
        "<a href="#backups" title="Backups">Backups</a>" : <i>[ <a href="backups.md">Backups</a>, ... ]</i>,
        "<a href="#databaseconfiguration" title="DatabaseConfiguration">DatabaseConfiguration</a>" : <i>[ <a href="databaseconfiguration.md">DatabaseConfiguration</a>, ... ]</i>,
        "<a href="#defaultaccessrules" title="DefaultAccessRules">DefaultAccessRules</a>" : <i>[ <a href="defaultaccessrules.md">DefaultAccessRules</a>, ... ]</i>,
        "<a href="#hybriddisasterrecovery" title="HybridDisasterRecovery">HybridDisasterRecovery</a>" : <i>[ <a href="hybriddisasterrecovery.md">HybridDisasterRecovery</a>, ... ]</i>,
        "<a href="#instantiatefrombackup" title="InstantiateFromBackup">InstantiateFromBackup</a>" : <i>[ <a href="instantiatefrombackup.md">InstantiateFromBackup</a>, ... ]</i>,
        "<a href="#standby" title="Standby">Standby</a>" : <i>[ <a href="standby.md">Standby</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
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
      - <a href="backups.md">Backups</a></i>
    <a href="#databaseconfiguration" title="DatabaseConfiguration">DatabaseConfiguration</a>: <i>
      - <a href="databaseconfiguration.md">DatabaseConfiguration</a></i>
    <a href="#defaultaccessrules" title="DefaultAccessRules">DefaultAccessRules</a>: <i>
      - <a href="defaultaccessrules.md">DefaultAccessRules</a></i>
    <a href="#hybriddisasterrecovery" title="HybridDisasterRecovery">HybridDisasterRecovery</a>: <i>
      - <a href="hybriddisasterrecovery.md">HybridDisasterRecovery</a></i>
    <a href="#instantiatefrombackup" title="InstantiateFromBackup">InstantiateFromBackup</a>: <i>
      - <a href="instantiatefrombackup.md">InstantiateFromBackup</a></i>
    <a href="#standby" title="Standby">Standby</a>: <i>
      - <a href="standby.md">Standby</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AvailabilityDomain

Name of the availability domain within the region where the Oracle Database Cloud Service instance is to be provisioned.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BringYourOwnLicense

Specify if you want to use an existing perpetual license to Oracle Database to establish the right to use Oracle Database on the new instance.
Default value is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A description of the Service Instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredState

Specifies the desired state of the service instance. Allowed values are `start`, `stop`,
and `restart`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Edition

Database edition for the service instance. Possible values are `SE`, `EE`, `EE_HP`, or `EE_EP`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HighPerformanceStorage

Specifies whether the service instance will be provisioned with high performance storage.
Default value is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpNetwork

This attribute is only applicable to accounts where regions are supported. The three-part name of an IP network to which the service instance is added. For example: /Compute-identity_domain/user/object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpReservations

Groups one or more IP reservations in use on this service instance. This attribute is only applicable to accounts where regions are supported.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Level

Service level for the service instance. Possible values are `BASIC` or `PAAS`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Service Instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationEmail

The email address to send notifications around successful or unsuccessful completions of the instance-creation operation.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

Specifies the location where the service instance is provisioned (only for accounts where regions are supported).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shape

Desired compute shape. Possible values are `oc3`, `oc4`, `oc5`, `oc6`, `oc1m`, `oc2m`, `oc3m`, or `oc4m`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshPublicKey

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet

Name of the subnet within the region where the Oracle Database Cloud Service instance is to be provisioned.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubscriptionType

Billing unit. Possible values are `HOURLY` or `MONTHLY`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

Oracle Database software version; one of: `12.2.0.1`, `12.1.0.2`, or `11.2.0.4`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backups

_Required_: No

_Type_: List of <a href="backups.md">Backups</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseConfiguration

_Required_: No

_Type_: List of <a href="databaseconfiguration.md">DatabaseConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultAccessRules

_Required_: No

_Type_: List of <a href="defaultaccessrules.md">DefaultAccessRules</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HybridDisasterRecovery

_Required_: No

_Type_: List of <a href="hybriddisasterrecovery.md">HybridDisasterRecovery</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstantiateFromBackup

_Required_: No

_Type_: List of <a href="instantiatefrombackup.md">InstantiateFromBackup</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Standby

_Required_: No

_Type_: List of <a href="standby.md">Standby</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CloudStorageContainer

Returns the <code>CloudStorageContainer</code> value.

#### ComputeSiteName

Returns the <code>ComputeSiteName</code> value.

#### DbaasMonitorUrl

Returns the <code>DbaasMonitorUrl</code> value.

#### EmUrl

Returns the <code>EmUrl</code> value.

#### GlassfishUrl

Returns the <code>GlassfishUrl</code> value.

#### Id

Returns the <code>Id</code> value.

#### IdentityDomain

Returns the <code>IdentityDomain</code> value.

#### Status

Returns the <code>Status</code> value.

#### Uri

Returns the <code>Uri</code> value.

