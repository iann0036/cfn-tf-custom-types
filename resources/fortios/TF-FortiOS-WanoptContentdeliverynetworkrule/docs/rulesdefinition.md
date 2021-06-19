# TF::FortiOS::WanoptContentdeliverynetworkrule RulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#matchmode" title="MatchMode">MatchMode</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#skiprulemode" title="SkipRuleMode">SkipRuleMode</a>" : <i>String</i>,
    "<a href="#contentid" title="ContentId">ContentId</a>" : <i>[ <a href="contentiddefinition.md">ContentIdDefinition</a>, ... ]</i>,
    "<a href="#matchentries" title="MatchEntries">MatchEntries</a>" : <i>[ <a href="matchentriesdefinition.md">MatchEntriesDefinition</a>, ... ]</i>,
    "<a href="#skipentries" title="SkipEntries">SkipEntries</a>" : <i>[ <a href="skipentriesdefinition.md">SkipEntriesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#matchmode" title="MatchMode">MatchMode</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#skiprulemode" title="SkipRuleMode">SkipRuleMode</a>: <i>String</i>
<a href="#contentid" title="ContentId">ContentId</a>: <i>
      - <a href="contentiddefinition.md">ContentIdDefinition</a></i>
<a href="#matchentries" title="MatchEntries">MatchEntries</a>: <i>
      - <a href="matchentriesdefinition.md">MatchEntriesDefinition</a></i>
<a href="#skipentries" title="SkipEntries">SkipEntries</a>: <i>
      - <a href="skipentriesdefinition.md">SkipEntriesDefinition</a></i>
</pre>

## Properties

#### MatchMode

Match criteria for collecting content ID. Valid values: `all`, `any`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

WAN optimization content delivery network rule name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipRuleMode

Skip mode when evaluating skip-rules. Valid values: `all`, `any`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentId

_Required_: No

_Type_: List of <a href="contentiddefinition.md">ContentIdDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchEntries

_Required_: No

_Type_: List of <a href="matchentriesdefinition.md">MatchEntriesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipEntries

_Required_: No

_Type_: List of <a href="skipentriesdefinition.md">SkipEntriesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

