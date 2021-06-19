# TF::OCI::MysqlMysqlBackup DbSystemSnapshotDefinition8

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#adminusername" title="AdminUsername">AdminUsername</a>" : <i>String</i>,
    "<a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>" : <i>String</i>,
    "<a href="#backuppolicy" title="BackupPolicy">BackupPolicy</a>" : <i>[ <a href="dbsystemsnapshotdefinition3.md">DbSystemSnapshotDefinition3</a>, ... ]</i>,
    "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
    "<a href="#configurationid" title="ConfigurationId">ConfigurationId</a>" : <i>String</i>,
    "<a href="#datastoragesizeingb" title="DataStorageSizeInGb">DataStorageSizeInGb</a>" : <i>Double</i>,
    "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="dbsystemsnapshotdefinition.md">DbSystemSnapshotDefinition</a>, ... ]</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
    "<a href="#endpoints" title="Endpoints">Endpoints</a>" : <i>[ <a href="dbsystemsnapshotdefinition5.md">DbSystemSnapshotDefinition5</a>, ... ]</i>,
    "<a href="#faultdomain" title="FaultDomain">FaultDomain</a>" : <i>String</i>,
    "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="dbsystemsnapshotdefinition2.md">DbSystemSnapshotDefinition2</a>, ... ]</i>,
    "<a href="#hostnamelabel" title="HostnameLabel">HostnameLabel</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>String</i>,
    "<a href="#ishighlyavailable" title="IsHighlyAvailable">IsHighlyAvailable</a>" : <i>Boolean</i>,
    "<a href="#maintenance" title="Maintenance">Maintenance</a>" : <i>[ <a href="dbsystemsnapshotdefinition7.md">DbSystemSnapshotDefinition7</a>, ... ]</i>,
    "<a href="#mysqlversion" title="MysqlVersion">MysqlVersion</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#portx" title="PortX">PortX</a>" : <i>Double</i>,
    "<a href="#shapename" title="ShapeName">ShapeName</a>" : <i>String</i>,
    "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#adminusername" title="AdminUsername">AdminUsername</a>: <i>String</i>
<a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>: <i>String</i>
<a href="#backuppolicy" title="BackupPolicy">BackupPolicy</a>: <i>
      - <a href="dbsystemsnapshotdefinition3.md">DbSystemSnapshotDefinition3</a></i>
<a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
<a href="#configurationid" title="ConfigurationId">ConfigurationId</a>: <i>String</i>
<a href="#datastoragesizeingb" title="DataStorageSizeInGb">DataStorageSizeInGb</a>: <i>Double</i>
<a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="dbsystemsnapshotdefinition.md">DbSystemSnapshotDefinition</a></i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
<a href="#endpoints" title="Endpoints">Endpoints</a>: <i>
      - <a href="dbsystemsnapshotdefinition5.md">DbSystemSnapshotDefinition5</a></i>
<a href="#faultdomain" title="FaultDomain">FaultDomain</a>: <i>String</i>
<a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="dbsystemsnapshotdefinition2.md">DbSystemSnapshotDefinition2</a></i>
<a href="#hostnamelabel" title="HostnameLabel">HostnameLabel</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>String</i>
<a href="#ishighlyavailable" title="IsHighlyAvailable">IsHighlyAvailable</a>: <i>Boolean</i>
<a href="#maintenance" title="Maintenance">Maintenance</a>: <i>
      - <a href="dbsystemsnapshotdefinition7.md">DbSystemSnapshotDefinition7</a></i>
<a href="#mysqlversion" title="MysqlVersion">MysqlVersion</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#portx" title="PortX">PortX</a>: <i>Double</i>
<a href="#shapename" title="ShapeName">ShapeName</a>: <i>String</i>
<a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
</pre>

## Properties

#### AdminUsername

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityDomain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupPolicy

_Required_: No

_Type_: List of <a href="dbsystemsnapshotdefinition3.md">DbSystemSnapshotDefinition3</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompartmentId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigurationId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataStorageSizeInGb

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

_Required_: No

_Type_: List of <a href="dbsystemsnapshotdefinition.md">DbSystemSnapshotDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Endpoints

_Required_: No

_Type_: List of <a href="dbsystemsnapshotdefinition5.md">DbSystemSnapshotDefinition5</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FaultDomain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

_Required_: No

_Type_: List of <a href="dbsystemsnapshotdefinition2.md">DbSystemSnapshotDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostnameLabel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsHighlyAvailable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Maintenance

_Required_: No

_Type_: List of <a href="dbsystemsnapshotdefinition7.md">DbSystemSnapshotDefinition7</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MysqlVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortX

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShapeName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

