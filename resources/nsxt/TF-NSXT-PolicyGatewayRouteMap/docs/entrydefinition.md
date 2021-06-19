# TF::NSXT::PolicyGatewayRouteMap EntryDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#prefixlistmatches" title="PrefixListMatches">PrefixListMatches</a>" : <i>[ String, ... ]</i>,
    "<a href="#communitylistmatch" title="CommunityListMatch">CommunityListMatch</a>" : <i>[ <a href="communitylistmatchdefinition.md">CommunityListMatchDefinition</a>, ... ]</i>,
    "<a href="#set" title="Set">Set</a>" : <i>[ <a href="setdefinition.md">SetDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#prefixlistmatches" title="PrefixListMatches">PrefixListMatches</a>: <i>
      - String</i>
<a href="#communitylistmatch" title="CommunityListMatch">CommunityListMatch</a>: <i>
      - <a href="communitylistmatchdefinition.md">CommunityListMatchDefinition</a></i>
<a href="#set" title="Set">Set</a>: <i>
      - <a href="setdefinition.md">SetDefinition</a></i>
</pre>

## Properties

#### Action

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixListMatches

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommunityListMatch

_Required_: No

_Type_: List of <a href="communitylistmatchdefinition.md">CommunityListMatchDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Set

_Required_: No

_Type_: List of <a href="setdefinition.md">SetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

