# TF::PagerDuty::EscalationPolicy RuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#escalationdelayinminutes" title="EscalationDelayInMinutes">EscalationDelayInMinutes</a>" : <i>Double</i>,
    "<a href="#target" title="Target">Target</a>" : <i>[ <a href="targetdefinition.md">TargetDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#escalationdelayinminutes" title="EscalationDelayInMinutes">EscalationDelayInMinutes</a>: <i>Double</i>
<a href="#target" title="Target">Target</a>: <i>
      - <a href="targetdefinition.md">TargetDefinition</a></i>
</pre>

## Properties

#### EscalationDelayInMinutes

The number of minutes before an unacknowledged incident escalates away from this rule.
* `targets` - (Required) A target block. Target blocks documented below.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Target

_Required_: No

_Type_: List of <a href="targetdefinition.md">TargetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

