# TF::AVI::Analyticsprofile SensitiveLogProfileDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#headerfieldrules" title="HeaderFieldRules">HeaderFieldRules</a>" : <i>[ <a href="headerfieldrulesdefinition.md">HeaderFieldRulesDefinition</a>, ... ]</i>,
    "<a href="#waffieldrules" title="WafFieldRules">WafFieldRules</a>" : <i>[ <a href="waffieldrulesdefinition.md">WafFieldRulesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#headerfieldrules" title="HeaderFieldRules">HeaderFieldRules</a>: <i>
      - <a href="headerfieldrulesdefinition.md">HeaderFieldRulesDefinition</a></i>
<a href="#waffieldrules" title="WafFieldRules">WafFieldRules</a>: <i>
      - <a href="waffieldrulesdefinition.md">WafFieldRulesDefinition</a></i>
</pre>

## Properties

#### HeaderFieldRules

_Required_: No

_Type_: List of <a href="headerfieldrulesdefinition.md">HeaderFieldRulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WafFieldRules

_Required_: No

_Type_: List of <a href="waffieldrulesdefinition.md">WafFieldRulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

