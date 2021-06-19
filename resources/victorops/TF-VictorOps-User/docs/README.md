# TF::VictorOps::User

A [user](https://portal.victorops.com/public/api-docs.html#/Users) is an individual within a VictorOps account.

Make sure the optional field 'replacement_user' is set to a default user_name to facilitate deleting users using TF. Alternatively, you can set the `VO_REPLACEMENT_USERNAME` env variable to the default username to replace all users when removed.

Note: We no longer allow creation of `admin` users through the Terraform (or the public API), the `is_admin` field value is ignored.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VictorOps::User",
    "Properties" : {
        "<a href="#email" title="Email">Email</a>" : <i>String</i>,
        "<a href="#expirationhours" title="ExpirationHours">ExpirationHours</a>" : <i>Double</i>,
        "<a href="#firstname" title="FirstName">FirstName</a>" : <i>String</i>,
        "<a href="#isadmin" title="IsAdmin">IsAdmin</a>" : <i>Boolean</i>,
        "<a href="#lastname" title="LastName">LastName</a>" : <i>String</i>,
        "<a href="#replacementuser" title="ReplacementUser">ReplacementUser</a>" : <i>String</i>,
        "<a href="#username" title="UserName">UserName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::VictorOps::User
Properties:
    <a href="#email" title="Email">Email</a>: <i>String</i>
    <a href="#expirationhours" title="ExpirationHours">ExpirationHours</a>: <i>Double</i>
    <a href="#firstname" title="FirstName">FirstName</a>: <i>String</i>
    <a href="#isadmin" title="IsAdmin">IsAdmin</a>: <i>Boolean</i>
    <a href="#lastname" title="LastName">LastName</a>: <i>String</i>
    <a href="#replacementuser" title="ReplacementUser">ReplacementUser</a>: <i>String</i>
    <a href="#username" title="UserName">UserName</a>: <i>String</i>
</pre>

## Properties

#### Email

The user's email address.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpirationHours

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirstName

The first name of the user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsAdmin

DEPRECATED - the field and its value will be ignored if specified.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LastName

The last name of the user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplacementUser

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserName

The username for this user.

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

#### DefaultEmailContactId

Returns the <code>DefaultEmailContactId</code> value.

#### Id

Returns the <code>Id</code> value.

