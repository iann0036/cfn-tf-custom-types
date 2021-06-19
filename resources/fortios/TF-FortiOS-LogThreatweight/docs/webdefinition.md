# TF::FortiOS::LogThreatweight WebDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#category" title="Category">Category</a>" : <i>Double</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#level" title="Level">Level</a>" : <i>[ <a href="leveldefinition.md">LevelDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#category" title="Category">Category</a>: <i>Double</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#level" title="Level">Level</a>: <i>
      - <a href="leveldefinition.md">LevelDefinition</a></i>
</pre>

## Properties

#### Category

Threat weight score for web category filtering matches.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

Entry ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Level

_Required_: No

_Type_: List of <a href="leveldefinition.md">LevelDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

