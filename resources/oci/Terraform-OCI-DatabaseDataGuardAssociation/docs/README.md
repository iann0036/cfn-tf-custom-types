# Terraform::OCI::DatabaseDataGuardAssociation

This resource provides the Data Guard Association resource in Oracle Cloud Infrastructure Database service.

Creates a new Data Guard association.  A Data Guard association represents the replication relationship between the
specified database and a peer database. For more information, see [Using Oracle Data Guard](https://docs.cloud.oracle.com/iaas/Content/Database/Tasks/usingdataguard.htm).

All Oracle Cloud Infrastructure resources, including Data Guard associations, get an Oracle-assigned, unique ID
called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response.
You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the
resource in the Console. For more information, see
[Resource Identifiers](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::DatabaseDataGuardAssociation",
    "Properties" : {
        "<a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>" : <i>String</i>,
        "<a href="#backupnetworknsgids" title="BackupNetworkNsgIds">BackupNetworkNsgIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#creationtype" title="CreationType">CreationType</a>" : <i>String</i>,
        "<a href="#databaseadminpassword" title="DatabaseAdminPassword">DatabaseAdminPassword</a>" : <i>String</i>,
        "<a href="#databaseid" title="DatabaseId">DatabaseId</a>" : <i>String</i>,
        "<a href="#deletestandbydbhomeondelete" title="DeleteStandbyDbHomeOnDelete">DeleteStandbyDbHomeOnDelete</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
        "<a href="#nsgids" title="NsgIds">NsgIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#peerdbsystemid" title="PeerDbSystemId">PeerDbSystemId</a>" : <i>String</i>,
        "<a href="#protectionmode" title="ProtectionMode">ProtectionMode</a>" : <i>String</i>,
        "<a href="#shape" title="Shape">Shape</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#transporttype" title="TransportType">TransportType</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::DatabaseDataGuardAssociation
Properties:
    <a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>: <i>String</i>
    <a href="#backupnetworknsgids" title="BackupNetworkNsgIds">BackupNetworkNsgIds</a>: <i>
      - String</i>
    <a href="#creationtype" title="CreationType">CreationType</a>: <i>String</i>
    <a href="#databaseadminpassword" title="DatabaseAdminPassword">DatabaseAdminPassword</a>: <i>String</i>
    <a href="#databaseid" title="DatabaseId">DatabaseId</a>: <i>String</i>
    <a href="#deletestandbydbhomeondelete" title="DeleteStandbyDbHomeOnDelete">DeleteStandbyDbHomeOnDelete</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
    <a href="#nsgids" title="NsgIds">NsgIds</a>: <i>
      - String</i>
    <a href="#peerdbsystemid" title="PeerDbSystemId">PeerDbSystemId</a>: <i>String</i>
    <a href="#protectionmode" title="ProtectionMode">ProtectionMode</a>: <i>String</i>
    <a href="#shape" title="Shape">Shape</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#transporttype" title="TransportType">TransportType</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AvailabilityDomain

The name of the availability domain that the standby database DB system will be located in. For example- "Uocm:PHX-AD-1".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupNetworkNsgIds

A list of the [OCIDs](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the network security groups (NSGs) that the backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see [Security Rules](https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). Applicable only to Exadata DB systems.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreationType

Specifies whether to create the peer database in an existing DB system or in a new DB system.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseAdminPassword

A strong password for the `SYS`, `SYSTEM`, and `PDB Admin` users to apply during standby creation.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseId

The database [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteStandbyDbHomeOnDelete

(Updatable) if set to true the destroy operation will destroy the standby dbHome/dbSystem that is referenced in the Data Guard Association. The Data Guard Association gets destroyed when standby dbHome/dbSystem is terminated. Only `true` is supported at this time. If you change an argument that is used during the delete operation you must run `terraform apply` first so that that the change in the value is registered in the statefile before running `terraform destroy`. `terraform destroy` only looks at what is currently on the statefile and ignores the terraform configuration files.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

The user-friendly name of the DB system that will contain the the standby database. The display name does not have to be unique.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

The hostname for the DB node.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsgIds

A list of the [OCIDs](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the network security groups (NSGs) that this resource belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see [Security Rules](https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). **NsgIds restrictions:**
* Autonomous Databases with private access require at least 1 Network Security Group (NSG). The nsgIds array cannot be empty.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerDbSystemId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DB system in which to create the standby database. You must supply this value if creationType is `ExistingDbSystem`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtectionMode

The protection mode to set up between the primary and standby databases. For more information, see [Oracle Data Guard Protection Modes](http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000) in the Oracle Data Guard documentation.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shape

The virtual machine DB system shape to launch for the standby database in the Data Guard association. The shape determines the number of CPU cores and the amount of memory available for the DB system. Only virtual machine shapes are valid options. If you do not supply this parameter, the default shape is the shape of the primary DB system.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

The OCID of the subnet the DB system is associated with. **Subnet Restrictions:**
* For 1- and 2-node RAC DB systems, do not use a subnet that overlaps with 192.168.16.16/28.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransportType

The redo transport type to use for this Data Guard association.  Valid values depend on the specified `protectionMode`:
* MAXIMUM_AVAILABILITY - SYNC or FASTSYNC
* MAXIMUM_PERFORMANCE - ASYNC
* MAXIMUM_PROTECTION - SYNC.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ApplyLag

Returns the <code>ApplyLag</code> value.

#### ApplyRate

Returns the <code>ApplyRate</code> value.

#### Id

Returns the <code>Id</code> value.

#### LifecycleDetails

Returns the <code>LifecycleDetails</code> value.

#### PeerDataGuardAssociationId

Returns the <code>PeerDataGuardAssociationId</code> value.

#### PeerDatabaseId

Returns the <code>PeerDatabaseId</code> value.

#### PeerDbHomeId

Returns the <code>PeerDbHomeId</code> value.

#### PeerRole

Returns the <code>PeerRole</code> value.

#### Role

Returns the <code>Role</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

