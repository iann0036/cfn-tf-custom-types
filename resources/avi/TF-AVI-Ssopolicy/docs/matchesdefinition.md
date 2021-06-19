# TF::AVI::Ssopolicy MatchesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#boolmatch" title="BoolMatch">BoolMatch</a>" : <i>Boolean</i>,
    "<a href="#intmatch" title="IntMatch">IntMatch</a>" : <i>Double</i>,
    "<a href="#ismandatory" title="IsMandatory">IsMandatory</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#validate" title="Validate">Validate</a>" : <i>Boolean</i>,
    "<a href="#stringmatch" title="StringMatch">StringMatch</a>" : <i>[ <a href="stringmatchdefinition.md">StringMatchDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#boolmatch" title="BoolMatch">BoolMatch</a>: <i>Boolean</i>
<a href="#intmatch" title="IntMatch">IntMatch</a>: <i>Double</i>
<a href="#ismandatory" title="IsMandatory">IsMandatory</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#validate" title="Validate">Validate</a>: <i>Boolean</i>
<a href="#stringmatch" title="StringMatch">StringMatch</a>: <i>
      - <a href="stringmatchdefinition.md">StringMatchDefinition</a></i>
</pre>

## Properties

#### BoolMatch

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntMatch

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsMandatory

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Validate

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StringMatch

_Required_: No

_Type_: List of <a href="stringmatchdefinition.md">StringMatchDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

