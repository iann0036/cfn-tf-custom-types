# TF::AzureRM::WebApplicationFirewallPolicy RuleGroupOverrideDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#disabledrules" title="DisabledRules">DisabledRules</a>" : <i>[ String, ... ]</i>,
    "<a href="#rulegroupname" title="RuleGroupName">RuleGroupName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#disabledrules" title="DisabledRules">DisabledRules</a>: <i>
      - String</i>
<a href="#rulegroupname" title="RuleGroupName">RuleGroupName</a>: <i>String</i>
</pre>

## Properties

#### DisabledRules

One or more Rule ID's.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleGroupName

The name of the Rule Group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

