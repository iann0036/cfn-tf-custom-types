# Terraform::AzureRM::FrontdoorFirewallPolicy ManagedRule Override

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#rulegroupname" title="RuleGroupName">RuleGroupName</a>" : <i>String</i>,
    "<a href="#exclusion" title="Exclusion">Exclusion</a>" : <i>[ <a href="managedrule-override-exclusion.md">Exclusion</a>, ... ]</i>,
    "<a href="#rule" title="Rule">Rule</a>" : <i>[ <a href="managedrule-override-rule.md">Rule</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#rulegroupname" title="RuleGroupName">RuleGroupName</a>: <i>String</i>
<a href="#exclusion" title="Exclusion">Exclusion</a>: <i>
      - <a href="managedrule-override-exclusion.md">Exclusion</a></i>
<a href="#rule" title="Rule">Rule</a>: <i>
      - <a href="managedrule-override-rule.md">Rule</a></i>
</pre>

## Properties

#### RuleGroupName

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Exclusion

_Required_: No
_Type_: List of <a href="managedrule-override-exclusion.md">Exclusion</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No
_Type_: List of <a href="managedrule-override-rule.md">Rule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

