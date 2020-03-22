# Terraform::Panos::BgpExportRuleGroup

This resource allows you to add/update/delete BGP export rule groups.

This resource manages clusters of export rules in a virtual router,
enforcing both the contents of individual rules as well as their
ordering.  Rules are defined in a `rule` config block.

Although you cannot modify non-group export rules with this
resource, the `position_keyword` and `position_reference` parameters allow you
to reference some other export rule that already exists, using it as
a means to ensure some rough placement within the ruleset as a whole.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::BgpExportRuleGroup",
    "Properties" : {
        "<a href="#positionkeyword" title="PositionKeyword">PositionKeyword</a>" : <i>String</i>,
        "<a href="#positionreference" title="PositionReference">PositionReference</a>" : <i>String</i>,
        "<a href="#virtualrouter" title="VirtualRouter">VirtualRouter</a>" : <i>String</i>,
        "<a href="#rule" title="Rule">Rule</a>" : <i>[ <a href="rule.md">Rule</a>, ... ]</i>,
        "<a href="#matchaddressprefix" title="MatchAddressPrefix">MatchAddressPrefix</a>" : <i>[ <a href="matchaddressprefix.md">MatchAddressPrefix</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::BgpExportRuleGroup
Properties:
    <a href="#positionkeyword" title="PositionKeyword">PositionKeyword</a>: <i>String</i>
    <a href="#positionreference" title="PositionReference">PositionReference</a>: <i>String</i>
    <a href="#virtualrouter" title="VirtualRouter">VirtualRouter</a>: <i>String</i>
    <a href="#rule" title="Rule">Rule</a>: <i>
      - <a href="rule.md">Rule</a></i>
    <a href="#matchaddressprefix" title="MatchAddressPrefix">MatchAddressPrefix</a>: <i>
      - <a href="matchaddressprefix.md">MatchAddressPrefix</a></i>
</pre>

## Properties

#### PositionKeyword

A positioning keyword for this group.  This
can be `before`, `directly before`, `after`, `directly after`, `top`,
`bottom`, or left empty (the default) to have no particular placement.  This
param works in combination with the `position_reference` param.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PositionReference

Required if `position_keyword` is one of the
"above" or "below" variants, this is the name of a non-group rule to use
as a reference to place this group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualRouter

The virtual router to put the rule into.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No

_Type_: List of <a href="rule.md">Rule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchAddressPrefix

_Required_: No

_Type_: List of <a href="matchaddressprefix.md">MatchAddressPrefix</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

