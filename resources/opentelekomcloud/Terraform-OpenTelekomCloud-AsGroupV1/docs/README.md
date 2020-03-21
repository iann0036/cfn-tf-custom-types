# Terraform::OpenTelekomCloud::AsGroupV1

Manages a V1 Autoscaling Group resource within OpenTelekomCloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenTelekomCloud::AsGroupV1",
    "Properties" : {
        "<a href="#availablezones" title="AvailableZones">AvailableZones</a>" : <i>[ String, ... ]</i>,
        "<a href="#cooldowntime" title="CoolDownTime">CoolDownTime</a>" : <i>Double</i>,
        "<a href="#deleteinstances" title="DeleteInstances">DeleteInstances</a>" : <i>String</i>,
        "<a href="#deletepublicip" title="DeletePublicip">DeletePublicip</a>" : <i>Boolean</i>,
        "<a href="#desireinstancenumber" title="DesireInstanceNumber">DesireInstanceNumber</a>" : <i>Double</i>,
        "<a href="#healthperiodicauditmethod" title="HealthPeriodicAuditMethod">HealthPeriodicAuditMethod</a>" : <i>String</i>,
        "<a href="#healthperiodicaudittime" title="HealthPeriodicAuditTime">HealthPeriodicAuditTime</a>" : <i>Double</i>,
        "<a href="#instanceterminatepolicy" title="InstanceTerminatePolicy">InstanceTerminatePolicy</a>" : <i>String</i>,
        "<a href="#instances" title="Instances">Instances</a>" : <i>[ String, ... ]</i>,
        "<a href="#lblistenerid" title="LbListenerId">LbListenerId</a>" : <i>String</i>,
        "<a href="#maxinstancenumber" title="MaxInstanceNumber">MaxInstanceNumber</a>" : <i>Double</i>,
        "<a href="#mininstancenumber" title="MinInstanceNumber">MinInstanceNumber</a>" : <i>Double</i>,
        "<a href="#notifications" title="Notifications">Notifications</a>" : <i>[ String, ... ]</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#scalingconfigurationid" title="ScalingConfigurationId">ScalingConfigurationId</a>" : <i>String</i>,
        "<a href="#scalinggroupname" title="ScalingGroupName">ScalingGroupName</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#lbaaslisteners" title="LbaasListeners">LbaasListeners</a>" : <i>[ <a href="lbaaslisteners.md">LbaasListeners</a>, ... ]</i>,
        "<a href="#networks" title="Networks">Networks</a>" : <i>[ <a href="networks.md">Networks</a>, ... ]</i>,
        "<a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>" : <i>[ <a href="securitygroups.md">SecurityGroups</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenTelekomCloud::AsGroupV1
Properties:
    <a href="#availablezones" title="AvailableZones">AvailableZones</a>: <i>
      - String</i>
    <a href="#cooldowntime" title="CoolDownTime">CoolDownTime</a>: <i>Double</i>
    <a href="#deleteinstances" title="DeleteInstances">DeleteInstances</a>: <i>String</i>
    <a href="#deletepublicip" title="DeletePublicip">DeletePublicip</a>: <i>Boolean</i>
    <a href="#desireinstancenumber" title="DesireInstanceNumber">DesireInstanceNumber</a>: <i>Double</i>
    <a href="#healthperiodicauditmethod" title="HealthPeriodicAuditMethod">HealthPeriodicAuditMethod</a>: <i>String</i>
    <a href="#healthperiodicaudittime" title="HealthPeriodicAuditTime">HealthPeriodicAuditTime</a>: <i>Double</i>
    <a href="#instanceterminatepolicy" title="InstanceTerminatePolicy">InstanceTerminatePolicy</a>: <i>String</i>
    <a href="#instances" title="Instances">Instances</a>: <i>
      - String</i>
    <a href="#lblistenerid" title="LbListenerId">LbListenerId</a>: <i>String</i>
    <a href="#maxinstancenumber" title="MaxInstanceNumber">MaxInstanceNumber</a>: <i>Double</i>
    <a href="#mininstancenumber" title="MinInstanceNumber">MinInstanceNumber</a>: <i>Double</i>
    <a href="#notifications" title="Notifications">Notifications</a>: <i>
      - String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#scalingconfigurationid" title="ScalingConfigurationId">ScalingConfigurationId</a>: <i>String</i>
    <a href="#scalinggroupname" title="ScalingGroupName">ScalingGroupName</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#lbaaslisteners" title="LbaasListeners">LbaasListeners</a>: <i>
      - <a href="lbaaslisteners.md">LbaasListeners</a></i>
    <a href="#networks" title="Networks">Networks</a>: <i>
      - <a href="networks.md">Networks</a></i>
    <a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>: <i>
      - <a href="securitygroups.md">SecurityGroups</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AvailableZones

The availability zones in which to create
the instances in the autoscaling group.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoolDownTime

The cooling duration (in seconds). The value ranges
from 0 to 86400, and is 900 by default.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteInstances

Whether to delete the instances in the AS group
when deleting the AS group. The options are `yes` and `no`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeletePublicip

Whether to delete the elastic IP address bound to the
instances of AS group when deleting the instances. The options are `true` and `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesireInstanceNumber

The expected number of instances. The default
value is the minimum number of instances. The value ranges from the minimum number of
instances to the maximum number of instances.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthPeriodicAuditMethod

The health check method for instances
in the AS group. The health check methods include `ELB_AUDIT` and `NOVA_AUDIT`.
If load balancing is configured, the default value of this parameter is `ELB_AUDIT`.
Otherwise, the default value is `NOVA_AUDIT`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthPeriodicAuditTime

The health check period for instances.
The period has four options: 5 minutes (default), 15 minutes, 60 minutes, and 180 minutes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceTerminatePolicy

The instance removal policy. The policy has
four options: `OLD_CONFIG_OLD_INSTANCE` (default), `OLD_CONFIG_NEW_INSTANCE`,
`OLD_INSTANCE`, and `NEW_INSTANCE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Instances

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LbListenerId

The ELB listener IDs. The system supports up to
three ELB listeners, the IDs of which are separated using a comma (,).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxInstanceNumber

The maximum number of instances.
The default value is 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinInstanceNumber

The minimum number of instances.
The default value is 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notifications

The notification mode. The system only supports `EMAIL`
mode which refers to notification by email.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingConfigurationId

The configuration ID which defines
configurations of instances in the AS group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingGroupName

The name of the scaling group. The name can contain letters,
digits, underscores(_), and hyphens(-),and cannot exceed 64 characters.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

The VPC ID. Changing this creates a new group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LbaasListeners

_Required_: No

_Type_: List of <a href="lbaaslisteners.md">LbaasListeners</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Networks

_Required_: No

_Type_: List of <a href="networks.md">Networks</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroups

_Required_: No

_Type_: List of <a href="securitygroups.md">SecurityGroups</a>

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

