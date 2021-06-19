# TF::PagerDuty::Ruleset

[Rulesets](https://support.pagerduty.com/docs/rulesets) allow you to route events to an endpoint and create collections of event rules, which define sets of actions to take based on event content.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::PagerDuty::Ruleset",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#team" title="Team">Team</a>" : <i>[ <a href="teamdefinition.md">TeamDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::PagerDuty::Ruleset
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#team" title="Team">Team</a>: <i>
      - <a href="teamdefinition.md">TeamDefinition</a></i>
</pre>

## Properties

#### Name

Name of the ruleset.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Team

_Required_: No

_Type_: List of <a href="teamdefinition.md">TeamDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### RoutingKeys

Returns the <code>RoutingKeys</code> value.

#### Type

Returns the <code>Type</code> value.

