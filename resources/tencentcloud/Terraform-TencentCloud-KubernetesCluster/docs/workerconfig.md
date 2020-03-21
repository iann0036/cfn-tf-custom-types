# Terraform::TencentCloud::KubernetesCluster WorkerConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
    "<a href="#count" title="Count">Count</a>" : <i>Double</i>,
    "<a href="#enhancedmonitorservice" title="EnhancedMonitorService">EnhancedMonitorService</a>" : <i>Boolean</i>,
    "<a href="#enhancedsecurityservice" title="EnhancedSecurityService">EnhancedSecurityService</a>" : <i>Boolean</i>,
    "<a href="#instancechargetype" title="InstanceChargeType">InstanceChargeType</a>" : <i>String</i>,
    "<a href="#instancechargetypeprepaidperiod" title="InstanceChargeTypePrepaidPeriod">InstanceChargeTypePrepaidPeriod</a>" : <i>Double</i>,
    "<a href="#instancechargetypeprepaidrenewflag" title="InstanceChargeTypePrepaidRenewFlag">InstanceChargeTypePrepaidRenewFlag</a>" : <i>String</i>,
    "<a href="#instancename" title="InstanceName">InstanceName</a>" : <i>String</i>,
    "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
    "<a href="#internetchargetype" title="InternetChargeType">InternetChargeType</a>" : <i>String</i>,
    "<a href="#internetmaxbandwidthout" title="InternetMaxBandwidthOut">InternetMaxBandwidthOut</a>" : <i>Double</i>,
    "<a href="#keyids" title="KeyIds">KeyIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#password" title="Password">Password</a>" : <i>String</i>,
    "<a href="#publicipassigned" title="PublicIpAssigned">PublicIpAssigned</a>" : <i>Boolean</i>,
    "<a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
    "<a href="#systemdisksize" title="SystemDiskSize">SystemDiskSize</a>" : <i>Double</i>,
    "<a href="#systemdisktype" title="SystemDiskType">SystemDiskType</a>" : <i>String</i>,
    "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
    "<a href="#datadisk" title="DataDisk">DataDisk</a>" : <i>[ <a href="workerconfig-datadisk.md">DataDisk</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
<a href="#count" title="Count">Count</a>: <i>Double</i>
<a href="#enhancedmonitorservice" title="EnhancedMonitorService">EnhancedMonitorService</a>: <i>Boolean</i>
<a href="#enhancedsecurityservice" title="EnhancedSecurityService">EnhancedSecurityService</a>: <i>Boolean</i>
<a href="#instancechargetype" title="InstanceChargeType">InstanceChargeType</a>: <i>String</i>
<a href="#instancechargetypeprepaidperiod" title="InstanceChargeTypePrepaidPeriod">InstanceChargeTypePrepaidPeriod</a>: <i>Double</i>
<a href="#instancechargetypeprepaidrenewflag" title="InstanceChargeTypePrepaidRenewFlag">InstanceChargeTypePrepaidRenewFlag</a>: <i>String</i>
<a href="#instancename" title="InstanceName">InstanceName</a>: <i>String</i>
<a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
<a href="#internetchargetype" title="InternetChargeType">InternetChargeType</a>: <i>String</i>
<a href="#internetmaxbandwidthout" title="InternetMaxBandwidthOut">InternetMaxBandwidthOut</a>: <i>Double</i>
<a href="#keyids" title="KeyIds">KeyIds</a>: <i>
      - String</i>
<a href="#password" title="Password">Password</a>: <i>String</i>
<a href="#publicipassigned" title="PublicIpAssigned">PublicIpAssigned</a>: <i>Boolean</i>
<a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>: <i>
      - String</i>
<a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
<a href="#systemdisksize" title="SystemDiskSize">SystemDiskSize</a>: <i>Double</i>
<a href="#systemdisktype" title="SystemDiskType">SystemDiskType</a>: <i>String</i>
<a href="#userdata" title="UserData">UserData</a>: <i>String</i>
<a href="#datadisk" title="DataDisk">DataDisk</a>: <i>
      - <a href="workerconfig-datadisk.md">DataDisk</a></i>
</pre>

## Properties

#### AvailabilityZone

Indicates which availability zone will be used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Count

Number of cvm.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnhancedMonitorService

To specify whether to enable cloud monitor service. Default is TRUE.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnhancedSecurityService

To specify whether to enable cloud security service. Default is TRUE.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceChargeType

The charge type of instance. Valid values are `PREPAID` and `POSTPAID_BY_HOUR`, The default is `POSTPAID_BY_HOUR`. Note: TencentCloud International only supports `POSTPAID_BY_HOUR`, `PREPAID` instance will not terminated after cluster deleted, and may not allow to delete before expired.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceChargeTypePrepaidPeriod

The tenancy (time unit is month) of the prepaid instance, NOTE: it only works when instance_charge_type is set to `PREPAID`. Valid values are 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceChargeTypePrepaidRenewFlag

When enabled, the CVM instance will be renew automatically when it reach the end of the prepaid tenancy. Valid values are `NOTIFY_AND_AUTO_RENEW`, `NOTIFY_AND_MANUAL_RENEW` and `DISABLE_NOTIFY_AND_MANUAL_RENEW`. NOTE: it only works when instance_charge_type is set to `PREPAID`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceName

Name of the CVMs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceType

Specified types of CVM instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetChargeType

Charge types for network traffic. Available values include TRAFFIC_POSTPAID_BY_HOUR.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetMaxBandwidthOut

Max bandwidth of Internet access in Mbps. Default is 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyIds

ID list of keys, should be set if `password` not set.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Password to access, should be set if `key_ids` not set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIpAssigned

Specify whether to assign an Internet IP address.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupIds

Security groups to which a CVM instance belongs.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

Private network ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemDiskSize

Volume of system disk in GB. Default is 50.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemDiskType

Type of a CVM disk, and available values include CLOUD_PREMIUM and CLOUD_SSD. Default is CLOUD_PREMIUM.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

ase64-encoded User Data text, the length limit is 16KB.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataDisk

_Required_: No

_Type_: List of <a href="workerconfig-datadisk.md">DataDisk</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

