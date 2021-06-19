# TF::FortiOS::WanoptContentdeliverynetworkrule SkipEntriesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#target" title="Target">Target</a>" : <i>String</i>,
    "<a href="#pattern" title="Pattern">Pattern</a>" : <i>[ <a href="patterndefinition.md">PatternDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#target" title="Target">Target</a>: <i>String</i>
<a href="#pattern" title="Pattern">Pattern</a>: <i>
      - <a href="patterndefinition.md">PatternDefinition</a></i>
</pre>

## Properties

#### Id

Rule ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Target

Option in HTTP header or URL parameter to match. Valid values: `path`, `parameter`, `referrer`, `youtube-map`, `youtube-id`, `youku-id`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pattern

_Required_: No

_Type_: List of <a href="patterndefinition.md">PatternDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

