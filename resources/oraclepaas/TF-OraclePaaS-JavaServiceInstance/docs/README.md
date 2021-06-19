# TF::OraclePaaS::JavaServiceInstance

The `oraclepaas_java_service_instance` resource creates and manages an Oracle Java Cloud Service instance on Oracle Cloud Infrastructure and Oracle Cloud Infrastructure Classic.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OraclePaaS::JavaServiceInstance",
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
        "<a href="#backups" title="Backups">Backups</a>" : <i>[ <a href="backupsdefinition.md">BackupsDefinition</a>, ... ]</i>,
        "<a href="#loadbalancer" title="LoadBalancer">LoadBalancer</a>" : <i>[ <a href="loadbalancerdefinition.md">LoadBalancerDefinition</a>, ... ]</i>,
        "<a href="#oracletrafficdirector" title="OracleTrafficDirector">OracleTrafficDirector</a>" : <i>[ <a href="oracletrafficdirectordefinition.md">OracleTrafficDirectorDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#weblogicserver" title="WeblogicServer">WeblogicServer</a>" : <i>[ <a href="weblogicserverdefinition.md">WeblogicServerDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OraclePaaS::JavaServiceInstance
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
      - <a href="backupsdefinition.md">BackupsDefinition</a></i>
    <a href="#loadbalancer" title="LoadBalancer">LoadBalancer</a>: <i>
      - <a href="loadbalancerdefinition.md">LoadBalancerDefinition</a></i>
    <a href="#oracletrafficdirector" title="OracleTrafficDirector">OracleTrafficDirector</a>: <i>
      - <a href="oracletrafficdirectordefinition.md">OracleTrafficDirectorDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#weblogicserver" title="WeblogicServer">WeblogicServer</a>: <i>
      - <a href="weblogicserverdefinition.md">WeblogicServerDefinition</a></i>
</pre>

## Properties

#### AssignPublicIp

Flag that specifies whether to assign (true) or not assign (false) public IP addresses to the nodes in your service instance. The default is `true`, which means any node added during service instance provisioning, or later added as part of a scaling operation, will have a public IP address assigned to it. This attribute is only applicable when provisioning an Oracle Java Cloud Service instance in a region on Oracle Cloud Infrastructure Classic, and a custom IP network is specified in `ip_network`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityDomain

Name of a data center location in the Oracle Cloud Infrastructure region that is specified in region. This is
only available for OCI.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupDestination

Specifies whether to enable backups for this Oracle Java Cloud Service instance.
Valid values are `BOTH` or `NONE`. Defaults to `BOTH`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BringYourOwnLicense

Flag that specifies whether to apply an existing on-premises license for Oracle WebLogic Server (true) to the new
Oracle Java Cloud Service instance you are provisioning. The default value is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Provides additional on the java service instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredState

Specifies the desired state of the service instance. Allowed values are `running` or `shutdown`.
The default is `running`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Edition

The edition for the service instance. Possible values are `SE`, `EE`, or `SUITE`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableAdminConsole

Flag that specifies whether to enable (true) or disable (false) the access
rules that control external communication to the WebLogic Server Administration Console, Fusion Middleware Control,
and Load Balancer Console.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceDelete

Flag that specifies whether you want to force the removal of the service instance even if the database
instance cannot be reached to delete the database schemas. Default value is `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpNetwork

The three-part name of a custom IP network to attach this service instance to. For example: `/Compute-identity_domain/user/object`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Level

Service level for the service instance. Possible values are `BASIC` or `PAAS`. Default
value is `PAAS`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MeteringFrequency

Billing unit. Possible values are `HOURLY` or `MONTHLY`. Default value is `HOURLY`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Service Instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationEmail

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

Name of the region where the Oracle Java Cloud Service instance is to be provisioned.
This attribute is only applicable to accounts where regions are supported. A region name must be specified if you
want to use ipReservations or ipNetwork.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceVersion

Oracle WebLogic Server software version. Valid values are: `12cRelease213`, `12cRelease212`, `12cR3`, or `11gR1`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotName

Name of the snapshot to clone from.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceServiceName

Name of the existing Oracle Java Cloud Service instance that has the snapshot from which you are creating a clone.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshPublicKey

The ssh key to connect to the java service instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet

A subdivision of a cloud network that is set up in the data center as specified in `availability_domain`.
This is only available for OCI.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseIdentityService

Flag that specifies whether to use Oracle Identity Cloud Service (true) or the local WebLogic identity store
(false) for user authentication and to maintain administrators, application users, groups and roles. The default
value is false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backups

_Required_: No

_Type_: List of <a href="backupsdefinition.md">BackupsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancer

_Required_: No

_Type_: List of <a href="loadbalancerdefinition.md">LoadBalancerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OracleTrafficDirector

_Required_: No

_Type_: List of <a href="oracletrafficdirectordefinition.md">OracleTrafficDirectorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeblogicServer

_Required_: No

_Type_: List of <a href="weblogicserverdefinition.md">WeblogicServerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### Status

Returns the <code>Status</code> value.

