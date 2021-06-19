# TF::AzureRM::FrontdoorFirewallPolicy OverrideDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#rulegroupname" title="RuleGroupName">RuleGroupName</a>" : <i>String</i>,
    "<a href="#exclusion" title="Exclusion">Exclusion</a>" : <i>[ <a href="exclusiondefinition.md">ExclusionDefinition</a>, ... ]</i>,
    "<a href="#rule" title="Rule">Rule</a>" : <i>[ <a href="ruledefinition.md">RuleDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#rulegroupname" title="RuleGroupName">RuleGroupName</a>: <i>String</i>
<a href="#exclusion" title="Exclusion">Exclusion</a>: <i>
      - <a href="exclusiondefinition.md">ExclusionDefinition</a></i>
<a href="#rule" title="Rule">Rule</a>: <i>
      - <a href="ruledefinition.md">RuleDefinition</a></i>
</pre>

## Properties

#### RuleGroupName

The managed rule group to override.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Exclusion

_Required_: No

_Type_: List of <a href="exclusiondefinition.md">ExclusionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No

_Type_: List of <a href="ruledefinition.md">RuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

