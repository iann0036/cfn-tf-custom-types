# TF::Dynatrace::CalculatedServiceMetric NumberRequestAttributeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#matchonchildcalls" title="MatchOnChildCalls">MatchOnChildCalls</a>" : <i>Boolean</i>,
    "<a href="#operator" title="Operator">Operator</a>" : <i>String</i>,
    "<a href="#requestattribute" title="RequestAttribute">RequestAttribute</a>" : <i>String</i>,
    "<a href="#unknowns" title="Unknowns">Unknowns</a>" : <i>String</i>,
    "<a href="#value" title="Value">Value</a>" : <i>Double</i>,
    "<a href="#values" title="Values">Values</a>" : <i>[ Double, ... ]</i>,
    "<a href="#source" title="Source">Source</a>" : <i>[ <a href="sourcedefinition.md">SourceDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#matchonchildcalls" title="MatchOnChildCalls">MatchOnChildCalls</a>: <i>Boolean</i>
<a href="#operator" title="Operator">Operator</a>: <i>String</i>
<a href="#requestattribute" title="RequestAttribute">RequestAttribute</a>: <i>String</i>
<a href="#unknowns" title="Unknowns">Unknowns</a>: <i>String</i>
<a href="#value" title="Value">Value</a>: <i>Double</i>
<a href="#values" title="Values">Values</a>: <i>
      - Double</i>
<a href="#source" title="Source">Source</a>: <i>
      - <a href="sourcedefinition.md">SourceDefinition</a></i>
</pre>

## Properties

#### MatchOnChildCalls

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Operator

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestAttribute

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unknowns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Values

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: No

_Type_: List of <a href="sourcedefinition.md">SourceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

