# Terraform::OraclePaaS::MysqlServiceInstance

The `oraclepaas_mysql_service_instance` resource creates and manages an Oracle MySQL Cloud Service instance on the Oracle Cloud Platform.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OraclePaaS::MysqlServiceInstance",
    "Properties" : {
        "<a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>" : <i>String</i>,
        "<a href="#backupdestination" title="BackupDestination">BackupDestination</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#ipnetwork" title="IpNetwork">IpNetwork</a>" : <i>String</i>,
        "<a href="#meteringfrequency" title="MeteringFrequency">MeteringFrequency</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notificationemail" title="NotificationEmail">NotificationEmail</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#shape" title="Shape">Shape</a>" : <i>String</i>,
        "<a href="#sshpublickey" title="SshPublicKey">SshPublicKey</a>" : <i>String</i>,
        "<a href="#subnet" title="Subnet">Subnet</a>" : <i>String</i>,
        "<a href="#vmuser" title="VmUser">VmUser</a>" : <i>String</i>,
        "<a href="#backups" title="Backups">Backups</a>" : <i>[ <a href="backups.md">Backups</a>, ... ]</i>,
        "<a href="#mysqlconfiguration" title="MysqlConfiguration">MysqlConfiguration</a>" : <i>[ <a href="mysqlconfiguration.md">MysqlConfiguration</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#enterprisemonitorconfiguration" title="EnterpriseMonitorConfiguration">EnterpriseMonitorConfiguration</a>" : <i>[ <a href="enterprisemonitorconfiguration.md">EnterpriseMonitorConfiguration</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OraclePaaS::MysqlServiceInstance
Properties:
    <a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>: <i>String</i>
    <a href="#backupdestination" title="BackupDestination">BackupDestination</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#ipnetwork" title="IpNetwork">IpNetwork</a>: <i>String</i>
    <a href="#meteringfrequency" title="MeteringFrequency">MeteringFrequency</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notificationemail" title="NotificationEmail">NotificationEmail</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#shape" title="Shape">Shape</a>: <i>String</i>
    <a href="#sshpublickey" title="SshPublicKey">SshPublicKey</a>: <i>String</i>
    <a href="#subnet" title="Subnet">Subnet</a>: <i>String</i>
    <a href="#vmuser" title="VmUser">VmUser</a>: <i>String</i>
    <a href="#backups" title="Backups">Backups</a>: <i>
      - <a href="backups.md">Backups</a></i>
    <a href="#mysqlconfiguration" title="MysqlConfiguration">MysqlConfiguration</a>: <i>
      - <a href="mysqlconfiguration.md">MysqlConfiguration</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#enterprisemonitorconfiguration" title="EnterpriseMonitorConfiguration">EnterpriseMonitorConfiguration</a>: <i>
      - <a href="enterprisemonitorconfiguration.md">EnterpriseMonitorConfiguration</a></i>
</pre>

## Properties

#### AvailabilityDomain

Name of the availability domain within the region where the Oracle Database Cloud Service instance is to be provisioned. This is applicable only if you wish to provision to an OCI instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupDestination

The destination where the database backups will be stored.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

. A description of the MySQL Instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpNetwork

This attribute is only applicable to accounts where regions are supported. The three-part name of an IP network to which the service instance is added. For example: /Compute-identity_domain/user/object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MeteringFrequency

. The billing frequency of the service instance. Allowed values are `MONTHLY` and `HOURLY`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

. The name of MySQL Cloud Service instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationEmail

The email address to send notifications around successful or unsuccessful completions of the instance-creation operation.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

. Specifies the region where the instance will be provisioned.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shape

The desired compute shape.  A shape defines the number of Oracle Compute Units (OCPUs) and amount of memory (RAM). See [About Shapes](http://www.oracle.com/pls/topic/lookup?ctx=cloud&id=OCSUG210) in _Using Oracle Compute Cloud Service_ for more information about shapes.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshPublicKey

. The public key for the secure shell (SSH). This key wil be used for authentication when the user logs on to the instance over SSH.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmUser

The user name of account to be created in the VM.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backups

_Required_: No

_Type_: List of <a href="backups.md">Backups</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MysqlConfiguration

_Required_: No

_Type_: List of <a href="mysqlconfiguration.md">MysqlConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnterpriseMonitorConfiguration

_Required_: No

_Type_: List of <a href="enterprisemonitorconfiguration.md">EnterpriseMonitorConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### BaseReleaseVersion

Returns the <code>BaseReleaseVersion</code> value.

#### EmUrl

Returns the <code>EmUrl</code> value.

#### ReleaseVersion

Returns the <code>ReleaseVersion</code> value.

#### ServiceVersion

Returns the <code>ServiceVersion</code> value.

