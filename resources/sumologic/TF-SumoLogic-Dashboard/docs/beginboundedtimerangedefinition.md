# TF::SumoLogic::Dashboard BeginBoundedTimeRangeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#from" title="From">From</a>" : <i>[ <a href="fromdefinition.md">FromDefinition</a>, ... ]</i>,
    "<a href="#to" title="To">To</a>" : <i>[ <a href="todefinition.md">ToDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#from" title="From">From</a>: <i>
      - <a href="fromdefinition.md">FromDefinition</a></i>
<a href="#to" title="To">To</a>: <i>
      - <a href="todefinition.md">ToDefinition</a></i>
</pre>

## Properties

#### From

_Required_: No

_Type_: List of <a href="fromdefinition.md">FromDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### To

_Required_: No

_Type_: List of <a href="todefinition.md">ToDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

