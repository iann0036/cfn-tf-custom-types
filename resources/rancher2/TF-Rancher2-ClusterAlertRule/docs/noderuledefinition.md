# TF::Rancher2::ClusterAlertRule NodeRuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#condition" title="Condition">Condition</a>" : <i>String</i>,
    "<a href="#cputhreshold" title="CpuThreshold">CpuThreshold</a>" : <i>Double</i>,
    "<a href="#memthreshold" title="MemThreshold">MemThreshold</a>" : <i>Double</i>,
    "<a href="#nodeid" title="NodeId">NodeId</a>" : <i>String</i>,
    "<a href="#selector" title="Selector">Selector</a>" : <i>[ <a href="selectordefinition.md">SelectorDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#condition" title="Condition">Condition</a>: <i>String</i>
<a href="#cputhreshold" title="CpuThreshold">CpuThreshold</a>: <i>Double</i>
<a href="#memthreshold" title="MemThreshold">MemThreshold</a>: <i>Double</i>
<a href="#nodeid" title="NodeId">NodeId</a>: <i>String</i>
<a href="#selector" title="Selector">Selector</a>: <i>
      - <a href="selectordefinition.md">SelectorDefinition</a></i>
</pre>

## Properties

#### Condition

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Selector

_Required_: No

_Type_: List of <a href="selectordefinition.md">SelectorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

