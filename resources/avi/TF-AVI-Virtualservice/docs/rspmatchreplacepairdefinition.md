# TF::AVI::Virtualservice RspMatchReplacePairDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#matchstring" title="MatchString">MatchString</a>" : <i>String</i>,
    "<a href="#replacementstring" title="ReplacementString">ReplacementString</a>" : <i>[ <a href="replacementstringdefinition.md">ReplacementStringDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#matchstring" title="MatchString">MatchString</a>: <i>String</i>
<a href="#replacementstring" title="ReplacementString">ReplacementString</a>: <i>
      - <a href="replacementstringdefinition.md">ReplacementStringDefinition</a></i>
</pre>

## Properties

#### MatchString

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplacementString

_Required_: No

_Type_: List of <a href="replacementstringdefinition.md">ReplacementStringDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

