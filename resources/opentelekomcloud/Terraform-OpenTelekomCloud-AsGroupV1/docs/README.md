# Terraform::OpenTelekomCloud::AsGroupV1

CloudFormation equivalent of opentelekomcloud_as_group_v1

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

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoolDownTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteInstances

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeletePublicip

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesireInstanceNumber

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthPeriodicAuditMethod

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthPeriodicAuditTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceTerminatePolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Instances

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LbListenerId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxInstanceNumber

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinInstanceNumber

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notifications

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingConfigurationId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

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

