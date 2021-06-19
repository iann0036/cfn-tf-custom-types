# TF::AWS::NetworkfirewallRuleGroup StatefulRuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#header" title="Header">Header</a>" : <i>[ <a href="headerdefinition.md">HeaderDefinition</a>, ... ]</i>,
    "<a href="#ruleoption" title="RuleOption">RuleOption</a>" : <i>[ <a href="ruleoptiondefinition.md">RuleOptionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#header" title="Header">Header</a>: <i>
      - <a href="headerdefinition.md">HeaderDefinition</a></i>
<a href="#ruleoption" title="RuleOption">RuleOption</a>: <i>
      - <a href="ruleoptiondefinition.md">RuleOptionDefinition</a></i>
</pre>

## Properties

#### Action

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Header

_Required_: No

_Type_: List of <a href="headerdefinition.md">HeaderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleOption

_Required_: No

_Type_: List of <a href="ruleoptiondefinition.md">RuleOptionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

