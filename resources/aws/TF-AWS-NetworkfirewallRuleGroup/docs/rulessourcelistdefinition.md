# TF::AWS::NetworkfirewallRuleGroup RulesSourceListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#generatedrulestype" title="GeneratedRulesType">GeneratedRulesType</a>" : <i>String</i>,
    "<a href="#targettypes" title="TargetTypes">TargetTypes</a>" : <i>[ String, ... ]</i>,
    "<a href="#targets" title="Targets">Targets</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#generatedrulestype" title="GeneratedRulesType">GeneratedRulesType</a>: <i>String</i>
<a href="#targettypes" title="TargetTypes">TargetTypes</a>: <i>
      - String</i>
<a href="#targets" title="Targets">Targets</a>: <i>
      - String</i>
</pre>

## Properties

#### GeneratedRulesType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetTypes

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Targets

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

