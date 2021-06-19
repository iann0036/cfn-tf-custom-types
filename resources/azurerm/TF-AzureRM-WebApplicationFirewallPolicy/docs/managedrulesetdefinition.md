# TF::AzureRM::WebApplicationFirewallPolicy ManagedRuleSetDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#version" title="Version">Version</a>" : <i>String</i>,
    "<a href="#rulegroupoverride" title="RuleGroupOverride">RuleGroupOverride</a>" : <i>[ <a href="rulegroupoverridedefinition.md">RuleGroupOverrideDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#version" title="Version">Version</a>: <i>String</i>
<a href="#rulegroupoverride" title="RuleGroupOverride">RuleGroupOverride</a>: <i>
      - <a href="rulegroupoverridedefinition.md">RuleGroupOverrideDefinition</a></i>
</pre>

## Properties

#### Type

The rule set type. Possible values: `Microsoft_BotManagerRuleSet` and `OWASP`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

The rule set version. Possible values: `0.1`, `1.0`, `2.2.9`, `3.0`, `3.1` and `3.2`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleGroupOverride

_Required_: No

_Type_: List of <a href="rulegroupoverridedefinition.md">RuleGroupOverrideDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

