# TF::AzureRM::SecurityCenterAutomation SourceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#eventsource" title="EventSource">EventSource</a>" : <i>String</i>,
    "<a href="#ruleset" title="RuleSet">RuleSet</a>" : <i>[ <a href="rulesetdefinition.md">RuleSetDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#eventsource" title="EventSource">EventSource</a>: <i>String</i>
<a href="#ruleset" title="RuleSet">RuleSet</a>: <i>
      - <a href="rulesetdefinition.md">RuleSetDefinition</a></i>
</pre>

## Properties

#### EventSource

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleSet

_Required_: No

_Type_: List of <a href="rulesetdefinition.md">RuleSetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

