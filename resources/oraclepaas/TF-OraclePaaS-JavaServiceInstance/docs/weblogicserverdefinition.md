# TF::OraclePaaS::JavaServiceInstance WeblogicServerDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#backupvolumesize" title="BackupVolumeSize">BackupVolumeSize</a>" : <i>String</i>,
    "<a href="#clustername" title="ClusterName">ClusterName</a>" : <i>String</i>,
    "<a href="#connectstring" title="ConnectString">ConnectString</a>" : <i>String</i>,
    "<a href="#ipreservations" title="IpReservations">IpReservations</a>" : <i>[ String, ... ]</i>,
    "<a href="#middlewarevolumesize" title="MiddlewareVolumeSize">MiddlewareVolumeSize</a>" : <i>String</i>,
    "<a href="#shape" title="Shape">Shape</a>" : <i>String</i>,
    "<a href="#upperstackproductname" title="UpperStackProductName">UpperStackProductName</a>" : <i>String</i>,
    "<a href="#admin" title="Admin">Admin</a>" : <i>[ <a href="admindefinition.md">AdminDefinition</a>, ... ]</i>,
    "<a href="#applicationdatabase" title="ApplicationDatabase">ApplicationDatabase</a>" : <i>[ <a href="applicationdatabasedefinition.md">ApplicationDatabaseDefinition</a>, ... ]</i>,
    "<a href="#cluster" title="Cluster">Cluster</a>" : <i>[ <a href="clusterdefinition.md">ClusterDefinition</a>, ... ]</i>,
    "<a href="#database" title="Database">Database</a>" : <i>[ <a href="databasedefinition.md">DatabaseDefinition</a>, ... ]</i>,
    "<a href="#domain" title="Domain">Domain</a>" : <i>[ <a href="domaindefinition.md">DomainDefinition</a>, ... ]</i>,
    "<a href="#managedservers" title="ManagedServers">ManagedServers</a>" : <i>[ <a href="managedserversdefinition.md">ManagedServersDefinition</a>, ... ]</i>,
    "<a href="#nodemanager" title="NodeManager">NodeManager</a>" : <i>[ <a href="nodemanagerdefinition.md">NodeManagerDefinition</a>, ... ]</i>,
    "<a href="#ports" title="Ports">Ports</a>" : <i>[ <a href="portsdefinition.md">PortsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#backupvolumesize" title="BackupVolumeSize">BackupVolumeSize</a>: <i>String</i>
<a href="#clustername" title="ClusterName">ClusterName</a>: <i>String</i>
<a href="#connectstring" title="ConnectString">ConnectString</a>: <i>String</i>
<a href="#ipreservations" title="IpReservations">IpReservations</a>: <i>
      - String</i>
<a href="#middlewarevolumesize" title="MiddlewareVolumeSize">MiddlewareVolumeSize</a>: <i>String</i>
<a href="#shape" title="Shape">Shape</a>: <i>String</i>
<a href="#upperstackproductname" title="UpperStackProductName">UpperStackProductName</a>: <i>String</i>
<a href="#admin" title="Admin">Admin</a>: <i>
      - <a href="admindefinition.md">AdminDefinition</a></i>
<a href="#applicationdatabase" title="ApplicationDatabase">ApplicationDatabase</a>: <i>
      - <a href="applicationdatabasedefinition.md">ApplicationDatabaseDefinition</a></i>
<a href="#cluster" title="Cluster">Cluster</a>: <i>
      - <a href="clusterdefinition.md">ClusterDefinition</a></i>
<a href="#database" title="Database">Database</a>: <i>
      - <a href="databasedefinition.md">DatabaseDefinition</a></i>
<a href="#domain" title="Domain">Domain</a>: <i>
      - <a href="domaindefinition.md">DomainDefinition</a></i>
<a href="#managedservers" title="ManagedServers">ManagedServers</a>: <i>
      - <a href="managedserversdefinition.md">ManagedServersDefinition</a></i>
<a href="#nodemanager" title="NodeManager">NodeManager</a>: <i>
      - <a href="nodemanagerdefinition.md">NodeManagerDefinition</a></i>
<a href="#ports" title="Ports">Ports</a>: <i>
      - <a href="portsdefinition.md">PortsDefinition</a></i>
</pre>

## Properties

#### BackupVolumeSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectString

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpReservations

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MiddlewareVolumeSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shape

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpperStackProductName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Admin

_Required_: No

_Type_: List of <a href="admindefinition.md">AdminDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationDatabase

_Required_: No

_Type_: List of <a href="applicationdatabasedefinition.md">ApplicationDatabaseDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cluster

_Required_: No

_Type_: List of <a href="clusterdefinition.md">ClusterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Database

_Required_: No

_Type_: List of <a href="databasedefinition.md">DatabaseDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

_Required_: No

_Type_: List of <a href="domaindefinition.md">DomainDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedServers

_Required_: No

_Type_: List of <a href="managedserversdefinition.md">ManagedServersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeManager

_Required_: No

_Type_: List of <a href="nodemanagerdefinition.md">NodeManagerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ports

_Required_: No

_Type_: List of <a href="portsdefinition.md">PortsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

