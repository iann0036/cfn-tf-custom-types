# TF::AVI::Network RangeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#begin" title="Begin">Begin</a>" : <i>[ <a href="begindefinition.md">BeginDefinition</a>, ... ]</i>,
    "<a href="#end" title="End">End</a>" : <i>[ <a href="enddefinition.md">EndDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#begin" title="Begin">Begin</a>: <i>
      - <a href="begindefinition.md">BeginDefinition</a></i>
<a href="#end" title="End">End</a>: <i>
      - <a href="enddefinition.md">EndDefinition</a></i>
</pre>

## Properties

#### Begin

_Required_: No

_Type_: List of <a href="begindefinition.md">BeginDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### End

_Required_: No

_Type_: List of <a href="enddefinition.md">EndDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

