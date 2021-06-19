# TF::CheckPoint::ManagementExceptionGroup AppliedThreatRulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#layer" title="Layer">Layer</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#position" title="Position">Position</a>" : <i>[ <a href="positiondefinition.md">PositionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#layer" title="Layer">Layer</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#position" title="Position">Position</a>: <i>
      - <a href="positiondefinition.md">PositionDefinition</a></i>
</pre>

## Properties

#### Layer

The layer of the threat rule to which the group is to be attached.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the threat rule to which the group is to be attached.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Position

Position in the rulebase.

_Required_: Yes

_Type_: List of <a href="positiondefinition.md">PositionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

