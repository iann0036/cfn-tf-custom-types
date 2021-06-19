# TF::Google::DataLossPreventionInspectTemplate RulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#exclusionrule" title="ExclusionRule">ExclusionRule</a>" : <i>[ <a href="exclusionruledefinition.md">ExclusionRuleDefinition</a>, ... ]</i>,
    "<a href="#hotwordrule" title="HotwordRule">HotwordRule</a>" : <i>[ <a href="hotwordruledefinition.md">HotwordRuleDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#exclusionrule" title="ExclusionRule">ExclusionRule</a>: <i>
      - <a href="exclusionruledefinition.md">ExclusionRuleDefinition</a></i>
<a href="#hotwordrule" title="HotwordRule">HotwordRule</a>: <i>
      - <a href="hotwordruledefinition.md">HotwordRuleDefinition</a></i>
</pre>

## Properties

#### ExclusionRule

_Required_: No

_Type_: List of <a href="exclusionruledefinition.md">ExclusionRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HotwordRule

_Required_: No

_Type_: List of <a href="hotwordruledefinition.md">HotwordRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

