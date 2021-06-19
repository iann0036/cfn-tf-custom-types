# TF::AVI::Natpolicy ProtocolDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#matchcriteria" title="MatchCriteria">MatchCriteria</a>" : <i>String</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>[ <a href="protocoldefinition.md">ProtocolDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#matchcriteria" title="MatchCriteria">MatchCriteria</a>: <i>String</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>
      - <a href="protocoldefinition.md">ProtocolDefinition</a></i>
</pre>

## Properties

#### MatchCriteria

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: Yes

_Type_: List of <a href="protocoldefinition.md">ProtocolDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

