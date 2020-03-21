# Terraform::AWS::WafWebAcl Rules

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
    "<a href="#ruleid" title="RuleId">RuleId</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#action" title="Action">Action</a>" : <i>[ &lt;a href=&#34;rules-action.md&#34;&gt;Action&lt;/a&gt;, ... ]</i>,
    "<a href="#overrideaction" title="OverrideAction">OverrideAction</a>" : <i>[ &lt;a href=&#34;rules-overrideaction.md&#34;&gt;OverrideAction&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#priority" title="Priority">Priority</a>: <i>Double</i>
<a href="#ruleid" title="RuleId">RuleId</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#action" title="Action">Action</a>: <i>
      - &lt;a href=&#34;rules-action.md&#34;&gt;Action&lt;/a&gt;</i>
<a href="#overrideaction" title="OverrideAction">OverrideAction</a>: <i>
      - &lt;a href=&#34;rules-overrideaction.md&#34;&gt;OverrideAction&lt;/a&gt;</i>
</pre>

## Properties

#### Priority

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleId

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Action

_Required_: No
_Type_: List of &lt;a href=&#34;rules-action.md&#34;&gt;Action&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideAction

_Required_: No
_Type_: List of &lt;a href=&#34;rules-overrideaction.md&#34;&gt;OverrideAction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

