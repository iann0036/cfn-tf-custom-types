# TF::AVI::Wafpolicy ApplicationSignaturesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#providerref" title="ProviderRef">ProviderRef</a>" : <i>String</i>,
    "<a href="#selectedapplications" title="SelectedApplications">SelectedApplications</a>" : <i>[ String, ... ]</i>,
    "<a href="#resolvedrules" title="ResolvedRules">ResolvedRules</a>" : <i>[ <a href="resolvedrulesdefinition.md">ResolvedRulesDefinition</a>, ... ]</i>,
    "<a href="#ruleoverrides" title="RuleOverrides">RuleOverrides</a>" : <i>[ <a href="ruleoverridesdefinition.md">RuleOverridesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#providerref" title="ProviderRef">ProviderRef</a>: <i>String</i>
<a href="#selectedapplications" title="SelectedApplications">SelectedApplications</a>: <i>
      - String</i>
<a href="#resolvedrules" title="ResolvedRules">ResolvedRules</a>: <i>
      - <a href="resolvedrulesdefinition.md">ResolvedRulesDefinition</a></i>
<a href="#ruleoverrides" title="RuleOverrides">RuleOverrides</a>: <i>
      - <a href="ruleoverridesdefinition.md">RuleOverridesDefinition</a></i>
</pre>

## Properties

#### ProviderRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SelectedApplications

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResolvedRules

_Required_: No

_Type_: List of <a href="resolvedrulesdefinition.md">ResolvedRulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleOverrides

_Required_: No

_Type_: List of <a href="ruleoverridesdefinition.md">RuleOverridesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

