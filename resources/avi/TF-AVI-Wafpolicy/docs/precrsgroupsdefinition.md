# TF::AVI::Wafpolicy PreCrsGroupsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enable" title="Enable">Enable</a>" : <i>Boolean</i>,
    "<a href="#index" title="Index">Index</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#excludelist" title="ExcludeList">ExcludeList</a>" : <i>[ <a href="excludelistdefinition.md">ExcludeListDefinition</a>, ... ]</i>,
    "<a href="#rules" title="Rules">Rules</a>" : <i>[ <a href="rulesdefinition.md">RulesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enable" title="Enable">Enable</a>: <i>Boolean</i>
<a href="#index" title="Index">Index</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#excludelist" title="ExcludeList">ExcludeList</a>: <i>
      - <a href="excludelistdefinition.md">ExcludeListDefinition</a></i>
<a href="#rules" title="Rules">Rules</a>: <i>
      - <a href="rulesdefinition.md">RulesDefinition</a></i>
</pre>

## Properties

#### Enable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Index

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeList

_Required_: No

_Type_: List of <a href="excludelistdefinition.md">ExcludeListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rules

_Required_: No

_Type_: List of <a href="rulesdefinition.md">RulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

