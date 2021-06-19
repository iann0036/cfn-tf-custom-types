# TF::AWS::AutoscalingGroup

Provides an Auto Scaling Group resource.

-> **Note:** You must specify either `launch_configuration`, `launch_template`, or `mixed_instances_policy`.

~> **NOTE on Auto Scaling Groups and ASG Attachments:** Terraform currently provides
both a standalone [`aws_autoscaling_attachment`](autoscaling_attachment.html) resource
(describing an ASG attached to an ELB or ALB), and an [`aws_autoscaling_group`](autoscaling_group.html)
with `load_balancers` and `target_group_arns` defined in-line. These two methods are not
mutually-exclusive. If `aws_autoscaling_attachment` resources are used, either alone or with inline
`load_balancers` or `target_group_arns`, the `aws_autoscaling_group` resource must be configured
to ignore changes to the `load_balancers` and `target_group_arns` arguments within a
[`lifecycle` configuration block](https://www.terraform.io/docs/configuration/meta-arguments/lifecycle.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::AutoscalingGroup",
    "Properties" : {
        "<a href="#availabilityzones" title="AvailabilityZones">AvailabilityZones</a>" : <i>[ String, ... ]</i>,
        "<a href="#capacityrebalance" title="CapacityRebalance">CapacityRebalance</a>" : <i>Boolean</i>,
        "<a href="#defaultcooldown" title="DefaultCooldown">DefaultCooldown</a>" : <i>Double</i>,
        "<a href="#desiredcapacity" title="DesiredCapacity">DesiredCapacity</a>" : <i>Double</i>,
        "<a href="#enabledmetrics" title="EnabledMetrics">EnabledMetrics</a>" : <i>[ String, ... ]</i>,
        "<a href="#forcedelete" title="ForceDelete">ForceDelete</a>" : <i>Boolean</i>,
        "<a href="#forcedeletewarmpool" title="ForceDeleteWarmPool">ForceDeleteWarmPool</a>" : <i>Boolean</i>,
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
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ [ <a href="tagsdefinition.md">TagsDefinition</a>, ... ], ... ]</i>,
        "<a href="#targetgrouparns" title="TargetGroupArns">TargetGroupArns</a>" : <i>[ String, ... ]</i>,
        "<a href="#terminationpolicies" title="TerminationPolicies">TerminationPolicies</a>" : <i>[ String, ... ]</i>,
        "<a href="#vpczoneidentifier" title="VpcZoneIdentifier">VpcZoneIdentifier</a>" : <i>[ String, ... ]</i>,
        "<a href="#waitforcapacitytimeout" title="WaitForCapacityTimeout">WaitForCapacityTimeout</a>" : <i>String</i>,
        "<a href="#waitforelbcapacity" title="WaitForElbCapacity">WaitForElbCapacity</a>" : <i>Double</i>,
        "<a href="#initiallifecyclehook" title="InitialLifecycleHook">InitialLifecycleHook</a>" : <i>[ <a href="initiallifecyclehookdefinition.md">InitialLifecycleHookDefinition</a>, ... ]</i>,
        "<a href="#instancerefresh" title="InstanceRefresh">InstanceRefresh</a>" : <i>[ <a href="instancerefreshdefinition.md">InstanceRefreshDefinition</a>, ... ]</i>,
        "<a href="#launchtemplate" title="LaunchTemplate">LaunchTemplate</a>" : <i>[ <a href="launchtemplatedefinition.md">LaunchTemplateDefinition</a>, ... ]</i>,
        "<a href="#mixedinstancespolicy" title="MixedInstancesPolicy">MixedInstancesPolicy</a>" : <i>[ <a href="mixedinstancespolicydefinition.md">MixedInstancesPolicyDefinition</a>, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tagdefinition.md">TagDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#warmpool" title="WarmPool">WarmPool</a>" : <i>[ <a href="warmpooldefinition.md">WarmPoolDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::AutoscalingGroup
Properties:
    <a href="#availabilityzones" title="AvailabilityZones">AvailabilityZones</a>: <i>
      - String</i>
    <a href="#capacityrebalance" title="CapacityRebalance">CapacityRebalance</a>: <i>Boolean</i>
    <a href="#defaultcooldown" title="DefaultCooldown">DefaultCooldown</a>: <i>Double</i>
    <a href="#desiredcapacity" title="DesiredCapacity">DesiredCapacity</a>: <i>Double</i>
    <a href="#enabledmetrics" title="EnabledMetrics">EnabledMetrics</a>: <i>
      - String</i>
    <a href="#forcedelete" title="ForceDelete">ForceDelete</a>: <i>Boolean</i>
    <a href="#forcedeletewarmpool" title="ForceDeleteWarmPool">ForceDeleteWarmPool</a>: <i>Boolean</i>
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
      - 
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#targetgrouparns" title="TargetGroupArns">TargetGroupArns</a>: <i>
      - String</i>
    <a href="#terminationpolicies" title="TerminationPolicies">TerminationPolicies</a>: <i>
      - String</i>
    <a href="#vpczoneidentifier" title="VpcZoneIdentifier">VpcZoneIdentifier</a>: <i>
      - String</i>
    <a href="#waitforcapacitytimeout" title="WaitForCapacityTimeout">WaitForCapacityTimeout</a>: <i>String</i>
    <a href="#waitforelbcapacity" title="WaitForElbCapacity">WaitForElbCapacity</a>: <i>Double</i>
    <a href="#initiallifecyclehook" title="InitialLifecycleHook">InitialLifecycleHook</a>: <i>
      - <a href="initiallifecyclehookdefinition.md">InitialLifecycleHookDefinition</a></i>
    <a href="#instancerefresh" title="InstanceRefresh">InstanceRefresh</a>: <i>
      - <a href="instancerefreshdefinition.md">InstanceRefreshDefinition</a></i>
    <a href="#launchtemplate" title="LaunchTemplate">LaunchTemplate</a>: <i>
      - <a href="launchtemplatedefinition.md">LaunchTemplateDefinition</a></i>
    <a href="#mixedinstancespolicy" title="MixedInstancesPolicy">MixedInstancesPolicy</a>: <i>
      - <a href="mixedinstancespolicydefinition.md">MixedInstancesPolicyDefinition</a></i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tagdefinition.md">TagDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#warmpool" title="WarmPool">WarmPool</a>: <i>
      - <a href="warmpooldefinition.md">WarmPoolDefinition</a></i>
</pre>

## Properties

#### AvailabilityZones

A list of one or more availability zones for the group. Used for EC2-Classic and default subnets when not specified with `vpc_zone_identifier` argument. Conflicts with `vpc_zone_identifier`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapacityRebalance

Indicates whether capacity rebalance is enabled. Otherwise, capacity rebalance is disabled.

_Required_: No

_Type_: Boolean

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

Allows deleting the Auto Scaling Group without waiting
for all instances in the pool to terminate.  You can force an Auto Scaling Group to delete
even if it's in the process of scaling a resource. Normally, Terraform
drains all the instances before deleting the group.  This bypasses that
behavior and potentially leaves resources dangling.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceDeleteWarmPool

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

The maximum size of the Auto Scaling Group.

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
this number of instances from this Auto Scaling Group to show up healthy in the
ELB only on creation. Updates will not wait on ELB instance number changes.
(See also [Waiting for Capacity](#waiting-for-capacity) below.).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinSize

The minimum size of the Auto Scaling Group.
(See also [Waiting for Capacity](#waiting-for-capacity) below.).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Auto Scaling Group. By default generated by Terraform. Conflicts with `name_prefix`.

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

A list of processes to suspend for the Auto Scaling Group. The allowed values are `Launch`, `Terminate`, `HealthCheck`, `ReplaceUnhealthy`, `AZRebalance`, `AlarmNotification`, `ScheduledActions`, `AddToLoadBalancer`.
Note that if you suspend either the `Launch` or `Terminate` process types, it can prevent your Auto Scaling Group from functioning properly.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of List of <a href="tagsdefinition.md">TagsDefinition</a>

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
for exactly this number of healthy instances from this Auto Scaling Group in
all attached load balancers on both create and update operations. (Takes
precedence over `min_elb_capacity` behavior.)
(See also [Waiting for Capacity](#waiting-for-capacity) below.).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitialLifecycleHook

_Required_: No

_Type_: List of <a href="initiallifecyclehookdefinition.md">InitialLifecycleHookDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceRefresh

_Required_: No

_Type_: List of <a href="instancerefreshdefinition.md">InstanceRefreshDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchTemplate

_Required_: No

_Type_: List of <a href="launchtemplatedefinition.md">LaunchTemplateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MixedInstancesPolicy

_Required_: No

_Type_: List of <a href="mixedinstancespolicydefinition.md">MixedInstancesPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tagdefinition.md">TagDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WarmPool

_Required_: No

_Type_: List of <a href="warmpooldefinition.md">WarmPoolDefinition</a>

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

