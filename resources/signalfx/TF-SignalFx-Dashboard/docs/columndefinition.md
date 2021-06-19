# TF::SignalFx::Dashboard ColumnDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#chartids" title="ChartIds">ChartIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#column" title="Column">Column</a>" : <i>[ <a href="columndefinition.md">ColumnDefinition</a>, ... ]</i>,
    "<a href="#height" title="Height">Height</a>" : <i>Double</i>,
    "<a href="#width" title="Width">Width</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#chartids" title="ChartIds">ChartIds</a>: <i>
      - String</i>
<a href="#column" title="Column">Column</a>: <i>
      - <a href="columndefinition.md">ColumnDefinition</a></i>
<a href="#height" title="Height">Height</a>: <i>Double</i>
<a href="#width" title="Width">Width</a>: <i>Double</i>
</pre>

## Properties

#### ChartIds

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Column

_Required_: No

_Type_: List of <a href="columndefinition.md">ColumnDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Height

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Width

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

