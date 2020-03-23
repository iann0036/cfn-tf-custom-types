# Terraform::AWS::AutoscalingGroup

Provides an AutoScaling Group resource.

-> **Note:** You must specify either `launch_configuration`, `launch_template`, or `mixed_instances_policy`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::AutoscalingGroup",
    "Properties" : {
        "<a href="#availabilityzones" title="AvailabilityZones">AvailabilityZones</a>" : <i>[ String, ... ]</i>,
        "<a href="#defaultcooldown" title="DefaultCooldown">DefaultCooldown</a>" : <i>Double</i>,
        "<a href="#desiredcapacity" title="DesiredCapacity">DesiredCapacity</a>" : <i>Double</i>,
        "<a href="#enabledmetrics" title="EnabledMetrics">EnabledMetrics</a>" : <i>[ String, ... ]</i>,
        "<a href="#forcedelete" title="ForceDelete">ForceDelete</a>" : <i>Boolean</i>,
        "<a href="#healthcheckgraceperiod" title="HealthCheckGracePeriod">HealthCheckGracePeriod</a>" : <i>Double</i>,
        "<a href="#healthchecktype" title="HealthCheckType">HealthCheckType</a>" : <i>String</i>,
        "<a href="#launchconfiguration" title="LaunchConfiguration">LaunchConfiguration</a>" : <i>String</i>,
        "<a href="#loadbalancers" title="LoadBalancers">LoadBalancers</a>" : <i>[ String, ... ]</i>,
        "<a href="#maxinstancelifetime" title="MaxInstanceLifetime">MaxInstanceLifetime</a>" : <i>Double</i>,
        "<a href="#maxsize" title="MaxSize">MaxSize</a>" : <i>Double</i>,
        "<a href="#metricsgranularity" title="MetricsGranularity">MetricsGranularity</a>" : <i>String</i>,
        "<a href="#minelbcapacity" title="MinElbCapacity">MinElbCapacity</a>" : <i>Double</i>,
        "<a href="#minsize" title="MinSize">MinSize</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nameprefix" title="NamePrefix">NamePrefix</a>" : <i>String</i>,
        "<a href="#placementgroup" title="PlacementGroup">PlacementGroup</a>" : <i>String</i>,
        "<a href="#protectfromscalein" title="ProtectFromScaleIn">ProtectFromScaleIn</a>" : <i>Boolean</i>,
        "<a href="#servicelinkedrolearn" title="ServiceLinkedRoleArn">ServiceLinkedRoleArn</a>" : <i>String</i>,
        "<a href="#suspendedprocesses" title="SuspendedProcesses">SuspendedProcesses</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ [ <a href="tags.md">Tags</a>, ... ], ... ]</i>,
        "<a href="#targetgrouparns" title="TargetGroupArns">TargetGroupArns</a>" : <i>[ String, ... ]</i>,
        "<a href="#terminationpolicies" title="TerminationPolicies">TerminationPolicies</a>" : <i>[ String, ... ]</i>,
        "<a href="#vpczoneidentifier" title="VpcZoneIdentifier">VpcZoneIdentifier</a>" : <i>[ String, ... ]</i>,
        "<a href="#waitforcapacitytimeout" title="WaitForCapacityTimeout">WaitForCapacityTimeout</a>" : <i>String</i>,
        "<a href="#waitforelbcapacity" title="WaitForElbCapacity">WaitForElbCapacity</a>" : <i>Double</i>,
        "<a href="#initiallifecyclehook" title="InitialLifecycleHook">InitialLifecycleHook</a>" : <i>[ <a href="initiallifecyclehook.md">InitialLifecycleHook</a>, ... ]</i>,
        "<a href="#launchtemplate" title="LaunchTemplate">LaunchTemplate</a>" : <i>[ <a href="launchtemplate.md">LaunchTemplate</a>, ... ]</i>,
        "<a href="#mixedinstancespolicy" title="MixedInstancesPolicy">MixedInstancesPolicy</a>" : <i>[ <a href="mixedinstancespolicy.md">MixedInstancesPolicy</a>, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tag.md">Tag</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#instancesdistribution" title="InstancesDistribution">InstancesDistribution</a>" : <i>[ <a href="instancesdistribution.md">InstancesDistribution</a>, ... ]</i>,
        "<a href="#launchtemplatespecification" title="LaunchTemplateSpecification">LaunchTemplateSpecification</a>" : <i>[ <a href="launchtemplatespecification.md">LaunchTemplateSpecification</a>, ... ]</i>,
        "<a href="#override" title="Override">Override</a>" : <i>[ <a href="override.md">Override</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::AutoscalingGroup
Properties:
    <a href="#availabilityzones" title="AvailabilityZones">AvailabilityZones</a>: <i>
      - String</i>
    <a href="#defaultcooldown" title="DefaultCooldown">DefaultCooldown</a>: <i>Double</i>
    <a href="#desiredcapacity" title="DesiredCapacity">DesiredCapacity</a>: <i>Double</i>
    <a href="#enabledmetrics" title="EnabledMetrics">EnabledMetrics</a>: <i>
      - String</i>
    <a href="#forcedelete" title="ForceDelete">ForceDelete</a>: <i>Boolean</i>
    <a href="#healthcheckgraceperiod" title="HealthCheckGracePeriod">HealthCheckGracePeriod</a>: <i>Double</i>
    <a href="#healthchecktype" title="HealthCheckType">HealthCheckType</a>: <i>String</i>
    <a href="#launchconfiguration" title="LaunchConfiguration">LaunchConfiguration</a>: <i>String</i>
    <a href="#loadbalancers" title="LoadBalancers">LoadBalancers</a>: <i>
      - String</i>
    <a href="#maxinstancelifetime" title="MaxInstanceLifetime">MaxInstanceLifetime</a>: <i>Double</i>
    <a href="#maxsize" title="MaxSize">MaxSize</a>: <i>Double</i>
    <a href="#metricsgranularity" title="MetricsGranularity">MetricsGranularity</a>: <i>String</i>
    <a href="#minelbcapacity" title="MinElbCapacity">MinElbCapacity</a>: <i>Double</i>
    <a href="#minsize" title="MinSize">MinSize</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nameprefix" title="NamePrefix">NamePrefix</a>: <i>String</i>
    <a href="#placementgroup" title="PlacementGroup">PlacementGroup</a>: <i>String</i>
    <a href="#protectfromscalein" title="ProtectFromScaleIn">ProtectFromScaleIn</a>: <i>Boolean</i>
    <a href="#servicelinkedrolearn" title="ServiceLinkedRoleArn">ServiceLinkedRoleArn</a>: <i>String</i>
    <a href="#suspendedprocesses" title="SuspendedProcesses">SuspendedProcesses</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - List of <a href="tags.md">Tags</a></i>
    <a href="#targetgrouparns" title="TargetGroupArns">TargetGroupArns</a>: <i>
      - String</i>
    <a href="#terminationpolicies" title="TerminationPolicies">TerminationPolicies</a>: <i>
      - String</i>
    <a href="#vpczoneidentifier" title="VpcZoneIdentifier">VpcZoneIdentifier</a>: <i>
      - String</i>
    <a href="#waitforcapacitytimeout" title="WaitForCapacityTimeout">WaitForCapacityTimeout</a>: <i>String</i>
    <a href="#waitforelbcapacity" title="WaitForElbCapacity">WaitForElbCapacity</a>: <i>Double</i>
    <a href="#initiallifecyclehook" title="InitialLifecycleHook">InitialLifecycleHook</a>: <i>
      - <a href="initiallifecyclehook.md">InitialLifecycleHook</a></i>
    <a href="#launchtemplate" title="LaunchTemplate">LaunchTemplate</a>: <i>
      - <a href="launchtemplate.md">LaunchTemplate</a></i>
    <a href="#mixedinstancespolicy" title="MixedInstancesPolicy">MixedInstancesPolicy</a>: <i>
      - <a href="mixedinstancespolicy.md">MixedInstancesPolicy</a></i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tag.md">Tag</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#instancesdistribution" title="InstancesDistribution">InstancesDistribution</a>: <i>
      - <a href="instancesdistribution.md">InstancesDistribution</a></i>
    <a href="#launchtemplatespecification" title="LaunchTemplateSpecification">LaunchTemplateSpecification</a>: <i>
      - <a href="launchtemplatespecification.md">LaunchTemplateSpecification</a></i>
    <a href="#override" title="Override">Override</a>: <i>
      - <a href="override.md">Override</a></i>
</pre>

## Properties

#### AvailabilityZones

A list of one or more availability zones for the group. This parameter should not be specified when using `vpc_zone_identifier`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultCooldown

The amount of time, in seconds, after a scaling activity completes before another scaling activity can start.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredCapacity

The number of Amazon EC2 instances that
should be running in the group. (See also [Waiting for
Capacity](#waiting-for-capacity) below.).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnabledMetrics

A list of metrics to collect. The allowed values are `GroupDesiredCapacity`, `GroupInServiceCapacity`, `GroupPendingCapacity`, `GroupMinSize`, `GroupMaxSize`, `GroupInServiceInstances`, `GroupPendingInstances`, `GroupStandbyInstances`, `GroupStandbyCapacity`, `GroupTerminatingCapacity`, `GroupTerminatingInstances`, `GroupTotalCapacity`, `GroupTotalInstances`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceDelete

Allows deleting the autoscaling group without waiting
for all instances in the pool to terminate.  You can force an autoscaling group to delete
even if it's in the process of scaling a resource. Normally, Terraform
drains all the instances before deleting the group.  This bypasses that
behavior and potentially leaves resources dangling.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckGracePeriod

Time (in seconds) after instance comes into service before checking health.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckType

"EC2" or "ELB". Controls how health checking is done.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchConfiguration

The name of the launch configuration to use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxInstanceLifetime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSize

The maximum size of the auto scale group.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricsGranularity

The granularity to associate with the metrics to collect. The only valid value is `1Minute`. Default is `1Minute`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinElbCapacity

Setting this causes Terraform to wait for
this number of instances from this autoscaling group to show up healthy in the
ELB only on creation. Updates will not wait on ELB instance number changes.
(See also [Waiting for Capacity](#waiting-for-capacity) below.).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinSize

The minimum size of the auto scale group.
(See also [Waiting for Capacity](#waiting-for-capacity) below.).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the auto scaling group. By default generated by Terraform.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamePrefix

Creates a unique name beginning with the specified
prefix. Conflicts with `name`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlacementGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtectFromScaleIn

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceLinkedRoleArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuspendedProcesses

A list of processes to suspend for the AutoScaling Group. The allowed values are `Launch`, `Terminate`, `HealthCheck`, `ReplaceUnhealthy`, `AZRebalance`, `AlarmNotification`, `ScheduledActions`, `AddToLoadBalancer`.
Note that if you suspend either the `Launch` or `Terminate` process types, it can prevent your autoscaling group from functioning properly.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetGroupArns

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TerminationPolicies

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcZoneIdentifier

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForCapacityTimeout

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForElbCapacity

Setting this will cause Terraform to wait
for exactly this number of healthy instances from this autoscaling group in
all attached load balancers on both create and update operations. (Takes
precedence over `min_elb_capacity` behavior.)
(See also [Waiting for Capacity](#waiting-for-capacity) below.).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitialLifecycleHook

_Required_: No

_Type_: List of <a href="initiallifecyclehook.md">InitialLifecycleHook</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchTemplate

_Required_: No

_Type_: List of <a href="launchtemplate.md">LaunchTemplate</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MixedInstancesPolicy

_Required_: No

_Type_: List of <a href="mixedinstancespolicy.md">MixedInstancesPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tag.md">Tag</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstancesDistribution

_Required_: No

_Type_: List of <a href="instancesdistribution.md">InstancesDistribution</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchTemplateSpecification

_Required_: No

_Type_: List of <a href="launchtemplatespecification.md">LaunchTemplateSpecification</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Override

_Required_: No

_Type_: List of <a href="override.md">Override</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

