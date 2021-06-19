# TF::AVI::Ssopolicy AccessTokenDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#tokenname" title="TokenName">TokenName</a>" : <i>String</i>,
    "<a href="#matches" title="Matches">Matches</a>" : <i>[ <a href="matchesdefinition.md">MatchesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#tokenname" title="TokenName">TokenName</a>: <i>String</i>
<a href="#matches" title="Matches">Matches</a>: <i>
      - <a href="matchesdefinition.md">MatchesDefinition</a></i>
</pre>

## Properties

#### TokenName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Matches

_Required_: No

_Type_: List of <a href="matchesdefinition.md">MatchesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

