# Terraform::Heroku::SpaceAppAccess

Provides a resource for managing permissions for the entire Private Space. Members with the admin role will always have full permissions in the Private Space, so using this resource on an admin will have no effect. The provided email must already be a member of the Heroku Team. Currently the only supported permission is `create_apps`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Heroku::SpaceAppAccess",
    "Properties" : {
        "<a href="#email" title="Email">Email</a>" : <i>String</i>,
        "<a href="#permissions" title="Permissions">Permissions</a>" : <i>[ String, ... ]</i>,
        "<a href="#space" title="Space">Space</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Heroku::SpaceAppAccess
Properties:
    <a href="#email" title="Email">Email</a>: <i>String</i>
    <a href="#permissions" title="Permissions">Permissions</a>: <i>
      - String</i>
    <a href="#space" title="Space">Space</a>: <i>String</i>
</pre>

## Properties

#### Email

The email of the existing Heroku Team member.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Permissions

The permissions to grant the team member for the Private Space. Currently `create_apps` is the only supported permission. If not provided the member will have no permissions to the space. Members with admin role will always have `create_apps` permissions, which cannot be removed.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Space

The name of the Private Space.

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

