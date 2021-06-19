# TF::AWS::AppmeshGatewayRoute GrpcRouteDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>[ <a href="actiondefinition.md">ActionDefinition</a>, ... ]</i>,
    "<a href="#match" title="Match">Match</a>" : <i>[ <a href="matchdefinition.md">MatchDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>
      - <a href="actiondefinition.md">ActionDefinition</a></i>
<a href="#match" title="Match">Match</a>: <i>
      - <a href="matchdefinition.md">MatchDefinition</a></i>
</pre>

## Properties

#### Action

_Required_: No

_Type_: List of <a href="actiondefinition.md">ActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Match

_Required_: No

_Type_: List of <a href="matchdefinition.md">MatchDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

