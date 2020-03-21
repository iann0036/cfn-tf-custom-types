# Terraform::FlexibleEngine::MrsClusterV1

Manages resource cluster within FlexibleEngine MRS.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::FlexibleEngine::MrsClusterV1",
    "Properties" : {
        "<a href="#availablezoneid" title="AvailableZoneId">AvailableZoneId</a>" : <i>String</i>,
        "<a href="#billingtype" title="BillingType">BillingType</a>" : <i>Double</i>,
        "<a href="#clusteradminsecret" title="ClusterAdminSecret">ClusterAdminSecret</a>" : <i>String</i>,
        "<a href="#clustername" title="ClusterName">ClusterName</a>" : <i>String</i>,
        "<a href="#clustertype" title="ClusterType">ClusterType</a>" : <i>Double</i>,
        "<a href="#clusterversion" title="ClusterVersion">ClusterVersion</a>" : <i>String</i>,
        "<a href="#corenodenum" title="CoreNodeNum">CoreNodeNum</a>" : <i>Double</i>,
        "<a href="#corenodesize" title="CoreNodeSize">CoreNodeSize</a>" : <i>String</i>,
        "<a href="#logcollection" title="LogCollection">LogCollection</a>" : <i>Double</i>,
        "<a href="#masternodenum" title="MasterNodeNum">MasterNodeNum</a>" : <i>Double</i>,
        "<a href="#masternodesize" title="MasterNodeSize">MasterNodeSize</a>" : <i>String</i>,
        "<a href="#nodepubliccertname" title="NodePublicCertName">NodePublicCertName</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#safemode" title="SafeMode">SafeMode</a>" : <i>Double</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#volumesize" title="VolumeSize">VolumeSize</a>" : <i>Double</i>,
        "<a href="#volumetype" title="VolumeType">VolumeType</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#addjobs" title="AddJobs">AddJobs</a>" : <i>[ <a href="addjobs.md">AddJobs</a>, ... ]</i>,
        "<a href="#componentlist" title="ComponentList">ComponentList</a>" : <i>[ <a href="componentlist.md">ComponentList</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::FlexibleEngine::MrsClusterV1
Properties:
    <a href="#availablezoneid" title="AvailableZoneId">AvailableZoneId</a>: <i>String</i>
    <a href="#billingtype" title="BillingType">BillingType</a>: <i>Double</i>
    <a href="#clusteradminsecret" title="ClusterAdminSecret">ClusterAdminSecret</a>: <i>String</i>
    <a href="#clustername" title="ClusterName">ClusterName</a>: <i>String</i>
    <a href="#clustertype" title="ClusterType">ClusterType</a>: <i>Double</i>
    <a href="#clusterversion" title="ClusterVersion">ClusterVersion</a>: <i>String</i>
    <a href="#corenodenum" title="CoreNodeNum">CoreNodeNum</a>: <i>Double</i>
    <a href="#corenodesize" title="CoreNodeSize">CoreNodeSize</a>: <i>String</i>
    <a href="#logcollection" title="LogCollection">LogCollection</a>: <i>Double</i>
    <a href="#masternodenum" title="MasterNodeNum">MasterNodeNum</a>: <i>Double</i>
    <a href="#masternodesize" title="MasterNodeSize">MasterNodeSize</a>: <i>String</i>
    <a href="#nodepubliccertname" title="NodePublicCertName">NodePublicCertName</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#safemode" title="SafeMode">SafeMode</a>: <i>Double</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#volumesize" title="VolumeSize">VolumeSize</a>: <i>Double</i>
    <a href="#volumetype" title="VolumeType">VolumeType</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#addjobs" title="AddJobs">AddJobs</a>: <i>
      - <a href="addjobs.md">AddJobs</a></i>
    <a href="#componentlist" title="ComponentList">ComponentList</a>: <i>
      - <a href="componentlist.md">ComponentList</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AvailableZoneId

ID of an available zone. Obtain the value
from Regions and Endpoints.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BillingType

The value is 12, indicating on-demand payment.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterAdminSecret

Indicates the password of the MRS Manager
administrator. The password for MRS 1.5.0: Must contain 6 to 32 characters.
Must contain at least two types of the following: Lowercase letters Uppercase
letters Digits Special characters of `~!@#$%^&*()-_=+\|[{}];:'",<.>/? Spaces
Must be different from the username. Must be different from the username written
in reverse order. The password for MRS 1.3.0: Must contain 8 to 64 characters.
Must contain at least four types of the following: Lowercase letters Uppercase
letters Digits Special characters of `~!@#$%^&*()-_=+\|[{}];:'",<.>/? Spaces
Must be different from the username. Must be different from the username written
in reverse order. This parameter needs to be configured only when safe_mode
is set to 1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterName

Cluster name, which is globally unique and contains
only 1 to 64 letters, digits, hyphens (-), and underscores (_).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterType

Type of clusters 0: analysis cluster 1: streaming
cluster The default value is 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterVersion

Version of the clusters.You can refer to the online documentation to have the full list of available versions. The latest version of MRS is used by default.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoreNodeNum

Number of Core nodes Value range: 3 to 100 A
maximum of 100 Core nodes are supported by default. If more than 100 Core nodes
are required, contact technical support engineers or invoke background APIs
to modify the database.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoreNodeSize

Instance specification of a Core node Configuration
method of this parameter is identical to that of master_node_size.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogCollection

Indicates whether logs are collected when cluster
installation fails. 0: not collected 1: collected The default value is 0. If
log_collection is set to 1, OBS buckets will be created to collect the MRS logs.
These buckets will be charged.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterNodeNum

Number of Master nodes The value is 2.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterNodeSize

Best match based on several years of commissioning
experience. MRS supports specifications of hosts, and host specifications are
determined by CPUs, memory, and disks space. Master nodes support s1.4xlarge.linux.mrs,
and s1.8xlarge.linux.mrs. Core nodes of a streaming cluster support s1.xlarge.linux.mrs,
c2.2xlarge.linux.mrs, s1.2xlarge.linux.mrs, s1.4xlarge.linux.mrs, s1.8xlarge.linux.mrs,
and d1.8xlarge.linux.mrs. Core nodes of an analysis cluster support all specifications.
s1.xlarge.linux.mrs CPU: 4-core Memory: 16 GB System Disk: 40 GB
c2.2xlarge.linux.mrs CPU: 8-core Memory: 16 GB System Disk: 40 GB
s1.4xlarge.linux.mrs CPU: 16-core Memory: 64 GB System Disk: 40 GB
s1.8xlarge.linux.mrs CPU: 32-core Memory: 128 GB System Disk: 40 GB
d1.xlarge.linux.mrs CPU: 6-core Memory: 55 GB System Disk: 40 GB Data Disk: 1.8 TB x 3 HDDs
d1.2xlarge.linux.mrs CPU: 12-core Memory: 110 GB System Disk: 40 GB Data Disk: 1.8 TB x 6 HDDs
d1.4xlarge.linux.mrs CPU: 24-core Memory: 220 GB System Disk: 40 GB Data Disk: 1.8 TB x 12 HDDs
d1.8xlarge.linux.mrs CPU: 48-core Memory: 440 GB System Disk: 40 GB Data Disk: 1.8 TB x 24 HDDs.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodePublicCertName

Name of a key pair You can use a key
to log in to the Master node in the cluster.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

Cluster region information. Obtain the value from
Regions and Endpoints.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SafeMode

MRS cluster running mode 0: common mode The value
indicates that the Kerberos authentication is disabled. Users can use all functions
provided by the cluster. 1: safe mode The value indicates that the Kerberos
authentication is enabled. Common users cannot use the file management or job
management functions of an MRS cluster and cannot view cluster resource usage
or the job records of Hadoop and Spark. To use these functions, the users must
obtain the relevant permissions from the MRS Manager administrator. The request
has the cluster_admin_secret parameter only when safe_mode is set to 1.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

Subnet ID Obtain the subnet ID from the management
console as follows: Register an account and log in to the management console.
Click Virtual Private Cloud and select Virtual Private Cloud from the left list.
On the Virtual Private Cloud page, obtain the subnet ID from the list.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeSize

Data disk storage space of a Core node Users can
add disks to expand storage capacity when creating a cluster. There are the
following scenarios: Separation of data storage and computing: Data is stored
in the OBS system. Costs of clusters are relatively low but computing performance
is poor. The clusters can be deleted at any time. It is recommended when data
computing is not frequently performed. Integration of data storage and computing:
Data is stored in the HDFS system. Costs of clusters are relatively high but
computing performance is good. The clusters cannot be deleted in a short term.
It is recommended when data computing is frequently performed. Value range:
100 GB to 32000 GB.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeType

Type of disks SATA and SSD are supported. SATA:
common I/O SSD: super high-speed I/O.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

ID of the VPC where the subnet locates Obtain the VPC
ID from the management console as follows: Register an account and log in to
the management console. Click Virtual Private Cloud and select Virtual Private
Cloud from the left list. On the Virtual Private Cloud page, obtain the VPC
ID from the list.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddJobs

_Required_: No

_Type_: List of <a href="addjobs.md">AddJobs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComponentList

_Required_: No

_Type_: List of <a href="componentlist.md">ComponentList</a>

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

#### AvailableZoneName

Returns the <code>AvailableZoneName</code> value.

#### ChargingStartTime

Returns the <code>ChargingStartTime</code> value.

#### ClusterId

Returns the <code>ClusterId</code> value.

#### ClusterState

Returns the <code>ClusterState</code> value.

#### CoreNodeProductId

Returns the <code>CoreNodeProductId</code> value.

#### CoreNodeSpecId

Returns the <code>CoreNodeSpecId</code> value.

#### CreateAt

Returns the <code>CreateAt</code> value.

#### DeploymentId

Returns the <code>DeploymentId</code> value.

#### Duration

Returns the <code>Duration</code> value.

#### ErrorInfo

Returns the <code>ErrorInfo</code> value.

#### ExternalAlternateIp

Returns the <code>ExternalAlternateIp</code> value.

#### ExternalIp

Returns the <code>ExternalIp</code> value.

#### Fee

Returns the <code>Fee</code> value.

#### HadoopVersion

Returns the <code>HadoopVersion</code> value.

#### InstanceId

Returns the <code>InstanceId</code> value.

#### InternalIp

Returns the <code>InternalIp</code> value.

#### MasterNodeIp

Returns the <code>MasterNodeIp</code> value.

#### MasterNodeProductId

Returns the <code>MasterNodeProductId</code> value.

#### MasterNodeSpecId

Returns the <code>MasterNodeSpecId</code> value.

#### OrderId

Returns the <code>OrderId</code> value.

#### PrivateIpFirst

Returns the <code>PrivateIpFirst</code> value.

#### Remark

Returns the <code>Remark</code> value.

#### SecurityGroupsId

Returns the <code>SecurityGroupsId</code> value.

#### SlaveSecurityGroupsId

Returns the <code>SlaveSecurityGroupsId</code> value.

#### TenantId

Returns the <code>TenantId</code> value.

#### UpdateAt

Returns the <code>UpdateAt</code> value.

#### Vnc

Returns the <code>Vnc</code> value.

