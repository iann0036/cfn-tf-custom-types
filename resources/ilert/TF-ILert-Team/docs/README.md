# TF::ILert::Team

A [team](https://api.ilert.com/api-docs/#tag/Teams) helps you to manage access to resources and simplify the user interface to show only the incidents and resources relevant to a team.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ILert::Team",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#visibility" title="Visibility">Visibility</a>" : <i>String</i>,
        "<a href="#member" title="Member">Member</a>" : <i>[ <a href="memberdefinition.md">MemberDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ILert::Team
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#visibility" title="Visibility">Visibility</a>: <i>String</i>
    <a href="#member" title="Member">Member</a>: <i>
      - <a href="memberdefinition.md">MemberDefinition</a></i>
</pre>

## Properties

#### Name

The name of the team.
- `visibility` - (Optional) The visibility of the team. Allowed values are `PUBLIC` and `PRIVATE`. Default: `PUBLIC`.
- `member` - (Optional) One or more [member](#member-arguments) blocks.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Visibility

The visibility of the team. Allowed values are `PUBLIC` and `PRIVATE`. Default: `PUBLIC`.
- `member` - (Optional) One or more [member](#member-arguments) blocks.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Member

_Required_: No

_Type_: List of <a href="memberdefinition.md">MemberDefinition</a>

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

