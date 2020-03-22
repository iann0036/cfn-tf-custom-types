# Terraform::Heroku::TeamCollaborator

A [Heroku Team Collaborator](https://devcenter.heroku.com/articles/platform-api-reference#team-app-collaborator) receives access to a specific Team-owned app.

To create a Heroku Team, use the [New Team](https://dashboard.heroku.com/teams/new) feature of Heroku Dashboard. For Heroku Enterprise accounts, new Teams may be created within the account by users with the right permissions.

A Heroku "team" was originally called an "organization", and that is still the identifier used elsewhere in this provider. For [`heroku_app`](app.html) & [`heroku_space`](space.html) resources, set the Heroku Team name as the "organization".

~> **NOTE:** This resource only works for Team-owned apps

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Heroku::TeamCollaborator",
    "Properties" : {
        "<a href="#app" title="App">App</a>" : <i>String</i>,
        "<a href="#email" title="Email">Email</a>" : <i>String</i>,
        "<a href="#permissions" title="Permissions">Permissions</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Heroku::TeamCollaborator
Properties:
    <a href="#app" title="App">App</a>: <i>String</i>
    <a href="#email" title="Email">Email</a>: <i>String</i>
    <a href="#permissions" title="Permissions">Permissions</a>: <i>
      - String</i>
</pre>

## Properties

#### App

The name of the team app that the team collaborator will be added to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

Email address of the team collaborator.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Permissions

List of permissions that will be granted to the team collaborator. The order in which
individual permissions are set here does not matter. Please [visit this link](https://devcenter.heroku.com/articles/app-permissions)
for more information on available permissions.

_Required_: Yes

_Type_: List of String

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

