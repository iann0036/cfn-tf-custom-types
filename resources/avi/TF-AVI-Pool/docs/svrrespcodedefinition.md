# TF::AVI::Pool SvrRespCodeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#codes" title="Codes">Codes</a>" : <i>[ Double, ... ]</i>,
    "<a href="#respcodeblock" title="RespCodeBlock">RespCodeBlock</a>" : <i>[ String, ... ]</i>,
    "<a href="#ranges" title="Ranges">Ranges</a>" : <i>[ <a href="rangesdefinition.md">RangesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#codes" title="Codes">Codes</a>: <i>
      - Double</i>
<a href="#respcodeblock" title="RespCodeBlock">RespCodeBlock</a>: <i>
      - String</i>
<a href="#ranges" title="Ranges">Ranges</a>: <i>
      - <a href="rangesdefinition.md">RangesDefinition</a></i>
</pre>

## Properties

#### Codes

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RespCodeBlock

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ranges

_Required_: No

_Type_: List of <a href="rangesdefinition.md">RangesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

