# TF::GoogleBeta::GoogleGameServicesGameServerConfig ScalingConfigsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#fleetautoscalerspec" title="FleetAutoscalerSpec">FleetAutoscalerSpec</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#schedules" title="Schedules">Schedules</a>" : <i>[ <a href="schedulesdefinition.md">SchedulesDefinition</a>, ... ]</i>,
    "<a href="#selectors" title="Selectors">Selectors</a>" : <i>[ <a href="selectorsdefinition.md">SelectorsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#fleetautoscalerspec" title="FleetAutoscalerSpec">FleetAutoscalerSpec</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#schedules" title="Schedules">Schedules</a>: <i>
      - <a href="schedulesdefinition.md">SchedulesDefinition</a></i>
<a href="#selectors" title="Selectors">Selectors</a>: <i>
      - <a href="selectorsdefinition.md">SelectorsDefinition</a></i>
</pre>

## Properties

#### FleetAutoscalerSpec

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedules

_Required_: No

_Type_: List of <a href="schedulesdefinition.md">SchedulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Selectors

_Required_: No

_Type_: List of <a href="selectorsdefinition.md">SelectorsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

