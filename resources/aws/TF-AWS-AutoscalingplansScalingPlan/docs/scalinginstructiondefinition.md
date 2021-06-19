# TF::AWS::AutoscalingplansScalingPlan ScalingInstructionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#disabledynamicscaling" title="DisableDynamicScaling">DisableDynamicScaling</a>" : <i>Boolean</i>,
    "<a href="#maxcapacity" title="MaxCapacity">MaxCapacity</a>" : <i>Double</i>,
    "<a href="#mincapacity" title="MinCapacity">MinCapacity</a>" : <i>Double</i>,
    "<a href="#predictivescalingmaxcapacitybehavior" title="PredictiveScalingMaxCapacityBehavior">PredictiveScalingMaxCapacityBehavior</a>" : <i>String</i>,
    "<a href="#predictivescalingmaxcapacitybuffer" title="PredictiveScalingMaxCapacityBuffer">PredictiveScalingMaxCapacityBuffer</a>" : <i>Double</i>,
    "<a href="#predictivescalingmode" title="PredictiveScalingMode">PredictiveScalingMode</a>" : <i>String</i>,
    "<a href="#resourceid" title="ResourceId">ResourceId</a>" : <i>String</i>,
    "<a href="#scalabledimension" title="ScalableDimension">ScalableDimension</a>" : <i>String</i>,
    "<a href="#scalingpolicyupdatebehavior" title="ScalingPolicyUpdateBehavior">ScalingPolicyUpdateBehavior</a>" : <i>String</i>,
    "<a href="#scheduledactionbuffertime" title="ScheduledActionBufferTime">ScheduledActionBufferTime</a>" : <i>Double</i>,
    "<a href="#servicenamespace" title="ServiceNamespace">ServiceNamespace</a>" : <i>String</i>,
    "<a href="#customizedloadmetricspecification" title="CustomizedLoadMetricSpecification">CustomizedLoadMetricSpecification</a>" : <i>[ <a href="customizedloadmetricspecificationdefinition.md">CustomizedLoadMetricSpecificationDefinition</a>, ... ]</i>,
    "<a href="#predefinedloadmetricspecification" title="PredefinedLoadMetricSpecification">PredefinedLoadMetricSpecification</a>" : <i>[ <a href="predefinedloadmetricspecificationdefinition.md">PredefinedLoadMetricSpecificationDefinition</a>, ... ]</i>,
    "<a href="#targettrackingconfiguration" title="TargetTrackingConfiguration">TargetTrackingConfiguration</a>" : <i>[ <a href="targettrackingconfigurationdefinition.md">TargetTrackingConfigurationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#disabledynamicscaling" title="DisableDynamicScaling">DisableDynamicScaling</a>: <i>Boolean</i>
<a href="#maxcapacity" title="MaxCapacity">MaxCapacity</a>: <i>Double</i>
<a href="#mincapacity" title="MinCapacity">MinCapacity</a>: <i>Double</i>
<a href="#predictivescalingmaxcapacitybehavior" title="PredictiveScalingMaxCapacityBehavior">PredictiveScalingMaxCapacityBehavior</a>: <i>String</i>
<a href="#predictivescalingmaxcapacitybuffer" title="PredictiveScalingMaxCapacityBuffer">PredictiveScalingMaxCapacityBuffer</a>: <i>Double</i>
<a href="#predictivescalingmode" title="PredictiveScalingMode">PredictiveScalingMode</a>: <i>String</i>
<a href="#resourceid" title="ResourceId">ResourceId</a>: <i>String</i>
<a href="#scalabledimension" title="ScalableDimension">ScalableDimension</a>: <i>String</i>
<a href="#scalingpolicyupdatebehavior" title="ScalingPolicyUpdateBehavior">ScalingPolicyUpdateBehavior</a>: <i>String</i>
<a href="#scheduledactionbuffertime" title="ScheduledActionBufferTime">ScheduledActionBufferTime</a>: <i>Double</i>
<a href="#servicenamespace" title="ServiceNamespace">ServiceNamespace</a>: <i>String</i>
<a href="#customizedloadmetricspecification" title="CustomizedLoadMetricSpecification">CustomizedLoadMetricSpecification</a>: <i>
      - <a href="customizedloadmetricspecificationdefinition.md">CustomizedLoadMetricSpecificationDefinition</a></i>
<a href="#predefinedloadmetricspecification" title="PredefinedLoadMetricSpecification">PredefinedLoadMetricSpecification</a>: <i>
      - <a href="predefinedloadmetricspecificationdefinition.md">PredefinedLoadMetricSpecificationDefinition</a></i>
<a href="#targettrackingconfiguration" title="TargetTrackingConfiguration">TargetTrackingConfiguration</a>: <i>
      - <a href="targettrackingconfigurationdefinition.md">TargetTrackingConfigurationDefinition</a></i>
</pre>

## Properties

#### DisableDynamicScaling

Boolean controlling whether dynamic scaling by AWS Auto Scaling is disabled. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxCapacity

The maximum capacity of the resource. The exception to this upper limit is if you specify a non-default setting for `predictive_scaling_max_capacity_behavior`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinCapacity

The minimum capacity of the resource.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PredictiveScalingMaxCapacityBehavior

Defines the behavior that should be applied if the forecast capacity approaches or exceeds the maximum capacity specified for the resource.
Valid values: `SetForecastCapacityToMaxCapacity`, `SetMaxCapacityAboveForecastCapacity`, `SetMaxCapacityToForecastCapacity`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PredictiveScalingMaxCapacityBuffer

The size of the capacity buffer to use when the forecast capacity is close to or exceeds the maximum capacity.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PredictiveScalingMode

The predictive scaling mode. Valid values: `ForecastAndScale`, `ForecastOnly`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceId

The ID of the resource. This string consists of the resource type and unique identifier.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalableDimension

The scalable dimension associated with the resource. Valid values: `autoscaling:autoScalingGroup:DesiredCapacity`, `dynamodb:index:ReadCapacityUnits`, `dynamodb:index:WriteCapacityUnits`, `dynamodb:table:ReadCapacityUnits`, `dynamodb:table:WriteCapacityUnits`, `ecs:service:DesiredCount`, `ec2:spot-fleet-request:TargetCapacity`, `rds:cluster:ReadReplicaCount`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingPolicyUpdateBehavior

Controls whether a resource's externally created scaling policies are kept or replaced. Valid values: `KeepExternalPolicies`, `ReplaceExternalPolicies`. Defaults to `KeepExternalPolicies`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduledActionBufferTime

The amount of time, in seconds, to buffer the run time of scheduled scaling actions when scaling out.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceNamespace

The namespace of the AWS service. Valid values: `autoscaling`, `dynamodb`, `ecs`, `ec2`, `rds`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomizedLoadMetricSpecification

_Required_: No

_Type_: List of <a href="customizedloadmetricspecificationdefinition.md">CustomizedLoadMetricSpecificationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PredefinedLoadMetricSpecification

_Required_: No

_Type_: List of <a href="predefinedloadmetricspecificationdefinition.md">PredefinedLoadMetricSpecificationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetTrackingConfiguration

_Required_: No

_Type_: List of <a href="targettrackingconfigurationdefinition.md">TargetTrackingConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

