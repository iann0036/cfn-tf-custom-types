# TF::AVI::Wafpolicy CrsOverridesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enable" title="Enable">Enable</a>" : <i>Boolean</i>,
    "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#excludelist" title="ExcludeList">ExcludeList</a>" : <i>[ <a href="excludelistdefinition.md">ExcludeListDefinition</a>, ... ]</i>,
    "<a href="#ruleoverrides" title="RuleOverrides">RuleOverrides</a>" : <i>[ <a href="ruleoverridesdefinition.md">RuleOverridesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enable" title="Enable">Enable</a>: <i>Boolean</i>
<a href="#mode" title="Mode">Mode</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#excludelist" title="ExcludeList">ExcludeList</a>: <i>
      - <a href="excludelistdefinition.md">ExcludeListDefinition</a></i>
<a href="#ruleoverrides" title="RuleOverrides">RuleOverrides</a>: <i>
      - <a href="ruleoverridesdefinition.md">RuleOverridesDefinition</a></i>
</pre>

## Properties

#### Enable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeList

_Required_: No

_Type_: List of <a href="excludelistdefinition.md">ExcludeListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleOverrides

_Required_: No

_Type_: List of <a href="ruleoverridesdefinition.md">RuleOverridesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

