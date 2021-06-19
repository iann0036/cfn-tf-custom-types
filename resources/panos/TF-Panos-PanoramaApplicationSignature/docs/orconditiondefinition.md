# TF::Panos::PanoramaApplicationSignature OrConditionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#equalto" title="EqualTo">EqualTo</a>" : <i>[ <a href="equaltodefinition.md">EqualToDefinition</a>, ... ]</i>,
    "<a href="#greaterthan" title="GreaterThan">GreaterThan</a>" : <i>[ <a href="greaterthandefinition.md">GreaterThanDefinition</a>, ... ]</i>,
    "<a href="#lessthan" title="LessThan">LessThan</a>" : <i>[ <a href="lessthandefinition.md">LessThanDefinition</a>, ... ]</i>,
    "<a href="#patternmatch" title="PatternMatch">PatternMatch</a>" : <i>[ <a href="patternmatchdefinition.md">PatternMatchDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#equalto" title="EqualTo">EqualTo</a>: <i>
      - <a href="equaltodefinition.md">EqualToDefinition</a></i>
<a href="#greaterthan" title="GreaterThan">GreaterThan</a>: <i>
      - <a href="greaterthandefinition.md">GreaterThanDefinition</a></i>
<a href="#lessthan" title="LessThan">LessThan</a>: <i>
      - <a href="lessthandefinition.md">LessThanDefinition</a></i>
<a href="#patternmatch" title="PatternMatch">PatternMatch</a>: <i>
      - <a href="patternmatchdefinition.md">PatternMatchDefinition</a></i>
</pre>

## Properties

#### EqualTo

_Required_: No

_Type_: List of <a href="equaltodefinition.md">EqualToDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GreaterThan

_Required_: No

_Type_: List of <a href="greaterthandefinition.md">GreaterThanDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LessThan

_Required_: No

_Type_: List of <a href="lessthandefinition.md">LessThanDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PatternMatch

_Required_: No

_Type_: List of <a href="patternmatchdefinition.md">PatternMatchDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

