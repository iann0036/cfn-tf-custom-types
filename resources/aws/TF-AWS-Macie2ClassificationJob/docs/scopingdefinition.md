# TF::AWS::Macie2ClassificationJob ScopingDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#excludes" title="Excludes">Excludes</a>" : <i>[ <a href="excludesdefinition.md">ExcludesDefinition</a>, ... ]</i>,
    "<a href="#includes" title="Includes">Includes</a>" : <i>[ <a href="includesdefinition.md">IncludesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#excludes" title="Excludes">Excludes</a>: <i>
      - <a href="excludesdefinition.md">ExcludesDefinition</a></i>
<a href="#includes" title="Includes">Includes</a>: <i>
      - <a href="includesdefinition.md">IncludesDefinition</a></i>
</pre>

## Properties

#### Excludes

_Required_: No

_Type_: List of <a href="excludesdefinition.md">ExcludesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Includes

_Required_: No

_Type_: List of <a href="includesdefinition.md">IncludesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

