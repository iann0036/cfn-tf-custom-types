# TF::AWS::AutoscalingPolicy PredictiveScalingConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#maxcapacitybreachbehavior" title="MaxCapacityBreachBehavior">MaxCapacityBreachBehavior</a>" : <i>String</i>,
    "<a href="#maxcapacitybuffer" title="MaxCapacityBuffer">MaxCapacityBuffer</a>" : <i>String</i>,
    "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
    "<a href="#schedulingbuffertime" title="SchedulingBufferTime">SchedulingBufferTime</a>" : <i>String</i>,
    "<a href="#metricspecification" title="MetricSpecification">MetricSpecification</a>" : <i>[ <a href="metricspecificationdefinition.md">MetricSpecificationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#maxcapacitybreachbehavior" title="MaxCapacityBreachBehavior">MaxCapacityBreachBehavior</a>: <i>String</i>
<a href="#maxcapacitybuffer" title="MaxCapacityBuffer">MaxCapacityBuffer</a>: <i>String</i>
<a href="#mode" title="Mode">Mode</a>: <i>String</i>
<a href="#schedulingbuffertime" title="SchedulingBufferTime">SchedulingBufferTime</a>: <i>String</i>
<a href="#metricspecification" title="MetricSpecification">MetricSpecification</a>: <i>
      - <a href="metricspecificationdefinition.md">MetricSpecificationDefinition</a></i>
</pre>

## Properties

#### MaxCapacityBreachBehavior

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxCapacityBuffer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchedulingBufferTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricSpecification

_Required_: No

_Type_: List of <a href="metricspecificationdefinition.md">MetricSpecificationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

