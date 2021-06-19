# TF::AVI::Wafpolicy RuleOverridesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enable" title="Enable">Enable</a>" : <i>Boolean</i>,
    "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
    "<a href="#ruleid" title="RuleId">RuleId</a>" : <i>String</i>,
    "<a href="#excludelist" title="ExcludeList">ExcludeList</a>" : <i>[ <a href="excludelistdefinition.md">ExcludeListDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enable" title="Enable">Enable</a>: <i>Boolean</i>
<a href="#mode" title="Mode">Mode</a>: <i>String</i>
<a href="#ruleid" title="RuleId">RuleId</a>: <i>String</i>
<a href="#excludelist" title="ExcludeList">ExcludeList</a>: <i>
      - <a href="excludelistdefinition.md">ExcludeListDefinition</a></i>
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

#### RuleId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeList

_Required_: No

_Type_: List of <a href="excludelistdefinition.md">ExcludeListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

