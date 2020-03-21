# Terraform::OraclePaaS::JavaServiceInstance

CloudFormation equivalent of oraclepaas_java_service_instance

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OraclePaaS::JavaServiceInstance",
    "Properties" : {
        "<a href="#assignpublicip" title="AssignPublicIp">AssignPublicIp</a>" : <i>Boolean</i>,
        "<a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>" : <i>String</i>,
        "<a href="#backupdestination" title="BackupDestination">BackupDestination</a>" : <i>String</i>,
        "<a href="#bringyourownlicense" title="BringYourOwnLicense">BringYourOwnLicense</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#desiredstate" title="DesiredState">DesiredState</a>" : <i>String</i>,
        "<a href="#edition" title="Edition">Edition</a>" : <i>String</i>,
        "<a href="#enableadminconsole" title="EnableAdminConsole">EnableAdminConsole</a>" : <i>Boolean</i>,
        "<a href="#forcedelete" title="ForceDelete">ForceDelete</a>" : <i>Boolean</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#ipnetwork" title="IpNetwork">IpNetwork</a>" : <i>String</i>,
        "<a href="#level" title="Level">Level</a>" : <i>String</i>,
        "<a href="#meteringfrequency" title="MeteringFrequency">MeteringFrequency</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notificationemail" title="NotificationEmail">NotificationEmail</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#serviceversion" title="ServiceVersion">ServiceVersion</a>" : <i>String</i>,
        "<a href="#snapshotname" title="SnapshotName">SnapshotName</a>" : <i>String</i>,
        "<a href="#sourceservicename" title="SourceServiceName">SourceServiceName</a>" : <i>String</i>,
        "<a href="#sshpublickey" title="SshPublicKey">SshPublicKey</a>" : <i>String</i>,
        "<a href="#subnet" title="Subnet">Subnet</a>" : <i>String</i>,
        "<a href="#useidentityservice" title="UseIdentityService">UseIdentityService</a>" : <i>Boolean</i>,
        "<a href="#backups" title="Backups">Backups</a>" : <i>[ &lt;a href=&#34;backups.md&#34;&gt;Backups&lt;/a&gt;, ... ]</i>,
        "<a href="#loadbalancer" title="LoadBalancer">LoadBalancer</a>" : <i>[ &lt;a href=&#34;loadbalancer.md&#34;&gt;LoadBalancer&lt;/a&gt;, ... ]</i>,
        "<a href="#oracletrafficdirector" title="OracleTrafficDirector">OracleTrafficDirector</a>" : <i>[ &lt;a href=&#34;oracletrafficdirector.md&#34;&gt;OracleTrafficDirector&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#weblogicserver" title="WeblogicServer">WeblogicServer</a>" : <i>[ &lt;a href=&#34;weblogicserver.md&#34;&gt;WeblogicServer&lt;/a&gt;, ... ]</i>,
        "<a href="#admin" title="Admin">Admin</a>" : <i>[ &lt;a href=&#34;admin.md&#34;&gt;Admin&lt;/a&gt;, ... ]</i>,
        "<a href="#listener" title="Listener">Listener</a>" : <i>[ &lt;a href=&#34;listener.md&#34;&gt;Listener&lt;/a&gt;, ... ]</i>,
        "<a href="#applicationdatabase" title="ApplicationDatabase">ApplicationDatabase</a>" : <i>[ &lt;a href=&#34;applicationdatabase.md&#34;&gt;ApplicationDatabase&lt;/a&gt;, ... ]</i>,
        "<a href="#cluster" title="Cluster">Cluster</a>" : <i>[ &lt;a href=&#34;cluster.md&#34;&gt;Cluster&lt;/a&gt;, ... ]</i>,
        "<a href="#database" title="Database">Database</a>" : <i>[ &lt;a href=&#34;database.md&#34;&gt;Database&lt;/a&gt;, ... ]</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>[ &lt;a href=&#34;domain.md&#34;&gt;Domain&lt;/a&gt;, ... ]</i>,
        "<a href="#managedservers" title="ManagedServers">ManagedServers</a>" : <i>[ &lt;a href=&#34;managedservers.md&#34;&gt;ManagedServers&lt;/a&gt;, ... ]</i>,
        "<a href="#nodemanager" title="NodeManager">NodeManager</a>" : <i>[ &lt;a href=&#34;nodemanager.md&#34;&gt;NodeManager&lt;/a&gt;, ... ]</i>,
        "<a href="#ports" title="Ports">Ports</a>" : <i>[ &lt;a href=&#34;ports.md&#34;&gt;Ports&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OraclePaaS::JavaServiceInstance
Properties:
    <a href="#assignpublicip" title="AssignPublicIp">AssignPublicIp</a>: <i>Boolean</i>
    <a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>: <i>String</i>
    <a href="#backupdestination" title="BackupDestination">BackupDestination</a>: <i>String</i>
    <a href="#bringyourownlicense" title="BringYourOwnLicense">BringYourOwnLicense</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#desiredstate" title="DesiredState">DesiredState</a>: <i>String</i>
    <a href="#edition" title="Edition">Edition</a>: <i>String</i>
    <a href="#enableadminconsole" title="EnableAdminConsole">EnableAdminConsole</a>: <i>Boolean</i>
    <a href="#forcedelete" title="ForceDelete">ForceDelete</a>: <i>Boolean</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#ipnetwork" title="IpNetwork">IpNetwork</a>: <i>String</i>
    <a href="#level" title="Level">Level</a>: <i>String</i>
    <a href="#meteringfrequency" title="MeteringFrequency">MeteringFrequency</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notificationemail" title="NotificationEmail">NotificationEmail</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#serviceversion" title="ServiceVersion">ServiceVersion</a>: <i>String</i>
    <a href="#snapshotname" title="SnapshotName">SnapshotName</a>: <i>String</i>
    <a href="#sourceservicename" title="SourceServiceName">SourceServiceName</a>: <i>String</i>
    <a href="#sshpublickey" title="SshPublicKey">SshPublicKey</a>: <i>String</i>
    <a href="#subnet" title="Subnet">Subnet</a>: <i>String</i>
    <a href="#useidentityservice" title="UseIdentityService">UseIdentityService</a>: <i>Boolean</i>
    <a href="#backups" title="Backups">Backups</a>: <i>
      - &lt;a href=&#34;backups.md&#34;&gt;Backups&lt;/a&gt;</i>
    <a href="#loadbalancer" title="LoadBalancer">LoadBalancer</a>: <i>
      - &lt;a href=&#34;loadbalancer.md&#34;&gt;LoadBalancer&lt;/a&gt;</i>
    <a href="#oracletrafficdirector" title="OracleTrafficDirector">OracleTrafficDirector</a>: <i>
      - &lt;a href=&#34;oracletrafficdirector.md&#34;&gt;OracleTrafficDirector&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#weblogicserver" title="WeblogicServer">WeblogicServer</a>: <i>
      - &lt;a href=&#34;weblogicserver.md&#34;&gt;WeblogicServer&lt;/a&gt;</i>
    <a href="#admin" title="Admin">Admin</a>: <i>
      - &lt;a href=&#34;admin.md&#34;&gt;Admin&lt;/a&gt;</i>
    <a href="#listener" title="Listener">Listener</a>: <i>
      - &lt;a href=&#34;listener.md&#34;&gt;Listener&lt;/a&gt;</i>
    <a href="#applicationdatabase" title="ApplicationDatabase">ApplicationDatabase</a>: <i>
      - &lt;a href=&#34;applicationdatabase.md&#34;&gt;ApplicationDatabase&lt;/a&gt;</i>
    <a href="#cluster" title="Cluster">Cluster</a>: <i>
      - &lt;a href=&#34;cluster.md&#34;&gt;Cluster&lt;/a&gt;</i>
    <a href="#database" title="Database">Database</a>: <i>
      - &lt;a href=&#34;database.md&#34;&gt;Database&lt;/a&gt;</i>
    <a href="#domain" title="Domain">Domain</a>: <i>
      - &lt;a href=&#34;domain.md&#34;&gt;Domain&lt;/a&gt;</i>
    <a href="#managedservers" title="ManagedServers">ManagedServers</a>: <i>
      - &lt;a href=&#34;managedservers.md&#34;&gt;ManagedServers&lt;/a&gt;</i>
    <a href="#nodemanager" title="NodeManager">NodeManager</a>: <i>
      - &lt;a href=&#34;nodemanager.md&#34;&gt;NodeManager&lt;/a&gt;</i>
    <a href="#ports" title="Ports">Ports</a>: <i>
      - &lt;a href=&#34;ports.md&#34;&gt;Ports&lt;/a&gt;</i>
</pre>

## Properties

#### AssignPublicIp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityDomain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupDestination

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

#### EnableAdminConsole

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceDelete

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

#### Level

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MeteringFrequency

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

#### ServiceVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceServiceName

_Required_: No

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

#### UseIdentityService

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backups

_Required_: No

_Type_: List of &lt;a href=&#34;backups.md&#34;&gt;Backups&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancer

_Required_: No

_Type_: List of &lt;a href=&#34;loadbalancer.md&#34;&gt;LoadBalancer&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OracleTrafficDirector

_Required_: No

_Type_: List of &lt;a href=&#34;oracletrafficdirector.md&#34;&gt;OracleTrafficDirector&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeblogicServer

_Required_: No

_Type_: List of &lt;a href=&#34;weblogicserver.md&#34;&gt;WeblogicServer&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Admin

_Required_: No

_Type_: List of &lt;a href=&#34;admin.md&#34;&gt;Admin&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Listener

_Required_: No

_Type_: List of &lt;a href=&#34;listener.md&#34;&gt;Listener&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationDatabase

_Required_: No

_Type_: List of &lt;a href=&#34;applicationdatabase.md&#34;&gt;ApplicationDatabase&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cluster

_Required_: No

_Type_: List of &lt;a href=&#34;cluster.md&#34;&gt;Cluster&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Database

_Required_: No

_Type_: List of &lt;a href=&#34;database.md&#34;&gt;Database&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

_Required_: No

_Type_: List of &lt;a href=&#34;domain.md&#34;&gt;Domain&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedServers

_Required_: No

_Type_: List of &lt;a href=&#34;managedservers.md&#34;&gt;ManagedServers&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeManager

_Required_: No

_Type_: List of &lt;a href=&#34;nodemanager.md&#34;&gt;NodeManager&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ports

_Required_: No

_Type_: List of &lt;a href=&#34;ports.md&#34;&gt;Ports&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Status

Returns the &lt;code&gt;Status&lt;/code&gt; value.

