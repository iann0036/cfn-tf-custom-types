# Terraform::AzureRM::FrontdoorFirewallPolicy Override Rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#ruleid" title="RuleId">RuleId</a>" : <i>String</i>,
    "<a href="#exclusion" title="Exclusion">Exclusion</a>" : <i>[ <a href="override-rule-exclusion.md">Exclusion</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#ruleid" title="RuleId">RuleId</a>: <i>String</i>
<a href="#exclusion" title="Exclusion">Exclusion</a>: <i>
      - <a href="override-rule-exclusion.md">Exclusion</a></i>
</pre>

## Properties

#### Action

The action to be applied when the rule matches. Possible values are `Allow`, `Block`, `Log`, or `Redirect`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Is the managed rule override enabled or disabled. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleId

Identifier for the managed rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Exclusion

_Required_: No

_Type_: List of <a href="override-rule-exclusion.md">Exclusion</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

