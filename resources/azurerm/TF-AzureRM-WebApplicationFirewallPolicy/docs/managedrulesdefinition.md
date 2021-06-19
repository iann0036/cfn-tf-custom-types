# TF::AzureRM::WebApplicationFirewallPolicy ManagedRulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#exclusion" title="Exclusion">Exclusion</a>" : <i>[ <a href="exclusiondefinition.md">ExclusionDefinition</a>, ... ]</i>,
    "<a href="#managedruleset" title="ManagedRuleSet">ManagedRuleSet</a>" : <i>[ <a href="managedrulesetdefinition.md">ManagedRuleSetDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#exclusion" title="Exclusion">Exclusion</a>: <i>
      - <a href="exclusiondefinition.md">ExclusionDefinition</a></i>
<a href="#managedruleset" title="ManagedRuleSet">ManagedRuleSet</a>: <i>
      - <a href="managedrulesetdefinition.md">ManagedRuleSetDefinition</a></i>
</pre>

## Properties

#### Exclusion

_Required_: No

_Type_: List of <a href="exclusiondefinition.md">ExclusionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedRuleSet

_Required_: No

_Type_: List of <a href="managedrulesetdefinition.md">ManagedRuleSetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

