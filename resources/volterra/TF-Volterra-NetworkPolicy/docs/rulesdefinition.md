# TF::Volterra::NetworkPolicy RulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#egressrules" title="EgressRules">EgressRules</a>" : <i>[ <a href="egressrulesdefinition.md">EgressRulesDefinition</a>, ... ]</i>,
    "<a href="#ingressrules" title="IngressRules">IngressRules</a>" : <i>[ <a href="ingressrulesdefinition.md">IngressRulesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#egressrules" title="EgressRules">EgressRules</a>: <i>
      - <a href="egressrulesdefinition.md">EgressRulesDefinition</a></i>
<a href="#ingressrules" title="IngressRules">IngressRules</a>: <i>
      - <a href="ingressrulesdefinition.md">IngressRulesDefinition</a></i>
</pre>

## Properties

#### EgressRules

_Required_: No

_Type_: List of <a href="egressrulesdefinition.md">EgressRulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IngressRules

_Required_: No

_Type_: List of <a href="ingressrulesdefinition.md">IngressRulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

