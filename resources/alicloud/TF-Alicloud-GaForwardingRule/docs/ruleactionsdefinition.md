# TF::Alicloud::GaForwardingRule RuleActionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#order" title="Order">Order</a>" : <i>Double</i>,
    "<a href="#ruleactiontype" title="RuleActionType">RuleActionType</a>" : <i>String</i>,
    "<a href="#forwardgroupconfig" title="ForwardGroupConfig">ForwardGroupConfig</a>" : <i>[ <a href="forwardgroupconfigdefinition.md">ForwardGroupConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#order" title="Order">Order</a>: <i>Double</i>
<a href="#ruleactiontype" title="RuleActionType">RuleActionType</a>: <i>String</i>
<a href="#forwardgroupconfig" title="ForwardGroupConfig">ForwardGroupConfig</a>: <i>
      - <a href="forwardgroupconfigdefinition.md">ForwardGroupConfigDefinition</a></i>
</pre>

## Properties

#### Order

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleActionType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardGroupConfig

_Required_: No

_Type_: List of <a href="forwardgroupconfigdefinition.md">ForwardGroupConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

