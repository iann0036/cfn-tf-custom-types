# TF::AVI::Httppolicyset RulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enable" title="Enable">Enable</a>" : <i>Boolean</i>,
    "<a href="#index" title="Index">Index</a>" : <i>Double</i>,
    "<a href="#log" title="Log">Log</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#action" title="Action">Action</a>" : <i>[ <a href="actiondefinition.md">ActionDefinition</a>, ... ]</i>,
    "<a href="#match" title="Match">Match</a>" : <i>[ <a href="matchdefinition.md">MatchDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enable" title="Enable">Enable</a>: <i>Boolean</i>
<a href="#index" title="Index">Index</a>: <i>Double</i>
<a href="#log" title="Log">Log</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#action" title="Action">Action</a>: <i>
      - <a href="actiondefinition.md">ActionDefinition</a></i>
<a href="#match" title="Match">Match</a>: <i>
      - <a href="matchdefinition.md">MatchDefinition</a></i>
</pre>

## Properties

#### Enable

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Index

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Log

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Action

_Required_: No

_Type_: List of <a href="actiondefinition.md">ActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Match

_Required_: No

_Type_: List of <a href="matchdefinition.md">MatchDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

