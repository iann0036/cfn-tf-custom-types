# TF::Volterra::VirtualHost WafTypeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#waf" title="Waf">Waf</a>" : <i>[ <a href="wafdefinition.md">WafDefinition</a>, ... ]</i>,
    "<a href="#wafrules" title="WafRules">WafRules</a>" : <i>[ <a href="wafrulesdefinition.md">WafRulesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#waf" title="Waf">Waf</a>: <i>
      - <a href="wafdefinition.md">WafDefinition</a></i>
<a href="#wafrules" title="WafRules">WafRules</a>: <i>
      - <a href="wafrulesdefinition.md">WafRulesDefinition</a></i>
</pre>

## Properties

#### Waf

_Required_: No

_Type_: List of <a href="wafdefinition.md">WafDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WafRules

_Required_: No

_Type_: List of <a href="wafrulesdefinition.md">WafRulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

