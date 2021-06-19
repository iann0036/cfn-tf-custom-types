# TF::Dynatrace::CalculatedServiceMetric DimensionDefinitionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dimension" title="Dimension">Dimension</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#topx" title="TopX">TopX</a>" : <i>Double</i>,
    "<a href="#topxaggregation" title="TopXAggregation">TopXAggregation</a>" : <i>String</i>,
    "<a href="#topxdirection" title="TopXDirection">TopXDirection</a>" : <i>String</i>,
    "<a href="#unknowns" title="Unknowns">Unknowns</a>" : <i>String</i>,
    "<a href="#placeholders" title="Placeholders">Placeholders</a>" : <i>[ <a href="placeholdersdefinition.md">PlaceholdersDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dimension" title="Dimension">Dimension</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#topx" title="TopX">TopX</a>: <i>Double</i>
<a href="#topxaggregation" title="TopXAggregation">TopXAggregation</a>: <i>String</i>
<a href="#topxdirection" title="TopXDirection">TopXDirection</a>: <i>String</i>
<a href="#unknowns" title="Unknowns">Unknowns</a>: <i>String</i>
<a href="#placeholders" title="Placeholders">Placeholders</a>: <i>
      - <a href="placeholdersdefinition.md">PlaceholdersDefinition</a></i>
</pre>

## Properties

#### Dimension

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopX

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopXAggregation

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopXDirection

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unknowns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Placeholders

_Required_: No

_Type_: List of <a href="placeholdersdefinition.md">PlaceholdersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

