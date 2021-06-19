# TF::FortiOS::ReportLayout HeaderDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#style" title="Style">Style</a>" : <i>String</i>,
    "<a href="#headeritem" title="HeaderItem">HeaderItem</a>" : <i>[ <a href="headeritemdefinition.md">HeaderItemDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#style" title="Style">Style</a>: <i>String</i>
<a href="#headeritem" title="HeaderItem">HeaderItem</a>: <i>
      - <a href="headeritemdefinition.md">HeaderItemDefinition</a></i>
</pre>

## Properties

#### Style

Report header style.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderItem

_Required_: No

_Type_: List of <a href="headeritemdefinition.md">HeaderItemDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

