# TF::GoogleBeta::GoogleDataprocAutoscalingPolicy BasicAlgorithmDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cooldownperiod" title="CooldownPeriod">CooldownPeriod</a>" : <i>String</i>,
    "<a href="#yarnconfig" title="YarnConfig">YarnConfig</a>" : <i>[ <a href="yarnconfigdefinition.md">YarnConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cooldownperiod" title="CooldownPeriod">CooldownPeriod</a>: <i>String</i>
<a href="#yarnconfig" title="YarnConfig">YarnConfig</a>: <i>
      - <a href="yarnconfigdefinition.md">YarnConfigDefinition</a></i>
</pre>

## Properties

#### CooldownPeriod

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### YarnConfig

_Required_: No

_Type_: List of <a href="yarnconfigdefinition.md">YarnConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

