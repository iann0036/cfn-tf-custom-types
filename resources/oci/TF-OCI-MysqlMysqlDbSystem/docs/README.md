# TF::OCI::MysqlMysqlDbSystem

This resource provides the Mysql Db System resource in Oracle Cloud Infrastructure MySQL Database service.

Creates and launches a DB System.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::MysqlMysqlDbSystem",
    "Properties" : {
        "<a href="#adminpassword" title="AdminPassword">AdminPassword</a>" : <i>String</i>,
        "<a href="#adminusername" title="AdminUsername">AdminUsername</a>" : <i>String</i>,
        "<a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>" : <i>String</i>,
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#configurationid" title="ConfigurationId">ConfigurationId</a>" : <i>String</i>,
        "<a href="#datastoragesizeingb" title="DataStorageSizeInGb">DataStorageSizeInGb</a>" : <i>Double</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="channelsdefinition.md">ChannelsDefinition</a>, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#faultdomain" title="FaultDomain">FaultDomain</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="channelsdefinition2.md">ChannelsDefinition2</a>, ... ]</i>,
        "<a href="#hostnamelabel" title="HostnameLabel">HostnameLabel</a>" : <i>String</i>,
        "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>String</i>,
        "<a href="#ishighlyavailable" title="IsHighlyAvailable">IsHighlyAvailable</a>" : <i>Boolean</i>,
        "<a href="#mysqlversion" title="MysqlVersion">MysqlVersion</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#portx" title="PortX">PortX</a>" : <i>Double</i>,
        "<a href="#shapename" title="ShapeName">ShapeName</a>" : <i>String</i>,
        "<a href="#shutdowntype" title="ShutdownType">ShutdownType</a>" : <i>String</i>,
        "<a href="#state" title="State">State</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#backuppolicy" title="BackupPolicy">BackupPolicy</a>" : <i>[ <a href="backuppolicydefinition.md">BackupPolicyDefinition</a>, ... ]</i>,
        "<a href="#maintenance" title="Maintenance">Maintenance</a>" : <i>[ <a href="maintenancedefinition.md">MaintenanceDefinition</a>, ... ]</i>,
        "<a href="#source" title="Source">Source</a>" : <i>[ <a href="channelsdefinition4.md">ChannelsDefinition4</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::MysqlMysqlDbSystem
Properties:
    <a href="#adminpassword" title="AdminPassword">AdminPassword</a>: <i>String</i>
    <a href="#adminusername" title="AdminUsername">AdminUsername</a>: <i>String</i>
    <a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>: <i>String</i>
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#configurationid" title="ConfigurationId">ConfigurationId</a>: <i>String</i>
    <a href="#datastoragesizeingb" title="DataStorageSizeInGb">DataStorageSizeInGb</a>: <i>Double</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="channelsdefinition.md">ChannelsDefinition</a></i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#faultdomain" title="FaultDomain">FaultDomain</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="channelsdefinition2.md">ChannelsDefinition2</a></i>
    <a href="#hostnamelabel" title="HostnameLabel">HostnameLabel</a>: <i>String</i>
    <a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>String</i>
    <a href="#ishighlyavailable" title="IsHighlyAvailable">IsHighlyAvailable</a>: <i>Boolean</i>
    <a href="#mysqlversion" title="MysqlVersion">MysqlVersion</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#portx" title="PortX">PortX</a>: <i>Double</i>
    <a href="#shapename" title="ShapeName">ShapeName</a>: <i>String</i>
    <a href="#shutdowntype" title="ShutdownType">ShutdownType</a>: <i>String</i>
    <a href="#state" title="State">State</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#backuppolicy" title="BackupPolicy">BackupPolicy</a>: <i>
      - <a href="backuppolicydefinition.md">BackupPolicyDefinition</a></i>
    <a href="#maintenance" title="Maintenance">Maintenance</a>: <i>
      - <a href="maintenancedefinition.md">MaintenanceDefinition</a></i>
    <a href="#source" title="Source">Source</a>: <i>
      - <a href="channelsdefinition4.md">ChannelsDefinition4</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AdminPassword

The password for the administrative user. The password must be between 8 and 32 characters long, and must contain at least 1 numeric character, 1 lowercase character, 1 uppercase character, and 1 special (nonalphanumeric) character.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminUsername

The username for the administrative user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityDomain

The availability domain on which to deploy the Read/Write endpoint. This defines the preferred primary instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompartmentId

The OCID of the compartment.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigurationId

The OCID of the Configuration to be used for this DB System.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataStorageSizeInGb

Initial size of the data volume in GBs that will be created and attached. Keep in mind that this only specifies the size of the database data volume, the log volume for the database will be scaled appropriately with its shape. It is required if you are creating a new database. It cannot be set if you are creating a database from a backup.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

_Required_: No

_Type_: List of <a href="channelsdefinition.md">ChannelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

(Updatable) User-provided data about the DB System.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

(Updatable) The user-friendly name for the DB System. It does not have to be unique.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FaultDomain

The fault domain on which to deploy the Read/Write endpoint. This defines the preferred primary instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

_Required_: No

_Type_: List of <a href="channelsdefinition2.md">ChannelsDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostnameLabel

The hostname for the primary endpoint of the DB System. Used for DNS.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

The IP address the DB System is configured to listen on. A private IP address of your choice to assign to the primary endpoint of the DB System. Must be an available IP address within the subnet's CIDR. If you don't specify a value, Oracle automatically assigns a private IP address from the subnet. This should be a "dotted-quad" style IPv4 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsHighlyAvailable

(Updatable) Specifies if the DB System is highly available.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MysqlVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

The port for primary endpoint of the DB System to listen on.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortX

The TCP network port on which X Plugin listens for connections. This is the X Plugin equivalent of port.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShapeName

The name of the shape. The shape determines the resources allocated
* CPU cores and memory for VM shapes; CPU cores, memory and storage for non-VM (or bare metal) shapes. To get a list of shapes, use the [ListShapes](https://docs.cloud.oracle.com/iaas/api/#/en/mysql/20190415/ShapeSummary/ListShapes) operation.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShutdownType

It is applicable only for stopping a DB System. Could be set to `FAST`, `SLOW` or `IMMEDIATE`. Default value is `FAST`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

(Updatable) The target state for the DB System. Could be set to `ACTIVE` or `INACTIVE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

The OCID of the subnet the DB System is associated with.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupPolicy

_Required_: No

_Type_: List of <a href="backuppolicydefinition.md">BackupPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Maintenance

_Required_: No

_Type_: List of <a href="maintenancedefinition.md">MaintenanceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: No

_Type_: List of <a href="channelsdefinition4.md">ChannelsDefinition4</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AnalyticsCluster

Returns the <code>AnalyticsCluster</code> value.

#### Channels

Returns the <code>Channels</code> value.

#### CurrentPlacement

Returns the <code>CurrentPlacement</code> value.

#### Endpoints

Returns the <code>Endpoints</code> value.

#### HeatWaveCluster

Returns the <code>HeatWaveCluster</code> value.

#### Id

Returns the <code>Id</code> value.

#### IsAnalyticsClusterAttached

Returns the <code>IsAnalyticsClusterAttached</code> value.

#### IsHeatWaveClusterAttached

Returns the <code>IsHeatWaveClusterAttached</code> value.

#### LifecycleDetails

Returns the <code>LifecycleDetails</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

#### TimeUpdated

Returns the <code>TimeUpdated</code> value.

