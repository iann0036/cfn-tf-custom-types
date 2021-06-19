# TF::AVI::L4policyset PortDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#matchcriteria" title="MatchCriteria">MatchCriteria</a>" : <i>String</i>,
    "<a href="#ports" title="Ports">Ports</a>" : <i>[ Double, ... ]</i>,
    "<a href="#portranges" title="PortRanges">PortRanges</a>" : <i>[ <a href="portrangesdefinition.md">PortRangesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#matchcriteria" title="MatchCriteria">MatchCriteria</a>: <i>String</i>
<a href="#ports" title="Ports">Ports</a>: <i>
      - Double</i>
<a href="#portranges" title="PortRanges">PortRanges</a>: <i>
      - <a href="portrangesdefinition.md">PortRangesDefinition</a></i>
</pre>

## Properties

#### MatchCriteria

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ports

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortRanges

_Required_: No

_Type_: List of <a href="portrangesdefinition.md">PortRangesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

