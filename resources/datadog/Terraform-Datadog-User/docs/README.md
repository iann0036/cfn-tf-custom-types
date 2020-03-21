# Terraform::Datadog::User

Provides a Datadog user resource. This can be used to create and manage Datadog users.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Datadog::User",
    "Properties" : {
        "<a href="#accessrole" title="AccessRole">AccessRole</a>" : <i>String</i>,
        "<a href="#disabled" title="Disabled">Disabled</a>" : <i>Boolean</i>,
        "<a href="#email" title="Email">Email</a>" : <i>String</i>,
        "<a href="#handle" title="Handle">Handle</a>" : <i>String</i>,
        "<a href="#isadmin" title="IsAdmin">IsAdmin</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Datadog::User
Properties:
    <a href="#accessrole" title="AccessRole">AccessRole</a>: <i>String</i>
    <a href="#disabled" title="Disabled">Disabled</a>: <i>Boolean</i>
    <a href="#email" title="Email">Email</a>: <i>String</i>
    <a href="#handle" title="Handle">Handle</a>: <i>String</i>
    <a href="#isadmin" title="IsAdmin">IsAdmin</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
</pre>

## Properties

#### AccessRole

Role description for user. Can be `st` (standard user), `adm` (admin user) or `ro` (read-only user).  Default is `st`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disabled

Whether the user is disabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

Email address for user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Handle

The user handle, must be a valid email.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsAdmin

(Optional) Whether the user is an administrator. **Warning**: the corresponding query parameter is ignored by the Datadog API, thus the argument would always trigger an execution plan.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name for user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

Role description for user. **Warning**: the corresponding query parameter is ignored by the Datadog API, thus the argument would always trigger an execution plan.

_Required_: No

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

#### Verified

Returns the <code>Verified</code> value.

