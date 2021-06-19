# TF::Heroku::TeamMember

A [Heroku Team Member](https://devcenter.heroku.com/articles/platform-api-reference#team-member) receives access to everything owned by the Team.

To create a Heroku Team, use the [New Team](https://dashboard.heroku.com/teams/new) feature of Heroku Dashboard. For Heroku Enterprise accounts, new Teams may be created within the account by users with the right permissions.

A Heroku "team" was originally called an "organization", and that is still the identifier used elsewhere in this provider. For [`heroku_app`](app.html) & [`heroku_space`](space.html) resources, set the Heroku Team name as the "organization".

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Heroku::TeamMember",
    "Properties" : {
        "<a href="#email" title="Email">Email</a>" : <i>String</i>,
        "<a href="#federated" title="Federated">Federated</a>" : <i>Boolean</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>,
        "<a href="#team" title="Team">Team</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Heroku::TeamMember
Properties:
    <a href="#email" title="Email">Email</a>: <i>String</i>
    <a href="#federated" title="Federated">Federated</a>: <i>Boolean</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
    <a href="#team" title="Team">Team</a>: <i>String</i>
</pre>

## Properties

#### Email

Email address of the member.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Federated

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

The role to assign the member. See [the API docs](https://devcenter.heroku.com/articles/platform-api-reference#team-member) for available options.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Team

The name of the Heroku Team.

_Required_: Yes

_Type_: String

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

