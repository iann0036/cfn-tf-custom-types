# TF::Rancher2::Cluster MonitoringDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#nodeselector" title="NodeSelector">NodeSelector</a>" : <i>[ <a href="nodeselectordefinition.md">NodeSelectorDefinition</a>, ... ]</i>,
    "<a href="#options" title="Options">Options</a>" : <i>[ <a href="optionsdefinition.md">OptionsDefinition</a>, ... ]</i>,
    "<a href="#provider" title="Provider">Provider</a>" : <i>String</i>,
    "<a href="#replicas" title="Replicas">Replicas</a>" : <i>Double</i>,
    "<a href="#updatestrategy" title="UpdateStrategy">UpdateStrategy</a>" : <i>[ <a href="updatestrategydefinition.md">UpdateStrategyDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#nodeselector" title="NodeSelector">NodeSelector</a>: <i>
      - <a href="nodeselectordefinition.md">NodeSelectorDefinition</a></i>
<a href="#options" title="Options">Options</a>: <i>
      - <a href="optionsdefinition.md">OptionsDefinition</a></i>
<a href="#provider" title="Provider">Provider</a>: <i>String</i>
<a href="#replicas" title="Replicas">Replicas</a>: <i>Double</i>
<a href="#updatestrategy" title="UpdateStrategy">UpdateStrategy</a>: <i>
      - <a href="updatestrategydefinition.md">UpdateStrategyDefinition</a></i>
</pre>

## Properties

#### NodeSelector

_Required_: No

_Type_: List of <a href="nodeselectordefinition.md">NodeSelectorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Options

_Required_: No

_Type_: List of <a href="optionsdefinition.md">OptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Provider

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Replicas

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateStrategy

_Required_: No

_Type_: List of <a href="updatestrategydefinition.md">UpdateStrategyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

